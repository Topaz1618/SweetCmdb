#_*_coding:utf-8_*_
# Author:Topaz
from src.plugins.basic import BasicPlugin


def get_server_info(hostname=None):
    response = BasicPlugin(hostname).execute()

