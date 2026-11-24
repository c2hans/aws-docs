---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_OnDemandDBInstances.html
---

# On-Demand DB instances for Aurora

Amazon RDS on-demand DB instances are billed based on the class of the DB instance (for example, db.t3.small or db.m5.large). For Amazon RDS pricing information, see the [Amazon RDS product page](https://aws.amazon.com/rds/pricing).

Billing starts for a DB instance as soon as the DB instance is available. Pricing is listed on a per-hour basis, but bills are calculated down to the second and show times in decimal form. Amazon RDS usage is billed in one-second increments, with a minimum of 10 minutes. In the case of billable configuration change, such as scaling compute or storage capacity, you're charged a 10-minute minimum. Billing continues until the DB instance terminates, which occurs when you delete the DB instance or if the DB instance fails.

If you no longer want to be charged for your DB instance, you must stop or delete it to avoid being billed for additional DB instance hours. For more information about the DB instance states for which you are billed, see [Viewing DB instance status in an Aurora cluster](accessing-monitoring.md#Overview.DBInstance.Status).

## Stopped DB instances
<a name="USER_OnDemandDBInstances.Stopped"></a>

While your DB instance is stopped, you're charged for provisioned storage, including Provisioned IOPS. You are also charged for backup storage, including storage for manual snapshots and automated backups within your specified retention window. You aren't charged for DB instance hours.

## Multi-AZ DB instances
<a name="USER_OnDemandDBInstances.MultiAZ"></a>

In Aurora, you create a Multi-AZ DB cluster by adding one or more Aurora Replicas in Availability Zones that are different from the writer DB instance's. Aurora always replicates your data across three Availability Zones in the cluster volume, whether the cluster has one DB instance or several. Each DB instance that you add increases your compute charges, but your storage charges stay the same.

Consider the following important details about Multi-AZ pricing:
+ **Compute costs**: Billed per DB instance-hour for each DB instance in the DB cluster, including the writer DB instance and each Aurora Replica.
+ **Storage costs**: Charged per GB-month for the storage that your DB cluster's shared cluster volume uses. All DB instances in the cluster, including Aurora Replicas in other Availability Zones, share the same cluster volume, so adding DB instances doesn't increase your storage charges.
+ **Data transfer costs**: Replication between the DB instances in your DB cluster is included in the cost, but other data transfer charges might apply based on your usage.

To accurately estimate your monthly costs based on your specific use case and AWS Region, you can use the AWS Pricing Calculator. With this tool, you can input your configuration details and get a comprehensive cost breakdown.

**Note**
Pricing is subject to change. See the [Amazon RDS Pricing page](https://aws.amazon.com/rds/pricing/) for the most up-to-date information.
