---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/rds-outpost-multi-az.html
---

# Amazon RDS on Outposts with Multi-AZ
<a name="rds-outpost-multi-az"></a>

In Multi-AZ deployments, Amazon RDS creates a primary DB instance on one AWS Outposts and RDS synchronously replicates the data to a standby DB instance on a different Outposts. In order to provide a resilient architecture, the two AWS Outposts must be anchored to different Availability Zones in a given region and must be operating on Customer-owned IP (CoIP) model. In order to allow the replication between the primary instance and the standby, there must be a network link between the two Outposts with a round-trip time (RTT) latency of single-digit milliseconds. We recommend 5 milliseconds or less. Also consider sizing the replication link between Outposts with sufficient bandwidth to avoid queuing replication jobs.

![Amazon RDS on Outpost with multi AZ](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-45-rds-outposts-multi-az.png)

## Considerations for Amazon RDS on Outposts with Multi-AZ
<a name="rds-outpost-multi-az-considerations"></a>

Review the following considerations for Amazon RDS on Outposts deployments in Multi-AZ:
+ Have at least two Outposts deployments anchored to different Availability Zones in the same AWS Region.
+ Both primary and standby instance requires a single VPC and one subnet per Outposts deployment.
+ Associate your DB instance’s VPC with all of your local gateway route tables.
+ Make sure that your Outposts use customer-owned IP routing.
+ Your local network must allow outbound and related inbound traffic between Outposts for Internet Security Association and Key Management Protocol (ISAKAMP) which use UPD port 500 and IPsec Network Address Translation Traversal (NAT-T) using UDP port 4500.
+ Local RDS backups are not supported for Multi-AZ deployments.
+ If your workload must abide by data residency regulations for your industry or geography, consult with regulators to determine if Multi-AZ RDS will meet your requirements.

For more details see [Working with Multi-AZ deployments for Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.maz.html).
