---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/eks-workloads.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Learn how to deploy workloads and add-ons to Amazon EKS
<a name="eks-workloads"></a>

Your workloads are deployed in containers, which are deployed in Pods in Kubernetes. A Pod includes one or more containers. Typically, one or more Pods that provide the same service are deployed in a Kubernetes service. Once you’ve deployed multiple Pods that provide the same service, you can:
+  [View information about the workloads](view-kubernetes-resources.md) running on each of your clusters using the AWS Management Console.
+ Vertically scale Pods up or down with the Kubernetes [Vertical Pod Autoscaler](vertical-pod-autoscaler.md).
+ Horizontally scale the number of Pods needed to meet demand up or down with the Kubernetes [Horizontal Pod Autoscaler](horizontal-pod-autoscaler.md).
+ Create an external (for internet-accessible Pods) or an internal (for private Pods) [network load balancer](network-load-balancing.md) to balance network traffic across Pods. The load balancer routes traffic at Layer 4 of the OSI model.
+ Create an [Application Load Balancer](alb-ingress.md) to balance application traffic across Pods. The application load balancer routes traffic at Layer 7 of the OSI model.
+ If you’re new to Kubernetes, this topic helps you [Deploy a sample application](sample-deployment.md).
+ You can [restrict IP addresses that can be assigned to a service](restrict-service-external-ip.md) with `externalIPs`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
