---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html
---

# Delegated administrator for AWS Organizations
<a name="orgs_delegate_policies"></a>

We recommend that you use the AWS Organizations management account and its users and roles only for tasks that must be performed by that account. We also recommend that you store your AWS resources in other member accounts in the organization and keep them out of the management account. This is because security features like Organizations service control policies (SCPs) do not restrict users or roles in the management account.

From the organization's management account, you can delegate policy management for Organizations to specified member accounts to perform policy actions that are by default available only to the management account.

For example resource-based delegation policies, see [Resource-based policy examples for AWS Organizations](security_iam_resource-based-policy-examples.md).

**Topics**
+ [Create a resource-based delegation policy](orgs-policy-delegate.md)
+ [Update a resource-based delegation policy](orgs-policy-delegate-update.md)
+ [View a resource-based delegation policy](view-delegated-resource-based-policy.md)
+ [Delete a resource-based delegation policy](delete-delegated-resource-based-policy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
