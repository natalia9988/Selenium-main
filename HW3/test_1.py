from testpage import OperationsHelper
import logging
import yaml
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


#

def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
    # залогинится
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    # создания поста
    testpage.click_new_post_button()
    testpage.enter_title_post(testdata["title_name"])
    testpage.enter_description_post(testdata["description_name"])
    testpage.enter_content_post(testdata["content_name"])
    testpage.click_create_new_post_button()
    time.sleep(3)
    testpage.go_to_site()

    # Проверка наличия названия поста на странице
    assert testpage.post() == "Blog"


def test_step_4(browser):
    logging.info("Test 4 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact()
    time.sleep(testdata["sleep_time"])
    testpage.contact_us_name(testdata["your_name"])
    testpage.contact_us_email(testdata["your_email"])
    testpage.contact_us_content(testdata["your_content"])
    testpage.click_contact_us()
    time.sleep(testdata["sleep_time"])
    assert testpage.alert() == 'Form successfully submitted'
