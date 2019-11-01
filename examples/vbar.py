import random
from powerbar import vbar

N = 40

data = [random.randrange(-100, 100) for _ in range(N)]

print(vbar(data))
print(N*'-')
print(vbar(data, style='1dot'))
print(N*'-')
print(vbar(data, width=2, sep=' ', style='2dota'))
print(N*'-')
print(vbar(data, width=2, sep='|', bg='.'))


