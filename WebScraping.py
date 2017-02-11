
# coding: utf-8

# In[1]:

import numpy as np
import requests as rq
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
filename = "web.csv"
f = open(filename, "w" )
header = "link_to_thread, name_of_thread, replies, views, last_post_time,  last_post_date"
f.write(header + "\n")
page_numbers = np.arange(1,6)
webpagenumbers = [str(page) for page in page_numbers]
for page in webpagenumbers:
    url= 'http://www.f150ecoboost.net/forum/42-2015-ford-f150-ecoboost-chat/index'+ page + '.html'
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    data = page_soup.find_all("div",{"class": "rating0 nonsticky"})
    for item in data:
        link_to_thread = item.div.div.a["href"]
        name_of_thread = item.div.div.a.text
        replies = item.ul.li.a.text
        views = item.ul.find_all("li")[1].text.split()[1] 
        last_post_time_result_set = item.dl.find_all("span",{"class": "time"})
        for x in last_post_time_result_set:
            last_post_time = x.text
            last_post_date_result_set = item.find_all("dl",{"class": "threadlastpost td"})
        for x in last_post_date_result_set:
            last_post_date = x.find_all("dd")[1].text.strip().split()[0]
            f.write(link_to_thread.replace(",","") + "," + name_of_thread.replace(",","") + "," + replies.replace(",","")+ "," + views.replace(",","") + "," + last_post_time+ "," + last_post_date.replace(",","")  + "\n") 
f.close()


# In[ ]:




# In[ ]:



