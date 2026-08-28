---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/database-assessment-pre-migration.html
---

# Assessing your database environment before migration
<a name="database-assessment-pre-migration"></a>

Before starting the migration, we recommend that you assess your on-premises database environment. An assessment can help you choose a migration approach and strategy that best aligns with your technical requirements and business needs.

We recommend that you complete the following assessment tasks:
+ Analyze and categorize the criticality of your PostgreSQL database.
+ Check the database size and project its future growth for at least the next five years.
+ Generate a [pgBadger](https://pgbadger.darold.net/documentation.html) report to analyze the database workload.
+ Understand the peak usage of I/O, CPU, concurrent connections, and other relevant metrics so that you can choose the appropriate [EC2 instance type](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/) for your workload.
+ Generate [PostgreSQL diagnostic support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.PostgreSQL.html), and then analyze the results to gain insights and anticipate the challenges of using AWS Database Migration Service (AWS DMS) for the migration.
+ Tune the `postgresql.conf` file to find out the optimal values for achieving the best performance of your instance sizes (that is, for disk IOPS, memory, and CPU).
+ Update the `pg_hba.conf` file so that both your application servers and bastion hosts connect to the same virtual private cloud (VPC).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
