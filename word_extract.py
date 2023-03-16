import re
import argparse

def extract_chinese_words(text):
    pattern = '[\u4e00-\u9fff]+' # match one or more Chinese characters
    return re.findall(pattern, text) 



if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input_file',type=str,default='hsk1_words_raw.txt')
    parser.add_argument('--output_file',type=str,default='temp.txt')
    args=parser.parse_args()
    with open(args.input_file,'r') as f1, open(args.output_file,'w') as f2 :
        word_list=extract_chinese_words(f1.read())
        f2.write("\n".join(word_list))
