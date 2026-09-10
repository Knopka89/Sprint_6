import allure

from pages.main_page import MainPage
from urls import Urls


class TestNavigation:
    @allure.title("Логотип Самоката открывает главную страницу")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_order_page()

        main_page.click_scooter_logo()

        assert main_page.wait_for_scooter_main_page() == Urls.BASE_URL

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert Urls.DZEN_URL in main_page.wait_for_dzen_page()
