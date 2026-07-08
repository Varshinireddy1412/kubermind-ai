import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.kubernetes.logs import get_pod_logs
from backend.ai.gemini_client import analyze_logs

pod_name = "flask-app-757cdb57d8-6khw6"

logs = get_pod_logs(pod_name)

print("=" * 70)
print("RAW LOGS")
print("=" * 70)
print(logs)

print("\n")
print("=" * 70)
print("AI ANALYSIS")
print("=" * 70)

result = analyze_logs(logs)

print(result)