import requests
from bs4 import BeautifulSoup as b4

if __name__ == "__main__":
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    req = requests.get(url)
    webcontent = b4(req.text, "lxml")
    sel = webcontent.find(class_ = "time")

    print("掛牌時間: {0}".format(sel.text)) 

    tables = webcontent.find("tbody")
    tables = tables.find_all("tr") 

    for i in tables:
        currency = i.find(class_ = "hidden-phone print_show").text.replace(' ', '').replace("\n", '').replace("\r", "")
        buyPrice = i.find(attrs = {"data-table":"本行即期買入"}).text.replace(' ', '').replace("\n", '').replace("\r", "")
        sellPrice = i.find(attrs = {"data-table":"本行即期賣出"}).text.replace(' ', '').replace("\n", '').replace("\r", "")
        buyPrice = float(buyPrice) if buyPrice != "-" else 0
        sellPrice = float(sellPrice) if sellPrice != "-" else 0

        print("貨幣: {:10} 即期中間價: {:3f}".format(currency , (buyPrice + sellPrice) / 2))
    
