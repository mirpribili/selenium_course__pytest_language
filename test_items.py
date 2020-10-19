import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    basket = browser.find_elements_by_css_selector("button.btn-primary.btn-add-to-basket")
    assert basket, "Кнопка не найдена"
    # ассерт можно проверить заменив линк на http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_208/
    #там нет кнопки добавить в корзину
