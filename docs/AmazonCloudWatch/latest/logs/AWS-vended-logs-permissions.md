---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions.html
---

# Logging that requires additional permissions [V1]
<a name="AWS-vended-logs-permissions"></a>

Some AWS services use a common infrastructure to send their logs to CloudWatch Logs, Amazon S3, or Firehose. To enable the AWS services listed in the preceding table to send their logs to these destinations, you must be logged in as a user that has certain permissions.

Additionally, permissions must be granted to AWS to enable the logs to be sent. AWS can automatically create those permissions when the logs are set up, or you can create them yourself first before you set up the logging. For cross-account delivery, you must manually create the permission policies yourself.

If you choose to have AWS automatically set up the necessary permissions and resource policies when you or someone in your organization first sets up the sending of logs, then the user who is setting up the sending of logs must have certain permissions, as explained later in this section. Alternatively, you can create the resource policies yourself, and then the users who set up the sending of logs do not need as many permissions.

The following topics provide more details for each of these destinations.

**Topics**
+ [Logs sent to CloudWatch Logs](AWS-logs-infrastructure-CWL.md)
+ [Logs sent to Amazon S3](AWS-logs-infrastructure-S3.md)
+ [Logs sent to Firehose](AWS-logs-infrastructure-Firehose.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
