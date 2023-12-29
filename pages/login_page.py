from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It isn't login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"
   
   
   
        # реализуйте проверку на корректный url адрес
        # реализуйте проверку, что есть форма логина
        # реализуйте проверку, что есть форма регистрации на странице