
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import ctypes
import bs4


class main:


    def start(self):
        self.login()
        # Wait for user to select chat
        while not self.driver.find_elements_by_class_name("im_dialog_wrap.active"):
            ctypes.windll.user32.MessageBoxW(0, "Choose your chat", "Wait For User ...", 0)
        self.driver.find_element_by_class_name("im_dialog_wrap.active").click()
        # Scroll Conversation pannel
        # Do while see difference in date text and keep last date
        # scrl_element = self.driver.find_element_by_class_name("im_history_col")
         
        while True:
            split_list = self.driver.find_elements_by_class_name("im_message_date_split_text")
            
            split_text = [x.text for x in split_list] 
            if not split_text.count(split_text[0]) == len(split_text) and len(split_text)>0:
                # avalin morede ekhtelaf barabar ba entehaye an rooz ast va ma ghable an ra pak mikonim
                split_text = list(set(split_text) - set(last_list))[0]
                break
            last_list = split_text
            self.driver.execute_script("arguments[0].scrollIntoView()", split_list[-1])

            
        self.extract_datahtml(split_text)
        print(12)
        
    def extract_datahtml(self, split_text):
        raw_src = self.driver.page_source
        raw_src = raw_src[raw_src.find(split_text):]
        pg_cntnt = bs4.BeautifulSoup(raw_src,"lxml")
        author_tg = pg_cntnt.find_all("a",{"class":"im_message_author"})
        print(author_tg)


    def __init__(self):
        self.driver = Chrome()
        self.driver.get('https://web.shad.ir/')

    def login(self):
        num = self.input_phonenumber()
        self.driver.find_element_by_name("phone_number").send_keys(num)
        self.driver.find_element_by_class_name("login_head_submit_btn").click() 
        self.driver.find_element_by_class_name("btn.btn-md.btn-md-primary").click() 
        rCode = input("Enter The Code : ")
        self.driver.find_element_by_name("phone_code").send_keys(rCode)
        return
    
    def input_phonenumber(self):
        numfile = open('MobileNumber.txt', 'r')
        number = numfile.readline()
        return number


if __name__ == "__main__":
    main().start()