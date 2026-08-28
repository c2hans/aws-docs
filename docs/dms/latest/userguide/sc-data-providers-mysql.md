---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-mysql.html
---

# Using a MySQL database as a source in DMS Schema Conversion
<a name="sc-data-providers-mysql"></a>

You can use MySQL databases as a migration source in DMS Schema Conversion.

You can use DMS Schema Conversion to convert database code objects from MySQL Database to the following targets:
+ PostgreSQL
+ Aurora PostgreSQL

The privileges required for MySQL as a source are as follows:
+ `SELECT ON *.*`
+ `SHOW VIEW ON *.*`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
