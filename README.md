# tpshopweb_appTest
## 自动化测试tpshop项目

其中web自动化测试使用selenium库
需安装测试所用浏览器对应的webdriver驱动

app自动化测试使用appium库
需安装Java-SDK和android-SDK来调试(配置环境变量)
还需手机打开开发者模式进行连接调试(打开USB调试，打开禁止权限监控)
或者下载手机模拟器，如nox夜神模拟器(把adb程序替换为Android-SDK下的adb)
打开模拟器\连接手机后，在终端输入：
adb devices      连接的设备/模拟器的状态的相关信息
adb shell dumpsys window | findstr mCurrentFocus   获取到app包名和界面名称
adb shell getprop ro.build.version.release    获取手机版本
另外还要用到appium服务端软件，使用时开启端口使得python的appium库能连接

本项目为PO模式（page object model）模板
