---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-recipients.html
---

# Recipients
<a name="notification-center-recipients"></a>

Recipients determine who receives in-app and email notifications. For Slack, the webhook URL is the destination — the recipients list is not used for routing.

Recipients are resolved at delivery time. You can specify users, groups, or project roles:

| Recipient type | Description |
| --- | --- |
| User | A specific portal user, identified by their account ID. |
| Group | A user group. Members are resolved dynamically at send time. |
| Role | A project role (`OWNER`, `MANAGER`, or `VIEWER`). All users with that role in the asset’s project receive the notification. |

Recipients are validated as resource members at rule creation time and re-checked at delivery time. Non-members are silently skipped.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
