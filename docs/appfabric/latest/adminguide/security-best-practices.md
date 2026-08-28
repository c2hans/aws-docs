---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/security-best-practices.html
---

# Security best practices for AWS AppFabric
<a name="security-best-practices"></a>

AWS AppFabric provides several security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

## Monitor for application without admin access
<a name="monitor-application-without-admin-access"></a>

With the read-only AWS Identity and Access Management (IAM) permission, anyone can integrate AppFabric with Amazon Quick and other security information and event management (SIEM) tools, such as Splunk. To monitor application security, data is delivered to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose delivery stream.

## Monitor for AppFabric events
<a name="monitor-appfabric-events"></a>

You can monitor AppFabric using Amazon CloudWatch metrics. CloudWatch collects data from AppFabric every minute and processes it into metrics. You can set alarms that set off notifications when metrics match specified thresholds. For more information, see [Monitoring AWS AppFabric with Amazon CloudWatch](monitoring-cloudwatch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
