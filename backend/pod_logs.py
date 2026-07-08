from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Pod name (change this if you want another pod)
pod_name = "flask-app-757cdb57d8-6khw6"
namespace = "default"

# Read logs
logs = v1.read_namespaced_pod_log(
    name=pod_name,
    namespace=namespace
)

print("=" * 60)
print(f"Logs for Pod: {pod_name}")
print("=" * 60)
print(logs)