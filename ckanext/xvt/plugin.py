import ckan.plugins as plugins
import model


class XVTPluginClass(plugins.SingletonPlugin):
    """
    Setup plugin
    """
    print '#############################'
    print '#        ckanext-xvt        #'
    print '#############################'

    model.add_record()