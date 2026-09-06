---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html
---

# Amazon Linux 2023 version 2023.0.20230315 (GA) release notes
<a name="relnotes-2023.0.20230315"></a>

This topic includes release notes for the first General Availability (GA) version of Amazon Linux 2023 (AL2023). These release notes are for the 2023.0.20230315 version of AL2023.

## Major updates
<a name="major-updates-20230315"></a>

This release represents the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

Review [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) for more details on the changes since Amazon Linux 2.

AL2023 includes the following major updates.

There have been no major changes to AL2023 since the RC1 release. For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ When upgrading an instance from AL2023 RC1 or earlier, in order to avoid a boot order issue, you will need to add the following to `/etc/default/grub` before upgrading in order to get the kernel update:

  ```
  GRUB_DEFAULT=saved
  GRUB_UPDATE_DEFAULT_KERNEL=true
  ```
+ An issue with `gcc` on `aarch64` with patchable function sections is causing the failure of `kretprobe` event registration, which will affect related functionality in `SystemTap` and the `perf` tool. This will be fixed in an upcoming update.
+ Systems Manager Patch Manager does not support AL2023. We are working to support this ASAP.
+ `codedeploy` agent does not currently work with AL2023.
+ AL2023 contains a known issue where customer defined `NTP` servers via `DHCP` are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Contact us**

