---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/tables-views.html
---

# System tables and views for Amazon Redshift queries
<a name="tables-views"></a>

System tables and views often hold information that can help you troubleshoot issues with your queries. For example, you can use system tables and views to figure out why some queries are hanging or why some queries are running longer than others. Here are some of the most commonly used views:
+ **STL\_QUERY** – Returns execution information about a database query
+ **STL\_QUERY\_METRICS** – Contains metrics information (such as the number of rows processed, CPU usage, input/output, and disk use) for queries that run in user-defined query queues
+ **STL\_QUERYTEXT** – Captures the query text for SQL commands
+ **STL\_TR\_CONFLICT** – Logs lock conflicts
+ **STL\_BCAST** – Logs information about network activity during execution of query steps that broadcast data

For more information about system tables and views, see [STL views for logging](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_STL_tables.html) in the Amazon Redshift documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
