import allure
import pytest

from conftest import driver
from data import comment, TestUrl
from helpers import info_client, about_scooter_rent
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.step('Тестируем оформление заказа с валидными данными')
    @pytest.mark.parametrize('button',
                             [MainPageLocators.order_button_down,
                              MainPageLocators.order_button_up],
                             )
    def test_created_order(self, driver, button):
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        main_page.created_order(button)
        order_page = OrderPage(driver)
        order_page.fill_form_about_info_client(
            name=info_client['name'],
            last_name=info_client['last_name'],
            address=info_client['address'],
            metro=info_client['metro'],
            phone=info_client['phone']
        )
        order_page.fill_form_about_rent(
            rent_day=about_scooter_rent['rent_day'],
            colour=about_scooter_rent['colour'],
            comment=comment
        )
        order_page.click_button_order_finall()
        order_page.confirmation_order()
        assert 'Заказ оформлен' in order_page.check_accept_order()




