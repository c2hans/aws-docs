---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-setting-up-alarms.html
---

# Setting up alarms on error logs
<a name="logging-setting-up-alarms"></a>

We recommend setting up a monitoring system on your `ERROR` logs to alert you of consistent failures. You can use Amazon CloudWatch metric filters and alarms to detect error patterns automatically.

**To create an alarm on error logs**

1. Create a metric filter on the `/aws/iotmanagedintegrations/EventLog` log group that matches error-level log entries.

1. Create a CloudWatch alarm on the metric filter that triggers when the error count exceeds your threshold.

1. Configure an Amazon Simple Notification Service topic as the alarm action to receive notifications.

For detailed instructions, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
