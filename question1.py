"""Importing webdriver to interact with firefox and  using pandas to create the array """
import pandas as pd
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
element = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
text = element.text
usernames = text.split("\n")[1:]
pass_word = driver.find_element(By.XPATH,'//div[@class = "login_password"]')
text1 = pass_word.text
pass_words = text1.split("\n")[1:]
data = {"User ID": range(1, len(usernames) + 1),
        "User Name": usernames,
        "Password": pass_words * len(usernames)}
df = pd.DataFrame(data)
df.to_excel("user credentials.xlsx", index=False)
#print(df)
driver.quit()
