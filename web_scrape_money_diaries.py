'''
This script connects to Refinery29's Money Diaries website and uses Selenium to
get the unique links for 500 money diaries. Using those links, it uses
Beautiful Soup to scrape the diarist metadata and text of their diary and saves
this to a dictionary.  Then the data is broken into 2 dataframes: the metadata
and the text data.
'''

# load packages
import os
import re

from bs4 import BeautifulSoup
import requests

import pandas as pd

from selenium import webdriver

# Get unique links for diaries
def get_diary_links():
    '''
    Get unique links for diaries using Selenium and Chromedriver. When
    chromedriver window opens, continue scrolling down to find
    additonal diaries

    Parameters
    ----------
    website : The Refinery29 money diaries link stem (set as default).

    Returns
    -------
    A variable called links_to_follow that contains the unique identifier for
    all of the money diaries that will be appended to the stem.
    '''

    chromedriver = '/Applications/chromedriver'
    os.environ['webdriver.chrome.driver'] = chromedriver

    website = 'https://www.refinery29.com/en-us/money-diary'
    driver = webdriver.Chrome(chromedriver)
    driver.get(website)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    find_href_links = [i['href'] for i in soup.find_all('a', href=True)]

    links_to_follow = find_href_links[22:-213]

    return links_to_follow

# Create a helper function to get information about each diarist
def get_diarist_value(soup, field_name):
    '''
    Grab a value from Money Diary. Takes a string attribute of a money diary
    and returns the individual value

    Parameters
    ----------
    soup : A BeautifulSoup object that initiates the scraping.
    field_name : The metadata label from the Refinery29 website.

    Returns
    -------
    A series containing the values for each of the individual diaries.
    '''
    blank = 'BLANK'
    try:
        obj = soup.find(text=re.compile(field_name))
        if obj and obj.next_element:
            individual_info = obj.next_element
            return individual_info.strip()
        return blank
    except TypeError:
        return blank

# Create a dictionary to hold the scraped data
def get_money_diaries_dict(id_link):
    '''
    Creates a dictionary of the categories of scraped data from each of the
    money diaries

    Parameters
    ----------
    id_link : The unique part of the link for one money diary.

    Returns
    -------
    A dictionary of scraped data for each of the money diaries.
    '''

    # Develop base URL
    base_url = 'https://www.refinery29.com'

    # Create full URL to scrape
    url = base_url + id_link

    # Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')

    headers = ['story_title', 'occupation', 'age', 'location', 'salary',
               'diary_text']

    # Story title
    story_title = id_link

    # Occupation
    occupation = get_diarist_value(soup, 'Occupation:')

    # Age
    age = get_diarist_value(soup, 'Age:')

    # Location
    location = get_diarist_value(soup, 'Location:')

    # Salary
    salary = get_diarist_value(soup, 'Salary:')

    # Diary text
    diary_text = []
    for div in soup.find_all('div', class_='section-text'):
        diary_text.append(div.text)

    data_dict = dict(zip(headers, [story_title, occupation, age, location,
                                   salary, diary_text]))

    return data_dict

# Scrape the data
def scrape_r29_money_diaries(links_to_follow):
    '''
    Returns 2 dataframes with information scraped from Refinery29: a
    metadata dataframe and a text dataframe

    Parameters
    ----------
    links_to_follow : The list of unique parts of the links for the money diaries.

    Returns
    -------
    Two dataframes with the information scraped from the Refinery29 website:
    diarist_df (the metadata dataframe) and text_df (the text dataframe)
    '''

    money_diary_list = []

    for link in links_to_follow:
        money_diary_list.append(get_money_diaries_dict(link))

    money_df = pd.DataFrame(money_diary_list)

    # Split the money df into 2 separate df to make processing text easier
    text_df = money_df[['story_title', 'diary_text']]
    diarist_df = money_df.drop('diary_text', axis=1)

    # Save dataframes to csv files
    text_df.to_csv(r'text_df.csv', index=False)
    diarist_df.to_csv(r'diarist_df.csv', index=False)

def main():
    '''
    Calls internal functions to the script to scrape data from Refinery29 website
    and then creates a text dataframe that contains the diary information and a diarist
    dataframe that contains diarist metadata.
    '''

    # Call internal functions to this script
    links_to_follow = get_diary_links()
    scrape_r29_money_diaries(links_to_follow)

main()
