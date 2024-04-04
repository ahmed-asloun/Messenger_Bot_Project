from utilities import *
 
def main():
    
    # Facebook_Profiles_numbers
    profiles = [6, 4, 3]
    
    #messages
    message1 = 'Type here your message'
    message2 = 'Type here your message'
    
    #spreadsheets
    spreadsheet_path = "path/to/spreadsheet"
    progress_sheet_path = "path/to/progress_sheet"
    
    # Headless Mode
    headless_mode = False
    
    # amount of fb_id's to send to using one profile
    sending_per_profile = 10
    
    
    # printing down the ascii art
    print_ascii_art()
    
    #initialising progress.csv
    initialise_progress_csv(progress_sheet_path)
    
    # filling fb_ids
    fb_ids = []
    get_facebook_ids(fb_ids, spreadsheet_path)
    
    try:
        bulk_sender(profiles, fb_ids, message1, message2, sending_per_profile, progress_sheet_path, headless_mode) 
    except:
        save_progress(progress_sheet_path)

if __name__ == "__main__":
    main()
