import random

from scipy import rand

print(random.random())
print(random.randint(1,50))
print(random.choice([30, 40, 50, 60, 70]))

# for 4 random items
print(random.sample([30, 40, 50, 60, 70],4))