import pytest
from appium import webdriver
import creds
import testrail, os

"""
TestRail integration
"""

def get_testrail_client():
    "Get the TestRail account credentials from the testrail.env file"
    testrail_file = os.path.join(os.path.dirname(__file__), 'creds.py')
    # Get the TestRail Url
    #testrail_url = Conf_Reader.get_value(testrail_file, 'TESTRAIL_URL')
    testrail_url = creds.TESTRAIL_URL
    client = testrail.APIClient(testrail_url)
    # Get and set the TestRail User and Password
    #client.user = Conf_Reader.get_value(testrail_file, 'TESTRAIL_USER')
    client.user = creds.TESTRAIL_USER
    #client.password = Conf_Reader.get_value(testrail_file, 'TESTRAIL_PASSWORD')
    client.password = creds.TESTRAIL_PASSWORD

    return client

def update_testrail(case_id, run_id, result_flag, msg=""):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    # Get the TestRail client account details
    client = get_testrail_client()

    # Update the result in TestRail using send_post function.
    # Parameters for add_result_for_case is the combination of runid and case id.
    # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5
    print('add_result_for_case/%s/%s' % (run_id, case_id))
    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': msg})
        except Exception as e:
            print('Exception in update_testrail() updating TestRail.')
            print('PYTHON SAYS: ')
            print(e)
        else:
            print('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, msg))

    return update_flag


#Update TestRail

#Test Run ID

#
# if result1 is True:
#     msg = "updating for true"
# else:
#     msg = "updating for false"
# update_testrail(case1_id, test_run_id, result1, msg=msg)
# update_testrail(case2_id, test_run_id, result2, msg=msg)
# update_testrail(case1_id, test_run_id, result3, msg=msg)
# update_testrail(case2_id, test_run_id, result4, msg=msg)

APPIUM = 'http://localhost:4723'
@pytest.fixture()
def driver():
    CAPS = {
        'platformName': 'Android',
        'deviceName': 'Android TV',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.discovery.dplay.enterprise',
        'appActivity': 'com.discovery.plus.presentation.activities.TVSplashActivity',
        'noReset': 'true'
    }

    # create a appium driver instance
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )
    yield driver
    driver.quit()


def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result

def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')
    count = 1
    test_run_id = 5
    for i in session.results.values():
        if i.passed:
            result = True
            msg = "updating for Pass"
            case_id = count
            count = count+1
            update_testrail(case_id, test_run_id, result, msg=msg)
        elif i.failed:
            result = False
            msg = "updating for Fail"
            case_id = count
            count = count + 1
            update_testrail(case_id, test_run_id, result, msg=msg)
