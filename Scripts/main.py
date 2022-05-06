from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from Test.test_login import TestLogin
from Test.test_search import TestSearch
from Test.test_order import TestOrder
from Test.test_contact import TestContactUS


# Get all test from Test
test1 = TestLoader().loadTestsFromTestCase(TestLogin)
test2 = TestLoader().loadTestsFromTestCase(TestSearch)
test3 = TestLoader().loadTestsFromTestCase(TestOrder)
test4 = TestLoader().loadTestsFromTestCase(TestContactUS)

# Creating test suites
# Sanity test suite
masterTestSuite = TestSuite([test1, test2, test3, test4])
runner = HTMLTestRunner(output=r'..\\Reports', combine_reports=True,
                        report_title="Final Report").run(masterTestSuite)
