---
source_url: https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-cloudwatch.html
---

# Monitoring Oracle Database@AWS with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor Oracle Database@AWS using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

The Oracle Database@AWS service reports metrics to CloudWatch in the `AWS/ODB` namespace. This namespace includes metrics for all Oracle Database@AWS deployment types, including Oracle Exadata Database Service on Dedicated Infrastructure, Autonomous Database Serverless, and Oracle Exadata Database Service on Exascale Infrastructure.

For a complete list of CloudWatch metrics, dimensions, and monitoring details for Oracle Database@AWS, see [Monitor with Amazon CloudWatch](https://docs.oracle.com/en-us/iaas/Content/database-at-aws-exadata-awsmn/awsmn-monitor-cloudwatch.html) in the Oracle Cloud Infrastructure documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database at AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
