from translator.hot.tosca.tosca_floating import ToscaFloatingIP

TARGET_CLASS_NAME = 'ToscaExtFloatingIp'


class ToscaExtFloatingIp(ToscaFloatingIP):

    toscatype = 'tosca.nodes.network.FloatingIP'

    def get_hot_attribute(self, attribute, args):
        if attribute == 'floating_ip_address':
            attr = {}
            attr['get_attr'] = [self.name, 'floating_ip_address']
            return attr
        return super(ToscaExtFloatingIp, self).get_hot_attribute(attribute, args)
