from selenium import webdriver
import unittest
import page
from locator import *
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"

class MainPageNavTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(DRIVER_PATH)
        cls.driver.get("https://tbcpay.ge/")

    def test_navBar(self):
        homePage = page.HomePage
        assert homePage.is_navBar_found(self)

    def test_services(self):
        homePage = page.HomePage
        assert homePage.is_services_matches(self)

    def test_transfers(self):
        homePage = page.HomePage
        assert homePage.is_transfers_matches(self)

    def test_business(self):
        homePage = page.HomePage
        assert homePage.is_business_matches(self)

    def test_abroad(self):
        homePage = page.HomePage
        assert homePage.is_abroad_matches(self)

    def tearDown(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

class MainPageSideNavTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(DRIVER_PATH)
        cls.driver.get("https://tbcpay.ge/")
        cls.homePage = page.HomePage(cls.driver)

    def test_sidebar(self):
        assert self.homePage.is_sidebar_found()
    def test_popular_services(self):
        assert self.homePage.is_popular_services_found()
    def test_mobile_connections(self):
        assert self.homePage.is_mobile_connections_found()
    def test_banks_insurance_microfinance(self):
        assert self.homePage.is_banks_insurance_microfinance_found()
    def test_bookmakers_casino_lottery(self):
        assert self.homePage.is_bookmakers_casino_lottery_found()
    def test_internet_telephone_television(self):
        assert self.homePage.is_internet_telephone_television_found()
    def test_utility_payments(self):
        assert self.homePage.is_utility_payments_found()
    def test_transfers(self):
        assert self.homePage.is_transport_found()
    def test_state_services(self):
        assert self.homePage.is_state_services_found()
    def test_other_services(self):
        assert self.homePage.is_other_services_found()

    def tearDown(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

class BalanceTopUpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(DRIVER_PATH)
        cls.driver.get("https://tbcpay.ge/")
        #cls.driver.maximize_window()
        cls.topUpPage = page.TopUpPage(cls.driver)

    def test_00_search_result(self):
        homePage = page.HomePage(self.driver)
        homePage.search_bar_element = "მობილური"
        assert homePage.is_result_found()
        homePage.click_topUp_button()
    
    def test_01_check_button(self):
        assert self.topUpPage.is_check_button_found()
    def test_02_input(self):
        assert self.topUpPage.is_num_input_found()

    def test_03_select_list_items(self):
        self.topUpPage.num_input_element = "555122334"
        self.topUpPage.click_check_button()
        assert self.topUpPage.is_select_service_found()

    def test_04_balance_top_up(self):
        self.topUpPage.click_select_service_button()
        assert self.topUpPage.is_top_up_balance_found()

    def test_05_meti_8(self):
        assert self.topUpPage.is_meti_8_found()

    def test_06_meti_10(self):
        assert self.topUpPage.is_meti_10_found()

    def test_07_select_meti_10(self):
        self.topUpPage.click_meti_10_button()
        assert self.topUpPage.is_debt_text_matches()

    def test_08_debt(self):
        assert self.topUpPage.is_debt_matches()

    def test_09_money_amount_text(self):
        assert self.topUpPage.is_money_amount_text_matches()
    def test_10_money_input(self):
        assert self.topUpPage.is_money_input_matches()

    def test_11_commision_text(self):
        assert self.topUpPage.is_commision_text_matches()
    def test_12_commision(self):
        assert self.topUpPage.is_commision_matches()

    def test_13_total_text(self):
        assert self.topUpPage.is_text_total_matches()
    def test_14_total_text(self):
        assert self.topUpPage.is_total_matches()

    def test_15_pay_button(self):
        assert self.topUpPage.is_pay_button_matches()
    
    def test_16_pay_redirect(self):
        self.topUpPage.click_pay_button()
        WebDriverWait(self.driver, 5).until(EC.url_changes(self.driver.current_url))
        assert "ecommerce.ufc.ge" in self.driver.current_url


    def setUp(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot_start", attachment_type=AttachmentType.PNG)
    def tearDown(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot_end", attachment_type=AttachmentType.PNG)


    @classmethod
    def tearDownClass(cls):
        pass
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()