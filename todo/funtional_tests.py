from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class todo(unittest.TestCase):
    def setUp(self):
         self.browser = webdriver.Firefox()

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
        self.assertTrue(inputbox.get_attribute('placeholder'),'Enter a todo item here')

        inputbox.send_keys('Go to walmart')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy bread')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    #Once user enters the todo item and then press enter, page will refresh
    #Then user's todo should be listed as a table


        self.check_item_in_the_table('1: Go to walmart')
        self.check_item_in_the_table('2: Buy bread')
    def tearDown(self):
         self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')



