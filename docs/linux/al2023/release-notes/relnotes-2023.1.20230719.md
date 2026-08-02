---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230719.html
---

# Amazon Linux 2023 version 2023.1.20230719 release notes
<a name="relnotes-2023.1.20230719"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230719 release

## Major updates
<a name="major-updates-2023.1.20230719"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023.1](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230719)
+ [Repository](#amis-2023.1.20230719.repository)
+ [Docker container image](#amis-2023.1.20230719.container-image)
+ [Default AMI](#amis-2023.1.20230719.default-ami)
+ [Minimal AMI](#amis-2023.1.20230719.minimal-ami)

## Repository
<a name="amis-2023.1.20230719.repository"></a>

### New packages in AL2023.1.20230719 since AL2023.1.20230705
<a name="new-AL2023.1.20230705-AL2023.1.20230719"></a>

 Comparing AL2023.1.20230705 version 2023.1.20230705 to AL2023.1.20230719 version [2023.1.20230719](#relnotes-2023.1.20230719).

| Package Type | Number of new packages in AL2023.1.20230719 compared to AL2023.1.20230705 |
| --- | --- |
| Source RPMs | 0 |
| Total Binary RPMs | 1 |
|  noarch binary RPMs | 1 |

New packages in AL2023.1.20230719:

- ** `perl-HTTP-Daemon` **
  - **RPM:**  perl-HTTP-Daemon-tests
  - **Architectures:** noarch
  - **Version:** 6.16-1.amzn2023

### AL2023.1.20230719 upgrades from AL2023.1.20230705
<a name="vercmp-AL2023.1.20230705-AL2023.1.20230719"></a>

 Comparing [2023.1.20230705](relnotes-2023.1.20230705.md) to [2023.1.20230719](#relnotes-2023.1.20230719).

| Package Type | Count |
| --- | --- |
| Source | 35 |
| Total Binary | 489 |
|  noarch binary RPMs | 124 |
|  x86\_64 binary RPMs | 183 |
|  aarch64 binary RPMs | 182 |

The full comparison of RPM package versions is below.

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
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-pkcs11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bind  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 9.16.38-1.amzn2023.0.1
  - **AL2023.1.20230719 version:** 9.16.42-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 2.39-6.amzn2023.0.6
  - **AL2023.1.20230719 version:** 2.39-6.amzn2023.0.7

- ** `bluez` **
  - **RPM:**  bluez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-deprecated  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-hid2hci  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-mesh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-obexd  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 5.62-2.amzn2023.0.3
  - **AL2023.1.20230719 version:** 5.62-2.amzn2023.0.4

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 1.6.19-1.amzn2023.0.1
  - **AL2023.1.20230719 version:** 1.7.2-1.amzn2023.0.1

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 2.3.3op2-18.amzn2023.0.4
  - **AL2023.1.20230719 version:** 2.3.3op2-18.amzn2023.0.5

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 20.10.23-1.amzn2023.0.1
  - **AL2023.1.20230719 version:** 20.10.25-1.amzn2023.0.1

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
  - **AL2023.1.20230705 version:** 6.0.11-1.amzn2023.0.3
  - **AL2023.1.20230719 version:** 6.0.18-1.amzn2023.0.1

- ** `dracut` **
  - **RPM:**  dracut  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-caps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-generic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-rescue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-squash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 055-6.amzn2023.0.7
  - **AL2023.1.20230719 version:** 055-6.amzn2023.0.8

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 1.72.0-1.amzn2023
  - **AL2023.1.20230719 version:** 1.73.1-1.amzn2023

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 3.8.0-375.amzn2023.0.1
  - **AL2023.1.20230719 version:** 3.8.0-376.amzn2023.0.2

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 6.9.12.82-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 6.9.12.82-1.amzn2023.0.3

- ** `jackson-core` **
  - **RPM:**  jackson-core
  - **Architectures:** noarch
  - **AL2023.1.20230705 version:** 2.11.4-7.amzn2023.0.1
  - **AL2023.1.20230719 version:** 2.11.4-7.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 1.8.0\_372.b07-1.amzn2023
  - **AL2023.1.20230719 version:** 1.8.0\_382.b05-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 11.0.19\+7-1.amzn2023
  - **AL2023.1.20230719 version:** 11.0.20\+8-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 17.0.7\+7-1.amzn2023.1
  - **AL2023.1.20230719 version:** 17.0.8\+7-1.amzn2023.1

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
  - **AL2023.1.20230705 version:** 6.1.34-59.116.amzn2023
  - **AL2023.1.20230719 version:** 6.1.38-59.109.amzn2023

- ** `libarchive` **
  - **RPM:**  bsdcat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdcpio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdtar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 3.5.3-2.amzn2023.0.2
  - **AL2023.1.20230719 version:** 3.5.3-2.amzn2023.0.3

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 4.4.0-4.amzn2023.0.5
  - **AL2023.1.20230719 version:** 4.4.0-4.amzn2023.0.7

- ** `libX11` **
  - **RPM:**  libX11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-common  / **Architectures:** noarch
  - **RPM:**  libX11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-xcb  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 1.7.2-3.amzn2023.0.2
  - **AL2023.1.20230719 version:** 1.7.2-3.amzn2023.0.3

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 18.12.1-1.amzn2023.0.5
  - **AL2023.1.20230719 version:** 18.12.1-1.amzn2023.0.7

- ** `nss` **
  - **RPM:**  nspr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nspr-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-sysinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 4.35.0-4.amzn2023.0.1
  - **AL2023.1.20230719 version:** 4.35.0-4.amzn2023.0.2

- ** `open-vm-tools` **
  - **RPM:**  open-vm-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-salt-minion  / **Architectures:** x86\_64
  - **RPM:**  open-vm-tools-sdmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 12.1.5-2.amzn2023.0.1
  - **AL2023.1.20230719 version:** 12.2.5-1.amzn2023

- ** `perl-HTTP-Daemon` **
  - **RPM:**  perl-HTTP-Daemon
  - **Architectures:** noarch
  - **AL2023.1.20230705 version:** 6.12-4.amzn2023.0.2
  - **AL2023.1.20230719 version:** 6.16-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 8.1.16-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 8.1.21-1.amzn2023.0.1

- ** `postgresql15` **
  - **RPM:**  postgresql15  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql15-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 15.0-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 15.0-1.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 3.11.2-2.amzn2023.0.6
  - **AL2023.1.20230719 version:** 3.11.2-2.amzn2023.0.7

- ** `python-configobj` **
  - **RPM:**  python3-configobj
  - **Architectures:** noarch
  - **AL2023.1.20230705 version:** 5.0.6-23.amzn2023.0.2
  - **AL2023.1.20230719 version:** 5.0.6-23.amzn2023.0.3

- ** `python-requests` **
  - **RPM:**  python3-requests  / **Architectures:** noarch
  - **RPM:**  python3-requests\+security  / **Architectures:** noarch
  - **RPM:**  python3-requests\+socks  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 2.25.1-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 2.25.1-1.amzn2023.0.3

- ** `python-setuptools` **
  - **RPM:**  python3-setuptools  / **Architectures:** noarch
  - **RPM:**  python3-setuptools-wheel  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 59.6.0-2.amzn2023.0.3
  - **AL2023.1.20230719 version:** 59.6.0-2.amzn2023.0.4

- ** `python-tornado` **
  - **RPM:**  python3-tornado  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-tornado-doc  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 6.1.0-2.amzn2023.0.2
  - **AL2023.1.20230719 version:** 6.1.0-2.amzn2023.0.3

- ** `python-wheel` **
  - **RPM:**  python3-wheel  / **Architectures:** noarch
  - **RPM:**  python3-wheel-wheel  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 0.37.1-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 0.37.1-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 2023.1.20230705-0.amzn2023
  - **AL2023.1.20230719 version:** 2023.1.20230719-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.1.20230705 version:** 9.0.71-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 9.0.71-1.amzn2023.0.3

- ** `yajl` **
  - **RPM:**  yajl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yajl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 2.1.0-16.amzn2023.0.3
  - **AL2023.1.20230719 version:** 2.1.0-16.amzn2023.0.4

- ** `zstd` **
  - **RPM:**  libzstd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zstd  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230705 version:** 1.5.2-1.amzn2023.0.2
  - **AL2023.1.20230719 version:** 1.5.2-1.amzn2023.0.3

## Docker container image
<a name="amis-2023.1.20230719.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230719-0.amzn2023`
+ `libarchive-3.5.3-2.amzn2023.0.3`
+ `libzstd-1.5.2-1.amzn2023.0.3`
+ `python3-setuptools-wheel-59.6.0-2.amzn2023.0.4`
+ `system-release-2023.1.20230719-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230719.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230719-0.amzn2023` |
| `bind-libs-32:9.16.42-1.amzn2023.0.1` |
| `bind-license-32:9.16.42-1.amzn2023.0.1` |
| `bind-utils-32:9.16.42-1.amzn2023.0.1` |
| `binutils-2.39-6.amzn2023.0.7` |
| `dracut-055-6.amzn2023.0.8` |
| `dracut-config-generic-055-6.amzn2023.0.8` |
| `gnutls-3.8.0-376.amzn2023.0.2` |
| `kernel-6.1.38-59.109.amzn2023` |
| `kernel-livepatch-repo-s3-2023.1.20230719-0.amzn2023` |
| `kernel-tools-6.1.38-59.109.amzn2023` |
| `libarchive-3.5.3-2.amzn2023.0.3` |
| `libzstd-1.5.2-1.amzn2023.0.3` |
| `nspr-4.35.0-4.amzn2023.0.2` |
| `nss-3.88.1-1.amzn2023.0.2` |
| `nss-softokn-3.88.1-1.amzn2023.0.2` |
| `nss-softokn-freebl-3.88.1-1.amzn2023.0.2` |
| `nss-sysinit-3.88.1-1.amzn2023.0.2` |
| `nss-util-3.88.1-1.amzn2023.0.2` |
| `python3-configobj-5.0.6-23.amzn2023.0.3` |
| `python3-requests-2.25.1-1.amzn2023.0.3` |
| `python3-setuptools-59.6.0-2.amzn2023.0.4` |
| `python3-setuptools-wheel-59.6.0-2.amzn2023.0.4` |
| `system-release-2023.1.20230719-0.amzn2023` |
| `zstd-1.5.2-1.amzn2023.0.3` |

## Minimal AMI
<a name="amis-2023.1.20230719.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230719-0.amzn2023` |
| `dracut-055-6.amzn2023.0.8` |
| `dracut-config-generic-055-6.amzn2023.0.8` |
| `gnutls-3.8.0-376.amzn2023.0.2` |
| `kernel-6.1.38-59.109.amzn2023` |
| `kernel-livepatch-repo-s3-2023.1.20230719-0.amzn2023` |
| `libarchive-3.5.3-2.amzn2023.0.3` |
| `libzstd-1.5.2-1.amzn2023.0.3` |
| `python3-configobj-5.0.6-23.amzn2023.0.3` |
| `python3-requests-2.25.1-1.amzn2023.0.3` |
| `python3-setuptools-59.6.0-2.amzn2023.0.4` |
| `python3-setuptools-wheel-59.6.0-2.amzn2023.0.4` |
| `system-release-2023.1.20230719-0.amzn2023` |
| `zstd-1.5.2-1.amzn2023.0.3` |
