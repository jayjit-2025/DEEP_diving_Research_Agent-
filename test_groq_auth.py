#!/usr/bin/env python3
"""
Test script to verify Groq API key and connectivity with Llama 3.3 70B
"""

import os
import sys

def test_groq_auth():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        if len(sys.argv) > 1:
            api_key = sys.argv[1]
        else:
            api_key = input("Enter your Groq API key (starts with gsk_...): ").strip()
    
    if not api_key:
        print("❌ Error: No API key provided.")
        return False
        
    print(f"Testing Groq authentication with model llama-3.3-70b-versatile...")
    try:
        from langchain.chat_models import init_chat_model
        model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq", api_key=api_key)
        response = model.invoke("Say hello in one brief sentence.")
        print("✅ Success! Response from Groq:")
        print(response.content)
        return True
    except Exception as e:
        print(f"❌ Groq authentication/call failed: {e}")
        return False

if __name__ == "__main__":
    test_groq_auth()
