# reshape_script.py
import arabic_reshaper
from bidi.algorithm import get_display
import pyperclip
import sys

# خذ النص من الحافظة (Clipboard)
text = pyperclip.paste()

# إعادة تشكيل الحروف
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

# وضع الناتج في الحافظة مرة ثانية
pyperclip.copy(bidi_text)
