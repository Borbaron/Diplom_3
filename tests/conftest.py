import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from data import Credentials
from pages.login_page import LoginPage


from curl import *


@pytest.fixture(params=["firefox", "chrome"], scope="function")
def driver(request):
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome()
    
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
    
    # Открываем страницу логина
    login_page.open_login_page()
    
    # Выполняем логин
    login_page.login(Credentials.email, Credentials.password)
    
    # Ждем кнопку "Оформить заказ" с увеличенным таймаутом
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )
    
    return login_page