#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 18:38
# @Author  : Gavin

"""
说明：
# 调用的到的 第三方模块：seldom、sys、time
# from seldom import Seldom
# import seldom
# 调用的到的 私有化模块：model/page_object/
"""

from PageObject.loginPage import login
from models.osDriver import osSystem
import seldom
from seldom import Seldom, ChromeConfig
import os
import sys
sys.path.append(os.pardir)


class test01_login(seldom.TestCase):
    def start(self):
        self.dr = login(Seldom.driver)
        self.dr.get(login.url)
        self.max_window()

    def down(self):
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """测试示例1"""
        self.dr.search_input(key='你')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test01')

    def test02(self):
        """测试示例2"""
        self.dr.search_input_loc.clear()
        self.dr.search_input_loc.send_keys('是')
        self.dr.search_button_loc.click()
        self.assertText("百度一下")
        print('用例说明：test02')

    def test03(self):
        """测试示例3"""
        self.dr.search_input(key='最')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test03')

    def test04(self):
        """测试示例4"""
        self.dr.search_input(key='棒')
        self.dr.search_button()
        self.assertText("百度一下4")
        print('用例说明：test04')

    def test05(self):
        """测试示例5"""
        self.dr.search_input(key='的')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test05')


if __name__ == '__main__':
    ChromeConfig.headless = False
    ChromeConfig.executable_path = osSystem(
        '../')  # 默认根据操作系统自行选择Chromedriver驱动
    seldom.main(
        path='../test_case/test01_login.py',
        browser='chrome',
        debug=False,
        rerun=0,
        timeout=10,
        save_last_run=True,
        title='自动化测试报告',
        description='测试环境：Chrome'
    )
