from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, ".basket-items")
    TEXT_IS_EMPTY = (By.CSS_SELECTOR, "#messages")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WATCH_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")

class LoginPageLocators():
    PART_URL = "login"
    #Подберите селекторы к формам регистрации и логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASS = (By.CSS_SELECTOR, 'input[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    NEW_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    NEW_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_NEW_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")

    
class ProductPageLocators():
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR,"div.product_main h1")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alert:nth-child(1)")



