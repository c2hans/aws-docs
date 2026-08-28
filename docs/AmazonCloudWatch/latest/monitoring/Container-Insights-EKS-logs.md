---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html
---

# Send logs to CloudWatch Logs
<a name="Container-Insights-EKS-logs"></a>

To send logs from your containers to Amazon CloudWatch Logs, you can use Fluent Bit. For more information, see [Fluent Bit](https://fluentbit.io/).

**Note**
As of February 10 2025, AWS has deprecated support for FluentD as a log forwarder to CloudWatch Logs. We recommend that you use Fluent Bit, which is a lightweight and resource-efficient alternative. Existing FluentD deployments will continue to function. Migrate your logging pipeline to Fluent Bit to make sure continued support and optimal performance.
Container Insights previously also supported using FluentD to send logs from your containers. FluentD has been deprecated and is now not supported for Container Insights. Use Fluent Bit instead.

**Topics**
+ [Set up Fluent Bit as a DaemonSet to send logs to CloudWatch Logs](Container-Insights-setup-logs-FluentBit.md)
+ [(Optional) Set up Amazon EKS control plane logging](Container-Insights-setup-control-plane-logging.md)
+ [(Optional) Enable the Use\_Kubelet feature for large clusters](ContainerInsights-use-kubelet.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
