from kubernetes import client, config


class KubernetesClient:
    """Small wrapper around the Kubernetes API."""

    def __init__(self) -> None:
        try:
            config.load_kube_config()
        except config.ConfigException:
            config.load_incluster_config()

        self.apps_api = client.AppsV1Api()

    def get_replicas(self, deployment_name: str, namespace: str = "default") -> int:
        """Return the current desired replica count."""
        deployment = self.apps_api.read_namespaced_deployment(
            name=deployment_name,
            namespace=namespace,
        )

        return deployment.spec.replicas or 0

    def scale_deployment(
        self,
        deployment_name: str,
        replicas: int,
        namespace: str = "default",
    ) -> None:
        """Update the desired replica count of a deployment."""
        body = {
            "spec": {
                "replicas": replicas,
            }
        }

        self.apps_api.patch_namespaced_deployment(
            name=deployment_name,
            namespace=namespace,
            body=body,
        )