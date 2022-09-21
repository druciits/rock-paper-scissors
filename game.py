p1 = input('Input Player1 turn:')
p2 = input('Input Player2 turn:')

if p1 == p2:
    print('Draw!')
elif p1 == 'rock' and p2 == 'paper':
    print('Player2 Wins!')
elif p1 == 'paper' and p2 == 'scissors':
    print('Player2 Wins!')
elif p1 == 'scissors' and p2 == 'rock':
    print('Player2 Wins!')
else:
    print('Player1 Wins!')
