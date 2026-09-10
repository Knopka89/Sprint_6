import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    ]
    METRO_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_OPTION = [By.XPATH, "//button[normalize-space()='{}']"]
    PHONE_FIELD = [
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    ]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    RENTAL_TITLE = [By.XPATH, "//div[text()='Про аренду']"]
    DELIVERY_DATE_FIELD = [
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']",
    ]
    RENTAL_PERIOD_DROPDOWN = [By.CLASS_NAME, "Dropdown-control"]
    RENTAL_PERIOD_OPTION = [
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and text()='{}']",
    ]
    COLOR_CHECKBOX = [By.ID, "{}"]
    COMMENT_FIELD = [
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']",
    ]
    ORDER_BUTTON = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    CONFIRM_ORDER_BUTTON = [By.XPATH, "//button[text()='Да']"]
    SUCCESS_MESSAGE = [
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(., 'Заказ оформлен')]",
    ]

    def wait_for_load_customer_form(self):
        self.wait_for_visibility(self.NAME_FIELD)

    def wait_for_load_rental_form(self):
        self.wait_for_visibility(self.DELIVERY_DATE_FIELD)

    def set_name(self, name):
        self.enter_text(self.NAME_FIELD, name)

    def set_surname(self, surname):
        self.enter_text(self.SURNAME_FIELD, surname)

    def set_address(self, address):
        self.enter_text(self.ADDRESS_FIELD, address)

    def set_metro(self, metro):
        self.enter_text(self.METRO_FIELD, metro)
        metro_option = [
            self.METRO_OPTION[0],
            self.METRO_OPTION[1].format(metro),
        ]
        self.wait_for_clickable_and_click(metro_option)

    def set_phone(self, phone):
        self.enter_text(self.PHONE_FIELD, phone)

    @allure.step("Заполнить данные заказчика")
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)

    @allure.step("Перейти ко второму шагу заказа")
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    def set_delivery_date(self, delivery_date):
        self.enter_text(self.DELIVERY_DATE_FIELD, delivery_date)
        self.click_element(self.RENTAL_TITLE)

    def set_rental_period(self, rental_period):
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        rental_period_option = [
            self.RENTAL_PERIOD_OPTION[0],
            self.RENTAL_PERIOD_OPTION[1].format(rental_period),
        ]
        self.click_element(rental_period_option)

    def set_color(self, color):
        color_checkbox = [
            self.COLOR_CHECKBOX[0],
            self.COLOR_CHECKBOX[1].format(color),
        ]
        self.click_element(color_checkbox)

    def set_comment(self, comment):
        self.enter_text(self.COMMENT_FIELD, comment)

    @allure.step("Заполнить данные об аренде")
    def fill_rental_form(
        self,
        delivery_date,
        rental_period,
        color,
        comment,
    ):
        self.set_delivery_date(delivery_date)
        self.set_rental_period(rental_period)
        self.set_color(color)
        self.set_comment(comment)

    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_clickable_and_click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Оформить заказ самоката")
    def create_order(
        self,
        name,
        surname,
        address,
        metro,
        phone,
        delivery_date,
        rental_period,
        color,
        comment,
    ):
        self.wait_for_load_customer_form()
        self.fill_customer_form(name, surname, address, metro, phone)
        self.click_next_button()
        self.wait_for_load_rental_form()
        self.fill_rental_form(
            delivery_date,
            rental_period,
            color,
            comment,
        )
        self.click_order_button()
        self.confirm_order()

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        success_message = self.wait_for_visibility(self.SUCCESS_MESSAGE)
        return success_message.text
