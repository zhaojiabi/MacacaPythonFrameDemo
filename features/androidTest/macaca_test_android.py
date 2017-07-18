#coding:utf-8

__author__ = 'JiaBi Zhao'

import unittest
import os
import time

from macaca import WebDriver
from macaca import asserters

from method.public import *
from method.element_method import *
from method.get_xpath import *
from method.get_data import *

path = os.path.abspath('.')
app_path = os.path.join(path,'app_file/chuizibianqian.apk')


desired_caps = {
    'platformName': 'android',
    'app': app_path,
    'reuse': 2,
    # 'udid': 'T8ROSCCY79KFBQU4',
    'autoDismissAlerts': 'true',
}

platform = desired_caps['platformName']
elementId = 'id'
elementXpath = 'xpath'
elementName = 'name'


server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUp...')
        # cls.driver = WebDriver(desired_caps, server_url)
        # cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        print('tearDown...')
        # cls.driver.quit()

    @testcase(desired_caps, server_url)
    def test_Android_login_001(self):
        print('case_smoke_001')
        is_displayed(find_element_with_name(self, platform, 'loginButtonName'))

        # find_element_with_id(self, platform, 'loginButtonId').click()
        
        # find_element_with_id(self, platform, 'usernameInputId').send_keys(get_data_vaule('account', 'type','phone','username'))
        
        # find_element_with_id(self, platform, 'userpasswordInputId').send_keys(get_data_vaule('account', 'type','phone','password'))
        
        # find_element_with_id(self, platform, 'submitId').click()

        # find_element_with_id(self, platform, 'devicesAddId').click()
        

    @testcase(desired_caps, server_url)
    def test_Android_logout_002(self):
        print('case_smoke_002')

        MacacaTest.login_test(self)

        find_element_with_id(self, platform, 'homeCenterId').click()
        
        find_element_with_id(self, platform, 'headPhonoId').click()

        find_element_with_id(self, platform, 'logoutButtonId').click()


    def login_test(self):

        find_element_with_id(self, platform, 'loginButtonId').click()

        find_element_with_id(self, platform, 'usernameInputId').send_keys(get_data_vaule('account', 'type','phone','username'))
        
        find_element_with_id(self, platform, 'userpasswordInputId').send_keys(get_data_vaule('account', 'type','phone','password'))
        
        find_element_with_id(self, platform, 'submitId').click()

        find_element_with_id(self, platform, 'devicesAddId').click()



def suite():
    suite = unittest.TestSuite()
    suite.addTest(MacacaTest("case_smoke_001"))
    # suite.addTest(MacacaTest("test_Android_logout_002"))
    return suite
