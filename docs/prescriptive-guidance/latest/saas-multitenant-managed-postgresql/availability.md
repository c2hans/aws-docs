---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/availability.html
---

# PostgreSQL availability for the pool model
<a name="availability"></a>

Pool models by their nature have only a single PostgreSQL instance. Therefore, designing your application for high availability is crucial. A failure or outage of a pooled database results in your application being degraded or becoming inaccessible for *all* your tenants.

Amazon RDS for PostgreSQL DB instances can be made redundant across two Availability Zones by enabling the high-availability feature. For more information, see [High availability (Multi-AZ) for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) in the Amazon RDS documentation. For cross-Region failover, you can create a read replica in a different AWS Region. (This read replica has to be promoted as part of a failover process.) In addition, you can replicate backups replicated across AWS Regions for recovery. For more information, see [Replicating automated backups to another AWS Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html) in the Amazon RDS documentation.

Aurora PostgreSQL-Compatible automatically backs up data in a way that can sustain the failure of multiple Availability Zones. (See [High availability for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html) in the Aurora documentation.) To make Aurora more resilient and recover faster, you can create Aurora read replicas in other Availability Zones. You can use Aurora global databases to replicate data into five additional AWS Regions for cross-Region recovery and automatic failover. (See [Using Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) in the Aurora documentation.) Additionally, you can enable [write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html) with Aurora global databases to achieve high availability across multiple AWS Regions.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/images/guide-img/df8a9c2c-aa88-448f-93ca-fcf7168e9781/images/6c7495ac-8a8f-4fbb-91c8-3af2e28ef37e.png)

Regardless of whether you're using Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible, we recommend that you implement high availability features to mitigate the impact of any outages for all multi-tenant SaaS applications that use a pool model.
