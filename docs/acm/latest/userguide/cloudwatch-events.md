---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html
---

# Using Amazon EventBridge
<a name="cloudwatch-events"></a>

You can use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) (formerly CloudWatch Events) to automate your AWS services and respond automatically to system events such as application availability issues or resource changes. Events from AWS services, including ACM, are delivered to Amazon EventBridge in near-real time. You can use events to trigger targets including AWS Lambda functions, AWS Batch jobs, Amazon SNS topics, and many others. For more information, see [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)

**Topics**
+ [Amazon EventBridge support for ACM](supported-events.md)
+ [Initiating actions with Amazon EventBridge in ACM](example-actions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
