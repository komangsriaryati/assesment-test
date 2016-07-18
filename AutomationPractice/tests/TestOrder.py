import unittest
from selenium import webdriver
import libraries.page

class TestOrder(unittest.TestCase):
    """Test class for order function"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

        # Load the main page.
        self.main_page = libraries.page.MainPage(self.driver)

    def test_order(self):
        """Test order function"
        Pre-condition:
        The page contains item that could be ordered.

        Steps:
        1. Open browser and go to destination URL.
        2. Hover to image product then Add To Cart button displayed.
        3. Click Add To Cart button.
        4. Click Proceed To Checkout.
        5. Click Proceed To Checkout on Shopping-cart summary.
        6. Input login data (email and password) and click Sign In.
        7. Click Proceed To Checkout on Address Process.
        8. Check term of service checkbox.
        9. Click Proceed To Checkout on Carrier Process.
        10. Select Payment Bank Wire.
        11. Click I confirm my order.

        Expected result:
        "Order process is completed
        """

        # Step 1 : Click Add To Cart
        products = []
        self.main_page.click_add_to_cart_button(products)
        self.driver.implicitly_wait(10)
        assert "Product successfully added to your shopping cart" in self.driver.page_source and "There is 1 item in your cart" in self.driver.page_source

        # Step 2 : Click Proceed To Checkout
        self.main_page.click_proceed_to_checkout_button()
        self.driver.implicitly_wait(10)
        assert "Shopping-cart summary" in self.driver.page_source
        self.assertEqual(self.main_page.get_product_quantity(), "1 Product")

        # Step 3 : Click Proceed To Checkout( Order Product )
        self.main_page.click_proceed_to_checkout_button()
        self.driver.implicitly_wait(10)
        assert "Authentication" in self.driver.page_source

        # Step 4 : Input login
        self.main_page.email_element = "komangsriaryati@yahoo.co.id"
        self.main_page.password_element = "automation123"
        self.main_page.click_sign_in_button()
        self.driver.implicitly_wait(10)
        assert "Your delivery address" in self.driver.page_source and "Your billing address" in self.driver.page_source

        # Step 5 : Address Process
        self.main_page.click_checkout_address_button()
        self.driver.implicitly_wait(10)
        assert "Shipping" in self.driver.page_source and "Choose a shipping option for this address" in self.driver.page_source

        # Step 6 : Carrier Process( check term of service and click proceed to check out )
        self.main_page.check_term_of_service()
        self.main_page.click_checkout_carrier_button()
        self.driver.implicitly_wait(10)
        assert "Please choose your payment method" in self.driver.page_source

        # Step 7 : Process Payment using Bank Wire
        self.main_page.bank_wire_payment()
        self.driver.implicitly_wait(10)
        assert "Order summary" in self.driver.page_source
        self.main_page.confirm_order_button()
        self.driver.implicitly_wait(10)
        assert "Your order on My Store is complete." in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


