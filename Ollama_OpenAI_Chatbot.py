#!/usr/bin/env python
# coding: utf-8

"""
Super simple chatbot interface:
- Ollama wrapper on OpenAI chat completion API
- Ollama Client hosts local server
- Gradio offers GUI on local endpoint http://localhost:11434 and public interface at https://<whatever>.gradio.live/
- Chatbot/QnA offers LLMs "neural-chat", "gemma2:2b", "mistral", "deepseek-r1:7b" to interact with

OpenAI chat completion API offers 3 distinct roles:
"user": End user interacts with model via messages (prompts or questions)
"assistant": AI model acts as an assistant responding to user messages
"system": Provide instructions and/or context to set behaviour of AI assistant
"""

import json
import openai
import gradio as gr
from typing import List, Tuple
from check_models import check_install_models

# Default prompt and model list
prompt = "What's the difference between the roles user, assistant and system, please?"
# model_list = ["neural-chat", "gemma2:2b", "mistral", "deepseek-r1:7b"]
model_list = ["gemma2:2b"]
check_install_models(model_list) # Helper function downloads missing models

### Local Chatbot Deployment

# Use OpenAI Client endpoint, connected to local Ollama instance
client = openai.Client(
   base_url="http://localhost:11434/v1",
   api_key="ollama"  # Authentication-free private access
)

# Prompt model via OpenAI client wrapper on Ollama server
def query_model(prompt: str,
                            role: str,
                            model_name: str) -> str:
   if not prompt.strip():
      return "Error: Empty prompt"
   try:
      response = client.chat.completions.create(
         model=model_name,
         messages=[{"role": role, "content": prompt}],
         temperature=0.7  # Controls creativity vs precision
      )
      return response.choices[0].message.content
   except Exception as e:
      return f"Error while querying {model_name}: {str(e)}"

# Wrapper over iterative QnAs
def chatbot_interface(input_text: str,
                                    role: str,
                                    model_name: str,
                                    chat_history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
   response_text = query_model(input_text, role, model_name)
   chat_history.append((f"{role}: {input_text}", f"assistant: {response_text}"))
   return "", chat_history

### Gradio interface on local server + public website
with gr.Blocks() as iface:
   gr.Markdown(f"## Chatbot Interface")
   with gr.Row():
        with gr.Column():
            chatbot = gr.Chatbot(type="messages")
            message = gr.Textbox(value=prompt, placeholder="Enter message here...", label="Message")
            role_dropdown = gr.Dropdown(choices=["user", "assistant", "system"], value="user", label="Select Role")
            model_dropdown = gr.Dropdown(choices=model_list, value="neural-chat", label="Select Model")
            chat_state = gr.State([])
            send_button = gr.Button("Send")
   send_button.click(fn=chatbot_interface, inputs=[message, role_dropdown, model_dropdown, chat_state], outputs=[message, chatbot])
iface.launch(share=True)
