import pytest
import allure
from base.base_test import BaseTest
from helpers.fake_data import FakeData


@allure.feature("Text Box Page")
class TestTextBox(BaseTest):

    @allure.title("Fill out the form and verify output data")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", FakeData().generate_fake_data(3))
    def test_text_box(self, data):
        self.text_box_page.open()
        self.text_box_page.enter_fullname(data["full_name"])
        self.text_box_page.enter_user_email(data["user_email"])
        self.text_box_page.enter_current_address(data["current_address"])
        self.text_box_page.enter_permanent_address(data["permanent_address"])
        self.text_box_page.click_submit_button()
        self.text_box_page.check_output(data)
        self.text_box_page.make_screenshot("Success")