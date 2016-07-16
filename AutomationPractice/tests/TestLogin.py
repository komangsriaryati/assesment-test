import unittest
from selenium import webdriver
import libraries.page

class TestMyStoreSearch(unittest.TestCase):
    """Test class for login function"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

    # region Valid Data Tests
    def test_login_valid_data(self):
        """Test login function for valid data
        Pre-condition:
        The email and password have been registered.

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        2. Input valid email and password.
        3. Click on the sign in button.

        Expected result:
        "Welcome to your account" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login with registered email and password
        main_page.email_element = "komangsriaryati@yahoo.co.id"
        main_page.password_element ="automation123"
        main_page.click_sign_in_button()
        self.driver.implicitly_wait(10)

        # Verifies "Welcome to your account. Here you can manage all of your personal information and orders." displayed
        assert "Welcome to your account. Here you can manage all of your personal information and orders." in self.driver.page_source
    # endregion

    # region Invalid Data Tests
    def test_login_blank(self):
        """Test login function for blank input
        Pre-condition:
        There is no value in email and password field.

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Click on the sign in button.

        Expected result:
        "An email address required" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login without specify email and password
        main_page.click_sign_in_button()
        self.driver.implicitly_wait(10)

        # Verifies "An email address required" displayed
        assert "An email address required" in self.driver.page_source

    def test_login_blank_password(self):
        """Test login function for blank input on password
        Pre-condition:
        There is no value in password field.

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Input email only.
        4. Click on the sign in button.

        Expected result:
        "Password is required" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login without specify password
        main_page.email_element = "komangsriaryati@yahoo.co.id"
        self.driver.implicitly_wait(10)
        main_page.click_sign_in_button()

        # Verifies "Password is required" displayed
        assert "Password is required" in self.driver.page_source

    def test_login_invalid_email_format(self):
        """Test login function for invalid email format

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Input invalid email format, e.g. "komangsriaryati"
        4. Click on the sign in button.

        Expected result:
        "Invalid email address" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login with invalid email format
        main_page.email_element = "komangsriaryati"
        self.driver.implicitly_wait(10)
        main_page.click_sign_in_button()

        # Verifies "Invalid email address" displayed
        assert "Invalid email address" in self.driver.page_source

    def test_login_invalid_password_format(self):
        """Test login function for invalid password i.e. password length < 5
        Pre-condition:
        Email has been registered.
        There is validation to check whether password consist of five characters minimum

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Input valid email.
        4. Input invalid password with length < 5 e.g. "test"
        5. Click on the sign in button.

        Expected result:
        "Invalid password" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login with invalid password format
        main_page.email_element = "komangsriaryati@yahoo.co.id"
        main_page.password_element = "test"
        self.driver.implicitly_wait(10)
        main_page.click_sign_in_button()

        # Verifies "Invalid password" displayed
        assert "Invalid password" in self.driver.page_source

    def test_login_unregistered_password(self):
        """Test login function for unregistered password i.e. "test123"
        Pre-condition:
        Email has been registered.

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Input valid email.
        4. Input unregistered password i.e. "test123"
        5. Click on the sign in button.

        Expected result:
        "Authentication failed" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login with unregistered password
        main_page.email_element = "komangsriaryati@yahoo.co.id"
        main_page.password_element = "test123"
        self.driver.implicitly_wait(10)
        main_page.click_sign_in_button()

        # Verifies "Authentication failed" displayed
        assert "Authentication failed" in self.driver.page_source
    # endregion

    def test_login_unregistered_email(self):
        """Test login function for unregistered email i.e. "automation@gmail.com"
        Pre-condition:
        Email has not been registered.

        Steps:
        1. Open browser and go to destination URL.
        2. Click sign in link on top left.
        3. Input unregistered email. i.e. "automation@gmail.com"
        4. Input unregistered password i.e. "test123"
        5. Click on the sign in button.

        Expected result:
        "Authentication failed" displayed
        """

        # Load the main page and click sign in.
        main_page = libraries.page.MainPage(self.driver)
        main_page.click_sign_in_link()

        # Login with unregistered password
        main_page.email_element = "automation@gmail.com"
        main_page.password_element = "test123"
        self.driver.implicitly_wait(10)
        main_page.click_sign_in_button()

        # Verifies "Authentication failed" displayed
        assert "Authentication failed" in self.driver.page_source
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()