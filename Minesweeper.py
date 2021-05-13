# Minesweeper, Minefinder or Minefield 1.0
# Written by Brendan Silva - February 2015

# This  program is free software: you can redistribute it and/or modify it under
# the  terms of the GNU General Public License as published by the Free Software
# Foundation,  either  version  3 of the License. This program is distributed in
# the  hope  that  it will be useful, but without any warranty; without even the
# implied  warranty  of merchantability or fitness for a particular purpose. See
# the GNU General Public License for more details. 

from random import randrange
from os import system
from os import devnull
if devnull == 'nul': runon = 1 # prompt
else: runon = 0 # shell

print
print ('--- Minesweeper ---')
print ('Programmed by Brendan Silva')
print
print ('How to play:')
print ('Choose a tile by entering the horizontal X and vertical Y')
print ('coordinates. E.g.: type "ab" to open the column tile B in.')
print ('line A. Type "q" to exit or return to the console...')
print

level = 0
while (level < 6) | (level > 26):
    n = raw_input('Set the difficulty level between 6 and 26.:')
    try: 
        level = int(n)
    except:
        if n.upper() == 'Q': quit()
        else: print('Incorrect entry!')

show = 0
tab = level * level
bomb = tab/10
findcount = tab - bomb
plays = 0
cols = []
for c in range(level): cols += chr(65 + c)
bombp = [range(bomb),range(bomb)]
field = []
for y in range(level):
    field += [[]]
    for x in range(level + 1):
        field[y] += [0]

c = 0
while c < bomb:
    p  = randrange(tab)
    py = p / level
    px = (p + 1) % level
    if  field[py][px] == 0:
        field[py][px] = -1
        bombp[0][c] = py
        bombp[1][c] = px
        c += 1

for c in range(bomb):
    y = bombp[0][c]
    x = bombp[1][c]
    for px in range(max(0, x - 1), min(level, x + 2)):
        for py in range(max(0, y - 1), min(level, y + 2)):
            if field[py][px] >= 0:
                field[py][px] += 1

def outcon():
    if runon: system('cls')
    else:
        system('reset') # xterm
        system('clear')
    l = ' ' * 3
    for c in cols: l += c + ' '
    l_ = l
    print l
    for y in range(level):
        l = cols[y] + ' |'
        for x in range(level):
            c = field[y][x]
            if ((field[y][level] >> x) & 1) | ((c < 0) * show):
                if c == 0: l += ' |'
                elif c < 0: l += '#|'
                else: l += str(c) + '|'
            else: l += '_|'
        print l + ' ' + cols[y]
    print l_
    
def find(y, x):
    global plays
    if not ((field[y][level] >> x) & 1):
        if field[y][x] >= 0:
            plays += 1
            field[y][level] |= (1 << x)
        if field[y][x] == 0:
            for fx in range(max(0, x - 1), min(level, x + 2)):
                for fy in range(max(0, y - 1), min(level, y + 2)):
                    if ((fy == y) & (fx == x)): continue
                    else:
                        find(fy, fx)

while (1):
    outcon()
    if plays == findcount:
        print chr(10) + '***** Success! *****'
        break
    print
    at = raw_input('Open: [' + str(plays) + '] out of ['+ str(findcount) + ']' + chr(10) + 'XY: -> ').upper()
    if at == 'Q':
        break
    elif len(at) == 2:
        if (at[0] in cols) & (at[1] in cols):
            x = ord(at[1]) - 65
            y = ord(at[0]) - 65
            if field[y][x] == -1:
                show = 1
                outcon()
                print chr(10) + 'Exploded! ---> ' + at[0] + ',' + at[1]
                break
            else:
                find(y, x)

raw_input ('Press RETURN to exit...')