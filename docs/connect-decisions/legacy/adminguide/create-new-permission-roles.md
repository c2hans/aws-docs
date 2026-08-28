---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/create-new-permission-roles.html
---

# Creating custom user permission roles
<a name="create-new-permission-roles"></a>

In addition to default user permission roles, you can create custom user permission roles to include multiple permission roles and add specific locations and products. Follow these steps to create new permission roles.

1. On the AWS Supply Chain dashboard, from the left navigation pane, choose the **Settings** icon. Choose **Permissions**, and then choose **Permission Roles**.

   The **Permission Roles** page appears.

1. Choose **Create New Role**.

1. On the **Manage Permission Role** page, under **Role Name**, enter a name.

1. Move the slider to select the user permission role.
   + **Manage** – Assigning users with manage permission can add, edit, and manage information.
   + **View** – Assigning users with view permission can only view the current information.

1.
**Note**
 You can only choose the products and locations under **Location Access** and **Product Access** if your instance is connected to a data source. For example, you can create a custom Admin user just to manage avocados in the Seattle location, or an Insight user just to manage the insights for avocados in the Seattle location.

   Under **Location Access**, search for the Regions as you type in the search bar and select the Regions.

1. Under **Product Access**, search for the products as you type in the search bar and select the products.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
