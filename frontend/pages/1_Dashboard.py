import streamlit as st

from backend.kubernetes.cluster import get_cluster_info
from backend.kubernetes.pods import get_all_pods
from backend.kubernetes.services import get_all_services

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("📊 AI Kubernetes Agent Dashboard")
st.markdown("### Live Kubernetes Cluster Monitoring")

st.divider()

# ---------------- LOAD DATA ----------------

pods = []
nodes = []
services = []

try:
    pods = get_all_pods()
except Exception as e:
    st.error(f"Pods Error: {e}")

try:
    nodes = get_cluster_info()
except Exception as e:
    st.error(f"Nodes Error: {e}")

try:
    services = get_all_services()
except Exception as e:
    st.error(f"Services Error: {e}")

pod_count = len(pods)
node_count = len(nodes)
service_count = len(services)

cluster_status = "🟢 Healthy" if node_count > 0 else "🔴 Unavailable"

# ---------------- METRICS ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Pods", pod_count)
col2.metric("Nodes", node_count)
col3.metric("Services", service_count)
col4.metric("Cluster", cluster_status)

st.divider()

# ---------------- POD TABLE ----------------

st.subheader("📦 Running Pods")

if pods:

    pod_table = []

    for pod in pods:

        pod_table.append({
            "Pod Name": pod["name"],
            "Namespace": pod["namespace"],
            "Status": pod["status"]
        })

    st.dataframe(
        pod_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("No pods found.")

st.divider()

# ---------------- SERVICES ----------------

st.subheader("🌐 Kubernetes Services")

if services:

    service_table = []

    for service in services:

        service_table.append({
            "Service": service["name"],
            "Namespace": service["namespace"],
            "Type": service["type"]
        })

    st.dataframe(
        service_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("No services found.")