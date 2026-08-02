---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/read-replicas-in-amazon-rds-from-on-premises-databases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 3.2 Read-replicas in Amazon RDS from on-premises databases
<a name="read-replicas-in-amazon-rds-from-on-premises-databases"></a>

 Requirements addressed:
+  **REQ1** (data residency)
+  **REQ4** (availability and durability)
+  **Customer-REQ1** (reliable connectivity)

 AWS services – [Amazon RDS](https://aws.amazon.com/rds/), [AWS DMS](https://aws.amazon.com/dms/)

![Read-replicas in Amazon RDS](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/read-replicas-amazon-rds.png)

 Read-replicas in Amazon RDS

 You can use [AWS Database Migration Service](https://aws.amazon.com/dms/) with Amazon RDS, Amazon S3, and an on-premises database (refer to [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html)).

 **REQ1** is fulfilled by performing collection of personal data (such as writes, changes, and updates) in the local primary database.

 **REQ4** is fulfilled by AWS Database Migration Service, which continuously copying data from the local database to Amazon RDS (2A & 2B) in the AWS Region, and (optionally) another copy to an Amazon S3 (3A & 3B) bucket for backup purposes. (Refer to [Using Amazon S3 as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)). Continuous data replication allows both homogeneous and heterogeneous data replications for supported database engines. For a full list supported database engines, refer to [Sources for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html) and [Targets for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html). Write, change, and update operations are restricted for other services (except AWS DMS) on Amazon RDS by allowing only read workloads using appropriate permissions. You can set up Amazon RDS to be the target replica by using native replication (4A & 4B) mechanisms provided by the local database engine.

 **Customer-REQ1** – AWS DMS or native replication flows an be performed over AWS Direct Connect and/or AWS Site-to-Site VPN. For more details, refer to 1:1: [Hybrid network connectivity from a data center to the AWS Cloud](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md).

 For more details about Oracle Disaster Recovery using DMS, refer to [Disaster recovery on Amazon RDS for Oracle using AWS DMS](https://aws.amazon.com/blogs/database/disaster-recovery-on-amazon-rds-for-oracle-using-aws-dms/). For details on native change data capture (CDC) in Oracle and MS SQL for continuous DB replication, refer to [How to work with native CDC support in AWS DMS](https://aws.amazon.com/blogs/database/aws-dms-now-supports-native-cdc-support/). For details on MS SQL ongoing replication, refer to [Introducing Ongoing Replication from Amazon RDS for SQL Server Using AWS Database Migration Service](https://aws.amazon.com/blogs/database/introducing-ongoing-replication-from-amazon-rds-for-sql-server-using-aws-database-migration-service/).
