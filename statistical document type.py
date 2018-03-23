import os

all_files = os.listdir(os.curdir) #使用os.curdir表示当前目录更标准
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file): #文件的话返回Ture
        type_dict.setdefault('文件夹',0)
      #If key is in the dictionary, return its value. If not,
      #insert key with a value of default and return default. default defaults to None.
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        #splitext('.cshrc') returns ('.cshrc', '').

        type_dict.setdefault(ext,0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个'%(each_type,type_dict[each_type]))
