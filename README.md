# Messenger Bot Project

This project automates the process of sending messages to multiple Facebook profiles using Selenium. It is designed to mimic human behavior by incorporating random wait times between sending messages. This can be useful for outreach campaigns or other scenarios where you need to send messages to a list of Facebook profiles.

## Features

- **Profile-based Messaging**: The bot sends messages to Facebook profiles based on the specified list of profiles.
- **Randomized Wait Times**: The bot waits for random durations between sending messages to simulate human behavior and avoid detection.
- **Customizable Messages**: You can customize the messages sent by modifying the `message1` and `message2` variables in the script.
- **Efficient Profile Management**: Profiles are managed in separate directories (`Facebook0`, `Facebook1`, etc.), making it easy to organize and switch between profiles.
- Automates sending messages on Facebook Messenger.
- Supports sending two different messages to each Facebook ID.
- Uses profiles to manage different instances of Chrome WebDriver.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmed-asloun/Messenger_Bot_Project.git

## Setup

1. **Install Dependencies**: Install the required Python packages using pip:
   ```bash
   pip install selenium pandas

Download Chrome WebDriver: Download the Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads) and place it in the specified path (`C:\\Users\\AHMED\\Desktop\\Ac\\Messenger_Bot_Project\\chromedriver.exe`).

Create Facebook Profiles Directories: Create directories named `Facebook0`, `Facebook1`, etc., at `C:\\Users\\AHMED\\Desktop\\Ac\\Facebook\\` to store profile data.

Prepare Outreaching List: Fill the `outreaching_list.csv` spreadsheet with Facebook IDs under the column 'Facebook Id'.

## Usage

1. **Run the Script**: Execute the `python main.py` script to start the messaging process.

2. **Monitor Progress**: The script will send messages to Facebook profiles as specified in the `outreaching_list.csv` spreadsheet.

3. **Customize Messages**: Modify the `message1` and `message2` variables in the script to customize the messages sent to each profile.

4. **Automated Messaging**: The bot will automatically handle sending messages, waiting between messages, and switching between Facebook profiles.

## Notes

- This project is designed for educational purposes and should be used responsibly and in compliance with Facebook's terms of service.
- It is recommended to test the bot with a small number of profiles before scaling up to avoid any issues.
- The user of the bot needs to check that the chromedriver's version and their Chrome version are the same.
"# Messenger_Bot_Project" 
"# Messenger_Bot_Project" 
