from Pages.login_page import FormPage, LoginData
from conftest import driver

class TestFormPage:

    def test_Login_form(self, driver):
        form_page = FormPage(driver, 'https://novosibirsk-drums-stage.soft.study/log-in')
        form_page.open()
        form_page.fill_fields_and_submit()

