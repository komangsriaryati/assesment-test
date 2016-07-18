import unittest
from selenium import webdriver
import libraries.page
from selenium.webdriver.support.ui import Select

class TestContactUs(unittest.TestCase):
    """Test class for contact us function"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

        # Load the main page and click Contact Us.
        self.main_page = libraries.page.MainPage(self.driver)
        self.main_page.click_contact_us_link()

        # Contact Us page is opened
        assert "Customer service - Contact us" in self.driver.page_source

    # region Valid Contact Us Tests
    def test_valid_data(self):
        """Test send message function for valid data.
        Steps:
        1. Open browser and go to destination URL.
        2. Click Contact Us link on top right.
        3. Select 'Customer Service' from Subject Heading
        4. Input valid email e.g. 'komangsriaryati@yahoo.co.id'
        5. Input message e.g. 'test'
        6. Click on the send button.

        Expected result:
        "Your message has been successfully sent to our team" displayed
        """
        # Input message fields with Customer Service option selected
        Select(self.main_page.select_subject_heading_dropdown()).select_by_value('2')
        self.main_page.contact_email_element = 'komangsriaryati@yahoo.co.id'
        self.main_page.message_element= 'test'
        self.main_page.select_send_button()

        # Verifies message is successfully sent
        assert "Your message has been successfully sent to our team" in self.driver.page_source
    # endregion

    #region Invalid Contact Us Tests
    def test_blank_email(self):
        """Test send message function for blank email.
        Pre-condition:
        There is no value in email address.

        Steps:
        1. Open browser and go to destination URL.
        2. Click Contact Us link on top right.
        3. Select 'Customer Service' from Subject Heading.
        4. Input message e.g. 'test'
        5. Click on the send button.

        Expected result:
        "Invalid email address" displayed
        """
        # Send message without input value on email field
        Select(self.main_page.select_subject_heading_dropdown()).select_by_value('2')
        self.main_page.message_element = 'test'
        self.main_page.select_send_button()

        # Verifies message "Invalid email address" displayed
        assert "Invalid email address" in self.driver.page_source

    def test_blank_subject_heading(self):
        """Test send message function for no option selected on subject heading.
        Pre-condition:
        There is no option selected on subject heading.

        Steps:
        1. Open browser and go to destination URL.
        2. Click Contact Us link on top right.
        3. Input valid email e.g. 'komangsriaryati@yahoo.co.id'
        4. Input message e.g. 'test'
        5. Click on the send button.

        Expected result:
        "Please select a subject from the list provided" displayed
        """
        # Send message without select option on subject heading
        self.main_page.contact_email_element = 'komangsriaryati@yahoo.co.id'
        self.main_page.message_element = 'test'
        self.main_page.select_send_button()

        # Verifies message "Please select a subject from the list provided" displayed
        assert "Please select a subject from the list provided" in self.driver.page_source

    def test_blank_message(self):
        """Test send message function for blank message.
        Pre-condition:
        There is no value in message box.

        Steps:
        1. Open browser and go to destination URL.
        2. Click Contact Us link on top right.
        3. Select 'Customer Service' from Subject Heading
        4. Input valid email e.g. 'komangsriaryati@yahoo.co.id'
        5. Click on the send button.

        Expected result:
        "The message cannot be blank" displayed
        """
        # Send message without input value on message box
        Select(self.main_page.select_subject_heading_dropdown()).select_by_value('2')
        self.main_page.contact_email_element = 'komangsriaryati@yahoo.co.id'
        self.main_page.select_send_button()

        # Verifies message "The message cannot be blank" displayed
        assert "The message cannot be blank" in self.driver.page_source
    # endregion

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()