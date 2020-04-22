import requests
from bs4 import BeautifulSoup
import tkinter as tk


class Souping(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry('500x300')

        self.pagelabel = tk.Label(self.master, text='Page: ')
        self.pagelabel.pack(side="top")
        self.page = tk.Entry(self.master)
        self.page.pack(side="top")

        self.tagslabel = tk.Label(self.master, text='Tags: ')
        self.tagslabel.pack(side="top")
        self.tags = tk.Entry(self.master)
        self.tags.pack(side="top")

        self.classeslabel = tk.Label(self.master, text='Classes: ')
        self.classeslabel.pack(side="top")
        self.classes = tk.Entry(self.master)
        self.classes.pack(side="top")

        self.scrape = tk.Button(self.master)
        self.scrape["text"] = "Scrape page"
        self.scrape["command"] = self.scrape_page
        self.scrape.pack()

        self.quit = tk.Button(self.master, text="Quit", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def write_to_file(self, html):
        f = open('scraping_data.txt', 'w')
        for item in html:
            f.writelines(item.get_text())
            f.flush()



    def scrape_page(self):
        url = self.page.get()
        tags = self.tags.get()
        classes = self.classes.get()

        page = requests.get(url)

        if page.status_code == 200:
            self.founddisplay = tk.Label(self.master, text=f'{page.status_code} - Website found')
        else:
            self.founddisplay = tk.Label(self.master, text=f'{page.status_code} - Website not found')

        soup = BeautifulSoup(page.text, 'html.parser')

        #{"class": #class}
        html = soup.findAll(tags, class_=classes)

        self.write_to_file(html)

        self.urldisplay = tk.Label(self.master, text=f'{url}\n ')
        self.urldisplay.pack(side="top")


root = tk.Tk()
app = Souping(master=root)
app.mainloop()