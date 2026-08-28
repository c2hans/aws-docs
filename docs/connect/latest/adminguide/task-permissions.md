---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/task-permissions.html
---

# Block agents from creating tasks in the Connect Customer Contact Control Panel (CCP)
<a name="task-permissions"></a>

To block agents from being able to create tasks, assign the **Contact Control Panel (CCP)**, **Restrict task creation** permission. By default this permissions is unchecked, which means all agents can create tasks.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

By default, the **Admin** security profile already has permissions to perform all tasks activities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
