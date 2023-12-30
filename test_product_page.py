from pages.product_page import ProductObject
import pytest
   
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    page.check_price("£9.99")
    page.check_name_of_product("The shellcoder's handbook")
    page.press_submit_button()
    page.solve_quiz_and_get_code()

def test_guest_can_add_product_to_basket2(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductObject(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")
    
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", 
                                        pytest.param("7", marks=pytest.mark.xfail),
                                  "8,9"])
def test_guest_can_add_product_to_basket3(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductObject(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")
  
    

