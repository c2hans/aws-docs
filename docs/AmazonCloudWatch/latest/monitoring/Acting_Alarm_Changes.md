---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Acting_Alarm_Changes.html
---

# Acting on alarm changes
<a name="Acting_Alarm_Changes"></a>

CloudWatch can notify users on two types of alarm changes: when an alarm changes state, and when the configuration of an alarm gets updated.

When an alarm evaluates, it might change from one state to another, such as ALARM or OK. For Metrics Insights alarms that monitor multiple time series, each time series (contributor) can only be in ALARM or OK state, never in INSUFFICIENT\_DATA state. This is because a time series only exists when data is present.

Additionally, CloudWatch sends events to Amazon EventBridge whenever alarms change state, and when alarms are created, deleted, or updated. You can write EventBridge rules to take actions or be notified when EventBridge receives these events.

For more information about alarm actions, see [Alarm actions](alarm-actions.md).

**Topics**
+ [Notifying users on alarm changes](Notify_Users_Alarm_Changes.md)
+ [Invoke a Lambda function from an alarm](alarms-and-actions-Lambda.md)
+ [Start a CloudWatch investigations from an alarm](Start-Investigation-Alarm.md)
+ [Stop, terminate, reboot, or recover an EC2 instance](UsingAlarmActions.md)
+ [Alarm events and EventBridge](cloudwatch-and-eventbridge.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