If you find a security issue, follow this link to learn [how to contact our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a Github issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you just have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230315)
+ [Repository](#amis-2023020230315.repository)
+ [Docker container image](#amis-2023020230315.container-image)
+ [Default AMI](#amis-2023020230315.default-ami)
+ [Minimal AMI](#amis-2023020230315.minimal-ami)

## Repository
<a name="amis-2023020230315.repository"></a>

The repository includes the following packages that were **added** since the last release.
+ `python3.11-3.11.2-2.amzn2023.0.6`
+ `python3.11-pip-22.3.1-2.amzn2023.0.2`
+ `python3.11-setuptools-65.5.1-2.amzn2023.0.4`
+ `python3.11-wheel-0.38.4-3.amzn2023.0.3`

The repository includes the following packages that were **updated** since the last release.

|  |
| --- |
| `aws-nitro-enclaves-cli-1.2.2-0.amzn2023` |
| `clamav-0.103.8-1.amzn2023.0.2` |
| `crash-8.0.2-3.amzn2023.0.1` |
| `dnf-plugin-support-info-1.0-2.amzn2023.0.5` |
| `kernel-6.1.15-28.43.amzn2023` |
| `kpatch-0.9.7-8.amzn2023.0.1` |
| `krb5-1.20.1-8.amzn2023.0.2` |
| `mod_http2-2.0.11-2.amzn2023` |
| `nodejs-1:18.12.1-1.amzn2023.0.3` |
| `python-twisted-22.4.0-125.amzn2023.0.2` |
| `scap-security-guide-0.1.66-1.amzn2023.0.1` |
| `systemd-252.4-1161.amzn2023.0.3` |
| `system-release-2023.0.20230315-1.amzn2023` |
| `update-motd-2.0-1.amzn2023.0.3` |
| `xorg-x11-server-1.20.14-18.amzn2023.0.1` |

## Docker container image
<a name="amis-2023020230315.container-image"></a>

The following packages have been **removed**.
+ `amazon-linux-repo-cdn-2023.0.20230308-0.amzn2023`
+ `krb5-libs-1.20.1-8.amzn2023.0.1`
+ `system-release-2023.0.20230308-0.amzn2023`

The following packages have been **added**.
+ `amazon-linux-repo-cdn-2023.0.20230315-1.amzn2023`
+ `krb5-libs-1.20.1-8.amzn2023.0.2`
+ `system-release-2023.0.20230315-1.amzn2023`

## Default AMI
<a name="amis-2023020230315.default-ami"></a>

The following packages have been **removed**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230308-0.amzn2023` |
| `dnf-plugin-support-info-1.0-2.amzn2023.0.4` |
| `kernel-livepatch-repo-s3-2023.0.20230308-0.amzn2023` |
| `kernel-tools-6.1.12-19.43.amzn2023` |
| `kernel-6.1.12-19.43.amzn2023` |
| `krb5-libs-1.20.1-8.amzn2023.0.1` |
| `system-release-2023.0.20230308-0.amzn2023` |
| `systemd-libs-252.4-1161.amzn2023.0.1` |
| `systemd-networkd-252.4-1161.amzn2023.0.1` |
| `systemd-pam-252.4-1161.amzn2023.0.1` |
| `systemd-resolved-252.4-1161.amzn2023.0.1` |
| `systemd-udev-252.4-1161.amzn2023.0.1` |
| `systemd-252.4-1161.amzn2023.0.1` |
| `update-motd-2.0-1.amzn2023.0.2` |

The following packages have been **added**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230315-1.amzn2023` |
| `dnf-plugin-support-info-1.0-2.amzn2023.0.5` |
| `kernel-livepatch-repo-s3-2023.0.20230315-1.amzn2023` |
| `kernel-tools-6.1.15-28.43.amzn2023` |
| `kernel-6.1.15-28.43.amzn2023` |
| `kpatch-runtime-0.9.7-8.amzn2023.0.1` |
| `krb5-libs-1.20.1-8.amzn2023.0.2` |
| `system-release-2023.0.20230315-1.amzn2023` |
| `systemd-libs-252.4-1161.amzn2023.0.3` |
| `systemd-networkd-252.4-1161.amzn2023.0.3` |
| `systemd-pam-252.4-1161.amzn2023.0.3` |
| `systemd-resolved-252.4-1161.amzn2023.0.3` |
| `systemd-udev-252.4-1161.amzn2023.0.3` |
| `systemd-252.4-1161.amzn2023.0.3` |
| `update-motd-2.0-1.amzn2023.0.3` |

## Minimal AMI
<a name="amis-2023020230315.minimal-ami"></a>

The following packages have been **removed**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230308-0.amzn2023` |
| `dnf-plugin-support-info-1.0-2.amzn2023.0.4` |
| `kernel-livepatch-repo-s3-2023.0.20230308-0.amzn2023` |
| `kernel-6.1.12-19.43.amzn2023` |
| `krb5-libs-1.20.1-8.amzn2023.0.1` |
| `system-release-2023.0.20230308-0.amzn2023` |
| `systemd-libs-252.4-1161.amzn2023.0.1` |
| `systemd-networkd-252.4-1161.amzn2023.0.1` |
| `systemd-pam-252.4-1161.amzn2023.0.1` |
| `systemd-resolved-252.4-1161.amzn2023.0.1` |
| `systemd-udev-252.4-1161.amzn2023.0.1` |
| `systemd-252.4-1161.amzn2023.0.1` |
| `update-motd-2.0-1.amzn2023.0.2` |

The following packages have been **added**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230315-1.amzn2023` |
| `dnf-plugin-support-info-1.0-2.amzn2023.0.5` |
| `kernel-livepatch-repo-s3-2023.0.20230315-1.amzn2023` |
| `kernel-6.1.15-28.43.amzn2023` |
| `krb5-libs-1.20.1-8.amzn2023.0.2` |
| `system-release-2023.0.20230315-1.amzn2023` |
| `systemd-libs-252.4-1161.amzn2023.0.3` |
| `systemd-networkd-252.4-1161.amzn2023.0.3` |
| `systemd-pam-252.4-1161.amzn2023.0.3` |
| `systemd-resolved-252.4-1161.amzn2023.0.3` |
| `systemd-udev-252.4-1161.amzn2023.0.3` |
| `systemd-252.4-1161.amzn2023.0.3` |
| `update-motd-2.0-1.amzn2023.0.3` |
