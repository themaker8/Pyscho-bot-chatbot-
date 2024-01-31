import openai
import gradio as gr
from gradio.themes.base import Base
#from . import web

openai.api_key = ""

messages = [{
    "role":
    "system",
    "content":
    "You are a student pyschologist and your work is to solve mental issues.Donot give answer which is not related to your work.",
}]


def Chat(user_input):
  messages.append({"role": "user", "content": user_input})
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=messages,
                                          temperature=0.3)
  output = response["choices"][0]["message"]["content"]
  return output


class Seafoam(Base):
  pass


seafoam = Seafoam()

with gr.Blocks(theme=seafoam) as demo:
  gr.Markdown("#Student Psycho Bot")
  inp = gr.Textbox(placeholder="USER:", label='user')
  out = gr.Textbox(placeholder="AI:")
  btn = gr.Button('Submit', variant='primary')
  cl_btn = gr.Button("Clear")
  btn.click(fn=Chat, inputs=inp, outputs=out)
  btn.click(lambda x: gr.update(value=""))

if __name__ == "__main__":
  demo.launch(share=True)
