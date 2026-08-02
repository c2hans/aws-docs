---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/automated-snapshot-copy.html
---

# Automated snapshots using AWS Backup
<a name="automated-snapshot-copy"></a>

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) centralizes and automates data protection across AWS services. AWS Backup is a fully managed, policy-based service for data protection at scale. The service is ideal for use cases such as regulatory compliance obligations, business policies for data protection, and business continuity goals.

The following diagram shows using an AWS Backup plan and backup vault to take snapshots of the Amazon RDS instance at scheduled intervals and copy the snapshots to the DR Region.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/images/guide-img/d84bd0dc-b6eb-4d26-8602-78820cdf415f/images/06eda206-3cf6-4dd7-92b2-a6e0e633fe35.png)

1. Snapshot restore points

AWS Backup doesn't have continuous replication enabled across AWS Regions, which means you will have extended recovery point objective (RPO). The RPO will depend on how frequently you are taking snapshots (defined in backup plan) on the primary database and copying to the standby Region. Because this is a snapshot-based solution, the RPO and recovery time objective (RTO) will depend on the snapshot frequency and restore time. This can vary, and it can be up to a couple hours depending on the database size.

The major benefits of using AWS Backup are the automated backup schedule and retention management. Specific requirements, such as taking a backup once a month or on a particular cadence, can be implemented.

The failover by restoring the snapshot from an AWS Backup service backup vault is manual and not transparent to the application. After you restore the snapshot as a new RDS instance in the standby Region, you must modify the application connection settings.
