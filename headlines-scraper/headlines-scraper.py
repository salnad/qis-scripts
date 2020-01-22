import requests
import time
from bs4 import BeautifulSoup
#Quantitative Investment Society
#Anup Diwakar (anupd)


#Change "notToday" and if statement "if 'Today'..." to make it more than 1 day


fileName = input("File name to write to: ")
file = open(fileName, 'a') #appending
notToday = False #del this if you change for more days
count = 1
while notToday == False: #change if more days
    url = "https://seekingalpha.com/market-news/" + str(count)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    response = requests.get(url, headers = headers)
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        newslst = soup.find(id="latest-news-list")
        itemlst = newslst.find_all(class_="item")
        for i in itemlst:
            if "Today" not in i.find(class_="share-line").get_text(): #change also if more days
                notToday = True
                break
            if i.get_text().split('\n')[1] == "On the hour" or i.get_text().split('\n')[1] == "At the close":
                continue
            else:
                file.write(i.get_text().split('\n')[1])
                file.write("\n")
        count += 1
    except:
        print("Messed up")
        break
file.close()
