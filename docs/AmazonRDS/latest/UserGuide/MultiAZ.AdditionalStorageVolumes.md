---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MultiAZ.AdditionalStorageVolumes.html
---

# Multi-AZ failover with additional storage volumes
<a name="MultiAZ.AdditionalStorageVolumes"></a>

Multi-AZ deployments support DB instances with additional storage volumes. During a failover, RDS automatically fails over to the standby instance with any additional storage volumes attached to the DB instance. This process ensures data consistency and availability.

When you configure a Multi-AZ deployment for a DB instance with additional storage volumes, Amazon RDS automatically replicates all volumes to the standby instance in a different Availability Zone. The replicated storage includes:
+ The primary storage volume
+ All additional storage volumes attached to your DB instance

During a failover, Amazon RDS promotes the standby instance and ensures that all storage volumes are available and consistent. The failover maintains the same storage configuration, including volume names, storage types, and performance characteristics.

After a successful failover, you can verify that all storage volumes are properly attached and accessible by viewing the storage configuration details. For more information, see [Viewing storage volume details for your DB instance](rds-storage-viewing.md).

The failover time for DB instances with additional storage volumes is similar to DB instances with only primary storage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
