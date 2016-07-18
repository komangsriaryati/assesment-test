from element import BasePageElementByName
from element import BasePageElementById
from locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException
from urlparse import parse_qs, urlparse
from selenium.webdriver.common.action_chains import ActionChains

class SearchTextElement(BasePageElementByName):
    locator = 'search_query'

# region Login
class EmailElement(BasePageElementByName):
    locator = 'email'

class PasswordElement(BasePageElementByName):
    locator = 'passwd'
# endregion

# region Contact Us
class MessageElement(BasePageElementByName):
    locator = 'message'

class ContactEmail(BasePageElementById):
    locator = 'email'
# endregion

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
       self.driver = driver

class MainPage(BasePage):
    """page action methods"""

    #Search text
    search_text_element = SearchTextElement()

    #Login elements
    email_element = EmailElement()
    password_element = PasswordElement()

    # Contact Us element
    contact_email_element = ContactEmail()
    message_element = MessageElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "My Store" appears in page title"""
        return "My Store" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        try:
            element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
            element.click()
        except NoSuchElementException:
            return

    def click_sign_in_link(self):
        """Triggers the sign in link"""
        try:
            element = self.driver.find_element(*MainPageLocators.SIGN_IN_LINK)
            element.click()
        except NoSuchElementException:
            return

    def click_sign_in_button(self):
        """Triggers the sign in button"""
        try:
            element = self.driver.find_element(*MainPageLocators.SUBMIT_LOGIN_BUTTON)
            element.click()
        except NoSuchElementException:
            return

    #region Contact Us
    def click_contact_us_link(self):
        """Triggers the Contact us link"""
        try:
            element = self.driver.find_element(*MainPageLocators.CONTACT_US_LINK)
            element.click()
        except NoSuchElementException:
            return

    def select_subject_heading_dropdown(self):
        """Triggers the Subject Heading Option"""
        try:
            return self.driver.find_element(*MainPageLocators.SUBJECT_HEADING_DROPDOWN)
        except NoSuchElementException:
            return

    def select_send_button(self):
        """Triggers the Send Button"""
        try:
            element = self.driver.find_element(*MainPageLocators.SEND_BUTTON)
            element.click()
        except NoSuchElementException:
            return
    # endregion

    def click_add_to_cart_button(self, products):
        """Triggers Add To Cart Button"""
        try:
            elements = self.driver.find_elements(*MainPageLocators.PRODUCT_IMAGE)
            for element in elements:
                if element.is_enabled():
                    # Get the product id
                    # Add the product that has not been added into cart
                    url= element.get_attribute('href')
                    parse_result = parse_qs(urlparse(url).query, keep_blank_values=True)
                    id_product = str(parse_result.get('id_product')[0])
                    if id_product not in products:
                        # Hover to product image to show up the Add To Cart button
                        ActionChains(self.driver).move_to_element(element).perform()
                        self.driver.implicitly_wait(10)
                        add_to_cart_button = self.driver.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
                        # Click Add To Cart button and
                        # add the product id into product list that has been added into cart
                        if add_to_cart_button.is_displayed():
                            add_to_cart_button.click()
                            products.extend(id_product)
                            break
        except NoSuchElementException:
            return

    def click_proceed_to_checkout_button(self):
        """Triggers proceed to checkout button"""
        try:
            element = self.driver.find_element(*MainPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
            element.click()
        except NoSuchElementException:
            return

    def get_product_quantity(self):
        """Get the product quality on shopping-cart summary"""
        try:
            quantity = self.driver.find_element(*MainPageLocators.PRODUCT_QUANTITY)
            return quantity.text
        except NoSuchElementException:
            return

    def click_checkout_address_button(self):
        """Triggers proceed to checkout button (Address Process)"""
        try:
            element = self.driver.find_element(*MainPageLocators.CHECKOUT_ADDRESS_BUTTON)
            element.click()
        except NoSuchElementException:
            return

    def click_checkout_carrier_button(self):
        """Triggers proceed to checkout button (Carrier Process)"""
        try:
            element = self.driver.find_element(*MainPageLocators.CHECKOUT_CARRIER_BUTTON)
            element.click()
        except NoSuchElementException:
            return

    def check_term_of_service(self):
        """Triggers proceed to check the term of service checkbox"""
        try:
            element = self.driver.find_element(*MainPageLocators.TERM_OF_SERVICE_CHECKBOX)
            element.click()
        except NoSuchElementException:
            return

    def bank_wire_payment(self):
        """Triggers proceed to pay using bank wire"""
        try:
            element = self.driver.find_element(*MainPageLocators.BANK_WIRE_PAYMENT)
            element.click()
        except NoSuchElementException:
            return

    def confirm_order_button(self):
        """Triggers proceed to confirm order"""
        try:
            element = self.driver.find_element(*MainPageLocators.CONFIRM_ORDER)
            element.click()
        except NoSuchElementException:
            return