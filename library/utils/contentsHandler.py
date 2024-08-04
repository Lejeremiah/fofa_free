# -*- coding: UTF-8 -*-
'''
@Project ：fofa_free 
@File    ：contentsHandler.py
@IDE     ：PyCharm 
@Author  ：lms.jeremiah@gmail.com
@Date    ：2024/07/29 19:58 
'''
import base64
import os
import datetime

import lxml.html
import urllib.parse as urlparse
import logging

class ContentsHandler():
    def __init__(self):
        self.file_name = 'result'
    def get_contents_by_cssselect(self,html_string_and_code):
        results = []

        html_string_broken = html_string_and_code['html']
        html_tree_broken = lxml.html.fromstring(html_string_broken)
        # html_string_pretty = lxml.html.tostring(html_tree_broken,pretty_print=True)
        # html_tree_pretty = lxml.html.tostring(html_string_pretty)
        html_tree_pretty = html_tree_broken

        divs_href_and_content = html_tree_pretty.cssselect('span.hsxa-host')
        for div in divs_href_and_content:
            content = div.text_content()
            content = content.replace('\n','').replace(' ','')
            if 'http' in content:
                result = content
            else:
                result = 'http://' + content
            # print(result)
            logging.info(result)
            results.append(result)

        self.save_contents_by_plaintext(html_string_and_code['url'],results)
    def save_contents_by_plaintext(self,url,results):
        querys = urlparse.urlparse(url).query
        querys = urlparse.parse_qs(querys)
        qbase64 = querys.get('qbase64')[0]
        keyword = base64.b64decode(qbase64).decode('utf8').replace(' ', '')

        if not os.path.exists('results'):
            os.mkdir('results')
        plaintext_file_name = 'results/result-%s.txt' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        plaintext_file = open(plaintext_file_name,'a+')

        plaintext_file.write(keyword+'\n')
        for line in results:
            plaintext_file.write(line+'\n')

        plaintext_file.close()




