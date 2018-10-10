# Python script to copy data from http://www.perlanproject.cloud/data/
from getters import get_directories, get_filenames, download_files
import pprint

# nested list to model directory tree
# recursive function to get directory tree

baseurl = 'http://www.perlanproject.cloud/data/'
print('Going to ' + baseurl)

urls = get_directories(baseurl)

print('Got the directories')


urls = get_filenames(urls)

print('Got the filenames')

print('Downloading...')

download_files(urls)

# pprint.pprint(urls)
