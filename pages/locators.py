from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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