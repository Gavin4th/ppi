'''
  @Author: DongGaocai 
  @Date: 2018-12-29 15:13:54 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-29 15:13:54 
'''
import warnings, os, pickle
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import FastText


if not os.path.exists("AImed.model"):
    # 将语料库转化为fasttext需要的格式
    package = list()
    with open("further corpus.txt","r",encoding="utf-8") as f:
        content = f.readlines()
        for sentence in content:
            package.append(sentence.split())
    model = FastText(package,size=20,window=3,min_count=1,iter=10)
    model.save("AImed.model")
        
    


