import requests
from bs4 import BeautifulSoup

def get_topics_page():
    # Get status of the requested page from github.com
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topic_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc