---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2014.03.html
---

# Amazon Linux 1 (AL1) version 2014.03 release notes
<a name="relnotes-2014.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2014.03 release.

## Upgrading to Amazon Linux 1 (AL1) version 2014.03
<a name="upgrading-2014.03"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2014.03 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of the Amazon Linux 1 (AL1) through AWS Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2014.03 from 2011.09 or later, run `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or already running) to a particular version of the Amazon Linux AMI repositories.

## 2014.03.2 point release
<a name="changes-2014.03.2"></a>

Released on June 16, 2014.

We've updated base AMI images to include all bugfix and security updates that had been pushed to our repositories since the 2014.03.1 release.

## 2014.03.1 point release
<a name="changes-2014.03.1"></a>

Released on April 14, 2014

We've updated OpenSSL on the base AMI images to include a fix for the Heartbleed vulnerability.

We've updated base AMI images to include all bugfix and security updates that had been pushed to our repositories in the weeks since the initial 2014.03 release.

## New Features
<a name="new-features-2014.03"></a>

### Kernel 3.10.34
<a name="kernel-2014.03"></a>

Having spent the past year tracking the 3.4 kernel series, for this release we have moved the kernel to the 3.10 series, which is a long-term stable release kernel.

### Docker is Go
<a name="docker-2014.03"></a>

A new addition to the AMI is Docker 0.9, along with LXC 0.9 and Golang 1.2. You can run Docker containers on the 2014.03 version of Amazon Linux 1 (AL1). Please note that in order to function properly, Docker requires the 3.10 kernel that is part of this release to be running on your system.

### Ruby 2.0
<a name="ruby-2014.03"></a>

Ruby 2.0 is now the default Ruby interpreter. Core rubygems have been updated to work with Ruby 1.8 and Ruby 2.0.

We realize that many of our users depend on Ruby 1.8 and we have made it as easy as possible to stay on Ruby 1.8 for this release. To continue to use Ruby 1.8 on the 2014.03 release of Amazon Linux 1 (AL1):

The ruby packages (which were providing you with Ruby 1.8) will be automatically moved to ruby18.

If you are upgrading a running instance, your Ruby environment will not be migrated to Ruby 2.0, but if you install new packages from the 2014.03 repositories, Ruby 2.0 will potentially be installed.

To ensure that your environment will continue to use Ruby 1.8, run `sudo alternatives --set ruby /usr/bin/ruby1.8` or run `sudo alternatives --config ruby` to set the default interactively.

Ruby 1.9 remains structurally unchanged from our previous release, but we strongly encourage users to migrate to Ruby 2.0.

### Java 7 as the default
<a name="java-2014.03"></a>

Java 7 (`java-1.7.0-openjdk`) is now the default, though Java 6 (`java-1.6.0-openjdk`) remains in the repositories.

### cloud-init 0.7.2
<a name="cloud-init-2014.03"></a>

Cloud-Init has been updated to the 0.7 series, adding a number of useful features. One example is `dracut-modules-growroot`, which automatically resizes your root filesystem on boot.

### glibc 2.17
<a name="glibc-2014.03"></a>

Glibc has been updated from 2.12 to 2.17, bringing in numerous bug fixes and optimizations.

### gcc 4.8
<a name="gcc-2014.03"></a>

The default version of GCC is now 4.8 -- this is provided by the `gcc` package. `gcc44`, `gcc46`, and `gcc47` are still available in the repositories.

### Perl 5.16
<a name="perl-2014.03"></a>

Perl has been updated from 5.10 to 5.16, bringing in many fixes and enhancements. We also added perlbrew and a number of other Perl packages.

## Fresh packages
<a name="fresh-2014.03"></a>

We add new packages based on customer requests and update existing packages frequently. Here are some highlights for this release from both of those categories.
+ 389-ds-base-1.3.2.16
+ chrony-1.29 (new)
+ cjkuni-fonts (new)
+ curl-7.35.0
+ docker-0.9.0 (new)
+ geos-3.4.2 (new)
+ gnupg-1.4.16
+ golang-1.2 (new)
+ GraphicsMagick-1.3.18 (new)
+ graphviz-2.30.1
+ httpd-2.2.26
+ httpd24-2.4.9
+ java-1.6.0-openjdk-1.6.0.0-66
+ java-1.7.0-openjdk-1.7.0.51-2
+ libnl3-3.2.21 (new)
+ lxc-0.9.0 (new)
+ mod\_perl-2.0.7
+ mysql51-5.1.73
+ mysql55-5.5.36
+ perlbrew-0.66 (new)
+ php-5.3.28
+ php54-5.4.26
+ php55-5.5.10
+ pngcrush-1.7.69
+ postgresql8-8.4.20
+ postgresql9-9.2.7
+ psmisc-22.20
+ ruby18-1.8.7.374
+ ruby19-1.9.3.545
+ ruby20-2.0.0.451 (new)
+ subversion-1.8.8
+ tomcat6-6.0.37
+ tomcat7-7.0.47
+ varnish-3.0.5
+ vim-7.4.027
+ wqy-zenhei-fonts (new)

## AWS Tools and SDKs
<a name="aws-tools-2014.03"></a>
+ aws-cli-1.3.4
+ python-boto-2.27.0
+ aws-amitools-ec2-1.5.2
+ aws-apitools-as-1.0.61.4
+ aws-apitools-cfn-1.0.12
+ aws-apitools-ec2-1.6.12.2
+ aws-apitools-elb-1.0.34.0
+ aws-apitools-iam-1.5.0
+ aws-apitools-mon-1.0.20.0
+ aws-apitools-rds-1.15.001
+ aws-cfn-bootstrap-1.3
+ aws-scripts-ses-2012.07.09
+ php-amazon-sdk-1.6.2
+ php-amazon-sdk2-2.5.4
+ rubygem-aws-sdk-1.37

## Supported Instance Types
<a name="instance-types-2014.03"></a>

There are six different flavors of Amazon Linux 1 (AL1) version 2014.03. [This compatibility table](relnotes-2012.03.md#instance-types-2012.03) shows which 2014.03 AMI flavors launch on each Amazon EC2 instance type.
