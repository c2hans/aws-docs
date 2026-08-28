---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/migration-phase-comparison-table.html
---

# Migration phase comparison table
<a name="migration-phase-comparison-table"></a>

The following table provides a summary of suitable migration scenarios for each tool to help you choose the option that best meets your business requirements.

|
|
|  Tool | Online migration | Offline migration | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |--- |--- |
| Oracle Data Pump | No | Yes | Yes | Yes |
| AWS DMS | Yes | Yes | Yes | Yes |
| Oracle GoldenGate | Yes | No | Yes | Yes |
| Oracle Recovery Manager (RMAN) | No | Yes | No | Yes |
| Oracle Data Guard | Yes | No | No | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
