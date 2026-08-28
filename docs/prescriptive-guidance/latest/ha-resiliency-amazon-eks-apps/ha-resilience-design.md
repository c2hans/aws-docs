---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/ha-resilience-design.html
---

# HA and resilience design considerations
<a name="ha-resilience-design"></a>

The shared responsibility model becomes more complex with Kubernetes. Amazon EKS control plane availability and resilience are managed by Amazon Web Services (AWS). Your organization manages the data plane, which can significantly affect the performance and availability of your microservices applications.

When designing a highly available and resilient application on Amazon EKS, consider the following components:
+ The microservices application: its pods and containers
+ The workload data plane: Ingress Controller, pod, system components such as the [Amazon Virtual Private Cloud (Amazon VPC) Container Network Interface (CNI)](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html), service mesh sidecars, and kube-proxy
+ The workload-mangement layer: controllers, admission controllers, network policy engines, and persistent data storage for these components
+ The Kubernetes control plane
+ Infrastructure: nodes, network, and network appliances

For the first three considerations, which refer to components that run within a Kubernetes cluster, this guide covers the following topics:
+ [Spreading workloads across nodes and Availability Zones](spread-workloads.md)
+ [Protecting critical workloads with a PDB](pdb.md)
+ [Configuring probes and health checks](probes-checks.md)
+ [Configuring container lifecycle hooks](lifecycle-hooks.md)
+ [Understanding pod eviction during zonal disruptions](pod-eviction.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
