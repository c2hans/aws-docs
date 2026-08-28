---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2014.09.html
---

# AL1 version 2014.09 release notes
<a name="relnotes-2014.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2014.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2014.09
<a name="upgrading-2014.09"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2014.09 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux AMI 2014.09 from 2011.09 or later, run `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or already running) to a particular version of the Amazon Linux 1 (AL1) repositories.

## 2014.09.2 point release
<a name="release-2014.09.2"></a>

Released on January 29, 2015

We've updated the base AMI to include all bugfix and security updates that have been pushed to our repositories since the 2014.09.1 release. This includes the "ghost" patches.

## 2014.09.1 point release
<a name="release-2014.09.1"></a>

Released on October 14, 2014

We've updated the base AMI to include all bugfix and security updates that have been pushed to our repositories since the initial 2014.09 release. This includes the "shellshock" patches.

## New features
<a name="new-features-2014.09"></a>

### New AMI flavors since our last major release
<a name="ami-2014.09"></a>

We introduced GP2-by-default AMIs as part of our 2014.03.2 release, and they are included in our 2014.09 release.

### Kernel 3.14
<a name="kernel-2014.09"></a>

Having spent the past release tracking the 3.10 kernel series, for this release we have moved the kernel to version 3.14.19, which is the most recent long-term stable release kernel.

Additionally, instances running the HVM AMIs will now restart 30 seconds after a kernel panic, instead of hanging indefinitely.

Customers who depend on the previous HVM AMI behavior to remove faulty hosts from their fleet can adjust the kernel.panic setting by creating a new file `/etc/sysctl.d/99-override.conf` with `kernel.panic=0` as the contents.

PV AMIs have always restarted on kernel panic.

### Ruby 2.1
<a name="ruby-2014.09"></a>

While Ruby 2.0 remains our default Ruby interpreter, we have added `ruby21` packages to this Amazon Linux 1 (AL1) release.

Also, we have updated all of our versions of Ruby to newer upstream patch levels:
+ ruby18-1.8.7.374
+ ruby19-1.9.3.547
+ ruby20-2.0.0.481
+ ruby21-2.1.2

### Java 8
<a name="java-2014.09"></a>

While Java 7 is still the default on the AMI, OpenJDK 1.8 is included in the repositories with the `java-1.8.0-openjdk` package name.

### Tomcat 8
<a name="tomcat-2014.09"></a>

Based on customer requests, we have added tomcat8 to the Amazon Linux 1 (AL1) repositories.

Also, we have updated all of our versions of Tomcat to the most recent upstream releases:
+ tomcat6-6.0.41
+ tomcat7-7.0.55
+ tomcat8-8.0.12

### PostgreSQL 9.3
<a name="postgresql-2014.09"></a>

Numerous customers have asked for PostgreSQL 9.3, and it is now available in our Amazon Linux 1 (AL1) repositories as a separate package from PostgreSQL 9.2.

PostgreSQL 9.3 is specifically named `postgresql93` and the 2014.09 release of Amazon Linux 1 (AL1) includes PostgreSQL 9.3.5.

Running `yum install postgresql9` or `yum install postgresql92` will still install PostgreSQL 9.2.

### Docker 1.2
<a name="docker-2014.09"></a>

After a truly spectacular number of customer requests, we introduced Docker in the 2014.03 release of Amazon Linux 1 (AL1). With this release, we continue to track upstream development closely.

### nginx 1.6
<a name="nginx-2014.09"></a>

Also based on customer requests, this release of Amazon Linux 1 (AL1) comes with Nginx 1.6.1.

### git 2
<a name="git-2014.09"></a>

With the 2014.09 release of Amazon Linux 1 (AL1), we've moved from Git 1.8 to Git 2.1. Users upgrading from older releases will move directly from the older git to the newer.

### PHP updates
<a name="php-2014.09"></a>

We have updated all of our PHP packages to newer upstream versions:
+ php-5.3.29
+ php54-5.4.32
+ php55-5.5.17

## New Packages
<a name="new-packages-2014.09"></a>

In addition to the features above, here are some other new packages added to our repositories, based on customer requests:
+ clamav-0.98.4
+ cowsay-3.03
+ llvm-3.5.0
+ ncdu-1.10
+ robotfindskitten-2.7182818.701
+ shorewall-4.5.4
+ stress-1.0.4
+ Lots and lots of perl modules

## Fresh Packages
<a name="fresh-packages-2014.09"></a>

Many of our packages have been re-synced to their latest upstream version.

Some of the more popular package updates are:
+ 389-ds-base-1.3.2.23
+ curl-7.38.0
+ gcc48-4.8.2
+ glibc-2.17
+ gnupg-1.4.18
+ gnupg2-2.0.24
+ httpd-2.2.29
+ httpd24-2.4.10
+ java-1.6.0-openjdk-1.6.0.0-67
+ java-1.7.0-openjdk-1.7.0.65
+ java-1.8.0-openjdk-1.8.0.20
+ jq-1.4
+ lighttpd-1.4.35
+ lua-5.1.4
+ mysql51-5.1.73
+ mysql55-5.5.39
+ openssh-6.2p2
+ openssl-1.0.1i
+ perl-5.16.3
+ php-5.3.29
+ php54-5.4.32
+ php55-5.5.17
+ pngcrush-1.7.70
+ postgresql8-8.4.20
+ postgresql92-9.2.9
+ postgresql93-9.3.5
+ R-3.1.1
+ rpm-4.11.2
+ ruby18-1.8.7.374
+ ruby19-1.9.3.547
+ ruby20-2.0.0.481
+ ruby21-2.1.2
+ spamassassin-3.4.0
+ subversion-1.8.8
+ tomcat6-6.0.41
+ tomcat7-7.0.55
+ tomcat8-8.0.12
+ wireshark-1.8.10

## AWS tools
<a name="aws-tools-2014.09"></a>

We have included updated versions of many AWS command line tools. If there is an additional AWS tool that you would like, please call it out\!
+ aws-cli-1.4.4
+ python-boto-2.32.1
+ aws-amitools-ec2-1.5.3
+ aws-apitools-as-1.0.61.6
+ aws-apitools-cfn-1.0.12
+ aws-apitools-ec2-1.7.1.1
+ aws-apitools-elb-1.0.35.0
+ aws-apitools-iam-1.5.0
+ aws-apitools-mon-1.0.20.0
+ aws-apitools-rds-1.15.001
+ aws-cfn-bootstrap-1.4
+ aws-scripts-ses-2014.05.14

## Discontinued packages
<a name="discontinued-packages-2014.09"></a>

We have discontinued support for Python 2.4, GCC 4.6, and GCC 4.7 in this Amazon Linux 1 (AL1) release.

## Supported Instance Types
<a name="instance-types-2014.09"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2014.09. [This compatibility table](relnotes-2012.03.md#instance-types-2012.03) shows which 2014.09 AMIs launch on each Amazon EC2 instance type.

## Looking ahead to our 2015.03 release
<a name="upcoming-in-2015.03"></a>

We are planning on deprecating several of our AMI flavors with the 2015.03 release, as follows:
+ We will no longer produce new 32-bit Amazon Linux AMIs.
+ We will no longer produce new "gpu" AMIs for the CG1 instance type. We recommend that customers migrate to the G2 instance type and the "graphics" AMI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
