#!/usr/bin/env python
# coding: utf-8

"""
Simple script to prompt each Ollama model on it's best use cases and training data
"Trick of the trade": Throws an error but continues execution if model in question isn't available locally ;)
Run "ollama pull <model>" to download it
Check the Model-Parameters-Size sheet in README on the corresponding memory footprint = All models would total to 412 GB
"""

import ollama

ollama_models = [
    "moondream",
    "gemma2:2b",
    "deepseek-r1:7b",
    "phi3",
    "codellama",
    "llama2-uncensored",
    "mistral",
    "neural-chat",
    "starling-lm",
    "llama3.1",
    "solar",
    "llama3.2-vision",
    "phi4",
    "gemma2:27b",
    "llama3.3",
    "llama3.2-vision:90b",
    "llama3.1:405b"
]

# Helper funtion checks Ollama is up and running
def check_ollama_service():
    try:
        # Check if Ollama is running
        ollama.list()
        return True
    except Exception as e:
        print(f"Error: Ollama service is not accessible: {e}")
        return False

# Helper funtion queries model with prompt
def query_model(model_name, prompt):
    try:        
        response = ollama.generate(
            model=model_name, 
            prompt=prompt
        )
        return response.response
    except Exception as e:
        return f"Error querying model {model_name}: {e}"

# Pre-liminary service check
if not check_ollama_service():
    sys.exit(1)

# Iterative over model list
for model_name in ollama_models:
    prompt = (
        f"Question 1: For which use cases is AI model {model_name} best prone to be used for? "
        f"Question 2: On which types of domain-specific data has AI model {model_name} been trained on?"
    )

    print(f"Model: {model_name}")
    try:
        response = query_model(model_name, prompt)
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"Failed to query {model}: {e}\n")
    print("=" * 50)
