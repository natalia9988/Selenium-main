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
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
# залогинится
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

# создания поста
    testpage.click_nwe_post_button()
    testpage.enter_title_post("new title")
    testpage.enter_content_post("content")
    testpage.click_create_nwe_post_button()

    time.sleep(3)

# Проверка наличия названия поста на странице
    assert testpage.post() == "new title"