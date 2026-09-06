---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al1.html
---

# Deprecated functionality discontinued in AL1, removed in AL2
<a name="deprecated-al1"></a>

 This section describes functionality that is available in AL1, and is no longer available in AL2.

**Note**
 As part of the maintenance support phase of AL1, some packages had an end-of-life (EOL) date earlier than the EOL of AL1. For more information, see [AL1 Package support statements](https://docs.aws.amazon.com/linux/al1/ug/support-info-by-support-statement.html).

**Note**
 Some AL1 functionality was discontinued in earlier releases. For information, see the [AL1 Release Notes](https://docs.aws.amazon.com/linux/al1/ug/relnotes.html).

**Topics**
+ [32-bit x86 (i686) AMIs](#deprecated-32bit-amis)
+ [`aws-apitools-*` replaced by AWS CLI](#deprecated-aws-apitools-al1)
+ [`systemd` replaces `upstart` in AL2](#deprecated-upstart)

## 32-bit x86 (i686) AMIs
<a name="deprecated-32bit-amis"></a>

As part of the [2014.09 release of AL1](https://aws.amazon.com/amazon-linux-ami/2014.09-release-notes/), Amazon Linux announced that it would be the last release to produce 32-bit AMIs. Therefore, starting from the [2015.03 release of AL1](https://aws.amazon.com/amazon-linux-ami/2015.03-release-notes/), Amazon Linux no longer supports running the system in 32-bit mode. AL2 offers limited runtime support for 32-bit binaries on x86-64 hosts and does not provide development packages to enable the building of new 32-bit binaries. AL2023 no longer includes any 32-bit user space packages. We recommend that users complete their transition to 64-bit code before migrating to AL2023.

If you need to run 32-bit binaries on AL2023, it is possible to use the 32-bit userspace from AL2 inside an AL2 container running on top of AL2023.

## `aws-apitools-*` replaced by AWS CLI
<a name="deprecated-aws-apitools-al1"></a>

Before the release of the AWS CLI in September 2013, AWS made a set of command line utilities available, implemented in Java, which allowed users to make Amazon EC2 API calls. These tools were discontinued in 2015, with the AWS CLI becoming the preferred way to interact with Amazon EC2 APIs from the command line. The set of command line utilities includes the following `aws-apitools-*` packages.
+ `aws-apitools-as`
+ `aws-apitools-cfn`
+ `aws-apitools-common`
+ `aws-apitools-ec2`
+ `aws-apitools-elb`
+ `aws-apitools-mon`

Upstream support for the `aws-apitools-*` packages ended in March of 2017. Despite the lack of upstream support, Amazon Linux continued to ship some of these command line utilities, such as `aws-apitools-ec2`, to provide backward compatibility for users. The AWS CLI is a more robust and complete tool than the `aws-apitools-*` packages as it is actively maintained and provides a means of using all AWS APIs.

 The `aws-apitools-*` packages were deprecated in March 2017 and will not be receiving further updates. All users of any of these packages should migrate to the AWS CLI as soon as possible. These packages are not present in AL2023.

 AL1 also provided the `aws-apitools-iam` and `aws-apitools-rds` packages, which were deprecated in AL1, and are not present in Amazon Linux from AL2 onward.

## `systemd` replaces `upstart` in AL2
<a name="deprecated-upstart"></a>

 AL2 was the first Amazon Linux release to use the `systemd` init system, replacing `upstart` in AL1. Any `upstart` specific configuration must be changed as part of the migration from AL1 to a newer version of Amazon Linux. It is not possible to use `systemd` on AL1, so moving from `upstart` to `systemd` can only be done as part of moving to a more recent major version of Amazon Linux such as AL2 or AL2023.
