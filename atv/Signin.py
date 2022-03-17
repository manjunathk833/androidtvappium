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
    'deviceName': 'Android TV',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.discovery.dplay.enterprise',
    'appActivity': 'com.discovery.plus.presentation.activities.TVSplashActivity',
    'noReset': 'true'
}


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    # Create dynamic wait instance
    wait = WebDriverWait(driver, 20)

    # find and select go to onboarding
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/debugSkipButton')))
    time.sleep(5.0)
    onbutton = driver.find_element(MobileBy.ID, 'com.discovery.dplay.enterprise:id/debugSkipButton')
    onbutton.click()

    # find and select sign in
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/welcomeSignIn')))
    signinbtn = driver.find_element(MobileBy.ID, 'com.discovery.dplay.enterprise:id/welcomeSignIn')
    signinbtn.click()

    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'e-mail')))
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'e-mail').send_keys('affiliate.skyq.uk.prod@test.com')
    driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@content-desc="password"]').send_keys('Affiliate123!')
    loginbtn = driver.find_element(MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="continue"]')
    driver.keyevent(20)
    driver.keyevent(20)
    driver.keyevent(23)
    time.sleep(10.0)
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/profilePickerTitle')))
finally:
    driver.quit()



