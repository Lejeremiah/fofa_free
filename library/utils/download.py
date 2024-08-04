# -*- coding: UTF-8 -*-
'''
@Project ：fofa_free 
@File    ：download.py
@IDE     ：PyCharm 
@Author  ：lms.jeremiah@gmail.com
@Date    ：2024/07/29 19:59 
'''
import time
import urllib.parse as urlparse
import datetime
import random

import requests
import logging

'''
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
'''

class Throttle():
    def __init__(self,delay):
        self.delay = delay
        self.domains = {}
    def wait(self,url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_time = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_time > 0:
                time.sleep(sleep_time)
        self.domains[domain] = datetime.datetime.now()


class Downloader():
    def __init__(self,
                 user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                 delay = 1,
                 num_retries = 2,

                 proxies = ['127.0.0.1:7890'],
                 cache = None
                 ):
        self.user_agent = user_agent
        self.num_retries = num_retries
        self.throttle = Throttle(delay)

        self.proxies = proxies
        self.cache = cache
    def __call__(self,url):
        '''
        :param url: download url
        :return: {
            'url': url,
            'html':html,
            'code':code,
            }
        '''


        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            headers = {'User-Agent':self.user_agent}
            proxy = random.choice(self.proxies) if self.proxies else None
            result = self.download(url=url,headers=headers,proxy=proxy,num_retries=self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result

    def download(self,url,headers,proxy=None,num_retries=2):
        # print("Downloading:",url)
        logging.info("Downloading:"+url)

        if proxy:
            proxies = {
                'https':'http://'+proxy,
                'http':'http://'+proxy
            }
        else:
            proxies = None

        try:
            response = requests.get(url=url,headers=headers,proxies=proxies)
            html = response.text
            code = response.status_code
            if 500 <= code < 600 and num_retries > 0:
                # print("Download Error:",url)
                logging.error("Download Error:"+url)
                result = self.download(url=url,headers=headers,proxy=proxy,num_retries=num_retries - 1)
                return result
        except requests.exceptions as e:
            # print("Download Error:",e.reason)
            logging.error("Download Error:"+e.reason)
            html = None
            code = None
            url = None
        return {
            'url':url,
            'html':html,
            'code':code
        }










