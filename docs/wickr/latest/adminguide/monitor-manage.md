---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/monitor-manage.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Monitoring and management
<a name="monitor-manage"></a>

## CloudWatch dashboards
<a name="cloudwatch-dashboards"></a>

Complete the following procedure to access CloudWatch dashboards.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **CloudWatch**.

1. Select **Dashboards**, and then select `WickrDataRetentionService-[NetworkID]`.

The deployment automatically creates CloudWatch dashboards showing:
+ **Error Rate**: Failed message processing attempts
+ **Storage Metrics**: S3 bucket size and object count

## Automatic alarms
<a name="automatic-alarms"></a>

Pre-configured CloudWatch alarms notify you of:
+ **Processing Failures**: Any messages failing to decrypt or store

Complete the following procedure to configure alarm notifications.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **CloudWatch**.

1. Choose **Alarms**.

1. Select a **Wickr Data Retention** alarm.

1. Choose **Actions**, and then choose **Edit**.

1. Add SNS topic for email and SMS notifications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
