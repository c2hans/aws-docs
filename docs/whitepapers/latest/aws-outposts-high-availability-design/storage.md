---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/storage.html
---

# Storage
<a name="storage"></a>

 The AWS Outposts rack service provides three storage types:
+  [Instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) on supported EC2 instance types
+  [Amazon Elastic Block Store (EBS) gp2 volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2) for persistent block storage
+  [Amazon Simple Storage Service on Outposts (S3 on Outposts)](https://aws.amazon.com/blogs/aws/amazon-s3-on-outposts-now-available/) for local object storage

 Instance storage is provided on supported servers (`C5d`, `M5d`, `R5d`, `G4dn`, and `I3en`). Just like in the Region, the data in an instance store persists only for the (running) [lifetime of the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html).

 Outposts EBS volumes and S3 on Outposts object storage are provided as part of the AWS Outposts rack managed services. Customers are responsible for capacity management of the Outpost storage pools. Customers specify their storage requirements for EBS and S3 storage when ordering an Outpost. AWS configures the Outpost with the number of storage servers required to provide the requested storage capacity. AWS is responsible for the availability of the EBS and S3 on Outposts storage services. Sufficient storage servers are provisioned to provide highly available storage services to the Outpost. Loss of a single storage server should not disrupt the services nor result in data loss.

 You can use the AWS Management Console and [CloudWatch metrics](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) to monitor Outpost EBS and [S3 on Outposts capacity utilization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsCapacity.html).
