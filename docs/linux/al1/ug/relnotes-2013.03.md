---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2013.03.html
---

# Amazon Linux 1 (AL1) version 2013.03 release notes
<a name="relnotes-2013.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2013.03 release.

## Upgrading to Amazon Linux 1 (AL1) version 2013.03
<a name="upgrading-2013.03"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2013.03.1 from earlier versions.

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the newer versions of the AMI, and to keep their systems updated. In some cases, customers seeking support for an older version of Amazon Linux 1 (AL1) through Amazon Premium Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2013.03.1 from 2011.09 or later, run `yum update`. When the upgrade is complete, reboot your instance.

## New Features
<a name="new-features-2013.03"></a>

### Kernel 3.4.43
<a name="kernel-2013.03"></a>

We have upgraded the kernel to version 3.4.43 which is part of the long-term stable release 3.4 kernel series. This replaces the 3.4.37 kernel that shipped with the initial Amazon Linux 1 (AL1) version 2013.03.

### OpenSSH 6.1
<a name="openssh-2013.03"></a>

In response to customer requests, we have moved to OpenSSH 6.1 for this release of Amazon Linux 1 (AL1). This enables the configuration option of `AuthenticationMethods` for requiring multi-factor authentication.

### OpenSSL 1.0.1
<a name="openssl-2013.03"></a>

Also based on customer requests, we have updated OpenSSL to 1.0.1.

### New AWS command line tools
<a name="aws-cli-2013.03"></a>

We are excited to include the Developer Preview of the new AWS Command Line Interface. The `aws-cli` tool is written in Python, and provides a one-stop-shop for controlling multiple AWS services through the command line.

### New and updated packages
<a name="new-updated-2013.03"></a>

Many of the packages in the AMI have been re-synced to their latest upstream version. For reference, we have produced a list of all source RPMs included in Amazon Linux 1 (AL1) version 2013.03. Here are some noteworthy additions and updates since the 2012.09.0 release of Amazon Linux 1 (AL1):
+ Boost 1.41 and 1.53
+ Boto 2.8.0
+ Cython 0.18 (New)
+ Ganglia 3.3.7 (New)
+ Git 1.8.1
+ HAProxy 1.4.22 (New)
+ Heartbeat 3.0.4 (New)
+ MySQL 5.1.67 and 5.5.30
+ Nagios 3.4.4
+ Nginx 1.2.7
+ PHP 5.3.20 and 5.4.11
+ PngCrush 1.7.43 (New)
+ PostgreSQL 8.4.13 and 9.2.3
+ Puppet 2.7.18
+ Tomcat 6.0.36 and 7.0.37

## Supported Instance Types
<a name="instance-types-2013.03"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2012.09. [This compatibility table](relnotes-2012.03.md#instance-types-2012.03) shows which 2012.09 AMI flavors launch on each Amazon EC2 instance type.
