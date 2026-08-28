---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.em.html
---

# Monitoring Aurora PostgreSQL Limitless Database with Enhanced Monitoring
<a name="limitless-monitoring.em"></a>

Enhanced Monitoring is required as part of enabling Aurora PostgreSQL Limitless Database. You can use it to monitor the operating system of your Limitless Database DB instances in real time.

Aurora publishes Enhanced Monitoring metrics in CloudWatch Logs. Some of the key metrics available include database connections, storage usage, and query latency. These can help identify performance bottlenecks.

For more information on Enhanced Monitoring metrics, see [OS metrics for Aurora](USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
