---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring.html
---

# Monitoring Amazon Verified Permissions API calls
<a name="monitoring"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Verified Permissions and your other AWS solutions. AWS provides the following tools to monitor Verified Permissions, report when something is wrong, and take automatic actions when appropriate:
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

For more information about monitoring Verified Permissions with CloudTrail, see [Logging Amazon Verified Permissions API calls using AWS CloudTrail](monitoring-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
