# Python script to copy data from http://www.perlanproject.cloud/data/
from getters import get_directories, get_filenames, download_files

# Define the top-level directory
baseurl = 'http://www.perlanproject.cloud/data/'

# Get the list of urls for the subdirectories
print('Going to ' + baseurl)
urls = get_directories(baseurl)
print('Got the directories')

# Get the list of filenames associated with each directory
urls = get_filenames(urls)
print('Got the filenames')

# This is to download the files
# print('Downloading...')
# download_files(urls)
