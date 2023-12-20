from reviewsParser import ReviewsParser
import pickle
import json

lubimyCzytacLinks = [
	'https://lubimyczytac.pl/ksiazki/opinie?page=1&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=2&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=4&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=5&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=6&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=7&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=8&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=9&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=10&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=11&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=12&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=13&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=14&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=16&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=17&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=18&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=21&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=22&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=23&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=24&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=25&listId=listId_13616_1&sortBy=youngest&rating%5B0%5D=0&rating%5B1%5D=10&showFirstLetter=0&paginatorType=Standard&isHighlightReview=1&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=4&listId=listId_13616_1&sortBy=popular&rating%5B0%5D=1&rating%5B1%5D=6&showFirstLetter=0&paginatorType=Standard&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=5&listId=listId_13616_1&sortBy=popular&rating%5B0%5D=1&rating%5B1%5D=6&showFirstLetter=0&paginatorType=Standard&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=13&listId=listId_13616_1&sortBy=popular&rating%5B0%5D=1&rating%5B1%5D=6&showFirstLetter=0&paginatorType=Standard&paginatorType=Standard',
    'https://lubimyczytac.pl/ksiazki/opinie?page=15&listId=listId_13616_1&sortBy=popular&rating%5B0%5D=1&rating%5B1%5D=6&showFirstLetter=0&paginatorType=Standard&paginatorType=Standard',
]

reviewsDataCollected = []

reviewsParser = ReviewsParser(lubimyCzytacLinks)

for url in reviewsParser.links:
    reviews = reviewsParser.getReviewsFromUrl(url)
    for review in reviews:
        reviewsDataCollected.append(review)
        
with open("reviewsDictList.pkl", 'wb') as file:
    pickle.dump(reviewsDataCollected, file)
    
with open("reviewsDictList.json", 'w') as json_file:
    json.dump(reviewsDataCollected, json_file, indent=2)