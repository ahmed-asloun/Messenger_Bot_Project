from utilities import *

# Facebook_Profiles_numbers
profiles = [3, 4, 6]
 
def main():
    
    #messages
    message1 = 'Hey, I have a question please'
    message2 = 'Do you offer a package that includes three rooms and a hallway for a specific price?'
    
    #spreadsheets
    spreadsheet_path = "C:/Users/AHMED/Desktop/Messenger_Bot_Project/outreaching_list.csv"
    progress_sheet_path = "C:/Users/AHMED/Desktop/Messenger_Bot_Project/progress.csv"
    
    # printing down the ascii art
    print_ascii_art()
    
    #initialising progress.csv
    initialise_progress_csv(progress_sheet_path)
    
    # filling fb_ids
    fb_ids = []
    get_facebook_ids(fb_ids, spreadsheet_path)
    
    count = 0  # Initialize count outside the loop
    break_outer_loop = False  # Flag to indicate when to break the outer loop
    fb_id_index = 2 # The index of the first Facebook Id
    try:
        for profile in profiles:
            if break_outer_loop:
                break
            driver = initialize_driver(f"C:\\Users\\AHMED\\Desktop\\Messenger_Bot_Project\\Facebook\\Facebook{profile}")
            start_index = count % len(fb_ids)  # Calculate the starting index for this profile_dir
            for fb_id in fb_ids[start_index:]:  # Iterate over 10 IDs at a time
                sending_messages(driver, fb_id, message1, message2, profile)
                progress(fb_id, profile, progress_sheet_path)
                count += 1
                fb_id_index += 1
                if count % 10 == 0:  # Move to the next profile_dir after sending to 10 IDs 
                    driver.quit()  # Quit the driver after processing each profile_dir
                elif count == len(fb_ids):
                    break_outer_loop = True  # Set the flag to break the outer loop
                    break  # Break out of the inner loop and then the outer loop
    except KeyboardInterrupt:
        save_progress(progress_sheet_path)

if __name__ == "__main__":
    main()