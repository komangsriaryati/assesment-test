# Requirements
1.Python 2.7.12
2.selenium-server-standalone-2.53.1

# Description
1. AutomationPractice Folder
   Proof of concept automation testing using selenium and python for AutomationPractice http://automationpractice.com
2. Test Cases Folder
   Contains 4 file test cases :
   - Contact Us Function Test Cases.xlsx
   - Login Function Test Cases.xlsx
   - Order Function Test Cases.xlsx
   - Search Funtion Test Cases.xlsx
3. Bug Report Folder
   Contains 1 bug report related to search function.

# How To Use and Verify
Please run the following tests :
1. TestContactUs.py that is containing 4 test ideas :
POSITIVE TEST:
- Send Message using Valid Data
NEGATIVE TESTS:
- Send Message using Blank Email
- Send Message using Blank Subject Heading
- Send Message using Blank Message
Refer to "Test Cases \ Contact Us Function Test Cases.xlsx"

2. TestLogin.py that is containing 7 test ideas :
POSITIVE TEST:
- Login using Valid Data
NEGATIVE TESTS:
- Login with Blank Value
- Login with Blank Password
- Login using Invalid Email Format
- Login using Invalid Password Format
- Login using Unregistered Password
- Login using Unregistered Email
Refer to "Test Cases \ Login Function Test Cases.xlsx"

3.TestOrder.py that is containing 1 test idea :
- Order Single Product
Refer to "Test Cases \ Order Function Test Cases.xlsx"

4. TestSearch.py that is containing 6 test ideas :
POSITIVE TESTS:
- Search Item Exists
- Search Category Exists
- Search Sub Category Exists
- Search Numeric Exists (FAILED - has been reported in bug report)
NEGATIVE TESTS:
- Search Item Not Exists
- Search Blank
Refer to "Test Cases \ Search Funtion Test Cases.xlsx"
Refer to "Bug Report \ Search Function - Numeric Exists Issue.docx"
