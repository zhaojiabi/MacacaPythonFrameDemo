# MacacaPythonFrameDemo
A frame about macaca with python／这是一个关于macaca+python组合的自动化测试框架体系，不考虑具体app的兼容特性，主要是分享这个框架的结构

1.macaca+python的环境搭建具体见下链接：

[Macaca 面向多端的自动化测试工具基于Python搭建详解 --Android、IOS搭建步骤](http://blog.csdn.net/weixin_39008941/article/details/73824909)

2.启动macaca server：

```
启动macaca server 命令，verbose表示输出详细日志信息
$macaca server --verbose
```

3.运行脚本：

```
#另开一个终端页面，进入目标文件夹下，输入如下命令
$./Run.sh
```

4.运行成功后文件显示：

在文件夹中生成以当时时间创建的文件夹，并在文件夹中放有这次的测试报告和截图。

测试报告为python unittest 扩展的测试报告，经过改动的HTMLTestRunner，具体改动见如下链接：

[Macaca+HTMLTestRunner测试报告模式修改，基于python unittest 测试框架扩展](http://blog.csdn.net/weixin_39008941/article/details/75222564)




