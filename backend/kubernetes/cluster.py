from kubernetes import client, config


def get_cluster_info():
    """
    Returns Kubernetes cluster node information.
    """
    config.load_kube_config()

    v1 = client.CoreV1Api()
    nodes = v1.list_node()

    cluster_data = []

    for node in nodes.items:
        cluster_data.append({
            "name": node.metadata.name,
            "status": node.status.conditions[-1].type
        })

    return cluster_data