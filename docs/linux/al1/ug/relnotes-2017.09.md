---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2017.09.html
---

# Amazon Linux 1 (AL1) version 2017.09 release notes
<a name="relnotes-2017.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2017.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2017.09
<a name="upgrading-2017.09"></a>

Please upgrade to Amazon Linux 1 (AL1) 2017.09 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2017.09 from 2011.09 or later, run `sudo yum clean all` followed by `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or one already running) to a particular version of the Amazon Linux 1 (AL1) repositories.

As mentioned in last release notes for AMI 2016.09 we have performed additional cleanup, and deprecated the following packages: `gcc44`, `mysql51`, `openssl097`, `php` (`php` 5.3, `php` 5.4, `php` 5.5) , `postgresql8`, `ruby18`, `ruby19`, `ruby21`, `ruby22`, `java-1.6.0-openjdk` and `tomcat6`.

## 2017.09.1 point release
<a name="release-2017.09.1"></a>

Released on November 6th, 2017.

We've updated the base AMI to include kernel 4.9.58 version containing updates for ena 1.4.0, Amazon EC2 P3 instance support, and security updates.

## New Features
<a name="new-2017.09"></a>

### Kernel 4.9.51
<a name="kernel-2017.09"></a>

The Kernel has been updated to latest 4.9.y stable tree, new ENA driver 1.3.0 as well as support for TCP Bottleneck Bandwidth and RTT (BBR) which improve network performance.

BBR is not enabled by default. You can enable it on your Amazon EC2 Instance via:

1.

   ```
   $ sudo modprobe tcp_bbr
   ```

1.

   ```
   $ sudo modprobe sch_fq
   ```

1.

   ```
   $ sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
   ```

Persistent configuration should look like:

1.

   ```
   $ sudo su -
   ```

1.

   ```
   $ cat <<EOF>> /etc/sysconfig/modules/tcpcong.modules
   >#!/bin/bash
   > exec /sbin/modprobe tcp_bbr >/dev/null 2>&1
   > exec /sbin/modprobe sch_fq >/dev/null 2>&1
   > EOF
   ```

1.

   ```
   $ chmod 755 /etc/sysconfig/modules/tcpcong.modules
   ```

1.

   ```
   $ echo "net.ipv4.tcp_congestion_control = bbr" >> /etc/sysctl.d/00-tcpcong.conf
   ```

### Amazon EC2 Systems Manager (SSM Agent)
<a name="ssm-2017.09"></a>

SSM Agent is now installed by default in the base Amazon Linux AMI. The SSM Agent allows you to use RunCommand in order to configure and run scripts on your Amazon EC2 Instances. See Amazon EC2 Systems Manager documentation for more details.

### Fresh Packages
<a name="fresh-2017.09"></a>

Many of our packages have been re-synced to newer upstream versions.

### New Packages
<a name="new-packages-2017.09"></a>

Postgres 9.6, Ruby 2.4, Python 3.6, Mysql 5.7, Tomcat 8.5, Nginx 1.12.1, Squid 3.5, OpenMPI 2.1, GCC 6.4

Python 3.6, the latest in the Python 3.x series, has been integrated with our existing Python experience and is now available in the Amazon Linux 1 (AL1) repositories. This includes the associated `virtualenv` and `pip` packages, which can be used to install and manage dependencies. The default python version for `/usr/bin/python` can be managed via `alternatives`, just like our existing Python packages. Python 3.6 and the associated `pip` and `virtualenv` packages can be installed via `sudo yum install python36 python36-virtualenv python36-pip`.

We've also added the latest in the Ruby 2.x series, Ruby 2.4, to the package repositories. You can install this new Ruby package with `sudo yum install ruby24`.

Amazon Linux 1 (AL1) now uses OpenSSL 1.0.2k. As a result of this improvement, we are happy to announce a much-requested feature: The HTTP/2 protocol is now supported by our `httpd24`, `nginx`, and `curl` packages.

We've integrated newer versions of some of our database offerings into the Amazon Linux 1 (AL1) repositories: Postgres 9.6 and MySQL 5.7 are now available and can be installed via `sudo yum install postgresql96` and `sudo yum install mysql57 respectively`.

Many customers have asked for an updated Squid package. Squid 3.5 is now available in the package repositories.

The Amazon Linux 1 (AL1) version 2017.09 repositories include the Nginx 1.12 release. You can install or upgrade to the latest version with `sudo yum install nginx`.

We've upgraded our Tomcat 8 package to provide Tomcat 8.5. Tomcat 8.5 provides a replacement for Tomcat 8 which has pulled forward many new features from Tomcat 9.0. You can install or upgrade to Tomcat 8.5 with `sudo yum install tomcat8`.

We've added GCC 6.4 to the Amazon Linux 2017.09 package repositories. This package can be installed alongside our existing GCC packages via `sudo yum install gcc64`.

In order to better support HPC workloads, we've updated our OpenMPI package from version 1.6.4 to OpenMPI 2.1.1. As part of this update, we are also providing OpenMPI 1.6.4 compatibility packages in order to allow you to continue building and running your existing OpenMPI applications.

## Known Issues
<a name="known-issues-2017.09"></a>

Since we've moved from tomcat 8 to tomcat 8.5, there may be a few minor backwards incompatibilities.

## Subscribe to Amazon Linux AMI Notifications
<a name="notifications-2017.09"></a>

We'd like to remind you about our SNS topic which can keep you informed of our regular Amazon Linux 1 (AL1) releases. To begin receiving notifications about our new AMI releases, please subscribe from the us-east-1 region to our SNS topic: `arn:aws:sns:us-east-1:137112412989:amazon-linux-ami-updates`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
