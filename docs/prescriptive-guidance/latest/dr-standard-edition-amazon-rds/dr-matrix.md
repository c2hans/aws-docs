---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/dr-matrix.html
---

# DR solution decision matrix
<a name="dr-matrix"></a>

Use the following table to review RPO, RTO, licensing and other features of disaster recovery options for Amazon RDS for Oracle and SQL Server and find the solutions that best fit your business requirements.

|
|
| Feature | RPO (approximate) | RTO (approximate) | Licensing | Readable standby | Automatic failover | Endpoint change in failover | Setup and maintenance complexity |
| --- |--- |--- |--- |--- |--- |--- |--- |
| Multi-AZ deployment<br />(in-Region) | 0 | 1–2 minutes | SE, SE2, and EE | No | Yes | No | Low |
| Amazon RDS PITR snapshot replication (cross-Region) | 25 minutes | Hours | SE, SE2, and EE | No | No | Yes | Low |
| Automated snapshots using AWS Backup (cross-Region) | Hours | Hours | SE, SE2, and EE | No | No | Yes | Medium |
| Native transaction log backup replication (SQL Server only) | 5–15 minutes | Minutes | SE and EE | Yes | No | Yes | High |
| AWS DMS | Secondsor minutes | Minutes | SE, SE2, and EE | Yes | No | Yes | High |
| Replica promotion (in-Region) | 0–5 Minutes | Minutes | EE only | Yes | No | Yes | Low |
| Automated snapshots using AWS Backup (in-Region) | 5 minutes | Hours | SE, SE2, and EE | No | No | Yes | Medium |
| Replica promotion (cross-Region) | 0–15 Minutes | Minutes | EE only | Yes | No | Yes | Medium |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
