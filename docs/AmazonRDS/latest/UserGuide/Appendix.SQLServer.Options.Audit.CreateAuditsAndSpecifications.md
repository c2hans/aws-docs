---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.CreateAuditsAndSpecifications.html
---

# Using SQL Server Audit
<a name="Appendix.SQLServer.Options.Audit.CreateAuditsAndSpecifications"></a>

You can control server audits, server audit specifications, and database audit specifications the same way that you control them for on-premises database servers.

## Creating audits
<a name="Appendix.SQLServer.Options.Audit.CreateAudits"></a>

You create server audits in the same way that you create them for on-premises database servers. For information about how to create server audits, see [CREATE SERVER AUDIT](https://docs.microsoft.com/sql/t-sql/statements/create-server-audit-transact-sql) in the Microsoft SQL Server documentation.

To avoid errors, adhere to the following limitations:
+ Don't exceed the maximum number of supported server audits per instance of 50.
+ Instruct SQL Server to write data to a binary file.
+ Don't use `RDS_` as a prefix in the server audit name.
+ For `FILEPATH`, specify `D:\rdsdbdata\SQLAudit`.
+ For `MAXSIZE`, specify a size between 2 MB and 50 MB.
+ Don't configure `MAX_ROLLOVER_FILES` or `MAX_FILES`.
+ Don't configure SQL Server to shut down the DB instance if it fails to write the audit record.

## Creating audit specifications
<a name="Appendix.SQLServer.Options.Audit.CreateSpecifications"></a>

You create server audit specifications and database audit specifications the same way that you create them for on-premises database servers. For information about creating audit specifications, see [CREATE SERVER AUDIT SPECIFICATION](https://docs.microsoft.com/sql/t-sql/statements/create-server-audit-specification-transact-sql) and [CREATE DATABASE AUDIT SPECIFICATION](https://docs.microsoft.com/sql/t-sql/statements/create-database-audit-specification-transact-sql) in the Microsoft SQL Server documentation.

To avoid errors, don't use `RDS_` as a prefix in the name of the database audit specification or server audit specification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
