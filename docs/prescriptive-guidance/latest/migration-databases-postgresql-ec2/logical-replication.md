---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/logical-replication.html
---

# Logical replication
<a name="logical-replication"></a>

Logical replication is row-level replication. You can set up logical replication between primary and secondary databases. Logical replication supports INSERT, UPDATE, DELETE, and TRUNCATE operations, but it doesn't support DDL operations such as CREATE, ALTER, and DROP.

## Architecture
<a name="architecture-ha-logical-replication"></a>

The following diagram shows the architecture for setting up HADR for your on-premises PostgreSQL database on Amazon EC2 by using logical replication.

![Logical replication architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/9452bde8-0fc5-4ecc-85a3-10aaafe0fe99.png)

In both physical and logical replication, you don't have the automatic failover option that you have in Amazon RDS and Amazon Aurora. However, you can use Patroni and etcd for automatic failover management.

## Limitations
<a name="limitations-ha-logical-replication"></a>

We recommend that you consider the following limitations of using logical replication before starting your migration:

1. The schema/DDL isn't replicated.

1. Tables must have a primary key or unique key.

1. Sequences aren't replicated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
