---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-security-logging-and-monitoring.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# Logging and Monitoring in AWS Snowball Edge
<a name="snowball-edge-security-logging-and-monitoring"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Snowball Edge and your AWS solutions. You should collect monitoring data so that you can more easily debug a multi-point failure if one occurs. AWS provides several tools for monitoring your AWS Snowball Edge resources and responding to potential incidents:

**AWS CloudTrail Logs**
CloudTrail provides a record of actions taken by a user, role, or an AWS service in the AWS Snowball Edge Job Management API or when using the AWS Console. Using the information collected by CloudTrail, you can determine the API request that was made to AWS Snowball Edge service, the IP address from which the request was made, who made the request, when it was made, and additional details. For more information, see [Logging AWS Snowball Edge API calls with AWS CloudTrail](logging-using-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
