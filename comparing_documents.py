
def bijiao(fname1,fname2):
    f1 = open(fname1,'r')
    f2 = open(fname2,'r')
    count = 0 #统计行数
    differ = [] #统计不一样的行数
    for line1 in f1:
        line2 = f2.readline() #记住这里的编程变换方法
        count += 1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
                   

fname1 = input('请输入第一个文件名：')
fname2 = input('请输入第二个文件名：')
differ = bijiao(fname1,fname2)
if len(differ) == 0:
    print('两个文件完全一样')
else:
    print('两个文件共有【%d】处不同'%len(differ))
    for each in differ:
        print('第%d行不一样'%each)
