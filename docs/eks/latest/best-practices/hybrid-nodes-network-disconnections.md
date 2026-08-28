---
source_url: https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-network-disconnections.html
---

# EKS Hybrid Nodes and network disconnections
<a name="hybrid-nodes-network-disconnections"></a>

The EKS Hybrid Nodes architecture can be new to customers who are accustomed to running local Kubernetes clusters entirely in their own data centers or edge locations. With EKS Hybrid Nodes, the Kubernetes control plane runs in an AWS Region and only the nodes run on-premises, resulting in a “stretched” or “extended” Kubernetes cluster architecture.

This leads to a common question, “What happens if my nodes get disconnected from the Kubernetes control plane?”

In this guide, we answer that question through a review of the following topics. It is recommended to validate the stability and reliability of your applications through network disconnections as each application may behave differently based on its dependencies, configuration, and environment. See the aws-samples/eks-hybrid-examples GitHub repo for test setup, procedures, and results you can reference to test network disconnections with EKS Hybrid Nodes and your own applications. The GitHub repo also contains additional details of the tests used to validate the behavior explained in this guide.
+  [Best practices for stability through network disconnections](hybrid-nodes-network-disconnection-best-practices.md)
+  [Kubernetes pod failover behavior through network disconnections](hybrid-nodes-kubernetes-pod-failover.md)
+  [Application network traffic through network disconnections](hybrid-nodes-app-network-traffic.md)
+  [Host credentials through network disconnections](hybrid-nodes-host-creds.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
