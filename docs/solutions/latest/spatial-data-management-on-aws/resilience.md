---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/resilience.html
---

# Resilience
<a name="resilience"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking.

## Disaster Recovery
<a name="disaster-recovery"></a>

 **What the Solution Provides**

The solution includes these built-in data protection features:
+  **DynamoDB Point-in-Time Recovery (PITR)**: Continuous backups with 35-day retention for all metadata tables
+  **S3 Versioning**: Enabled on the asset bucket to protect against accidental deletion and overwrites

 **Recommended Best Practices**

For production deployments, implement these additional backup measures:

1.  **DynamoDB On-Demand Backups**
   + Create on-demand backups before major changes (schema updates, bulk data operations, version upgrades)
   + On-demand backups are retained until explicitly deleted, unlike PITR’s 35-day limit
   + Use AWS Backup to schedule regular DynamoDB backups (daily or weekly)

1.  **S3 Asset Bucket Backups**
   + Configure AWS Backup to create regular backups of the asset bucket
   + Consider S3 Cross-Region Replication (CRR) to a secondary region for regional disaster recovery

1.  **Cross-Account Backup** (for critical data)
   + Copy DynamoDB backups to a separate AWS account for protection against account-level issues
   + Replicate critical S3 assets to a bucket in a different AWS account

For true disaster recovery from regional failures, implement cross-region replication and multi-region deployment.

## High Availability
<a name="high-availability"></a>

 **Multi-AZ Deployment**
+ VPC spans 2 Availability Zones
+ NAT Gateways deployed in both AZs
+ Lambda functions can execute in either AZ
+ DynamoDB and S3 are inherently multi-AZ

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
