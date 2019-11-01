import random
from powerbar import spark

N = 20

data = [random.randrange(-100, 100) for _ in range(N)]

print(spark(data))
print(N*'-')
print(spark(data, width=2, sep=' '))
print(N*'-')
print(spark(data, width=2, sep='|'))
print(N*'-')

import time

for _ in range(50):
    data = [random.randrange(-100, 100) for _ in range(N)]
    print(spark(data), end='\r', flush=True)
    time.sleep(0.1)
print()
