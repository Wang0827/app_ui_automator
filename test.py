from appium import webdriver
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.kalading.engineers'
desired_caps['appActivity'] = 'com.kalading.engineers.MainActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.kalading.engineers:id/getback_password_phonenum").send_keys("13072902013")
driver.find_element_by_id("com.kalading.engineers:id/getback_password_codes").send_keys("111111")
driver.find_element_by_id("com.kalading.engineers:id/getback_password_submit").click()  # 输入密码登录
driver.implicitly_wait(10)
driver.find_element_by_id("com.kalading.engineers:id/gesturepwd_guide_btn").click()  # 点击下一步
driver.find_element_by_id("com.kalading.engineers:id/right_btn").click()  # 点击下一步
driver.find_element_by_id("com.kalading.engineers:id/left_btn").click()  # 点击取消
driver.find_element_by_android_uiautomator('new UiSelector().text("日常管理")').click()
sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("基本设置")').click()
sleep(2)
driver.find_element_by_id("android:id/button2").click()  # 蓝牙点击取消
sleep(2)
driver.find_element_by_id("com.kalading.engineers:id/tv_blue_list_back").click()  # 点击返回按钮返回注销页面
sleep(2)
driver.find_element_by_id("com.kalading.engineers:id/next").click()  # 点击注销按钮
