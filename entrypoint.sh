#!/bin/bash
# Example of pulling and starting Llama 3.1

# Ensure the correct path is set
export PATH=$PATH:/path/to/ollama

# Command to pull the Llama 3.1 model
ollama pull llama-3.1

# Command to start the Ollama service
ollama serve --port 7869