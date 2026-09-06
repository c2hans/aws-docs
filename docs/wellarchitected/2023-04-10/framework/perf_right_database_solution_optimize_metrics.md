---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_right_database_solution_optimize_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP05 Optimize data storage based on access patterns and metrics
<a name="perf_right_database_solution_optimize_metrics"></a>

 Use performance characteristics and access patterns that optimize how data is stored or queried to achieve the best possible performance. Measure how optimizations such as indexing, key distribution, data warehouse design, or caching strategies impact system performance or overall efficiency.

 **Common anti-patterns:**
+  You only use manual log file searching for metrics.
+  You only publish metrics to internal tools.

 **Benefits of establishing this best practice:** In order to ensure you are meeting the metrics required for the workload, you must monitor database performance metrics related to both reads and writes. You can use this data to add new optimizations for both reads and writes to the data storage layer.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimize data storage based on metrics and patterns: Use reported metrics to identify any underperforming areas in your workload and optimize your database components. Each database system has different performance related characteristics to evaluate, such as how data is indexed, cached, or distributed among multiple systems. Measure the impact of your optimizations.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Database Caching](https://aws.amazon.com/caching/database-caching/)
+  [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
+  [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
+  [Amazon DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/)
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
+  [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
+  [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
+  [Cloud Databases with AWS](https://aws.amazon.com/products/databases/)
+  [Analyzing performance anomalies with DevOps Guru for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/devops-guru-for-rds.html)
+  [Read/Write Capacity Mode for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html)

 **Related videos:**
+  [AWS purpose-built databases (DAT209-L)](https://www.youtube.com/watch?v=q81TVuV5u28)
+  [Amazon Aurora storage demystified: How it all works (DAT309-R)](https://www.youtube.com/watch?v=uaQEGLKtw54)
+  [Amazon DynamoDB deep dive: Advanced design patterns (DAT403-R1)](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Hands-on Labs for Amazon DynamoDB](https://amazon-dynamodb-labs.workshop.aws/hands-on-labs.html)
