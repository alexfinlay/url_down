import requests
import wget
import urllib
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.com"
#BASE_URL = "https://google.ca"
NEW_CREATED_FILE = "newfile.txt"


def download_page(url):
    r = requests.get(url, allow_redirects=True)

    # Open file and write text to it (text being page html)
    with open(NEW_CREATED_FILE, 'wt') as new_file:
        new_file.write(r.text)


def read_downloaded_file():
    with open(NEW_CREATED_FILE, 'rt') as html_file:
        html_data = html_file.read()
        return html_data


def html_parse(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    for links in (soup.find_all('a')):
        print(BASE_URL+links.get('href'))


def get_image_links(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    for images in (soup.find_all('img')):
        try:
            final_url = BASE_URL+images.get('src')
            #print(images.get('src'))
            wget.download(final_url)
        except urllib.error.HTTPError:
            print("There was an error : Ignoring and moving on")


link = "https://realpython.com/python-print/"
#link = "https://google.ca"

# TODO if the file !exists download it
#download_page(link)
page_html = read_downloaded_file()
html_parse(page_html)
print("\n---------------------------\n")
get_image_links(page_html)

#TODO for more practice
# - Find social links like twitter etc
# - get an input url from the user
# - get the IP of the webserver
# - get the storage file name from the user
# - read up on arguments as opposed to input()