---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-install-EKS.html
---

# Set up and configure Prometheus metrics collection on Amazon EKS and Kubernetes clusters
<a name="ContainerInsights-Prometheus-install-EKS"></a>

To collect Prometheus metrics from clusters running Amazon EKS or Kubernetes, you can use the CloudWatch agent as a collector or use the AWS Distro for OpenTelemetry collector. For information about using the AWS Distro for OpenTelemetry collector, see [https://aws-otel.github.io/docs/getting-started/container-insights/eks-prometheus](https://aws-otel.github.io/docs/getting-started/container-insights/eks-prometheus).

The following sections explain how to collect Prometheus metrics using the CloudWatch agent. They explain how to install the CloudWatch agent with Prometheus monitoring on clusters running Amazon EKS or Kubernetes, and how to configure the agent to scrape additional targets. They also provide optional tutorials for setting up sample workloads to use for testing with Prometheus monitoring.

**Topics**
+ [Install the CloudWatch agent with Prometheus metrics collection on Amazon EKS and Kubernetes clusters](ContainerInsights-Prometheus-Setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
