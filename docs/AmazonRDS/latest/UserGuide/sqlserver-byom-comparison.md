---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-byom-comparison.html
---

# Differences between Developer Edition and BYOM
<a name="sqlserver-byom-comparison"></a>

The following table compares Developer Edition BYOM with Standard and Enterprise Edition BYOM on RDS for SQL Server.

|  | Developer Edition BYOM | Standard/Enterprise Edition BYOM |
| --- | --- | --- |
| Licensing requirement | No License Mobility required. See [Preparing for Developer Edition](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.preparing.html). | License Mobility through Software Assurance required. See [Creating and managing BYOM engine versions for RDS for SQL Server](sqlserver-byom-creating-cev.md). |
| Cumulative Update Download | Customer needs to provide it | No action is required for CU files. Simply select the desired minor engine version when creating your CEV, and Amazon RDS will automatically download the appropriate CU. |
| Multi-AZ | Not supported | Supported |
| Read Replica | Not supported | Supported |
| SQL Server Integration Service (SSIS) | Not supported | Supported |
| SQL Server Reporting Service (SSRS), SQL Server Analysis Service (SSAS) | Not supported | Not supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
