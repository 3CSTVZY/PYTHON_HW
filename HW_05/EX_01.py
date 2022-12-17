# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint as ri

print('Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
      'Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять\n'
      'первому игроку, чтобы забрать все конфеты у своего конкурента?')
print()

count = 0
who = 0
player1 = False
player2 = False
bot = False
bot_add = 0
sweets = 150
grabsweets = 0
sp1 = 0
sp2 = 0
run = True

bot_add = int(input('Choose ypur opponent\n 1 -> Human  2 -> Bot: '))


who = (ri(1, 2))
if who == 1:
    player1 = True
    bot = False
    player2 = False
else:
    if bot_add == 2:
        bot = True
    else:
        player2 = True
        player1 = False


while run:
    run = False

    print(f'Now in basket are {sweets} sweets')
    print()

    if player1:
        runp1 = True
        while runp1:
            print(f'1st player turn\nIn player"s basket are {sp1} sweets')
            print()

            grabsweets = int(input('How many sweets do you wanna take?: '))
            if grabsweets <= 28 and grabsweets > 0 and sweets > 0 and grabsweets<=sweets:
                for i in range(grabsweets):
                    sweets -= 1

                for i in range(grabsweets):
                    sp1 += 1
                runp1 = False
            
            else:
                print('You took too many sweets, try again!')
                print(f'Now in basket are {sweets} sweets')
                print()
        player1 = False
        if bot_add == 2:
            bot = True
            player2 = False
        else:
            bot = False
            player2 = True
        print()

    elif player2:
        runp2 = True
        while runp2:
            print(f'2nd player turn\nIn player"s basket are {sp1} sweets')
            print()
            grabsweets = int(input('How many sweets do you wanna take?: '))
            if grabsweets <= 28 and grabsweets > 0 and sweets > 0 and grabsweets<=sweets:
                for i in range(grabsweets):
                    sweets -= 1
                    sp2 += 1
                runp2 = False
            
            else:
                print('You took too many sweets, try again!')
                print(f'Now in basket are {sweets} sweets')
                print()
        player2 = False
        if bot_add == 2:
            bot = True
            player1 = False
        else:
            bot = False
            player1 = True
        print()

    elif bot:
        print(f'Now is Bot turn\nIn player"s basket are {sp1} sweets')
        print()

        if sweets > 80 and sweets % 2 == 0:
            print('I"ll take 28 sweets')
            sweets -= 28
            player1 = True
            bot = False
        elif sweets > 56 and sweets % 2 != 0:
            print('I"ll take 21 sweets')
            sweets -= 21
            player1 = True
            bot = False
        elif sweets < 28:
            print(f'I"ll take {sweets} sweets')
            sweets -= sweets
            player1 = True
            bot = False
        elif sweets > 28 and sweets <= 56:
            grabsweets = 0
            for grabsweets in range(28):
                if sweets - grabsweets == 29:
                    print(f'I"ll take {grabsweets} swwets')
                    sweets -= grabsweets
            player1 = True
            bot = False    
        print()

    if sweets > 0:
        run = True
    else:
        if player1 and bot_add == 2:
            print('Bot wins')
            break
        elif player1 and bot_add == 1:
            print('2nd player wins')
            break
        else:
            print('1st player wins')
            break