#_*_coding:utf-8_*_
# Author:Topaz
from src.plugins.basic import BasicPlugin
from config import settings
import importlib


def get_server_info(hostname=None):
    response = BasicPlugin(hostname).execute()
    if not response.status:
        return response
    for k,v in settings.PLUGINS_DICT.items():
        plugin_path,plugin_name = v.rsplit('.',1)
        item_plugin  = getattr(importlib.import_module(plugin_path),plugin_name)
        obj = item_plugin(hostname).execute()
        response.data[k] = obj
    return response


