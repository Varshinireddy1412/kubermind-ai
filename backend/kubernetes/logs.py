from kubernetes import client, config


def get_pod_logs(pod_name, namespace="default"):

    config.load_kube_config()

    v1 = client.CoreV1Api()

    logs = v1.read_namespaced_pod_log(
        name=pod_name,
        namespace=namespace,
        tail_lines=100
    )

    return logs.decode() if isinstance(logs, bytes) else logs