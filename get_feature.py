'''
  @Author: DongGaocai 
  @Date: 2018-12-29 15:51:12 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-29 15:51:12 
'''
import warnings, os, pickle, nltk
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import FastText
from sklearn.feature_extraction.text import CountVectorizer


vectorizer = CountVectorizer()
# pos list
# pos_list = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP',
# 'NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP','TO','UH','VB','VBD','VBG','VBN',
# 'VBP','VBZ','WDT','WP','WP$','WRB']
# result = vectorizer.fit_transform(pos_list)

# get the fasttext word vector
def get_fasttext_feature(word):
    model = FastText.load("AImed.model")
    vector = model.wv[word]
    return vector
# get the pos vector
# sentences = list()
pos_tag = list()
with open("further corpus.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        temp = list()
        line = line.strip()
        # sentences.append(line)
        text = nltk.word_tokenize(line)
        pos_result = nltk.pos_tag(text)
        for item in pos_result:
            temp.append(item[1])
        pos_tag.append(" ".join(temp))

result = vectorizer.fit(pos_tag) 

def get_pos_feature(sentence):
    # vector = vectorizer.transform([pos]).toarray()[0]
    # return vector
    templist = list()
    word_token = nltk.word_tokenize(sentence)
    p_result = nltk.pos_tag(word_token)
    for item in p_result:
        templist.append(item[1])
    str = " ".join(templist)
    return vectorizer.transform([str]).toarray()[0]




    
   




