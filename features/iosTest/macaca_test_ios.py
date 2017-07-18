#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver
from retrying import retry

from method.public import *
from method.element_method import *
from method.get_xpath import *
from method.get_data import *

path = os.path.abspath('.')
app_path = os.path.join(path,'app_file/')

desired_caps = {
    'platformName': 'iOS',
    'uuid': 'c457653f3a062f64888ab747a608684c481b0c55',
    'bundleId': 'com.tuya.smart.Hoc',
    'app': app_path,
    'autoDismissAlerts': 'false',
    'reuse': 2
}

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

    @classmethod
    def tearDownClass(cls):
        print('tearDown...')

    @testcase(desired_caps, server_url)
    def test_IOS_login_001(self):
        print('case_ios_001')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MacacaTest("test_IOS_login_001"))
    return suite


