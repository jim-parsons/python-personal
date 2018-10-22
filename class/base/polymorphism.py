class Animal(object):
    def run(self):
        print('animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running...')


class Cat(Animal):
    def run(self):
        print('cat is running')


class Bird(Animal):
    def run(self):
        print('bird is flying...')


class Timer(object):
    """
    这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
    """
    def run(self):
        print("Timer类没有继承Animal,但是有run()方法,即可使用run_twice()方法")


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()

    a = list()
    print(isinstance(a, list))
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))

    print('================')
    run_twice(dog)
    print('================')
    run_twice(Bird())
    print('================')
    run_twice(Timer())
    