from selenium import webdriver
import time
import random
import string

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
print ("A random number from range is : ",end="") 
print (random.randrange(20, 50, 3)) 
chars = string.ascii_letters + string.punctuation

# to be initialized
size = 12
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
