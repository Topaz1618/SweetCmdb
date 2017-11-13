#_*_coding:utf-8_*_
# Author:Topaz
from config import settings
from src.client import SweetAgent

def handle():
    # print(settings.MODE)
    if settings.MODE == "agent":
        cli = SweetAgent()
    elif settings.MODE == "ssh":
        print("ssh")
    elif settings.MODE == "salt":
        print("salt")
    else:
        raise Exception("请配置资产采集方式,如agent/ssh/salt")
    cli.process()

