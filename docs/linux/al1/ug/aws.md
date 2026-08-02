---
source_url: https://docs.aws.amazon.com/linux/al1/ug/aws.html
---

# Using AL1 on AWS
<a name="aws"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and AL2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

 Because AL1, is now EOL, support for newer instance types and AWS Regions will not be added.

## Repository configuration
<a name="repository-config"></a>

For AL1 and AL2, AMIs are a snapshot of the packages available at the time the AMI was created, with the exception of security updates. Any packages not on the original AMI, but installed at run time, will be the latest version available. To get the latest packages available for AL1, run **yum update -y**.

For AL2023, the repository configuration has changed compared to AL1 and AL2. For more information about the AL2023 repository, see [Managing packages and operating system updates](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html).

Versions up to AL2023 were configured to deliver a continuous flow of updates to roll from one minor version of Amazon Linux to the next version, also called *rolling releases*. As a best practice, we recommend you update your AMI to the latest available AMI. Don't launch Amazon Linux AMIs that use an older version.

In-place upgrades are not supported between major Amazon Linux versions, such as from AL1 to AL2 or from AL2 to AL2023. For more information, see [Amazon Linux availability](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html#amazon-linux-availability).

**Using lock-on-launch in Amazon Linux**
You can disable rolling releases by enabling the *lock-on-launch* feature. The lock-on-launch feature locks your instance to receive updates only from the specified release of the AMI

For example, you can launch a 2017.09 AMI and have it receive only the updates that were released prior to the 2018.03 AMI, until you are ready to migrate to the 2018.03 AMI.

**Important**
If you enable the lock-on-launch feature and choose a version of the repositories that is not the latest, you don't receive further updates. To receive rolling releases, you must use the latest AMI, or consistently update your AMI with the repositories pointed to latest.

To enable the lock-on-launch feature in new instances, launch it with the following user data passed to cloud-init:

```
#cloud-config
repo_releasever: 2017.09
```

**To lock existing instances to their current AMI version**

1. Edit `/etc/yum.conf`.

1. Comment out `releasever=latest`.

1. To clear the cache, run **yum clean all**.
