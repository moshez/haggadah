from importlib import resources
import os

import reportlab

import haggadah

def install_font():
    data = resources.read_binary(haggadah, 'ShlomoSemiStam.ttf')
    location = os.path.dirname(os.path.dirname(reportlab.__file__))
    fonts = os.path.join(location, 'fonts')
    os.makedirs(fonts, exist_ok=True)
    with open(os.path.join(fonts, 'ShlomoSemiStam.ttf'), 'wb') as fpout:
        fpout.write(data)

install_font()
