import nltk
from get_feature import *
import numpy as np

str = 'physical interaction entityone otherprotein coactivator CREB not sufficient repression entitytwo mediated transcription'
text = nltk.word_tokenize(str)
result = nltk.pos_tag(text)
intial_vector = np.zeros(33)
for item in result:
    intial_vector += get_pos_feature(item[1])

print(intial_vector)

