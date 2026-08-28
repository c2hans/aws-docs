---
source_url: https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html
---

# Mounting EFS file systems
<a name="mounting-fs"></a>

To mount EFS file systems, we recommend that you use the EFS mount helper. The EFS mount helper helps you mount your EFS file systems on EC2 Linux and Mac instances running the supported distributions. The mount helper is part of the open-source collection of tools that is installed when you install the Amazon EFS client (`amazon-efs-utils`). For more information about the Amazon EFS client and the supported distributions, see [Installing the Amazon EFS client](using-amazon-efs-utils.md).

Alternatively, you can manually mount EFS file systems using the standard Linux NFS client. Amazon EFS supports the Network File System versions 4.0 and 4.1 (NFSv4) protocols when mounting your file systems on Amazon EC2 instances.

Additionally, you can use the EFS mount helper or NFS to configure an EC2 instance to automatically mount an EFS file system when the instance starts.

**Topics**
+ [Mounting considerations for Linux](mounting-fs-mount-cmd-general.md)
+ [Mounting EFS file systems using the EFS mount helper](efs-mount-helper.md)
+ [Using Network File System to mount EFS file systems](mounting-fs-old.md)
+ [Automatically mounting EFS file systems](mount-fs-auto-mount-onreboot.md)
+ [Unmounting file systems](unmounting-fs.md)
+ [Tutorial: Create an EFS file system and mount it on an EC2 instance using the AWS CLI](wt1-getting-started.md)
+ [Tutorial: Mounting with on-premises Linux clients](mounting-fs-mount-helper-direct.md)
+ [Tutorial: Mount a file system from a different VPC](efs-different-vpc.md)
+ [Troubleshooting mount issues](troubleshooting-efs-mounting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
