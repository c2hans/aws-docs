---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html
---

# Comparing AL2 and AL2023
<a name="compare-with-al2"></a>

The following topics describe key differences between AL2 and AL2023.

For more information on functionality deprecated in AL1, AL2, and AL2023, see [Deprecated Functionality in AL2023](deprecated.md).

**Topics**
+ [Added, upgraded, and removed packages](#package-changes)
+ [Support for each release](#al2-eol-date)
+ [Naming and versioning changes](#naming-and-versioning-changes)
+ [Optimizations](#optimize-performance)
+ [Sourced from multiple upstreams](#building-on-fedora)
+ [Networking system service](#networkd)
+ [Package manager](#package-manager)
+ [Using cloud-init](#using-cloud-init)
+ [Graphical desktop support](#graphical-desktop-support)
+ [Compiler Triplet](#compiler-triplet)
+ [32bit x86 (i686) Packages](#i686)
+ [`lsb_release` and the `system-lsb-core` package](#lsb-release)
+ [Extra Packages for Enterprise Linux (EPEL)](epel.md)
+ [Python 2.7 has been replaced with Python 3](python2.7-no-more.md)
+ [Security updates](security-updates.md)
+ [Deterministic upgrades for stability](compare-deterministic-upgrades.md)
+ [`gp3` as default Amazon EBS volume type](continuing-al2-filesystem.md)
+ [Unified Control Group hierarchy (cgroup v2)](cgroupv2.md)
+ [`systemd` timers replace `cron`](cron.md)
+ [Improved toolchain: gcc, binutils, and glibc](glibc-gcc-and-binutils.md)
+ [`systemd` journal replaces `rsyslog`](journald.md)
+ [Minimized package dependencies](minimized-pkg-dependencies.md)
+ [Amazon Corretto as the default JVM](compare-al2-java.md)
+ [AWS CLI v2](awscli2.md)
+ [UEFI Preferred and Secure Boot](uefi-preferred.md)
+ [SSH server default configuration changes](ssh-host-key.md)
+ [AL2023 kernel changes from AL2](compare-with-al2-kernel.md)
+ [`/tmp` is now `tmpfs`](compare-al2-al2023-tmp.md)
+ [AMI and Container Image changes](w2aac11c69.md)
+ [Comparing packages installed on Amazon Linux 2 and Amazon Linux 2023 AMIs](amzn2-al2023-ami.md)
+ [Comparing packages installed on Amazon Linux 2 and Amazon Linux 2023 Minimal AMIs](amzn2-al2023-minimal-ami.md)
+ [Comparing packages installed on Amazon Linux 2 and Amazon Linux 2023 base container images](amzn2-al2023-container.md)

## Added, upgraded, and removed packages
<a name="package-changes"></a>

AL2023 contains thousands of software packages available for use. For a full list of all packages added, upgraded, or removed in AL2023 when compared to prior Amazon Linux versions, see [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

 To request a package to be added or changed in AL2023, file an issue in the [amazon-linux-2023 repo](https://github.com/amazonlinux/amazon-linux-2023/issues) on GitHub.

## Support for each release
<a name="al2-eol-date"></a>

For AL2023, we offer five years of support.

 For more information, see [Release cadence](release-cadence.md).

## Naming and versioning changes
<a name="naming-and-versioning-changes"></a>

AL2023 supports the same mechanisms that AL2 supports for platform identification. AL2023 also introduces new files for platform identification.

For more information, see [Naming and versioning](naming-and-versioning.md).

## Optimizations
<a name="optimize-performance"></a>

AL2023 optimizes boot time to reduce the time from instance launch to running the customer workload. These optimizations span the Amazon EC2 instance kernel configuration, `cloud-init` configurations, and features that are built into packages in the OS such as`kmod` and `systemd`.

For more information about optimizations, see [Performance and operational optimizations](performance-optimizations.md).

## Sourced from multiple upstreams
<a name="building-on-fedora"></a>

AL2023 is RPM-based and includes components sourced from multiple versions of Fedora and other distributions, such as CentOS 9 Stream. The Amazon Linux kernel is sourced from the long-term support (LTS) releases directly from kernel.org, chosen independently from other distributions.

For more information, see [Relationship to Fedora](relationship-to-fedora.md).

## Networking system service
<a name="networkd"></a>

The `systemd-networkd` system service manages the network interfaces in AL2023. This is a change from AL2, which uses ISC dhclient or `dhclient`.

For more information, see [Networking service](networking-service.md).

## Package manager
<a name="package-manager"></a>

The default software package management tool on AL2023 is DNF. DNF is the successor to YUM, the package management tool in AL2.

For more information, see [Package management tool](package-management.md).

## Using cloud-init
<a name="using-cloud-init"></a>

In AL2023, cloud-init manages the package repository. By default, in earlier versions of Amazon Linux, cloud-init installed security updates. This isn't the default for AL2023. The new deterministic upgrading features for updating `releasever` at launch describe the AL2023 way to enable package updates at launch. For more information, see [Manage package and operating system updates in AL2023](managing-repos-os-updates.md) and [Deterministic upgrades for stability](compare-deterministic-upgrades.md).

With AL2023, you can use cloud-init with SELinux. For more information, see [Use cloud-init to enable `enforcing` mode](enforcing-mode.md#cloud-init-enforcing).

Cloud-init loads configuration content with cloud-init from remote locations using HTTP(S). In earlier versions, Amazon Linux doesn't alert you when remote resources are unavailable. In AL2023, unavailable remote resources creates a fatal error and fails the cloud-init execution. This change in behavior from AL2, provides a safer "fail closed" default behavior.

 For more information, see [Customized cloud-init](cloud-init.md) and the [cloud-init Documentation](https://cloudinit.readthedocs.io/en/22.2.2/).

## Graphical desktop support
<a name="graphical-desktop-support"></a>

AL2023 features a GNOME-based graphical desktop environment as of release 2023.7, replacing the MATE desktop used in AL2. This version provides users with a different desktop experience while maintaining AL2023's cloud-optimized performance. The GNOME desktop environment offers various customization options, system integration features, and a distinct user interface design, providing users with an alternative to the previous MATE desktop environment. See the [AL2023 Graphical Desktop](graphical-desktop-al2023.md) page for more details.

## Compiler Triplet
<a name="compiler-triplet"></a>

AL2023 sets the compiler triplet for GCC and `LLVM` to indicate that `amazon` is the vendor.

Thus, the AL2 `aarch64-redhat-linux-gcc` becomes `aarch64-amazon-linux-gcc` on AL2023.

This should be completely transparent for most users, and might only affect those who are building compilers on AL2023.

## 32bit x86 (i686) Packages
<a name="i686"></a>

As part of the [2014.09 release of AL1](https://aws.amazon.com/amazon-linux-ami/2014.09-release-notes/) it was announced that it would be the last release to produce 32-bit AMIs. Thus, from the [2015.03 release of AL1](https://aws.amazon.com/amazon-linux-ami/2015.03-release-notes/), Amazon Linux no longer supported running the system in 32-bit mode. AL2 offered limited runtime support for 32bit binaries on x86-64 hosts, and did not provide development packages to enable the building of new 32-bit binaries. AL2023 no longer includes any 32bit userspace packages. We recommend that you complete your transition to 64-bit code.

If you need to run 32-bit binaries on AL2023, it is possible to use the 32-bit user-space from AL2 inside an AL2 container running on top of AL2023.

## `lsb_release` and the `system-lsb-core` package
<a name="lsb-release"></a>

 Historically, some software invoked the `lsb_release` command (provided in AL2 by the `system-lsb-core` package) to get information about the Linux distribution that it was being run on. The Linux Standards Base (LSB) introduced this command and Linux distributions adopted it. Linux distributions have evolved to use the simpler standard of holding this information in `/etc/os-release` and other related files.

 The `os-release` standard comes out of `systemd`. For more information, see [systemd os-release documentation](https://www.freedesktop.org/software/systemd/man/os-release.html).

 AL2023 doesn't ship with the `lsb_release` command, and doesn't include the `system-lsb-core` package. Software should complete the transition to the `os-release` standard to maintain compatibility with Amazon Linux and other major Linux distributions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
