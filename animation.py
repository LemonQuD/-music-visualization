import colorama
colorama.init()

from sty import fg, Style, RgbFg


qui = fg(255, 10, 10) + 'This is red text using 24bit colors.'

fg = Style(RgbFg(255, 150, 50))

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(qui, buf, sep='\n')