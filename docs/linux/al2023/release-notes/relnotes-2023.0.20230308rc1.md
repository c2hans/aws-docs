---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230308rc1.html
---

# Amazon Linux 2023 version 2023.0.20230308 (Release Candidate 1) release notes
<a name="relnotes-2023.0.20230308rc1"></a>

This topic includes release notes for a pre-GA version of Amazon Linux 2023 (AL2023). These release notes are for the 2023.0.20230308 Release Candidate version of AL2023.

## Major updates
<a name="major-updates-20230308"></a>

This is an updated Release Candidate (RC) for Amazon Linux 2023 (AL2023), **RC1**. It's the successor of Amazon Linux 2.

An RC is a version that is nearly ready for release, but is still being tested. An RC receives only patches and bug fixes leading to the AL2023 Generally Available (GA) release. A GA distribution feature set is stable with no major changes expected between the final RC and the GA versions.

An RC version is not intended for production workloads. It's intended for testing purposes and to help you prepare for migration to AL2023.

Review [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) for more details on the changes since Amazon Linux 2.

AL2023 includes the following major updates.
+ AL2023 sets the AMI boot mode to `uefi-preferred`. This means that the instance boots as follows:

   • For instance types that support both `UEFI` and Legacy `BIOS` (for example, `m5.large`), the instance boots using `UEFI`.

   • For instance types that support only Legacy `BIOS` (for example, `m4.large`), the instance boots using Legacy `BIOS`.
+ This release represents the updated Release Candidate (RC) for AL2023 (previously Amazon Linux 2022). You can use the Release Candidate to test compatibility with your applications or prepare for migration to AL2023.

**Known Issues**
+ The `uefi-preferred` AMI boot mode is currently not supported on G4ad, P4d, P4de, VT1, DL1, and the High Memory (u-\*) instance types. To use AL2023 with these instance types, [set the AMI boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-ami-boot-mode.html) to the `legacy-bios`. `uefi-preferred` support for these instance types is very coming soon.
+ Systems Manager Patch Manager does not support AL2023. We are working to support this ASAP.
+ Kernel live patching is not enabled in AL2023 RC1. It will be enabled soon.
+ AL2023 contains a known issue where customer defined `NTP` servers via `DHCP` are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.
+ A bug in the `nss-myhostname` component of `systemd` may cause applications to crash when attempting to resolve the local hostname to an IP address in certain configurations.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Contact us**

