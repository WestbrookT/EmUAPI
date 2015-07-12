from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if len(sys.argv) != 3:
  print("Usage: empeep.py <user> <pass>")
  exit(-1)

# script inputs
user = sys.argv[1]
pw = sys.argv[2]

# initialize selenium
driver = webdriver.Firefox()
driver.implicitly_wait(10) # wait for js to load i think it the critical piece
driver.get("http://empeopled.com")

# click login
login = driver.find_element_by_class_name("header-login")
login.click()

driver.find_element_by_name("login_id").is_displayed()

# fill out login window
login = driver.find_element_by_id("login_modal")
username = login.find_element_by_name("login_id")
password = login.find_element_by_name("login_password")
buttons = login.find_elements_by_tag_name("button")
submit = buttons[2]

# click login submit
username.send_keys(user)
password.send_keys(pw)
submit.click()

# print username and avatar link
u = driver.find_element_by_class_name("xp-user")
name = u.find_element_by_class_name("xp-user-profile")
avatar = u.find_element_by_class_name("xp-user-avatar")
print(name.get_attribute("href"))
print(avatar.get_attribute("src"))

# print currently displayed feed links
tags = driver.find_elements_by_class_name("post-link")
d = {}
for t in tags:
  d[t.get_attribute("href")] = t
tags = d.values()

for t in tags:
  print(t.get_attribute("href"))
