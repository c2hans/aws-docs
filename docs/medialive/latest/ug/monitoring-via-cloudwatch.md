---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitoring-via-cloudwatch.html
---

# Monitoring a channel or multiplex using Amazon CloudWatch Events
<a name="monitoring-via-cloudwatch"></a>

MediaLive automatically turns the following information into events in CloudWatch Events:
+ Reporting on the [state of a channel or multiplex](monitor-activity-types-channel.md).
+ [Alerts ](monitor-activity-types-alerts-channels.md)generated when a channel is running.

You can use Amazon CloudWatch Events to manage these events. For example, you can create event rules and deliver the events in emails or SMS messages. You can deliver events to a number of destinations. This chapter describes how to deliver them through Amazon Simple Notification Service (SNS).

For complete information about the options for managing events using Amazon CloudWatch Events, see the [CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html).

For complete information about using Amazon SNS, see the [SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

Note that events are emitted on a best-effort basis.

**Topics**
+ [JSON for a state change event](monitoring-cloudwatch-json-state-change.md)
+ [JSON for an alert event](monitoring-cloudwatch-json-alert.md)
+ [Option 1: Send all MediaLive events to an email address](option-1.md)
+ [Option 2: Send events for specific channels to an email address](option-2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
