---
source_url: https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html
---

# Service Quotas and Amazon CloudWatch alarms
<a name="configure-cloudwatch"></a>

You can create Amazon CloudWatch alarms to notify you when you're close to a quota value threshold. Setting an alarm can help alert you if you need to request a quota increase.

**To create a CloudWatch alarm for a quota**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, choose **AWS services** and then select a service.

1. Select a quota that supports CloudWatch alarms.

   If you actively use the quota, utilization appears beneath the quota description. If CloudWatch alarms are supported, the CloudWatch alarms section appears at the bottom of the page.

1. In **Amazon CloudWatch alarms**, choose **Create**.

1. For **Alarm threshold**, choose a threshold.

1. For **Alarm name**, enter a name for the alarm. This name must be unique within the AWS account.

1. Choose **Create**.

**Note**
To add a notification to the CloudWatch alarm, see [Creating a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the *Amazon CloudWatch User Guide*.

**To delete a CloudWatch alarm**

1. Choose the service quota with the alarm.

1. Select the alarm.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
