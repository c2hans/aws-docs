---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/standard-order-eventbridge-requirements.html
---

# Amazon EventBridge access requirements
<a name="standard-order-eventbridge-requirements"></a>

Use the following Amazon EventBridge access requirements to create and delete Shopify integrations with Connect Customer Customer Profiles:
+ `events:ListTargetsByRule`
+ `events:PutRule`
+ `events:PutTargets`
+ `events:DeleteRule`
+ `events:RemoveTargets`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
