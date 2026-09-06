---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2013.09.html
---

# Amazon Linux 1 (AL1) version 2013.09 release notes
<a name="relnotes-2013.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2013.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2013.09
<a name="upgrading-2013.09"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2013.09 from earlier versions.

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the newer versions of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of the Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2013.09 from 2011.09 or later, run `yum update`. When the upgrade is complete, reboot your instance.

## 2013.09.2 point release
<a name="new-features-2013.09.2"></a>

This 2013.09.2 point release of Amazon Linux 1 (AL1) version 2013.09 was released on December 12, 2013.

We added support for the I2 instance family.

We updated base AMI images to include all bugfix and security updates that were pushed to our repositories since the 2013.09.1 release.

## 2013.09.1 point release
<a name="new-features-2013.09.1"></a>

Released on November 11, 2013

With the 2013.09.1 point release, we have added the following new features:
+ Support for the enhanced networking features that were part of the C3 instance type launch.
+ An Instance Store (S3) HVM AMI is now available. The AMI IDs are on our detail page.
+ As part of the G2 instance type launch, an Amazon Linux 1 (AL1) AMI with NVIDIA GRID GPU is available. This should not be confused with the pre-existing GPU-enabled Amazon Linux 1 (AL1) AMI that has previously been available (and still is) for the CG1 instance type.
+ Based on customer requests, PHP 5.5 is now available in the Amazon Linux 1 (AL1) repositories as the `php55` package.
+ We have updated base AMI images, including all bugfix and security updates that had been pushed to our repositories in the weeks since the initial 2013.09 release.

## New Features
<a name="new-features-2013.09"></a>

### Kernel 3.4.68
<a name="kernel-2013.09"></a>

We have upgraded the kernel to version 3.4.68 which is part of the long-term stable release 3.4 kernel series.

### AWS CLI 1.1
<a name="aws-cli-2013.09"></a>

The AWS Command Line Interface has celebrated its GA release in the interval since we included the Developer Preview version in the 2013.03 release of Amazon Linux 1 (AL1). We provide the latest version of this python-based interface to AWS, including command-line completion for bash and zsh.

### GPT partitioning on HVM AMIs
<a name="gpt-2013.09"></a>

The root device of the Amazon Linux HVM AMI is now partitioned using the GPT format, where previous releases used the MBR format. The partition table can be manipulated by GPT-aware tools such as `parted` and `gdisk`.

### Ruby 1.9
<a name="ruby-2013.09"></a>

We've improved the Ruby 1.9 experience on Amazon Linux 1 (AL1) by updating to the latest patch level (448). Our Ruby 1.9 packages fix several other bugs, including a load issue with rake and a fixed bigdecimal so that Ruby on Rails is easier to install.

Ruby now has alternatives support in Amazon Linux 1 (AL1). You can switch between Ruby 1.8 and 1.9 with one command. To use Ruby 1.9, for example (as root):

```
$ yum install ruby19
     $ alternatives --set ruby /usr/bin/ruby1.9
```

To pick the Ruby version interactively:

```
$ alternatives --config ruby
```

We expect Ruby 2.0 to land in our Amazon Linux 1 (AL1) "preview" repository in advance of our 2014.03 release.

### nginx 1.4.2
<a name="nginx-2013.09"></a>

With this release, we have upgraded to Nginx 1.4.2, based on numerous customer requests. This replaces the 1.2.x Nginx packages that we had previously in Amazon Linux 1 (AL1). The upstream release notes detail the changes between 1.2 and 1.4.

### `rpm` 4.11.1 and `yum` 3.4.3
<a name="rpm-yum-2013.09"></a>

