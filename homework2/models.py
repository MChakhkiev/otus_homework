from random import randint, choice


class Desk:

    def __init__(self):
        self.rows = [['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-', '-']]
        numbers = [i for i in range(1, 90)]
        for row in self.rows:
            index = -1
            numbers_ind = 0
            for i in range(5):
                index = randint(index+1, 4 + i)
                numbers_ind = randint(numbers_ind, len(numbers)-5+i)
                row[index] = numbers.pop(numbers_ind)
        self.numbers = 15

    def cross_out(self, num):
        for i, row in enumerate(self.rows):
            try:
                row[row.index(num)] = '-'
                self.numbers -= 1
                return True
            except ValueError:
                if i == 2:
                    return False
                pass


class Member:

    def __init__(self, name):
        self.name = name
        self.desk = Desk()

    def __str__(self):
        return self.name


class Bot(Member):

    def __init__(self):
        name_list = open('botnames.txt', 'r').read().split('\n')
        name = choice(name_list)
        super().__init__(name)


class User(Member):

    def __init__(self, name):
        super().__init__(name)


class Bag:

    def __init__(self):
        self.numbers = [i for i in range(1, 91)]

    def get_num(self):
        num = choice(self.numbers)
        self.numbers.remove(num)
        return num
#
#
# class Game:
#
#     def __init__(self, m: list):
#         self.members = []
#         for member in m:
#             self.members.append(Bot() if member == 'bot' else User(member))
#         self.bag = Bag()
#
#     def round_start(self):
#         self.bag.get_num()


if __name__ == '__main__':
    desk1 = Desk()
    print(desk1.cross_out(85))
    b = Bot()
