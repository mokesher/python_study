#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os,sys
os_path = os.path.dirname(os.getcwd())
print(os_path)
sys.path.append(os_path)
print(os.getcwd())
import text




print(os.path.dirname(os.path.abspath(__file__)))