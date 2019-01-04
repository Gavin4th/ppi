'''
  @Author: DongGaocai 
  @Date: 2018-12-29 15:16:57 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-29 15:16:57 
'''
# count the number of the words in the txt, including drop the same words
L = []
with open('further corpus.txt',encoding='utf-8') as f:
    text = f.read()
    L = L + text.split()
print('一共有{}个词'.format(len(L)))
del_same_list = list(set(L))
print('去重后有{}个词'.format(len(del_same_list))) 

# 一共有63462个词
# 去重后有2573个词