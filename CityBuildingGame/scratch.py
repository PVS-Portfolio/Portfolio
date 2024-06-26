import matplotlib.pyplot as plt
import random
from numpy import exp

size = 100

def decide_tree(x, y, map):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if map[x+i][y+j] == 'f':
                num += 1
    r = random.random()
    if num >= 3:
        if r < .75:
            return True
    else:
        if r < .1:
            return True
    return False

def test():
    num_starts = 3
    tiles = []
    probs = []
    for i in range(size):
        row = ['.'] * size
        prob = [0. for j in range(size)]
        tiles.append(row)
        probs.append(prob)

    q = [.1 * i for i in range(1, 11)]

    for i in range(num_starts):
        startx, starty = random.randint(3, size - 3), random.randint(3, size - 3)
        probs[startx][starty] = 1.

        for qx in range(len(q)):
            for row in range(max(0, startx - qx), min(startx + qx, size - 1)):
                for col in range(max(0, starty - qx), min(starty + qx, size - 1)):
                    probs[row][col] = q[qx]
                    print(probs[row][col])

    for row in range(size):
        for col in range(size):
            r = random.random()
            if r < probs[row][col]:
                tiles[row][col] = 'f'

    # startx, starty = random.randint(3, size - 3), random.randint(3, size - 3)
    # tiles[startx][starty] = 'f'
    # for i in range(-1, 2):
    #     for j in range(-1, 2):
    #         if i == 0 and j == 0:
    #             continue
    #         tiles[startx + i][starty + j] = 'f'
    #
    # for x, y in [[startx-2, starty], [startx+2, starty],
    #              [startx, starty-2], [startx, starty+2]]:
    #     if decide_tree(x, y, tiles):
    #         tiles[x][y] = 'f'

    fig, ax = plt.subplots(1)
    x = []
    y = []
    c = []
    for i in range(size):
        for j in range(size):
            x.append(i)
            y.append(j)
            if tiles[i][j] == 'f':
                c.append('g')
            else:
                c.append('k')


    ax.scatter(x, y, c=c, s=4)
    plt.show()

def sigmoid(x, quantity_demanded, max_price, price_range):
    # return (1 / (1 + exp(-(x+30))))

    k = 4/quantity_demanded + .01
    return max_price - (1 / (1 + exp(-k * (x - quantity_demanded)))) * price_range

def get_price(item, in_stock, quantity_demanded, max_price, price_range, mode='buy'):
    if mode == 'buy':
        midpoint = quantity_demanded
        k = 4 / midpoint + .01
    elif mode == 'sell':
        midpoint = int(quantity_demanded * 1.5)
        k = 8 / midpoint + .01
        max_price = int(max_price * 1.5)
        price_range = int(price_range * 1.5)
    return max_price - (1 / (1 + exp(-k * (in_stock - midpoint)))) * price_range

# 25 -> .15
# 50 -> .075
# 100 -> .05
# 200 -> .04
# 400 -> .02

def demand():
    pass


plt.subplots(1)

for total in [100]:
    x = list(range(total))
    r = 50
    maxp = 60
    y1 = [get_price(None, i, 50/2, maxp, r) for i in x]
    y2 = [get_price(None, i, 50 / 2, maxp, r, mode='sell') for i in x]
    # x = [25, 50, 100, 200, 400]
    # y = [.15, .075, .05, .04, .02]
    plt.scatter(x, y1, c='b')
    plt.scatter(x, y2, c='r')

    # plt.plot(x, [4/i + .01 for i in x])
plt.show()