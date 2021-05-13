# Tower of Hanoi 1.0 
# Written by Brendan Silva - February 2014

# This  program is free software: you can redistribute it and/or modify it under
# the  terms of the GNU General Public License as published by the Free Software
# Foundation,  either  version  3 of the License. This program is distributed in
# the  hope  that  it will be useful, but without any warranty; without even the
# implied  warranty  of merchantability or fitness for a particular purpose. See
# the GNU General Public License for more details. 

from os import system
from os import devnull
if devnull == 'nul': runon = 1 # prompt
else: runon = 0 # shell

print
print ('--- Tower of Hanoi ---')
print ('Programmed by Brendan Silva')
print
print ('How to play:')
print ('Enter the letters of the source column and the destination column.')
print ('E.g.: type "as" to move from column "A" to column "S".')
print ('Type "q" to exit or return to the console...')
print

level = 0
dist = 10
plays = 0

while (level < 3) | (level > 9):
    n = raw_input('Set the difficulty level between 3 and 9:')
    try: 
        level = int(n)
    except:
        if n.upper() == 'Q': quit()
        else: print('Incorrect entry!')

tower = {}
tower['A'] = range(1, level + 1)
for x in 'SD': tower[x] = map(int, list('0' * level))

def outcon():
    view = chr(10)
    empty = ' ' * level
    jump = ' ' * dist
    for x in 'ASD': view += empty + x + empty + jump
    view += chr(10) + '-' * (6 * level + dist * 2 + 3) + chr(10)
    col = (empty + ':' + empty + jump) * 3 + chr(10)
    view += col
    for x in range(0, level):
        for y in 'ASD':
            s = tower[y][x]
            if s: view += ' ' * (level - s) + '-' * s + str(s) + '-' * s + ' ' * (level - s)
            else: view += empty + ':' + empty
            view += jump
        view += chr(10)
        view += col
    if runon: system('cls')
    else:
        system('reset') # xterm
        system('clear')
    print (view)


while (1):
    outcon()

    if (tower['S'] == range(1, level + 1)) or (tower['D'] == range(1, level + 1)):
        print ('Success!')
        total = pow(2, level) - 1
        print ('Movements: %s (necessary = %s)' % (plays, total))
        break

    move = raw_input('[%s] Move a disc: ' % plays)
    if move.upper() == 'Q': break

    fromto = 0
    if len(move) == 2:
        move = move.upper()
        if not (move[0] == move[1]):
            fromto = 1
            for x in move:
                if not x in tower.keys():
                    fromto = 0

    if fromto: 
        pop = -1
        for x in range(0, level):
            if tower[move[0]][x]:
                pop = x
                break

        for x in range(level, 0, -1):
            if not tower[move[1]][x - 1]:
                push = x - 1
                break

        if (pop >= 0):
            x = 0
            first = 0
            try: x = (tower[move[1]][push + 1] > tower[move[0]][pop])
            except: first = 1

            if first or x:
                plays += 1
                tower[move[1]][push] = tower[move[0]][pop]
                tower[move[0]][pop] = 0

raw_input ('Press RETURN to exit...')