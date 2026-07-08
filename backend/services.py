from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Get all services
services = v1.list_service_for_all_namespaces()

print("\nKubernetes Services")
print("-" * 80)
print(f"{'Service Name':30} {'Namespace':20} {'Type'}")
print("-" * 80)

for service in services.items:
    print(
        f"{service.metadata.name:30} "
        f"{service.metadata.namespace:20} "
        f"{service.spec.type}"
    )