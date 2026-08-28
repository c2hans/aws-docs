---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_event_response_auto_event_response.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP07 Automate responses to events
<a name="ops_event_response_auto_event_response"></a>

 Automate responses to events to reduce errors caused by manual processes, and to ensure prompt and consistent responses.

 There are multiple ways to automate runbook and playbook actions on AWS. To respond to an event from a state change in your AWS resources, or from your own custom events, you should create [CloudWatch Events rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) to trigger responses through CloudWatch targets (for example, Lambda functions, Amazon Simple Notification Service (Amazon SNS) topics, Amazon ECS tasks, and AWS Systems Manager Automation).

 To respond to a metric that crosses a threshold for a resource (for example, wait time), you should create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to perform one or more actions using Amazon EC2 actions, Auto Scaling actions, or to send a notification to an Amazon SNS topic. If you need to perform custom actions in response to an alarm, invoke Lambda through an Amazon SNS notification. Use Amazon SNS to publish event notifications and escalation messages to keep people informed.

 AWS also supports third-party systems through the AWS service APIs and SDKs. There are a number of monitoring tools provided by AWS Partners and third parties that allow for monitoring, notifications, and responses. Some of these tools include New Relic, Splunk, Loggly, SumoLogic, and Datadog.

 You should keep critical manual procedures available for use when automated procedures fail

 **Common anti-patterns:**
+  A developer checks in their code. This event could have been used to start a build and then perform testing but instead nothing happens.
+  Your application logs a specific error before it stops working. The procedure to restart the application is well understood and could be scripted. You could use the log event to invoke a script and restart the application. Instead, when the error happens at 3am Sunday morning, you are woken up as the on-call resource responsible to fix the system.

 **Benefits of establishing this best practice:** By using automated responses to events, you reduce the time to respond and limit the introduction of errors from manual activities.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate responses to events: Automate responses to events to reduce errors caused by manual processes, and to ensure prompt and consistent responses.
  +  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
  +  [Creating a CloudWatch Events rule that triggers on an event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html)
  +  [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html)
  +  [CloudWatch Events event examples from supported services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch Features](https://aws.amazon.com/cloudwatch/features/)
+  [CloudWatch Events event examples from supported services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html)
+  [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html)
+  [Creating a CloudWatch Events rule that triggers on an event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html)
+  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)

 **Related videos:**
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU)

 **Related examples:**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
