from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Get all pods from all namespaces
pods = v1.list_pod_for_all_namespaces()

print("\nPods in the Kubernetes Cluster")
print("-" * 80)
print(f"{'Pod Name':35} {'Namespace':25} {'Status'}")
print("-" * 80)

# Assume the cluster is healthy
problem_found = False

# Display all pods
for pod in pods.items:
    print(f"{pod.metadata.name:35} {pod.metadata.namespace:25} {pod.status.phase}")

    # Check if any pod is not running
    if pod.status.phase != "Running":
        problem_found = True

print("-" * 80)

# Display overall cluster health
if problem_found:
    print("⚠️ Cluster Health: Unhealthy")
else:
    print("✅ Cluster Health: Healthy")