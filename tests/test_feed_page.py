import pytest
import allure
from pages.feed_page import FeedPage

@allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
def test_order_counter_increases(driver, login_user):    
    login_page = login_user  # Фикстура login_user должна логинить пользователя
    feed_page = FeedPage(driver)

    # 1. Убедитесь что пользователь залогинен
    # Фикстура login_user уже должна это делать, но проверим:
    print("Проверяю авторизацию...")
    
    # 2. Открываем ленту заказов
    feed_page.open_feed_page()
    all_time_counter_before = feed_page.get_all_time_counter()
    print(f"Счетчик до: {all_time_counter_before}")

    # 3. Создаем заказ (теперь пользователь залогинен)
    order_number = feed_page.create_quick_order()
    print(f"Создан заказ №{order_number}")

    # 4. Проверяем
    feed_page.open_feed_page()
    all_time_counter_after = feed_page.get_all_time_counter()
    print(f"Счетчик после: {all_time_counter_after}")
    
    assert all_time_counter_after > all_time_counter_before

@allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
def test_today_counter_increases(driver, login_user):
    """Проверяет, что при создании нового заказа увеличивается счетчик за сегодня."""
    login_page = login_user
    feed_page = FeedPage(driver)

    # 1. Открываем ленту заказов
    feed_page.open_feed_page()
    
    # 2. Получаем начальное значение счетчика за сегодня
    today_counter_before = feed_page.get_today_counter()
    print(f"Счетчик 'За сегодня' до: {today_counter_before}")

    # 3. Создаем новый заказ
    order_number = feed_page.create_quick_order()
    print(f"Создан заказ №{order_number}")

    # 4. Снова открываем ленту и проверяем счетчик
    feed_page.open_feed_page()
    today_counter_after = feed_page.get_today_counter()
    print(f"Счетчик 'За сегодня' после: {today_counter_after}")
    
    # 5. Проверяем увеличение счетчика
    assert today_counter_after > today_counter_before, \
        f"Счетчик за сегодня не увеличился: было {today_counter_before}, стало {today_counter_after}"
    
    print(f"✅ Счетчик 'Выполнено за сегодня' увеличился на {today_counter_after - today_counter_before}")


@allure.title("После оформления заказа его номер появляется в разделе «В работе»")
def test_order_appears_in_work_section(driver, login_user):
    """Проверяет, что номер созданного заказа появляется в разделе 'В работе'."""
    login_page = login_user
    feed_page = FeedPage(driver)

    # Создаем заказ
    order_number = feed_page.create_quick_order()
    print(f"Создан заказ: {order_number}")

    # Открываем ленту
    feed_page.open_feed_page()

    # Проверяем что заказ появился
    assert feed_page.is_order_in_work(order_number), \
        f"Заказ {order_number} не найден в разделе 'В работе'"