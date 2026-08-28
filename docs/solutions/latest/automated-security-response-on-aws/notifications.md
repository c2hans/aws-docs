---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/notifications.html
---

# Notifications
<a name="notifications"></a>

This solution uses an Amazon Simple Notification Service (Amazon SNS) topic to publish remediation results. You can use subscriptions to this topic to extend the capabilities of the solution. For example, you can send email notifications and update trouble tickets.
+  **SO0111-ASR\_Topic** – Used to send general informational and error messages related to executed remediations.
+  **SO0111-ASR\_Alarm\_Topic** – Used to notify when one of the solution’s alarms is triggered, indicating that the solution is not functioning as expected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
