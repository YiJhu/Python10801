'''
B10802014 猜數字遊戲
Guess the number game
'''
import random

def game():
    count = 0
    x = random.randint(1, 20)
    #print('答案是: %s'%(x)) 
    for count in range(5):
        number = int(input('請輸入你的數字:'))
        if number < x:
            print('\n太小了\n')
            count += 1
        if number > x:
            print('\n太大了\n')
            count += 1
        if number == x:
            print('\n恭喜你猜對了，答案是: %s\n進行下一輪遊戲\n'%(x))
            break
    else:
        print('\n以經連續猜錯5次，答案是: %s\n進行下一輪遊戲\n'%(x))

while True:
    game()
