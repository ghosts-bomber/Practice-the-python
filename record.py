def split_file(f):
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:5] != '=====':
            (role,line_spoken) = each_line.split(':',1)
            if role == 'aaa':
                boy.append(line_spoken)
            else:
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)
            count += 1
            boy = []
            girl = []
    save_file(boy,girl,count)
def save_file(boy,girl,count):
    file_boy_name = '%s%c%d.txt' %('aaa','_',count)
    file_girl_name = '%s%c%d.txt' %('bbb','_',count)
    f1 = open(file_boy_name,'xt')
    f1.writelines(boy)
    f2 = open(file_girl_name,'xt')
    f2.writelines(girl)
    f1.close()
    f2.close()

f = open('a.txt','rt')
split_file(f)
f.close()
