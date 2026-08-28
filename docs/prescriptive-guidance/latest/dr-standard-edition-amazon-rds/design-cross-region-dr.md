---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/design-cross-region-dr.html
---

# Designing cross-Region DR solutions for Amazon RDS standard editions
<a name="design-cross-region-dr"></a>

When it comes to disaster recovery capabilities, standard editions offer the following cross-Region options:
+ Automated snapshots using AWS Backup
+ Amazon RDS point-in-time recovery (PITR) snapshot replication
+ Native transaction log backup replication
+ AWS Database Migration Service (AWS DMS)

It's essential to understand the recovery time objective (RTO) and recovery point objective (RPO) requirements along with the budget while designing cross-Region DR solutions. You can minimize RPO by configuring a combination of synchronous and asynchronous  DR strategies and options. However, this will increase infrastructure cost.

It's hard to achieve near zero RPO with Amazon RDS standard editions because there are no synchronous replication options. However, AWS can provide competitive RPO by using various cost-effective options.

The following table summarizes the DR solutions and their availability in each license model, with enterprise editions included to give you a complete view:
+ Amazon RDS for Microsoft SQL Server Standard Edition (SE)
+ Amazon RDS for Oracle Standard Edition 2 (SE2)
+ Enterprise Edition (EE) of Amazon RDS for Oracle and Amazon RDS for SQL Server

|
|
| Solution | DR site scope | RDS for SQL Server | RDS for Oracle |
| --- |--- |--- |--- |
| **SE** | **EE** | **SE2** | **EE** |
| Multi-AZ deployment | In-Region | Yes | Yes | Yes | Yes |
| Mounted or read-only replica promotion | In-Region, cross-Region | No | Yes | No | Yes |
| Automated snapshots using AWS Backup | In-Region, cross-Region | Yes | Yes | Yes | Yes |
| Amazon RDS PITR snapshot replication | In-Region, cross-Region | Yes | Yes | Yes | Yes |
| Native transaction log backup replication | In-Region, cross-Region | Yes | Yes | Not Applicable | Not Applicable |
| AWS DMS | In-Region, cross-Region | Yes | Yes | Yes | Yes |

The following sections discuss the options available for cross-Region disaster recovery for standard editions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
