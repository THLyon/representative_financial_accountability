import requests
from bs4 import BeautifulSoup

import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv("WEB_APP_STRING")
client_secret = os.getenv("REDDIT_SECRET_STRING")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
user_agent = os.getenv("APP_NAME")


reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                      username = username,  
                     password = password, 
                     user_agent = user_agent) 

subreddit = reddit.subreddit()


# Function to scrape politician names from a webpage
def scrape_politician_names(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Modify the following line based on the HTML structure of the webpage
        politician_names = [name.text for name in soup.find_all('div', class_='politician-name')]
        
        return politician_names
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# Function to make API calls for politician information
def get_politician_info(name):
    api_url = f"https://api.example.com/politician-info?name={name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Parse the response or return it as needed
        politician_info = response.json()
        return politician_info
    else:
        print(f"Failed to retrieve information for {name}. Status code: {response.status_code}")
        return None

# Example usage
webpage_url = "https://example.com/politicians"
politician_names = scrape_politician_names(webpage_url)

if politician_names:
    for name in politician_names:
        politician_info = get_politician_info(name)
        if politician_info:
            print(f"Information for {name}: {politician_info}")
