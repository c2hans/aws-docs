---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html
---

# Amazon SNS message delivery status
<a name="sns-topic-attributes"></a>

Amazon SNS provides support for logging the delivery status of notification messages sent to topics with the following Amazon SNS endpoints:
+ Amazon Data Firehose
+ Amazon Simple Queue Service
+ AWS Lambda
+ HTTPS
+ Platform application endpoint

Delivery status logs are sent to Amazon CloudWatch Logs, providing insights into message delivery operations. These logs help you:
+ Determine whether a message was successfully delivered to an endpoint.
+ Identify the response from the endpoint to Amazon SNS.
+ Measure message dwell time (time between publish timestamp and handoff to the endpoint).

You can configure delivery status logging using the AWS Management Console, AWS SDKs, Query API, or AWS CloudFormation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
