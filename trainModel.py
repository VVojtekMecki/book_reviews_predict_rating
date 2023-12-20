import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import json

# with open("reviewsDictList.pkl", 'rb') as file:
#     reviewsDicts = pickle.load(file)
    
with open('reviewsDictList.json', 'r') as file:
    data = json.load(file)

nlp = spacy.load("en_core_web_md")

reviews = []
ratings = []

for review in data:
    # removes html tags, new line, dots and other digits
    text = re.sub(r'<[^>]+>|\\n|\.|,|:|&|;|-|"', '', review['text'])
    
    # tokenize
    tokens = nlp(text)
    # tokens into one string
    processedText = ' '.join([token.text for token in tokens if not token.is_stop])
    reviews.append(processedText)
    
    ratings.append(int(review['rating']))

y = [[rating] for rating in ratings]
# Convert a collection of raw documents to a matrix of TF-IDF features.
vectorizer = TfidfVectorizer(max_features=16384)
X = vectorizer.fit_transform(reviews)

# creating the test i train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

joblib.dump(model, 'reviewModel.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
