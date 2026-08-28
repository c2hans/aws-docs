---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.html
---

# Monitoring Aurora PostgreSQL Limitless Database with CloudWatch Database Insights
<a name="limitless-monitoring.cwdbi"></a>

The Standard mode of Database Insights is required as part of enabling Aurora PostgreSQL Limitless Database. You can use it to monitor the database load (DB Load) of your Limitless Database DB instances in real time. DB Load measures the level of session activity in a database. You can use Database Insights to analyze and troubleshoot the performance of your Aurora PostgreSQL Limitless Database DB instances at scale.

For more information about CloudWatch Database Insights, see the following.
+ [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md)
+ [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) in the *Amazon CloudWatch User Guide*
+ [Get started with CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Get-Started.html) in the *Amazon CloudWatch User Guide*
+ [Configuring your database to monitor slow SQL queries with Database Insights for Amazon Aurora](USER_DatabaseInsights.SlowSQL.md)

For information about turning on the Advanced mode or Standard mode of Database Insights, see the following topics.

**Topics**
+ [Turning on the Advanced mode of Database Insights for Aurora PostgreSQL Limitless Database](limitless-monitoring.cwdbi.advanced.md)
+ [Turning on the Standard mode of Database Insights for Aurora PostgreSQL Limitless Database](limitless-monitoring.cwdbi.standard.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
