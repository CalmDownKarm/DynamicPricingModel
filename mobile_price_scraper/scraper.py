
#web scraper for scraping prices of all mobile phones from mysmartprice.com
# hacked it down in few min to fetch data for our model, so not a very clean implementation 
import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    f = open('mobile_price.csv','w')
    while page <= max_pages:
        print(page)
        #creating url
        if page ==1:
           url = 'http://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html#subcategory=mobile'
        else:
           url = 'http://www.mysmartprice.com/mobile/pricelist/pages/mobile-price-list-in-india-'+str(page)+'.html#subcategory=mobile'
        source_code = requests.get(url, allow_redirects=False)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text,'html.parser')
        mobile_detail = list()
        for mobile in soup.findAll(['a','span'],{'class':['prdct-item__name','prdct-item__prc-val']}):#pulling out all the mobile name and prices
            mobile_data = mobile.text.strip().replace(",","")
            mobile_detail.append(mobile_data)
            if len(mobile_detail) == 2:
                f.write(mobile_detail[0]+","+mobile_detail[1]+"\n")#writing to a file
                # print(mobile_detail)
                mobile_detail = []
        page+=1
    f.close()


spider(115)#115 were total number of pages on website at the time of bulding thsi scraper may change in future