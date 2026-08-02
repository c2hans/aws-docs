---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-08.html
---

# WKLD.08 Encrypt Amazon EBS volumes
<a name="wkld-08"></a>

Verify that encryption by default is enabled for Amazon Elastic Block Store (Amazon EBS) volumes in your AWS account. Enabling encryption by default ensures that new Amazon EBS volumes and snapshots are encrypted automatically, removing the need to configure encryption for each volume individually. Encrypted volumes have the same input/output operations per second (IOPS) performance as unencrypted volumes with a minimal effect on latency. For more information, see [Must-know best practices for Amazon EBS encryption](https://aws.amazon.com/blogs/storage/must-know-best-practices-for-amazon-ebs-encryption/) on the AWS Compute Blog.

To enable encryption by default for Amazon EBS volumes, see [Enable encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) in the Amazon EBS documentation. Enabling encryption by default does not encrypt existing unencrypted volumes. To encrypt an existing unencrypted Amazon EBS volume, create an encrypted snapshot copy of the volume and then create a new encrypted volume from that snapshot. For step-by-step instructions, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html) in the Amazon EBS documentation.

**Note**
Encrypting Amazon EBS volumes with an AWS managed AWS KMS key is available at no additional charge. Customer managed keys incur a monthly charge per key and a charge per API call. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).
