from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def should_be_basket_page_url(self):
        assert "/basket/" in self.browser.current_url, "URL shoud contains login."

    def should_be_basket_is_empty_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "basket is not empty PRODUCT"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IS_EMPTY), "basket is not empty TEXT"

    