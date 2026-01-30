import pytest
import requests
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from data import Credentials
from pages.login_page import LoginPage
from locators.main_locators import OrderLocators

from curl import *


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для тестов: chrome или firefox",
        choices=["chrome", "firefox"]
    )

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
    
    driver.get(main_site)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    """Фикстура для логина пользователя."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(Credentials.email, Credentials.password)
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(OrderLocators.ORDER_BUTTON)
    )
    
    return login_page