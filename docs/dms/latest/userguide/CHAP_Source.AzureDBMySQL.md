---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.AzureDBMySQL.html
---

# Using Microsoft Azure Database for MySQL flexible server as a source for AWS DMS
<a name="CHAP_Source.AzureDBMySQL"></a>

With AWS DMS, you can use Microsoft Azure Database for MySQL flexible server as a source in much the same way as you do MySQL.

For information about versions of Microsoft Azure Database for MySQL flexible server that AWS DMS supports as a source, see [Sources for AWS DMS](CHAP_Introduction.Sources.md).

For more information about using a customer-managed MySQL-compatible database with AWS DMS, see [Using a self-managed MySQL-compatible database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.CustomerManaged).

## Limitations when using Azure MySQL as a source for AWS Database Migration Service
<a name="CHAP_Source.AzureDBMySQL.limitations"></a>
+ The defaut value for the Azure MySQL flexible server system variable `sql_generate_invisible_primary_key` is `ON`, and the server automatically adds a generated invisible primary key (GIPK) to any table that is created without an explicit primary key. AWS DMS doesn’t support ongoing replication for MySQL tables with GIPK constraints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
