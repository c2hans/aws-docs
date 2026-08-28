---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-troubleshooting.html
---

# Troubleshoot issues in Network Flow Monitor
<a name="CloudWatch-NetworkFlowMonitor-troubleshooting"></a>

This section provides guidance for troubleshooting errors with Network Flow Monitor, including solving issues with installing agents.

## Troubleshoot issues in EKS agents installation
<a name="CloudWatch-NetworkFlowMonitor-troubleshooting.ec2-agent-installation"></a>

When you try to upgrade the AWS Network Flow Monitor Agent add-on for EKS from v1.0.0 to v1.0.1 in AWS Management Console, you might receive the following error message:

"Service account `aws-network-flow-monitoring-agent-service-account` in pod identity configuration is not supported for addon `aws-network-flow-monitoring-agent`."

This error is returned because a resource was renamed. The EKS add-on v1.0.1 changes the service account name from `aws-network-flow-monitoring-agent-service-account` to `aws-network-flow-monitor-agent-service-account`.

Then, if **Not set** is not selected in the console, the pod identity association is not reset to the new resource name.

To fix this issue, do the following when you upgrade to the new version by using the console:

1. Under **Pod Identity IAM role for service account**, select **Not set**.

1. Select **New version (v1.0.1)**.

1. Select **Upgrade**.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
