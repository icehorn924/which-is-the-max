# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:38:04 2020

@author: Nelson
"""

import os
import numpy as np
import random, xlwt
import ntpath
#

#rootdir = 'E:/TEST/1-5'
#path_read = []    #path_read saves all executable files
directory_name=input("please input filename: ")
#directory_name='E:/TEST/1-5'
def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files
filenames=list_all_files(directory_name)
print("1、读取到文件夹中存在以下文件：")
for filename in filenames:
	print("\t"+filename)
#文件预览，确定要删除的行数量
max2=[]

for filename in filenames:
    i=0
    file_open_path=(filename)
    print(filename)
    f = open("Output.txt",'a')
    f.write(filename)
    f.write('\n')
    workbook=xlwt.Workbook(encoding='utf-8')
    worksheet=workbook.add_sheet('OHT')
    worksheet.write(0,0,label='编号')
    worksheet.write(0,1,label='最大值')


    with open(file_open_path,"r",encoding="utf-8") as file_project:
        list1=np.loadtxt(file_project,delimiter="\t",usecols=(2),dtype=float)
        #print(list1)
        list1.sort()
        n=len(list1)
        max1=list1[n-1]
    print(max1)
    #worksheet.write(i,1,label=max1)

    #参数对应行列值
    n=len(filenames)
    j=0
    for j in range(n):
        j=j+1
        worksheet.write(j,0,label=ntpath.basename(filenames[j-1])[:-14])
        worksheet.write(j,1,label=max1)
    workbook.save('Excel_test.xls')
    max2=str(max1)
    f = open("Label.txt",'a')
    f.write(max2)
    f.write('\n')
input("请输入什么退出")
