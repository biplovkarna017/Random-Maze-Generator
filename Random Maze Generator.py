
import random
import matplotlib.pyplot as plt


def generate_maze():
    MAX = 14

    list1 = [(0, -1), (0, 0)]
    dead = []
    for i in range(-8, 9):
        dead.append((i, -1))
    for i in range(-1, 15):
        dead.append((8, i))
        dead.append((-8, i))

    # y = 0
    proceed = True
    while list1[-1][-1] != MAX:
        pres = list1[-1]
        prev = list1[-2]
        x = pres[0]
        y = pres[-1]
        diffx = x - prev[0]
        diffy = y - prev[-1]
        combined = list1+dead
        # UP
        if diffx == 0 and diffy > 0 and all(element in combined for element in [(x+1, y), (x-1, y), (x, y+1)]):
            proceed = False
        # DOWN
        elif diffx == 0 and diffy < 0 and all(element in combined for element in [(x+1, y), (x-1, y), (x, y-1)]):
            proceed = False
        # RIGHT
        elif diffy == 0 and diffx > 0 and all(element in combined for element in [(x, y+1), (x, y-1), (x+1, y)]):
            proceed = False
        # LEFT
        elif diffy == 0 and diffx < 0 and all(element in combined for element in [(x, y+1), (x, y-1), (x-1, y)]):
            proceed = False
        if not proceed:
            dead.append(list1.pop())

        if proceed:
            num1 = random.randint(1, 3)
            if diffx == 0:
                if num1 == 2 and x != -7:
                    x -= 1
                elif num1 == 3 and x != 7:
                    x += 1
                elif num1 == 1:
                    if diffy > 0:
                        y += 1
                    elif diffy < 0 and y != 0:
                        y -= 1
            elif diffy == 0:
                if num1 == 1:
                    y += 1
                elif num1 == 2 and y != 0:
                    y -= 1
                elif num1 == 3:
                    if diffx > 0 and x != 7:
                        x += 1
                    elif diffx < 0 and x != -7:
                        x -= 1
            if (x, y) not in combined:
                list1.append((x, y))
        proceed = True
    return list1


list1 = []
while len(list1) < 100:
    list1 = generate_maze()
px, py = zip(*list1[1:])
plt.plot(px, py, 'o-')
plt.grid()
plt.xticks(range(-7, 8), labels=[])
plt.yticks(range(0, 15), labels=[])


plt.show()
