---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies-policy-eval.html
---

# Verified Access policy evaluation
<a name="auth-policies-policy-eval"></a>

A policy document is a set of one or more policy statements (`permit` or `forbid` statements). The policy applies if the conditional clause (the `when` statement) is true. In order for a policy document to allow access, at least one permit policy in the document must apply and no forbid policies can apply. If no permit policies apply and/or one or more forbid policies apply, then the policy document denies access. If you have defined policy documents for both the Verified Access group and the Verified Access endpoint, both documents must allow access. If you have not defined a policy document for the Verified Access endpoint, only the Verified Access group policy needs access.

AWS Verified Access validates the syntax when you create the policy, but it does not validate the data you put in the conditional clause.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
