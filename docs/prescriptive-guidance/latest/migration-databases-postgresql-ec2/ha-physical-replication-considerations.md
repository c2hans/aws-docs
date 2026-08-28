---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/ha-physical-replication-considerations.html
---

# Physical replication
<a name="ha-physical-replication-considerations"></a>

Physical replication is block-level replication where a WAL file is shipped from a primary database to a secondary database. Physical replication is also called *streaming replication* because it allows a standby server to stay more up-to-date than is possible with file-based log shipping. The standby server connects to the primary database. Then, the primary database streams WAL records to the standby database without waiting for the WAL file to be filled. Physical replication is an option worth considering if you have a small or medium-sized database and you're planning to use the same database version. Also, you can use physical replication for larger databases, but the sync can take a considerable amount of time. You can use either of the following two methods with physical replication:

1. **Asynchronous** – The asynchronous method is the default option. If the primary server crashes, then some transactions that were committed to the database could fail to be replicated on the standby server and cause data loss.

1. **Synchronous** – The synchronous method offers the ability to confirm that all changes made by a transaction are transferred to one or more synchronous standby servers.

## Architecture
<a name="architecture-physical-replication"></a>

The following diagram shows the architecture for setting up HADR for your on-premises PostgreSQL database on Amazon EC2 by using physical replication.

![Physical replication architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/ade2ef34-ba22-4e40-8a74-57b89b1aa40d.png)

The diagram shows the following workflow:

1. Replicate the database on an EC2 instance and copy over the archive files.

1. Promote the new replica as the database writer endpoint.

1. Point the application to the new target database.

## Limitations
<a name="limitations-physical-replication"></a>

We recommend that you consider the following limitations of using physical replication before starting your migration:
+ A significant amount of diskspace is required on the server to take backups and then copy the backups on Amazon EC2.
+ A significant amount of bandwidth is required to synchronize the source and target databases and achieve faster copying for the archive log.
+ Source and target databases must have the same version of PostgreSQL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
