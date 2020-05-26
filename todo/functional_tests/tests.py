from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time
from django.test import LiveServerTestCase

class todo(LiveServerTestCase):
    def setUp(self):
         self.browser = webdriver.Firefox()

    MAX_WAIT = 10
    def wait_until_selenium_find_item_in_the_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError,WebDriverException) as e:
                if (time.time() - start_time) > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)
    #user story
    #As a user, title and header text as 'To-Do'
    def test_01user_start_a_list_and_then_displays_it_later(self):
        self.browser.get('http://127.0.0.1:8000/todo')
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

    #User wants to enter todo item in the input box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a todo item here')
        inputbox.send_keys('Go to walmart')
        inputbox.send_keys(Keys.ENTER)
        self.wait_until_selenium_find_item_in_the_table('1: Go to walmart')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy bread')
        inputbox.send_keys(Keys.ENTER)

        #self.wait_until_selenium_find_item_in_the_table('2: Buy bread')
        self.wait_until_selenium_find_item_in_the_table('1: Go to walmart')
        self.wait_until_selenium_find_item_in_the_table('2: Buy bread')

    @unittest.skip
    def test_02multipleuser_additems_retrieves_list_with_different_urls(self):
        #first user
        self.browser.get('http://127.0.0.1:8000/todo')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # User wants to enter todo item in the input box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a todo item here')
        inputbox.send_keys('Go to walmart')
        inputbox.send_keys(Keys.ENTER)
        self.wait_until_selenium_find_item_in_the_table('1: Go to walmart')
        first_user_url = self.browser.current_url
        self.assertRegex(first_user_url, '/todo/.+')
        #second user
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000/todo')
        body_text = self.browser.find_element_by_tag_name('body')
        self.assertNotEqual('1: Go to walmart', body_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a todo item here')
        inputbox.send_keys('Buy shirt')
        inputbox.send_keys(Keys.ENTER)
        self.wait_until_selenium_find_item_in_the_table('1: Buy shirt')
        second_user_url = self.browser.current_url
        self.assertRegex(second_user_url, '/todo/.+')
        self.assertNotEqual(first_user_url,second_user_url)


    def tearDown(self):
         self.browser.quit()






