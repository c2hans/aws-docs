---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/data-providers-oracle-dw.html
---

# Using an Oracle Data Warehouse database as a source in DMS Schema Conversion
<a name="data-providers-oracle-dw"></a>

You can use Oracle Data Warehouse databases as a migration source in DMS Schema Conversion to convert database code objects and application code to Amazon Redshift.

For information about supported Oracle database versions, see [Source data providers for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion). For more information about using DMS Schema Conversion with a source Oracle database, see the [ Oracle to PostgreSQL migration step-by-step walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql.html).

## Privileges for using an Oracle Data Warehouse database as a source
<a name="data-providers-oracle-dw-privileges"></a>

The following privileges are required for Oracle Data Warehouse as a source:
+ CONNECT
+ SELECT\_CATALOG\_ROLE
+ SELECT ANY DICTIONARY

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
