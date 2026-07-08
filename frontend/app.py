import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from backend.kubernetes.cluster import get_cluster_info
from backend.kubernetes.pods import get_all_pods
from backend.kubernetes.services import get_all_services
from backend.kubernetes.logs import get_pod_logs
from backend.ai.gemini_client import analyze_logs

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Kubernetes Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD DATA ----------------

pods = []
nodes = []
services = []

# Load Pods
try:
    pods = get_all_pods()
except Exception as e:
    st.error(f"Pods Error:\n{e}")

# Load Nodes
try:
    nodes = get_cluster_info()
except Exception as e:
    st.error(f"Nodes Error:\n{e}")

# Load Services
try:
    services = get_all_services()
except Exception as e:
    st.error(f"Services Error:\n{e}")

pod_count = len(pods)
node_count = len(nodes)
service_count = len(services)

cluster_status = "Healthy"

if node_count == 0:
    cluster_status = "Unavailable"

# ---------------- CSS ----------------

st.markdown("""
<style>

.main{
background:#0f172a;
}

section[data-testid="stSidebar"]{
background:#111827;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white;
}

.block-container{
padding-top:2rem;
}

.metric-card{
background:#1e293b;
padding:25px;
border-radius:18px;
text-align:center;
box-shadow:0px 6px 20px rgba(0,0,0,.4);
}

.metric-number{
font-size:40px;
font-weight:bold;
color:#38bdf8;
}

.metric-title{
color:#cbd5e1;
font-size:18px;
}

.hero{
background:linear-gradient(90deg,#2563eb,#06b6d4);
padding:25px;
border-radius:18px;
margin-bottom:25px;
text-align:center;
color:white;
}

.stButton>button{
width:100%;
height:45px;
border-radius:10px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 AI Kubernetes Agent")

    st.markdown("---")

    st.button("🏠 Dashboard")
    st.button("📦 Pods")
    st.button("📜 Logs")
    st.button("🚀 Deployments")
    st.button("🤖 AI Assistant")
    st.button("⚙️ Settings")

# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
<h1>🤖 AI Kubernetes Agent</h1>
<h4>AI Powered Kubernetes & DevOps Assistant</h4>
</div>
""", unsafe_allow_html=True)

# ---------------- METRICS ----------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{pod_count}</div>
<div class="metric-title">Pods</div>
</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{node_count}</div>
<div class="metric-title">Nodes</div>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{service_count}</div>
<div class="metric-title">Services</div>
</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-number">{cluster_status}</div>
<div class="metric-title">Cluster</div>
</div>
""",unsafe_allow_html=True)

st.divider()

# ---------------- PODS ----------------

st.subheader("📦 Kubernetes Pods")

if pods:

    for pod in pods:

        status="🟢"

        if pod["status"]!="Running":
            status="🔴"

        st.success(
            f"{status} {pod['name']} | Namespace : {pod['namespace']} | Status : {pod['status']}"
        )

else:

    st.warning("No Pods Found")

st.divider()

# ---------------- AI ----------------

st.subheader("🤖 AI Assistant")

if pods:

    pod_names=[pod["name"] for pod in pods]

    selected_pod=st.selectbox(
        "Select Pod",
        pod_names
    )

    if st.button("Analyze Selected Pod"):

        try:

            logs=get_pod_logs(selected_pod)

            st.subheader("📜 Pod Logs")

            st.code(logs)

            result=analyze_logs(logs)

            st.subheader("🤖 AI Analysis")

            st.write(result)

        except Exception as e:

            st.error(e)

else:

    st.warning("No Pods Available")