from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT = 5

class NewVisitorTest(unittest.TestCase):
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
        self.browser.get('http://localhost:8000')

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

        #此時仍有一個文字方塊，讓使用者可以輸入另一個項目
        #輸入"使用孔雀羽毛製作蒼蠅"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #網頁再次更新，現在清單中有兩個代辦項目
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #網頁產生一個唯一的URL給使用者
        #網頁有一些文字說明這個效果
        self.fail('Finish the test!')
        #前往URL-顯示使用者的代辦清單

if __name__ == '__main__':
    unittest.main(warnings='ignore')