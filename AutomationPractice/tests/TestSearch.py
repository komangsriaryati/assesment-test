import unittest
from selenium import webdriver
import libraries.page

class TestSearch(unittest.TestCase):
    """Test class for search function"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

        # Load the main page.
        self.main_page = libraries.page.MainPage(self.driver)

    # region Valid Data Tests
    def test_search_item_exists(self):
        """Test search function for item exists i.e. "blouse"
        Pre-condition:
        The page contains item "blouse".

        Steps:
        1. Open browser and go to destination URL.
        2. Type in search text field "blouse".
        3. Click on the search button.

        Expected result:
        "No results were found for your search" does not displayed
        """

        # Sets the text of search textbox to "blouse"
        self.main_page.search_text_element = "blouse"
        self.main_page.click_search_button()

        # Verifies "No results were found for your search" does not displayed
        assert "No results were found for your search" not in self.driver.page_source

    def test_search_category_exists(self):
        """Test search function for category exists i.e. "dresses"
        Pre-condition:
        The page contains category "dresses".

        Steps:
        1. Open browser and go to destination URL.
        2. Type in search text field "dresses".
        3. Click on the search button.

        Expected result:
        "No results were found for your search" does not displayed
        """

        # Sets the text of search textbox to "dresses"
        self.main_page.search_text_element = "dresses"
        self.main_page.click_search_button()

        # Verifies "No results were found for your search" does not displayed
        assert "No results were found for your search" not in self.driver.page_source

    def test_search_sub_category_exists(self):
        """Test search function for category exists i.e. "casual"
        Pre-condition:
        The page contains sub category "casual".

        Steps:
        1. Open browser and go to destination URL.
        2. Type in search text field "casual".
        3. Click on the search button.

        Expected result:
        "No results were found for your search" does not displayed
        """

        # Sets the text of search textbox to "casual"
        self.main_page.search_text_element = "casual"
        self.main_page.click_search_button()

        # Verifies "No results were found for your search" does not displayed
        assert "No results were found for your search" not in self.driver.page_source

    def test_search_numeric_exists(self):
        """Test search function for numeric exists i.e. 16
        Pre-condition:
        The page contains price 16.

        Steps:
        1. Open browser and go to destination URL.
        2. Type in search text field 16.
        3. Click on the search button.

        Expected result:
        "No results were found for your search" does not displayed
        """

        # Sets the text of search textbox to 16
        self.main_page.search_text_element = "16"
        self.main_page.click_search_button()

        # Verifies "No results were found for your search" does not displayed
        assert "No results were found for your search" not in self.driver.page_source
    # endregion

    # region Invalid Data Tests
    def test_search_item_not_exists(self):
        """Test search function for item that does not exist i.e. "not exists"
        Pre-condition:
        The page does not contain item "not exists".

        Steps:
        1. Open browser and go to destination URL.
        2. Type in search text field "not exists".
        3. Click on the search button.

        Expected result:
        "No results were found for your search" displayed
        """

        # Sets the text of search textbox to "not exists"
        self.main_page.search_text_element = "not exists"
        self.main_page.click_search_button()

        # Verifies "No results were found for your search" displayed
        assert "No results were found for your search" in self.driver.page_source

    def test_search_blank(self):
        """Test search function for blank input
        Pre-condition:
        There is no text in search text field.

        Steps:
        1. Open browser and go to destination URL.
        3. Click on the search button.

        Expected result:
        "Please enter a search keyword" displayed
        """

        # Click the search button
        self.main_page.click_search_button()

        # Verifies "Please enter a search keyword" displayed
        assert "Please enter a search keyword" in self.driver.page_source
    # endregion

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
