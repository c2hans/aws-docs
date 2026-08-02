---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/continuing-al2-filesystem.html
---

# `gp3` as default Amazon EBS volume type
<a name="continuing-al2-filesystem"></a>

The AL2023 AMI and AL2 both use the XFS file system on the root file system. For AL2023, the `mkfs`options for the root device file system are further optimized for Amazon EC2. AL2023 also supports a number of other file systems that you can use on other volumes to meet your specific requirements.

AL2023 AMIs use Amazon EBS `gp3` volumes by default, whereas AL2 AMIs use Amazon EBS `gp2` volumes by default. You can change the volume type when you launch an instance.

For more information about Amazon EBS volume types, see [Amazon EBS General Purpose Volumes](https://aws.amazon.com//ebs/general-purpose/).

For more information about launching an Amazon EC2 instance, see [Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) in the *Amazon EC2 User Guide*.
