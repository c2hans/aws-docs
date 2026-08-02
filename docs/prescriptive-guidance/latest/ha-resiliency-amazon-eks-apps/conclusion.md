---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

When you design your architecture for high application availability and resiliency, consider the following components:
+ The microservices application (its pods and containers)
+ The workload data plane (Ingress Controller, pod, system components such as the [Amazon VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html), service mesh sidecars, and kube-proxy)
+ The workload-management layer (controllers, admission controllers, network policy engines, and persistent data storage for these components)
+ The Kubernetes control plane
+ Infrastructure (nodes, network, and network appliances)

To address those component considerations, use the following key strategies:
+ To help ensure high availability and fault tolerance, spread workloads across nodes and Availability Zones.
+ To protect critical workloads, maintain application stability during disruptions by using pod disruption budgets (PDBs).
+ To help ensure that pods are running and serving traffic correctly, configure startup probes, liveness probes, readiness probes, and load balancer health checks.
+ To manage container state transitions efficiently, configure container lifecycle hooks.
+ To provide control over the eviction process during node failures or maintenance, configure the pod eviction time.

By implementing these practices, you can significantly enhance the reliability and resilience of applications running on Amazon EKS, ensuring robust performance and high availability.
