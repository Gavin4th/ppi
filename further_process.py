'''
  @Author: DongGaocai 
  @Date: 2018-12-27 16:28:17 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-27 16:28:17 
'''
# further deal with the corpus
'''
Following the best practices in the literature, we have trimmed down 
each sentence to a smaller segment that contains the 2 entities, the 
words between the entities, and a few words before and after. The purpose 
of the trimming operation is to remove the parts of the sentence that 
aren’t relevant to the relation extraction.
'''
from nltk.corpus import stopwords


english_stopwords = stopwords.words('english')
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','/']

def Normalization(string):
    # to delete some punctuations
    for punctuation in english_punctuations:
        if punctuation in string:
            string = string.replace(punctuation,'')
    # change the word into the lower case
    string = string.lower()
    # judge whether the string is composed with digital only
    if string.isdigit():
        string = ''
    # remove the stirng that has only two or one characters
    if len(string) <= 2:
        string = ''
    # remove the stopwords
    if string in english_stopwords:
        string = ''
    return  string

window_size = 3 # the num of word the before and after the entity
with open('corpus.txt','r',encoding = 'utf-8') as f:
    with open('further corpus.txt','a',encoding = 'utf-8') as file:
        content = f.readlines()
        for line in content:
            line = line.split('\t')
            sentence2list = line[0].split()
            # make sure that wo don't overflow but using the min and max methods
            first_index = max(sentence2list.index('entityone')-window_size,0)
            second_index = min(sentence2list.index('entitytwo')+window_size,len(sentence2list))
            trimmed_sentence = sentence2list[first_index:second_index]
            for word in trimmed_sentence:
                # Normalization
                trimmed_sentence[trimmed_sentence.index(word)] = Normalization(word)
                # remove the none object
                for item in trimmed_sentence:
                    if item == '':
                        trimmed_sentence.remove(item)  
            file.write(' '.join(trimmed_sentence)+'\n')
        print('file saved ok!')
                

