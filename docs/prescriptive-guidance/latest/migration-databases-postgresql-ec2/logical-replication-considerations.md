---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/logical-replication-considerations.html
---

# Logical replication
<a name="logical-replication-considerations"></a>

Logical replication is a method of replicating data objects and their changes based on the replication identity of the objects and their changes. Logical replication uses a *publish* and *subscribe* model where one or more subscribers subscribes to one or more publications on a publisher node. Subscribers pull data from the publications that they subscribe to.

Logical replication gives you fine-grained control over both data replication and security. You can use logical replication in the following use cases:
+ Replicating between different major versions of PostgreSQL
+ Replicating between PostgreSQL instances on different platforms (for example, Linux to Windows)

## Architecture
<a name="architecture-logical-replication"></a>

The following workflow steps show how a logical replication architecture works:

1. You take a snapshot of the data on the publisher database and copy that data to the subscriber database.

1. The changes in the publisher databases are sent to the subscriber in real time.

1. The subscriber applies the data in the same order as the publisher so that transactional consistency is guaranteed for publications within a single subscription.

A *publication* can be defined on a primary instance (publisher). A publication is a set of changes generated from a table or a group of tables. You can choose changes from a combination of INSERT, UPDATE, DELETE, and TRUNCATE operations. By default, all these changes are replicated to the subscriber database. This is in contrast with physical replication, where exact block addresses are used for a byte-by-byte replication. A published table must have a [REPLICA IDENTITY](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-ALTERTABLE-REPLICA-IDENTITY) configured to replicate UPDATE and DELETE operations so that appropriate rows to update or delete can be identified on the subscriber side. In most cases, the replica identity is determined by either a primary key or unique key. If a primary key is not present and you can't create one, then you can set the replica identity to `full`. This means the entire row becomes the key. We recommend that you set the replica identity to `full` as a last resort because this setting is inefficient.

A *subscription* is the downstream side of logical replication. The node where a subscription is defined is referred to as the *subscriber*. A subscription defines the connection to another database and set of publications (one or more) to which it wants to subscribe.

## Configuration settings
<a name="config-settings"></a>

The following configurations are required for publisher settings:
+ Set `wal_level` to `logical`.
+ Set `max_replication_slots` to accommodate at least the number of subscriptions expected to connect and some reserve slots for table synchronization.
+ Set `max_wal_senders` to accommodate `max_replication_slots` and your number of physical replicas.

The following configurations are required for subscriber settings:
+ Set `max_replication_slots` to accommodate the least number of subscriptions that you plan to add to the subscriber and some reserve subscriptions for table synchronization.
+ Set `max_logical_replication_workers` to accommodate at least the number of subscriptions and some reserve workers for the table synchronization.
+ Set `max_worker_processes` at least to (`max_logical_replication_workers` \+ `1`).

Each subscription receives changes through one replication slot.

The following steps show how to perform logical replication:

1. Create a publisher by using the [CREATE PUBLICATION](https://www.postgresql.org/docs/10/sql-createpublication.html) command for a group of tables (which will be part of replication) in the source database.

1. Create a subscriber by using the [CREATE SUBSCRIPTION](https://www.postgresql.org/docs/10/sql-createsubscription.html) command, and then provide publication details when you create the subscriber.

1. The initial data load automatically begins from the source database to the target database.

1. The change data that's captured by replication slots is replicated to the target database.

1. Use [pg\_stat\_replication](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW) (a catalog table) to check the status of replication. Use [pg\_stat\_replication\_slots](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-SLOTS-VIEW) to check the replication slot.

For more information, see the [Using logical replication to replicate managed Amazon RDS for PostgreSQL and Amazon Aurora to self-managed PostgreSQL](https://aws.amazon.com/blogs/database/using-logical-replication-to-replicate-managed-amazon-rds-for-postgresql-and-amazon-aurora-to-self-managed-postgresql/) post in the AWS Database Blog.

## Limitations
<a name="limitations-logical-replication"></a>

We recommend that you consider the following limitations of the logical replication method before starting your migration:
+ Logical replication currently has the most restrictions and functionality gaps.
+ Logical replication can't replicate data definition language (DDL), sequence, and large object operations. A truncate action (which applies to a table with a foreign key) must include related tables in the same subscription.

For more information on the limitations of logical replication, see [31.6. Restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html) in the PostgreSQL documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
