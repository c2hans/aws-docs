---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/ha-postgresql-databases-ec2.html
---

# Setting up high availability
<a name="ha-postgresql-databases-ec2"></a>

As a best practice, we recommend that you set up high availability and disaster recovery (HADR) for your PostgreSQL database on Amazon EC2. You can use replication mechanisms that are native to PostgreSQL to set up HADR and data protection for your PostgreSQL database on Amazon EC2. The following options are available in PostgreSQL:
+ Physical replication
+ Logical replication
+ Patroni and etcd

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
