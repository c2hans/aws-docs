---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-space-roles.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Granting space roles for a team
<a name="managing-teams-space-roles"></a>

Teams are a way to group users so that you can grant and manage team access to projects in CodeCatalyst. As an example, you can use teams to quickly manage roles and permissions for users by giving a team the ability to manage a space for users.

A team can have role permissions, such as **Power user**, in a space. You can change the space role for a team, but note that all members of the team will inherit those permissions.

You must have the **Space administrator** role to manage teams.

**Changing the space role for a team**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space. Choose **Settings**, and then choose **Teams**.

1. In **Actions**, choose **Change space role**. You can change the space role to one of the following. This changes the role for all members of the team.
   + **Space administrator** - For details, see [Space administrator role](ipa-role-types.md#ipa-role-space-admin).
   + **Limited access** - For details, see [Limited access role](ipa-role-types.md#ipa-role-limited-access).
   + **Power user** - For details, see [Power user role](ipa-role-types.md#ipa-role-power-user).

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
