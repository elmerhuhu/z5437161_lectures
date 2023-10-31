""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg

# 注意需要有toolkit_config这个文件在根目录下面，没有的需要去补充
# cfg.DATADIR表示的是.toolkit\data这个文件夹
SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')


# ---------------------------------------------------------------------------- 
#   Opening the `SRCFILE` and reading its contents with the read method
# ---------------------------------------------------------------------------- 
# This will open the file located at `SRCFILE` and return a handler (file
# object):
fobj  = open(SRCFILE, mode= 'r')
# print(type(fobj))
# print(fobj)# 无法被打印

# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts  = fobj.read()
# print(type(cnts))
# print(cnts)# 打印所有内容

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
# print(cnts[:20])# 相当于这个文件第一行

# Check if the file is closed
# print(fobj.closed)

# Close the file
# fobj.close()
# print(fobj.closed)
# 以上是传统的读取文件的方式，但注意我们写代码过程中不会这样用


# ---------------------------------------------------------------------------- 
#   Comparing different approaches to get the contents
# ---------------------------------------------------------------------------- 
# Remember that we previously closed the file so we need to open it again
fobj = open(SRCFILE, mode='r')
# Contents using `.read`
# cnts = fobj.read()
# print(f"First 20 characters in cnts: '{cnts[:20]}'")

# Start with an empty string
# Iterate over each line of fobj # <comment>
# Add line to the string `cnts_copy` # <comment>

# cnts_copy = ''
# for line in fobj:
#    cnts_copy += line
# print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# print(type(cnts_copy))

# close the file
# fobj.close()

#以上for-loop循环读取文件内容是较为常用的方法


#一行一行读取的方法
# ---------------------------------------------------------------------------- 
#   Reading one line at a time
# ---------------------------------------------------------------------------- 
fobj = open(SRCFILE, mode='r')

# Read the first line
# first_line = next(fobj) #读取下一行
# print(first_line)

# After that, the fobj iterator now points to the second line in the file

# second_line = next(fobj)
# print(second_line)
#
#
# for line in fobj:
#    print(f"fobj now point to : '{line}'")
#    break


# close the file
# fobj.close()

#still，以上在写码时候均不推荐，需要使用下列context managers


#context managers可想象为一个箱子，所有操作在箱子里面完成，不和箱子外面有所交互
#一旦python解释器完成这个箱子里面的操作，文件会自动关闭
#也就说，在这个箱子以外文件都不是打开的状态
#保证我们的文件在不用到的时候是关闭的，只在我们读写的时候才是打开的

# ---------------------------------------------------------------------------- 
#   Using context managers
# ---------------------------------------------------------------------------- 
# Instead of fobj = open(SRCFILE, mode='r'), use a context manager:

# with open(SRCFILE, mode='r') as fobj:# context managers,下面的执行需要缩进，箱子里面
#    cnts = fobj.read()
#    # Check if the object is closed inside the manager
#    print(f'Is the fobj closed inside the manager? {fobj.closed}')


# Notice that we did not close the object when using a context manager
# But after exiting the context manager, the file will automatically close

# print(f'Is the fobj closed after we exit the manager? {fobj.closed}')

#以上需要熟悉，with open(文件路径, mode='r'/'w') as fobj(变量名，可修改):


# ---------------------------------------------------------------------------- 
#   Writing content to a file
# ---------------------------------------------------------------------------- 
# Auxiliary function to print the lines of a file
def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as 
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")


#  This will create the file located at `DSTFILE` and write some content to it

# with open(DSTFILE, mode='w') as fobj:
#     fobj.write('This is a line')
#

# Exiting the context manager will close the file
# We can then print its contents
# print_lines(DSTFILE)


# If you open the same file again in writing mode, the line we wrote above
# will be erased:

# 之前的文件被覆盖
# with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is another line')
#
# print_lines(DSTFILE)
#


# ---------------------------------------------------------------------------- 
#   The write method does not add terminate the line.
# ---------------------------------------------------------------------------- 

# 同时写入多句
# with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line')
#    fobj.write('This is a another line')
# print_lines(DSTFILE)


# ---------------------------------------------------------------------------- 
#   Notice that the write method does not add a newline character (\n). You
#   must add it yourself:
# ---------------------------------------------------------------------------- 

# 加入换行符号：
# with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
# print_lines(DSTFILE)
#可检查newfile
#但打印print的时候line0和line1之间存在空行，是python的特点
#可用rstrip()去除，下例

# ---------------------------------------------------------------------------- 
# Auxiliary function to print the lines of a file
# ---------------------------------------------------------------------------- 
def print_lines_rstrip(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as 
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")

#
# with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
# print_lines_rstrip(DSTFILE)
#

# 总结：需要掌握的就是with open

# 之后的quiz中讲
# ---------------------------------------------------------------------------- 
#   Quiz: Create the save_open function here
# ---------------------------------------------------------------------------- 
def safe_open(pth, mode):
    """ Opens the file in `pth` using the mode in `mode` and returns 
    a file object. 

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading, 
        and 'a' for appending. See the `open` function for more options.
    """
    pass








