from collections import Iterable
import inltk
from inltk.inltk import setup
setup('hi')

from inltk.inltk import tokenize

hindi_text = """प्राकृतिकभाषासीखनाबहुतदिलचस्पहै।"""

# tokenize(input text, language code)
tokens = tokenize(hindi_text, "hi")
print(tokens)
