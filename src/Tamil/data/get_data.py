from bs4 import BeautifulSoup
import requests

URL = 'http://www.edubilla.com/tamil/bharathiyar-kavithaigal/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
results = soup.find_all('a',class_ = 'clr-Sienna fw300 kural')

page_links = []
for link in results:
    page_links.append(link.get('href'))

print(page_links)

for link in page_links:
    poem_page = requests.get(link)
    poem_soup = BeautifulSoup(poem_page.content, 'html.parser')
    # print(poem_soup)
    poem_results = poem_soup.find_all('span',class_ = 'fw100 kural')
    for poem_link in poem_results:
        try: 
            with open('E:/CODE/github-repos/poetry-generator/src/Tamil/data/uncleaned/bharathiyar_poems.txt','a',encoding='utf-8') as f:
                f.write(poem_link.text)
        except:
             with open('E:/CODE/github-repos/poetry-generator/src/Tamil/data/uncleaned/bharathiyar_poems.txt','w',encoding='utf-8') as f:
                f.write(poem_link.text)
    with open('E:/CODE/github-repos/poetry-generator/src/Tamil/data/uncleaned/bharathiyar_poems.txt','a',encoding='utf-8') as f:
            f.write('\n')