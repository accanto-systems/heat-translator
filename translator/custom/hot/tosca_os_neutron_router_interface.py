from translator.custom.hot.os_hot_resource import OSHotResource

TARGET_CLASS_NAME = 'OSNeutronRouterInterface'
HOT_TYPE = 'OS::Neutron::RouterInterface'

class OSNeutronRouterInterface(OSHotResource):
    '''Translate TOSCA node type os.nodes.neutron.RouterInterface'''

    toscatype = 'os.nodes.neutron.RouterInterface'

    def __init__(self, nodetemplate, csar_dir=None):
        super(OSNeutronRouterInterface, self).__init__(HOT_TYPE, nodetemplate, csar_dir=csar_dir)
    
    
