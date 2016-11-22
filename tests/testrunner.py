import os
import unittest

import HTMLTestRunner
from ios.testsmoke01 import TestSmoke01


def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(TestSmoke01)
    suite_tests = unittest.TestSuite([search_tests])

    with open(os.path.join(os.getcwd(), 'TestReport.html'), "w") as hlr:
        runner = HTMLTestRunner.HTMLTestRunner(stream=hlr, title='Test Report Smoke', description='Test Suite')
        runner.run(suite_tests)


if __name__ == "__main__":
    main()