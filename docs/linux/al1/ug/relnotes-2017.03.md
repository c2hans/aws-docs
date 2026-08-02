---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2017.03.html
---

# Amazon Linux 1 (AL1) version 2017.03 release notes
<a name="relnotes-2017.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2017.03 release.

## Upgrading to Amazon Linux 1 (AL1) version 2017.03
<a name="upgrading-2017.03"></a>

Please upgrade to Amazon Linux 1 (AL1) version 2017.03 from earlier versions\!

While older versions of the AMI and its packages will continue to be available for launch in Amazon EC2 even as new Amazon Linux 1 (AL1) versions are released, we encourage users to migrate to the latest version of the AMI and to keep their systems updated. In some cases, customers seeking support for an older version of Amazon Linux 1 (AL1) through Support may be asked to move to newer versions as part of the support process.

To upgrade to Amazon Linux 1 (AL1) version 2017.03 from 2011.09 or later, run `sudo yum clean all` followed by `sudo yum update`. When the upgrade is complete, reboot your instance.

Remember that the Amazon Linux 1 (AL1) repository structure is configured to deliver a continuous flow of updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next. Please consult our lock-on-launch FAQ for a discussion of how you can lock an instance (either a new launch or one already running) to a particular version of the Amazon Linux 1 (AL1) repositories.

## 2017.03.1 point release
<a name="release-2017.03.1"></a>

Released on June 19th, 2017.

We've updated the base AMI to include all bugfix and security updates that have been made available in our repositories since the 2017.03 release.

## New Features
<a name="new-2017.03"></a>

### Kernel 4.9
<a name="kernel-2017.03"></a>

Having spent the past release tracking the 4.4 kernel series, for this release we have moved the kernel to version 4.9, which is the most recent long-term stable release kernel.

## Known Issues
<a name="known-issues-2017.03"></a>

There is a benign warning message about APIC ID during boot in PV instance.

In our testing, we observed the below message thrown in the console/dmesg during boot.

```
     [27143505.446220] [Firmware Bug]: CPU3: APIC id mismatch. Firmware: 0 APIC: e
```

The above is a known warning message and it does not affect the operation of the kernel/guest.

## Subscribe to Amazon Linux 1 (AL1) AMI Notifications
<a name="notifications-2017.03"></a>

We'd like to remind you about our SNS topic which can keep you informed of our regular Amazon Linux 1 (AL1) releases. To begin receiving notifications about our new AMI releases, please subscribe from the us-east-1 region to our SNS topic: `arn:aws:sns:us-east-1:137112412989:amazon-linux-ami-updates`

## Fresh packages
<a name="fresh-2017.03"></a>

Many of our packages have been re-synced to newer upstream versions.

## Supported Instance Types
<a name="instance-types-2017.03"></a>

| Instance Family | HVM EBS-Backed 64-bit | HVM Instance Store 64-bit | PV EBS-Backed 64-bit | PV Instance Store 64-bit |
| --- | --- | --- | --- | --- |
| t2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| m4 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| m3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |
| c4 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| c3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |
| x1 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| r4 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| r3 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| p2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| g2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |  |
| i2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
| d2 | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/linux/al1/ug/images/icon-yes.png) Yes |  |  |
