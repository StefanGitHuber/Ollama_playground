#!/bin/bash

# Simple bash script runs over a selected list of Ollama models to print models architecture, params etc.
# NOTE: Downloads each model, would in total be 412 GB. Please check the Model-Parameters-Size sheet
# Each call occupies GBs of disk space (running locally is the purpose of Ollama)
models=(
    "deepseek-r1:7b"
    "moondream"
    "gemma2:2b"
    "llama3.2:1b"
    "llama3.2"
    "phi3"
    "codellama"
    "llama2-uncensored"
    "mistral"
    "neural-chat"
    "starling-lm"
    "llava"
    "llama3.1"
    "gemma2"
    "solar"
    "llama3.2-vision"
    "phi4"
    "gemma2:27b"
    "llama3.3"
    "llama3.2-vision:90b"
    "llama3.1:405b"
)

### Ollama REPL command /show info reveals model info
for model in "${models[@]}"
do
    echo "Running model: $model"
    expect -c "spawn ollama run $model; send \"/show info\r\"; expect \"architecture\"; send \"/exit\r\"; interact" | awk '/architecture/,/quantization/'
    echo "====================================="
done

### Printed results
"""
Running model: deepseek-r1:7b
    architecture        qwen2     
    parameters          7.6B      
    context length      131072    
    embedding length    3584      
    quantization        Q4_K_M    
=====================================
Running model: moondream
    architecture        phi2    
    parameters          1.4B    
    context length      2048    
    embedding length    2048    
    quantization        Q4_0    
    architecture        clip       
    parameters          454.45M    
    embedding length    1152
=====================================
Running model: gemma2:2b
    architecture        gemma2    
    parameters          2.6B      
    context length      8192      
    embedding length    2304      
    quantization        Q4_0      
=====================================
Running model: llama3.2:1b
    architecture        llama     
    parameters          1.2B      
    context length      131072    
    embedding length    2048      
    quantization        Q8_0      
=====================================
Running model: llama3.2
    architecture        llama     
    parameters          3.2B      
    context length      131072    
    embedding length    3072      
    quantization        Q4_K_M    
=====================================
Running model: phi3
    architecture        phi3      
    parameters          3.8B      
    context length      131072    
    embedding length    3072      
    quantization        Q4_0      
=====================================
Running model: codellama
    architecture        llama    
    parameters          6.7B     
    context length      16384    
    embedding length    4096     
    quantization        Q4_0     
=====================================
Running model: llama2-uncensored
    architecture        llama    
    parameters          6.7B     
    context length      2048     
    embedding length    4096     
    quantization        Q4_0     
=====================================
Running model: mistral
    architecture        llama    
    parameters          7.2B     
    context length      32768    
    embedding length    4096     
    quantization        Q4_0     
=====================================
Running model: neural-chat
    architecture        llama    
    parameters          7.2B     
    context length      32768    
    embedding length    4096     
    quantization        Q4_0
=====================================
Running model: starling-lm
    architecture        llama    
    parameters          7.2B     
    context length      8192     
    embedding length    4096     
    quantization        Q4_0     
=====================================
Running model: llava
    architecture        llama    
    parameters          7.2B     
    context length      32768    
    embedding length    4096     
    quantization        Q4_0     
    architecture        clip       
    parameters          311.89M    
    embedding length    1024       
    dimensions          768
=====================================
Running model: llama3.1
    architecture        llama     
    parameters          8.0B      
    context length      131072    
    embedding length    4096      
    quantization        Q4_K_M    
=====================================
Running model: gemma2
    architecture        gemma2    
    parameters          9.2B      
    context length      8192      
    embedding length    3584      
    quantization        Q4_0      
=====================================
Running model: solar
    architecture        llama    
    parameters          10.7B    
    context length      4096     
    embedding length    4096     
    quantization        Q4_0     
=====================================
Running model: llama3.2-vision
    architecture        mllama    
    parameters          9.8B      
    context length      131072    
    embedding length    4096      
    quantization        Q4_K_M    
    architecture        mllama     
    parameters          895.03M    
    embedding length    1280       
    dimensions          4096
"""
