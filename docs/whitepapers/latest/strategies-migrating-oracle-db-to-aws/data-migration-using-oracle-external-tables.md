---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-migration-using-oracle-external-tables.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data migration using Oracle external tables
<a name="data-migration-using-oracle-external-tables"></a>

 Oracle external tables are a feature of Oracle Database that allows you to query data in a flat file as if the file were an Oracle table. The process for using Oracle external tables for data migration to AWS is almost exactly the same as the one used for Oracle Data Pump. The Oracle Data Pump-based method is better for large database migrations.

 The external tables method is useful if your current process uses this method and you don’t want to switch to the Oracle Data Pump-based method. Following are the main steps:

1.  Move the external table files to `RDS DATA_PUMP_DIR`.

1.  Create external tables using the files loaded.

1.  Import data from the external tables to the database tables.

 Depending on the size of the data file, you can choose to either write the file directly to `RDS DATA_PUMP_DIR` from an on-premises server, or use an Amazon EC2 bridge instance, as in the case of the Data Pump-based method. If the file size is large and you choose to use a bridge instance, use compression and encryption on the files as well as Tsunami UDP or a WAN accelerator, exactly as described for the Data Pump-based migration.

 To learn more about Oracle external tables, see [External Tables Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sutil/oracle-external-tables-concepts.html#GUID-44323E01-7D72-45EC-915A-99E596769D9E) in the Oracle documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
