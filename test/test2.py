#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2021/3/3 13:56
# @Author  : Gavin
import os
import platform

os_system = platform.system()
localPath = os.listdir("C:/Users/gavin/AppData/Local/Google/Chrome/Application")[0][0:2]

print(localPath)