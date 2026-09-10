import allure
import pytest

from data import TestData
from pages.main_page import MainPage


class TestFaq:
    @allure.title("Проверка ответа в разделе «Вопросы о важном»")
    @pytest.mark.parametrize(
        "question_number, expected_answer",
        TestData.FAQ_DATA,
    )
    def test_question_opens_correct_answer(
        self,
        driver,
        question_number,
        expected_answer,
    ):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_question(question_number)
        actual_answer = main_page.get_answer_text(question_number)

        assert actual_answer == expected_answer
