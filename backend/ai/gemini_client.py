

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_logs(logs):
    """
    Analyze Kubernetes logs using Gemini AI.
    """

    prompt = f"""
You are an expert Kubernetes and DevOps Engineer.

Analyze these Kubernetes pod logs.

Answer in this format:

Overall Status:
Errors Found:
Root Cause:
Recommended Fix:
Best Practices:

Logs:

{logs}
"""

    response = model.generate_content(prompt)

    return response.text