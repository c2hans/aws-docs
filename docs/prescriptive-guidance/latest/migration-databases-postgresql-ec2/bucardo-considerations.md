---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/bucardo-considerations.html
---

# Bucardo
<a name="bucardo-considerations"></a>

[Bucardo](https://bucardo.org/Bucardo/) is one of the earliest invocation-based replication tools developed to achieve replication in PostgreSQL. Bucardo is rarely used now that PostgreSQL offers built-in replication.

Here are the most common use cases for Bucardo:
+ Your source database is running on an old version of PostgreSQL (earlier than PostgreSQL 9.2).
+ You're migrating a PostgreSQL database from one cloud provider to another online.

## Architecture
<a name="architecture-bucardo"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using Bucardo.

![Bucardo architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/2133fb23-8f26-4cb7-a58c-96286e1f60a6.png)

The diagram shows the following workflow:

1. Create an EC2 instance.

1. Install PostgreSQL and [Bucardo](https://bucardo.org/Bucardo/installation/) on the EC2 instance.

1. Register the source and target database.

1. Add tables (which should be part of replication).

1. Start Bucardo replication.

1. Use the COPY command to migrate the initial load. Then, Bucardo replicates delta changes later.

## Considerations
<a name="limitations-bucardo"></a>

We recommend that you consider the following limitations of using Bucardo before starting your migration:
+ There is extra overhead on the source database during migration because Bucardo uses invocation-based replication.
+ Bucardo, when installed, must have enough disk space and other resources to accumulate the delta during backup and restore activity and to replicate the delta faster as soon as the restore finishes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
