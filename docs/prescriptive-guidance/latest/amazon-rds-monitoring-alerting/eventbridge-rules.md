---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/eventbridge-rules.html
---

# EventBridge rules
<a name="eventbridge-rules"></a>

[Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html) are delivered to EventBridge, and you can use [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) to react to those events. For example, you can create EventBridge rules that would notify you and take an action if one specific DB instance stops or starts up, as the following screen shows.

![Eventbridge rules for DB instance stops and starts](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/65136ef3-f99e-4d7c-a30a-44220d89af1a.png)

The rule that detects *The DB instance has been stopped* event has the Amazon RDS event ID `RDS-EVENT-0087`, so you set the `Event Pattern` property of the rule to:

```
{
  "source": ["aws.rds"],
  "detail-type": ["RDS DB Instance Event"],
  "detail": {
    "SourceArn": ["arn:aws:rds:eu-west-3:111122223333:db:database-3"],
    "EventID": ["RDS-EVENT-0087"]
  }
}
```

This rule monitors the DB instance `database-3` only, and watches for the `RDS-EVENT-0087` event. When EventBridge detects the event, it sends the event to a resource or endpoint, known as a [target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html). This is where you can specify the action you want to take if the Amazon RDS instance shuts down. You can send the event to many possible targets, including an SNS topic, an Amazon Simple Queue Service (Amazon SQS) queue, a Lambda function, AWS Systems Manager Automation, an AWS Batch job, API Gateway, and many others. For example, you might create an SNS topic that will send a notification email and SMS, and assign that SNS topic as the target of the EventBridge rule. If the Amazon RDS DB instance `database-3` has been stopped, Amazon RDS delivers the event `RDS-EVENT-0087` to EventBridge, where it gets detected. EventBridge then calls the target, which is the SNS topic. The SNS topic is configured to send an email (as shown in the following illustration) and an SMS.

![SNS topic configuration](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/d1794204-4e5c-4241-9388-db9dc7adffb7.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
