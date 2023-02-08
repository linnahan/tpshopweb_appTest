import os
import unittest
from htmltestreport import HTMLTestReport
from tpshopweb_appTest.config import DIR_PATH

# 判断是否有report、img、log这三个文件夹，没有的话创建
report_path = os.path.join(DIR_PATH, "report")
img_path = os.path.join(DIR_PATH, "img")
log_path = os.path.join(DIR_PATH, "log")
os.makedirs(report_path, exist_ok=True)
os.makedirs(img_path, exist_ok=True)
os.makedirs(log_path,exist_ok=True)

# 运行script文件夹脚本案例，并保存测试报告
suite = unittest.defaultTestLoader.discover("./script")
file_path = os.path.join(DIR_PATH, "report", "tpshop_auto.html")
HTMLTestReport(file_path).run(suite)