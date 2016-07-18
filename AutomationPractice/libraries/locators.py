from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators."""

    # region Search
    SEARCH_BUTTON = (By.NAME, 'submit_search')
    # endregion

    # region Login
    SIGN_IN_LINK = (By.CLASS_NAME, 'login')
    SUBMIT_LOGIN_BUTTON = (By.NAME, 'SubmitLogin')
    # endregion

    # region Contact Us
    CONTACT_US_LINK = (By.LINK_TEXT, 'Contact us')
    SUBJECT_HEADING_DROPDOWN = (By.ID, 'id_contact')
    SEND_BUTTON = (By.ID, 'submitMessage')
    # endregion

    # region order
    PRODUCT_IMAGE = (By.CLASS_NAME, 'product_img_link')
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, 'Add to cart')
    PROCEED_TO_CHECKOUT_BUTTON = (By.LINK_TEXT,'Proceed to checkout')
    PRODUCT_QUANTITY = (By.ID,'summary_products_quantity')
    CHECKOUT_ADDRESS_BUTTON = (By.NAME,'processAddress')
    CHECKOUT_CARRIER_BUTTON = (By.NAME, 'processCarrier')
    TERM_OF_SERVICE_CHECKBOX = (By.NAME, 'cgv')
    BANK_WIRE_PAYMENT = (By.CLASS_NAME, 'bankwire')
    CONFIRM_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')
    # endregion