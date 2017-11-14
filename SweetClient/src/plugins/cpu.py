#_*_coding:utf-8_*_
# Author:Topaz
import os
from .base import BasePlugin
from lib.response import BaseResponse
from config.settings import BASEDIR

class CpuPlugin(BasePlugin):
    def linux(self):
        response = BaseResponse()
        try:
            if self.test_mode:
                output = open(os.path.join(BASEDIR,'files/cpuinfo.out'),'r').read()
            else:
                #去执行命令
                print("非测试模式")
            response.data = self.parse(output)
        except Exception as e:
            #错误写到日志
            print('抓到错误',e)
        return response

    @staticmethod
    def parse(output):
        cpu_physical_set = set()
        response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}
        output = output.strip()
        for item in output.split('\n\n'):
            for row_line in item.split('\n'):
                key,value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
            response['cpu_physical_count'] = len(cpu_physical_set)
        return response