from selenium.webdriver.common.by import By

class LoginLocators:

    ENT_EMAIL = (By.NAME, "name")
    ENT_PASS = (By.NAME, "Пароль")
    ENT_LINK = (By.XPATH, "//button[text()='Войти']")
