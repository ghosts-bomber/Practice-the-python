def file_view(file_name,line_name):
    print('\n文件%s的前%s的内容如下：\n'%(file_name,line_name))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(),end = ' ')
    f.close()
file_name = input(r'请输入要打开的文件（C:\\text.txt）:')
line_num = input('请输入需要显示的文件前几行：')
file_view(file_name,line_num)
