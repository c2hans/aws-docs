---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-for-apps-only.html
---

# Using IAM Identity Center for user access to applications only
<a name="identity-center-for-apps-only"></a>

 You can use IAM Identity Center for user access to applications such as Kiro, AWS accounts, or both. You can connect your existing identity provider and synchronize users and groups from your directory, or [create and manage users directly in IAM Identity Center](quick-start-default-idc.md). For information about how to connect your existing identity provider to IAM Identity Center, see the [IAM Identity Center identity source tutorials](tutorials.md).

**Already using IAM for access to AWS accounts?**

You don’t need to make any changes to your current AWS account workflows to use IAM Identity Center for access to AWS managed applications. If you’re using [federation with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam) for AWS account access, your users can continue to access AWS accounts in the same way they always have, and you can continue to use your existing workflows to manage that access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
