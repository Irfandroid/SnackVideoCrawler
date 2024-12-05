# **SnackVideoCrawler**
**Overview**
The SnackVideo Crawler is a Python script designed to scrape video data from the SnackVideo website based on specified keywords. The script retrieves information such as video ID, URL, username, author, views, likes, comments, shares, followers, and upload date. The collected data is then saved in an Excel file for further analysis.

**Features**
Crawls SnackVideo for posts containing specified keywords.
Extracts relevant video information in a structured format.
Saves the extracted data to an Excel file.
Automatically runs daily at a specified time using a scheduler.

**Prerequisites**
Python 3.x installed on your machine.
Internet connection to access the SnackVideo website.
Basic knowledge of running Python scripts.
**Installation**
Clone or Download the Repository: If you are using a version control system, clone the repository. Otherwise, download the script file.



Run the Script: Open your terminal or command prompt, navigate to the directory where crawler.py is located, and run the script using the following command:
python crawler.py



Scheduled Execution: The script will now run the main() function every day at 19:02 (7:02 PM). You can change the time in the schedule.every().day.at("19:02").do(main) line to your desired time.


**Output**
The output of the script is an Excel file named snackvideo_data.xlsx, which is saved in an output folder. If the folder does not exist, it will be created automatically.
