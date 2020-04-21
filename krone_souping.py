import requests
from bs4 import BeautifulSoup

url = "https://www.krone.at"
page = requests.get(url)
if page.status_code == 200:
    print("success: website accessed")
else:
    print("error: website NOT accessed")


def write_to_file():
    f = open('krone_data.txt', 'w')
    for first_article_tags in first_article:
        f.writelines(first_article_tags)
        f.flush()


soup = BeautifulSoup(page.text, 'html.parser')
first_article = soup.findAll(class_='box col-xs-12 c_anmod krn-dup-checker krn-regio-dup-checker')
write_to_file()
