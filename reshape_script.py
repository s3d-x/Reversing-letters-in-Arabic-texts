# reshape_script.py Discord: 4SAAD
import arabic_reshaper
from bidi.algorithm import get_display
import pyperclip
import sys


text = pyperclip.paste()


reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)


pyperclip.copy(bidi_text)
