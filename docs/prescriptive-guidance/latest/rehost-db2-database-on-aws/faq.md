---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to frequently asked questions about migrating Db2 from on premises to Amazon EC2 on AWS.

## What is the best way to copy the schema?
<a name="q1"></a>

Use db2look to export all schema definitions. On the source, run the following command.

```
db2look -d sample -a -e -x -l -o db2look.<db-name>.ddl
```

On the target, run the command `db2 -tvf db2look.<db-name>.ddl`.

## How do I select the right logical replication tools?
<a name="q2"></a>

When it comes to selecting the right logical replication tools, knowledge, performance, and license cost are the major factors to consider. The main reason for using replication is to reduce the migration outage window for databases that are critical to the business. If you have in-house knowledge of these products, it makes the setup much easier.

Licensing cost is important because the license is required only for the duration of migration. If you have multiple databases to convert, you can work with the vendor to determine opportunities for license reuse or recycling. For the most basic descriptions of the IBM replication tools, Q Replication is fast, SQL Replication is less expensive, and InfoSphere CDC is versatile.

For third-party replication tools, including [Qlik Replicate](https://help.qlik.com/en-US/replicate/May2025/Content/Replicate/Main/Introduction/replicat_concepts.htm) and [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/), see the vendors' websites for details.

## How can I migrate Db2 on z/OS to Amazon EC2?
<a name="q3"></a>

Db2 on z/OS is big endian. All logical replication tools can be used to migrate data. LOAD FROM CURSOR and Optim HPU are also supported for migration from z/OS.

## Are there any fallback solutions to consider?
<a name="q4"></a>

For data unload and load, you can consider unloading changed data, but there are challenges because not all tables have the column to indicate changes. HADR failover (option 2) has a built-in fallback solution: Changed data is automatically sent back to the on-premises server after takeover is complete (primary and secondary role switch). If you use logical replication, you can set up two-way replication to support fallback.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
