import time

import powerbar
import colorful

print('starting app...')
pb1 = powerbar.ProgressBar()
pb1.bar.style = colorful.italic_green_on_blue, colorful.italic_green
pb1.prefix = 'Preparing: |'

for i in range(101):
    pb1.value = i
    pb1.draw()
    time.sleep(.1)


