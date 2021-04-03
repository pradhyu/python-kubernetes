from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

ret2 = v1.list_service_for_all_namespaces(watch=False)
for item in ret2.items:
    print(f"{item.metadata.namespace} -> {item.metadata.name}")
