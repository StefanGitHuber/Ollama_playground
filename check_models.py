#!/usr/bin/env python
# coding: utf-8

import subprocess
import json
import sys
import time

# System shell command interface
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
        return None

# Retrieve list of local Ollama models
def get_installed_models():
    output = run_command("ollama list")
    if output is None:
        return []

    # Skip header line and parse model names
    models = []
    for line in output.strip().split('\n')[1:]:
        if line:
            # First word in line = model name
            models.append(line.split()[0])
    return models

# Ollama pull <model>
def download_model(model_name):
    print(f"Downloading {model_name} ...")
    result = run_command(f"ollama pull {model_name}")
    if result is not None:
        print(f"Successfully downloaded {model_name}")
        return True
    else:
        print(f"Failed to download {model_name}")
        return False

# Check Ollama installation + required models, installing missing ones
def check_install_models(model_list):
    if run_command("ollama --version") is None:
        return False
    installed_models = get_installed_models()
    for model in model_list:
        if model not in installed_models:
            download_model(model)
