l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn1(i):
    return i % 2 == 0


def fn(func, lst):
    new_list = []
    for n in lst:
        if func(n):
            new_list.append(n)
    return new_list


print(fn(fn1, l))

print('-' * 20)

# filter()
# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数：
#  1.函数，根据该函数来过滤序列（可迭代的结构）
#  2.需要过滤的序列（可迭代的结构）
# 返回值：
#   过滤后的新序列（可迭代的结构）

fn2 = lambda a, b: a + b

r = filter(lambda i: i > 5, l)
print(type(r))
print(list(r))

# map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回

r = map(lambda i: i ** 2, l)
print(list(r))

# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ， key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小

l = ['bb', 'aaaa', 'c', 'ddddddddd', 'fff']
l.sort(key=len)
print(l)

l = [2, 5, '1', 3, '6', '4']
l.sort(key=int)
print(l)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序
#   并且使用sorted()排序不会影响原来的对象，而是返回一个新对象

l = [2, 5, '1', 3, '6', '4']
print('排序前:', l)
print(sorted(l, key=int))
print('排序后:', l)

"""
闭包
"""
print('闭包' + '-' * 20)


def make_average():
    nums = []

    def averager(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return averager


averager = make_average()
print(averager(20))

"""
装饰器
"""
print('装饰器' + '-' * 20)


def add(a, b):
    '''
        求任意两个数的和
    '''
    r = a + b
    return r


def mul(a, b):
    '''
        求任意两个数的积
    '''
    r = a * b
    return r


def fn():
    print('我是fn函数....')


def begin_end(old):
    def new_function(*args, **kwargs):
        print('开始执行...')
        result = old(*args, **kwargs)
        print('结束执行...')
        return result

    return new_function


def fn3(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    '''

    # 创建一个新函数
    def new_function(*args, **kwargs):
        print('fn3装饰~开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('fn3装饰~执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


f = begin_end(fn)
f()
print('=======')


@fn3
@begin_end
def hello_world():
    print('hello world!')


hello_world()
