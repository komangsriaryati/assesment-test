# Requirements
1. Python 2.7.12
2. selenium-server-standalone-2.53.1

# Description
1. AutomationPractice Folder : Proof of concept automation testing using selenium and python for AutomationPractice http://automationpractice.com
2. Test Cases Folder contains 4 file test cases :
   - Contact Us Function Test Cases.xlsx
   - Login Function Test Cases.xlsx
   - Order Function Test Cases.xlsx
   - Search Funtion Test Cases.xlsx
3. Bug Report Folder contains 1 bug report related to search function.

# How To Use and Verify
- TestContactUs.py that is containing 4 test ideas (Refer to "Test Cases \ Contact Us Function Test Cases.xlsx")
1. POSITIVE TEST - Send Message using Valid Data
2. NEGATIVE TEST - Send Message using Blank Email
3. NEGATIVE TEST - Send Message using Blank Subject Heading
4. NEGATIVE TEST - Send Message using Blank Message

- TestLogin.py that is containing 7 test ideas (Refer to "Test Cases \ Login Function Test Cases.xlsx")
1. POSITIVE TEST - Login using Valid Data
2. NEGATIVE TEST - Login with Blank Value
3. NEGATIVE TEST - Login with Blank Password
4. NEGATIVE TEST - Login using Invalid Email Format
5. NEGATIVE TEST - Login using Invalid Password Format
6. NEGATIVE TEST - Login using Unregistered Password
7. NEGATIVE TEST - Login using Unregistered Email

- TestOrder.py that is containing 1 test idea (Refer to "Test Cases \ Order Function Test Cases.xlsx")
1. Order Single Product

- TestSearch.py that is containing 6 test ideas (Refer to "Test Cases \ Search Funtion Test Cases.xlsx" and "Bug Report \ Search Function - Numeric Exists Issue.docx")
1. POSITIVE TEST - Search Item Exists
2. POSITIVE TEST - Search Category Exists
3. POSITIVE TEST - Search Sub Category Exists
4. POSITIVE TEST - Search Numeric Exists (FAILED - has been reported in bug report)
5. NEGATIVE TEST - Search Item Not Exists
6. NEGATIVE TEST - Search Blank

