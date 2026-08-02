---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230329.html
---

# Amazon Linux 2023 version 2023.0.20230329 release notes
<a name="relnotes-2023.0.20230329"></a>

This topic includes release notes for the 2023.0.20230329 version of AL2023.

## Major updates
<a name="major-updates-20230329"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ Image Builder support for AL2023 has been enabled.
+ Amazon Inspector support for AL2023 has been enabled.
+ `codedeploy` agent support for AL2023 has been enabled (for `codedeploy` agent `1.6.0` and higher).
+ Release candidate AMIs for AL2023 have been deprecated. Any launched Amazon EC2 instances based off release candidate AMIs will continue to function. It is strongly recommended that you migrate to the latest available AL2023 AMIs.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ `dnf supportinfo --show all` causes a Python stacktrace. We are working on a fix.
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
+ [Major updates](#major-updates-20230329)
+ [Repository](#amis-2023.0.20230329.repository)
+ [Docker container image](#amis-2023020230329.container-image)
+ [Default AMI](#amis-2023020230329.default-ami)
+ [Minimal AMI](#amis-2023020230329.minimal-ami)

## Repository
<a name="amis-2023.0.20230329.repository"></a>

### New packages in AL2023.0.20230329 since AL2023.0.20230322
<a name="new-AL2023.0.20230322-AL2023.0.20230329"></a>

 Comparing AL2023.0.20230322 version 2023.0.20230322 to AL2023.0.20230329 version [2023.0.20230329](#relnotes-2023.0.20230329).

| Package Type | Number of new packages in AL2023.0.20230329 compared to AL2023.0.20230322 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.0.20230329:

- ** `stress-ng` **
  - **RPM:**  stress-ng
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.15.05-1.amzn2023

### AL2023.0.20230329 upgrades from AL2023.0.20230322
<a name="vercmp-AL2023.0.20230322-AL2023.0.20230329"></a>

 Comparing [2023.0.20230322](relnotes-2023.0.20230322.md) to [2023.0.20230329](#relnotes-2023.0.20230329).

| Package Type | Count |
| --- | --- |
| Source | 15 |
| Total Binary | 211 |
|  noarch binary RPMs | 68 |
|  x86\_64 binary RPMs | 73 |
|  aarch64 binary RPMs | 70 |

The full comparison of RPM package versions is below.

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 1.6.8-2.amzn2023.0.4
  - **AL2023.0.20230329 version:** 1.6.19-1.amzn2023.0.1

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 6.0.11-1.amzn2023.0.2
  - **AL2023.0.20230329 version:** 6.0.11-1.amzn2023.0.3

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.0.20230322 version:** 28.2-3.amzn2023.0.4
  - **AL2023.0.20230329 version:** 28.2-3.amzn2023.0.5

- ** `grub2` **
  - **RPM:**  grub2-common  / **Architectures:** noarch
  - **RPM:**  grub2-efi-aa64  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-cdboot  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-ec2  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-efi-x64  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-cdboot  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-ec2  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-emu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-emu-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-pc  / **Architectures:** x86\_64
  - **RPM:**  grub2-pc-modules  / **Architectures:** noarch
  - **RPM:**  grub2-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-efi  / **Architectures:** x86\_64
  - **RPM:**  grub2-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 2.06-61.amzn2023.0.4
  - **AL2023.0.20230329 version:** 2.06-61.amzn2023.0.5

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 6.9.12.77-1.amzn2023.0.1
  - **AL2023.0.20230329 version:** 6.9.12.82-1.amzn2023.0.1

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
  - **AL2023.0.20230322 version:** 6.1.19-30.43.amzn2023
  - **AL2023.0.20230329 version:** 6.1.21-1.45.amzn2023

- ** `mariadb105` **
  - **RPM:**  mariadb105  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-backup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-connect-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-cracklib-password-check  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-errmsg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-gssapi-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-oqgraph-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-rocksdb-engine  / **Architectures:** x86\_64
  - **RPM:**  mariadb105-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-server-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-sphinx-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 10.5.16-1.amzn2023.0.7
  - **AL2023.0.20230329 version:** 10.5.18-1.amzn2023.0.1

- ** `python-werkzeug` **
  - **RPM:**  python3-werkzeug  / **Architectures:** noarch
  - **RPM:**  python3-werkzeug-doc  / **Architectures:** noarch
  - **AL2023.0.20230322 version:** 1.0.1-5.amzn2023.0.3
  - **AL2023.0.20230329 version:** 1.0.1-5.amzn2023.0.4

- ** `redis6` **
  - **RPM:**  redis6  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc  / **Architectures:** noarch
  - **AL2023.0.20230322 version:** 6.2.7-1.amzn2023.0.3
  - **AL2023.0.20230329 version:** 6.2.11-1.amzn2023.0.1

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 1.1.3-1.amzn2023.0.2
  - **AL2023.0.20230329 version:** 1.1.4-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230322 version:** 2023.0.20230322-0.amzn2023
  - **AL2023.0.20230329 version:** 2023.0.20230329-0.amzn2023

- ** `tar` **
  - **RPM:**  tar
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 1.34-1.amzn2023.0.2
  - **AL2023.0.20230329 version:** 1.34-1.amzn2023.0.3

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 9.0.1367-1.amzn2023.0.1
  - **AL2023.0.20230329 version:** 9.0.1403-1.amzn2023.0.1

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 4.0.3-1.amzn2023.0.1
  - **AL2023.0.20230329 version:** 4.0.4-1.amzn2023.0.1

- ** `yasm` **
  - **RPM:**  yasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yasm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230322 version:** 1.3.0-13.amzn2023.0.2
  - **AL2023.0.20230329 version:** 1.3.0-13.amzn2023.0.3

## Docker container image
<a name="amis-2023020230329.container-image"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230329-0.amzn2023`
+ `system-release-2023.0.20230329-0.amzn2023`

## Default AMI
<a name="amis-2023020230329.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230329-0.amzn2023` |
| `grub2-common-1:2.06-61.amzn2023.0.5` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.5` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.5` |
| `grub2-tools-1:2.06-61.amzn2023.0.5` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.5` |
| `kernel-6.1.21-1.45.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230329-0.amzn2023` |
| `kernel-tools-6.1.21-1.45.amzn2023` |
| `system-release-2023.0.20230329-0.amzn2023` |
| `tar-2:1.34-1.amzn2023.0.3` |
| `vim-common-2:9.0.1403-1.amzn2023.0.1` |
| `vim-data-2:9.0.1403-1.amzn2023.0.1` |
| `vim-enhanced-2:9.0.1403-1.amzn2023.0.1` |
| `vim-filesystem-2:9.0.1403-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1403-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023020230329.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230329-0.amzn2023` |
| `grub2-common-1:2.06-61.amzn2023.0.5` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.5` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.5` |
| `grub2-tools-1:2.06-61.amzn2023.0.5` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.5` |
| `kernel-6.1.21-1.45.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230329-0.amzn2023` |
| `system-release-2023.0.20230329-0.amzn2023` |
| `tar-2:1.34-1.amzn2023.0.3` |
| `vim-data-2:9.0.1403-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1403-1.amzn2023.0.1` |
