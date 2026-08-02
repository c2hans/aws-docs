---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/sites-strategies.html
---

# DR sites and common Amazon RDS DR strategies
<a name="sites-strategies"></a>

A disaster recovery (DR) site is a secondary location used by an organization for restoring its business-critical IT infrastructure and applications when a primary site has been impacted by disaster. DR sites are often built in a remote location to help ensure that the disaster affecting the main site will not also affect the secondary site. DR sites available to you within AWS can be broadly categorized as near DR and far DR:
+ Near DR is often referred to as in-Region disaster recovery. The DR solution is configured among the Availability Zones to protect the system when there is an Availability Zone outage or planned maintenance.
+ Far DR is often referred to as cross-Region disaster recovery. The solution is configured across AWS Regions to protect the system from Region-wide outages or for conducting planned switchovers to meet compliance policies.

## Synchronous DR
<a name="synchronous"></a>

In synchronous DR, data is replicated to the DR site at the same time as new data is being created or updated on the primary site. To achieve a synchronous DR solution for standard edition databases, you can use Multi-AZ deployment.

Multi-AZ deployment (near DR) is an AWS managed near-DR solution that provides synchronous replication of your RDS database to a standby instance in a different Availability Zone within the same Region. If the primary database becomes unavailable because of an outage at the Availability Zone level, AWS automatically promotes the standby database to the primary role. This ensures minimal data loss and downtime. However, it's important to note that Multi-AZ deployment does not protect against Region-level outages. It also doesn't provide any DR capabilities outside of the AWS Cloud.

## Asynchronous DR options
<a name="asynchronous"></a>

In asynchronous DR, replication is not performed at the same time as changes are made in the primary. Data is replicated only at the intervals defined by the recovery point objective. To implement an asynchronous DR solution, you can use the following options:
+ Automated [snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) managed using AWS Backup – AWS Backup is a fully managed backup service that automates the backup and recovery of your Amazon RDS database based on your point-in-time recovery (PITR) settings. With AWS Backup, you can take snapshots, create backup schedules, retention policies, and backup plans to protect your data against accidental deletion, corruption, or hardware failures. You can restore your database to a new RDS instance in the same AWS Region or in a different Region.

  AWS Backup is an active-passive DR option because you have to manually initiate the restore process in the case of a primary database failure. You can use AWS Backup in conjunction with a Multi-AZ deployment, combining synchronous and asynchronous solutions to provide an additional layer of protection against data loss.
+ Amazon RDS PITR snapshot replication – RDS snapshots are a manual DR option. You define a point-in-time snapshot configuration for your RDS database instance, and the snapshots are stored in Amazon Simple Storage Service (Amazon S3). You can then enable cross-Region replication to replicate changes from the primary database to the standby database in a different Region.

  Amazon RDS PITR snapshot replication is an active-passive DR option because you have to manually initiate the restore process and promote the standby database to the primary role if the original primary database fails. However, this option provides more flexibility than Multi-AZ deployment, and you can use it to protect against Region-level outages.
