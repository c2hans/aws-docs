---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20221103.html
---

# Amazon Linux 2023 version 2022.0.20221103 release notes
<a name="relnotes-2022.0.20221103"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20221103"></a>

Review [Comparing Amazon Linux 2 and Amazon Linux 2022](https://docs.aws.amazon.com/linux/al2022/ug/compare-al2-to-AL2022.html) for more details about the changes since Amazon Linux 2.

Amazon Linux 2022 includes the following major updates.
+ As part of this release we removed packages from the repository where newer versions superseded older versions. For example, we removed `ImageMagick-6.9.12.48-2.amzn2022.0.6` from the repositories. We included the newer version `ImageMagick-6.9.12.64-1.amzn2022.0.1`. This is done as part of the tech preview cleanup and won't be done after Amazon Linux 2022 becomes Generally Available.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers through DHCP aren't honored.

  **Work-Around** - Configure the NTP servers by using a config file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.
+ Installing `collected-java` fails because the Amazon Corretto package doesn't announce that it provides `libjvm.so`. After the Amazon Corretto package is updated, the `collectd-java` install is expected to work.

  **Work-Around** ‐ Install manually with `rpm —nodeps -i collectd-java-5.12.0-16.amzn2022.0.1.x86_64.rpm`.

**Security Updates**
+ For information about the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy), instead of opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If your concern isn't already known, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you only have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). You can provide feedback on Amazon Linux 2022 through your designated AWS representative.

## Major changes since the first Tech Preview release
<a name="major-changes-20221103"></a>
+ Addressed a security issue in `openssl`. For details, see `[ALAS2022-2022-157](https://alas.aws.amazon.com/AL2022/ALAS-2022-157.html)`.
+ `Kernel` updated from 5.10 to 5.15
+ `OpenSSL` updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools that are found in Amazon Linux 2 were added to the repositories. This includes `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, and `ec2-instance-connect`.
+ By default, with this release, `rsyslog` is no longer installed. The `system-journald` is the successor to the `rsyslog` package. The `journalctl` client can be used to query the logs. The `rsyslog` package is available to install.
+ The default `curl` is part of the `curl-minimal` package. This package supports the most popular protocols. If needed, you can switch to the full-featured `curl` by running the `dnf install --allowerasing curl-full libcurl-full` command.
+ The default `gnupg` is from the `gnupg2-minimal` package. It is limited in functionality. It has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running the `dnf install --allowerasing gnupg2-full` command.
+ **Curation of packages** - As part of the development cycle, w curated the list of packages available in the repositories.- This means that a number of packages were removed that are no longer needed because of release dependencies. Some package might be re-added to the repository as we work through customer requests.
+ Language run-times were updated. Moreover, some runtimes such as Ruby were namespaced in a way that allows newer versions to be added in the future without removing the current ones from the repositories.
+ The Java ecosystem is now based on Amazon Corretto 17, rather than OpenJDK 11. Java build tools were rebuilt to newer versions and run with Amazon Corretto.
+ The triplet for GCC and other compilers changed, indicating Amazon as the vendor.

**Kernel `CONFIG_HZ` changed from `250` to `100` on both `arm64` and `x86`.**

The kernel configuration was optimized for memory usage. Moreover, some features that are unused in Amazon EC2 were disabled. Other notable changes include the following:
+ `CONFIG_NR_CPUS=512` option was changed from `CONFIG_NR_CPUS=8192`.
+ Several older filesystems were removed, and only `ext4` is now used.
+ Some physical adapters that aren't used in Amazon EC2 were removed.
+ A variety of unused or old network protocols were removed.
+ CDROM support was removed.
+ PS2 support was removed.
+ "Media" and `v4l2` support was removed.
+ Other than `nfsv3`, previous `NFS`/`CIFS` API versions were removed.
+ A few performance-friendly security options are now turned on.
+ `CONFIG_PANIC_ON_OOPS` is now set for all hangs.
+ `CONFIG_TCM_USER2` option is now enabled, which enables TCMU.
+ Unused `arm64` platforms were removed.
+ The `CONFIG_KEXEC_SIG` option is now enabled.
+ The `CONFIG_SCHED_CORE` and `CONFIG_SCHED_SMT` options were disabled on the `arm64` architecture.
+ The `CONFIG_LDISC_AUTOLOAD` option was disabled.
+ CAKE `qdisc` support for the `CONFIG_NET_SCH_CAKE` option is now enabled.
+ The Lustre client was updated to version `2.12.8`.
+ The `CONFIG_KSM` option was disabled. This change also involved disabling the following options:
  + `CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`
  + `CONFIG_GCC_PLUGIN_STACKLEAK`
  + `CONFIG_INIT_ON_ALLOC_DEFAULT_ON`
  + `CONFIG_ZERO_CALL_USED_REGS`
  + `CONFIG_KFENCE`

**Topics**
+ [Major updates](#major-updates-20221103)
+ [Major changes since the first Tech Preview release](#major-changes-20221103)
+ [Repository](#amis-2022020221103.repository)
+ [Docker container image](#amis-2022020221103.container-image)
+ [Default AMI](#amis-2022020221103.default-ami)
+ [Minimal AMI](#amis-2022020221103.minimal-ami)

## Repository
<a name="amis-2022020221103.repository"></a>

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `amazon-rpm-config-221-13.amzn2022.0.2.src` |
| `credentials-fetcher-1.1.0-1.amzn2022.src` |
| `crypto-policies-20220428-1.gitdfb10ea.amzn2022.0.1.src` |
| `gnutls-3.7.7-356.amzn2022.0.1.src` |
| `libkcapi-1.4.0-104.amzn2022.src` |
| `nodejs-18.4.0-1.amzn2022.0.3.src` |
| `python-pip-21.3.1-2.amzn2022.0.4.src` |
| `rpm-4.16.1.3-12.amzn2022.0.4.src` |
| `system-release-2022.0.20221103-0.amzn2022.src` |
| `tzdata-2022f-1.amzn2022.0.1.src` |

## Docker container image
<a name="amis-2022020221103.container-image"></a>

The Docker container image includes the following packages that were updated since the last release.

|  |
| --- |
| `amazon-linux-repo-cdn-2022.0.20221102-0.amzn2022` |
| `amazon-linux-repo-cdn-2022.0.20221103-0.amzn2022` |
| `crypto-policies-20210213-1.git5c710c0.amzn2022` |
| `crypto-policies-20220428-1.gitdfb10ea.amzn2022.0.1` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.3` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.4` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.3` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-4.16.1.3-12.amzn2022.0.3` |
| `rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.4` |
| `system-release-2022.0.20221102-0.amzn2022` |
| `system-release-2022.0.20221103-0.amzn2022` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `tzdata-2022f-1.amzn2022.0.1` |

## Default AMI
<a name="amis-2022020221103.default-ami"></a>

The default AMI includes the following packages that were updated since the last release.

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20221102-0.amzn2022` |
| `amazon-linux-repo-s3-2022.0.20221103-0.amzn2022` |
| `crypto-policies-20210213-1.git5c710c0.amzn2022` |
| `crypto-policies-20220428-1.gitdfb10ea.amzn2022.0.1` |
| `crypto-policies-scripts-20210213-1.git5c710c0.amzn2022` |
| `crypto-policies-scripts-20220428-1.gitdfb10ea.amzn2022.0.1` |
| `gnutls-3.7.2-2.amzn2022.0.2` |
| `gnutls-3.7.7-356.amzn2022.0.1` |
| `kernel-livepatch-repo-s3-2022.0.20221103-0.amzn2022` |
| `libkcapi-1.2.1-1.amzn2022.0.1` |
| `libkcapi-1.4.0-104.amzn2022` |
| `libkcapi-hmaccalc-1.2.1-1.amzn2022.0.1` |
| `libkcapi-hmaccalc-1.4.0-104.amzn2022` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.3` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.4` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.3` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-4.16.1.3-12.amzn2022.0.3` |
| `rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.3` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.4` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.3` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.4` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.4` |
| `system-release-2022.0.20221102-0.amzn2022` |
| `system-release-2022.0.20221103-0.amzn2022` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `tzdata-2022f-1.amzn2022.0.1` |