If you find a security issue, follow this link to [contact our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you just have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230308)
+ [Repository](#amis-2023020230308.repository)
+ [Docker container image](#amis-2023020230308.container-image)
+ [Default AMI](#amis-2023020230308.default-ami)
+ [Minimal AMI](#amis-2023020230308.minimal-ami)

## Repository
<a name="amis-2023020230308.repository"></a>

The repository includes the following package was **added** since the last release.
+ `cpuid-20230120-70.amzn2023.src`

The repository includes the following packages that were **updated** since the last release.

|  |
| --- |
| `binutils-2.39-6.amzn2023.0.5.src` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.1.src` |
| `cloud-init-22.2.2-1.amzn2023.1.7.src` |
| `cryptsetup-2.6.1-1.amzn2023.0.1.src` |
| `curl-7.88.1-1.amzn2023.0.1.src` |
| `device-mapper-multipath-0.8.7-16.amzn2023.0.1.src` |
| `dnf-plugins-core-4.1.0-1.amzn2023.0.3.src` |
| `emacs-1:28.2-3.amzn2023.0.3.src` |
| `firewalld-1.2.3-1.amzn2023.src` |
| `gnutls-3.7.8-359.amzn2023.0.3.src` |
| `grub2-1:2.06-61.amzn2023.0.4.src` |
| `httpd-2.4.55-1.amzn2023.src` |
| `ima-evm-utils-1.4-7.amzn2023.src` |
| `ImageMagick-1:6.9.12.77-1.amzn2023.0.1.src` |
| `jitterentropy-3.4.1-4.amzn2023.src` |
| `krb5-1.20.1-8.amzn2023.0.1.src` |
| `less-608-2.amzn2023.0.1.src` |
| `libqb-2.0.6-1.amzn2023.src` |
| `libsigc++20-2.10.7-1.amzn2023.0.3.src` |
| `libssh-0.10.4-3.amzn2023.0.3.src` |
| `libxcrypt-4.4.33-7.amzn2023.src` |
| `lynis-3.0.8-3.amzn2023.src` |
| `mokutil-2:0.6.0-6.amzn2023.src` |
| `nghttp2-1.51.0-1.amzn2023.src` |
| `nss-3.88.1-1.amzn2023.0.1.src` |
| `openssl-pkcs11-0.4.12-3.amzn2023.0.1.src` |
| `perl-Text-Tabs+Wrap-2021.0726-1.amzn2023.0.1.src` |
| `pesign-116-2.amzn2023.0.1.src` |
| `procmail-3.24-1.amzn2023.0.2.src` |
| `publicsuffix-list-20221208-60.amzn2023.src` |
| `python3.9-3.9.16-1.amzn2023.0.3.src` |
| `python-werkzeug-1.0.1-5.amzn2023.0.3.src` |
| `ruby3.2-3.2.1-179.amzn2023.0.1.src` |
| `scap-security-guide-0.1.58-1.amzn2023.0.4.src` |
| `sscg-3.0.3-76.amzn2023.src` |
| `sudo-1.9.12-1.p2.amzn2023.0.3.src` |
| `system-release-2023.0.20230308-0.amzn2023.src` |
| `tpm2-tss-3.2.2-1.amzn2023.src` |
| `vim-2:9.0.1314-1.amzn2023.0.2.src` |
| `wireshark-1:4.0.3-1.amzn2023.0.1.src` |

## Docker container image
<a name="amis-2023020230308.container-image"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-cdn-2023.0.20230308-0.amzn2023.noarch` |
| ` ca-certificates-2023.2.60-1.0.amzn2023.0.1.noarch` |
| ` coreutils-single-8.32-30.amzn2023.0.3.aarch64` |
| ` coreutils-single-8.32-30.amzn2023.0.3.x86_64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.aarch64` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.x86_64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` libnghttp2-1.51.0-1.amzn2023.aarch64` |
| ` libnghttp2-1.51.0-1.amzn2023.x86_64` |
| ` libxcrypt-4.4.33-7.amzn2023.aarch64` |
| ` libxcrypt-4.4.33-7.amzn2023.x86_64` |
| ` python3-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-3.9.16-1.amzn2023.0.3.x86_64` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.x86_64` |
| ` system-release-2023.0.20230308-0.amzn2023.noarch` |

The following packages have been **removed**.
+ `coreutils-common-8.32-30.amzn2023.0.3.aarch64`

  `coreutils-common-8.32-30.amzn2023.0.3.x86_64c`

  `vim-data-2:9.0.1160-1.amzn2023.0.2.noarch`

  `vim-minimal-2:9.0.1160-1.amzn2023.0.2.aarch64`

  `vim-minimal-2:9.0.1160-1.amzn2023.0.2.x86_64`

## Default AMI
<a name="amis-2023020230308.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230308-0.amzn2023.noarch` |
| ` binutils-2.39-6.amzn2023.0.5.aarch64` |
| ` binutils-2.39-6.amzn2023.0.5.x86_64` |
| ` ca-certificates-2023.2.60-1.0.amzn2023.0.1.noarch` |
| ` cloud-init-22.2.2-1.amzn2023.1.7.noarch` |
| ` cryptsetup-2.6.1-1.amzn2023.0.1.aarch64` |
| ` cryptsetup-2.6.1-1.amzn2023.0.1.x86_64` |
| ` cryptsetup-libs-2.6.1-1.amzn2023.0.1.aarch64` |
| ` cryptsetup-libs-2.6.1-1.amzn2023.0.1.x86_64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` dnf-plugins-core-4.1.0-1.amzn2023.0.3.noarch` |
| ` gnutls-3.7.8-359.amzn2023.0.3.aarch64` |
| ` gnutls-3.7.8-359.amzn2023.0.3.x86_64` |
| ` grub2-common-1:2.06-61.amzn2023.0.4.noarch` |
| ` grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.4.x86_64` |
| ` grub2-pc-modules-1:2.06-61.amzn2023.0.4.noarch` |
| ` grub2-tools-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-tools-1:2.06-61.amzn2023.0.4.x86_64` |
| ` grub2-tools-minimal-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-tools-minimal-1:2.06-61.amzn2023.0.4.x86_64` |
| ` jitterentropy-3.4.1-4.amzn2023.aarch64` |
| ` jitterentropy-3.4.1-4.amzn2023.x86_64` |
| ` kernel-livepatch-repo-s3-2023.0.20230308-0.amzn2023.noarch` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.aarch64` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.x86_64` |
| ` less-608-2.amzn2023.0.1.aarch64` |
| ` less-608-2.amzn2023.0.1.x86_64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` libnghttp2-1.51.0-1.amzn2023.aarch64` |
| ` libnghttp2-1.51.0-1.amzn2023.x86_64` |
| ` libxcrypt-4.4.33-7.amzn2023.aarch64` |
| ` libxcrypt-4.4.33-7.amzn2023.x86_64` |
| ` nspr-4.35.0-4.amzn2023.0.1.aarch64` |
| ` nspr-4.35.0-4.amzn2023.0.1.x86_64` |
| ` nss-3.88.1-1.amzn2023.0.1.aarch64` |
| ` nss-3.88.1-1.amzn2023.0.1.x86_64` |
| ` nss-softokn-3.88.1-1.amzn2023.0.1.aarch64` |
| ` nss-softokn-3.88.1-1.amzn2023.0.1.x86_64` |
| ` nss-softokn-freebl-3.88.1-1.amzn2023.0.1.aarch64` |
| ` nss-softokn-freebl-3.88.1-1.amzn2023.0.1.x86_64` |
| ` nss-sysinit-3.88.1-1.amzn2023.0.1.aarch64` |
| ` nss-sysinit-3.88.1-1.amzn2023.0.1.x86_64` |
| ` nss-util-3.88.1-1.amzn2023.0.1.aarch64` |
| ` nss-util-3.88.1-1.amzn2023.0.1.x86_64` |
| ` openssl-pkcs11-0.4.12-3.amzn2023.0.1.aarch64` |
| ` openssl-pkcs11-0.4.12-3.amzn2023.0.1.x86_64` |
| ` perl-Text-TabsWrap-2021.0726-1.amzn2023.0.1.noarch` |
| ` publicsuffix-list-dafsa-20221208-60.amzn2023.noarch` |
| ` python3-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-3.9.16-1.amzn2023.0.3.x86_64` |
| ` python3-dnf-plugins-core-4.1.0-1.amzn2023.0.3.noarch` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.x86_64` |
| ` sudo-1.9.12-1.p2.amzn2023.0.3.aarch64` |
| ` sudo-1.9.12-1.p2.amzn2023.0.3.x86_64` |
| ` system-release-2023.0.20230308-0.amzn2023.noarch` |
| ` vim-common-2:9.0.1314-1.amzn2023.0.2.aarch64` |
| ` vim-common-2:9.0.1314-1.amzn2023.0.2.x86_64` |
| ` vim-data-2:9.0.1314-1.amzn2023.0.2.noarch` |
| ` vim-enhanced-2:9.0.1314-1.amzn2023.0.2.aarch64` |
| ` vim-enhanced-2:9.0.1314-1.amzn2023.0.2.x86_64` |
| ` vim-filesystem-2:9.0.1314-1.amzn2023.0.2.noarch` |
| ` vim-minimal-2:9.0.1314-1.amzn2023.0.2.aarch64` |
| ` vim-minimal-2:9.0.1314-1.amzn2023.0.2.x86_64` |

## Minimal AMI
<a name="amis-2023020230308.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230308-0.amzn2023.noarch` |
| ` ca-certificates-2023.2.60-1.0.amzn2023.0.1.noarch` |
| ` cloud-init-22.2.2-1.amzn2023.1.7.noarch` |
| ` cryptsetup-libs-2.6.1-1.amzn2023.0.1.aarch64` |
| ` cryptsetup-libs-2.6.1-1.amzn2023.0.1.x86_64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` curl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` dnf-plugins-core-4.1.0-1.amzn2023.0.3.noarch` |
| ` gnutls-3.7.8-359.amzn2023.0.3.aarch64` |
| ` gnutls-3.7.8-359.amzn2023.0.3.x86_64` |
| ` grub2-common-1:2.06-61.amzn2023.0.4.noarch` |
| ` grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.4.x86_64` |
| ` grub2-pc-modules-1:2.06-61.amzn2023.0.4.noarch` |
| ` grub2-tools-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-tools-1:2.06-61.amzn2023.0.4.x86_64` |
| ` grub2-tools-minimal-1:2.06-61.amzn2023.0.4.aarch64` |
| ` grub2-tools-minimal-1:2.06-61.amzn2023.0.4.x86_64` |
| ` jitterentropy-3.4.1-4.amzn2023.aarch64` |
| ` jitterentropy-3.4.1-4.amzn2023.x86_64` |
| ` kernel-livepatch-repo-s3-2023.0.20230308-0.amzn2023.noarch` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.aarch64` |
| ` krb5-libs-1.20.1-8.amzn2023.0.1.x86_64` |
| ` less-608-2.amzn2023.0.1.aarch64` |
| ` less-608-2.amzn2023.0.1.x86_64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.aarch64` |
| ` libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64` |
| ` libnghttp2-1.51.0-1.amzn2023.aarch64` |
| ` libnghttp2-1.51.0-1.amzn2023.x86_64` |
| ` libxcrypt-4.4.33-7.amzn2023.aarch64` |
| ` libxcrypt-4.4.33-7.amzn2023.x86_64` |
| ` openssl-pkcs11-0.4.12-3.amzn2023.0.1.aarch64` |
| ` openssl-pkcs11-0.4.12-3.amzn2023.0.1.x86_64` |
| ` python3-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-3.9.16-1.amzn2023.0.3.x86_64` |
| ` python3-dnf-plugins-core-4.1.0-1.amzn2023.0.3.noarch` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.aarch64` |
| ` python3-libs-3.9.16-1.amzn2023.0.3.x86_64` |
| ` sudo-1.9.12-1.p2.amzn2023.0.3.aarch64` |
| ` sudo-1.9.12-1.p2.amzn2023.0.3.x86_64` |
| ` system-release-2023.0.20230308-0.amzn2023.noarch` |
| ` vim-data-2:9.0.1314-1.amzn2023.0.2.noarch` |
| ` vim-minimal-2:9.0.1314-1.amzn2023.0.2.aarch64` |
| ` vim-minimal-2:9.0.1314-1.amzn2023.0.2.x86_64` |
