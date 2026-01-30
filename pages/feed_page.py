from pages.base_page import BasePage
from locators.feed_locators import FeedLocators
from locators.main_locators import OrderLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.feed_url = feed_url
        self.main_site = main_site

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        self.open_url(self.feed_url)
        self.wait_for_page_load()
        self.wait_for_element(FeedLocators.ALL_TIME_COUNTER, timeout=10)

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        element = self.wait_for_element(FeedLocators.ALL_TIME_COUNTER)
        return int(element.text)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        counter_element = self.wait_for_element(FeedLocators.TODAY_COUNTER, timeout=10)
        return int(counter_element.text)

    @allure.step("Создать быстрый заказ (булка + ингредиент)")
    def create_quick_order(self):
        self.open_url(self.main_site)

        with allure.step("Добавить булку в конструктор"):
            self.drag_and_drop(FeedLocators.BUN_FLUR, FeedLocators.CONSTRUCTOR_DROP)

        with allure.step("Добавить ингредиент в конструктор"):
            self.drag_and_drop(FeedLocators.INGREDIENT_SAUCE, FeedLocators.CONSTRUCTOR_DROP)

        with allure.step("Нажать кнопку оформления заказа"):
            confirm_button = self.wait_for_element(FeedLocators.ORDER_BUTTON)
            confirm_button.click()

        with allure.step("Получить номер созданного заказа"):
            self.wait_for_element_to_disappear(FeedLocators.ORDER_NUMBER_PLACEHOLDER)

            order_number_element = self.wait_for_element(FeedLocators.NEW_ORDER_NUMBER, timeout=15)
            real_order_number = order_number_element.text

        with allure.step("Закрыть модальное окно заказа"):
            self.wait_for_overlay_to_disappear(OrderLocators.OVERLAY, timeout=20)
            close_button = self.wait_for_element(FeedLocators.CLOSE_ORDER_MODAL, timeout=30)
            close_button.click()

        return real_order_number

    @allure.step("Проверить что заказ {order_number} находится в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        clean_number = order_number.replace('#', '')
        order_locator = FeedLocators.specific_order_in_work(clean_number)

        try:
            self.wait_for_element(order_locator, timeout=20)
            return True
        except:
            return False