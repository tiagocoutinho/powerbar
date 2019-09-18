import sys
import tty
import shutil
import termios
import collections

import wcwidth
import blessings


class TermState:

    def __init__(self, fd=None):
        if fd is None:
            fd = sys.stdin.fileno()
        self.fd = fd

    def __enter__(self):
        self.settings = termios.tcgetattr(self.fd)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        termios.tcsetattr(self.fd, termios.TCSANOW, self.settings)


def get_cursor_position(reader=None, writer=None):
    """Return current cursor position (0, 0) - (t.height-1, t.width-1)"""
    if reader is None:
        reader = sys.stdin
    if writer is None:
        writer = sys.stdout
    rfd = reader.fileno()
    with TermState(rfd) as ts:
        settings = ts.settings[:]
        settings[3] &= ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(rfd, termios.TCSANOW, settings)
        writer.write('\x1b[6n')
        writer.flush()
        buff = sys.stdin.read(6)[2:] # discard '\x1b[
        while True:
            if buff[-1] == 'R':
                break
            buff += reader.read(1)
        y, x = buff[:-1].split(';')
        return int(y) - 1, int(x) - 1


ulen = wcwidth.wcswidth


class Terminal(blessings.Terminal):

    def get_position(self):
        return get_cursor_position(None, self.stream)

    def write_at(self, text, x=None, y=None):
        if x is None and y is None:
            self.stream.write(text)
            return
        ipos = self.get_position()
        if y is None:
            y = ipos[0]
        if x is None:
            x = ipos[1]
        self.stream.write('{}{}{}'.format(self.move(y,x), text, self.move(*ipos)))
        self.stream.flush()
