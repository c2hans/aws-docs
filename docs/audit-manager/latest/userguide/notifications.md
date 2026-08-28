---
source_url: https://docs.aws.amazon.com/audit-manager/latest/userguide/notifications.html
---

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

# Notifications in AWS Audit Manager
<a name="notifications"></a>

AWS Audit Manager can notify you about user actions through [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/).

Audit Manager sends notifications when one of the following events occurs:
+ An audit owner delegates a control set for review.
+ A delegate submits a reviewed control set back to the audit owner.
+ An audit owner completes the review of a control set.

## Additional resources
<a name="notifications-missing-troubleshooting"></a>
+ To configure your notifications in Audit Manager, see [Configuring your Audit Manager notifications](settings-notifications.md).
+ To find answers to common questions and issues, see [Troubleshooting notification issues](notification-issues.md) in the *Troubleshooting* section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
