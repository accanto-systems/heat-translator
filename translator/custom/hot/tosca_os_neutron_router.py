from translator.custom.hot.os_hot_resource import OSHotResource

TARGET_CLASS_NAME = 'OSNeutronRouter'
HOT_TYPE = 'OS::Neutron::Router'

class OSNeutronRouter(OSHotResource):
    '''Translate TOSCA node type os.nodes.neutron.Router'''

    toscatype = 'os.nodes.neutron.Router'

    def __init__(self, nodetemplate, csar_dir=None):
        super(OSNeutronRouter, self).__init__(HOT_TYPE, nodetemplate, csar_dir=csar_dir)
    
    