The core components of RPM and Yum have been updated to newer versions, with RPM 4.11 and Yum 3.4.3 being featured in this release. Both of these updates provide numerous bug fixes, performance improvements, and new features. The upstream release notes have a plethora of additional information:
+ [RPM 4.11.0](http://rpm.org/wiki/Releases/4.11.0)
+ [RPM 4.11.1](http://rpm.org/wiki/Releases/4.11.1)
+ Yum 3.4.0
+ Yum 3.4.1
+ Yum 3.4.2
+ Yum 3.4.3

These updates should not impact your upgrade path if you are moving from previous versions of Amazon Linux 1 (AL1) via a `yum update`.

### R 3.0
<a name="R-2013.09"></a>

Coming off of its major release earlier this year, we have upgraded R to 3.0.1.

### OpenSSH 6.2
<a name="openssh-2013.09"></a>

We moved to OpenSSH 6 in our 2013.03 release due to customer requests. We continue to follow the 6.x upstream here, with OpenSSH 6.2 in the 2013.09 release.

### No 32-bit packages on 64-bit AMIs
<a name="x86-2013.09"></a>

The 64-bit Amazon Linux AMIs no longer contain 32-bit libraries or executables. This could result in an errors when trying to use a 32-bit application on a 64-bit instance, such as: `bash: my-app: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory`

The yum package manager will still install 32-bit dependencies as required by other packages you install. You can also install them yourself, for example (as root): `yum install glibc.i?86`

### New Packages
<a name="new-packages-2013.09"></a>

We add new packages to Amazon Linux 1 (AL1) based on customer requests, such as:
+ collectl-3.6.7
+ fail2ban-0.8.10
+ htop-1.0.1
+ libjpeg-turbo-1.2.1
+ libpagemap-0.0.1
+ libpuzzle-0.11
+ mod\_geoip-1.2.7
+ most-5.0.0
+ php-libpuzzle-0.11
+ python-inotify-0.9.1
+ python-oauth2-1.5.211
+ pyxattr-0.5.0
+ rssh-2.3.4
+ sip-4.14.6

Please continue to let us know whenever there are new packages that you would like in the Amazon Linux AMI repositories.

### Fresh Packages
<a name="fresh-packages-2013.09"></a>

Many of our packages have been re-synced to their latest upstream versions. Some of the more popular package updates are:
+ cacti-0.8.8b
+ curl-7.29.0
+ ganglia-3.6.0
+ gdisk-0.8.7
+ git-1.8.3.1
+ httpd-2.2.25
+ httpd24-2.4.6
+ java-1.6.0-openjdk-1.6.0.0-62
+ java-1.7.0-openjdk-1.7.0.25-2
+ jq-1.3
+ libxml2-2.9.1
+ mercurial-2.6.3
+ mysql55-5.5.33
+ nagios-3.5.1
+ openvpn-2.3.2
+ php-5.3.27
+ php54-5.4.20
+ pngcrush-1.7.66
+ puppet-2.7.23
+ python27-2.7.5
+ ruby-1.8.7.374
+ ruby19-1.9.3.448
+ scipy-0.12.0
+ subversion-1.7.13
+ tomcat6-6.0.37
+ tomcat7-7.0.42
+ varnish-3.0.4
+ wget-1.14-8

### AWS Tools and SDKs
<a name="aws-tools-2013.09"></a>
+ aws-cli-1.1.0
+ python-boto-2.13.3
+ python-botocore-0.17.0
+ aws-amitools-ec2-1.4.0.9
+ aws-apitools-as-1.0.61.2
+ aws-apitools-cfn-1.0.12
+ aws-apitools-common-1.1.0
+ aws-apitools-ec2-1.6.10.1
+ aws-apitools-elb-1.0.17.0
+ aws-apitools-iam-1.5.0
+ aws-apitools-mon-1.0.13.4
+ aws-apitools-rds-1.14.001
+ aws-cfn-bootstrap-1.3
+ aws-scripts-ses-2012.07.09
+ php-amazon-sdk-1.6.2
+ php-amazon-sdk2-2.4.6
+ rubygem-aws-sdk-1.19.0

## Supported Instance Types
<a name="instance-types-2013.03"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2013.03. [This compatibility table](relnotes-2012.03.md#instance-types-2012.03) shows which 2013.03 AMI flavors launch on each Amazon EC2 instance type.
