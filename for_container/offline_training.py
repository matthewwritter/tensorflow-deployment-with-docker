import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

training_data = pd.DataFrame([
        ["this is a short sentence", 0],
        ["this is a long sentence with lots of words in it that makes it annoying", 1],
        ["this is another short sentence", 0],
        ["this is sentence is too long for people to like so it should be selected against", 1],
], columns = ['txt', 'is_too_long'])

def preprocessor(txt):
    return len(txt.split())

training_data['txt_len'] = training_data.txt.apply(preprocessor)

lr = LogisticRegression()

lr.fit(training_data[['txt_len']].values, training_data['is_too_long'])

test_txt1 = "now I want to see whether this sentence is too long for people to want to read"
test_txt2 = "maybe short enough?"

with open('basic_model.pkl', 'wb') as f:
    pickle.dump(lr, f)

print(training_data)
print(lr)
print(lr.predict([[preprocessor(test_txt1)]]))
print(lr.predict([[preprocessor(test_txt2)]]))

with open('basic_model.pkl', 'rb') as f:
    lr2 = pickle.load(f)

print(lr2.predict([[preprocessor(test_txt1)]]))
print(lr2.predict([[preprocessor(test_txt2)]]))



