'''
  @Author: DongGaocai 
  @Date: 2018-12-28 16:38:54 
  @Last Modified by: DongGaocai 
  @Last Modified time: 2018-12-28 16:38:54 
'''
with open("corpus.txt","r",encoding="utf-8") as f1:
    with open("label.txt","a",encoding="utf-8") as f2:
        content = f1.readlines()
        for line in content:
            line = line.split('\t')[1].strip()
            if line == 'False':
                f2.write('0'+'\n')
            else:
                f2.write('1'+'\n')
    print('file saved!')
            