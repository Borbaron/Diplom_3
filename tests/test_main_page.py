import allure
import pytest
from pages.base_page import BasePage
from locators.main_locators import OrderLocators
from selenium.common.exceptions import TimeoutException
from curl import *

class TestOrder:
    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.wait_for_overlay_to_disappear(OrderLocators.OVERLAY) 
        base_page.click_on_element(OrderLocators.LENTA_ZAKAZOV_TEXT)
        base_page.click_on_element(OrderLocators.KONSTRUKTOR_TEXT)
        assert base_page.get_current_url() == main_site

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        base_page = BasePage(driver)
        base_page.wait_for_overlay_to_disappear(OrderLocators.OVERLAY)
        base_page.click_on_element(OrderLocators.LENTA_ZAKAZOV_TEXT)
        assert base_page.get_current_url().endswith("/feed")

    @allure.title("При клике на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingridient_window_open(self, driver):
        base_page = BasePage(driver)
        base_page.wait_for_overlay_to_disappear(OrderLocators.OVERLAY)
        base_page.click_on_element(OrderLocators.INGREDIENT_SAUCE)
        assert base_page.wait_for_element(OrderLocators.INGREDIENT_DETAILS_TITLE)   

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_window(self, driver):
        base_page = BasePage(driver)
        base_page.wait_for_overlay_to_disappear(OrderLocators.OVERLAY)
        base_page.click_on_element(OrderLocators.INGREDIENT_SAUCE)
        base_page.wait_for_element(OrderLocators.INGREDIENT_DETAILS_TITLE)
        base_page.click_on_element(OrderLocators.MODAL_CLOSE_BUTTON)   
        try:
             base_page.wait_for_element_to_disappear(OrderLocators.INGREDIENT_DETAILS_TITLE, timeout=3)
             assert True
        except TimeoutException:
             assert False


    @allure.title("Проверка увеличения счетчика ингредиента")
    def test_increase_ingredient_count(self, driver):
        base_page = BasePage(driver)
        base_page.wait_for_overlay_to_disappear(OrderLocators.OVERLAY)
        initial_count = 0 
        base_page.drag_and_drop(OrderLocators.INGREDIENT_SAUCE, OrderLocators.CONSTRUCTOR_DROP) 
        final_count_element = base_page.wait_for_element(OrderLocators.INGREDIENT_COUNTER, timeout=5)
        final_count = int(final_count_element.text)
        assert final_count == initial_count + 1, f"Expected counter to be 1, but got {final_count}"

