
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

def main():
    driver = Chrome()
    driver.get('https://web.shad.ir/')
    login()

    


def login():
    num = input_phonenumber()
    driver.find_element_by_name("phone_number").send_keys(num)
    driver.find_element_by_class_name("login_head_submit_btn").click() 
    driver.find_element_by_class_name("btn.btn-md.btn-md-primary").click() 
    rCode = input("Enter The Code : ")
    driver.find_element_by_name("phone_code").send_keys(rCode)
    return

def input_phonenumber():
    numfile = open('MobileNumber.txt', 'r')
    number = numfile.readline()
    return number


if __name__ == "__main__":
    main()