from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    # print(content)
    soup=BeautifulSoup(content, 'lxml')
    # print(soup)
    tags=soup.find('p')
    print(tags)