---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-cloudwatch-events.html
---

# Monitoring AWS Elemental MediaPackage with CloudWatch Events
<a name="monitoring-cloudwatch-events"></a>

Amazon CloudWatch Events enables you to automate your AWS services and respond automatically to system events such as application availability issues or error conditions. AWS services deliver events to CloudWatch Events in near real-time. You can write simple rules to indicate which events are of interest to you, and what automated actions to take when an event matches a rule. The actions that can be automatically triggered include the following:
+ Invoking an AWS Lambda function
+ Invoking AWS Systems Manager Run Command
+ Relaying the event to Amazon Kinesis Data Streams
+ Activating an AWS Step Functions state machine

An example of using CloudWatch Events with MediaPackage is notifying an Amazon SNS topic if you reach the maximum stream input. MediaPackage emits events on a best effort basis.

For more information about creating rules in CloudWatch Events, see the [Amazon CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/).

For a list of events that MediaPackage emits, see [AWS Elemental MediaPackage events](cloudwatch-events-example.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
