---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/stop-cloudtrail-from-sending-events-to-cloudwatch-logs.html
---

# Stopping CloudTrail from sending events to CloudWatch Logs
<a name="stop-cloudtrail-from-sending-events-to-cloudwatch-logs"></a>

You can stop sending AWS CloudTrail events to Amazon CloudWatch Logs by updating a trail to disable CloudWatch Logs settings.

## Stop sending events to CloudWatch Logs (console)
<a name="stop-cloudtrail-from-sending-events-to-cloudwatch-logs-console"></a>

**To stop sending CloudTrail events to CloudWatch Logs**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, choose **Trails**.

1. Choose the name of the trail for which you want to disable CloudWatch Logs integration.

1. In **CloudWatch Logs**, choose **Edit**.

1. Clear the **Enabled** check box.

1. Choose **Save changes**.

## Stop sending events to CloudWatch Logs (CLI)
<a name="stop-cloudtrail-from-sending-events-to-cloudwatch-logs-cli"></a>

You can remove the CloudWatch Logs log group as a delivery endpoint by running the [**update-trail**](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md) command. The following command clears the log group and role from the trail configuration by replacing the values for the log group ARN and CloudWatch Logs role ARN with empty values.

```
aws cloudtrail update-trail --name {{trail_name}} --cloud-watch-logs-log-group-arn="" --cloud-watch-logs-role-arn=""
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
