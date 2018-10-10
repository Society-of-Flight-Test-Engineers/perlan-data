import requests
import bs4
import re
import os

def get_directories(url):
# Recursively retrieves the directory tree and stores it in a list of empty dictionaries

    url_list = [{url:[]}]
    # requests gets the initial page
    r = requests.get(url)

    # BeautifulSoup parses the HTML
    s = bs4.BeautifulSoup(r.text, features="html.parser")


    # finds all of the "a" tags inside of the "pre" tag that have an href
    # that STARTS '^('
    # with NOT "/" '[^/]'
    # contains one or more word characters"\w" or percent signs "%" '[\w%]+'
    # and ends with a "/" '/)

    for item in s.pre.find_all('a', href=re.compile(r"^([^/][\w%]+/)")):
        url_list.extend(get_directories(url + item['href']))
        
    
    return url_list


def get_filenames(url_list):
# Given a list of dictionaries with a url as key and an empty list as value
# Retrieves the list of files for download

    # Given the list of url dictionaries, go through each one
    for i, url in enumerate(url_list):

        # Get the url "k" and the list "v" (v is not used)
        (k, v), = url.items()  # pylint: disable=W0612
        
        # Go to the website url

        r = requests.get(k)

        # Get the text
        s = bs4.BeautifulSoup(r.text, features="html.parser")


        # Find in all "a" tags the "href" with
        # One or more word characters "\w", percent signs "%" or dashes "-" '^([\w%-]+'
        # a single period "." '.{1}'
        # ending in 3 or 4 word characters "\w" '\w{3,4})'

        for item in s.pre.find_all('a', href=re.compile(r"^([\w%-]+\.{1}\w{3,4})")):
            # Append the filename to the list that is the value that goes with the url
            url_list[i][k].append((item['href']))


    return url_list



def download_files(url_list, dirname = 'C:/Users/natha/OneDrive - Georgia Institute of Technology/Perlan/perlan-data'):
# Given a list of urls and the filenames available at that url
# Navigate to the url and download the file to the local machine
# that is running the script
    for url in url_list:
        (k, v), = url.items()
        for fname in v:
            r = requests.get(k + fname)
            filename = dirname + (k + fname).replace('http://www.perlanproject.cloud','')
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
            print(filename)
