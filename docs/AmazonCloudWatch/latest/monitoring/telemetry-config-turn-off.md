---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-off.html
---

# Disabling telemetry configuration
<a name="telemetry-config-turn-off"></a>

When you no longer need telemetry configuration, you can turn it off. When telemetry configuration is turned off, it no longer shows the status of telemetry for resources in your account or organization. You can turn on telemetry configuration again at any time. For more information, see [Setting up telemetry configuration](telemetry-config-turn-on.md).

**To turn off telemetry configuration**

1. [Open the CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#telemetry-config:account-settings).

1. In the navigation pane, choose **Ingestion**.

1. Choose **Turn off**.

**Note**
Turning off telemetry configuration does not delete or modify any existing telemetry settings for your resources. It only stops the centralized management and visibility of these settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
