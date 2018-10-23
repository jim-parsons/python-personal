class Student(object):

    # 使用装饰器的时候，需要注意：
    # 1. 装饰器名，函数名需要一直
    # 2. property需要先声明，再写setter，顺序不能倒过来
    @property  # getter方法
    def score(self):
        """
        用@property会把成员函数x转换为getter,修饰后相当于
        score = property()
        score = score.getter()
        :return:
        """
        print('@property...')
        return self._score

    @score.setter  # setter方法
    def score(self, value):
        print('set ...')
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Person(object):
    def __init__(self):
        self.__name = 'SDAF'

    def __getattr__(self, item):
        # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
        # 只有在没有找到的情况下才会调用__getattr
        if item == 'score':
            return 90
        if item == 'age':
            return lambda: 25

    def __call__(self, *args, **kwargs):
        #  需要定义一个__call__()方法，就可以直接对实例进行调用
        print('my name is %s' % self.__name)


if __name__ == '__main__':
    """
    @property装饰器会把成员函数x转换为getter，相当于做了x = property(); x = x.getter(x_get) 
    @x.setter装饰器会把成员函数x转换为setter，相当于做了x = x.seter(x_set).
    """
    s = Student()
    print(hasattr(s, 'score'))
    print('========')
    s.score = 60  # 相等于调用了setter()
    print(s.score)  # 相等于调用了getter()
    print("========")
    print(s.score)

    print("========")
    p = Person()
    print(p.score)
    print(p.age())
    p()
    #  通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
    print(callable(Person()))
    print(callable(p))
