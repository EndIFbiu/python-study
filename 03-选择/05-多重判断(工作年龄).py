"""
if 条件1:
    条件1成立执行的代码1
    条件1成立执行的代码2
    ......
elif 条件2：
    条件2成立执行的代码1
    条件2成立执行的代码2
    ......
......
else:
    以上条件都不成立执行执行的代码
"""

age = int(input('请输入您的年龄：'))

if age < 16:
    print(f'您输入的年龄是{age}，童工')
elif (age >= 16) and (age < 65):
    print(f'您输入的年龄是{age}，合法')
else:
    print(f'您输入的年龄是{age}，退休年龄')
