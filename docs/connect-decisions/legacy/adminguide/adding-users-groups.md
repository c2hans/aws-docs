---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/adminguide/adding-users-groups.html
---

# Managing user permission roles
<a name="adding-users-groups"></a>

As an AWS Supply Chain administrator, you can either use the default user permission roles or create custom permission roles. AWS Supply Chain has the following default user permission roles:
+ **Administrator** – Access to create, view, and manage all data and user permissions.
+ **Data Analyst** – Access to create, view, and manage all data connections.
+ **Inventory Manager** – Access to create, view, and manage Insights.
+ **Demand Planner** – Access to create, view and manage forecasts, overrides, and publish demand plans.
+ **Partner Data Manager** – Access to manage and view partners, manage and view data requests, and view sustainability data.
+ **Supply Planner** – Access to manage and view supply plans.

**Note**
As an AWS Supply Chain administrator, before you add users, note the following:
Each default user permission role is defined with a set of permissions. You can add users to default user permission roles or create custom permission roles.
A user can only be assigned to one user permission role.
You cannot edit or delete default user permission roles.
When you edit a custom permission role you created, the permissions for all the users under the custom permission role are updated.
When you delete a custom permission role you created, all the users under the custom permission role will lose access to AWS Supply Chain.
Adding groups is not supported in AWS Supply Chain.

**Topics**
+ [Adding users](adding-new-users.md)
+ [Updating user permissions](permission-roles.md)
+ [Deleting users](deleting-users.md)
+ [Creating custom user permission roles](create-new-permission-roles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
