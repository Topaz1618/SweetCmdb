#_*_coding:utf-8_*_
# Author:Topaz
from .base import BasePlugin
from lib.response import BaseResponse
class BasicPlugin(BasePlugin):
    '''
    获取基本信息：
    1.系统平台
    2.系统版本
    3.主机名
    '''
    def client_os(self):
        '''获取系统平台 linux/windows'''
        if self.test_mode:
            output = 'linux'
        return output.strip()
    def os_version(self):
        '''获取系统版本'''
        if self.test_mode:
            output =  """CentOS release 6.6 (Final)\nKernel \r on an \m"""
        return output.strip().split('\n')[0]
    def client_hostname(self):
        '''获取主机名'''
        if self.test_mode:
            output = 'c1.com'
        return output.strip()
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
            ##这里要加到错误日志，先略过哈，都捋完再来搞
            print(e)
        return response