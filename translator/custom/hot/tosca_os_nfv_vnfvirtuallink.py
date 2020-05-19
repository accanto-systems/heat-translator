from translator.hot.syntax.hot_resource import HotResource

TARGET_CLASS_NAME = 'OSNfvVnfVirtualLink'
HOT_TYPE = 'OS::Neutron::Net'

class OSNfvVnfVirtualLink(HotResource):
    """Translate TOSCA node type os.nodes.nfv.VnfVirtualLink, an extension to tosca.nodes.nfv.VnfVirtualLink"""

    toscatype = 'os.nodes.nfv.VnfVirtualLink'

    def __init__(self, nodetemplate, csar_dir=None):
        # Check if it refers to an existing Network by name
        self.network_name = None
        for prop in nodetemplate.get_properties_objects():
            if prop.name == 'name':
                self.network_name = prop.value
                break
        if self.network_name is None:
            super(OSNfvVnfVirtualLink, self).__init__(nodetemplate, csar_dir=csar_dir)
        else:
            # We're customising the translation
            super(OSNfvVnfVirtualLink, self).__init__(nodetemplate, type=HOT_TYPE, csar_dir=csar_dir)

    def handle_properties(self):
        self.properties = {'name': self.network_name}

    def handle_expansion(self):
        return []
            