from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomeView(object):
    for_you_text = (MobileBy.XPATH,'//android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')
    exit_button = (MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonPositive')
    cancel_button = (MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonNegative')
    def __init__(self, driver):
        self.driver = driver

    def verify_home(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.for_you_text))
        return self.driver.find_element(*self.for_you_text).is_displayed()

    def app_exit_confirm(self):
        wait = WebDriverWait(self.driver, 20)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(19)
        self.driver.back()
        wait.until(EC.presence_of_element_located(self.exit_button))
        exit = self.driver.find_element(*self.exit_button)
        exit.click()
        return exit.is_displayed()

    def app_exit_cancel(self):
        wait = WebDriverWait(self.driver, 20)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(19)
        self.driver.back()
        wait.until(EC.presence_of_element_located(self.cancel_button))
        exit = self.driver.find_element(*self.cancel_button)
        exit.click()
        wait.until(EC.presence_of_element_located(self.for_you_text))
        return self.driver.find_element(*self.for_you_text).is_displayed()

    def sign_out_cancel(self):
        wait = WebDriverWait(self.driver, 20)

        # buttons: "Start X-Day Free Trial" and "Sign In
        wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/profilePickerTitle')))
        wait.until(EC.presence_of_element_located((MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView')))
        el1 = self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
        el1.click()
        el1.click()
        wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')
        # time.sleep(3.0)
        # down
        self.driver.keyevent(21)
        self.driver.keyevent(21)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(23)
        self.driver.keyevent(22)
        self.driver.keyevent(22)
        self.driver.keyevent(22)
        time.sleep(1.0)
        self.driver.keyevent(22)
        time.sleep(1.0)
        self.driver.keyevent(22)
        self.driver.keyevent(22)
        self.driver.keyevent(20)
        self.driver.keyevent(23)
        time.sleep(3.0)
        wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonNegative')))
        cancelso = self.driver.find_element(MobileBy.ID, 'com.discovery.dplay.enterprise:id/buttonNegative')
        cancelso.click()
        return cancelso.is_displayed()
