---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/aws-database-migration-service.html
---

# AWS DMS
<a name="aws-database-migration-service"></a>

AWS Database Migration Service (AWS DMS) is a managed service that helps you move data to the AWS Cloud easily and securely. If your database is relatively small and your application can tolerate a moderate level of downtime, then AWS DMS is a migration option worth considering. You can use AWS DMS even if you have minimal downtime requirements. This is because AWS DMS offers full load and continuous replication support.

AWS DMS offers the following advantages:
+ Supports both homogeneous and heterogeneous migrations
+ Uses change data capture to keep the source and target databases in sync and to minimize downtime during a migration

## Architecture
<a name="architecture-aws-dms"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using AWS DMS.

![AWS DMS architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/2683ebd7-48c5-4819-a718-3a6a5bac67d2.png)

The diagram shows the following workflow:

1. Create a PostgreSQL database instance in Amazon EC2.

1. Create a replication instance in AWS DMS.

1. Create source and target endpoints for a replication task in AWS DMS.

1. Create a replication task that's responsible for migrating data from a source database to a target database.

1. Complete the migration and clean up the resources.

For more information on how to use AWS DMS, see [Working with self-managed PostgreSQL databases as a source in AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.Prerequisites) in the AWS DMS documentation.

## Limitations
<a name="logical-replication-considerations"></a>

For more information on AWS DMS limitations, see [Limitations on using a PostgreSQL database as a DMS source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.Limitations) in the AWS DMS documentation.
