---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering-scope.html
---

# Amazon SNS subscription filter policy scope
<a name="sns-message-filtering-scope"></a>

The `FilterPolicyScope` subscription attribute allows you define the filtering scope by setting one of the following values:
+ `MessageAttributes` – Applies the filter policy to message attributes (default setting).
+ `MessageBody` – Applies the filter policy to the message body.

**Note**
If no filter policy scope is defined for an existing filter policy, the scope defaults to `MessageAttributes`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
