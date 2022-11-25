# Marlena Gryt
# Python 2022/2023
# Zd 7.6

import itertools
import random

iterA = itertools.cycle([0, 1]) 
iterB = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
iterC = itertools.cycle([num for num in range(1, 8)])

for _ in range(15):
    print("{}   {}   {}".format(next(iterA), next(iterB), next(iterC)))
