---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP02 Use technologies that support data access and storage patterns
<a name="sus_sus_data_a3"></a>

 Use storage that best supports how your data is accessed and stored to minimize the resources provisioned while supporting your workload. For example, Solid State Devices (SSDs) are more energy intensive than magnetic drives and should be used only for active data use cases. Use energy-efficient, archival-class storage for infrequently accessed data.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor your data access patterns.
+  Migrate data to the appropriate technology based on access pattern.
+  Migrate archival data to storage designed for that purpose.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
+  [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
+  [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
+  [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [What is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)

 **Related videos:**
+  [Architectural Patterns for Data Lakes on AWS](https://www.youtube.com/watch?v=XpTly4XHmqc&ab_channel=AWSEvents)
