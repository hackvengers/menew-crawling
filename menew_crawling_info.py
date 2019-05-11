from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys
import platform
from bs4 import BeautifulSoup
import requests
from outerinfofeed import OuterInfo

hashtag = ['김치볶음밥']
maxNumOfFeed = 5
filename = 'Output_'+hashtag[0]+'_'+str(maxNumOfFeed)

start_time = time.time()
info = OuterInfo(hashtag,maxNumOfFeed,filename=filename)

urlAndTag = info.urlAndTag()[0]

url = urlAndTag[0]
tag = urlAndTag[1]
req = requests.get(url)