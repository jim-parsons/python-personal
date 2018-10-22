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
    # s.score = 999
