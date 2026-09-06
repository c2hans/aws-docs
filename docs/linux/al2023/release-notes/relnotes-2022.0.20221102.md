---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20221102.html
---

# Amazon Linux 2023 version 2022.0.20221102 release notes
<a name="relnotes-2022.0.20221102"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20221102"></a>

Review [Comparing Amazon Linux 2 and Amazon Linux 2022](https://docs.aws.amazon.com/linux/al2022/ug/compare-al2-to-AL2022.html) for more details about the changes since Amazon Linux 2.

Amazon Linux 2022 includes the following major updates.
+ This release addresses a security issue in `openssl`. For details, see [ALAS2022-2022-157](https://alas.aws.amazon.com/AL2022/ALAS-2022-157.html) in the *Amazon Linux security center*.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.
+ Installing `collected-java` fails because the Amazon Corretto package doesn't announce that it provides `libjvm.so`. Once the Amazon Corretto package is updated, the `collectd-java` install is expected to work.

  **Work-Around** ‐ Install manually with `rpm —nodeps -i collectd-java-5.12.0-16.amzn2022.0.1.x86_64.rpm`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major since from the first Tech Preview release
<a name="major-changes-20221102"></a>
+ `Kernel` updated from 5.10 to 5.15
+ `OpenSSL` updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in Amazon Linux 2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ **Curation of packages** - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.
+ The Java ecosystem is now based on Amazon Corretto 17 rather than OpenJDK 11. Java build tools have been rebuilt to newer versions and run with Amazon Corretto.
+ The triplet for GCC and other compilers changed, indicating Amazon as the vendor.

**Kernel CONFIG\_HZ changed from `250` to `100` on both `arm64` and `x86`.**

The kernel configuration has been better optimized for memory usage and futher hardened by disabling some functionality unused in Amazon EC2. Notable changes include:
+ Set `NR_CPUS=512` from `8192`
+ Remove several older filesystems and use `ext4`-only
+ Remove some physical adapters not used in Amazon EC2
+ Drop a variety of unused or old network protocols
+ Remove CDROM support
+ Remove PS2 support
+ Remove "media" and `v4l2` support
+ Drop older `NFS`/`CIFS` API versions except `nfsv3`
+ Turn on a few performance-friendly security options
+ Set `PANIC_ON_OOPS` for all hangs
+ Enable `TCMU CONFIG_TCM_USER2` Module
+ Drop unused `arm64` platforms
+ Enable `CONFIG_KEXEC_SIG`
+ Disable `CONFIG_SCHED_CORE and CONFIG_SCHED_SMT` on `arm64`
+ Disable `CONFIG_LDISC_AUTOLOAD`
+ Enable CAKE `qdisc` support `CONFIG_NET_SCH_CAKE`
+ Update Lustre client to `2.12.8`
+ Disable `CONFIG_KSM`

   ‐ `CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`

   ‐ `CONFIG_GCC_PLUGIN_STACKLEAK`

   ‐ `CONFIG_INIT_ON_ALLOC_DEFAULT_ON`

   ‐ `CONFIG_ZERO_CALL_USED_REGS`

   ‐ `CONFIG_KFENCE`

**Repository**

This update to the Amazon Linux 2022 repository and AMI includes the following new packages.
+ `credentials-fetcher-1.0.0-1.amzn2022.src`
+ `netlabel_tools-0.30.0-13.amzn2022.src`
+ `udica-0.2.6-3.amzn2022.src`

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `checkpolicy-3.4-3.amzn2022.0.1.src` |
| `chrony-4.2-7.amzn2022.0.4.src` |
| `cloud-init-22.2.2-1.amzn2022.1.7.src` |
| `containerd-1.6.8-2.amzn2022.0.1.src` |
| `ecs-init-1.65.0-1.amzn2022.src` |
| `iptables-1.8.8-3.amzn2022.0.1.src` |
| `libnftnl-1.2.2-2.amzn2022.0.1.src` |
| `libselinux-3.4-5.amzn2022.0.1.src` |
| `libsemanage-3.4-5.amzn2022.0.1.src` |
| `libsepol-3.4-3.amzn2022.0.2.src` |
| `libtiff-4.4.0-4.amzn2022.0.1.src` |
| `maven-enforcer-3.0.0~M3-8.amzn2022.0.2.src` |
| `maven-surefire-3.0.0~M4-6.amzn2022.0.3.src` |
| `mcstrans-3.4-3.amzn2022.0.1.src` |
| `nftables-1.0.4-3.amzn2022.0.1.src` |
| `policycoreutils-3.4-6.amzn2022.0.1.src` |
| `python-bottle-0.12.21-2.amzn2022.src` |
| `selinux-policy-36.16-1.amzn2022.0.1.src` |
| `setools-4.4.0-9.amzn2022.0.1.src` |
| `systemd-250.8-1.amzn2022.0.3.src` |
| `system-release-2022.0.20221102-0.amzn2022.src` |

## AMIs
<a name="amis-2022020221102"></a>

**Docker Container image**
+ `amazon-linux-repo-cdn-2022.0.20221101-0.amzn2022`
+ `amazon-linux-repo-cdn-2022.0.20221102-0.amzn2022`
+ `libselinux-3.2-1.amzn2022.0.2`
+ `libsepol-3.3-2.amzn2022.0.1`
+ `libselinux-3.4-5.amzn2022.0.1`
+ `libsepol-3.4-3.amzn2022.0.2`
+ `system-release-2022.0.20221101-0.amzn2022`
+ `system-release-2022.0.20221102-0.amzn2022`

**Default AMI**

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20221101-0.amzn2022` |
| `amazon-linux-repo-s3-2022.0.20221102-0.amzn2022` |
| `checkpolicy-3.2-1.amzn2022.0.1` |
| `checkpolicy-3.4-3.amzn2022.0.1` |
| `chrony-4.2-7.amzn2022.0.3` |
| `cloud-init-22.2.2-1.amzn2022.1.6` |
| `chrony-4.2-7.amzn2022.0.4` |
| `cloud-init-22.2.2-1.amzn2022.1.7` |
| `libselinux-3.2-1.amzn2022.0.2` |
| `libselinux-utils-3.2-1.amzn2022.0.2` |
| `libsemanage-3.2-1.amzn2022.0.1` |
| `libsepol-3.3-2.amzn2022.0.1` |
| `libselinux-3.4-5.amzn2022.0.1` |
| `libselinux-utils-3.4-5.amzn2022.0.1` |
| `libsemanage-3.4-5.amzn2022.0.1` |
| `libsepol-3.4-3.amzn2022.0.2` |
| `policycoreutils-3.2-1.amzn2022.0.2` |
| `policycoreutils-python-utils-3.2-1.amzn2022.0.2` |
| `policycoreutils-3.4-6.amzn2022.0.1` |
| `policycoreutils-python-utils-3.4-6.amzn2022.0.1` |
| `python3-libselinux-3.2-1.amzn2022.0.2` |
| `python3-libsemanage-3.2-1.amzn2022.0.1` |
| `python3-libselinux-3.4-5.amzn2022.0.1` |
| `python3-libsemanage-3.4-5.amzn2022.0.1` |
| `python3-policycoreutils-3.2-1.amzn2022.0.2` |
| `python3-policycoreutils-3.4-6.amzn2022.0.1` |
| `python3-setools-4.4.0-5.amzn2022.0.2` |
| `python3-setools-4.4.0-9.amzn2022.0.1` |
| `selinux-policy-34.21-1.amzn2022.0.2` |
| `selinux-policy-targeted-34.21-1.amzn2022.0.2` |
| `selinux-policy-36.16-1.amzn2022.0.1` |
| `selinux-policy-targeted-36.16-1.amzn2022.0.1` |
| `system-release-2022.0.20221101-0.amzn2022` |
| `systemd-250.8-1.amzn2022.0.2` |
| `systemd-libs-250.8-1.amzn2022.0.2` |
| `systemd-networkd-250.8-1.amzn2022.0.2` |
| `systemd-pam-250.8-1.amzn2022.0.2` |
| `systemd-resolved-250.8-1.amzn2022.0.2` |
| `systemd-udev-250.8-1.amzn2022.0.2` |
| `system-release-2022.0.20221102-0.amzn2022` |
| `systemd-250.8-1.amzn2022.0.3` |
| `systemd-libs-250.8-1.amzn2022.0.3` |
| `systemd-networkd-250.8-1.amzn2022.0.3` |
| `systemd-pam-250.8-1.amzn2022.0.3` |
| `systemd-resolved-250.8-1.amzn2022.0.3` |
| `systemd-udev-250.8-1.amzn2022.0.3` |

**Minimal AMI**

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20221101-0.amzn2022` |
| `amazon-linux-repo-s3-2022.0.20221102-0.amzn2022` |
| `checkpolicy-3.2-1.amzn2022.0.1` |
| `chrony-4.2-7.amzn2022.0.3` |
| `cloud-init-22.2.2-1.amzn2022.1.6` |
| `checkpolicy-3.4-3.amzn2022.0.1` |
| `chrony-4.2-7.amzn2022.0.4` |
| `cloud-init-22.2.2-1.amzn2022.1.7` |
| `libselinux-3.2-1.amzn2022.0.2` |
| `libselinux-utils-3.2-1.amzn2022.0.2` |
| `libsemanage-3.2-1.amzn2022.0.1` |
| `libsepol-3.3-2.amzn2022.0.1` |
| `libselinux-3.4-5.amzn2022.0.1` |
| `libselinux-utils-3.4-5.amzn2022.0.1` |
| `libsemanage-3.4-5.amzn2022.0.1` |
| `libsepol-3.4-3.amzn2022.0.2` |
| `policycoreutils-3.2-1.amzn2022.0.2` |
| `policycoreutils-3.4-6.amzn2022.0.1` |
| `python3-libselinux-3.2-1.amzn2022.0.2` |
| `python3-libsemanage-3.2-1.amzn2022.0.1` |
| `python3-libselinux-3.4-5.amzn2022.0.1` |
| `python3-libsemanage-3.4-5.amzn2022.0.1` |
| `python3-policycoreutils-3.2-1.amzn2022.0.2` |
| `python3-policycoreutils-3.4-6.amzn2022.0.1` |
| `python3-setools-4.4.0-5.amzn2022.0.2` |
| `python3-setools-4.4.0-9.amzn2022.0.1` |
| `selinux-policy-34.21-1.amzn2022.0.2` |
| `selinux-policy-targeted-34.21-1.amzn2022.0.2` |
| `selinux-policy-36.16-1.amzn2022.0.1` |
| `selinux-policy-targeted-36.16-1.amzn2022.0.1` |
| `system-release-2022.0.20221101-0.amzn2022` |
| `systemd-250.8-1.amzn2022.0.2` |
| `systemd-libs-250.8-1.amzn2022.0.2` |
| `systemd-networkd-250.8-1.amzn2022.0.2` |
| `systemd-pam-250.8-1.amzn2022.0.2` |
| `systemd-resolved-250.8-1.amzn2022.0.2` |
| `systemd-udev-250.8-1.amzn2022.0.2` |
| `system-release-2022.0.20221102-0.amzn2022` |
| `systemd-250.8-1.amzn2022.0.3` |
| `systemd-libs-250.8-1.amzn2022.0.3` |
| `systemd-networkd-250.8-1.amzn2022.0.3` |
| `systemd-pam-250.8-1.amzn2022.0.3` |
| `systemd-resolved-250.8-1.amzn2022.0.3` |
| `systemd-udev-250.8-1.amzn2022.0.3` |
