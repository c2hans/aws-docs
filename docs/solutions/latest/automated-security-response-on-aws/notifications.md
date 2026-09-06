---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/notifications.html
---

# Notifications
<a name="notifications"></a>

This solution uses an Amazon Simple Notification Service (Amazon SNS) topic to publish remediation results. You can use subscriptions to this topic to extend the capabilities of the solution. For example, you can send email notifications and update trouble tickets.
+  **SO0111-ASR\_Topic** – Used to send general informational and error messages related to executed remediations.
+  **SO0111-ASR\_Alarm\_Topic** – Used to notify when one of the solution’s alarms is triggered, indicating that the solution is not functioning as expected.
