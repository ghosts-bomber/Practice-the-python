def file_write(fname):
    

    f = open(fname + '.txt','x')
    print('单独输入\‘:w\’保存退出')
    while True:
        shuru = input()
        if shuru != ':w':
            f.write('%s\n' %shuru)
        else:
            break

    f.close()

fname = input('请输入文件名：')
file_write(fname)
