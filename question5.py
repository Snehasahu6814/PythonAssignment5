"""importing pandas and webdrivers to interact with the application and perform operations"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Launch Chrome driver
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
# List to store all the  product details
product_details = []
# Login with the username and password
username_input = driver.find_element(By.ID, "user-name")
username_input.clear()
username_input.send_keys("standard_user")
time.sleep(4)
password_input = driver.find_element(By.ID, "password")
password_input.clear()
password_input.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(4)
openpyxl.load_workbook("C:/Users/Sneha.sahu/OneDrive - Happiest Minds Technologies Limited/Product Details.xlsx")

# username_input2 = driver.find_element(By.ID, "user-name")
# username_input2.clear()
# username_input2.send_keys("problem_user")
# time.sleep(4)

df_product_details = pd.DataFrame(product_details)
# Appending  the product details to the "Product Details" sheet in the existing Excel file
with pd.ExcelWriter("Product Details.xlsx", mode="a", engine="openpyxl") as writer:
    df_product_details.to_excel(writer, sheet_name="Order Details", index=False)
