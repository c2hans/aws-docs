---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/monitoring-overview.html
---

# Monitoring AWS Verified Access
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Verified Access. AWS provides the following monitoring tools to watch Verified Access, report when something is wrong, and take automatic actions when appropriate:
+ **Access logs** – Capture detailed information about requests to access applications. For more information, see [Verified Access logs](access-logs.md).
+ **AWS CloudTrail** – Captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Log Verified Access API calls using AWS CloudTrail](logging-using-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
