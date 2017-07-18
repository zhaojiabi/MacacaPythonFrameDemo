#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import os
import time

from xml.dom.minidom import parse
import xml.dom.minidom

from method.get_xpath import *
from method.get_data import *


path = os.path.abspath('.')
elementId = 'id'
elementXpath = 'xpath'
elementName = 'name'

# self ; platform = android/ios; valuename = xml文件，需要获取的值的tag;
def find_element_with_id(self, platform, valuename):
    element = get_element_path(elementId, platform, valuename)
    self.driver.wait_for_element_by_id(element)
    return self.driver.element_by_id(element)

# self ; platform = android/ios; valuename = xml文件，值的tag;
def find_element_with_xpath(self, platform, valuename):
    element = get_element_path(elementXpath, platform, valuename)
    self.driver.wait_for_element_by_xpath(element)
    return self.driver.element_by_xpath(element)

# self ; platform = android/ios; valuename = xml文件，值的tag;
# app中英文，匹配的时候有关系
def find_element_with_name(self, platform, valuename):
    element = get_element_path(elementName, platform, valuename)
    self.driver.wait_for_element_by_name(element)
    return self.driver.element_by_name(element)

def assert_true_name(self, platform, valuename, text):
    element = find_element_with_name(self, platform, valuename) 
    print element

    element.i
    if element != text:
        raise self.assertTrue(False, "page has not the text.")

    # element = get_element_path(elementName, platform, valuename)
    # self.driver.wait_for_element_by_name(element)
    # return self.driver.element_by_name(element)