---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-data-collected-database-analytics.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Data collected by the Agentless Collector database and analytics data collection module
<a name="agentless-collector-data-collected-database-analytics"></a>

The Application Discovery Service Agentless Collector (Agentless Collector) database and analytics data collection module collects the following metrics from your data environment. For information about setting up data collection, see [Using the database and analytics data collection module](agentless-collector-gs-database-analytics-collection.md).

When you use the database and analytics data collection module to collect **Metadata and database capacity**, it captures the following metrics.
+ Available memory on your OS servers
+ Available storage on your OS servers
+ Database version and edition
+ Number of CPUs on your OS servers
+ Number of schemas
+ Number of stored procedures
+ Number of tables
+ Number of triggers
+ Number of views
+ Schema structure

After you launch the schema analysis in the AWS DMS console, your data collection module analyzes and displays the following metrics.
+ Database support dates
+ Number of lines of code
+ Schema complexity
+ Similarity of schemas

When you use the database and analytics data collection module to collect **Metadata, database capacity, and resource utilization**, it captures the following metrics.
+ I/O throughput on your database servers
+ Input/output operations per second (IOPS) on your database servers
+ Number of CPUs that your OS servers use
+ Memory usage on your OS servers
+ Storage usage on your OS servers

You can use the database and analytics data collection module to collect metadata, capacity, and utilization metrics from your Oracle and SQL Server databases. At the same time, for PostgreSQL and MySQL databases, the data collection module can collect only metadata.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
