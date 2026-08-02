---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_right_storage_solution_optimize_patterns.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF03-BP03 Make decisions based on access patterns and metrics
<a name="perf_right_storage_solution_optimize_patterns"></a>

 Choose storage systems based on your workload's access patterns and configure them by determining how the workload accesses data. Increase storage efficiency by choosing object storage over block storage. Configure the storage options you choose to match your data access patterns.

 How you access data impacts how the storage solution performs. Select the storage solution that aligns best to your access patterns, or consider changing your access patterns to align with the storage solution to maximize performance.

 Creating a RAID 0 array allows you to achieve a higher level of performance for a file system than what you can provision on a single volume. Consider using RAID 0 when I/O performance is more important than fault tolerance. For example, you could use it with a heavily used database where data replication is already set up separately.

 Select appropriate storage metrics for your workload across all of the storage options consumed for the workload. When using filesystems that use burst credits, create alarms to let you know when you are approaching those credit limits. You must create storage dashboards to show the overall workload storage health.

 For storage systems that are a fixed size, such as Amazon EBS or Amazon FSx, ensure that you are monitoring the amount of storage used versus the overall storage size and create automation if possible to increase the storage size when reaching a threshold

 **Common anti-patterns:**
+  You assume that storage performance is adequate if customers are not complaining.
+  You only use one tier of storage, assuming all workloads fit within that tier.

 **Benefits of establishing this best practice:** You need a unified operational view, real-time granular data, and historical reference to optimize performance and resource utilization. You can create automatic dashboards and data with one-second granularity to perform metric math on your data and derive operational and utilization insights for your storage needs.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimize your storage usage and access patterns: Choose storage systems based on your workload's access patterns and the characteristics of the available storage options. Determine the best place to store data that will enable you to meet your requirements while reducing overhead. Use performance optimizations and access patterns when configuring and interacting with data based on the characteristics of your storage (for example, striping volumes or partitioning data).

 Select appropriate metrics for storage options: Ensure that you select the appropriate storage metrics for the workload. Each storage option offers various metrics to track how your workload performs over time. Ensure that you are measuring against any storage burst metrics (for example, monitoring burst credits for Amazon EFS). For storage systems that are fixed sized, such as Amazon Elastic Block Store or Amazon FSx, ensure that you are monitoring the amount of storage used versus the overall storage size. Create automation when possible to increase the storage size when reaching a threshold.

 Monitor metrics: Amazon CloudWatch can collect metrics across the resources in your architecture. You can also collect and publish custom metrics to surface business or derived metrics. Use CloudWatch or third-party solutions to set alarms that indicate when thresholds are breached.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/)
+  [EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
+  [Monitoring and understanding Amazon EBS performance using Amazon CloudWatch](https://aws.amazon.com/blogs/storage/valuable-tips-for-monitoring-and-understanding-amazon-ebs-performance-using-amazon-cloudwatch/)

 **Related videos:**
+  [Deep dive on Amazon EBS (STG303-R1)](https://www.youtube.com/watch?v=wsMWANWNoqQ)
+  [Optimize your storage performance with Amazon S3 (STG343)](https://www.youtube.com/watch?v=54AhwfME6wI)

 **Related examples:**
+  [Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver)
+  [Amazon EBS CSI Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
+  [Amazon EFS Utilities](https://github.com/aws/efs-utils)
+  [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale)
+  [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
