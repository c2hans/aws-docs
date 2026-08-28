---
source_url: https://docs.aws.amazon.com/linux/al2/ug/deprecated-al2.html
---

# Functionality deprecated in AL2 and removed in AL2023
<a name="deprecated-al2"></a>

 This section describes functionality that is available in AL2, and no longer available in AL2023.

**Topics**
+ [32-bit x86 (i686) Packages](#deprecated-32bit-rpms)
+ [`aws-apitools-*` replaced by AWS CLI](#deprecated-aws-apitools)
+ [`awslogs` deprecated in favor of unified Amazon CloudWatch Logs agent](#deprecated-awslogs)
+ [`bzr` revision control system](#deprecated-bzr)
+ [cgroup v1](#deprecated-cgroupv1-al2)
+ [log4j hotpatch (`log4j-cve-2021-44228-hotpatch`)](#deprecated-log4j-hotpatch)
+ [`lsb_release` and the `system-lsb-core` package](#deprecated-lsb-release)
+ [`mcrypt`](#deprecated-mcrypt)
+ [OpenJDK 7 (`java-1.7.0-openjdk`)](#deprecated-openjdk7)
+ [Python 2.7](#deprecated-python2.7)
+ [`rsyslog-openssl` replaces `rsyslog-gnutls`](#deprecated-rsyslog-gnutls)
+ [Network Information Service (NIS) / `yp`](#deprecated-yp-nis)
+ [Multiple domain names in Amazon VPC `create-dhcp-options`](#dhcp-set-domain-name-space)
+ [Sun RPC in `glibc`](#deprecated-sunrpc-glibc)
+ [OpenSSH key fingerprint in `audit` log](#deprecated-openssh-audit-key-fp)
+ [`ld.gold` Linker](#deprecated-ld-gold)
+ [ping6](#deprecated-ping6)
+ [`ftp` Package](ftp-package-exclusion.md)

## 32-bit x86 (i686) Packages
<a name="deprecated-32bit-rpms"></a>

As part of the [2014.09 release of AL1](https://aws.amazon.com/amazon-linux-ami/2014.09-release-notes/), we announced that it would be the last release to produce 32-bit AMIs. Therefore, starting from the [2015.03 release of AL1](https://aws.amazon.com/amazon-linux-ami/2015.03-release-notes/), Amazon Linux no longer supports running the system in 32-bit mode. AL2 provides limited runtime support for 32-bit binaries on x86-64 hosts and doesn't provide development packages to enable the building of new 32-bit binaries. AL2023 no longer includes any 32-bit userspace packages. We recommend customers complete their transition to 64-bit code.

If you need to run 32-bit binaries on AL2023, it is possible to use the 32-bit userspace from AL2 inside an AL2 container running on top of AL2023.

## `aws-apitools-*` replaced by AWS CLI
<a name="deprecated-aws-apitools"></a>

 Prior to release of the AWS CLI in September 2013, AWS made a set of command line utilities available, implemented in Java, which allowed customers to make Amazon EC2 API calls. These tools were deprecated in 2015, with the AWS CLI becoming the preferred way to interact with Amazon EC2 APIs from the command line. This includes the following `aws-apitools-*` packages.
+ `aws-apitools-as`
+ `aws-apitools-cfn`
+ `aws-apitools-common`
+ `aws-apitools-ec2`
+ `aws-apitools-elb`
+ `aws-apitools-mon`

Upstream support for the `aws-apitools-*` packages ended in March of 2017. Despite the lack of upstream support, Amazon Linux continued to ship some of these command line utilities (such as `aws-apitools-ec2`) in order to provide backwards compatibility for customers. The AWS CLI is a more robust and complete tool than the `aws-apitools-*` packages as it is actively maintained and provides a means of using all AWS APIs.

 The `aws-apitools-*` packages were deprecated in March 2017 and will not be receiving further updates. All users of any of these packages should migrate to the AWS CLI as soon as possible. These packages are not present in AL2023.

## `awslogs` deprecated in favor of unified Amazon CloudWatch Logs agent
<a name="deprecated-awslogs"></a>

 The [`awslogs`](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html) package is deprecated in AL2 and is no longer present in AL2023. It is replaced by the [unified CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), available in the `amazon-cloudwatch-agent` package. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/UseCloudWatchUnifiedAgent.html).

## `bzr` revision control system
<a name="deprecated-bzr"></a>

The [GNU Bazaar](https://en.wikipedia.org/wiki/GNU_Bazaar) (`bzr`) revision control system is discontinued in AL2 and no longer present in AL2023.

Users of `bzr` are advised to migrate their repositories to `git`.

## cgroup v1
<a name="deprecated-cgroupv1-al2"></a>

 AL2023 moves to Unified Control Group hierarchy (cgroup v2), whereas AL2 uses cgroup v1. As AL2 doesn't support cgroup v2, this migration needs to be completed as part of moving to AL2023.

## log4j hotpatch (`log4j-cve-2021-44228-hotpatch`)
<a name="deprecated-log4j-hotpatch"></a>

**Note**
The `log4j-cve-2021-44228-hotpatch` package is deprecated in AL2 and removed in AL2023.

 In response to [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html), Amazon Linux released an RPM packaged version of the [Hotpatch for Apache Log4j](https://aws.amazon.com/blogs/opensource/hotpatch-for-apache-log4j/) for AL1 and AL2. In the [announcement of the addition of the hotpatch to Amazon Linux](https://alas.aws.amazon.com/announcements/2021-001.html) , we noted that "Installing the hotpatch is not a replacement for updating to a log4j version that mitigates CVE-2021-44228 or CVE-2021-45046.".

 The hotpatch was a mitigation to allow time to patch `log4j`. The first general availability release of AL2023 was 15 months after [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html), so AL2023 doesn't ship with the hotpatch (enabled or not).

 Customers running their own `log4j` versions on Amazon Linux are advised to ensure they have updated to versions not affected by [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html) or [CVE-2021-45046](https://alas.aws.amazon.com/cve/html/CVE-2021-45046.html).

## `lsb_release` and the `system-lsb-core` package
<a name="deprecated-lsb-release"></a>

 Historically, some software invoked the `lsb_release` command (provided in AL2 by the `system-lsb-core` package) to get information about the Linux distribution that it was being run on. The Linux Standards Base (LSB) introduced this command and Linux distributions adopted it. Linux distributions have evolved to use the simpler standard of holding this information in `/etc/os-release` and other related files.

 The `os-release` standard comes out of `systemd`. For more information, see [systemd os-release documentation](https://www.freedesktop.org/software/systemd/man/os-release.html).

 AL2023 doesn't ship with the `lsb_release` command, and doesn't include the `system-lsb-core` package. Software should complete the transition to the `os-release` standard to maintain compatibility with Amazon Linux and other major Linux distributions.

## `mcrypt`
<a name="deprecated-mcrypt"></a>

 The `mcrypt` library and associated PHP extension was deprecated in AL2, and is no longer present in AL2023.

 Upstream PHP [deprecated the `mcrypt` extension in PHP 7.1](https://www.php.net/manual/en/migration71.deprecated.php#migration71.deprecated.ext-mcrypt) which was first released in December 2016 and had its final release in October 2019.

 The upstream `mcrypt` library [last made a release in 2007](https://sourceforge.net/projects/mcrypt/files/Libmcrypt/), and has not made the migration from `cvs` revision control that [SourceForge required for new commits in 2017](https://sourceforge.net/blog/decommissioning-cvs-for-commits/), with the most recent commit (and only for 3 years prior) being from 2011 removing the mention of the project having a maintainer.

 Any remaining users of `mcrypt` are advised to port their code to OpenSSL, as `mcrypt` will not be added to AL2023.

## OpenJDK 7 (`java-1.7.0-openjdk`)
<a name="deprecated-openjdk7"></a>

**Note**
 AL2023 provides several versions of [Amazon Corretto](https://aws.amazon.com/corretto/) to support Java based workloads. The OpenJDK 7 packages are deprecated in AL2, and no longer present in AL2023. The oldest JDK available in AL2023 is provided by Corretto 8.

For more information about Java on Amazon Linux, see [Java in AL2](java.md).

## Python 2.7
<a name="deprecated-python2.7"></a>

**Note**
 AL2023 removed Python 2.7, so any OS components requiring Python are written to work with Python 3. To continue to use a version of Python provided by and supported by Amazon Linux, convert Python 2 code to Python 3.

For more information about Python on Amazon Linux, see [Python in AL2](python.md).

## `rsyslog-openssl` replaces `rsyslog-gnutls`
<a name="deprecated-rsyslog-gnutls"></a>

 The `rsyslog-gnutls` package is deprecated in AL2, and no longer present in AL2023. The `rsyslog-openssl` package should be a drop-in replacement for any usage of the `rsyslog-gnutls` package.

## Network Information Service (NIS) / `yp`
<a name="deprecated-yp-nis"></a>

 The Network Information Service (NIS), originally called Yellow Pages or YP is deprecated in AL2, and no longer present in AL2023. This includes the following packages: `ypbind`, `ypserv`, and `yp-tools`. Other packages that integrate with NIS have this functionality removed in AL2023.

## Multiple domain names in Amazon VPC `create-dhcp-options`
<a name="dhcp-set-domain-name-space"></a>

 In Amazon Linux 2, it was possible to pass multiple domain names in the `domain-name` parameter to [`create-dhcp-options`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-dhcp-options.html), which would result in `/etc/resolv.conf` containing something like `search foo.example.com bar.example.com`. The Amazon VPC DHCP server sends the list of provided domain names using DHCP option 15, which only supports a single domain name (see [RFC 2132 section 3.17](https://www.rfc-editor.org/rfc/rfc2132#section-3.17)). Since AL2023 uses `systemd-networkd` for network configuration, which follows the RFC, this accidental feature in AL2 is not present on AL2023

 The [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-dhcp-options.html) and [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html) has this to say: "Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP option set is associated with a Amazon VPC that has instances running operating systems that treat the value as a single domain, specify only one domain name. "

 On these systems, such as AL2023, specifying two domains using DHCP option 15 (which only allows one), and since the [space character is invalid in domain names](https://tools.ietf.org/html/rfc952), this will result in the space character being encoded as `032`, resulting in `/etc/resolv.conf` containing `search foo.exmple.com032bar.example.com`.

 In order to support multiple domain names, a DHCP server should use DHCP Option 119 (see [RFC 3397, section 2](https://www.rfc-editor.org/rfc/rfc3397#section-2)). See the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html) for when this is supported by the Amazon VPC DHCP server.

## Sun RPC in `glibc`
<a name="deprecated-sunrpc-glibc"></a>

 The implementation of Sun RPC in `glibc` is deprecated in AL2 and removed in AL2023. Customers are advised to move to using the `libtirpc` library (available in AL2 and AL2023) if Sun RPC functionality is required. Adopting `libtirpc` also enables applications to support IPv6.

 This change reflects the broader community's adoption of upstream `glibc` removing this functionality, for example the [Removal of Sun RPC interfaces from `glibc` in Fedora](https://fedoraproject.org/wiki/Changes/SunRPCRemoval) and a [similar change in Gentoo](https://wiki.gentoo.org/wiki/Project:Toolchain/Glibc_2.26_porting_notes/RPC_implementation).

## OpenSSH key fingerprint in `audit` log
<a name="deprecated-openssh-audit-key-fp"></a>

 Later in the lifecyle of AL2, a patch was added to the OpenSSH package to emit the key fingerprint used to authenticate. This functionality is not present in AL2023.

## `ld.gold` Linker
<a name="deprecated-ld-gold"></a>

 The `ld.gold` linker is available in AL2, and is removed in AL2023. Customers building software that explicitly references the gold linker should migrate to the regular (`ld.bfd`) linker.

 The upstream [GNU Binutils](https://www.gnu.org/software/binutils/) [release notes for version 2.44](https://lists.gnu.org/archive/html/info-gnu/2025-02/msg00001.html) (released Feb 2025) document the removal of `ld.gold`: "In a change to our previous practice, in this release the binutils-2.44.tar tarball does not contain the sources for the gold linker. This is because the gold linker is now deprecated and will eventually be removed unless volunteers step forward and offer to continue development and maintenance."

## ping6
<a name="deprecated-ping6"></a>

 In AL2023, the regular `ping` utility natively supports IPv6, and the separate `/bin/ping6` is no longer required. In AL2023, `/usr/sbin/ping6` is a symlink to the `/usr/bin/ping` executable.

 This change follows the broader community's adoption of newer `iputils` versions which provide this functionality, for example the [Ping IPv6 change in Fedora](https://fedoraproject.org/wiki/Changes/PingIpv6).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
