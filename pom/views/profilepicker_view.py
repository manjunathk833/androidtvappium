from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePickerView(object):
    #class variables

    # for network_image
    profile_image = (MobileBy.ID, 'com.discovery.dplay.enterprise:id/profilePickerTitle')
    cur_profile_image = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView')
    for_you_text = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="For You"]/android.widget.TextView')
    def __init__(self, driver):
        self.driver = driver


    def verify_profile(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.profile_image))
        wait.until(EC.presence_of_element_located(self.cur_profile_image))
        return self.driver.find_element(*self.cur_profile_image).is_displayed()

    def nav_to_home(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.profile_image))
        wait.until(EC.presence_of_element_located(self.cur_profile_image))
        el1 = self.driver.find_element(*self.cur_profile_image)
        el1.click()
        el1.click()
        wait.until(EC.presence_of_element_located(self.for_you_text))
        return self.driver.find_element(*self.for_you_text).is_displayed()

    def nav_back(self):
        None