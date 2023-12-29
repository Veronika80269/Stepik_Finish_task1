from pages.product_page import ProductObject
   
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductObject(browser, link)
    page.open()
    page.check_price("£9.99")
    page.check_name_of_product("The shellcoder's handbook")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    
