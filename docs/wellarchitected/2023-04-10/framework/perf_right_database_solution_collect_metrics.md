---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_right_database_solution_collect_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP03 Collect and record database performance metrics
<a name="perf_right_database_solution_collect_metrics"></a>

 To understand how your data management systems are performing, it is important to track relevant metrics. These metrics will help you to optimize your data management resources, to ensure that your workload requirements are met, and that you have a clear overview on how the workload performs. Use tools, libraries, and systems that record performance measurements related to database performance.

 There are metrics that are related to the system on which the database is being hosted (for example, CPU, storage, memory, IOPS), and there are metrics for accessing the data itself (for example, transactions per second, queries rates, response times, errors). These metrics should be readily accessible for any support or operational staff, and have sufficient historical record to be able to identify trends, anomalies, and bottlenecks.

 **Desired outcome:** To monitor the performance of your database workloads, you must record multiple performance metrics over a period of time. This allows you to detect anomalies as well as measure performance against business metrics to ensure you are meeting your workload needs.

 **Common anti-patterns:**
+  You only use manual log file searching for metrics.
+  You only publish metrics to internal tools used by your team and don’t have a comprehensive picture of your workload.
+  You only use the default metrics recorded by your selected monitoring software.
+  You only review metrics when there is an issue.
+  You only monitor system level metrics, not capturing data access or usage metrics.

 **Benefits of establishing this best practice:** Establishing a performance baseline helps in understanding normal behavior and requirements of workloads. Abnormal patterns can be identified and debugged faster improving performance and reliability of the database. Database capacity can be configured to ensure optimal cost without compromising performance.

 **Level of risk exposed if this best practice is not established:** High
+  Inability to differentiate out of normal vs. normal performance level will create difficulties in issue identification, and decision making.
+  Potential cost savings may not be identified.
+  Growth patterns will not be identified which might result in reliability or performance degradation.

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify, collect, aggregate, and correlate database-related metrics. Metrics should include both the underlying system that is supporting the database and the database metrics. The underlying system metrics might include CPU utilization, memory, available disk storage, disk I/O, and network inbound and outbound metrics while the database metrics might include transactions per second, top queries, average queries rates, response times, index usage, table locks, query timeouts, and number of connections open. This data is crucial to understand how the workload is performing and how the database solution is used. Use these metrics as part of a data-driven approach to tune and optimize your workload's resources.

 **Implementation steps:**

1.  Which database metrics are important to track?

   1.  [Monitoring metrics for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)

   1.  [Monitoring with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)

   1.  [Enhanced monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.overview.html)

   1.  [DynamoDB metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html)

   1.  [Monitoring DynamoDB DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Monitoring.html)

   1.  [Monitoring MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-cloudwatch.html)

   1.  [Monitoring Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics.html)

   1.  [Timeseries metrics and dimensions](https://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)

   1.  [Cluster level metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Monitoring.Metrics.html)

   1.  [Monitoring Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/monitoring.html)

   1.  [Monitoring Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/monitoring.html)

1.  Would the database monitoring benefit from a machine learning solution that detects operational anomalies performance issues?

   1.  [Amazon DevOps Guru for Amazon RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.how-it-works.html) provides visibility into performance issues and makes recommendations for corrective actions.

1.  Do you need application level details about SQL usage?

   1.  [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html#api-segmentdocuments-sql) can be instrumented into the application to gain insights and encapsulate all the data points for single query.

1.  Do you currently have an approved logging and monitoring solution?

   1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) can collect metrics across the resources in your architecture. You can also collect and publish custom metrics to surface business or derived metrics. Use CloudWatch or third-party solutions to set alarms that indicate when thresholds are breached.

1.  You identified and configured your data retention policies to match my security and operational goals?

   1.  [Default data retention for CloudWatch metrics](https://aws.amazon.com/cloudwatch/faqs/#AWS_resource_.26_custom_metrics_monitoring)

   1.  [Default data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management)

 **Level of effort for the implementation plan: **There is a *medium* level of effort to identify, track, collect, aggregate, and correlate metrics from all database resources.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/)
+ [ Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
+ [ Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
+  [Amazon DynamoDB Accelerator ](https://aws.amazon.com/dynamodb/dax/)
+ [Amazon DynamoDB best practices ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
+ [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
+ [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
+ [Cloud Databases with AWS](https://aws.amazon.com/products/databases/)
+  [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/)

 **Related videos:**
+ [AWS purpose-built databases (DAT209-L) ](https://www.youtube.com/watch?v=q81TVuV5u28)
+  [Amazon Aurora storage demystified: How it all works (DAT309-R) ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+  [Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1) ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)
+  [AWS Dataset Ingestion Metrics Collection Framework](https://github.com/awslabs/aws-dataset-ingestion-metrics-collection-framework)
+  [Amazon RDS Monitoring Workshop](https://www.workshops.aws/?tag=Enhanced%20Monitoring)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
