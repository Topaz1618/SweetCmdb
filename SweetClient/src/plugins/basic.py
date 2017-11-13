#_*_coding:utf-8_*_
# Author:Topaz
from .base import BasePlugin
from lib.response import BaseResponse
class BasicPlugin(BasePlugin):
    def client_os(self):
        a = 111
        return a

    def os_version(self):
        a = 222
        return a

    def client_hostname(self):
        a = 333
        return a
    def linux(self):
        print('linux ')
        response = BaseResponse()
        try:
            ret = {
                'client_os': self.client_os(),
                'os_version':self.os_version(),
                'hostname':self.client_hostname(),
            }
            response.data = ret
        except Exception as e:
            print(e)
