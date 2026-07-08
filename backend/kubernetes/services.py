from kubernetes import client, config


def get_all_services():
    """
    Returns all Kubernetes services.
    """
    config.load_kube_config()

    v1 = client.CoreV1Api()
    services = v1.list_service_for_all_namespaces()

    service_list = []

    for service in services.items:
        service_list.append({
            "name": service.metadata.name,
            "namespace": service.metadata.namespace,
            "type": service.spec.type
        })

    return service_list