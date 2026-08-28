---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/continuing-al2-filesystem.html
---

# `gp3` as default Amazon EBS volume type
<a name="continuing-al2-filesystem"></a>

The AL2023 AMI and AL2 both use the XFS file system on the root file system. For AL2023, the `mkfs`options for the root device file system are further optimized for Amazon EC2. AL2023 also supports a number of other file systems that you can use on other volumes to meet your specific requirements.

AL2023 AMIs use Amazon EBS `gp3` volumes by default, whereas AL2 AMIs use Amazon EBS `gp2` volumes by default. You can change the volume type when you launch an instance.

For more information about Amazon EBS volume types, see [Amazon EBS General Purpose Volumes](https://aws.amazon.com/ebs/general-purpose/).

For more information about launching an Amazon EC2 instance, see [Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
