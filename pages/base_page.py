import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента с локатором: {locator}")
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента c локатором: {locator}")
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент c локатором: {locator}")
    def click_on_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Перетаскивание элемента {source_locator} в элемент {target_locator} с помощью JavaScript")
    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент из source_locator в target_locator с помощью JavaScript."""
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        self.driver.execute_script("""
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            return event;
        }
        var source = arguments[0];
        var target = arguments[1];
        var dragStartEvent = createEvent('dragstart');
        source.dispatchEvent(dragStartEvent);
        var dragEnterEvent = createEvent('dragenter');
        target.dispatchEvent(dragEnterEvent);
        var dragOverEvent = createEvent('dragover');
        dragOverEvent.preventDefault = function () { };
        target.dispatchEvent(dragOverEvent);
        var dropEvent = createEvent('drop');
        target.dispatchEvent(dropEvent);
        var dragEndEvent = createEvent('dragend');
        source.dispatchEvent(dragEndEvent);
        """, source, target)

    @allure.step("Получить текст элемента c локатором: {locator}")
    def get_text_on_element(self, locator, timeout=20):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step("Подождать пока оверлей исчезнет")
    def wait_for_overlay_to_disappear(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание, пока элемент станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ждать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Не дождались исчезновения элемента за {timeout} секунд")
