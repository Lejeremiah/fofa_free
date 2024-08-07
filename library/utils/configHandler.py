# -*- coding: UTF-8 -*-
'''
@Project ：fofa_free 
@File    ：configHandler.py.py
@IDE     ：PyCharm 
@Author  ：lms.jeremiah@gmail.com
@Date    ：2024/08/06 17:59 
'''
import yaml

with open('config.yaml', 'r', encoding="utf-8") as yaml_file:
    config = yaml.safe_load(yaml_file)

print(config['account']['fofa_token'])
print(config['search']['content'])

