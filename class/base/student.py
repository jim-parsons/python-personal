class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("wrong score...")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


if __name__ == '__main__':
    s1 = Student('jack', 60)
    print(s1.get_name())
    # s1.__name = 'new'
    # print(s1.__name)
    # print(s1.get_name())
    