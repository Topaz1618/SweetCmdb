#_*_coding:utf-8_*_
# Author:Topaz
from src import plugins

class SweetBase():
    def __init__(self):
        self.a = 'aaa'

class SweetAgent(SweetBase):
    def __init__(self):
        super(SweetAgent,self).__init__()

    def process(self):
        print("agent process")
        server_info = plugins.get_server_info()

class SweetSSH():
    pass

class SweetSalt():
    pass

