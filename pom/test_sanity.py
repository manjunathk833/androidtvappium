from views.profilepicker_view import ProfilePickerView
from views.home_view import HomeView

# driver object is instanciated by pytest wherever it is used, as parameter in this instance

# Test Case 1-Test Profile picker screen

def test_profile_picker(driver):
    profilescreen = ProfilePickerView(driver)
    profile_image_displayed = profilescreen.verify_profile()
    if profile_image_displayed == True:
        assert True
    else:
        assert False

#Test Case 2-Validate Home Screen
def test_nav_home_screen(driver):
    profilescreen = ProfilePickerView(driver)
    for_u = profilescreen.nav_to_home()
    if for_u == True:
        assert True
    else:
        assert False

#Test Case 3-Validate Exit
def test_exit(driver):
    profilescreen = ProfilePickerView(driver)
    for_u = profilescreen.nav_to_home()
    homescreen = HomeView(driver)
    exit = homescreen.app_exit_confirm()
    if exit == True:
        assert True
    else:
        assert False

#Test Case 4: Validate Cancel exit
def test_cancel_exit(driver):
    profilescreen = ProfilePickerView(driver)
    for_u = profilescreen.nav_to_home()
    homescreen = HomeView(driver)
    cancel = homescreen.app_exit_cancel()
    if cancel == True:
        assert True
    else:
        assert False

def test_cancel_signout(driver):
    homescreen = HomeView(driver)
    cancelso = homescreen.sign_out_cancel()
    if cancelso == True:
        assert True
    else:
        assert False


# def test_1(driver):
#     assert True
#
# def test_2(driver):
#     assert False
#
#
# def test_3(driver):
#     assert True
#
#
# def test_4(driver):
#     assert False
#
# def test_5(driver):
#     assert False

