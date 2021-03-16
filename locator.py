from selenium.webdriver.common.by import By

class HomePageLocator(object):
    #navbar
    NAVBAR = (By.XPATH, "//nav[@class='container flex-start']")
    SERVICES_NAV = (By.XPATH, "//nav[@class='container flex-start']//a[2]//span")
    TRAMSFERS_NAV = (By.XPATH, "//nav[@class='container flex-start']//a[3]//span")
    BUSINESS_NAV = (By.XPATH, "//nav[@class='container flex-start']//a[4]//span")
    ABROAD_NAV = (By.XPATH, "//nav[@class='container flex-start']//a[5]//span")

    #sidebar 
    SIDEBAR = (By.XPATH, "//div[@class='flex-start']//ul")
    POPULAR_SERVICES = (By.XPATH, "//div[@class='flex-start']//ul//li[1]//a//div[@class='text-container']")
    MOBILE_CONNECTIONS = (By.XPATH, "//div[@class='flex-start']//ul//li[2]//a//div[@class='text-container']")
    BANKS_INSURANCE_MICROFINANCE = (By.XPATH, "//div[@class='flex-start']//ul//li[3]//a//div[@class='text-container']")
    BOOKMAKERS_CASINO_LOTTERY = (By.XPATH, "//div[@class='flex-start']//ul//li[4]//a//div[@class='text-container']")
    INTERNET_TELEPHONE_TELEVISION = (By.XPATH, "//div[@class='flex-start']//ul//li[5]//a//div[@class='text-container']")
    UTILITY_PAYMENTS = (By.XPATH, "//div[@class='flex-start']//ul//li[6]//a//div[@class='text-container']")
    TRANSPORT = (By.XPATH, "//div[@class='flex-start']//ul//li[7]//a//div[@class='text-container']")
    STATE_SERVICES = (By.XPATH, "//div[@class='flex-start']//ul//li[8]//a//div[@class='text-container']")
    OTHER_SERVICES = (By.XPATH, "//div[@class='flex-start']//ul//li[9]//a//div[@class='text-container']")

    #searchbar
    SEARCHBAR = (By.NAME, "searchWord")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # TOP UP
    MOBILE_TOP_UP = (By.XPATH, "//a[contains(@title, 'მობილური ბალანსის შევსება')]")

class TopUpPageLocator(object):
    NUMBER_INPUT = (By.XPATH, "//input[@name='1213-abonentCode']")
    CHECK_BUTTON = (By.XPATH, "//button[@type='submit']")

    SELECT_SERVICE = (By.XPATH, "//div[@class='select-input ']")
    
    LIST_TOP_UP_BALANCE = (By.XPATH, "//div[@class = 'options']//a[2]//span")
    LIST_METI_8 = (By.XPATH, "//div[@class = 'options']//a[3]//span")
    LIST_METI_10 = (By.XPATH, "//div[@class = 'options']//a[4]")
    # saxelebit povna
    # LIST_TOP_UP_BALANCE = (By.XPATH, "//a[contains(@title, 'ბალანსის შევსება')]")
    # LIST_METI_8 = (By.XPATH, '//a[contains(@title, `"მეტი" - 8 ₾`)]')
    # LIST_METI_10 = (By.XPATH, '//a[contains(@title, `"მეტი" - 10 ₾`)]')

    # FINAL
    DEBT_TEXT = (By.XPATH, "//div[contains(@class, 'main-block')]//div[1]//small//span")
    DEBT_AMOUNT = (By.XPATH, "//p[@class='debt']")
    DEBT_AMOUNT_SYMBOL = (By.XPATH, "//p[@class='debt']//span")

    MONEY_AMOUNT_TEXT = (By.XPATH, "//div[contains(@class, 'main-block')]//div[2]//small//span[1]")
    MONEY_AMOUNT_SYMBOL = (By.XPATH, "//div[contains(@class, 'main-block')]//div[2]//small//span[2]")
    MONEY_AMOUNT = (By.XPATH, "//input[@name='1327']")

    COMMISION_TEXT = (By.XPATH, "//div[contains(@class, 'main-block')]//div[3]//small//span[1]")
    COMMISION_AMOUNT = (By.XPATH, "//button[contains(@class, 'commission ')]//span[1]")
    COMMISION_SYMBOL = (By.XPATH, "//button[contains(@class, 'commission ')]//span[2]")

    TOTAL_TEXT = (By.XPATH, "//div[@class='info']//small//span")
    TOTAL_AMOUNT = (By.XPATH, "//div[@class='info']//b")
    TOTAL_AMOUNT_SYMBOL = (By.XPATH, "//div[@class='info']//b//span")

    PAY_BUTTON = (By.XPATH, "//button[contains(@class, 'pay-btn')]")
    PAY_BUTTON_TEXT = (By.XPATH, "//button[contains(@class, 'pay-btn')]//span")

