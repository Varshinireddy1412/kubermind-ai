from kubernetes import client, config


def get_all_pods():
    """
    Returns all pods in the Kubernetes cluster.
    """
    config.load_kube_config()

    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces()

    pod_list = []

    for pod in pods.items:
        pod_list.append({
            "name": pod.metadata.name,
            "namespace": pod.metadata.namespace,
            "status": pod.status.phase
        })

    return pod_list