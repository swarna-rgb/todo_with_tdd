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
                print('I am in except')
                if (time.time() - start_time) > self.MAX_WAIT:
                    raise e
                print('I am sleeping')
                time.sleep(0.5)



    def check_item_in_the_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    #user story
    #As a user, title and header text as 'To-Do'
    def test_user_start_a_list_and_then_displays_it_later(self):
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
        #time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy bread')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(0.1)

        #self.wait_until_selenium_find_item_in_the_table('2: Buy bread')

    #Once user enters the todo item and then press enter, page will refresh
    #Then user's todo should be listed as a table
        #self.check_item_in_the_table('1: Go to walmart')
        #self.check_item_in_the_table('2: Buy bread')

        self.wait_until_selenium_find_item_in_the_table('1: Go to walmart')
        self.wait_until_selenium_find_item_in_the_table('2: Buy bread')

    def tearDown(self):
         self.browser.quit()


# if __name__ == '__main__':
#     unittest.main(warnings='ignore')



