---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/configuring-stack-policies.html
---

# Configuring stack policies
<a name="configuring-stack-policies"></a>

When you configure a stack policy, the `Effect`, `Action`, `Principal`, and `Resource` elements are required. You can optionally define a `Condition` element too.

When you create a stack policy, by default, it prevents updates for all resources in the stack. You customize the stack policy to define which actions are explicitly allowed. If you want to invert the policy, you can define an `Allow` statement that permits all actions and then specify explicit `Deny` statements that prevent actions on only specific resources. For reference, see this [example stack policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#stack-policy-intro-example) in the CloudFormation documentation.

For more information about using these elements to create custom stack policies and more example policies, see [Defining a stack policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#stack-policy-reference) and [More example stack policies](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#stack-policy-samples) in the CloudFormation documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
