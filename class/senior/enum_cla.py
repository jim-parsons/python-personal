from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


def test01():
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def test02():
    d1 = WeekDay.Mon
    d2 = WeekDay['Tue']
    print(d1)
    print(d1.value)
    print(WeekDay['Tue'])
    print(WeekDay['Tue'].value)
    print(d2 == WeekDay['Tue'])
    print(WeekDay(1))

    for name, member in WeekDay.__members__.items():
        print(name, '=>', member)


if __name__ == '__main__':
    # test01()
    test02()
