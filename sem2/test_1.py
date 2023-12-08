import yaml
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata["address"])


# def test_step1():
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#     btn_selector = "button"
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
#     err_lable = site.find_element("xpath", x_selector3)
#     assert err_lable.text == "401"
def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_step_3(log_xpath, pass_xpath, result_xpath, btn_xpath, site,
                res_log, button_create, description_selector,
                content_selector, button_post, title_selector):
    input1 = site.find_element('xpath', log_xpath)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', pass_xpath)
    input2.send_keys(testdata['password'])
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    btn_create_post = site.find_element('xpath', button_create)
    btn_create_post.click()
    time.sleep(testdata['sleep_time'])
    input_title = site.find_element('xpath', title_selector)
    input_title.send_keys(testdata['title_name'])
    input_description = site.find_element('xpath', description_selector)
    input_description.send_keys(testdata['content_name'])
    input_content = site.find_element('xpath', content_selector)
    input_content.send_keys(testdata['description_name'])
    btn_post_1 = site.find_element('xpath', button_post)
    time.sleep(testdata['sleep_time'])
    btn_post_1.click()
    res_label = site.find_element('xpath', res_log)
    assert res_label.text == 'Create Post'
