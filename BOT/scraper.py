import selfbot
from bs4 import BeautifulSoup
import requests

test = selfbot.main()

class scrape():
     async def textify():
        r = requests.get(test.var2).content

        soup =BeautifulSoup(r, "html")

        time = soup.select_one("span", {"class":"ytp-time-duration"}.text)
        print(time)