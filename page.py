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
import time
from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class Page(unittest.TestCase):

    def __init__(self, driver, config, locators):
        self.driver = driver
        self.config = config
        self.locators = locators

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(os.path.join(self.config['temp_path'], file_name))

    def get_element_by_css(self, selector):

        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, selector)), 'element timed out: %s' % selector)
        except TimeoutException as e:
            self.fail(e)

    def get_element_by_id(self, selector):

        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.ID, selector)), 'element timed out: %s' % selector)
        except TimeoutException as e:
            self.fail(e)


