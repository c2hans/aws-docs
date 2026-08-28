---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/setting_custom_roles.html
---

# Creating and assigning custom user roles to access Amazon Q in AWS Supply Chain
<a name="setting_custom_roles"></a>

To create and assign custom user roles in AWS Supply Chain, perform the following procedure:

**Note**
If you are an AWS Supply Chain administrator or have a custom user role with administrator privileges, you can access Amazon Q across all datasets without any additional permission requirements after Amazon Q is enabled on your account. This section is only applicable if you want to grant Amazon Q access permissions to non-administrator users.

1. In the left navigation pane on the Supply Chain dashboard, choose the **Settings** icon.

1. Under **Users and Permissions**, choose **Permission Roles**.

   The **Permission Roles** page appears.

1. Choose **Create New Role**.

   The **Manage Permission Role** page appears.

1. Under **Role Name**, enter a name for the role.

1. Choose the module or administrator access for the permission role you are creating.
**Note**
You must choose an administrator role or AWS Supply Chain module to enable Amazon Q in AWS Supply Chain. Amazon Q in AWS Supply Chain cannot be enabled independently.

1. Slide the **Amazon Q in AWS Supply Chain** button to create a user role to view and interact with **Amazon Q** in the **AWS Supply Chain** web application.

1. Under **Additional Data Permissions**, view the datasets that are automatically listed as per the user role you selected.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
