from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT = 5

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.1)

    def test_can_start_a_list_and_retrieve_it_later(self):
        #發現一個很酷的線上待辦事項app
        #察看首頁
        self.browser.get(self.live_server_url)

        #發現網頁標題與標頭顯示待辦事項清單
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #馬上輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #在文字方塊輸入"購買孔雀羽毛"
        inputbox.send_keys('Buy peacock feathers')

        #按下enter時，網頁會更新，現在網頁列出
        #"1.購買孔雀羽毛"，一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        user_unique_list_url = self.browser.current_url
        self.assertRegex(user_unique_list_url, 'lists/.+')

        #此時仍有一個文字方塊，讓使用者可以輸入另一個項目
        #輸入"使用孔雀羽毛製作蒼蠅"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #網頁再次更新，現在清單中有兩個代辦項目
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #新的使用者來到網站

        #使用新的瀏覽器工作階段以確保上一位使用者的資料都不會被cookie等機制送出
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #新使用者造訪網頁。沒有任何前一位使用者的清單內容
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #輸入一個新的項目，做出一個新的清單
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('3: Buy milk')

        #新使用者取得獨一無二url
        other_user_unique_url = self.browser.current_url
        self.assertRegex(other_user_unique_url, '/lists/.+')
        self.assertNotEqual(user_unique_list_url, other_user_unique_url)

        #還是沒有任何前一位使用者的清單內容
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

