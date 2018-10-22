#  正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass


def test01():
    s = Student()
    Student.ag = '123'  # 动态给类绑定一个属性
    print(Student.ag)
    s.name = 'Misadf'  # 动态给实例绑定一个属性
    print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


def set_score(self, score):
    self.score = score


def test02():
    from types import MethodType
    s = Student()
    s.set_age = MethodType(set_age, s)  # 对另一个实例是不起作用的
    s.set_age(22)
    print(s.age)


def test03():
    # 给class绑定方法后，所有实例均可调用
    Student.set_score = set_score
    s1 = Student()
    s2 = Student()
    s1.set_score(100)
    s2.set_score(10)
    print(s1.score)
    print(s2.score)


class Person(object):
    """
    只允许对Person实例添加name和age属性
    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    """
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    p = Person()
    p.name = 'person'
    p.age = 12
    print('%s: %s' % (p.name, p.age))
