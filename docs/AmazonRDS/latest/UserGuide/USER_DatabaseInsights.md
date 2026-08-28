---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html
---

# Monitoring Amazon RDS databases with CloudWatch Database Insights
<a name="USER_DatabaseInsights"></a>

Monitor the database load (DB Load) for your fleet of Amazon RDS DB instances with Database Insights. DB Load measures the level of session activity in your database. You can use Database Insights to analyze and troubleshoot the performance of your Amazon RDS databases at scale.

With Database Insights, you can visualize the DB Load on your fleet of databases and filter the load by waits, SQL statements, hosts, or users.

By default, RDS enables the Standard mode of Database Insights for your Amazon RDS databases.

For information about using Database Insights in the Amazon CloudWatch console, see [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) in the *Amazon CloudWatch User Guide*.

## Pricing
<a name="USER_Database-Insights-pricing"></a>

For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Topics**
+ [Pricing](#USER_Database-Insights-pricing)
+ [Amazon RDS DB engine, Region, and instance class support for Database Insights](USER_DatabaseInsights.Engines.md)
+ [Turning on the Advanced mode of Database Insights for Amazon RDS](USER_DatabaseInsights.TurningOnAdvanced.md)
+ [Turning on the Standard mode of Database Insights for Amazon RDS](USER_DatabaseInsights.TurningOnStandard.md)
+ [Configuring your database to monitor slow SQL queries with Database Insights for Amazon RDS](USER_DatabaseInsights.SlowSQL.md)
+ [Considerations for Database Insights for Amazon RDS](USER_DatabaseInsights.Considerations.md)
+ [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon RDS](USER_PerfInsights.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
