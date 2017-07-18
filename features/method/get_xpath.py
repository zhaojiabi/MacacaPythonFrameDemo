#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
import time

from xml.dom.minidom import parse
import xml.dom.minidom


path = os.path.abspath('.')
xpath_path = os.path.join(path,'features/data/xpath.xml')


DOMTree = xml.dom.minidom.parse(xpath_path)
data = DOMTree.documentElement


def get_xmlnode(node, name):
    return node.getElementsByTagName(name)

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue 

def get_element_path(typename, platform, valuename):

    datalist = data.getElementsByTagName(typename)
    nodelist = datalist[0].getElementsByTagName(platform)

    for node in nodelist: 
        node_name = node.getElementsByTagName(valuename)
        value = node_name[0].childNodes[0].nodeValue 
        
        print value
        return value

    
    # b= bb[0]
    # print b.firstChild.data
    # return b.firstChild.data

    