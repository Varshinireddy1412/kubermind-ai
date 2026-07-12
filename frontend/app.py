import streamlit as st

st.set_page_config(
    page_title="AI Kubernetes Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Kubernetes Agent")

st.markdown("""
# Welcome 👋

This is the main page of the AI Kubernetes Agent.

Use the navigation menu on the left to access different modules.
""")

st.info("""
Available Modules

📊 Dashboard

📦 Pods

📜 Logs

🚀 Deployments

🤖 AI Assistant

⚙️ Settings
""")

st.success("Select a page from the left sidebar to continue.")