from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# to be initialized
filepath = 'data.txt'
name = "chat_name"
message = " your_message "
count = 10

# read from file and send message line by line
file = open('data.txt', 'r')
file_data = f.read().splitlines()

input('Press enter after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    # Message Format: 'i your_message file data (line by line)'
    # remove "str(i+1) , message to just send file data
    msg_box.send_keys(str(i+1) + message + file_data[i])
    button = driver.find_element_by_class_name('_2lkdt')
    button.click()
    # interval between messages in seconds
    time.sleep(0.5)
f.close()
