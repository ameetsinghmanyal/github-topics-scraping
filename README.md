# Top Repositories for Topics on GitHub

### Overview

 Welcome to the repository for a Python Script that scrapes the list of topics from GitHub, retrieves the top repositories for each topic, and saves the data into CSV files.
 The code is returning a list of topics from GitHub along with their descriptions and URLs. 
 It then scrapes the top repositories for each topic and saves the information in CSV files in a 'data' directory
 
 In this project we have used the [**Github Topics**](https://github.com/topics) as our data    
 
### Install Packages
```
pip install pandas
pip install bs4
pip install requests
```

### Workflow
Here are the steps I follwed:

- I'll scrape data from https://github.com/topics
- Will get a list of topics. For each topic, I'll get topic title, topic page URL and topic description
- For each topic, I'll get the top 25 repositories in the topic from the topic page
- For each repository, I'll grab the repo name, username, stars and repo URL
- For each topic I'll create a CSV file
