__author__='igx'

from scrapy.cmdline import  execute

import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy","crawl","a51job"])