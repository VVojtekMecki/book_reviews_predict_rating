from reviewModelTool import ReviewModelTool

reviewModel = ReviewModelTool('reviewModel.joblib', 'vectorizer.joblib')

with open('testReview.txt', encoding='utf-8') as file:
    test_review = file.read()
    
reviewModel.predictReviewRating(test_review)