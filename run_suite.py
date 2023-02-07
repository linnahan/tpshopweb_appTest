import os
import unittest
from htmltestreport import HTMLTestReport
from tpshopweb_appTest.config import DIR_PATH

# 判断是否有report、img、log这三个文件夹，没有的话创建
report_path = DIR_PATH + os.sep + "report"
img_path = DIR_PATH + os.sep + "img"
log_path = DIR_PATH + os.sep + "log"
if not os.path.exists(report_path):
    os.makedirs(report_path)
if not os.path.exists(img_path):
    os.makedirs(img_path)
if not os.path.exists(log_path):
    os.makedirs(log_path)

# 运行script文件夹脚本案例，并保存测试报告
suite = unittest.defaultTestLoader.discover("./script")
file_path = DIR_PATH + os.sep + "report" + os.sep + "tpshop_auto.html"
HTMLTestReport(file_path).run(suite)