from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import pandas as pd
import csv
from termcolor import colored
import shutil
import os
from datetime import datetime




# creating a chrome instance
def initialize_driver(profile_path, headless_mode):
    # Path to the Chrome WebDriver executable
    chrome_driver_path = "C:\\Users\\AHMED\\Desktop\\Messenger_Bot_Project\\chromedriver.exe"
    
    # Create a chrome_options  object and set the user data directory    
    chrome_options  = Options()
    # to work on aspecific dir
    chrome_options .add_argument("user-data-dir=" + profile_path)
    
    if headless_mode:
        # To run in headless mode
        chrome_options .add_argument("--headless")
    # to delete log (facebook log warnings)
    chrome_options .add_argument('--log-level=3')
    
    # Create a Chrome WebDriver instance with the specified options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options )
    
    return driver

def sending_messages(driver, fb_id, message1, message2, profile, headless_mode):
    # Random Sleep durations
    sleep_duration_Loading_account = random.randint(7, 12)
    sleep_duration = random.randint(4, 8)
    
    # Maximizing the window
    if not headless_mode:
        driver.maximize_window()
    
    wait = WebDriverWait(driver, 20)
    driver.get(f'https://www.messenger.com/t/{fb_id}')
    sleep(sleep_duration_Loading_account)
    
    try:
        continue_as_login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]')))
        if continue_as_login.is_displayed():
            continue_as_login.click()
            sleep(sleep_duration_Loading_account)
    except TimeoutException:
        # Handle the case when the element is not found or not clickable
        pass
    
    print(f"Sending message 1 to Facebook Id = {fb_id} by Profile{profile}")
    # sending message1
    try:
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]')))
        message_box.send_keys(message1)
        send_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/div[1]")))
        send_button.click()
        sleep(sleep_duration)
        print(colored(f"Message 1 sent to Facebook Id = {fb_id} by Profile{profile}\n", "green"))
    except TimeoutException:
        print(colored("Element not found, pass", "light_yellow"))
        pass
    
    print(f"Sending message 2 to Facebook Id = {fb_id} by Profile{profile}")
    # Sending message2
    try:
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]')))
        message_box.send_keys(message2)
        send_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/div[1]")))
        send_button.click()
        sleep(sleep_duration)
        print(colored(f"Message 2 sent to Facebook Id = {fb_id} by Profile{profile}\n", "green"))
    except TimeoutException:
        print(colored("Element not found, pass", "light_yellow"))
        pass

# reading outreaching_list.csv & filling fb_ids[]
def get_facebook_ids(fb_ids, spreadsheet_path):
    df = pd.read_csv(spreadsheet_path)
    for _, row in df.iterrows():
        fb_ids.append(row['Facebook Id'])

# Initilising the progress_spredsheet, on every bulk send
def initialise_progress_csv(spreadsheet_path):
    with open(spreadsheet_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sent to Facebook Id", "by"])

# updating the progress.csv
def progress(fb_id, profile, spreadsheet_path):
    with open(spreadsheet_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["sent to Facebook Id", "by"])
        writer.writerow({"sent to Facebook Id":fb_id, "by":f"profile{profile}"})

# Prints out the ASCII Art logo.
def print_ascii_art():
    with open("C:\\Users\\AHMED\\Desktop\\Messenger_Bot_Project\\assets\\ascii_art.txt", "r") as f:
        ascii_art = f.read()
        print(colored(ascii_art, "cyan"))

#saving the progress.csv sheet with timestamp after Keyboadinterrupt
def save_progress(sheet_path):
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  new_file_name = f"progress_{timestamp}.csv"
  shutil.copy(sheet_path, os.path.join("C:/Users/AHMED/Desktop/Messenger_Bot_Project/progress", new_file_name))

def bulk_sender(profiles, fb_ids, message1, message2, sending_per_profile, progress_sheet_path, headless_mode):
    count = 0  # Initialize count outside the loop
    break_outer_loop = False  # Flag to indicate when to break the outer loop
    for profile in profiles:
            if break_outer_loop:
                break
            driver = initialize_driver(f"C:\\Users\\AHMED\\Desktop\\Messenger_Bot_Project\\Facebook\\Facebook{profile}",headless_mode)
            start_index = count % len(fb_ids)  # Calculate the starting index for this profile_dir
            for fb_id in fb_ids[start_index:]:  # Iterate over 10 IDs at a time
                sending_messages(driver, fb_id, message1, message2, profile, headless_mode)
                progress(fb_id, profile, progress_sheet_path)
                count += 1
                if count % sending_per_profile == 0:# Move to the next profile_dir after sending to 10IDs 
                    driver.quit()  # Quit the driver after processing each profile_dir
                    break
                elif count == len(fb_ids):
                    break_outer_loop = True  # Set the flag to break the outer loop
                    break  # Break out of the inner loop and then the outer loop
