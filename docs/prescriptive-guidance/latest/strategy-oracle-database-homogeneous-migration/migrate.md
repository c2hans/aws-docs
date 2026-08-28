---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/migrate.html
---

# Phase 3: Migrate
<a name="migrate"></a>

During this phase, you migrate the data. Oracle supports a variety of migration tools. You can choose the appropriate data migration tool based on factors such as database availability requirements (online or offline migration), licensing, migration strategy, and target for the database,.

Oracle provides native tools such as [Oracle Data Pump Export and Import](https://docs.oracle.com/cd/E11882_01/server.112/e22490/part_dp.htm), [Oracle Recovery Manager (RMAN)](https://docs.oracle.com/cd/E29505_01/backup.1111/e10642/rcmquick.htm), [Oracle GoldenGate](https://www.oracle.com/au/integration/goldengate/#:~:text=OCI%20GoldenGate%20is%20a%20real,in%20the%20Oracle%20Cloud%20Infrastructure.), and [Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/introduction-to-oracle-data-guard-concepts.html). Other tools, such as [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), are complementary and aid in migration. For example, you can use [Oracle Data Pump export and import with AWS DMS](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/) to perform online migration with near zero downtime.

The following table lists migration tools and the targets that they support.

|
|
| Migration tool | Supports Amazon EC2 | Supports Amazon RDS for Oracle | Supports Amazon RDS Custom for Oracle |
| --- |--- |--- |--- |
| Oracle Data Pump Export and Import | Yes | Yes | Yes |
| AWS DMS | Yes | Yes | Yes |
| Oracle GoldenGate | Yes | Yes | Yes |
| Oracle Data Guard | Yes | No | Yes |
| Oracle RMAN | Yes | No | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
