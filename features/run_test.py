#coding:utf-8

__author__ = 'JiaBi Zhao'

import unittest
import os
import time

from macaca import WebDriver

import androidTest.macaca_test_android
import iosTest.macaca_test_ios
import HTMLTestRunner

path = os.path.abspath('.')

if __name__ == '__main__':
    
    # #打开一个文件，将result写入此file中
    fp=open(path+"/result.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Macaca Python Frame Demo Test',description=u'Test Result:')

    #运行测试组
    #运行androidTest文件夹下的macaca_test_android文件中的suit方法
    runner.run(androidTest.macaca_test_android.suite())
    #运行iosTest文件夹下的macaca_test_ios文件中的suit方法
    #runner.run(iosTest.macaca_test_ios.suite())
    fp.close()

