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

keyword_handler = KeywordsHandler()
downloader = Downloader()
contents_handler = ContentsHandler(config["search"]["content"])

def handler(i):
    url = keyword_handler.handle_by_login(config["search"]["content"], i)
    content = downloader(url)
    contents_handler.get_contents_by_cssselect(content)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)

    for i in range(int(config["search"]["page"])):
        pool.submit(handler, i)
    pool.shutdown()
    contents_handler.destroy()


