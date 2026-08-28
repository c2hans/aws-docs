---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-with-cloudwatch-events.html
---

# Monitoring with Amazon EventBridge events
<a name="monitoring-with-cloudwatch-events"></a>

EventBridge enables you to automate your AWS services and respond automatically to system events such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you, and what automated actions to take when an event matches a rule.

The actions that can be automatically triggered using EventBridge include the following:
+ Invoking an AWS Lambda function
+ Invoking Amazon EC2 Run Command
+ Relaying the event to Amazon Kinesis Data Streams
+ Activating an AWS Step Functions state machine
+ Notifying an Amazon SNS topic or an Amazon SQS queue

For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

**Topics**
+ [MediaConnect flow state change event](monitoring-cloudwatch-events-flow-state-change.md)
+ [MediaConnect flow maintenance event](monitoring-cloudwatch-events-flow-maintenance.md)
+ [MediaConnect flow health event](monitoring-cloudwatch-events-flow-health.md)
+ [MediaConnect alert event](monitoring-cloudwatch-events-alert.md)
+ [MediaConnect source health event](monitoring-cloudwatch-events-source-health.md)
+ [MediaConnect output health event](monitoring-cloudwatch-events-output-health.md)
+ [MediaConnect output status change event](monitoring-cloudwatch-events-output-status-change.md)
+ [MediaConnect flow content quality event](monitoring-eventbridge-events-content-quality.md)
+ [MediaConnect router input content quality event](monitoring-eventbridge-events-router-input-content-quality.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
