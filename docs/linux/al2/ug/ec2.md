---
source_url: https://docs.aws.amazon.com/linux/al2/ug/ec2.html
---

# AL2 on Amazon EC2
<a name="ec2"></a>

**Note**
 AL2 is no longer the current version of Amazon Linux. AL2023 is the successor to AL2. For more information, see [Comparing AL2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html) in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

**Topics**
+ [Launch Amazon EC2 instance with AL2 AMI](#launch-ec2-instance)
+ [Find the latest AL2 AMI using Systems Manager](#find-latest-al2-using-systems-manager)
+ [Connect to an Amazon EC2 instance](#connect-to-amazon-linux-limits-ec2)
+ [AL2 AMI boot mode](#default-boot-mode-al2)
+ [Package repository](#package-repository)
+ [Using cloud-init on AL2](amazon-linux-cloud-init.md)
+ [Configure AL2 instances](configure-ec2-instance.md)
+ [User provided kernels](UserProvidedKernels.md)
+ [AL2 AMI release notifications](linux-ami-notifications.md)
+ [Configure the AL2 MATE desktop connection](amazon-linux-ami-mate.md)
+ [AL2 Tutorials](al2-tutorials.md)

## Launch Amazon EC2 instance with AL2 AMI
<a name="launch-ec2-instance"></a>

You can launch an Amazon EC2 instance with the AL2 AMI. For more information, see [Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance).

## Find the latest AL2 AMI using Systems Manager
<a name="find-latest-al2-using-systems-manager"></a>

Amazon EC2 provides AWS Systems Manager public parameters for public AMIs maintained by AWS that you can use when launching instances. For example, the EC2-provided parameter `/aws/service/ami-amazon-linux-latest/amzn2-ami-kernel-default-hvm-x86_64-gp2` is available in all Regions and always points to the latest version of the AL2 AMI in a given Region.

To find the latest AL2023 AMI using AWS Systems Manager, see [Get started with AL2023](https://docs.aws.amazon.com/linux/al2023/ug/get-started.html).

The Amazon EC2 AMI public parameters are available from the following path:

`/aws/service/ami-amazon-linux-latest`

You can view a list of all Amazon Linux AMIs in the current AWS Region by running the following AWS CLI command.

```
aws ssm get-parameters-by-path --path /aws/service/ami-amazon-linux-latest --query "Parameters[].Name"
```

**To launch an instance using a public parameter**
The following example uses the EC2-provided public parameter to launch an `m5.xlarge` instance using the latest AL2 AMI.

To specify the parameter in the command, use the following syntax: `resolve:ssm:{{public-parameter}}`, where `resolve:ssm` is the standard prefix and `public-parameter` is the path and name of the public parameter.

In this example, the `--count` and `--security-group` parameters are not included. For `--count`, the default is 1. If you have a default VPC and a default security group, they are used.

```
aws ec2 run-instances
    --image-id resolve:ssm:{{/aws/service/ami-amazon-linux-latest/amzn2-ami-kernel-default-hvm-x86_64-gp2}}
    --instance-type {{m5.xlarge}}
    --key-name {{MyKeyPair}}
```

For more information, see [Using public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters.html) in the *AWS Systems Manager User Guide*.

**Understanding Amazon Linux 2 AMI names**
Amazon Linux 2 AMI names use the following naming scheme:

`amzn2-ami-[minimal-][kernel-{5.10,default,4.14}]-hvm-{x86_64,aarch64}-{ebs,gp2}`
+ **Minimal** AMIs come with a minimized set of pre-installed packages to reduce image size.
+ **kernel-VERSION** determines the kernel version that is pre-installed on the respective AMI:
  + `kernel-5.10` selects Linux kernel version 5.10. *This is the recommended kernel version for AL2.*
  + `kernel-default` selects the recommended default kernel for AL2. It is an alias for kernel-5.10.
  + `kernel-4.14` selects Linux kernel version 4.14. *This is only provided for compatibility with older AMI releases. Do not use this version for new instance launches. Expect this AMI to become unsupported.*
  + A special set of AMI names exists without reference to a specific kernel. These AMIs are an alias for kernel-4.14.*These AMIs are only provided for compatibility with older AMI releases. Do not use this AMI name for new instance launches. Expect the kernel for these AMIs to be updated.*
+ **x86\_64/aarch64** determines the CPU platform to run the AMI on. Select x86\_64 for Intel and AMD based EC2 instances. Select aarch64 for EC2 Graviton instances.
+ **ebs/gp2** determines the EBS volume type used to serve the respective AMI. See [EBS Volume Types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) for reference. *Always select gp2.*

## Connect to an Amazon EC2 instance
<a name="connect-to-amazon-linux-limits-ec2"></a>

There are several ways to connect to your Amazon Linux instance, including SSH, AWS Systems Manager Session Manager, and EC2 Instance Connect. For more information, see [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.

**SSH users and **sudo****
Amazon Linux does not allow remote `root` secure shell (SSH) by default. Also, password authentication is disabled to prevent brute force attacks. To enable SSH logins to an Amazon Linux instance, you must provide your key pair to the instance at launch. You must also set the security group used to launch your instance to allow SSH access. By default, the only account that can log in remotely using SSH is `ec2-user`. This account also has **sudo** privileges. If you enable remote `root` login, be aware that it is less secure than relying on key pairs and a secondary user.

## AL2 AMI boot mode
<a name="default-boot-mode-al2"></a>

AL2 AMIs don't have a boot mode parameter set. Instances launched from AL2 AMIs follow the default boot mode value of the instance type. For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide*.

## Package repository
<a name="package-repository"></a>

This information applies to AL2. For information about AL2023, see [Manage packages and operating system updates in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html) in the *Amazon Linux 2023 User Guide*.

AL2 and AL1 are designed to be used with online package repositories hosted in each Amazon EC2 AWS Region. The repositories are available in all Regions and are accessed using **yum** update tools. Hosting repositories in each Region enables us to deploy updates quickly and without any data transfer charges.

**Important**
The last version of AL1 reached EOL on December 31, 2023 and will not receive any security updates or bug fixes starting January 1, 2024. For more information, see [Amazon Linux AMI end-of-life](https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/).

If you don't need to preserve data or customizations for your instances, you can launch new instances using the current AL2 AMI. If you do need to preserve data or customizations for your instances, you can maintain those instances through the Amazon Linux package repositories. These repositories contain all the updated packages. You can choose to apply these updates to your running instances. Earlier versions of the AMI and update packages continue to be available for use, even as new versions are released.

**Note**
To update and install packages without internet access on an Amazon EC2 instance, see [How can I update yum or install packages without internet access on my Amazon EC2 instances running AL1, AL2, or AL2023?](https://repost.aws/knowledge-center/ec2-al1-al2-update-yum-without-internet)

To install packages, use the following command:

```
[ec2-user ~]$ sudo yum install {{package}}
```

If you find that Amazon Linux doesn't contain an application that you need, you can install the application directly on your Amazon Linux instance. Amazon Linux uses RPMs and yum for package management, and that is likely the most direct way to install new applications. You should check to see if an application is available in our central Amazon Linux repository first, because many applications are available there. From there, you can add these applications to your Amazon Linux instance.

To upload your applications onto a running Amazon Linux instance, use **scp** or **sftp** and then configure the application by logging in to your instance. Your applications can also be uploaded during the instance launch by using the **PACKAGE\_SETUP** action from the built-in cloud-init package. For more information, see [Using cloud-init on AL2](amazon-linux-cloud-init.md).

### Security updates
<a name="security-updates"></a>

Security updates are provided using the package repositories. Both security updates and updated AMI security alerts are published in the [Amazon Linux Security Center](https://alas.aws.amazon.com). For more information about AWS security policies or to report a security problem, see [AWS Cloud Security](https://aws.amazon.com/security/).

AL1 and AL2 are configured to download and install critical or important security updates at launch time. Kernel updates are not included in this configuration.

In AL2023, this configuration has changed compared to AL1 and AL2. For more information about security updates for AL2023, see [Security updates and features](https://docs.aws.amazon.com/linux/al2023/ug/security-features.html) in the *Amazon Linux 2023 User Guide*.

We recommend that you make the necessary updates for your use case after launch. For example, you might want to apply all updates (not just security updates) at launch, or evaluate each update and apply only the ones applicable to your system. This is controlled using the following cloud-init setting: `repo_upgrade`. The following snippet of cloud-init configuration shows how you can change the settings in the user data text you pass to your instance initialization:

```
#cloud-config
repo_upgrade: security
```

 The possible values for `repo_upgrade` are as follows:

`critical`
Apply outstanding critical security updates.

`important`
Apply outstanding critical and important security updates.

`medium`
Apply outstanding critical, important, and medium security updates.

`low`
Apply all outstanding security updates, including low-severity security updates.

`security`
Apply outstanding critical or important updates that Amazon marks as security updates.

`bugfix`
Apply updates that Amazon marks as bug fixes. Bug fixes are a larger set of updates, which include security updates and fixes for various other minor bugs.

`all`
Apply all applicable available updates, regardless of their classification.

`none`
Don't apply any updates to the instance on start up.

**Note**
Amazon Linux does not mark any updates as `bugfix`. To apply non-security related updates from Amazon Linux use `repo_upgrade: all`.

The default setting for `repo_upgrade` is security. That is, if you don't specify a different value in your user data, by default, Amazon Linux performs the security upgrades at launch for any packages installed at that time. Amazon Linux also notifies you of any updates to the installed packages by listing the number of available updates upon login using the `/etc/motd` file. To install these updates, you need to run **sudo yum upgrade** on the instance.

### Repository configuration
<a name="repository-config"></a>

For AL1 and AL2, AMIs are a snapshot of the packages available at the time the AMI was created, with the exception of security updates. Any packages not on the original AMI, but installed at runtime, will be the latest version available. To get the latest packages available for AL2, run **yum update -y**.

**Troubleshooting tip**
If you get a `cannot allocate memory` error running **yum update** on nano instance types, such as `t3.nano`, you might need to allocate swap space to enable the update.

For AL2023, the repository configuration has changed compared to AL1 and AL2. For more information about the AL2023 repository, see [Managing packages and operating system updates](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html).

Versions up to AL2023 were configured to deliver a continuous flow of updates to roll from one minor version of Amazon Linux to the next version, also called *rolling releases*. As a best practice, we recommend you update your AMI to the latest available AMI rather than launching old AMIs and applying updates.

In-place upgrades are not supported between major Amazon Linux versions, such as from AL1 to AL2 or from AL2 to AL2023. For more information, see [Amazon Linux availability](what-is-amazon-linux.md#amazon-linux-availability).
