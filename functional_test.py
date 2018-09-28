from selenium import webdriver
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
        self.fail('Finish the test!')

        #馬上輸入一個待辦事項

        #在文字方塊輸入"購買孔雀羽毛"

        #按下enter時，網頁會更新，現在網頁列出
        #"1.購買孔雀羽毛"，一個待辦事項清單項目

        #此時仍有一個文字方塊，讓使用者可以輸入另一個項目
        #輸入"使用孔雀羽毛製作蒼蠅"

        #網頁再次更新，現在清單中有兩個代辦項目

        #網頁產生一個唯一的URL給使用者
        #網頁有一些文字說明這個效果

        #前往URL-顯示使用者的代辦清單

if __name__ == '__main__':
    unittest.main(warnings='ignore')