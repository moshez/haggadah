
from bidi import algorithm

def write(canvas, language, x, y, words):
    canvas.setFont(language, 14)
    canvas.drawString(x, y, algorithm.get_display(words))

def write_multi(canvas, language, x, y, lines):
    for idx, line in enumerate(lines):
        height = y - (idx * 14)
        write(canvas, language, x, height, line)

def write_lines(canvas, language, x, y, text):
    write_multi(canvas, language, x, y, text.splitlines())