import bs4
import urllib.request
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

req = Request('https://www.metasrc.com/tft/champions', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soupPage = soup(webpage, "html.parser")
containers = soupPage.findAll("tr",{"class":"_sr6vt7"});

exportFilename = "championData.csv"
f = open(exportFilename, "w")
headers = "Name, Classes, Cost, HP, Attack, Armor, MR, AS, Range\n"
f.write("")


for container in containers:
	cols = container.findAll("td",{"class":"_byr3u7"});
	
	championName = cols[0].span.text

	classCol = cols[1]
	masks = classCol.findAll("svg");
	className = ""
	for mask in masks:
		className = className +  mask.mask["id"]
	className = className.replace("Mask"," ")
	className = className.title()
	championClasses = className

	championCost = cols[2].span.text
	championHP =  cols[3].text
	championHP = championHP[(championHP.index('.')+2):]

	championAttack =  cols[4].text
	championArmor = cols[5].text
	championMagicResist = cols[6].text
	championAttackSpeed = cols[7].text
	championRange = cols[8].span.text

	f.write(championName+","+championClasses+","+championCost+","+championHP+","+championAttack+","+championArmor+","+championMagicResist+","+championAttackSpeed+","+championRange+"\n")