import requests
from bs4 import BeautifulSoup
import re
import json
from langdetect import detect


class ReviewsParser:
    def __init__(self, links: list[str]):
        self.links = links

    @staticmethod
    def isTextEng(text):
        return detect(text) == 'en'

    def getReviewsFromUrl(self, url) -> list[dict]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        scriptData = soup.find('script', id='__NEXT_DATA__')
        reviews = []
        
        if scriptData is not None:
            scriptText = scriptData.text

            try:
                jsonScriptText = json.loads(scriptText)
                jsonReviews = jsonScriptText['props']['pageProps']['apolloState'] 
                
                for entry in jsonReviews:
                    match = re.match('^Review.*', entry)
                    if match:
                        append_dict = {"text": str(jsonReviews[entry]['text']),
                                    "rating": str(jsonReviews[entry]['rating'])}
                        reviews.append(append_dict)
                
                #parse only english reviews        
                english_reviews = [review for review in reviews if self.isTextEng(review['text'])]
                return english_reviews

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return reviews
        else:
            return reviews

