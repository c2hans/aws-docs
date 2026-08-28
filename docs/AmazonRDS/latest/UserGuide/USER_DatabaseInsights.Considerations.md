---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Considerations.html
---

# Considerations for Database Insights for Amazon RDS
<a name="USER_DatabaseInsights.Considerations"></a>

Following are considerations for Database Insights for Amazon RDS.
+ You can't manage Database Insights for a DB instance in a Multi-AZ DB cluster.
+ To enable the Advanced mode of Database Insights, you must enable Performance Insights and set the Performance Insights retention period to at least 465 days (15 months). There is no additional cost to set the Performance Insights retention period to 15 months besides the cost of Database Insights. For information about pricing for Database Insights, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).
+ To enable Database Insights, each DB instance in a Multi-AZ DB cluster must have the same Performance Insights and Enhanced Monitoring settings.
+ Modifying a DB instance to enable either mode of Database Insights doesn't cause downtime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
