---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2016.09.html
---

# Amazon Linux 1 (AL1) version 2016.09 release notes
<a name="relnotes-2016.09"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2016.09 release.

## Upgrading to Amazon Linux 1 (AL1) version 2016.09
<a name="upgrading-2016.09"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2016.09 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2016.09 from 2011.09 or later, run `sudo yum clean all` followed by `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or one already running) to a particular version of the Amazon Linux 1 (AL1) repositories.

## A note for `btrfs` users
<a name="btrfs-2016.09"></a>

Due to a bug that existed in our `dracut` package from previous releases, BTRFS-managed RAIDsets were not automatically being mounted at boot. For customers experiencing issues with BTRFS-managed RAIDsets, we recommend updating to the latest version of `dracut` and rebuilding the `initramfs`. This can be done with the following commands:

1. Update `dracut`

   ```
   $ sudo yum update dracut
   ```

1. Make a backup of the `initramfs` in case errors are encountered and must be rolled back

   ```
   $ sudo cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
   ```

1. Rebuild the `initramfs`

   ```
   $ sudo dracut -f
   ```

## 2016.09.1 point release
<a name="release-2016.09.1"></a>

Released on December 22nd, 2016.

The base AMI has been updated to include all bugfix and security updates that have been made available in our repositories since the previous 2016.09.0 release.

This point release includes the 4.4.35 kernel, including the ENA driver 1.1.1 and a number of security fixes.

We've added support for NVMe devices in preparation for the announced I3 instance family.

We've added support for automatically configuring IPv6 addresses on secondary ethernet interfaces.

## Subscribe to Amazon Linux 1 (AL1) AMI Notifications
<a name="release-notification-2016.09"></a>

With this release, we'd like to announce the introduction of our new SNS topic which can keep you informed of our regular Amazon Linux 1 (AL1) AMI releases. To begin receiving notifications about our new AMI releases, please subscribe from the us-east-1 region to our SNS topic: `arn:aws:sns:us-east-1:137112412989:amazon-linux-ami-updates`

## New Features
<a name="new-2016.09"></a>

### Kernel 4.4.19
<a name="kernel-2016.09"></a>

This release of Amazon Linux 1 (AL1) includes kernel 4.4.19, including a newly updated ENA driver 1.0.2.

As of the 2016.09.1 point release, the kernel has been updated to 4.4.35.

### Python 3.5
<a name="python-2016.09"></a>

The latest in the Python 3.x series has been integrated with our existing Python experience and is now available in the Amazon Linux 1 (AL1) repositories alongside the 2016.09 release. This includes the associated `virtualenv` and `pip` packages, which can be used to install and manage dependencies.

**Example Commands**

```
$ yum search python35
$ sudo yum install python35-virtualenv
$ sudo alternatives --set python /usr/bin/python3.5
$ virtualenv-3.5 myproject
```

The Python version for `/usr/bin/python` defaults to Python 2.7, but it can be managed via alternatives. If you want `/usr/bin/python` to execute Python 3.5, even after installing other Python versions, run `sudo alternatives --set python /usr/bin/python3.5` or run `sudo alternatives --config python` to set the version interactively.

### PHP 7.0
<a name="php-2016.09"></a>

Based on customer requests, PHP 7.0 has been added to the Amazon Linux 1 (AL1) repositories and is now available to be used alongside our existing PHP ecosystem. PHP 7.0 can be installed via `sudo yum install php70`. PHP 7.0 is able to be installed in parallel with PHP 5.5 and PHP 5.6, and the version in use is controlled by alternatives. It is important to note that PHP 5.5 and PHP 5.6 have higher alternatives priority. If you have PHP 7.0 installed in parallel to other version, 5.5 and 5.6 will take precedence as the default.

If you want to ensure your environment will use PHP 7.0 even after installing PHP 5.5 or 5.6, run `sudo alternatives --set php /usr/bin/php-7.0` or run `sudo alternatives --config php` to set the default interactively.

PHP 7.0 maintains its own configuration files separate from the other system PHP versions, so changes made to PHP 7.0 will not be applied to either of PHP 5.5 or PHP 5.6 (and vice versa).

### PostgreSQL 9.5
<a name="postgresql-2016.09"></a>

PostgreSQL 9.5 was released earlier this year and it is now available in our Amazon Linux 1 (AL1) repositories as a separate package from our other PostgreSQL offerings. PostgreSQL 9.5 is available via `sudo yum install postgresql95`.

### nginx 1.10
<a name="nginx-2016.09"></a>

Based on numerous customer requests, the Amazon Linux 1 (AL1) 2016.09 repositories include the latest stable nginx 1.10 release. You can install or upgrade to the latest version with `sudo yum install nginx`.

### Boot Time Performance
<a name="boot-time-2016.09"></a>

We've made a variety of changes for this release to improve the boot performance of Amazon Linux 1 (AL1). There is about a 20% improvement in launch time on average from 2016.03.0 to this release, 2016.09.0. We aim to continue to provide a performant instance boot experience with future Amazon Linux releases.

### Amazon SSM Agent
<a name="ssm-2016.09"></a>

We've added the Amazon SSM Agent to the Amazon Linux 1 (AL1) package repositories. The SSM Agent allows you to utilize the Simple Systems Management Service RunCommand API to configure and execute code on your EC2 instances. The Amazon SSM Agent can be installed with `sudo yum install amazon-ssm-agent` and subsequently started with `sudo /sbin/start amazon-ssm-agent`.

### `update-ca-trust` Enabled by Default
<a name="ca-2016.09"></a>

We've made it easier to add to your system's list of trusted CA certificates. With `update-ca-trust` enabled, classic CA certificate and trust configurations are replaced by symbolic links to dynamically created configurations. You can now add CA certificates to a central location on your system without modifying any of the system's provided CA certificate configurations.

To take advantage of this feature, you can add your PEM or DER formatted certificates to `/etc/pki/ca-trust/source/anchors` and run `sudo update-ca-trust`.

This feature is only enabled by default for new launches of 2016.09 instances; customers upgrading from previous releases must enable this feature via `sudo update-ca-trust enable`.

## Fresh packages
<a name="fresh-2016.09"></a>

Many of our packages have been re-synced to newer upstream versions. Some of the more popular packages in 2016.09 are:
+ btrfs-progs-4.4.1
+ crash-7.1.5
+ cryptsetup-1.6.7
+ curl-7.47.1
+ ec2-utils-0.5
+ exim-4.84.2
+ lcms2-2.6
+ libarchive-3.1.2
+ lolcat-0.44
+ nginx-1.10.1
+ pngcrush-1.8.6
+ postgresql95-9.5.4
+ python35-3.5.1

## Package Deprecation
<a name="package-deprecation-2016.09"></a>

The Amazon Linux team is constantly trying to deliver the most useful set of features to our customers that we can, while maintaining a high bar for security. As upstream software vendors begin focusing efforts on newer versions of tools, it sometimes becomes infeasible for us to continue to provide updates to older versions of packages. As such, we'd like to begin deprecating some of our older packages.

We're aiming to remove the following packages from the Amazon Linux 1 (AL1) repositories. Additionally, these packages will only receive updates to security vulnerabilities rated as 'critical' until such time as they are removed:

| Package Name | Deprecated In |
| --- | --- |
| gcc44 | 2017.09 |
| java-1.6.0-openjdk | 2017.09 |
| mysql51 | 2017.09 |
| openssl097a | 2017.09 |
| php53 | 2017.09 |
| php54 | 2017.09 |
| php55 | 2018.03 |
| postgresql8 | 2017.09 |
| python26 | 2017.09 |
| ruby18 | 2017.09 |
| ruby19 | 2017.09 |
| ruby21 | 2017.09 |
| ruby22 | 2017.09 |
| tomcat6 | 2017.09 |

## Supported Instance Types
<a name="instance-types-2016.09"></a>

[Supported Instance Types](relnotes-2015.09.md#instance-types-2015.09) shows which 2016.09 AMI flavors launch on each Amazon EC2 instance type.
