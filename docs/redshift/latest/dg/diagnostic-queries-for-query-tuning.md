---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/diagnostic-queries-for-query-tuning.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Diagnostic queries for query tuning
<a name="diagnostic-queries-for-query-tuning"></a>

Use the following queries to identify issues with queries or underlying tables that can affect query performance. We recommend using these queries with the query tuning processes discussed in [Query analysis and improvement](c-query-tuning.md).

**Note**
These queries are for Amazon Redshift provisioned clusters. These queries are not for use with Redshift Serverless workgroups.

**Topics**
+ [Identifying queries that are top candidates for tuning](identify-queries-that-are-top-candidates-for-tuning.md)
+ [Identifying tables with data skew or unsorted rows](identify-tables-with-data-skew-or-unsorted-rows.md)
+ [Identifying queries with nested loops](identify-queries-with-nested-loops.md)
+ [Reviewing queue wait times for queries](review-queue-wait-times-for-queries.md)
+ [Reviewing query alerts by table](review-query-alerts-by-table.md)
+ [Identifying tables with missing statistics](identify-tables-with-missing-statistics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
