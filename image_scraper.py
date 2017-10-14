from bs4 import BeautifulSoup
import urllib
import shutil
import requests
from urllib.parse import urljoin
import sys
import time

def make_soup(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    html = urllib.request.urlopen(req)
    return BeautifulSoup(html, 'html.parser')

def save_image(source):
    filename = source.strip().split('/')[-1].strip()
    print ('Getting: ' + filename)
    response = requests.get(source, stream=True)
    time.sleep(1) # delay to avoid corrupted previews
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    print ('Downloading images to current working directory.')

    for idx, image in enumerate(images):
        try:
            source = image.get('src')
            save_image(urljoin(url, source))
        except:
            print ('An error occured. Continuing.')
    print ('Done.')

get_images('https://brightside.me/article/100-best-photographs-without-photoshop-46555')