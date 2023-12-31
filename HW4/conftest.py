import pytest
import yaml
# import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from HW4.email_report import sendemail
import requests
import logging

with open(r"testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="function")
def browser():
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def send_email():
    yield
    sendemail()


@pytest.fixture()
def login():
    response = requests.post(testdata["url_login"],
                             data={'username': testdata["login_1"], 'password': testdata["password_1"]})
    if response.status_code == 200:
        return response.json()['token']
