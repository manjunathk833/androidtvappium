from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'dplus_emea-androidTV-v15.1.0_ENTERPRISE-vc1604874021.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'AOSP TV on x86',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.discovery.dplay.enterprise',
    'appActivity': 'com.discovery.plus.presentation.activities.TVSplashActivity',
    'noReset': 'true'
}


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

#Test Case 1 App launch and navigate to home screen for a sign in user
# try:
#     # Create dynamic wait instance
#     wait = WebDriverWait(driver, 20)
#
#     # buttons: "Start X-Day Free Trial" and "Sign In
#     wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/profilePickerTitle')))
#     driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]').click()
#
#     wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')))
#
# finally:
#     driver.quit()


try:
    # Create dynamic wait instance
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[2]')))
    time.sleep(10.0)
    driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[2]').click()
    wait.until(EC.presence_of_element_located((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[2]')))
    driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[2]').click()

    # # wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/profilePickerTitle')))
    # # driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]').click()

    wait.until(EC.presence_of_element_located((MobileBy.ID, '/android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')))
    # driver.back()
    # driver.back()
    # wait.until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[1]')))
    # driver.back()
    # wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonPositive')))
    # driver.find_element(MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonPositive').click()

finally:
    driver.quit()



