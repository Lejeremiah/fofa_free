# -*- coding: UTF-8 -*-
'''
@Project ：fofa_free 
@File    ：keywordsHandler.py.py
@IDE     ：PyCharm 
@Author  ：lms.jeremiah@gmail.com
@Date    ：2024/07/29 19:59 
'''

'''

protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && country="CN" && before="2023-05-02"
'''
import base64
import datetime
# from datetime import datetime,timedelta



class KeywordsHandler():
    def __init__(self):

        '''
        base_query
        '''
        self.qbase64 = None

        '''
        extract_query
        '''
        self.country = 'CN'
        self.after = '2023-05-22'
        self.before = '2023-05-22'

        '''
        url_query
        '''
        self.page_size = '10'
        self.full = 'false'
    def handle_by_api(self):
        pass
    def handle_by_nologin(self,query,times:int):
        base_url = 'https://fofa.info/result'

        query = query.replace('\n',' ')
        time_for_before = (datetime.datetime.now() + datetime.timedelta(days=-times)).strftime('%Y-%m-%d')
        query = query + '&& before="' + time_for_before + '" '
        time_for_after = (datetime.datetime.now() + datetime.timedelta(days=-times-1)).strftime('%Y-%m-%d')
        query = query + '&& after="' + time_for_after + '" '
        # print(query)

        query_base64 = base64.b64encode(query.encode()).decode('utf-8')
        final_url = base_url + '?qbase64=' + query_base64 + '&full=false&page_size=10'
        # print(final_url)
        return final_url
    def handle_by_login(self,query,times:int):
        base_url = 'https://fofa.info/result'

        query = query.replace('\n',' ')
        time_for_before = (datetime.datetime.now() + datetime.timedelta(days=-times)).strftime('%Y-%m-%d')
        query = query + '&& before="' + time_for_before + '" '
        time_for_after = (datetime.datetime.now() + datetime.timedelta(days=-times-1)).strftime('%Y-%m-%d')
        query = query + '&& after="' + time_for_after + '" '
        # print(query)

        query_base64 = base64.b64encode(query.encode()).decode('utf-8')
        final_url = base_url + '?qbase64=' + query_base64 + '&full=false&page_size=10'
        # print(final_url)
        return final_url