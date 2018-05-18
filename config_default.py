#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Default configurations.
'''

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'examdb'
    },
    'session': {
        'secret': 'AwEsOmE'
    },     
}
question_source='/home/judgeFile/data'
student_source ='/home/exam/source/excel'
remind_source = '/home/exam/source'
exampage_source ='/home/exam/source/exampage'
server_num=0
import logging
logging_level = logging.DEBUG
