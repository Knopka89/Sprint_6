import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import Urls


class MainPage:
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
    FAQ_TITLE = [By.XPATH, "//div[text()='Вопросы о важном']"]
    FAQ_QUESTION = [By.ID, "accordion__heading-{}"]
    FAQ_ANSWER = [By.ID, "accordion__panel-{}"]
    TOP_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    SCOOTER_LOGO = [By.XPATH, "//a[@href='/']"]
    YANDEX_LOGO = [By.XPATH, "//a[@href='//yandex.ru']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_load_home_page()
        self.accept_cookies()

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.FAQ_TITLE)
        )

    def accept_cookies(self):
        cookie_buttons = self.driver.find_elements(*self.COOKIE_BUTTON)
        if cookie_buttons and cookie_buttons[0].is_displayed():
            cookie_buttons[0].click()

    def get_question_locator(self, question_number):
        return [
            self.FAQ_QUESTION[0],
            self.FAQ_QUESTION[1].format(question_number),
        ]

    def get_answer_locator(self, question_number):
        return [
            self.FAQ_ANSWER[0],
            self.FAQ_ANSWER[1].format(question_number),
        ]

    @allure.step("Открыть вопрос номер {question_number}")
    def click_question(self, question_number):
        question_locator = self.get_question_locator(question_number)
        self.driver.find_element(*question_locator).click()

    @allure.step("Получить ответ на вопрос номер {question_number}")
    def get_answer_text(self, question_number):
        answer_locator = self.get_answer_locator(question_number)
        answer = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(answer_locator)
        )
        return answer.text

    @allure.step("Нажать кнопку заказа: {button_position}")
    def click_order_button(self, button_position):
        if button_position == "top":
            self.driver.find_element(*self.TOP_ORDER_BUTTON).click()
        else:
            self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()

    @allure.step("Переключиться в новое окно")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.number_of_windows_to_be(2)
        )
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_scooter_main_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(Urls.BASE_URL)
        )
        return self.driver.current_url

    def wait_for_dzen_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(Urls.DZEN_URL)
        )
        return self.driver.current_url
