class Hello(object):
    def hello(self, name='world'):
        print('hello %s' % name)


"""
class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
"""

"""
定义类,然后创建示例
"""

"""
如果想创建类,则需要根据metaclass创建出类
"""


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


#  Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass


"""
__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。
"""

if __name__ == '__main__':
    h = Hello()
    h.hello()
    print(type(Hello))  # <class 'type'>
    print(type(h))  # <class '__main__.Hello'>
    print('===========')
    L = MyList()
    L.add(1)
    L.add(2)
    print(L)
