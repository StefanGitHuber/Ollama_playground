# Ollama_playground
Simplest Python scripts running Ollama locally to play with small-sized AI models.

## Install possibly missing python packages
pip install -r requirements.txt

## Ollama_OpenAI_Chatbot.py
Super simple chatbot interface:
- Ollama wrapper on OpenAI chat completion API
- Ollama Client hosts local server
- Gradio offers GUI on local endpoint http://localhost:11434 and public interface at https://<whatever>.gradio.live/

## Ollama_DeepSeek.py 
- requires a model (download chosen DeepSeek via pull request)
ollama pull deepseek-r1:7b

- Ollama Client hosts local server at http://localhost:11434
- Prompts "deepseek-r1:7b"
- Optional: Run GUI using Gradio

## Ollama_model_data.py
- Prompt list of small Ollama models on it's best use cases and training data

## Ollama_model_params.sh
- Simple bash script runs over a selected list of small Ollama models.
- Uses Ollama REPL command "/show info" to reveals model infos like architecture, num of params, context + embedding length, quantization method etc

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

250209: Been dealing lately with the question "which model most efficient+performant for which task" to establish a model portfolio. To avoid "using a sledgehammer to crack a nut" in order to save clients money lowering computational efforts + (GPU) server costs. **Fit small models to easy tasks => leverage big models on complex tasks.**

| Model              | Parameters | Size   |
|--------------------|------------|--------|
| Moondream 2        | 1.4B       | 829 MB |
| Gemma 2            | 2B         | 1.6 GB |
| Llama 3.2          | 1B         | 1.3 GB |
| Llama 3.2          | 3B         | 2.0 GB |
| Phi 3 Mini         | 3.8B       | 2.3 GB |
| Code Llama         | 7B         | 3.8 GB |
| Llama 2 Uncensored | 7B         | 3.8 GB |
| Mistral            | 7B         | 4.1 GB |
| Neural Chat        | 7B         | 4.1 GB |
| Starling           | 7B         | 4.1 GB |
| LLaVA              | 7B         | 4.5 GB |
| Llama 3.1          | 8B         | 4.7 GB |
| Gemma 2            | 9B         | 5.5 GB |
| Solar              | 10.7B      | 6.1 GB |
| Llama 3.2 Vision   | 11B        | 7.9 GB |
| Phi 4              | 14B        | 9.1 GB |
| Gemma 2            | 27B        | 16 GB  |
| Llama 3.3          | 70B        | 43 GB  |
| Llama 3.2 Vision   | 90B        | 55 GB  |
| Llama 3.1          | 405B       | 231 GB |

