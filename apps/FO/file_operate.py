# !/bin/env python
# -*- coding=utf-8 -*-


import os
import shutil

import sys  # 导入sys模块

sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000


class File_Ope():
    def __init__(self):
        pass

    def lastname(self, path):
        """
        遍历文件后缀名
        返回左右后缀名
        """
        ln_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if "." in file:  # 此处加判断,避免类似于000avrdfads1 文件夹下 存储000avrdfads1
                    a = file.split(".")[-1]
                    if a not in ln_list:
                        ln_list.append(a)
        return ln_list

    def makedir(self, path):
        """
        创建文件夹
        """
        for i in self.lastname(path):
            target = f'{path}{os.sep}{i}'
            if os.path.exists(target):
                # print("存在")
                pass
            else:
                os.mkdir(target)

    def return_road(self, path):
        """
        返回文件名称的绝对路径
        返回存储文件的路径
        老路径,新路径
        """
        for root, dirs, files in os.walk(path):
            new_path_list = []
            old_path_list = []
            for file in files:
                old_path = os.path.join(root, file)
                # print(old_path.split("."))
                if old_path not in old_path_list:
                    old_path_list.append(old_path)
                for j in self.lastname(path):
                    new_path = path + os.sep + j
                    if new_path not in new_path_list:
                        new_path_list.append(new_path)
            return old_path_list, new_path_list

    def re_all_file(self, path):
        ln_list = []
        for root, dirs, files in os.walk(path):
            for f in files:
                m = os.path.join(root, f)
                if m not in ln_list:
                    ln_list.append(m)

        return ln_list

    def move_file(self, path):
        for new in self.return_road(path)[1]:
            m = new.split(os.sep)[-1]  # exe
            # print( j.split(os.sep)[-1] )
            for old in self.re_all_file(path):  # exe
                n = old.split(os.sep)[-1].split(".")[-1]
                if n == m:
                    self.makedir(path)
                    # print(old,new)
                    print(f"从{old}复制到{new}文件夹")
                    try:
                        shutil.copy(old, new)
                    except Exception as e:
                        print(e)

if __name__ == '__main__':
    path = r"E:\OIP1"
    File_Ope().move_file(path)
