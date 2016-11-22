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
from selenium.common.exceptions import TimeoutException
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page import Page

WAIT_TIME = 10


class EggsForFood(Page, unittest.TestCase):

    def __init__(self, driver, config, locators):
        self.driver = driver
        self.config = config
        self.locators = locators

        self.action = TouchAction(self.driver)

    def open_test_fundraising(self):
        self.driver.get(self.config.get('fund_test_url'))

    def wait_test_page_loaded(self):
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(EC.presence_of_element_located((By.ID, 'testUrl')),
                                                        'element not found: testUrl')
        except TimeoutException as e:
            self.fail(e)

    def enter_test_url(self, url):
        self.get_element_by_id('testUrl').send_keys(url)

    def enter_entity_type(self, entity_type):
        self.get_element_by_id('entityType').send_keys(entity_type)

    def enter_entity_id(self, entity_id):
        self.get_element_by_id('entityID').send_keys(entity_id)

    def set_test_site(self, entity_type, entity_id, campaign=None):
        self.enter_test_url(self.config.get('test_site'))
        self.enter_entity_type(entity_type)
        self.enter_entity_id(entity_id)
        if campaign:
            self.get_element_by_id().send_keys()

        el = self.get_element_by_id('submit')
        el.click()

    def select_start_fundraising(self):
        self.get_element_by_id('ammadoStartFundraising').click()

