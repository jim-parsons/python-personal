# 创建一个变量来保存你的名字
from time import time

name = '孙悟空'

# 使用四种方式来输出，欢迎 xxx 光临
# 拼串
print('欢迎 '+name+' 光临！')
# 多个参数
print('欢迎',name,'光临！')
# 占位符
print('欢迎 %s 光临！'%name)
# 格式化字符串
print(f'欢迎 {name} 光临！')

# 字符串的复制（将字符串和数字相乘）
a = 'abc'
# * 在语言中表示乘法
# 如果将字符串和数字相乘，则解释器会将字符串重复指定的次数并返回
a = a * 20

print(a)


a = True
a = False
print('a =',a)

# 布尔值实际上也属于整型，True就相当于1，False就相当于0
print(1 + False)


# 类型转换四个函数 int() float() str() bool()
# int() 可以用来将其他的对象转换为整型
# 规则：
#   布尔值：True -> 1   False -> 0
#   浮点数：直接取整，省略小数点后的内容
#   字符串：合法的整数字符串，直接转换为对应的数字
#           如果不是一个合法的整数字符串，则报错 ValueError: invalid literal for int() with base 10: '11.5'
#   对于其他不可转换为整型的对象，直接抛出异常 ValueError
# float() 和 int()基本一致，不同的是它会将对象转换为浮点数
# str() 可以将对象转换为字符串
#  True -> 'True'
#  False -> 'False'
#  123 -> '123'
#  。。。
#  bool() 可以将对象转换为布尔值，任何对象都可以转换为布尔值
#   规则：对于所有表示空性的对象都会转换为False，其余的转换为True
#       哪些表示的空性：0 、 None 、 '' 。。。
print(10 / 3)
print(10 // 3)
print(5 // 2)
print('2' > '1') # T
print('2' > '11') # T
print('2' > '21') # F

# 在Python中可以对两个字符串进行大于（等于）或小于（等于）的运算，
#   当对字符串进行比较时，实际上比较的是字符串的Unicode编码
#   比较两个字符串的Unicode编码时，是逐位比较的
#   利用该特性可以对字符串按照字母顺序进行排序，但是对于中文来说意义不是特别大
#   注意：如果不希望比较两个字符串的Unicode编码，则需要将其转换为数字然后再比较
#   0061 > 0062

print(1 and 2) # 1代表true

# and高 or高
# 如果or的优先级高，或者两个运算符的优先级一样高
#   则需要先进行或运算，则运算结果是3
# 如果and的优先级高，则应该先计算与运算
#   则运算结果是1
print(1 or 2 and 3)
print(10 < 20 > 15)

# username = input('请输入你的用户名:')
#
# if username == 'admin':
#     print('欢迎管理员光临！')


i = 0

while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print(f'{j}*{i}={i*j} ', end='')

    print()


start = time()
i = 2
while i <= 100000:
    flag = True
    j = 2
    while j <= i**0.5:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        pass
    i += 1

print("程序执行花费了：",time() - start , "秒")
