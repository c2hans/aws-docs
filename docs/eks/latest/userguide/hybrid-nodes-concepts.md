---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-concepts.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Concepts for hybrid nodes
<a name="hybrid-nodes-concepts"></a>

With *Amazon EKS Hybrid Nodes*, you join physical or virtual machines running in on-premises or edge environments to Amazon EKS clusters running in the AWS Cloud. This approach brings many benefits, but also introduces new networking concepts and architectures for those familiar with running Kubernetes clusters in a single network environment.

The following sections dive deep into the Kubernetes and networking concepts for EKS Hybrid Nodes and details how traffic flows through the hybrid architecture. These sections require that you are familiar with basic Kubernetes networking knowledge, such as the concepts of pods, nodes, services, Kubernetes control plane, kubelet and kube-proxy.

We recommend reading these pages in order, starting with the [Networking concepts for hybrid nodes](hybrid-nodes-concepts-networking.md), then the [Kubernetes concepts for hybrid nodes](hybrid-nodes-concepts-kubernetes.md), and finally the [Network traffic flows for hybrid nodes](hybrid-nodes-concepts-traffic-flows.md).

**Topics**
+ [Networking concepts for hybrid nodes](hybrid-nodes-concepts-networking.md)
+ [Kubernetes concepts for hybrid nodes](hybrid-nodes-concepts-kubernetes.md)
+ [Network traffic flows for hybrid nodes](hybrid-nodes-concepts-traffic-flows.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
