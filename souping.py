import requests
from bs4 import BeautifulSoup

url = "https://www.ratemyprofessors.com/"
page = requests.get(url)
if page.status_code == 200:
    print("success: website accessed")
else:
    print("error: website NOT accessed")


def write_to_file(file):
    print("-------------Text-------------")
    f = open('data.txt', 'w')
    for mytag in proftags:
        txt = mytag.get_text()
        f.writelines(txt)
        print(txt)
    f.flush()
    print("success: wrote to file!")


soup = BeautifulSoup(page.text, "html.parser")
proftags = soup.findAll("span")
write_to_file(proftags)


