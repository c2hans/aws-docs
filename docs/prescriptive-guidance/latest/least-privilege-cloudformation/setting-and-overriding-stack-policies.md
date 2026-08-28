---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/setting-and-overriding-stack-policies.html
---

# Setting and overriding stack policies
<a name="setting-and-overriding-stack-policies"></a>

After you create a stack policy, you associate it to a stack. If you are assigning the stack policy to an existing stack, you must use the AWS Command Line Interface (AWS CLI). However, if you are assigning the policy at the time of stack creation, you can use either the CloudFormation console or the AWS CLI. For instructions, see [Setting a stack policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#protect-stack-resources-protecting) in the CloudFormation documentation.

When you do want to allow users to update or delete the resources in the stack, you need to temporarily override the stack policy. This override allows you to perform otherwise denied actions on the protected resources in that stack. For instructions, see [Updating protected resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#protect-stack-resources-protecting) in the CloudFormation documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
