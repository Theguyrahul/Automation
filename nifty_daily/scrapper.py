# Imports
import requests
import pywhatkit as kit
import datetime
from bs4 import BeautifulSoup

# Constants
group_id = "Put Your Group ID Here"
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 2

#links 
nifty_link = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE?hl=en"
bnk_nifty_link = "https://www.google.com/finance/quote/NIFTY_BANK:INDEXNSE?hl=en"

# Defining a class
class nifty:
    def get_htmls(self):
        # Requests
        nifty_url = requests.get(nifty_link).text
        bnk_url = requests.get(bnk_nifty_link).text
        return nifty_url,bnk_url

    def extract_closing(self):
        nifty_url ,bnk_url = self.get_htmls()

        # Soups
        nifty_close =   BeautifulSoup(nifty_url,"html.parser")
        bnk_nifty_close=  BeautifulSoup(bnk_url,"html.parser")

        # Vars
        nifty_close = nifty_close.find("div",class_="YMlKec fxKbKc").text
        bnk_nifty_close = bnk_nifty_close.find("div",class_="YMlKec fxKbKc").text
        nifty_close = float(nifty_close[:2]+nifty_close[3:])
        bnk_nifty_close = float(bnk_nifty_close[:2]+bnk_nifty_close[3:])
        return nifty_close,bnk_nifty_close

    def send_msg(self):
        nifty_close , bnk_nifty_close = self.extract_closing()
        # Massege
        msg = f"Nifty Close: {nifty_close}\nBank Nifty Close: {bnk_nifty_close}"
        kit.sendwhatmsg_to_group(group_id, msg, hours, minutes)
        print(msg)

if __name__ == "__main__":
    bot = nifty()
    bot.send_msg()
        