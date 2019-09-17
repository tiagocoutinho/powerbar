import emoji
import pytest
import wcwidth
import colorful

Rocket = emoji.EMOJI_UNICODE[':rocket:']

from progbar import Bar


@pytest.mark.parametrize('text', [None, '', 'hello', 'go '+ Rocket],
                         ids=['t(<dft>)', 't()', 't(simple)', 't(emoji)'])
@pytest.mark.parametrize('width', [None, 21, 80],
                         ids=['w(<dft>)', 'w(21)', 'w(80)'])
@pytest.mark.parametrize('completed', [None, 0, 0.25, 0.77, 1.0],
                         ids=['pdefault', '0%', '25%', '77%', '100%'])
@pytest.mark.parametrize('formatter', [None, 'on_blue', 'red_on_blue'],
                         ids=['f(<dft>)', 'f(on_blue)', 'f(red_on_blue)'])
def test_formatter(width, text, completed, formatter):
    bar = Bar()
    if width is None:
        width = 10
    else:
        bar.width = width
    if text is None:
        text = ''
    else:
        bar.text = text
    if completed is None:
        completed = 0
    else:
        bar.completed = completed
    ltxt = wcwidth.wcswidth(text)
    spaces = width - ltxt
    txt = (spaces//2 * ' ') + text + (spaces//2 * ' ') + (spaces % 2 * ' ')

    if formatter is None:
        assert str(bar) == txt
    else:
        with colorful.with_8_ansi_colors() as cf:
            bar.formatter = getattr(cf, formatter)
            pos = int(width * completed)
            assert str(bar) == '{}{}'.format(bar.formatter(txt[:pos]), txt[pos:])
