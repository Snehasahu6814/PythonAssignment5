"Importing openpyxl to read and write from the excel sheet"
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
excel_file = "product details.xlsx"
order_details = pd.read_excel(excel_file, sheet_name="Order Details",engine="openpyxl")
for index, order in order_details.iterrows():
    id=order["Order Id"]
    user = order["User Type "]
    product_name = order["Product Name"]
    quantity = order["Quantity"]
    expected_price = order["Total Price"]
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    username_field.send_keys(user)
    password_field.send_keys("secret_sauce")
    login_button.click()
    # Add the product to the cart
    add_to_cart_button = driver.find_element(By.XPATH,
                                             f"//*[text()='{product_name}']/ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/button")
    add_to_cart_button.click()
    time.sleep(1)  # Waiting for the cart to update items 
    cart_item_count = driver.find_element(
            By.XPATH, '//*[@class="fa-layers-counter shopping_cart_badge"]'
        ).text
    if int(cart_item_count)>=1:
        click_cart_item = driver.find_element(By.XPATH,
                                              '//*[@class="fa-layers-counter shopping_cart_badge"]')
        click_cart_item.click()       
    # Proceed to checkout
        checkout_button = driver.find_element(By.XPATH, '//*[@class="btn_action checkout_button"]')
        checkout_button.click()
    # Fill in the checkout information
        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        first_name_field.send_keys("Sneha")
        last_name_field.send_keys("Sahu")
        postal_code_field.send_keys("208020")
        continue_button = driver.find_element(By.CLASS_NAME, 'cart_button')
        continue_button.click()
    # Verify the total price
        total_price = driver.find_element(
            By.XPATH, '//*[@class="summary_subtotal_label"]'
        ).text
        price_index = total_price.index('$')
        total = total_price[price_index:]
        print(total_price)
        print("total",total)
        print("Expected Price",expected_price)
        if str(total) != str(expected_price).strip():
            order_details.at[index, "Order Status"] = "Failure"
            #order_ss.append( "Failure")
            print("Failure")
            driver.quit()
            continue
    # Complete the order
        finish_button = driver.find_element(By.XPATH, '//*[@class="btn_action cart_button"]')
        finish_button.click()
    # Mark the order as successful
        order_details.at[index, "Order Status"] = "Success"
        #order_ss.append("Success")
        driver.quit()
        print("Success")
order_details.to_excel("product details.xlsx",
                       sheet_name="Order Details", index=False, engine="openpyxl")
