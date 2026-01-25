from pages.base_page import BasePage
import allure
from curl import *
from locators.login_locators import LoginLocators
from locators.main_locators import OrderLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = login_url

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.driver.get(self.login_url)

    @allure.step("Ввести логин и пароль и нажать кнопку 'Войти'")
    def login(self, email, password):
        self.wait_for_overlay_to_disappear(OrderLocators.OVERLAY, timeout=10)
        self.driver.find_element(*LoginLocators.ENT_EMAIL).send_keys(email)
        self.driver.find_element(*LoginLocators.ENT_PASS).send_keys(password)
        self.driver.find_element(*LoginLocators.ENT_LINK).click()



