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
1. TestContactUs.py that is containing 4 test ideas (Refer to "Test Cases \ Contact Us Function Test Cases.xlsx")
   - POSITIVE TEST - Send Message using Valid Data
   - NEGATIVE TEST - Send Message using Blank Email
   - NEGATIVE TEST - Send Message using Blank Subject Heading
   - NEGATIVE TEST - Send Message using Blank Message
   
2. TestLogin.py that is containing 7 test ideas (Refer to "Test Cases \ Login Function Test Cases.xlsx")
   - POSITIVE TEST - Login using Valid Data
   - NEGATIVE TEST - Login with Blank Value
   - NEGATIVE TEST - Login with Blank Password
   - NEGATIVE TEST - Login using Invalid Email Format
   - NEGATIVE TEST - Login using Invalid Password Format
   - NEGATIVE TEST - Login using Unregistered Password
   - NEGATIVE TEST - Login using Unregistered Email

3. TestOrder.py that is containing 1 test idea (Refer to "Test Cases \ Order Function Test Cases.xlsx")
   - Order Single Product
   
4. TestSearch.py that is containing 6 test ideas (Refer to "Test Cases \ Search Funtion Test Cases.xlsx" and "Bug Report \ Search Function - Numeric Exists Issue.docx")
   - POSITIVE TEST - Search Item Exists
   - POSITIVE TEST - Search Category Exists
   - POSITIVE TEST - Search Sub Category Exists
   - POSITIVE TEST - Search Numeric Exists (FAILED - has been reported in bug report)
   - NEGATIVE TEST - Search Item Not Exists
   - NEGATIVE TEST - Search Blank

