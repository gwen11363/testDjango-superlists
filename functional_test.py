from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #此時仍有一個文字方塊，讓使用者可以輸入另一個項目
        #輸入"使用孔雀羽毛製作蒼蠅"
        self.fail('Finish the test!')

        #網頁再次更新，現在清單中有兩個代辦項目

        #網頁產生一個唯一的URL給使用者
        #網頁有一些文字說明這個效果

        #前往URL-顯示使用者的代辦清單

if __name__ == '__main__':
    unittest.main(warnings='ignore')