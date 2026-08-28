---
source_url: https://docs.aws.amazon.com/ram/latest/userguide/security-monitoring.html
---

# Logging and monitoring in AWS RAM
<a name="security-monitoring"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS RAM and your AWS solutions. You should collect monitoring data from all parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs. AWS provides several tools for monitoring your AWS RAM resources and responding to potential incidents:

**Amazon EventBridge**
Delivers a near-real-time stream of system events that describe changes in AWS resources. EventBridge enables automated event-driven computing, as you can write rules that watch for certain events and trigger automated actions in other AWS services when these events happen. For more information, see [Monitoring AWS RAM using EventBridge](using-eventbridge.md).

**AWS CloudTrail**
Captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Logging AWS RAM API calls with AWS CloudTrail](cloudtrail-logging.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
