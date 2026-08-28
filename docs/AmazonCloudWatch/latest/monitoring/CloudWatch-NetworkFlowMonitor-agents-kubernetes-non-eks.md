---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.html
---

# Install agents for self-managed Kubernetes instances
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks"></a>

Follow the steps in this section to install Network Flow Monitor agents for workloads on self-managed Kubernetes clusters. After you complete the steps, Network Flow Monitor agent pods will be running on all of your self-managed Kubernetes cluster nodes.

If you use Amazon Elastic Kubernetes Service (Amazon EKS), the installation steps to follow are in the following section: [Install the EKS AWS Network Flow Monitor Agent add-on](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md).

**Topics**
+ [Before you begin](CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin.md)
+ [Download Helm charts and install agents](CloudWatch-NetworkFlowMonitor-agents-kubernetes-install-agents.md)
+ [Configure permissions for agents to deliver metrics](CloudWatch-NetworkFlowMonitor-agents-kubernetes-permissions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
