'''
  @Author: DongGaocai 
  @Date: 2019-01-01 13:32:45 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2019-01-01 13:32:45 
'''
import warnings,os,pickle,nltk
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import Word2Vec
from gensim.models import FastText
from gensim.models.word2vec import LineSentence
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
from get_feature import *


# 总特征list
total_feature_list = list()
# 总标签list
label_list = list()
with open("label.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        label = line.strip()
        label_list.append(label)

model = FastText.load("AImed.model")
with open("further corpus.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        sentence2list = line.strip().split()
        temp = list()
        initial_vector = np.zeros(20)
        # initial_pos_vector = np.zeros(33)
        # 实体e1的向量
        v1 = model.wv['entityone']
        for item in v1:
            temp.append(item)
        # 句子的向量
        for word in sentence2list:
            vector = model.wv[word]
            initial_vector += vector
        for item in initial_vector/len(sentence2list):
            temp.append(item)
        # 实体e2的向量
        v2 = model.wv['entitytwo']
        for item in v2:
            temp.append(item)
        # 其他实体的向量
        other_vector = model.wv['otherprotein']
        for item in other_vector:
            temp.append(item)
        # break
        # pos 的向量
        #--------------------------------------------------
        # text = nltk.word_tokenize(line.strip())
        # pos_result = nltk.pos_tag(text)
        # for item in pos_result:
        #     pos_vector = get_pos_feature(item[1])
        #     initial_pos_vector += pos_vector
        # for item in initial_pos_vector/len(pos_result):
        #     temp.append(item)
        #--------------------------------------------------
        pos_vector = get_pos_feature(line.strip())
        for item in pos_vector:
            temp.append(item)
        total_feature_list.append(temp)
        
x_train, x_test, y_train, y_test = train_test_split(np.array(total_feature_list),np.array(label_list),test_size = 0.25)
clf = SVC(C=1.0, cache_size=200, class_weight='balanced', coef0=0.0, decision_function_shape='ovr',degree=3,
gamma='auto',kernel='rbf',max_iter=-1,probability=False,random_state=None, shrinking=True,
tol=0.001, verbose=False)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(classification_report(y_test,y_pred))


        

    