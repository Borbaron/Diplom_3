from selenium.webdriver.common.by import By

class FeedLocators:

    ALL_TIME_COUNTER = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
    BUN_FLUR = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")
    CONSTRUCTOR_DROP = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    NEW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__') and contains(@class, 'text_type_digits-large')]")
    TODAY_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")
    IN_WORK_NUMBERS = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")
    NO_ORDERS_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[text()='Все текущие заказы готовы!']")
    CLOSE_ORDER_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    NO_ORDERS_IN_WORK = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul//li[contains(text(), 'Все текущие заказы готовы!')]")
    SPECIFIC_ORDER_IN_WORK = lambda number: (By.XPATH, f"//li[@class='text text_type_digits-default mb-2' and text()='{number}']")
