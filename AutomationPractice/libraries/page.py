from element import BasePageElementByName
from locators import MainPageLocators

class SearchTextElement(BasePageElementByName):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'search_query'

class EmailElement(BasePageElementByName):
    locator = 'email'

class PasswordElement(BasePageElementByName):
    locator = 'passwd'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
       self.driver = driver

class MainPage(BasePage):
    """Home page action methods"""

    #Search text
    search_text_element = SearchTextElement()

    #Login element
    email_element = EmailElement()
    password_element = PasswordElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "My Store" appears in page title"""
        return "My Store" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

    def click_sign_in_link(self):
        """Triggers the sign in link"""
        element = self.driver.find_element(*MainPageLocators.SIGN_IN_LINK)
        element.click()

    def click_sign_in_button(self):
        """Triggers the sign in link"""
        element = self.driver.find_element(*MainPageLocators.SUBMIT_LOGIN_BUTTON)
        element.click()
