#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import os
import time

from xml.dom.minidom import parse
import xml.dom.minidom


path = os.path.abspath('.')
data_path = os.path.join(path,'features/data/data.xml')


DOMTree = xml.dom.minidom.parse(data_path)
data = DOMTree.documentElement


def get_attrvalue(node, attrname):
     return node.getAttribute(attrname)



# style = xml中的大类 ; typename = 细分属性; typevalue = 细分属性的值; valuename = xml文件，需要获取的值的tag;
def get_data_vaule(style, typename, typevalue, valuename):
    nodelist = data.getElementsByTagName(style)

    for node in nodelist: 
        if typevalue == node.getAttribute(typename):
            node_name = node.getElementsByTagName(valuename)
            value = node_name[0].childNodes[0].nodeValue
            print value
            return value
    return 