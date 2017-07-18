#coding:utf-8

__author__ = 'JiaBi Zhao'

import unittest
import os
import time
import HTMLTestRunner
from macaca import WebDriver

# path = os.path.abspath('.')
# app_path = os.path.join(path,'app/tuyasmart.apk')
# print(app_path)

# desired_caps = {
#     'platformName': 'android',
#     # path2 = os.path.split(os.path.abspath('.'))
#     # path = os.path.join(os.path.split(os.path.abspath('.'))[0],'app/tuyasmart.apk')
#     # 'app': 'https://npmcdn.com/android-app-bootstrap@latest/android_app_bootstrap/build/outputs/apk/android_app_bootstrap-debug.apk',
#     # 'app': '/Users/zhaojiabi/Downloads/tuyasmart.apk',
#     'app': app_path,
#     'reuse': 2,
#     # 'udid': 'T8ROSCCY79KFBQU4',
#     'autoDismissAlerts': 'true',
    
# }

# server_url = {
#     'hostname': 'localhost',
#     'port': 3456
# }

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
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        print('tearDown...')
        cls.driver.quit()

    def test_Android_login_001(self):
        print('testing')
        print(self)
        # self.driver.elements_by_class_name('android.widget.TextView')[0].click()
        self.driver.element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        self.driver.take_screenshot()
        #     # .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]') \
        #     # .send_keys('中文+Test+12345678')   \

        # els =self.driver \
        #     .elements_by_class_name('android.widget.EditText')\
        #     .send_keys('13456825963')
        # els[1].send_keys('Kitty12345')

        # self.driver \
        #     .elements_by_class_name('android.widget.Button')\
        #     .click()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(MacacaTest("test_Android_login_001"))
    return suite