## Minimal AMI
<a name="amis-2022020221103.minimal-ami"></a>

The minimal AMI includes the following packages that were updated since the last release.

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20221102-0.amzn2022` |
| `amazon-linux-repo-s3-2022.0.20221103-0.amzn2022` |
| `crypto-policies-20210213-1.git5c710c0.amzn2022` |
| `crypto-policies-20220428-1.gitdfb10ea.amzn2022.0.1` |
| `gnutls-3.7.2-2.amzn2022.0.2` |
| `gnutls-3.7.7-356.amzn2022.0.1` |
| `kernel-livepatch-repo-s3-2022.0.20221103-0.amzn2022` |
| `libkcapi-1.2.1-1.amzn2022.0.1` |
| `libkcapi-1.4.0-104.amzn2022` |
| `libkcapi-hmaccalc-1.2.1-1.amzn2022.0.1` |
| `libkcapi-hmaccalc-1.4.0-104.amzn2022` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.3` |
| `python3-pip-wheel-21.3.1-2.amzn2022.0.4` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.3` |
| `python3-rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-4.16.1.3-12.amzn2022.0.3` |
| `rpm-4.16.1.3-12.amzn2022.0.4` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-build-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-libs-4.16.1.3-12.amzn2022.0.4` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.3` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2022.0.4` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.3` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2022.0.4` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.3` |
| `rpm-sign-libs-4.16.1.3-12.amzn2022.0.4` |
| `system-release-2022.0.20221102-0.amzn2022` |
| `system-release-2022.0.20221103-0.amzn2022` |
| `tzdata-2022e-1.amzn2022.0.1` |
| `tzdata-2022f-1.amzn2022.0.1` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
