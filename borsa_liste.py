import requests
from bs4 import BeautifulSoup
import os

'''
pip install bs4
pip install requests
pip install lxml
'''

Url = "https://www.kap.org.tr/tr/Pazarlar"
R = requests.get(Url)
Soup = BeautifulSoup(R.text,"lxml")
List = Soup.find("div", {"class": "w-col w-col-9 w-clearfix sub-col asd"}).find_all("div", {"class": "column-type7 wmargin"})


Url1 = "https://www.oyakyatirim.com.tr/viop/baslangic-teminatlari-kaldirac-oranlari"
R1 = requests.get(Url1)
Soup1 = BeautifulSoup(R1.text, "lxml")


yildiz_pazar = List[0].find_all("div", {"class": "comp-cell _02 vtable"})
#names=[i.get_text() for i in name]
#print(names)
ana_pazar = List[1].find_all("div", {"class": "comp-cell _02 vtable"})
alt_pazar = List[2].find_all("div", {"class": "comp-cell _02 vtable"})

desktop_file = os.path.join(os.environ['USERPROFILE'], "Desktop\\list")
if not os.path.exists(desktop_file):
    os.makedirs(desktop_file)


class dosya_adi():
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        desktop = os.path.join(os.environ['USERPROFILE'], "Desktop\\list", self.dosya_adi + ".txt")
        self.file = open(desktop, "w")

    def pazarlar(self, pazar):       
        for i in pazar:
            i.find("a", {"class": "vcell"})
            self.file.write("BIST:" + i.text.strip() + ",")

    def viop(self, viop_adi):
        for tr in Soup1.find_all('tr'):
            td = tr.find('td')
            if td:
                self.file.write("BIST:" + td.text.strip() + ",")


yildiz = dosya_adi("yildiz pazar")
yildiz.pazarlar(yildiz_pazar)

ana = dosya_adi("ana pazar")
ana.pazarlar(ana_pazar)

alt = dosya_adi("alt pazar")
alt.pazarlar(alt_pazar)

viop_adi = dosya_adi("viop")
viop_adi.viop(Soup1)
