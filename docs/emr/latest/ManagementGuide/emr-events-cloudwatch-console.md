---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-events-cloudwatch-console.html
---

# Creating rules for Amazon EMR events with CloudWatch
<a name="emr-events-cloudwatch-console"></a>

Amazon EMR automatically sends events to a CloudWatch event stream. You can create rules that match events according to a specified pattern, and route the events to targets to take action, such as sending an email notification. Patterns are matched against the event JSON object. For more information about Amazon EMR event details, see [Amazon EMR events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#emr_event_type) in the *Amazon CloudWatch Events User Guide*.

For information about setting up CloudWatch event rules, see [Creating a CloudWatch rule that triggers on an event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
