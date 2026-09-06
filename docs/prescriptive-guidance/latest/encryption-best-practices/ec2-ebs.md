---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/ec2-ebs.html
---

# Amazon Elastic Compute Cloud and Amazon Elastic Block Store
<a name="ec2-ebs"></a>

[Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down. [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) provides block-level storage volumes for use with EC2 instances.

Consider the following encryption best practices for these services:
+ Tag all EBS volumes with the appropriate data classification key and value. This helps you determine and implement the appropriate security and encryption requirements, according to your policy.
+ According to your encryption policy and the technical feasibility, configure encryption for data in transit between EC2 instances or between EC2 instances and your on-premises network.
+ Encrypt both the boot and data EBS volumes of an EC2 instance. An encrypted EBS volume protects the following data:
  + Data at rest inside the volume
  + All data moving between the volume and the instance
  + All snapshots created from the volume
  + All volumes created from those snapshots

  For more information, see [How EBS encryption works](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html).
+ Enable encryption by default for EBS volumes for your account in the current AWS Region. This enforces encryption of any new EBS volumes and snapshot copies. It has no effect on existing EBS volumes or snapshots. For more information, see [Enable encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html#encryption-by-default).
+ Encrypt the instance store root volume for an Amazon EC2 instance. This helps you protect configuration files and data stored with the operating system. For more information, see [How to protect data at rest with Amazon EC2 instance store encryption](https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/) (AWS blog post)
+ In AWS Config, implement the [encrypted-volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) rule to automated checks that validate and enforce appropriate encryption configurations.
