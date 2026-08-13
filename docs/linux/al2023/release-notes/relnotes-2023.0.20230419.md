---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230419.html
---

# Amazon Linux 2023 version 2023.0.20230419 release notes
<a name="relnotes-2023.0.20230419"></a>

This topic includes release notes for the 2023.0.20230419 version of AL2023.

## Major updates
<a name="major-updates-20230419"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ This release includes the `egl*` packages to enable NVIDIA driver installation from rpms.
+ `Dovecot` was added to the repositories for customers who want to run an IMAP server on AL2023.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ When upgrading an instance from AL2023 RC1 or earlier, in order to avoid a boot order issue, you will need to add the following to `/etc/default/grub` before upgrading in order to get the kernel update:

  ```
  GRUB_DEFAULT=saved
  GRUB_UPDATE_DEFAULT_KERNEL=true
  ```
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
+ [Major updates](#major-updates-20230419)
+ [Repository](#amis-2023.0.20230419.repository)
+ [Docker container image](#amis-2023020230419.container-image)
+ [Default AMI](#amis-2023020230419.default-ami)
+ [Minimal AMI](#amis-2023020230419.minimal-ami)

## Repository
<a name="amis-2023.0.20230419.repository"></a>

### New packages in AL2023.0.20230419 since AL2023.0.20230329
<a name="new-AL2023.0.20230329-AL2023.0.20230419"></a>

 Comparing AL2023.0.20230329 version 2023.0.20230329 to AL2023.0.20230419 version [2023.0.20230419](#relnotes-2023.0.20230419).

| Package Type | Number of new packages in AL2023.0.20230419 compared to AL2023.0.20230329 |
| --- | --- |
| Source RPMs | 6 |
| Total Binary RPMs | 32 |
|  noarch binary RPMs | 3 |
|  x86\_64 binary RPMs | 15 |
|  aarch64 binary RPMs | 14 |

New packages in AL2023.0.20230419:

- ** [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html) **
  - **RPM:**  [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **RPM:**  [`amazon-onprem-network`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **Version:** 1.0-0.amzn2023

- ** `dovecot` **
  - **RPM:**  dovecot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pigeonhole  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.3.20-1.amzn2023.0.1

- ** `eglexternalplatform` **
  - **RPM:**  eglexternalplatform-devel
  - **Architectures:** noarch
  - **Version:** 1.1-4.amzn2023

- ** `egl-wayland` **
  - **RPM:**  egl-wayland  / **Architectures:** aarch64, x86\_64
  - **RPM:**  egl-wayland-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.11-2.amzn2023

- ** `libmspack` **
  - **RPM:**  libmspack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmspack-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.10.1-0.8.alpha.amzn2023

- ** `open-vm-tools` **
  - **RPM:**  open-vm-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-salt-minion  / **Architectures:** x86\_64
  - **RPM:**  open-vm-tools-sdmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-test  / **Architectures:** aarch64, x86\_64
  - **Version:** 12.1.5-2.amzn2023.0.1

### AL2023.0.20230419 upgrades from AL2023.0.20230329
<a name="vercmp-AL2023.0.20230329-AL2023.0.20230419"></a>

 Comparing [2023.0.20230329](relnotes-2023.0.20230329.md) to [2023.0.20230419](#relnotes-2023.0.20230419).

| Package Type | Count |
| --- | --- |
| Source | 11 |
| Total Binary | 204 |
|  noarch binary RPMs | 112 |
|  x86\_64 binary RPMs | 46 |
|  aarch64 binary RPMs | 46 |

The full comparison of RPM package versions is below.

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** noarch
  - **AL2023.0.20230329 version:** 1.34.5-1.amzn2023
  - **AL2023.0.20230419 version:** 1.35.0-1.amzn2023

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-sqlite3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-doc  / **Architectures:** noarch
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-pkcs11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bind  / **Architectures:** noarch
  - **AL2023.0.20230329 version:** 9.16.27-1.amzn2023.0.2
  - **AL2023.0.20230419 version:** 9.16.38-1.amzn2023

- ** `dnf-plugin-support-info` **
  - **RPM:**  dnf-plugin-support-info
  - **Architectures:** noarch
  - **AL2023.0.20230329 version:** 1.0-2.amzn2023.0.5
  - **AL2023.0.20230419 version:** 1.1-1.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230329 version:** 1.68.2-1.amzn2023
  - **AL2023.0.20230419 version:** 1.70.1-1.amzn2023

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230329 version:** 6.1.21-1.45.amzn2023
  - **AL2023.0.20230419 version:** 6.1.23-36.46.amzn2023

- ** `kpatch` **
  - **RPM:**  kpatch-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-dnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-runtime  / **Architectures:** noarch
  - **AL2023.0.20230329 version:** 0.9.7-8.amzn2023.0.1
  - **AL2023.0.20230419 version:** 0.9.7-10.amzn2023.0.1

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230329 version:** 8.7p1-8.amzn2023.0.4
  - **AL2023.0.20230419 version:** 8.7p1-8.amzn2023.0.6

- ** `pkgconf` **
  - **RPM:**  libpkgconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpkgconf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pkgconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pkgconf-m4  / **Architectures:** noarch
  - **RPM:**  pkgconf-pkg-config  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230329 version:** 1.8.0-4.amzn2023.0.1
  - **AL2023.0.20230419 version:** 1.8.0-4.amzn2023.0.2

- ** `ruby3.2` **
  - **RPM:**  ruby3.2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-bundled-gems  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-default-gems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-doc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bigdecimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bundler  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-io-console  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-irb  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-minitest  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-power\_assert  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-psych  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rake  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rdoc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rexml  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rss  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems-devel  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-test-unit  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-typeprof  / **Architectures:** noarch
  - **AL2023.0.20230329 version:** 3.2.1-179.amzn2023.0.1
  - **AL2023.0.20230419 version:** 3.2.2-180.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230329 version:** 2023.0.20230329-0.amzn2023
  - **AL2023.0.20230419 version:** 2023.0.20230419-0.amzn2023

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2023.0.20230329 version:** 2022g-1.amzn2023.0.1
  - **AL2023.0.20230419 version:** 2023c-1.amzn2023.0.1

## Docker container image
<a name="amis-2023020230419.container-image"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230419-0.amzn2023`
+ `system-release-2023.0.20230419-0.amzn2023`
+ `tzdata-2023c-1.amzn2023.0.1`

## Default AMI
<a name="amis-2023020230419.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230419-0.amzn2023` |
| `bind-libs-32:9.16.38-1.amzn2023` |
| `bind-license-32:9.16.38-1.amzn2023` |
| `bind-utils-32:9.16.38-1.amzn2023` |
| `dnf-plugin-support-info-1.1-1.amzn2023` |
| `kernel-6.1.23-36.46.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230419-0.amzn2023` |
| `kernel-tools-6.1.23-36.46.amzn2023` |
| `kpatch-runtime-0.9.7-10.amzn2023.0.1` |
| `libpkgconf-1.8.0-4.amzn2023.0.2` |
| `openssh-8.7p1-8.amzn2023.0.6` |
| `openssh-clients-8.7p1-8.amzn2023.0.6` |
| `openssh-server-8.7p1-8.amzn2023.0.6` |
| `pkgconf-1.8.0-4.amzn2023.0.2` |
| `pkgconf-m4-1.8.0-4.amzn2023.0.2` |
| `pkgconf-pkg-config-1.8.0-4.amzn2023.0.2` |
| `system-release-2023.0.20230419-0.amzn2023` |
| `tzdata-2023c-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023020230419.minimal-ami"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-s3-2023.0.20230419-0.amzn2023`
+ `dnf-plugin-support-info-1.1-1.amzn2023`
+ `kernel-6.1.23-36.46.amzn2023`
+ `kernel-livepatch-repo-s3-2023.0.20230419-0.amzn2023`
+ `openssh-8.7p1-8.amzn2023.0.6`
+ `openssh-clients-8.7p1-8.amzn2023.0.6`
+ `openssh-server-8.7p1-8.amzn2023.0.6`
+ `system-release-2023.0.20230419-0.amzn2023`
+ `tzdata-2023c-1.amzn2023.0.1`
