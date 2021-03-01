
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import ctypes

class main:


    def start(self):
        self.login()
        # Wait for user to select chat
        while not self.driver.find_elements_by_class_name("im_dialog_wrap.active"):
            ctypes.windll.user32.MessageBoxW(0, "Choose your chat", "Wait For User ...", 0)
        self.driver.find_element_by_class_name("im_dialog_wrap.active").click()
        # Scroll Conversation pannel
        scrl_element = self.driver.find_element_by_class_name("im_history_col")
        while True:
            split_list = self.driver.find_elements_by_class_name("im_message_date_split_text")
            split_text = [x.text for x in split_list] 
            if not split_text.count(split_text[0]) == len(split_text) and len(split_text)>1:
                break
            self.driver.execute_script('arguments[0].scrollTo(0, -arguments[0].scrollHeight)', scrl_element)

            
        
        print(12)
        

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