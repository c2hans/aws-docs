---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies.html
---

# Verified Access policies
<a name="auth-policies"></a>

AWS Verified Access policies allow you to define rules for accessing your applications hosted in AWS. They are written in Cedar, an AWS policy language. Using Cedar, you can create policies that are evaluated against the trust data sent from the identity or device-based trust providers that you configure to use with Verified Access.

For more detailed information about the Cedar policy language, see the [Cedar Reference Guide](https://docs.cedarpolicy.com/).

When you [create a Verified Access group](create-verified-access-group.md) or [create a Verified Access endpoint](verified-access-endpoints.md), you have the option to define the Verified Access policy. You can create a group or endpoint without defining the Verified Access policy, but all access requests will be blocked until you define a policy. Alternatively, you can add or change a policy on an existing Verified Access group or endpoint after it has been created.

**Topics**
+ [Policy statements](auth-policies-policy-statement-struct.md)
+ [Built-in operators](built-in-policy-operators.md)
+ [Policy evaluation](auth-policies-policy-eval.md)
+ [Policy logic short circuit](auth-policies-policy-eval-short-circ.md)
+ [Example policies](trust-data-iam-add-pol.md)
+ [Policy assistant](policy-assistant.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
