from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.kalading.engineers'
desired_caps['appActivity'] = 'com.kalading.engineers.MainActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:5038/wd/hub', desired_caps)

WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((MobileBy.ID, "com.kalading.engineers:id/getback_password_phonenum")))
driver.find_element_by_id("com.kalading.engineers:id/getback_password_phonenum").send_keys("13072902013")
driver.find_element_by_id("com.kalading.engineers:id/getback_password_codes").send_keys("111111")
driver.find_element_by_id("com.kalading.engineers:id/getback_password_submit").click()  # 输入密码登录
driver.implicitly_wait(10)
driver.find_element_by_id("com.kalading.engineers:id/gesturepwd_guide_btn").click()  # 点击下一步
driver.find_element_by_id("com.kalading.engineers:id/right_btn").click()  # 点击下一步


element = driver.find_element_by_id("com.kalading.engineers:id/gesturepwd_create_lockview")
size = element.size  # 打印定位到的元素的长宽
step = int(size["width"] / 6)
ori = element.location  # 元素起点坐标
point1 = (ori["x"] + step, ori["y"] + step)
point2 = (point1[0] + step * 2, point1[1])
point3 = (point2[0], point2[1] + step * 2)
point4 = (point3[0], point3[1] + step * 2)
point5 = (point4[0] + step * 2, point4[1])

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(300). \
    move_to(x=point2[0], y=point2[1]).wait(300). \
    move_to(x=point3[0], y=point3[1]).wait(300). \
    move_to(x=point4[0], y=point4[1]).wait(300). \
    move_to(x=point5[0], y=point5[1]).wait(300). \
    release().perform().release()

driver.find_element_by_id("com.kalading.engineers:id/right_btn").click()

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(300). \
    move_to(x=point2[0], y=point2[1]).wait(300). \
    move_to(x=point3[0], y=point3[1]).wait(300). \
    move_to(x=point4[0], y=point4[1]).wait(300). \
    move_to(x=point5[0], y=point5[1]).wait(300). \
    release().perform()

driver.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()

element = driver.find_element_by_id("com.kalading.engineers:id/gesturepwd_unlock_lockview")
size = element.size  # 打印定位到的元素的长宽
step = int(size["width"] / 6)
ori = element.location  # 元素起点坐标
point1 = (ori["x"] + step, ori["y"] + step)
point2 = (point1[0] + step * 2, point1[1])
point3 = (point2[0], point2[1] + step * 2)
point4 = (point3[0], point3[1] + step * 2)
point5 = (point4[0] + step * 2, point4[1])
TouchAction(driver).press(x=point1[0], y=point1[1]).wait(300). \
    move_to(x=point2[0], y=point2[1]).wait(300). \
    move_to(x=point3[0], y=point3[1]).wait(300). \
    move_to(x=point4[0], y=point4[1]).wait(300). \
    move_to(x=point5[0], y=point5[1]).wait(300). \
    release().perform()


sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("日常管理")').click()
sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("基本设置")').click()
sleep(2)
driver.find_element_by_id("android:id/button2").click()  # 蓝牙点击取消
sleep(2)
driver.find_element_by_id("com.kalading.engineers:id/tv_blue_list_back").click()  # 点击返回按钮返回注销页面
sleep(2)
driver.find_element_by_id("com.kalading.engineers:id/next").click()  # 点击注销按钮
