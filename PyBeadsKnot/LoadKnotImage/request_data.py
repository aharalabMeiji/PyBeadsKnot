import os 
import requests
from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint 

def make_knotimages_dataset():
    url = "http://katlas.org/wiki/The_Hoste-Thistlethwaite_Knot_Table_K11a1-K11n185"
    response = request.urlopen(url)
    soup = BeautifulSoup(response,features="html.parser")
    pprint(soup.select("td")[0].select("img")[0].attrs['src'])
    for i,h in enumerate(soup.select("td")):
        knot_name,ext=h.select("img")[0].attrs["src"].split(".")
        url="http://katlas.org"+h.select("img")[0].attrs["src"]
        print(i+1,url)
        response=requests.get(url,allow_redirects=False,timeout=5)
        with open(os.path.join("./data/gif",knot_name.split("/")[-1]+"."+ext),"wb") as fout:
            fout.write(response.content)

    response.close()

if __name__=="__main__":
    make_knotimages_dataset()