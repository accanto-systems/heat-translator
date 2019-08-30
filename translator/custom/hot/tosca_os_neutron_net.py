from translator.custom.hot.os_hot_resource import OSHotResource

TARGET_CLASS_NAME = 'OSNeutronNet'
HOT_TYPE = 'OS::Neutron::Net'

class OSNeutronNet(OSHotResource):
    '''Translate TOSCA node type os.nodes.neutron.Net'''

    toscatype = 'os.nodes.neutron.Net'

    def __init__(self, nodetemplate, csar_dir=None):
        super(OSNeutronNet, self).__init__(HOT_TYPE, nodetemplate, csar_dir=csar_dir)
        # Never set. This is an attribute the tosca_network_port expects on an Network, although it can be None.
        # So we have an empty var here so this Network can be used in place of a tosca.nodes.network.Network type
        self.existing_resource_id = None
