import allure
import pytest

from data import TestData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize(
        (
            "order_button, name, surname, address, metro, phone, "
            "delivery_date, rental_period, color, comment"
        ),
        TestData.ORDER_DATA,
    )
    def test_successful_order(
        self,
        driver,
        order_button,
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
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.create_order(
            name,
            surname,
            address,
            metro,
            phone,
            delivery_date,
            rental_period,
            color,
            comment,
        )

        assert "Заказ оформлен" in order_page.get_success_message()
