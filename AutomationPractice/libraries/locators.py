from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators."""
    SEARCH_BUTTON = (By.NAME, 'submit_search')
    SIGN_IN_LINK = (By.CLASS_NAME, 'login')
    SUBMIT_LOGIN_BUTTON = (By.NAME, 'SubmitLogin')