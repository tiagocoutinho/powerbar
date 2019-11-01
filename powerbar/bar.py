# -*- coding: utf-8 -*-

import wcwidth

STYLES = {
    'vbar': '▁▂▃▄▅▆▇█',
    'hbar': '░▒▓█',
    'circle': '◔◑◕●',
    '1dot': '⡀⡄⡆⡇',
    '2dot': '⣀⣤⣶⣿',
    '2dota': '⣀⣄⣤⣦⣶⣷⣿',
    '2dotb': '⣀⣄⣆⣇⣧⣷⣿',
    'squares': '□◱◧▣■',
    'block2': '⬜⬛',
    'blocka': '⬜',
    'blockb': '⬛',
}

DEFAULT_STYLE = 'vbar'
DEFAULT_HEIGHT = 5
DEFAULT_BG = ' '

def spark_indexes(data, style_size, minimum=None, maximum=None):
    minimum = min(data) if minimum is None else minimum
    maximum = max(data) if maximum is None else maximum
    interval = abs(maximum - minimum)
    C = (style_size - 1) / interval
    return (int((v - minimum) * C) for v in data)


def spark_iter(seq, width=1, style=DEFAULT_STYLE, **opts):
    ticks = STYLES[style]
    style_size = len(ticks)
    assert style_size > 1
    return (ticks[idx]*width for idx in spark_indexes(seq, style_size, **opts))


def spark(data, sep='', **opts):
    return sep.join(spark_iter(data, **opts))


def vbar_indexes(data, height, style_size, minimum=None, maximum=None):
    minimum = min(data) if minimum is None else minimum
    maximum = max(data) if maximum is None else maximum
    interval = abs(maximum - minimum)
    C = (style_size*height-1) / interval
    abs_indexes = (int((v-minimum)*C) for v in data)
    return ((i // style_size, i % style_size) for i in abs_indexes)


def vbar_iter(data, width=1, height=DEFAULT_HEIGHT, style=DEFAULT_STYLE,
              bg=DEFAULT_BG, **opts):
    ticks = STYLES[style]
    bar_width = wcwidth.wcwidth(ticks[0])
    bg *= bar_width
    indexes = tuple(vbar_indexes(data, height, len(ticks), **opts))
    for row in range(height-1, -1, -1):
        for n, i in indexes:
            c = bg if row > n else (ticks[i] if row == n else ticks[-1])
            yield c*width
        yield '\n'


def vbar_line_iter(data, **opts):
    sep = opts.pop('sep', '')
    left = opts.pop('left', '')
    right = opts.pop('right', '')
    line = [left]
    for item in vbar_iter(data, **opts):
        if item == '\n':
            line.append(right)
            yield sep.join(line)
            line = [left]
        else:
            line.append(item)


def vbar(data, **opts):
    return '\n'.join(vbar_line_iter(data, **opts))
