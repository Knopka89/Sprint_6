import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:
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

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_customer_form(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.NAME_FIELD
            )
        )

    def wait_for_load_rental_form(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.DELIVERY_DATE_FIELD
            )
        )

    def set_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def set_metro(self, metro):
        self.driver.find_element(*self.METRO_FIELD).send_keys(metro)
        metro_option = [
            self.METRO_OPTION[0],
            self.METRO_OPTION[1].format(metro),
        ]
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(metro_option)
        ).click()

    def set_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    @allure.step("Заполнить данные заказчика")
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)

    @allure.step("Перейти ко второму шагу заказа")
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def set_delivery_date(self, delivery_date):
        self.driver.find_element(*self.DELIVERY_DATE_FIELD).send_keys(delivery_date)
        self.driver.find_element(*self.RENTAL_TITLE).click()

    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN).click()
        rental_period_option = [
            self.RENTAL_PERIOD_OPTION[0],
            self.RENTAL_PERIOD_OPTION[1].format(rental_period),
        ]
        self.driver.find_element(*rental_period_option).click()

    def set_color(self, color):
        color_checkbox = [
            self.COLOR_CHECKBOX[0],
            self.COLOR_CHECKBOX[1].format(color),
        ]
        self.driver.find_element(*color_checkbox).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

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
        self.driver.find_element(*self.ORDER_BUTTON).click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                self.CONFIRM_ORDER_BUTTON
            )
        ).click()

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
        success_message = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )
        return success_message.text
