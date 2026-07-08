from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

nodes = v1.list_node()

print("Cluster Information")
print("-" * 40)
print(f"Total Nodes: {len(nodes.items)}")

for node in nodes.items:
    print(f"Node Name : {node.metadata.name}")
    print(f"Status    : {node.status.conditions[-1].type}")
    print("-" * 40)