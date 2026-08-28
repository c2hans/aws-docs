---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-work-with-eks.html
---

# Work with EKS
<a name="CloudWatch-NetworkFlowMonitor-work-with-eks"></a>

Using Network Flow Monitor, you can collect performance metrics for workloads that use Amazon Elastic Kubernetes Service (Amazon EKS). This chapter shows you how to install the agent step-by-step and describes the different EKS scenarios you can monitor. You'll also find detailed descriptions of the metadata that Network Flow Monitor provides for Amazon EKS in the console to help you understand network performance.

To gain the benefits of Network Flow Monitor performance monitoring, you must first install the AWS Network Flow Monitor Agent add-on for Amazon EKS. For more information, see [Install the EKS AWS Network Flow Monitor Agent add-on](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md).

If you want to monitor a single EKS cluster with enhanced visibility of workload traffic and performance insights within the cluster and with external destinations, see [Amazon EKS Network Observability](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html).

**Topics**
+ [Install the EKS AWS Network Flow Monitor Agent add-on](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md)
+ [Additional network path metadata included for Amazon EKS](CloudWatch-NetworkFlowMonitor-work-with-eks.performance-metadata.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
