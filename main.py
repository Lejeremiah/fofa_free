# -*- coding: UTF-8 -*-
'''
@Project ：fofa_free 
@File    ：main.py.py
@IDE     ：PyCharm 
@Author  ：lms.jeremiah@gmail.com
@Date    ：2024/07/29 18:36 
'''

import library.utils.log
import logging

from library.utils.download import Downloader
from library.utils.keywordsHandler import KeywordsHandler
from library.utils.contentsHandler import ContentsHandler
from concurrent.futures import ThreadPoolExecutor
from library.utils.configHandler import config

# keyword_handler.handle_by_nologin('''
# protocol=="socks5" &&
# "Version:5" &&
# "Method:No Authentication(0x00)" &&
# country="CN"
# ''',2)
#
# url = keyword_handler.handle_by_nologin('''
#     app="ThinkPHP" &&
#     body="__destruct" &&
#     status_code="200"
#     ''',i)


downloader = Downloader()
keyword_handler = KeywordsHandler()
contents_handler = ContentsHandler()



def handler(i):
    url = keyword_handler.handle_by_nologin(config["search"]["content"], i)
    content =  downloader(url)
    contents_handler.get_contents_by_cssselect(content)



if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)

    for i in range(int(config["search"]["page"])):
        pool.submit(handler,i)
    pool.shutdown()

