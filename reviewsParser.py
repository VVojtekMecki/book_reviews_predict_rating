import codecs
import requests
from bs4 import BeautifulSoup


class ReviewsParser:
    def __init__(self, links: list[str]):
        self.links = links

    def getReviewsFromUrl(self, url) -> list[dict]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        reviews = []

        scriptData = soup.find('span', id='reviewListAllLoader')
        
        paragraphs = scriptData.find_all('p', class_='expandTextNoJS p-expanded js-expanded mb-0')
        
        rates = scriptData.find_all('span', class_="big-number")
        
        for id, rate in enumerate(rates):
            text = str(paragraphs[id].text.encode('utf-8').decode('unicode_escape').strip())
            text = codecs.decode(text, 'unicode_escape')
            
            dict = {
                'text': text,
                'rating': str(float(rate.text)/2)
            }
            reviews.append(dict)
            
        return reviews
        