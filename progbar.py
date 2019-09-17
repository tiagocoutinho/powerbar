import wcwidth

ulen = wcwidth.wcswidth


class Bar:
    text = ''
    formatter = None
    width = 10

    # [0.0, 1.0]
    completed = 0

    def __str__(self):
        formatter = self.formatter or (lambda x:x)
        width = self.width
        text_width = ulen(self.text)
        content_empty_width = width - text_width
        content_empty = content_empty_width // 2 * ' '
        content_extra = content_empty_width % 2 * ' '
        step = int(self.completed * width)
        content = f'{content_empty}{self.text}{content_empty}{content_extra}'
        return '{}{}'.format(formatter(content[:step]), content[step:])


class ProgressBar:

    def __init__(self, prefix='|', suffix='|', bar_text='{b.percentage:3}%', total=100, width=40):
        self.prefix = prefix
        self.suffix = suffix
        self.bar_text = bar_text
        self.value = 0
        self.total = total
        self.width = width
        self.bar = Bar()

    @property
    def completed(self):
        return self.value / self.total

    @property
    def percentage(self):
        return self.completed * 100

    def render(self):
        bar = self.bar
        prefix = self.prefix.format(b=self)
        suffix = self.suffix.format(b=self)
        prefix_width = ulen(prefix)
        suffix_width = ulen(suffix)
        bar.width = self.width - prefix_width - suffix_width
        bar.text = self.bar_text.format(b=self)
        bar.completed = self.completed
        return f'{prefix}{bar}{suffix}'
