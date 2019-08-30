from translator.custom.hot.os_hot_resource import OSHotResource

TARGET_CLASS_NAME = 'OSSecurityGroupRule'
HOT_TYPE = 'OS::Neutron::SecurityGroupRule'

class OSSecurityGroupRule(OSHotResource):
    '''Translate TOSCA node type os.nodes.neutron.SecurityGroupRule'''

    toscatype = 'os.nodes.neutron.SecurityGroupRule'

    def __init__(self, nodetemplate, csar_dir=None):
        super(OSSecurityGroupRule, self).__init__(HOT_TYPE, nodetemplate, csar_dir=csar_dir)
    
    
