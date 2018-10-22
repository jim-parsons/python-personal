class Student(object):
    def __init__(self, name):
        self.__name = name


#  由于Python是动态语言，根据类创建的实例可以任意绑定属性。


class Student1(object):
    name = 'Student'


if __name__ == '__main__':
    s = Student('Jack')
    s.score = 90
    print(s)

    s = Student1()
    print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
    print(Student1.name)  # 打印类的name属性
    print('===========')
    s.name = 'Mos'
    print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    print(Student1.name)  # 但是类属性并未消失，用Student.name仍然可以访问
    print('===========')
    del s.name  # 如果删除实例的name属性
    print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
