---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/identities.html
---

# Set up your workforce in IAM Identity Center
<a name="identities"></a>

IAM Identity Center is the AWS solution for connecting your workforce users to AWS managed applications such as Kiro and Amazon Quick, and other AWS resources. You can connect your existing identity provider and synchronize users and groups from your directory, or create and manage your users directly in IAM Identity Center.

**Already using IAM for access to AWS accounts?**

You don’t need to make any changes to your current AWS account workflows to use IAM Identity Center for access to AWS managed applications. If you’re using [federation with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam) for AWS account access, your users can continue to access AWS accounts in the same way they always have, and you can continue to use your existing workflows to manage that access.

Choose the approach that best fits your organization's identity management strategy and existing infrastructure.

**Topics**
+ [Users, groups, and provisioning in IAM Identity Center](users-groups-provisioning.md)
+ [Manage your identity source](manage-your-identity-source.md)
+ [Manage users in the Identity Center directory](manage-your-identity-source-sso.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
