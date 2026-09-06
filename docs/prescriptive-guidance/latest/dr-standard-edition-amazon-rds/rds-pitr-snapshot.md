---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/rds-pitr-snapshot.html
---

# Amazon RDS PITR snapshot replication
<a name="rds-pitr-snapshot"></a>

An Amazon RDS database instance can be configured to replicate snapshots and transaction logs to a destination AWS Region of your choice. After you configure [backup replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html) for a DB instance, Amazon RDS initiates a cross-Region copy of all snapshots and transaction logs as soon as they are ready on the DB instance.

The following diagram shows how Amazon RDS facilitates the automated transfer of snapshots and transaction logs across AWS Regions to maintain the point-in-time recovery (PITR) requirements as configured in the settings of the primary Amazon RDS instance. From the primary Region, snapshots are copied to the secondary Region. Logs are stored in an S3 bucket in the primary Region and copied to an S3 bucket in the secondary Region.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/images/guide-img/d84bd0dc-b6eb-4d26-8602-78820cdf415f/images/68d7b028-b873-4869-8cc5-2a68cb0a4301.png)

1. Transaction or redo logs

Amazon RDS PITR snapshot replication is based on asynchronous replication, so the underlying RPO is on the slightly higher side, ranging 5–30 minutes. The time depends on redo or transaction log generation and network transfer time.

Recovery time objective (RTO) for the cross-Region Amazon RDS PITR snapshot replication backup strategy is based on the snapshot restore time and recovering the database to a point in time by applying the archived redo or transaction logs. The process can take up to a few hours.

One advantage of this strategy is that it's managed. It's also cost effective because the setup requires no additional infrastructure.

Cross-Region Amazon RDS PITR snapshot replication has [limited availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#USER_ReplicateBackups.RegionVersionAvailability) across AWS Regions. Be sure to check availability when you choose your DR Region.
