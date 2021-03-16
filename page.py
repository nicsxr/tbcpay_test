from locator import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class SearchBarElement(BasePageElement):
    locator = "searchWord"

class NumberInputElement(BasePageElement):
    locator = "1213-abonentCode"

class HomePage(BasePage):

    def is_navBar_found(self):
        return self.driver.find_element(*HomePageLocator.NAVBAR)
    def is_services_matches(self):
        return "სერვისები" == self.driver.find_element(*HomePageLocator.SERVICES_NAV).get_attribute("innerHTML")
    def is_transfers_matches(self):
        return "გადარიცხვები" == self.driver.find_element(*HomePageLocator.TRAMSFERS_NAV).get_attribute("innerHTML")
    def is_business_matches(self):
        return "ბიზნესისთვის" == self.driver.find_element(*HomePageLocator.BUSINESS_NAV).get_attribute("innerHTML")
    def is_abroad_matches(self):
        return "გადაიხადე უცხოეთიდან" == self.driver.find_element(*HomePageLocator.ABROAD_NAV).get_attribute("innerHTML")

    def is_sidebar_found(self):
        return self.driver.find_element(*HomePageLocator.SIDEBAR)
    def is_popular_services_found(self):
        return self.driver.find_element(*HomePageLocator.POPULAR_SERVICES)
    def is_mobile_connections_found(self):
        return self.driver.find_element(*HomePageLocator.MOBILE_CONNECTIONS)
    def is_banks_insurance_microfinance_found(self):
        return self.driver.find_element(*HomePageLocator.BANKS_INSURANCE_MICROFINANCE)
    def is_bookmakers_casino_lottery_found(self):
        return self.driver.find_element(*HomePageLocator.BOOKMAKERS_CASINO_LOTTERY)
    def is_internet_telephone_television_found(self):
        return self.driver.find_element(*HomePageLocator.INTERNET_TELEPHONE_TELEVISION)
    def is_utility_payments_found(self):
        return self.driver.find_element(*HomePageLocator.UTILITY_PAYMENTS)
    def is_transport_found(self):
        return self.driver.find_element(*HomePageLocator.TRANSPORT)
    def is_state_services_found(self):
        return self.driver.find_element(*HomePageLocator.STATE_SERVICES)
    def is_other_services_found(self):
        return self.driver.find_element(*HomePageLocator.OTHER_SERVICES)

    search_bar_element = SearchBarElement()

    def click_topUp_button(self):
        element = self.driver.find_element(*HomePageLocator.MOBILE_TOP_UP)
        element.click()

    def is_result_found(self):
        return self.driver.find_element(*HomePageLocator.MOBILE_TOP_UP)



class TopUpPage(BasePage):
    num_input_element = NumberInputElement()

    def is_check_button_found(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(TopUpPageLocator.CHECK_BUTTON))
        return self.driver.find_element(*TopUpPageLocator.CHECK_BUTTON)

    def is_num_input_found(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(TopUpPageLocator.NUMBER_INPUT))
        return self.driver.find_element(*TopUpPageLocator.NUMBER_INPUT)


    def is_select_service_found(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(TopUpPageLocator.SELECT_SERVICE))
        return self.driver.find_element(*TopUpPageLocator.SELECT_SERVICE)


    # LIST ITEMS
    def is_top_up_balance_found(self):
        return self.driver.find_element(*TopUpPageLocator.LIST_TOP_UP_BALANCE)
    def is_meti_8_found(self):
        return self.driver.find_element(*TopUpPageLocator.LIST_METI_8)
    def is_meti_10_found(self):
        return self.driver.find_element(*TopUpPageLocator.LIST_METI_10)


    # ACTIONS
    def click_select_service_button(self):
        element = self.driver.find_element(*TopUpPageLocator.SELECT_SERVICE)
        element.click()

    def click_check_button(self):
        element = self.driver.find_element(*TopUpPageLocator.CHECK_BUTTON)
        element.click()
        self.driver.find_element(*TopUpPageLocator.NUMBER_INPUT).send_keys("\n")

    def click_meti_10_button(self):
        element = self.driver.find_element(*TopUpPageLocator.LIST_METI_10)
        element.click()

    # FINAl
    def is_debt_matches(self):
        return "10.00" == self.driver.find_element(*TopUpPageLocator.DEBT_AMOUNT).get_attribute("innerHTML")[:5] and "c" == self.driver.find_element(*TopUpPageLocator.DEBT_AMOUNT_SYMBOL).get_attribute("innerHTML")
    def is_debt_text_matches(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(TopUpPageLocator.DEBT_TEXT))
        return "დავალიანება" == self.driver.find_element(*TopUpPageLocator.DEBT_TEXT).get_attribute("innerHTML")

    def is_money_amount_text_matches(self):
        return "თანხის ოდენობა" == self.driver.find_element(*TopUpPageLocator.MONEY_AMOUNT_TEXT).get_attribute("innerHTML")
    def is_money_input_matches(self):
        return "10" == self.driver.find_element(*TopUpPageLocator.MONEY_AMOUNT).get_attribute("value") and "c" == self.driver.find_element(*TopUpPageLocator.MONEY_AMOUNT_SYMBOL).get_attribute("innerHTML")


    def is_commision_matches(self):
        return "0.12" == self.driver.find_element(*TopUpPageLocator.COMMISION_AMOUNT).get_attribute("innerHTML") and "c" == self.driver.find_element(*TopUpPageLocator.COMMISION_SYMBOL).get_attribute("innerHTML")
    
    def is_commision_text_matches(self):
        return "საკომისიო" == self.driver.find_element(*TopUpPageLocator.COMMISION_TEXT).get_attribute("innerHTML")

    def is_total_matches(self):
        return "10.12" == self.driver.find_element(*TopUpPageLocator.TOTAL_AMOUNT).get_attribute("innerHTML")[:5] and "c" == self.driver.find_element(*TopUpPageLocator.TOTAL_AMOUNT_SYMBOL).get_attribute("innerHTML")
    def is_text_total_matches(self):
        return "ჯამში გადასახდელი" == self.driver.find_element(*TopUpPageLocator.TOTAL_TEXT).get_attribute("innerHTML")

    def is_pay_button_matches(self):
        return "გადახდა" == self.driver.find_element(*TopUpPageLocator.PAY_BUTTON_TEXT).get_attribute("innerHTML")

    def click_pay_button(self):
        element = self.driver.find_element(*TopUpPageLocator.PAY_BUTTON)
        element.click()