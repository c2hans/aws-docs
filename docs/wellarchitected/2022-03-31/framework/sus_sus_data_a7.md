---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a7.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP06 Use shared file systems or object storage to access common data
<a name="sus_sus_data_a7"></a>

 Adopt shared storage and single sources of truth to avoid data duplication and reduce the total storage requirements of your workload. Fetch data from shared storage only as needed. Detach unused volumes to make more resources available.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Migrate data to shared storage when the data has multiple consumers.
+  Fetch data from shared storage only as needed.
+  Delete data as appropriate for your usage patterns, and implement time-to-live (TTL) functionality to manage cached data.
+  Detach volumes from clients that are not actively using them.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon FSx](https://aws.amazon.com/fsx/)
+  [Caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Strategies.html)
+  [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
+  [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
