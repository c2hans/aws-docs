---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-4/ug/permission-profiles.html
---

# Permission policy
<a name="permission-profiles"></a>

Research and Engineering Studio (RES) allows an administrative user to create custom permission profiles that grant selected users additional permissions to manage the project that they are part of. Each project comes with two [default permission profiles](permission-matrix.md)- "Project Member" and "Project Owner" that can be customized after deployment.

Currently, administrators can grant two collections of permissions using a permission profile:

1. Project management permissions which consist of "Update project membership" that allows a designated user to add other users and groups to, or remove them from, a project, and "Update project status" that allows a designated user to enable or disable a project.

1. VDI session management permissions which consist of "Create Session" that allows a designated user to create a VDI session within their project, and "Create/Terminate another user's session" that allows a designated user to create or terminate the sessions of other users within a project.

In this way, administrators can delegate project-based permissions to non-administrators in their environment.

**Topics**
+ [Project management permissions](permission-profiles-permission-project-management.md)
+ [VDI session management permissions](permission-profiles-permission-vdi-sessions.md)
+ [Managing permission profiles](permission-profiles-permission-management.md)
+ [Default permissions profiles](permission-matrix.md)
+ [Environment boundaries](permission-profiles-environment-boundaries.md)
+ [Desktop sharing profiles](permission-profiles-desktop-sharing-profiles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
