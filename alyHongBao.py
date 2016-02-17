#coding:utf-8
import os
import HTMLTestRunner
import unittest
import time
from appium import webdriver

import logging


# Returns abs path relative to self file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):
    def get_element_by_id(self,driver,id_str):
        # 因为python client 没有验证元素是否存在，find不存在的元素会抛出异常
        try:
            node = driver.find_element_by_id(id_str)
            return node
        except Exception:
            return False

    def test_(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'BX9035L70L'  #adb devices查到的设备名
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['appPackage'] = "com.eg.android.AlipayGphone"  #被测App的包名
        desired_caps['appActivity'] = "com.eg.android.AlipayGphone.AlipayLogin" #启动时的Activity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


        # 循环获取，避免因为在闪屏页时间过长无法获取到首页按钮
        while True:
            node = self.get_element_by_id(driver,"com.alipay.android.phone.openplatform:id/xiuxiu_new_year_eve") #首页 咻一咻按钮
            if node:
                node.click()
                break
            time.sleep(1)
        time.sleep(1)

        #点击按钮
        for i in range(1, 2000):
            start = self.get_element_by_id(driver,"com.alipay.android.wallet.newyear:id/huxi") #咻一咻主界面按钮
            if start:
                start.click()

            time.sleep(0.5)
            action = self.get_element_by_id(driver,"com.alipay.android.wallet.newyear:id/actionBtn") #操作按钮,分享好友，观看现场...各种
            if action:
                # 获取按钮文字，通过文字判断是否有红包
                actionText = self.get_element_by_id(driver,"com.alipay.android.wallet.newyear:id/actionBtnText")
                if not actionText or actionText.text == "" or actionText.text.find("播")!= -1 or actionText.text.find("享")!= -1 or actionText.text.find("观看")!= -1 or actionText.text.find("试试看")!= -1:
                    # 过滤无用弹出
                    pass
                else:
                    action.click()
                    time.sleep(0.5)
            close = self.get_element_by_id(driver,"com.alipay.android.wallet.newyear:id/egg_card_close");#关闭弹出层
            if close:
                close.click()
        fp.close()
        driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中
    filename="./myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')
    runner.run(testunit)

