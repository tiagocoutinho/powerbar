# -*- coding: utf-8 -*-

from .tools import ulen, Terminal


class Bar:

    text = ''
    style = None
    width = 10

    # [0.0, 1.0]
    completed = 0

    def __str__(self):
        text, style, width = self.text, self.style, self.width
        if style is None:
            style = 2*(lambda x:x,)
        elif not isinstance(style, (tuple, list)):
            style = style, lambda x:x
        f1, f2 = style
        text_width = ulen(text)
        content_empty_width = width - text_width
        content_empty = content_empty_width // 2 * ' '
        content_extra = content_empty_width % 2 * ' '
        step = int(self.completed * width)
        content = f'{content_empty}{text}{content_empty}{content_extra}'
        return '{}{}'.format(f1(content[:step]), f2(content[step:]))


class CharBar:

    ASCII = " 123456789#"
    UTF = " " + ''.join(map(chr, range(0x258F, 0x2587, -1)))
    BLANK = "  "

    text = ''
    style = None
    width = 10

    # [0.0, 1.0]
    completed = 0
    charset = UTF

    def __str__(self):
        text, width = self.text, self.width
        text_width = ulen(text)
        bar_width = width - text_width
        nb_syms = len(self.charset) - 1
        bar_length, frac_bar_length = divmod(
            int(self.completed * bar_width * nb_syms), nb_syms)

        bar = self.charset[-1] * bar_length
        frac_bar = self.charset[frac_bar_length]

        # whitespace padding
        if bar_length < bar_width:
            return bar + frac_bar + \
                self.charset[0] * (bar_width - bar_length - 1) + text
        return bar + self.charset[0] * (bar_width - bar_length) + text


class PBar:

    def __init__(self, prefix='|', suffix='|', text='{b.percentage:4.1f}%',
                 total=100, width=40):
        self.prefix = prefix
        self.suffix = suffix
        self.text = text
        self.value = 0
        self.total = total
        self.width = width
        self.bar = Bar()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def completed(self):
        return self._value / self.total

    @property
    def percentage(self):
        return self.completed * 100

    def __str__(self):
        bar = self.bar
        prefix = self.prefix.format(b=self)
        suffix = self.suffix.format(b=self)
        prefix_width = ulen(prefix)
        suffix_width = ulen(suffix)
        bar.width = self.width - prefix_width - suffix_width
        bar.text = self.text.format(b=self)
        bar.completed = self.completed
        return f'{prefix}{bar}{suffix}'


class ProgressBar(PBar):

    def __init__(self, **kwargs):
        self.terminal = kwargs.pop('terminal', None) or Terminal()
        self.position = kwargs.pop('position', None)
        if self.position is None:
            self.position = self.terminal.get_position()
#            self.terminal.stream.write('\n')
        super().__init__(**kwargs)

    def draw(self):
        y, x = self.position
        self.terminal.write_at(str(self), x, y)
