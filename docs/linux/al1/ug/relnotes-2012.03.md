---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2012.03.html
---

# Amazon Linux 1 (AL1) version 2012.03 release notes
<a name="relnotes-2012.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2012.03 release.

## Upgrading to Amazon Linux 1 (AL1) version 2012.03
<a name="upgrading-2012.03"></a>

Think about migrating to Amazon Linux 1 (AL1) version 2012.03 from earlier versions.

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the newer versions of the AMI, and to keep their systems updated. In some cases, customers seeking support for an older version of the Amazon Linux 1 (AL1) through Amazon Premium Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2012.03 from 2011.09 or 2011.02, run `yum update`. When the transaction is complete, reboot your instance.

## New Features
<a name="new-features-2012.03"></a>

### AWS tools
<a name="aws-tools-2012.03"></a>

We have included updated versions of all the AWS command line tools that are part of Amazon Linux 1 (AL1). See the 2012.03 package list for more details.

### Tomcat 7
<a name="tomcat-2012.03"></a>

Support is included for both Tomcat 6 and Tomcat 7. Both are included in the package repository, and can be installed via `yum install tomcat6` or `yum install tomcat7`.

### MySQL 5.5
<a name="mysql-2012.03"></a>

New Amazon Linux 1 (AL1) version 2012.03 users who `yum install mysql` (or `yum install mysql55`) will get MySQL 5.5 by default, unless they explicitly choose to install the older MySQL 5.1. Users upgrading via yum from Amazon Linux AMI 2011.09 instances with the older MySQL 5.1 installed will stay with MySQL 5.1, which is still available as `mysql51` in the package repository.

### PostgreSQL 9
<a name="postgresql-2012.03"></a>

Similar to MySQL, new Amazon Linux 1 (AL1) version 2012.03 users who `yum install postgresql` (or `yum install postgresql9`) will get PostgreSQL 9 by default, unless they explicitly choose to install the older PostgreSQL 8. Users upgrading via `yum` from Amazon Linux 1 (AL1) version 2011.09 instances with the older PostgreSQL 8.4.x installed will stay with PostgreSQL 8, which is still available as `postgresql8` in the package repository.

### Kernel 3.2
<a name="kernel-2012.03"></a>

The Amazon Linux 1 (AL1) version 2012.03.3 point release shipped with kernel version 3.2.21, replacing the 3.2.12 kernel that shipped with the initial Amazon Linux 1 (AL1) version 2012.03.

### GCC 4.6
<a name="gcc-2012.03"></a>

While GCC 4.4.6 remains the default, we have included GCC 4.6.2, specifically for use on EC2 instances that support AVX. Run yum install gcc46 in order to get the packages. GCC 4.6 enables Amazon Linux 1 (AL1) to take advantage of the AVX support available on `cc2.8xlarge` instance types.

### Python 2.7
<a name="python-2012.03"></a>

While Python 2.6 is still the default, users can `yum install python27`.

### Ruby 1.9.3
<a name="ruby-2012.03"></a>

While Ruby 1.8.7 is still the default, users can `yum install ruby19`.

### CUDA toolkit 4.1
<a name="cuda-2012.03"></a>

The CUDA toolkit version 4.1 is available on the GPU-enabled HVM AMI (in us-east-1).

### Fresh Packages
<a name="fresh-2012.03"></a>

Many of the packages in the AMI have been re-synced to their latest upstream version. For reference, we have produced a list of all source RPMs included in Amazon Linux 1 (AL1) version 2012.03.

### Supported Instance Types
<a name="instance-types-2012.03"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2012.03. This compatibility table shows which 2012.03 AMI flavors launch on each Amazon EC2 instance type.

| Instance Type | EBS-Backed 32-bit | EBS-Backed 64-bit | Instance Store 32-bit | Instance Store 64-bit | Cluster Compute EBS-Backed 64-bit | Cluster GPU EBS-Backed 64-bit |
| --- | --- | --- | --- | --- | --- | --- |
| t1.micro | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |  |
| m1.small | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m1.medium | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m1.large |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m1.xlarge |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| c1.medium | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| c1.xlarge |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m2.xlarge |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m2.2xlarge |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| m2.4xlarge |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| cc1.4xlarge |  |  |  |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| cc2.8xlarge |  |  |  |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |
| cg1.4xlarge |  |  |  |  |  | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |

### Frequently Asked Terms
<a name="faq-2011.09"></a>

The Amazon Linux 1 (AL1) FAQs is updated with both general and technical topics.

**What steps do I take to upgrade from PostgreSQL 9.1 to 9.2?**
 Please note that you can avoid this issue entirely by running the latest Amazon Linux AMI, on which PostgreSQL 9.2 is the default.
PostgreSQL 9.2 offers important new features and performance improvements and it has been included in Amazon Linux 1 (AL1) version 2012.09 release based on customer requests.
After upgrading PostgreSQL from 9.1 to 9.2, the database service will no longer start. This happens because the 9.1 version of the database format is not immediately usable with the 9.2 server. We have provided the `postgresql-upgrade` package as an automatic install alongside the latest release of postgresql 9.2. This allows you to perform an in-place upgrade on your database using service postgresql upgrade.
Behind the scenes, this runs `pg_upgrade` to migrate your database to the new format. Note that the upgrade will reset configuration files such as `pg_hba.conf` to a clean state. Your old configuration files are stored in `/var/lib/pgsql9/data-old`, and can be copied over the default files in `/var/lib/pgsql9/data` after your review.
Once the upgrade is finished and the configuration files are restored, the service should start normally.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
