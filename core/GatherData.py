import requests
from bs4 import BeautifulSoup
#from GetLinks import GetLinks

class GetData():

    #def __init__(self):
        #The code written here will be removed if we are implementing agentic structure
        #obj1 = GetLinks()
        #self.links1, self.links2 = obj1.get_links()

    def get_data(self, links1: list[str], links2: list[str]) -> dict:
        #links is a list of all the urls
        Art = {}
        for i in range(4):
            demo = links1[i]

            html_text = requests.get(demo).text
            soup = BeautifulSoup(html_text, 'lxml')
            info = soup.select('div.relative.lg\\:col-span-2 p')

            for p in info:
                text_parts = [t for t in p.strings if t.parent == p]
                text = ''.join(text_parts).strip()
                #print(text)
            #the above for loop will get all the text from the paragraph and will remove any inner tags present in it.
            Art[demo] = text

        for i in range(3):
            demo = links2[i]

            html_text = requests.get(demo).text
            soup = BeautifulSoup(html_text, 'lxml')
            info = soup.select("div.entry-content.wp-block-post-content.is-layout-constrained.wp-block-post-content-is-layout-constrained p")

            for p in info:
                text = p.get_text(strip=True)
            
            Art[demo] = text


        #print(Art)
        return Art

#o1 = GetData()
#o1.get_data()

