"""importing pandas and webdrivers to interact with the application and perform operations"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# Launch Chrome driver
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
# List to store product details
product_details = []
# Login with a user
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
# Retrieve product information
product_elements = driver.find_elements(By.XPATH,"//div[@class='inventory_item']")
for product_element in product_elements:
    product_id=product_element.find_element(By.XPATH,
    ".//div[@class='inventory_item_img']/a").get_attribute("href").split("=")[-1]
    product_name=product_element.find_element(By.XPATH,
    ".//div[@class='inventory_item_name']").text
    product_description = product_element.find_element(By.XPATH,
    ".//div[@class='inventory_item_desc']").text
    product_price=product_element.find_element(By.XPATH,
    ".//div[@class='inventory_item_price']").text
    product_details.append({
        "Product ID": product_id,
        "Product Name": product_name,
        "Description": product_description,
        "Price": product_price
    })
# Close the driver
driver.quit()
# Create a DataFrame from the product details
df_product_details = pd.DataFrame(product_details)
# Append the product details to the "Product Details" sheet in the existing Excel file
with pd.ExcelWriter("user credentials.xlsx", mode="a", engine="openpyxl") as writer:
    df_product_details.to_excel(writer, sheet_name="Product Details", index=False)
