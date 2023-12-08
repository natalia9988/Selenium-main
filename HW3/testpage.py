from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


# класс поиска локаторов
class TestSearchLocators:
    # — локатор поля ввода логина
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    # — локатор поля ввода пароля
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # — локатор кнопки логина
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    # — локатор поля с ошибкой
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_CREATE_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_RES_CREATE = (By.XPATH, """//*[@id="app"]/main/div/div[3]/div[1]/a/h2""")
    LOCATOR_HOME = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_YOUR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


# класс с методами (действиями с локаторами из файла test_1)

class OperationsHelper(BasePage):
    # функция ввода логина
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    # функция ввода пароля
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    # функция нажатия кнопки login
    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    # функция вывода текста (в нашем случае 401)
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_text_blog(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
        text = text_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
        return text

    def click_new_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description_post(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_create_new_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST, time=2)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST[1]}")
        return text

    def click_contact(self):
        logging.info('Click contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def contact_us_name(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        title_field.clear()
        title_field.send_keys(word)

    def contact_us_email(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        title_field.clear()
        title_field.send_keys(word)

    def contact_us_content(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_CONTENT[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT)
        title_field.clear()
        title_field.send_keys(word)

    def click_contact_us(self):
        logging.info('Click create contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def alert(self):
        alert = self.driver.switch_to.alert
        return alert.text
