from bs4 import  BeautifulSoup
with open("./book.html",'r') as f:
    soup=BeautifulSoup(f,"lxml")
    print(soup.get_text())