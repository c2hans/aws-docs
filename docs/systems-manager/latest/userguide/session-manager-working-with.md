---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Working with Session Manager
<a name="session-manager-working-with"></a>

You can use the AWS Systems Manager console, the Amazon Elastic Compute Cloud (Amazon EC2) console, or the AWS Command Line Interface (AWS CLI) to start sessions that connect you to the managed nodes your system administrator has granted you access to using AWS Identity and Access Management (IAM) policies. Depending on your permissions, you can also view information about sessions, resume inactive sessions that haven't timed out, and end sessions. After a session is established, it is not affected by IAM role session duration. For information about limiting session duration with Session Manager, see [Specify an idle session timeout value](session-preferences-timeout.md) and [Specify maximum session duration](session-preferences-max-timeout.md).

For more information about sessions, see [What is a session?](session-manager.md#what-is-a-session)

**Topics**
+ [Install the Session Manager plugin for the AWS CLI](session-manager-working-with-install-plugin.md)
+ [Start a session](session-manager-working-with-sessions-start.md)
+ [End a session](session-manager-working-with-sessions-end.md)
+ [View session history](session-manager-working-with-view-history.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
