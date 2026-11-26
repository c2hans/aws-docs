---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/kubernetes.html
---

# Use ELB for Envoy with Kubernetes

You can use Elastic Load Balancing for Envoy (ELB for Envoy) to run the Envoy proxy for your Amazon EKS workloads without operating Envoy inside your cluster. You define your routing with Kubernetes Gateway API resources, such as Gateway and HTTPRoute. Envoy Gateway runs in your cluster as the xDS control plane. Its remote infrastructure provider calls the ELB for Envoy API to create the proxy, and AWS runs the proxy fleet in the ELB for Envoy account.

If you already use Envoy Gateway, you keep your Gateway API resources and your xDS control plane. Only the place where Envoy runs changes.

**Topics**
+ [Overview](kubernetes-overview.md)
+ [Getting started](kubernetes-get-started.md)
+ [Where to learn more](kubernetes-learn-more.md)
