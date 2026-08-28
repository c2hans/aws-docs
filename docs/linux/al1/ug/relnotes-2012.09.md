---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2012.09.html
---

# Amazon Linux 1 (AL1) version 2012.09 release notes
<a name="relnotes-2012.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2012.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2012.09
<a name="upgrading-2012.09"></a>

Think about migrating to Amazon Linux 1 (AL1) version 2012.09 from earlier versions.

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux AMI versions are released, we encourage users to migrate to the newer versions of the AMI, and to keep their systems updated. In some cases, customers seeking support for an older version of the Amazon Linux AMI through Amazon Premium Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2012.09 from 2012.03, 2011.09 or 2011.02, run `yum update`. When the transaction is complete, reboot your instance.

## New Features
<a name="new-features-2012.09"></a>

### Kernel 3.2.38
<a name="kernel-2012.09"></a>

The Amazon Linux 1 (AL1) version 2012.09.1 point release shipped with kernel version 3.2.38, replacing the 3.2.30 kernel that shipped with the initial Amazon Linux 1 (AL1) version 2012.09.

### Apache 2.4 and PHP 5.4
<a name="apache-php-2012.09"></a>

 This release supports multiple versions of both Apache and PHP, and they are engineered to work together in specific combinations. The first combination is the default, Apache 2.2 in conjunction with PHP 5.3, which are installed by running `yum install httpd php`. Based on customer requests, we support Apache 2.4 in conjunction with PHP 5.4 in the package repositories. These packages are accessed by running `yum install httpd24 php54`.

### OpenJDK 7
<a name="jdk-2012.09"></a>

While OpenJDK 1.6 is still installed by default on the AMI, OpenJDK 1.7 is included in the package repositories, and available for installation. You can install it by running `yum install java-1.7.0-openjdk`.

### R 2.15
<a name="R-2012.09"></a>

Also coming from your requests, we have added the R language to Amazon Linux 1 (AL1). We are here to serve your statistical analysis needs\! Simply `yum install R` and off you go.

### Multiple versions of GCC
<a name="gcc-2012.09"></a>

The default version of GCC that is available in the package repositories is GCC 4.6, which is a change from the 2012.03 AMI in which the default was GCC 4.4 and GCC 4.6 was shipped as an optional package. Furthermore, GCC 4.7 is available in the repositories. If you `yum install gcc` you will get GCC 4.6. For the other versions, either run `yum install gcc44` or `yum install gcc47`.

### Multiple Network Intherfaces and IP Addresses
<a name="network-2012.09"></a>

Additional network interfaces attached while the instance is running will be configured automatically. Secondary IP addresses will be refreshed during DHCP lease renewal, and the related routing rules will be updated. This functionality is provided by the `ec2-net-utils` package, which can be removed if manual control over network configuration is required.

### AWS tools
<a name="aws-tools-2012.09"></a>

We have included updated versions of all the AWS command line tools that are part of Amazon Linux 1 (AL1). See the 2012.09 package list for more details.

### CUDA toolkit 4.2.9
<a name="cuda-2012.09"></a>

The CUDA toolkit version 4.2.9 is available on the Cluster GPU AMI.

### Fresh packages
<a name="fresh-2012.09"></a>

Many of the packages in the AMI have been re-synced to their latest upstream version. For reference, we have produced a list of all source RPMs included in Amazon Linux 1 (AL1) version 2012.09.

## Supported Instance Types
<a name="instance-types-2012.09"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2012.09. [This compatibility table](relnotes-2012.03.md#instance-types-2012.03) shows which 2012.09 AMI flavors launch on each Amazon EC2 instance type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
