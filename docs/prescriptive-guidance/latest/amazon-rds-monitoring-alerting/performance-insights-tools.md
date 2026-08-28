---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/performance-insights-tools.html
---

# Amazon RDS Performance Insights
<a name="performance-insights-tools"></a>

[Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/) is a database performance tuning and monitoring tool that expands Amazon RDS monitoring features. It helps you analyze the performance of your database by visualizing the DB instance load and filtering the load by waits, SQL statements, hosts, or users. The tool combines multiple metrics into a single interactive graph that helps you identify the type of bottleneck your DB instance might have, such as lock waits, high CPU consumption, or I/O latency, and determine which SQL statements are creating the bottleneck. The following screen illustration shows an example visualization.

![Example graph from Amazon RDS Performance Insights](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/ad864f85-a4d5-4098-82f9-f3b13de8675e.png)

You have to [enable Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html) during the DB instance creation process to collect metrics for the Amazon RDS DB instances in your account. The free tier includes seven days of performance data history and one million API requests per month. Optionally, you can purchase longer retention periods. For complete pricing information, see [Performance Insights Pricing](https://aws.amazon.com/rds/performance-insights/pricing/).

For information about how you can use Performance Insights to monitor your DB instances, see the [DB instance monitoring](database-instance-monitoring.md) section later in this guide.

Performance Insights automatically [publishes metrics to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.html). In addition to using the Performance Insights tool itself, you can take advantage of the additional features that CloudWatch provides. You can examine the Performance Insights metrics by using the CloudWatch console, the AWS CLI, or the CloudWatch API. You can also add CloudWatch alarms, as with any other metrics. For example, you might want to trigger an SMS notification to DBAs or take a corrective action if the `DBLoad` metric breaches the threshold value you set. You can also add the Performance Insights metrics to your existing CloudWatch dashboards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
