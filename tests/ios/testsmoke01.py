#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from appium import webdriver

from utils import reader
from utils.desiredcaps import get_capabilities


from pages.eggsforfood import EggsForFood


class TestSmoke01(unittest.TestCase):

    def __init__(self, test):

        self.conf = reader.get_conf()
        self.locators = reader.get_locators()
        super(TestSmoke01, self).__init__(test)
    
    def setUp(self):
        
        desired_capabilities = get_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_fundraise_1(self):

        eggsforfood = EggsForFood(self.driver, self.conf, self.locators)

        eggsforfood.open_test_fundraising()

        eggsforfood.set_test_site('company', 'testcompany')

        eggsforfood.select_start_fundraising()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSmoke01("test_fundraise_1"))
    # suite.addTest(TestSmoke01("test_fundraise_2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)