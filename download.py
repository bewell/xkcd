import csv
from BeautifulSoup import BeautifulSoup
import urllib
import re

writer = csv.writer(open("d:/python/notes.csv", 'wb'))
writer.writerow(["Name","AltText","path"])


def getStuff(number, csv):
	xkcdSite = urllib.urlopen('http://www.xkcd.com/%s' % number)
	soup = BeautifulSoup(xkcdSite)
	imageurlcontent = soup.find('div', {"id": "comic"}).find("img")
#Find the http link and save the jpg
	url = re.search("http.+\"\ t", str(imageurlcontent))
	imgUrl = url.group(0).replace("\" t", "")
	urllib.urlretrieve(imgUrl, "comics/" + str(number) + ".jpg")
	print 'Finish Image ' + str(number)
#Find the title text and save into the csv file
	altTextSearch = re.search("title.+\ alt=", str(imageurlcontent))
	altText = altTextSearch.group(0)[:-6].replace('title="', "")
	csv.writerow([str(number),altText,"/comics/" + str(number) + ".jpg"])
	print 'Finish Text ' + str(number)

for count in range(1, 1305):
        if(count == 404):
           continue #It wouldn't be xkcd, if it didn't have a joke with 404.
	getStuff(count, writer)
