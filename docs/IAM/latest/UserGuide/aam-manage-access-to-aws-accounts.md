---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/aam-manage-access-to-aws-accounts.html
---

# Manage access to AWS accounts
<a name="aam-manage-access-to-aws-accounts"></a>

Account access manager is integrated with IAM Identity Center and AWS Organizations to centrally manage the assignment of existing IAM roles across multiple AWS accounts without configuring each of your accounts individually. With account access manager, you assign existing IAM roles in your AWS accounts to IAM Identity Center users and groups to control their access to specific AWS accounts.

With account access manager, your teams can create their own custom [IAM roles](id_roles.md) in their AWS accounts, and you as administrator use account access manager to centrally manage assignments of IAM Identity Center users and groups to these IAM roles.

**Note**
Within the context of account access manager, the terms *users* and *groups* exclusively refer to workforce *users* and *groups* in IAM Identity Center.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
