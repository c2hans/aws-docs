---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/eventbridge-integration.html
---

# Connect application components with Amazon EventBridge
<a name="eventbridge-integration"></a>

 You can integrate IAM Identity Center with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to raise events that initiate administrative notifications or invoke automated workflows in response to specific IAM Identity Center actions recorded in CloudTrail events.

 For example, you might configure [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to detect when a user deletes an application or when IAM Identity Center creates a new group. Depending on your use case, you can route these events to an Amazon SNS topic to notify administrators or invoke additional automation using AWS Lambda, [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html), or other [EventBridge-supported services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-target).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
