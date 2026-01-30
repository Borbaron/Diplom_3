import pytest
import allure
from pages.feed_page import FeedPage

@allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
def test_order_counter_increases(driver, login_user):    
    login_page = login_user 
    feed_page = FeedPage(driver)
    feed_page.open_feed_page()
    all_time_counter_before = feed_page.get_all_time_counter()
    order_number = feed_page.create_quick_order()
    feed_page.open_feed_page()
    all_time_counter_after = feed_page.get_all_time_counter()
    
    assert all_time_counter_after > all_time_counter_before

@allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
def test_today_counter_increases(driver, login_user):
    login_page = login_user
    feed_page = FeedPage(driver)
    feed_page.open_feed_page()
    today_counter_before = feed_page.get_today_counter()
    order_number = feed_page.create_quick_order()
    feed_page.open_feed_page()
    today_counter_after = feed_page.get_today_counter()

    assert today_counter_after > today_counter_before, \
        f"Счетчик за сегодня не увеличился: было {today_counter_before}, стало {today_counter_after}"


@allure.title("После оформления заказа его номер появляется в разделе «В работе»")
def test_order_appears_in_work_section(driver, login_user):
    login_page = login_user
    feed_page = FeedPage(driver)
    order_number = feed_page.create_quick_order()
    feed_page.open_feed_page()

    assert feed_page.is_order_in_work(order_number), \
        f"Заказ {order_number} не найден в разделе 'В работе'"