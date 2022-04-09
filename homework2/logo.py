from models import *


if __name__ == '__main__':
    print('Добро пожаловать')
    members = []
    while True:
        command = input('Добавить игрока:\n1-бот\n2-игрок\n3-начать игру\n')
        if command == '1':
            newMember = Bot()
            members.append(newMember)
        if command == '2':
            name = input('Введите имя игрока:')
            newMember = User(name)
            members.append(newMember)
        if command == '3':
            if len(members) < 2:
                print('Необходимо как минимум два игрока')
            else:
                print('Начинаем игру')
                numbers = [i for i in range(1, 90)]
                done = False
                while True:
                    if done:
                        break
                    num = choice(numbers)
                    numbers.remove(num)
                    print(f'Вытащен номер - {num}')
                    for member in members:
                        print(member.name)
                        print('---------')
                        for row in member.desk.rows:
                            print(row)
                        print('---------')
                        if isinstance(member, Bot):
                            if member.desk.cross_out(num):
                                print(f'{member.name} стер номер!')
                            if member.desk.numbers == 0:
                                print(f"Бот {member.name} Победил!")
                                done = True
                                members.clear()
                        else:
                            command = input('Стереть номер? (y/любой другой инпут):')
                            if command == 'y':
                                if member.desk.cross_out(num):
                                    print(f'{member.name} стер номер!')
                                    if member.desk.numbers == 0:
                                        print(f"Игрок {member.name} Победил!")
                                        done = True
                                        members.clear()
                                else:
                                    print('Такого номера нет! Вы проиграли!')
                                    members.remove(member)
                                    if len(members) == 1:
                                        print(f'Остался единственный игрок {members[0].name}')
                                        done = True
                                        members.clear()
                            else:
                                if member.desk.cross_out(num):
                                    print('Вы пропустили свой номер, вы проиграли!')
                                    members.remove(member)
                                    if len(members) == 1:
                                        print(f'Остался единственный игрок {members[0].name}')
                                        done = True
                                        members.clear()




