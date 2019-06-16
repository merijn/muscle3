import pytest
from ymmsl import (ComputeElement, Conduit, Identifier, Model,
                   Reference, YmmslDocument)

from libmuscle.configuration import Configuration

from muscle_manager.instance_registry import InstanceRegistry
from muscle_manager.logger import Logger
from muscle_manager.mmp_server import MMPServicer
from muscle_manager.topology_store import TopologyStore


@pytest.fixture
def logger():
    return Logger()


@pytest.fixture
def configuration():
    return Configuration()


@pytest.fixture
def instance_registry():
    expected_instances = ['macro']
    for i in range(10):
        expected_instances.append('micro[{}]'.format(i))
    return InstanceRegistry(expected_instances)


@pytest.fixture
def topology_store() -> TopologyStore:
    ymmsl = YmmslDocument(
            'v0.1',
            Model(
                'test_model',
                [
                    ComputeElement('macro', 'macro_implementation'),
                    ComputeElement(
                        'micro', 'micro_implementation', [10, 10])],
                [
                    Conduit('macro.out', 'micro.in'),
                    Conduit('micro.out', 'macro.in')
                ]))

    return TopologyStore(ymmsl)


@pytest.fixture
def mmp_servicer(logger, configuration, instance_registry, topology_store):
    return MMPServicer(logger, configuration, instance_registry,
                       topology_store)


@pytest.fixture
def loaded_instance_registry(instance_registry):
    instance_registry.add(Reference('macro'), ['direct:macro'], [])
    for j in range(10):
        for i in range(10):
            name = Reference('micro') + j + i
            location = 'direct:{}'.format(name)
            instance_registry.add(name, [location], [])
    return instance_registry


@pytest.fixture
def registered_mmp_servicer(logger, configuration, loaded_instance_registry,
                            topology_store):
    return MMPServicer(logger, configuration, loaded_instance_registry,
                       topology_store)


@pytest.fixture
def topology_store2() -> TopologyStore:
    ymmsl = YmmslDocument(
            'v0.1',
            Model(
                'test_model',
                [
                    ComputeElement('macro', 'macro_implementation'),
                    ComputeElement('meso', 'meso_implementation', [5]),
                    ComputeElement('micro', 'micro_implementation', [5, 10])
                ],
                [
                    Conduit('macro.out', 'meso.in'),
                    Conduit('meso.out', 'micro.in'),
                    Conduit('micro.out', 'meso.in'),
                    Conduit('meso.out', 'macro.in')
                ]))

    return TopologyStore(ymmsl)


@pytest.fixture
def loaded_instance_registry2():
    expected_instances = ['macro']
    for i in range(5):
        expected_instances.append('meso[{}]'.format(i))
    for j in range(5):
        for i in range(10):
            expected_instances.append('micro[{}][{}]'.format(j, i))
    instance_registry = InstanceRegistry(expected_instances)

    instance_registry.add(Reference('macro'), ['direct:macro'], [])

    for j in range(5):
        name = Reference('meso') + j
        location = 'direct:{}'.format(name)
        instance_registry.add(name, [location], [])

    for j in range(5):
        for i in range(10):
            name = Reference('micro') + j + i
            location = 'direct:{}'.format(name)
            instance_registry.add(name, [location], [])
    return instance_registry


@pytest.fixture
def registered_mmp_servicer2(
        logger, configuration, loaded_instance_registry2, topology_store2):
    return MMPServicer(logger, configuration, loaded_instance_registry2,
                       topology_store2)
