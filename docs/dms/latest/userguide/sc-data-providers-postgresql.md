---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-postgresql.html
---

# Using a PostgreSQL database as a source in DMS Schema Conversion
<a name="sc-data-providers-postgresql"></a>

You can use PostgreSQL databases as a migration source in DMS Schema Conversion.

You can use DMS Schema Conversion to convert database code objects from PostgreSQL database to the following targets:
+ MySQL
+ Aurora MySQL

The privileges required for PostgreSQL as a source are as follows:
+ CONNECT ON DATABASE <database\_name>
+ USAGE ON SCHEMA <database\_name>
+ SELECT ON ALL TABLES IN SCHEMA <database\_name>
+ SELECT ON ALL SEQUENCES IN SCHEMA <database\_name>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
