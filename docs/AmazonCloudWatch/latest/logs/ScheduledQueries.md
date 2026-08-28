---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ScheduledQueries.html
---

# Automating log analysis with scheduled queries
<a name="ScheduledQueries"></a>

Scheduled queries enable you to automate the execution of log queries on a regular schedule. Instead of manually running queries to analyze your log data, you can configure scheduled queries to run automatically and deliver results to destinations such as Amazon S3 buckets, Amazon EventBridge event buses, or lookup tables. This automation is ideal for generating regular reports, monitoring trends, keeping lookup tables current with your latest log data, or triggering downstream processes based on log analysis results.

Scheduled queries support all three query languages available for log queries:
+ [**Logs Insights query language (Logs Insights QL)**](CWL_AnalyzeLogData_LogsInsights.md)
+ [**OpenSearch Service Piped Processing Language (PPL)**](CWL_AnalyzeLogData_PPL.md)
+ [**OpenSearch Service Structured Query Language (SQL)**](CWL_AnalyzeLogData_SQL.md)

**Topics**
+ [Understanding scheduled queries concepts](scheduled-queries-concepts.md)
+ [Schedule expression reference](scheduled-queries-schedule-reference.md)
+ [Best practices](scheduled-queries-best-practices.md)
+ [Getting started with scheduled queries](scheduled-queries-getting-started.md)
+ [Configuring S3 destinations for scheduled queries](scheduled-queries-s3-destination.md)
+ [Configuring lookup table destinations for scheduled queries](scheduled-queries-lookup-table-destination.md)
+ [Troubleshooting scheduled queries](scheduled-queries-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
