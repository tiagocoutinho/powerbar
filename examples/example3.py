import functools

import gevent
import colorful

from powerbar import ProgressBar, Terminal


term = Terminal()

pb1 = ProgressBar(terminal=term)
pb1.bar.style = colorful.italic_green_on_blue, colorful.italic_green
pb1.prefix = 'Preparing: |'

pb2 = ProgressBar(terminal=term)
pb2.bar.style = colorful.inversed
pb2.prefix = 'bla: |'

width = 45
pos = 0, term.width - width
pb3 = ProgressBar(terminal=term, width=width, position=pos)
pb3.bar.style = colorful.on_red
pb3.prefix = 'hi there: |'
pb3.text = '{b.value:3}/{b.total:3}'

def loop(bar, interval):
    for i in range(101):
        bar.value = i
        bar.draw()
        gevent.sleep(interval)

t1 = gevent.spawn(loop, pb1, 0.1)
t2 = gevent.spawn(loop, pb2, 0.15)
t3 = gevent.spawn(loop, pb3, 0.05)


with term.hidden_cursor():
    try:
        gevent.joinall([t1, t2, t3])
    except KeyboardInterrupt:
        print('Ctrl-C pressed. Bailing out')


