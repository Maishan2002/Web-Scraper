from bs4 import BeautifulSoup
import requests

info = []

class scrape:
    def __init__(self , page):
        self.url = url

    def page_scrape(self):
        self.page = requests.get(self.url)
        self.html_content = BeautifulSoup(self.page.content , 'html.parser')
        self.cards = self.html_content.find_all('div' , {'class':['col-md-12 bordered items', 'en']})
        for card in self.cards:
            self.title = card.find('a' , class_ = 'iulaan-title').text
            self.link  = card.find('a' , class_ = 'iulaan-title').get("href")
            self.office = card.find('a' , class_ = 'iulaan-office').text.replace('\n' , '').replace('  ', '')
            self.date_card = card.find_all('div' , class_ = 'info')
            self.start_date = self.date_card[0].text.replace('\n' , '').replace('  ', '').replace('ތާރީޚު:  ' , '')
            self.deadline = self.date_card[1].text.replace('\n' , '').replace('  ', '').replace('ސުންގަޑި:  ' , '')
            info.append([self.title , self.link , self.office , self.start_date , self.deadline])

    
for i in range(2):
    url = f'https://www.gazette.gov.mv/iulaan?type=vazeefaa&page={i+1}'
    scrape(url).page_scrape()

f=open("jobs.txt", "w+" , encoding = "utf16")

for job in info:
    job_listing = "\n".join(job)
    f.write(job_listing)
    for x in range(2):
        f.write("\n")

f.close()

print(len(info))




