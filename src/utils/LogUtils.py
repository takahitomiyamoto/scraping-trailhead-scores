#!/usr/bin/env python3
# coding: UTF-8

from datetime import datetime


class LogUtils:
    # output the debug message
    def debug(self, text):
        msg = ''
        msg = msg + '['
        msg = msg + datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        msg = msg + '] '
        msg = msg + text
        print(msg)
