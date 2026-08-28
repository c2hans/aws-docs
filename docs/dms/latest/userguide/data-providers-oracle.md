---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/data-providers-oracle.html
---

# Using an Oracle database as a source in DMS Schema Conversion
<a name="data-providers-oracle"></a>

You can use Oracle databases as a migration source in DMS Schema Conversion.

To connect to your Oracle database, use the Oracle System ID (SID). To find the Oracle SID, submit the following query to your Oracle database:

```
SELECT sys_context('userenv','instance_name') AS SID FROM dual;
```

You can use DMS Schema Conversion to convert database code objects from Oracle Database to the following targets:
+ Aurora MySQL
+ Aurora PostgreSQL
+ RDS for MySQL
+ RDS for PostgreSQL

For information about the supported Oracle database versions, see [Source data providers for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion).

For more information about using DMS Schema Conversion with a source Oracle database, see the [Oracle to PostgreSQL migration step-by-step walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql.html).

## Privileges for Oracle as a source
<a name="data-providers-oracle-permissions"></a>

The following privileges are required for Oracle as a source:
+ CONNECT
+ SELECT\_CATALOG\_ROLE
+ SELECT ANY DICTIONARY
+ SELECT ON SYS.ARGUMENT$

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
