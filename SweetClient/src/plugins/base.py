#_*_coding:utf-8_*_
# Author:Topaz
import subprocess
from lib.log import Logger
from config import settings

class BasePlugin(object):
    def __init__(self,hostname=''):
        self.logger = Logger()
        self.test_mode = settings.MODE  #是否测试模式
        self.mode_list = ['agent','salt','ssh']
        self.mode = settings.MODE
        self.hostname = hostname
    def execute(self):
        print("hello base execute")
        return self.linux()
    def linux(self):
        raise Exception('Yo must implement linux method.')
