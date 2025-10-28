"""
Configuration template for AI Fashion Stylist
Copy this to config.py and add your actual API keys
"""

import os

# NVIDIA API Configuration
NVIDIA_API_KEY = "your-nvidia-api-key-here"  # Replace with your actual NVIDIA API key
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

# Application Settings
MAX_TOKENS = 1000
TEMPERATURE = 0.7
TIMEOUT_SECONDS = 30

# Scoring Weights
FUZZY_WEIGHT = 0.6
QUANTUM_WEIGHT = 0.4
MEMORY_BIAS_WEIGHT = 0.05

# Fashion Database
FASHION_DB_PATH = "fashion_db.json"
MEMORY_FILE_PATH = "memory.json"

# Web Application Settings
WEB_HOST = "0.0.0.0"
WEB_PORT = 5001
DEBUG_MODE = True

def get_nvidia_headers():
    """Get headers for NVIDIA API requests"""
    return {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

def get_api_config():
    """Get API configuration dictionary"""
    return {
        "nvidia_api_key": NVIDIA_API_KEY,
        "nvidia_base_url": NVIDIA_BASE_URL,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "timeout": TIMEOUT_SECONDS
    }