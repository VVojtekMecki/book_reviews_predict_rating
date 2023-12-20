from reviewsParser import ReviewsParser
import pickle
import json


reviewsList = [
    'https://www.goodreads.com/book/show/929782/reviews',
    'https://www.goodreads.com/book/show/46170/reviews',
    'https://www.goodreads.com/book/show/1232/reviews',
    'https://www.goodreads.com/book/show/100915/reviews',
    'https://www.goodreads.com/book/show/14318/reviews',
    'https://www.goodreads.com/book/show/17274667/reviews',
    'https://www.goodreads.com/book/show/2767052/reviews',
    'https://www.goodreads.com/book/show/5907/reviews',
    'https://www.goodreads.com/book/show/1003725/reviews',
    'https://www.goodreads.com/book/show/41865/reviews',
    'https://www.goodreads.com/book/show/55702231/reviews',
    'https://www.goodreads.com/book/show/4934/reviews',
    'https://www.goodreads.com/book/show/18796/reviews',
    'https://www.goodreads.com/book/show/70401/reviews',
    'https://www.goodreads.com/book/show/22557520/reviews',
    'https://www.goodreads.com/book/show/581125/reviews'
]

reviewsDataCollected = []

reviewsParser = ReviewsParser(reviewsList)

for url in reviewsParser.links:
    reviews = reviewsParser.getReviewsFromUrl(url)
    for review in reviews:
        reviewsDataCollected.append(review)
        
with open("reviewsDictList.pkl", 'wb') as file:
    pickle.dump(reviewsDataCollected, file)
    
with open("reviewsDictList.json", 'w') as json_file:
    json.dump(reviewsDataCollected, json_file, indent=2)