from selenium.webdriver.common.by import By

class OrderLocators:

    KONSTRUKTOR_TEXT = (By.XPATH, "//a[@href='/']")
    LENTA_ZAKAZOV_TEXT = (By.XPATH, "//a[@href='/feed']")
    OVERLAY = (By.CSS_SELECTOR, "img.Modal_modal__loading__3534A")
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_DROP = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    INGREDIENT_COUNTER = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']/../div[contains(@class, 'counter_counter__')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")