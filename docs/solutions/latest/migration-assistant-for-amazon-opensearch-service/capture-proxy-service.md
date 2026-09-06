---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/capture-proxy-service.html
---

# Capture Proxy Service on Amazon EKS
<a name="capture-proxy-service"></a>

For zero-downtime migrations, the workflow creates capture proxy pods, a Kubernetes Service in front of those pods, and Apache Kafka wiring so captured traffic can be replayed later. Client traffic is sent to the proxy Service, which forwards requests to the source cluster and records them for later replay. On Amazon EKS, the Service can be backed by AWS load-balancer infrastructure (Application Load Balancer or Network Load Balancer), and the bootstrap path handles the platform wiring for you.

The proxy is secure by default. If you do not configure TLS explicitly, the workflow provisions a self-signed certificate for the proxy. You can also configure cert-manager-issued certificates, an existing AWS Private CA, or a new AWS Private CA via ACK using the bootstrap script’s TLS flags. If you intentionally want plaintext HTTP, set the proxy TLS mode to `plaintext`.
