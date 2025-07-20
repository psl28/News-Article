import requests
from bs4 import BeautifulSoup

#newspage1 = https://arstechnica.com/ai/
#newspage2 = https://techcrunch.com/category/artificial-intelligence/
#newspage3 = https://www.artificialintelligence-news.com/artificial-intelligence-news/

class GetLinks():

    def get_links(self) -> tuple[list[str], list[str]]:
        url = "https://arstechnica.com/ai/"
        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text, 'lxml')
        articles = soup.find_all('article')

        l1 = [] #list stores the links to the articles
            
        for each in articles:
            a1 = each.a.get('href')
            l1.append(a1)
        

        url2 = "https://techcrunch.com/category/artificial-intelligence/"
        html_text2 = requests.get(url2).text

        soup2 = BeautifulSoup(html_text2, 'lxml')
        articles2 = soup2.select('li h3 a')
        l2 = []
        
        for a in articles2:
            link = a.get('href')
            l2.append(link)

        l2 = l2[1:6]
        l1 = l1[:5]

        return l1,l2
    

#a = GetLinks()
#a.get_links()
'''def np3():
    url = "https://www.artificialintelligence-news.com/artificial-intelligence-news/"
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    articles = soup.select(' h1 a')
    print(articles)
    l1 = []
    for a in articles:
        link = a.get('href')
        l1.append(link)

    #print(l1)'''

