"""
文件操作的作用就是把一些内容(数据)存储存放起来，
可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力
"""

# 打开 open()
f = open('03test.txt', 'w')

# 读写操作
f.write('aaa')

# 关闭
f.close()