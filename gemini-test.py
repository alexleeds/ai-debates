import pathlib
import textwrap

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-pro')

# %%time
response = model.generate_content("Hello, Gemini, are you there?")

print(response.text)
# to_markdown(response.text)