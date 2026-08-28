---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.Monitoring.html
---

# Monitoring Oracle GoldenGate
<a name="Appendix.OracleGoldenGate.Monitoring"></a>

When you use Oracle GoldenGate for replication, make sure that the Oracle GoldenGate process is up and running and the source and target databases are synchronized. You can use the following monitoring tools:
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a monitoring service that is used in this pattern to monitor GoldenGate error logs.
+ [Amazon SNS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html) is a message notification service that is used in this pattern to send email notifications.

For detailed instructions, see [Monitor Oracle GoldenGate logs by using Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
