#_*_coding:utf-8_*_
# Author:Topaz
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from src import main
if __name__ == "__main__":
    main.handle()