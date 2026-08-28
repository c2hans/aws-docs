---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c-optimizing-query-performance.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Query performance tuning
<a name="c-optimizing-query-performance"></a>

Amazon Redshift uses queries based on structured query language (SQL) to interact with data and objects in the system. Data manipulation language (DML) is the subset of SQL that you use to view, add, change, and delete data. Data definition language (DDL) is the subset of SQL that you use to add, change, and delete database objects such as tables and views.

Once your system is set up, you typically work with DML the most, especially the [SELECT](r_SELECT_synopsis.md) command for retrieving and viewing data. To write effective data retrieval queries in Amazon Redshift, become familiar with SELECT and apply the tips outlined in [Amazon Redshift best practices for designing tables](c_designing-tables-best-practices.md) to maximize query efficiency.

To understand how Amazon Redshift processes queries, use the [Query processing](c-query-processing.md) and [Query analysis and improvement](c-query-tuning.md) sections. Then you can apply this information in combination with diagnostic tools to identify and remove issues in query performance.

To identify and address some of the most common and most serious issues you are likely to encounter with Amazon Redshift queries, use the [Query troubleshooting](queries-troubleshooting.md) section.

**Topics**
+ [Query processing](c-query-processing.md)
+ [Query analysis and improvement](c-query-tuning.md)
+ [Query troubleshooting](queries-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
