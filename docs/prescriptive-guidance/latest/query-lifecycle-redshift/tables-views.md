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
