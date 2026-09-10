import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_for_visibility(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_clickable_and_click(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        ).click()

    def wait_for_windows(self, number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(number)
        )

    def switch_to_window(self, window_number):
        self.driver.switch_to.window(
            self.driver.window_handles[window_number]
        )

    @allure.step("Переключиться в новое окно")
    def switch_to_new_window(self):
        self.wait_for_windows(2)
        self.switch_to_window(1)

    def wait_for_url(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    def wait_for_url_contains(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(url)
        )

    def get_current_url(self):
        return self.driver.current_url
