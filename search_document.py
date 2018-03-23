import os
def search_file(start_dir,target):
    os.chdir(start_dir)
    #Change the current working directory to path

    for each_file in os.listdir(os.curdir):
        # os.curdir The constant string used by the operating system to refer to the current directory.

        if each_file == target:
            print(os.getcwd() + os.sep + each_file)#使用os.sep是程序标准
            # os.getcwd  Return a string representing the current working directory.
            # os.sep The character used by the operating -
            # -system to separate pathname components.
        if os.path.isdir(each_file):
            search_file(each_file,target) #递归调用
            os.chdir(os.pardir) #递归调用后切记返回上一层目录
            # os.pardir The constant string used by the operating system to refer to the parent directory. 


start_dir = input('请输入待查找的初始目录:')
target = input('请输入需要查找的目标文件：')
search_file(start_dir,target)
