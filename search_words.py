import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys) #由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置。'%(each_key,str(key_dict[each_key])))

def pos_in_line(line,key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1) # 用户的角度是从1开始数
        begin = line.find(key,begin + 1) # 从下一个位置继续查找
    # bytearray.find(sub[, start[, end]]): Return the lowest index in the data where the subsequence
    # sub is found, such that sub is contained in the slice s[start:end]. Optional arguments start and
    # end are interpreted as in slice notation. Return -1 if sub is not found.


    return pos

def search_in_file(file_name,key):
    f = open(file_name)
    count = 0 # 记录行数
    key_dict = dict() # 字典，用户存放key所在行数对应的具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line,key) # key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict

def search_file(key,detail):
    all_files = os.walk(os.getcwd())
    # os.walk() Generate the file names in a directory tree by walking
    # the tree either top-down or bottom-up
    #print(type(all_files)) # 测试 是一个类
    txt_files = []

    for i in all_files:
        #print(type(i)) #测试为一个元组
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt': # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0],each_file)
                # os.path.join(path, *paths):Join one or more path components intelligently
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file,key)
        if key_dict:
            print('====================================================')
            print('在文件【%s】中找到关键字【%s】'%(each_txt_file,key))
            if detail in ['Yes','YES','yes']:
                print_pos(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES、NO）：'%key)
search_file(key,detail)
