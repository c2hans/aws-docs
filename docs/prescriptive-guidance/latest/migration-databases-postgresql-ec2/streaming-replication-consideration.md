---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/streaming-replication-consideration.html
---

# Streaming replication
<a name="streaming-replication-consideration"></a>

You can use streaming replication to keep WAL data or XLOG records current by continuously shipping and applying the WAL data or XLOG records to standby servers. If your business application can't experience any downtime, then streaming replication is a migration option to consider.

## Architecture
<a name="architecture-streaming-replication"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using streaming replication.

![Streaming replication architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/af71bfcc-3fa0-40dc-9291-f92786bbf09a.png)

The diagram shows the following workflow:

1. Replicate the database on an EC2 instance and copy over archive files.

1. Promote the new replica as the database writer endpoint.

1. Point the application to the new target database.

## Limitations
<a name="limitations-streaming-replication"></a>

We recommend that you consider the following limitations of using streaming replication before starting your migration:
+ A significant amount of diskspace is required on the server to take backups and then copy the backups to Amazon EC2.
+ A significant amount of bandwidth is required to synchronize the source and target databases and achieve faster copying for the archive log.
+ Source and target databases must have the same version of PostgreSQL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
