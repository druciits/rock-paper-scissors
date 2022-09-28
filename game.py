import random
x = ['rock', 'paper', 'scissors']
p1s = []
p2s = []

while(True):
    print('ROCK, PAPER, SCISSORS')
    print("Let's begin!")

    p1 = input('Enter your choice or type exit:')
    p2 = random.choice(x)

    if p1 == 'exit':
        break

    p1s.append(p1)
    p2s.append(p2)

    print(f'You:{p1}   vs.   Computer:{p2}')

    if p1 == p2:
        print('Draw!')
    elif p1 == 'rock' and p2 == 'paper':
        print('Computer Wins!')
    elif p1 == 'paper' and p2 == 'scissors':
        print('Computer Wins!')
    elif p1 == 'scissors' and p2 == 'rock':
        print('Computer Wins!')
    else:
        print('You Win!')                                                                                                                                                                


print(f'You have played {len(p1s)} times')
print(p1s)
print(p2s)
