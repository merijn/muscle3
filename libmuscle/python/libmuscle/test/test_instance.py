import sys
from typing import Generator, List
from unittest.mock import MagicMock, patch

import pytest
from ymmsl import Conduit, Operator, Reference, Settings

from libmuscle.communicator import _ClosePort, Message
from libmuscle.instance import Instance
from libmuscle.configuration_store import ConfigurationStore


@pytest.fixture
def sys_argv_manager() -> Generator[None, None, None]:
    old_argv = sys.argv
    sys.argv = sys.argv + ['--muscle-manager=localhost:9000']
    yield None
    sys.argv = old_argv


@pytest.fixture
def log_file_in_tmpdir(tmpdir) -> Generator[None, None, None]:
    old_argv = sys.argv
    sys.argv = sys.argv + ['--muscle-log-file={}'.format(tmpdir)]
    yield None
    sys.argv = old_argv


@pytest.fixture
def sys_argv_index() -> Generator[None, None, None]:
    old_argv = sys.argv
    sys.argv = ['', '--muscle-index=13,42']
    yield
    sys.argv = old_argv


@pytest.fixture
def instance():
    with patch('libmuscle.instance.MMPClient') as mmp_client, \
         patch('libmuscle.instance.Communicator') as comm_type:
        communicator = MagicMock()
        settings = Settings()
        settings['test1'] = 12
        msg = Message(0.0, 1.0, 'message', settings)
        communicator.receive_message.return_value = msg
        comm_type.return_value = communicator

        mmp_client_object = MagicMock()
        mmp_client_object.request_peers.return_value = (None, None, None)
        mmp_client.return_value = mmp_client_object

        instance = Instance('test_instance', {
            Operator.F_INIT: ['in', 'not_connected'],
            Operator.O_F: ['out']})
        instance._f_init_cache = dict()
        instance._f_init_cache[('in', None)] = msg
        yield instance


@pytest.fixture
def instance2():
    with patch('libmuscle.instance.MMPClient') as mmp_client, \
         patch('libmuscle.instance.Communicator') as comm_type:
        mmp_client_object = MagicMock()
        mmp_client_object.request_peers.return_value = (None, None, None)
        mmp_client.return_value = mmp_client_object
        instance = Instance('test_instance', {
            Operator.F_INIT: ['in[]'],
            Operator.O_F: ['out']})
        yield instance


def test_create_instance(
        sys_argv_index, log_file_in_tmpdir, sys_argv_manager):
    with patch('libmuscle.instance.MMPClient') as mmp_client, \
         patch('libmuscle.instance.Communicator') as comm_type:
        mmp_client_object = MagicMock()
        mmp_client_object.request_peers.return_value = (None, None, None)
        mmp_client.return_value = mmp_client_object
        ports = {
            Operator.F_INIT: ['in'],
            Operator.O_F: ['out']}
        instance = Instance('test_instance', ports)
        assert instance._name == Reference('test_instance')
        assert instance._index == [13, 42]
        assert instance._declared_ports == ports
        assert isinstance(instance._configuration_store, ConfigurationStore)
        assert len(instance._configuration_store.base) == 0
        assert len(instance._configuration_store.overlay) == 0
        mmp_client.assert_called_once_with('localhost:9000')
        assert mmp_client_object._register.called_with()
        assert mmp_client_object._connect.called_with()
        comm_type.assert_called_with(Reference('test_instance'), [13, 42],
                                     ports, instance._profiler)
        assert instance._communicator == comm_type.return_value
        assert isinstance(instance._configuration_store, ConfigurationStore)
        assert len(instance._configuration_store.base) == 0


def test_extract_manager_location(sys_argv_manager) -> None:
    assert (Instance._Instance__extract_manager_location() ==
            'localhost:9000')


def test_get_parameter_value(instance):
    ref = Reference
    settings = Settings()
    settings[ref('test1')] = 'test'
    settings[ref('test2')] = 12
    settings[ref('test3')] = 27.1
    settings[ref('test4')] = True
    settings[ref('test5')] = [2.3, 5.6]
    settings[ref('test6')] = [[1.0, 2.0], [3.0, 4.0]]
    instance._configuration_store.base = settings

    assert instance.get_parameter_value('test1') == 'test'
    assert instance.get_parameter_value('test2') == 12
    assert instance.get_parameter_value('test3') == 27.1
    assert instance.get_parameter_value('test4') is True
    assert instance.get_parameter_value('test5') == [2.3, 5.6]
    assert instance.get_parameter_value('test6') == [
            [1.0, 2.0], [3.0, 4.0]]

    assert instance.get_parameter_value('test1', 'str') == 'test'
    assert instance.get_parameter_value('test2', 'int') == 12
    assert instance.get_parameter_value('test3', 'float') == 27.1
    assert instance.get_parameter_value('test4', 'bool') is True
    assert (instance.get_parameter_value('test5', '[float]') ==
            [2.3, 5.6])
    assert (instance.get_parameter_value('test6', '[[float]]') ==
            [[1.0, 2.0], [3.0, 4.0]])

    with pytest.raises(KeyError):
        instance.get_parameter_value('testx')

    with pytest.raises(TypeError):
        instance.get_parameter_value('test1', 'int')
    with pytest.raises(TypeError):
        instance.get_parameter_value('test6', '[float]')
    with pytest.raises(TypeError):
        instance.get_parameter_value('test5', '[[float]]')
    with pytest.raises(ValueError):
        instance.get_parameter_value('test2', 'nonexistenttype')


