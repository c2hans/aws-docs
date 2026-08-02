---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a5.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP04 Minimize over-provisioning in block storage
<a name="sus_sus_data_a5"></a>

 To minimize total provisioned storage, create block storage with size allocations that are appropriate for the workload. Use elastic volumes to expand storage as data grows without having to resize storage attached to compute resources. Regularly review elastic volumes and shrink over-provisioned volumes to fit the current data size.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor the utilization of your data volumes.
+  Use elastic volumes and managed block data services to automate allocation of additional storage as your persistent data grows.
+  Set target levels of utilization for your data volumes, and resize volumes outside of expected ranges.
+  Size read-only volumes to fit the data.
+  Migrate data to object stores to avoid provisioning the excess capacity from fixed volume sizes on block storage.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html)
+  [Amazon FSx Documentation](https://docs.aws.amazon.com/fsx/index.html)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
