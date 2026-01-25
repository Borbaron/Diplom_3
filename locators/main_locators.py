from selenium.webdriver.common.by import By

class OrderLocators:

    KONSTRUKTOR_TEXT = (By.XPATH, "//a[@href='/']")
    LENTA_ZAKAZOV_TEXT = (By.XPATH, "//a[@href='/feed']")
    OVERLAY = (By.XPATH, "/html/body/div/div/div/img")
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_DROP = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    INGREDIENT_COUNTER = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']/../div[contains(@class, 'counter_counter__')]")