def test_list_ports(instance):
    ports = instance.list_ports()
    assert instance._communicator.list_ports.called_with()
    assert ports == instance._communicator.list_ports.return_value


def test_is_vector_port(instance):
    instance._communicator.get_port.return_value.is_vector = MagicMock(
            return_value=True)
    is_vector = instance.is_vector_port('out_port')
    assert is_vector is True
    assert instance._communicator.get_port.called_with('out_port')


def test_send_message(instance, message):
    instance.send_message('out', message, 1)
    assert instance._communicator.send_message.called_with(
            'out', message, 1)


def test_send_message_invalid_port(instance, message):
    instance._communicator.port_exists.return_value = False
    with pytest.raises(ValueError):
        instance.send_message('does_not_exist', message, 1)


def test_receive_message(instance):
    instance._communicator.get_port.return_value = MagicMock(
            operator=Operator.F_INIT)
    msg = instance.receive_message('in')
    assert msg.timestamp == 0.0
    assert msg.next_timestamp == 1.0
    assert instance._communicator.receive_message.called_with(
            'in', None)
    assert msg.data == 'message'

    with pytest.raises(RuntimeError):
        instance.receive_message('in')


def test_receive_message_default(instance):
    instance._communicator.port_exists.return_value = True
    port = instance._communicator.get_port.return_value
    port.operator = Operator.F_INIT
    port.is_connected.return_value = False
    instance.receive_message('not_connected', 1, 'testing')
    assert instance._communicator.receive_message.called_with(
            'not_connected', 1, 'testing')
    with pytest.raises(RuntimeError):
        instance.receive_message('not_connected', 1)


def test_receive_message_invalid_port(instance):
    instance._communicator.port_exists.return_value = False
    with pytest.raises(ValueError):
        instance.receive_message('does_not_exist', 1)


def test_receive_message_with_parameters(instance):
    msg = instance.receive_message_with_parameters('in', 1)
    assert (instance._communicator.receive_message
            .called_with('in', 1))
    assert msg.timestamp == 0.0
    assert msg.next_timestamp == 1.0
    assert msg.data == 'message'
    assert msg.settings['test1'] == 12


def test_receive_message_with_parameters_default(instance):
    instance.receive_message_with_parameters('not_connected', 1, 'testing')
    assert instance._communicator.receive_message.called_with(
            'not_connected', 1, 'testing')


def test_receive_parallel_universe(instance) -> None:
    instance._configuration_store.overlay['test2'] = 'test'
    with pytest.raises(RuntimeError):
        instance.receive_message('in')


def test_reuse_instance_receive_overlay(instance):
    instance._configuration_store.overlay = Settings()
    test_base_settings = Settings()
    test_base_settings['test1'] = 24
    test_base_settings['test2'] = [1.3, 2.0]
    test_overlay = Settings()
    test_overlay['test2'] = 'abc'
    recv = instance._communicator.receive_message
    recv.return_value = Message(0.0, None, test_overlay, test_base_settings)
    instance.reuse_instance()
    assert instance._communicator.receive_message.called_with(
        'muscle_parameters_in')
    assert len(instance._configuration_store.overlay) == 2
    assert instance._configuration_store.overlay['test1'] == 24
    assert instance._configuration_store.overlay['test2'] == 'abc'


def test_reuse_instance_closed_port(instance):
    def receive_message(port_name, slot=None, default=None):
        if port_name == 'muscle_parameters_in':
            return Message(0.0, None, Settings(), Settings())
        elif port_name == 'in':
            return Message(0.0, None, _ClosePort(), Settings())
        assert False    # pragma: no cover

    def get_port(port_name):
        port = MagicMock()
        port.is_vector.return_value = False
        if port_name == 'not_connected':
            port.is_connected.return_value = False
        else:
            port.is_connected.return_value = True
        return port

    instance._communicator.receive_message = receive_message
    instance._communicator.list_ports.return_value = {
            Operator.F_INIT: ['in', 'not_connected'],
            Operator.O_F: ['out']}
    instance._communicator.get_port = get_port

    do_reuse = instance.reuse_instance()
    assert do_reuse is False


def test_reuse_instance_vector_port(instance2):
    def receive_message(port_name, slot=None, default=None):
        if port_name == 'muscle_parameters_in':
            return Message(0.0, None, Settings(), Settings())
        elif port_name == 'in':
            data = 'test {}'.format(slot)
            return Message(0.0, None, data, Settings())
        assert False    # pragma: no cover

    instance2._communicator.receive_message = receive_message
    instance2._communicator.list_ports.return_value = {
            Operator.F_INIT: ['in'],
            Operator.O_F: ['out']}

    port = MagicMock()
    port.is_vector.return_value = True
    port.is_connected.return_value = True
    port.get_length.return_value = 10
    instance2._communicator.get_port.return_value = port

    do_reuse = instance2.reuse_instance()
    assert do_reuse is True

    msg = instance2.receive_message('in', 5)
    assert msg.timestamp == 0.0
    assert msg.next_timestamp is None
    assert msg.data == 'test 5'


def test_reuse_instance_no_f_init_ports(instance):
    instance._communicator.receive_message.return_value = Message(
            0.0, None, Settings(), Settings())
    instance._communicator.list_ports.return_value = {}
    instance._communicator.parameters_in_connected.return_value = False
    do_reuse = instance.reuse_instance()
    assert do_reuse is True
    do_reuse = instance.reuse_instance()
    assert do_reuse is False


def test_reuse_instance_miswired(instance):
    with pytest.raises(RuntimeError):
        instance.reuse_instance()
