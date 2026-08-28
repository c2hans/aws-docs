---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.advanced-options.html
---

# Advanced configuration options for a monitor
<a name="CloudWatch-IM-get-started.advanced-options"></a>

This section provides the steps for configuring advanced options for a monitor in Internet Monitor. These configuration options are optional but can be useful in some scenarios.

For example, you might choose to set a city-network maximum limit if traffic for the application that you monitor with Internet Monitor occasionally spikes, and you want to help make sure that your bill for Internet Monitor is predictable.

Or, you might want to set custom or local thresholds for health events, because you want to pay close attention to issues in specific geographies where you have a concentration of clients.

The topics in this section provide detailed descriptions of each feature, and list the steps to configure options for your needs.

**Topics**
+ [Choose a city-networks limit](IMCityNetworksMaximum.md)
+ [Change health event thresholds](CloudWatch-IM-get-started.change-threshold.md)
+ [Publish internet measurements to S3](CloudWatch-IM-get-started.Publish-to-S3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
