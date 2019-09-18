import time

from powerbar import ProgressBar, Terminal
import colorful

term = Terminal()

pb1 = ProgressBar(terminal=term)
pb1.bar.style = colorful.italic_green_on_blue, colorful.italic_green
pb1.prefix = 'Preparing: |'

pb2 = ProgressBar(terminal=term)
pb2.bar.style = colorful.inversed
pb2.prefix = 'bla: |'

width = 25
pos = 0, term.width - width
pb3 = ProgressBar(terminal=term, width=width, position=pos)
pb3.bar.style = colorful.on_red
pb3.prefix = 'hi there: |'
pb3.text = '{b.value:3}/{b.total:3}'

for i in range(101):
    #pb2.prefix = f'm{i:03} |'
    pb1.draw()
    pb2.draw()
    pb3.draw()
    time.sleep(0.1)
    pb1.value = i
    pb2.value = i
    pb3.value = i

pb1.draw()
pb2.draw()
pb3.draw()


