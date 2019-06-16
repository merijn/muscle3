from collections import OrderedDict

import pytest
from ymmsl import (ComputeElement, Conduit, Model, Operator, Reference,
                   Settings, YmmslDocument)

from libmuscle.communicator import Message
from libmuscle.instance import Instance
from muscle_manager.muscle_manager import run_simulation


def qmc(instance_id: str):
    """qMC implementation.
    """
    instance = Instance(instance_id, {Operator.O_F: ['parameters_out[]']})

    while instance.reuse_instance():
        # o_f
        settings0 = Settings({'test2': 14.4})

        assert instance.is_connected('parameters_out')
        assert instance.is_vector_port('parameters_out')
        assert not instance.is_resizable('parameters_out')
        length = instance.get_port_length('parameters_out')
        assert length == 10
        for slot in range(length):
            instance.send_message('parameters_out',
                                  Message(0.0, None, settings0), slot)


def macro(instance_id: str):
    """Macro model implementation.
    """
    instance = Instance(instance_id, {
            Operator.O_I: ['out'], Operator.S: ['in']})

    while instance.reuse_instance():
        # f_init
        assert instance.get_parameter_value('test2') == 14.4
        # o_i
        instance.send_message('out', Message(0.0, 10.0, 'testing'))
        # s/b
        msg = instance.receive_message('in')
        assert msg.data == 'testing back'


def micro(instance_id: str):
    """Micro model implementation.
    """
    instance = Instance(instance_id, {
            Operator.F_INIT: ['in'], Operator.O_F: ['out']})

    assert instance.get_parameter_value('test2') == 13.3
    while instance.reuse_instance():
        # f_init
        assert instance.get_parameter_value('test2', 'float') == 14.4
        msg = instance.receive_message('in')
        assert msg.data == 'testing'

        # with pytest.raises(RuntimeError):
        #     instance.receive_message_with_parameters('in')

        # o_f
        instance.send_message('out', Message(0.1, None, 'testing back'))


def explicit_micro(instance_id: str):
    """Micro model implementation with explicit parameters.

    Receives overlay parameters explicitly, rather than having MUSCLE
    handle them.
    """
    instance = Instance(instance_id, {
            Operator.F_INIT: ['in'], Operator.O_F: ['out']})

    while instance.reuse_instance(False):
        # f_init
        assert instance.get_parameter_value('test2', 'float') == 13.3
        msg = instance.receive_message_with_parameters('in')
        assert msg.data == 'testing'
        assert msg.settings['test2'] == 14.4
        assert instance.get_parameter_value('test2') == 13.3

        # o_f
        instance.send_message(
                'out', Message(0.1, None, 'testing back', msg.settings))


def test_parameter_overlays(log_file_in_tmpdir):
    """A positive all-up test of parameter overlays.
    """
    elements = [
            ComputeElement('qmc', 'qmc'),
            ComputeElement('macro', 'macro', [10]),
            ComputeElement('micro', 'micro', [10])]

    conduits = [
                Conduit('qmc.parameters_out', 'macro.muscle_parameters_in'),
                Conduit('macro.out', 'micro.in'),
                Conduit('micro.out', 'macro.in')]

    model = Model('test_model', elements, conduits)

    settings = Settings(OrderedDict([
                ('test1', 13),
                ('test2', 13.3),
                ('test3', 'testing'),
                ('test4', True),
                ('test5', [2.3, 5.6]),
                ('test6', [[1.0, 2.0], [3.0, 1.0]])]))

    experiment = YmmslDocument('v0.1', model, settings)

    submodels = {'qmc': qmc}
    for i in range(9):
        submodels['macro[{}]'.format(i)] = macro
        submodels['micro[{}]'.format(i)] = micro
    submodels['macro[9]'] = macro
    submodels['micro[9]'] = explicit_micro
    run_simulation(experiment, submodels)
