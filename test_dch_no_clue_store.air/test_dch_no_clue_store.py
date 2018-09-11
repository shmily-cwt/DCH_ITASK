# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from common import config
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco(text="未进").click()
poco("com.iris.dch.itask:id/listview").child("android.widget.FrameLayout")[1].click()
poco(text="销售平台").click()
txt1 = ''
try:
    txt1 = poco("com.iris.dch.itask:id/tv_add").get_text()
except BaseException as e:
    txt1 = ''
if txt1 == '':
    poco("com.iris.dch.itask:id/tv_id_card").click()
    #text("130768877665243565")
    text(config.get_id_card())
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.dch.itask:id/tv_province").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_city").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_canton").click()
    poco(text="东城区").click()
    poco("com.iris.dch.itask:id/tv_address").click()
    text("jhssdferweirufidsf")
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.165625])
    poco(text="车辆信息").click()
    poco("com.iris.dch.itask:id/rb_intent1").click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.165625])
else:
    poco("com.iris.dch.itask:id/tv_add").click()
    poco("com.iris.dch.itask:id/tv_id_card").click()
    #text("130768877665243565")
    text(config.get_id_card())
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.dch.itask:id/tv_province").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_city").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_canton").click()
    poco(text="东城区").click()
    poco("com.iris.dch.itask:id/tv_address").click()
    text("jhssdferweirufidsf")
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.165625])
    poco(text="车辆信息").click()
    poco("com.iris.dch.itask:id/rb_intent1").click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.165625])
    
    




    


