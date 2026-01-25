from pages.base_page import BasePage
from locators.feed_locators import FeedLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from curl import *

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.feed_url = feed_url
        self.main_site = main_site

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        self.driver.get(self.feed_url)
        self.wait_for_page_load()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(FeedLocators.ALL_TIME_COUNTER)
        )

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        element = self.driver.find_element(*FeedLocators.ALL_TIME_COUNTER)
        return int(element.text)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        counter_element = self.wait_for_element(FeedLocators.TODAY_COUNTER, timeout=10)
        return int(counter_element.text)

    @allure.step("Создать быстрый заказ (булка + ингредиент)")
    def create_quick_order(self):
        self.driver.get(self.main_site)

        with allure.step("Добавить булку в конструктор"):
            self.drag_and_drop(FeedLocators.BUN_FLUR, FeedLocators.CONSTRUCTOR_DROP)
            print("Булка добавлена в конструктор")
        
        with allure.step("Добавить ингредиент в конструктор"):
            self.drag_and_drop(FeedLocators.INGREDIENT_SAUCE, FeedLocators.CONSTRUCTOR_DROP)
            print("Ингредиент добавлен")

        with allure.step("Нажать кнопку оформления заказа"):
            confirm_button = self.wait_for_element(FeedLocators.ORDER_BUTTON)
            confirm_button.click()

        with allure.step("Получить номер созданного заказа"):
            order_number_element = self.wait_for_element(FeedLocators.NEW_ORDER_NUMBER, timeout=15)
            initial_number = order_number_element.text
            print(f"Первоначальный номер в модальном окне: {initial_number}")
        
            if initial_number == '9999':
                print("Ожидаю обновления номера заказа...")
                real_order_number = self.wait_for_order_number_to_change(initial_number, timeout=30)
            else:
                real_order_number = initial_number
        
            print(f"Реальный номер заказа: {real_order_number}")
        
        with allure.step("Закрыть модальное окно заказа"):
            close_button = self.wait_for_element(FeedLocators.CLOSE_ORDER_MODAL, timeout=5)
            close_button.click()
        
        return real_order_number

    @allure.step("Ожидать изменения номера заказа с {initial_number}")
    def wait_for_order_number_to_change(self, initial_number, timeout=30):
        """Ожидает, когда номер заказа в модальном окне изменится."""
        def number_changed(driver):
            try:
                current_element = driver.find_element(*FeedLocators.NEW_ORDER_NUMBER)
                current_number = current_element.text
                return current_number if current_number != initial_number else False
            except:
                return False
    
        new_number = WebDriverWait(self.driver, timeout).until(number_changed)
        return new_number

    @allure.step("Проверить что заказ {order_number} находится в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        """Проверяет, находится ли заказ в разделе 'В работе'."""
        clean_number = order_number.replace('#', '')
        order_locator = FeedLocators.SPECIFIC_ORDER_IN_WORK(clean_number)
        
        try:
            self.wait_for_element(order_locator, timeout=20)
            return True
        except:
            return False
