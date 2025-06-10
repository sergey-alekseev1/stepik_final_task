import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_basket(browser):
    browser.get(link)

    # Явное ожидание кнопки "Добавить в корзину"
    wait = WebDriverWait(browser, 10)  # ждать до 10 секунд
    button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")),
        message="Кнопка 'Добавить в корзину' не найдена"
    )

    assert button.is_displayed(), "Кнопка 'Добавить в корзину' не отображается"