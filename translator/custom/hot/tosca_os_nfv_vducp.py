from translator.hot.tosca.etsi_nfv.tosca_nfv_vducp import ToscaNfvVducp

TARGET_CLASS_NAME = 'OSNfvVducp'

class OSNfvVducp(ToscaNfvVducp):
    """Translate TOSCA node type os.nodes.nfv.VduCp, an extension to tosca.nodes.nfv.VduCp"""

    toscatype = 'os.nodes.nfv.VduCp'

    def get_hot_attribute(self, attribute, args):
        if attribute == 'ip_address':
            attr = {}
            attr['get_attr'] = [self.name, 'fixed_ips', '0', 'ip_address']
            return attr
        return super(OSNfvVducp, self).get_hot_attribute(attribute, args)

