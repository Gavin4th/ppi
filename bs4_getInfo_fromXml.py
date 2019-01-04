'''
  @Author: DongGaocai 
  @Date: 2018-12-27 10:53:33 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-27 10:53:33 
'''
# function:use the bs4 library to extration the info we need from the corpus whose format is xml
# tag,NavigableString,BeautifulSoup,Comment
from bs4 import BeautifulSoup
import re


entity_dict = dict() # entity[id]  = entity
sentence_dict = dict() # the same as above
total_entity_list = list() # search the list to transform the entity to other
idPattern = re.compile(r'(.*)\.e') # to find the sentence's id according to the pair's id
charoffsetPattern = re.compile(r'(.*)-(.*)') # find two position
with open("AImed.xml","r",encoding="utf-8") as f:
    lines = f.readlines()
    with open("corpus.txt","a",encoding='utf-8') as file:
        for line in lines:
            soup = BeautifulSoup(line,'lxml')
            if soup.sentence:
                sentence_dict[soup.sentence['id']] = soup.sentence['text']
            if soup.entity:
                # build the dict
                entity_dict[soup.entity['id']] = soup.entity['charoffset']
                # first = charoffsetPattern.search(offset).group(1)
                # second = charoffsetPattern.search(offset).group(2)
                # build the list
                total_entity_list.append(soup.entity['text'])
            if soup.pair:
                interaction = soup.pair['interaction']
                e1_offset = entity_dict[soup.pair['e1']]
                e2_offset = entity_dict[soup.pair['e2']]
                e1_begin_pos = int(charoffsetPattern.search(e1_offset).group(1))
                e1_end_pos = int(charoffsetPattern.search(e1_offset).group(2))
                e2_begin_pos = int(charoffsetPattern.search(e2_offset).group(1))
                e2_end_pos = int(charoffsetPattern.search(e2_offset).group(2))
                sentenceID = idPattern.search(soup.pair['e1']).group(1)
                sentence = sentence_dict[sentenceID]
                #print(e1_begin_pos,e1_end_pos,e2_begin_pos,e2_end_pos)
                # sentence = sentence.replace(sentence[e1_begin_pos:e1_end_pos+1],'entityone')
                replace_sentence = sentence[0:e1_begin_pos] + ' entityone ' + sentence[e1_end_pos+1:e2_begin_pos]+' entitytwo '+sentence[e2_end_pos+1:len(sentence)]
                for item in total_entity_list:
                    if item in replace_sentence and item != sentence[e1_begin_pos:e1_end_pos+1] and item != sentence[e2_begin_pos:e2_end_pos+1]:
                         replace_sentence = replace_sentence.replace(item,' otherprotein ')
                replace_sentence = replace_sentence.replace(',','')
                replace_sentence = replace_sentence.replace('.','')
                replace_sentence = replace_sentence.replace('/','')
                replace_sentence = replace_sentence.replace('-','')
                replace_sentence = replace_sentence.replace('(','')
                replace_sentence = replace_sentence.replace(')','')
                replace_sentence = replace_sentence.replace(':','')
                file.write(replace_sentence+'\t'+interaction+'\n')
    print('file saved!')






