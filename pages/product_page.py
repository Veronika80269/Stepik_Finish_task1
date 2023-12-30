from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import MainPageLocators

class ProductObject(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
       
    def check_price(self, price):
       assert self.is_element_present(*ProductPageLocators.PRICE),"Price is different!"
    
    def check_name_of_product(self, name_of_product):
        fact_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert name_of_product == fact_name, "The name is different!"

    def press_submit_button(self): 
       SUBMIT_BUTTON = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
       SUBMIT_BUTTON.click() 
        
    def check_add_of_product(self, expect_message):
        fact_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        assert expect_message == fact_message, "The message is different!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
        
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"  
