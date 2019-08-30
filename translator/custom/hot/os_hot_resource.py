
from translator.hot.syntax.hot_resource import HotResource


class OSHotResource(HotResource):

    def __init__(self, hot_type, nodetemplate, csar_dir=None):
        super(OSHotResource, self).__init__(nodetemplate,
                                               type=hot_type,
                                               csar_dir=csar_dir)

    def __is_property_allowed(self, property_key, property_value):
        return True

    def handle_properties(self):
        tosca_props = self.get_tosca_props()
        self.properties = {}
        for key, value in tosca_props.items():
            if self.__is_property_allowed(key, value):
                self.properties[key] = value

    def __is_attribute_allowed(self, attribute, args):
        return True

    def get_hot_attribute(self, attribute, args):
        attr = {}
        if self.__is_attribute_allowed(attribute, args):
            attr['get_attr'] = [self.name, attribute]
        return attr