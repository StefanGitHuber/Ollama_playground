### Ollama_playground
Simplest Python scripts running Ollama locally to play with small-sized AI models.

## Install possibly missing python packages
pip install -r requirements.txt

## Ollama_DeepSeek.py 
- requires a model (download chosen DeepSeek via pull request)
ollama pull deepseek-r1:7b

- Ollama Client hosts local server at http://localhost:11434
- Prompts "deepseek-r1:7b"
- Optional: Run GUI using Gradio
