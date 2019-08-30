from translator.custom.hot.os_hot_resource import OSHotResource

TARGET_CLASS_NAME = 'OSSecurityGroup'
HOT_TYPE = 'OS::Neutron::SecurityGroup'

class OSSecurityGroup(OSHotResource):
    '''Translate TOSCA node type os.nodes.neutron.SecurityGroup'''

    toscatype = 'os.nodes.neutron.SecurityGroup'

    def __init__(self, nodetemplate, csar_dir=None):
        super(OSSecurityGroup, self).__init__(HOT_TYPE, nodetemplate, csar_dir=csar_dir)
    
    
