---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/known-issues.html
---

# Known issues
<a name="known-issues"></a>

The Amazon DCV Access Console has the following known issues.

## Cannot delete users from UI
<a name="cannot-delete-users"></a>

To prevent users from logging into the UI, users can be disabled. To disable users, import the users with the `disabled` column set to true for the user.

## Cannot manage Amazon DCV host servers
<a name="cannot-manage-host-servers"></a>

While the Access Console allows administrators to view the underlying hosts they have the Amazon DCV sessions installed on. However, it does not allow administrators to manage those resources directly. If you wish to start, terminate, or reboot your hosts, you must do so from your cloud or on-premise environment directly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
