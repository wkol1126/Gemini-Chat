import pathlib
import textwrap
import google.generativeai as genai
import gradio as gr
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

api_key='AIzaSyC0Opxr3qsL0GOZ58sEHukrtQ9hagdCDiM'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def greet(contents):
  for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
      print(m.name)

 # response = model.generate_content(contents)
  response = chat.send_message(contents)
  return response.text


app = gr.Interface(fn=greet, inputs="text", outputs="text")
app.launch()