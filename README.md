# Ollama_playground
Simplest Python scripts running Ollama locally to play with small-sized AI models.

## Install possibly missing python packages
pip install -r requirements.txt

## Ollama_DeepSeek.py 
- requires a model (download chosen DeepSeek via pull request)
ollama pull deepseek-r1:7b

- Ollama Client hosts local server at http://localhost:11434
- Prompts "deepseek-r1:7b"
- Optional: Run GUI using Gradio

## Note:
I used to experient with AI models using Hugging Face (HF) python libraries, especially the efficient transformers lib.
It's a comprehensive + powerful toolkit working with LLMs.

But with the advent of smaller LMs, Ollama offers a specialized + streamlined experience:
- Specialized for inference, lower overhead
- Centralized Model Hub, Curated Selection of Open-Source Models
- runs + manages open-source models efficiently
- adds layer of abstraction on top of libraries like transformers
- more user-friendly + optimized environment for specific use cases
- serve LLMs locally through REST API
