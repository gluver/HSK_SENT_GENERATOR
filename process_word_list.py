# %%
import os 
import argparse
from collections import Counter
import re

def find_word_list(folder_path):
    pattern = r"hsk.*_+list"
    full_paths=[]
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if re.match(pattern, filename):
                full_path = os.path.join(root, filename)
                full_paths.append(full_path)
    return full_paths        
#%%
word_counter=Counter()
wl_full_paths=find_word_list('.')
for path in wl_full_paths:
    with open(path,'r') as f:
        wl=f.readlines()
        wl=[w.rstrip() for w in wl]
        word_counter.update(wl)
print(word_counter.most_common(20) )       

#%%
len(word_counter),wl_full_paths
#%%
def print_batches(lst, batch_size):
    for i in range(0, len(lst), batch_size):
        batch = lst[i:i+batch_size]
        if len(batch) == batch_size:
            print(batch)
        else:
            print(lst[i:])

        
print_batches(list(word_counter.keys()),200)
#%%
def write_in_batches(data, batch_size, filename):
    with open(filename, 'w') as f:
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            if len(batch) != batch_size:
                batch=data[i:]
            line = ','.join(batch) + '\n'
            f.write(line)
            
write_in_batches(list(word_counter.keys()),400,'temp.txt')
# if __name__=='__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--wordlist_dir',type=str,default='./')
#     args=parser.parse_args()
#     wl_full_paths=find_word_list(args.wordlist_dir)
#     for path in wl_full_paths:
#         with open(path,'r') as f:
#             wl=f.readlines()
    
    
# %%
