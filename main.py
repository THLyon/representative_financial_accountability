import requests
from bs4 import BeautifulSoup

import praw
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("WEB_APP_STRING")
client_secret = os.getenv("REDDIT_SECRET_STRING")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
user_agent = os.getenv("APP_NAME")

reddit = praw.Reddit(client_id=client_id,  
                     client_secret=client_secret,  
                     username=username,  
                     password=password, 
                     user_agent=user_agent) 

subreddit = reddit.subreddit()


# scrape politician names from a webpage
def scrape_politician_names(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        politician_names = []

        for paragraph in soup.find_all('p'):
            text_content = paragraph.get_text()

            if 'Sen.' in text_content:
                start_index = text_content.index('Sen.') + len('Sen.')
                end_index = text_content.index('(')
                politician_name = text_content[start_index:end_index].strip()

                politician_names.append(politician_name)
        
        return politician_names
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# API calls for politician info
def get_politician_info(name):
    api_url = f"https://api.example.com/politician-info?name={name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        politician_info = response.json()
        return politician_info
    else:
        print(f"Failed to retrieve information for {name}. Status code: {response.status_code}")
        return None

if politician_names:
    for name in politician_names:
        politician_info = get_politician_info(name)
        if politician_info:
            print(f"Information for {name}: {politician_info}")
