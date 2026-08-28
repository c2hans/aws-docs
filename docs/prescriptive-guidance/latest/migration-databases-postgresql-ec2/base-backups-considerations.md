---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/base-backups-considerations.html
---

# Base backup
<a name="base-backups-considerations"></a>

A base backup is for rehosting to the AWS Cloud without changing your database and Linux versions. Base backups are applicable to databases smaller than 500 GB. To perform a base backup, you must use Direct Connect to set up a direct link between your on-premises PostgreSQL database and the AWS Cloud.

## Architecture
<a name="architecture-for-base-backups"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using a base backup.

![Base backup architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/05218c96-50c3-43e8-b0e4-5a8d09de4e8a.png)

The diagram shows the following workflow:

1. Use the [pg\_basebackup](https://www.postgresql.org/docs/current/app-pgbasebackup.html) PostgreSQL utility to take a physical backup of the data from your on-premises database, and then copy that backup to the Amazon EC2 data directory location in the AWS Cloud.

1. Complete the PostgreSQL migration.

1. Perform a [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html) operation on the database.

1. Validate your data.

1. Point your application to the new PostgreSQL database on the EC2 instance.

## Limitations
<a name="limitations-base-backup"></a>

We recommend that you consider the following limitations of using base backups before starting your migration:
+ A dump and restore can be time-consuming for larger databases (that is, databases from 50 GB to 300 GB).
+ This option requires complete database downtime.
+ A significant amount of diskspace is required on the server to take backups and then copy the backups to Amazon EC2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
