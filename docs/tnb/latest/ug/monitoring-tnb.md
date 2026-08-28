---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/monitoring-tnb.html
---

# Monitoring AWS TNB
<a name="monitoring-tnb"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS TNB and your other AWS solutions. AWS provides AWS CloudTrail to watch AWS TNB, report when something is wrong, and take automatic actions when appropriate.

Use CloudTrail to capture detailed information about the calls made to AWS APIs. You can store these calls as log files in Amazon S3. You can use these CloudTrail logs to determine such information as which call was made, the source IP address where the call came from, who made the call, and when the call was made.

The CloudTrail logs contain information about the calls to API actions for AWS TNB. They also contain information for calls to API actions from services such as Amazon EC2 and Amazon EBS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
