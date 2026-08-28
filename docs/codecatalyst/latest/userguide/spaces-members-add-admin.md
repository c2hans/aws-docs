---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-add-admin.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Inviting a user directly to a space
<a name="spaces-members-add-admin"></a>

You can invite users directly to your CodeCatalyst space. This is useful when you want to invite that user to help you manage the space by assigning them the **Space administrator** or **Power user** role. Assigning one of those roles to other users can help you distribute the responsibilities of managing the space across more people without having to invite these users to any projects.

**Note**
You must have the **Space administrator** or **Power user** role to invite members.

The **Space administrators** table shows users with the **Space administrator** role. These users are not shown in the **Space members** table because they are automatically (implicitly) assigned to all projects in the space and do not have a role in a project.

Members who accept a project invitation are added to the space by default. The **Project members** table shows all members in the space that have a role in a project.

For more information about how to accept an invitation and sign in for the first time, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md).

**To invite a user to your space**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space.

1. Choose **Settings**, and then choose **Members**.

1. Choose **Invite**.

1. Enter the email of the person you would like to invite to join your space. In **Role**, choose the role you want to assign that user in the space.

1. Choose **Invite**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
