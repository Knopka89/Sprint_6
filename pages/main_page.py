import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
    FAQ_TITLE = [By.XPATH, "//div[text()='Вопросы о важном']"]
    FAQ_QUESTION = [By.ID, "accordion__heading-{}"]
    FAQ_ANSWER = [By.ID, "accordion__panel-{}"]
    TOP_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    SCOOTER_LOGO = [By.XPATH, "//a[@href='/']"]
    YANDEX_LOGO = [By.XPATH, "//a[@href='//yandex.ru']"]

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.open_page(Urls.BASE_URL)
        self.wait_for_load_home_page()
        self.accept_cookies()

    @allure.step("Открыть страницу заказа Самоката")
    def open_order_page(self):
        self.open_page(Urls.ORDER_URL)

    def wait_for_load_home_page(self):
        self.wait_for_visibility(self.FAQ_TITLE)

    def accept_cookies(self):
        cookie_buttons = self.find_elements(self.COOKIE_BUTTON)
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
        self.click_element(question_locator)

    @allure.step("Получить ответ на вопрос номер {question_number}")
    def get_answer_text(self, question_number):
        answer_locator = self.get_answer_locator(question_number)
        answer = self.wait_for_visibility(answer_locator)
        return answer.text

    @allure.step("Нажать кнопку заказа: {button_position}")
    def click_order_button(self, button_position):
        if button_position == "top":
            self.click_element(self.TOP_ORDER_BUTTON)
        else:
            self.click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def wait_for_scooter_main_page(self):
        self.wait_for_url(Urls.BASE_URL)
        return self.get_current_url()

    def wait_for_dzen_page(self):
        self.wait_for_url_contains(Urls.DZEN_URL)
        return self.get_current_url()
