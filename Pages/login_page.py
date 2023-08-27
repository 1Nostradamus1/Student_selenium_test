import time
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginData:
    login_prod = "******"
    password_prod = "**********"

class LocatorsLoginPage:
    loginInput = (By.ID, 'normalLogin_username')
    passwordInput = (By.ID, 'normalLogin_password')


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        loginInput = self.element_is_visible(LocatorsLoginPage.loginInput).send_keys(LoginData.login_prod)
        passwordInput = self.element_is_visible(LocatorsLoginPage.passwordInput)
        passwordInput.send_keys(LoginData.password_prod)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(6)

