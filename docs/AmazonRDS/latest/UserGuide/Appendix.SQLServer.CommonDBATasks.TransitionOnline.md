---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TransitionOnline.html
---

# Transitioning a Amazon RDS for SQL Server database from OFFLINE to ONLINE
<a name="Appendix.SQLServer.CommonDBATasks.TransitionOnline"></a>

You can transition your Microsoft SQL Server database on an Amazon RDS DB instance from `OFFLINE` to `ONLINE`.

| SQL Server method | Amazon RDS method |
| --- | --- |
| ALTER DATABASE {{db\_name}} SET ONLINE; | EXEC rdsadmin.dbo.rds\_set\_database\_online {{db\_name}} |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
