#coding:utf-8

__author__ = 'JiaBi Zhao'

import unittest
import os
import time
import traceback

# import HTMLTestRunner
from macaca import WebDriver
from macaca import WebDriverException



path = os.path.abspath('.')
# app_path = os.path.join(path,'app_file/tuyasmart.apk')


def screenshot(name, self):
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screenshot = name + '_' + date_time + '.png'
    screenshot_path = path + '/' + screenshot
    print(screenshot_path)
    
    self.driver.save_screenshot(screenshot_path)


def testcase(desired_caps, server_url):
    def _testcase(func):
        # args[0] 是self传值，第一个参数一定要是self
        def wrapper(*args, **kwargs):
            try:
                # test case 开始之前的操作，初始化
                print("before %s." % func.__name__)
                args[0].driver = WebDriver(desired_caps, server_url)
                args[0].driver.init()

                # test case 结束之后的操作，卸载应用
                ret = func(*args, **kwargs)

                # test case 结束之后的操作，卸载应用
                print("after %s." % func.__name__)
                os.system('adb uninstall com.tuya.smart') 
                args[0].driver.quit()
                return ret
            except AssertionError,e:
                print("AssertionError")
                screenshot('screenshot', args[0])
                traceback.print_exc()

                # test case 结束之后的操作，卸载应用
                os.system('adb uninstall com.tuya.smart') 
                args[0].driver.quit()
                # raise e
            except WebDriverException,e:
                print("WebDriverException")
                screenshot('screenshot', args[0])

                # test case 结束之后的操作，卸载应用
                os.system('adb uninstall com.tuya.smart') 
                args[0].driver.quit()
                # traceback.print_exc()
                raise traceback.print_exc()
        return wrapper
    return _testcase
