#_*_coding:utf-8_*_
# Author:Topaz
from src import plugins

class SweetBase():
    def __init__(self):
        self.a = 'aaa'

class SweetAgent(SweetBase):
    def __init__(self):
        super(SweetAgent,self).__init__()
    def load_local_cert(self):
        pass

    def process(self):
        print("agent process")
        server_info = plugins.get_server_info() #本台client所有信息拿到了
        if not server_info.status:
            return
        local_cert = self.load_local_cert()


class SweetSSH():
    pass

class SweetSalt():
    pass

