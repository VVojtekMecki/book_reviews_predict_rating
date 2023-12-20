from reviewsParser import ReviewsParser
import pickle


reviewsList = []

reviewsDataCollected = []

reviewsParser = ReviewsParser(reviewsList)

for url in reviewsParser.links:
    reviews = reviewsParser.getReviewsFromUrl(url)
    for review in reviews:
        reviewsDataCollected.append(review)
        
with open("reviewsDictList.pkl", 'wb') as file:
    pickle.dump(reviewsDataCollected, file)