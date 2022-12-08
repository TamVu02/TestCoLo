
import json
from underthesea import word_tokenize

def tsv2json(input_file,output_file):
    arr = []
    file = open(input_file, 'r',encoding='utf-8')
    id=0
    titles=['article_id','text','summary']

    while True:
        line = file.readline()
        if not line:
            break

        part_token=line.split('\t')

        text_sent_token=part_token[0].split('.')
        text_txt=''
        for sent in text_sent_token:
            if(sent!=''):
                sent=word_tokenize(sent,format='text')
                text_txt=text_txt+sent+'. '

        sum_sent_token=part_token[1].split('.')
        sum_txt=''
        for sent in sum_sent_token:
            if(sent!='\n'):
                sent=word_tokenize(sent,format='text')
                sum_txt=sum_txt+sent+'. '

        line = str(id) +'\t'+text_txt+'\t'+sum_txt

        d = {}
        for t,f in zip(titles,line.split('\t')):
            d[t] = f.strip()
        arr.append(d)
        id=id+1

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(json.dumps(arr, indent=4,ensure_ascii=False),)

import os
print('========== Converting tsv file to jsonl file ==========\n')
for dirname, _, filenames in os.walk(r"C:\Users\LAPTOP88\Downloads\Wikilingual\Wikilingual"):
    for filename in filenames:
        filepath=os.path.join(dirname, filename)
        input_filename = filepath
        output_filename = filename.replace('.tsv','')+'.jsonl'
        tsv2json(input_filename,output_filename)
        print('Successfully save to data',output_filename,'\n')

