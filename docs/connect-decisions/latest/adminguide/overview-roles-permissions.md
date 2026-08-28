---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/adminguide/overview-roles-permissions.html
---

# Overview of roles and permissions
<a name="overview-roles-permissions"></a>

As an Amazon Connect Decisions administrator, you can either use the default user permission roles or create custom permission roles. Amazon Connect Decisions has the following default user permission roles:
+ **Administrator** – Access to create, view, and manage all data and user permissions.
![Administrator role permissions](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/overview-roles-permissions-administrator.png)
+ **Manager** – Access to create, view, and manage the following.
![Manager role permissions](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/overview-roles-permissions-manager.png)
+ **Planner** – Access to create, view and manage the following.
![Planner role permissions](http://docs.aws.amazon.com/connect-decisions/latest/adminguide/images/overview-roles-permissions-planner.png)

**Note**
As an Amazon Connect Decisions administrator, before you add users, note the following:
Each default user permission role is defined with a set of permissions. You can add users to default user permission roles or create custom permission roles.
A user can only be assigned to one user permission role.
You cannot edit or delete default user permission roles.
When you edit a custom permission role you created, the permissions for all the users under the custom permission role are updated.
When you delete a custom permission role you created, all the users under the custom permission role will lose access to Amazon Connect Decisions.
Adding groups is not supported in Amazon Connect Decisions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
