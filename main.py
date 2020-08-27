from bs4 import BeautifulSoup
import requests

URL = 'https://greenteapress.com/wp/think-python/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')



def main():

    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    f= open("pdf_links.txt","w+")
    for link in links:
        if "pdf" in link:
            f.write(f"{link}\n")
            print(link)
    f.close()

main()
