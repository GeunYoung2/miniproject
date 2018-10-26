import nltk
import numpy as np
import pandas as pd
import tensorflow as tf

# nltk.download('averaged_perceptron_tagger')
# nltk.download("gutenberg")
# nltk.download('punkt')
# nltk.download('reuters')
# nltk.download("stopwords")
# nltk.download("webtext")
# nltk.download("wordnet")

#
data=pd.read_csv("data/mbti_1.csv",delimiter=',')
x=data.iloc[:,[0]] # (8675, 1)
y=data.iloc[:,[1]]# (8675, 1)

# print(y.iloc[0])

from nltk.tokenize import WordPunctTokenizer
for i in range(len(y)):
    string=y.iloc[i]
    tokenizer = WordPunctTokenizer()
    print(tokenizer.tokenize(string))

    # string=y.iloc[i]
    # tokenizer = RegexpTokenizer("\s+", gaps=True)
    # print(tokenizer.tokenize(string))

    # tokenizer = RegexpTokenizer("[\w']+")
    # print(tokenizer.tokenize(string))


    # english_stops = set(stopwords.words('english'))
    # print([word for word in words if word not in english_stops])

# for i in range

# x_scale = x.copy()
# for i in range(len(x.iloc[0])):
#     X_scale.iloc[:,i] = standard(X.iloc[:, i])
# y_scale = standard(y)

