---
source_url: https://docs.aws.amazon.com/athena/latest/ug/work-with-data.html
---

# Create databases and tables
<a name="work-with-data"></a>

Amazon Athena supports a subset of data definition language (DDL) statements and ANSI SQL functions and operators to define and query external tables where data resides in Amazon Simple Storage Service.

When you create a database and table in Athena, you describe the schema and the location of the data, making the data in the table ready for real-time querying.

To improve query performance and reduce costs, we recommend that you partition your data and use open source columnar formats for storage in Amazon S3, such as [Apache parquet](https://parquet.apache.org) or [ORC](https://orc.apache.org/).

**Topics**
+ [Create databases](creating-databases.md)
+ [Create tables](creating-tables.md)
+ [Name databases, tables, and columns](tables-databases-columns-names.md)
+ [Escape reserved keywords](reserved-words.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
