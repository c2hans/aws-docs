---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/automate-sync-configuration-configurable-ADsync.html
---

# Automate your sync configuration for configurable AD sync
<a name="automate-sync-configuration-configurable-ADsync"></a>

To ensure that your automated workflow works as expected with configurable AD sync, we recommend that you perform the following steps to automate your sync configuration.

**To automate your sync configuration for configurable AD sync**

1. In Active Directory, create a *parent sync group* to contain all users and groups that you want to sync into IAM Identity Center. For example, you can name the group *IAMIdentityCenterAllUsersAndGroups*.

1. In IAM Identity Center, add the parent sync group to your configurable sync list. IAM Identity Center will synchronize all users, groups, sub-groups, and members of all groups contained within the parent sync group.

1. Use the Active Directory user and group management API actions provided by Microsoft to add or remove users and groups from the parent sync group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
