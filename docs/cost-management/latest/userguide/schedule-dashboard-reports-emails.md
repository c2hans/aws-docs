---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/schedule-dashboard-reports-emails.html
---

# Understanding scheduled report emails
<a name="schedule-dashboard-reports-emails"></a>

When a scheduled report is generated, recipients receive an email notification containing:
+ A secure, time-limited download link to access the PDF report. The link expires after 15 days.
+ A unique password required to open the PDF file. Each report generation produces a new password.
+ The report name, dashboard name, and generation timestamp.

PDF reports are encrypted and stored in AWS-managed Amazon S3 buckets. The download links use pre-signed URLs that grant time-limited access to the specific PDF file.

**Controlling access to report download links and passwords**
Scheduled reports are delivered through AWS User Notifications, and the notification event that AWS User Notifications creates for each delivery contains the download link and the PDF password. Permissions to read notification events are separate from permissions for AWS Billing and Cost Management and AWS Cost Explorer. For example, a principal with the `notifications:ListNotificationEvents` and `notifications:GetNotificationEvent` permissions can retrieve the link and the password even if it can't otherwise view your cost and usage data, and no AWS permissions are required to open the link.
Grant permissions to read notification events only to principals that you intend to have access to the cost and usage data in your reports. For more information, see [Identity and access management for AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/security-iam.html) in the *AWS User Notifications User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
