---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-sybase-ASE.html
---

# Using a SAP ASE (Sybase ASE) database as a source in AWS DMS Schema Conversion
<a name="dm-data-providers-source-sybase-ASE"></a>

You can use SAP ASE (Sybase ASE) databases as a migration source in DMS Schema Conversion.

You can use DMS Schema Conversion to convert database code objects from SAP ASE (Sybase ASE) Database to the following targets:
+ Aurora PostgreSQL
+ RDS for PostgreSQL

For information about the supported SAP ASE (Sybase ASE) database versions, see [Source data providers for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion)

## Privileges for SAP ASE (Sybase ASE) as a source database
<a name="dm-data-providers-source-sybase-ASE.privileges"></a>

The following privileges are required when using SAP ASE (Sybase ASE) as a source database:
+ USE master
+ select on dbo.spt\_values
+ select on asehostname

For each database to be migrated, grant the following privileges:
+ USE db\_name *(Replace db\_name with the name of the database being migrated)*
+ select on dbo.sysusers
+ select on dbo.sysobjects
+ select on dbo.sysindexes
+ select on dbo.syscolumns
+ select on dbo.sysreferences
+ select on dbo.syscomments
+ select on dbo.syspartitions
+ select on dbo.syspartitionkeys
+ select on dbo.sysconstraints
+ select on dbo.systypes
+ select on dbo.sysqueryplans

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
