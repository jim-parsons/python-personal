def get_info(target):
    """获得一个对象的所有属性和方法，可以使用dir()函数"""
    print(dir(target))


def get_len(target):
    """调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法"""
    print(len(target))


class MyDog(object):

    def __len__(self):
        return 100


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


if __name__ == '__main__':
    get_info('ABC')
    get_len('Abc')

    print('============')
    dog = MyDog()
    print(len(dog))
    print('============')

    obj = MyObject()
    print(hasattr(obj, 'x'))
    print(obj.x)
    print('============')
    print(hasattr(obj, 'y'))
    print('============')
    setattr(obj, 'y', 19)  # 设置属性和值
    print(getattr(obj, 'y'))

    print('============')

    print(getattr(obj, 'z', 404))  # 可以传入一个default参数，如果属性不存在，就返回默认值：

    print('============')
    fn = getattr(obj, 'power')
    print(fn())
