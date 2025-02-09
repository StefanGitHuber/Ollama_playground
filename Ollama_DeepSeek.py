#!/usr/bin/env python
# coding: utf-8

"""
Super simple script to test DeepSeek locally:
- Ollama Client hosts local server at http://localhost:11434
- Ollama API call generate queries "deepseek-r1:7b" on a prompt
- Retrieve + parse JSON response from DeepSeek

Optionally: Run GUI using Gradio
- local interface at http://127.0.0.1:7860/
- public interface at https://<whatever>.gradio.live/
"""

import gradio as gr
import json
import os
from ollama import Client

bshow_gui = True
model_name = "deepseek-r1:7b"
prompt = "Explain 1. on which data patterns you have been trained on,\n and 2. for which industrial uses cases"
print(f"Prompt to {model_name}:\n{prompt}\n")

# Instantiate Ollama client on local endpoint
client = Client(host='http://localhost:11434')  

# Query DeepSeek and parse response
def query_model(prompt):
   try:
      response = client.generate(model=model_name, prompt=prompt)
      return response['response']
   except Exception as e:
      return f"An error occurred: {e}"

if bshow_gui:
   # Gradio GUI interface
   iface = gr.Interface(fn=query_model, inputs="text", outputs="text", title=f"Prompt {model_name}", examples=[[prompt]])
   iface.launch(share=True)
else:
   # Print to std out
   response = query_model(prompt)
   print(f"Response: \n{response}")
