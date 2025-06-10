import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr, etc.")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\n[INFO] Запуск Chrome с языком: '{user_language}'")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print(f"\n[INFO] Запуск Firefox с языком: '{user_language}'")
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name должен быть 'chrome' или 'firefox'")

    yield browser
    print("\n[INFO] Закрытие браузера")
    if browser:
        browser.quit()
