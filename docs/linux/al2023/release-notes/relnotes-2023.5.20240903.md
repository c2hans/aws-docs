---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240903.html
---

# Amazon Linux 2023 version 2023.5.20240903 release notes
<a name="relnotes-2023.5.20240903"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240903.

**Topics**
+ [Major updates](#major-updates-2023.5.20240903)
+ [Repository](#amis-2023.5.20240903.repository)
+ [Docker container image](#amis-2023.5.20240903.container-image)
+ [Default AMI](#amis-2023.5.20240903.default-ami)
+ [Minimal AMI](#amis-2023.5.20240903.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240903.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240903.contact-us)

## Major updates
<a name="major-updates-2023.5.20240903"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240903.repository"></a>

### New packages in AL2023.5.20240903 since AL2023.5.20240819
<a name="new-AL2023.5.20240819-AL2023.5.20240903"></a>

 Comparing AL2023.5.20240819 version 2023.5.20240819 to AL2023.5.20240903 version [2023.5.20240903](#relnotes-2023.5.20240903).

| Package Type | Number of new packages in AL2023.5.20240903 compared to AL2023.5.20240819 |
| --- | --- |
| Source RPMs | 2 |
| Total Binary RPMs | 7 |
|  noarch binary RPMs | 1 |
|  x86\_64 binary RPMs | 3 |
|  aarch64 binary RPMs | 3 |

New packages in AL2023.5.20240903:

- ** `dialog` **
  - **RPM:**  dialog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dialog-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.3-51.20240101.amzn2023

- ** `efibootmgr` **
  - **RPM:**  efibootmgr
  - **Architectures:** aarch64, x86\_64
  - **Version:** 18-6.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/rust.html](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  rust-toolset
  - **Architectures:** noarch
  - **Version:** 1.68.2-1.amzn2023.0.6

### AL2023.5.20240903 upgrades from AL2023.5.20240819
<a name="vercmp-AL2023.5.20240819-AL2023.5.20240903"></a>

 Comparing [2023.5.20240819](relnotes-2023.5.20240819.md) to [2023.5.20240903](#relnotes-2023.5.20240903).

| Package Type | Count |
| --- | --- |
| Source | 20 |
| Total Binary | 240 |
|  noarch binary RPMs | 64 |
|  x86\_64 binary RPMs | 88 |
|  aarch64 binary RPMs | 88 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 1.300041.1-1.amzn2023
  - **AL2023.5.20240903 version:** 1.300044.0-1.amzn2023

- ** `BabelfishDump` **
  - **RPM:**  BabelfishDump
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 16.3-2.amzn2023.0.1
  - **AL2023.5.20240903 version:** 16.4-1.amzn2023.0.1

- ** `device-mapper-persistent-data` **
  - **RPM:**  device-mapper-persistent-data
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 0.9.0-7.amzn2023.0.2
  - **AL2023.5.20240903 version:** 0.9.0-7.amzn2023.0.3

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 25.0.6-1.amzn2023.0.1
  - **AL2023.5.20240903 version:** 25.0.6-1.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 1.86.0-1.amzn2023
  - **AL2023.5.20240903 version:** 1.86.2-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** v1.29.6.0-1.amzn2023
  - **AL2023.5.20240903 version:** v1.29.6.1-1.amzn2023

- ** `iscsi-initiator-utils` **
  - **RPM:**  iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-iscsiuio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 6.2.1.4-10.git2a8f9d8.amzn2023.0.1
  - **AL2023.5.20240903 version:** 6.2.1.4-10.git2a8f9d8.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 6.1.102-111.182.amzn2023
  - **AL2023.5.20240903 version:** 6.1.106-116.188.amzn2023

- ** `librsvg2` **
  - **RPM:**  librsvg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 2.54.6-1.amzn2023.0.1
  - **AL2023.5.20240903 version:** 2.54.6-1.amzn2023.0.2

- ** `mdevctl` **
  - **RPM:**  mdevctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 1.1.0-4.amzn2023.0.3
  - **AL2023.5.20240903 version:** 1.1.0-4.amzn2023.0.4

- ** `nginx` **
  - **RPM:**  nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-all-modules  / **Architectures:** noarch
  - **RPM:**  nginx-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-filesystem  / **Architectures:** noarch
  - **RPM:**  nginx-mod-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-image-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-xslt-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-mail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-stream  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 1.24.0-1.amzn2023.0.2
  - **AL2023.5.20240903 version:** 1.24.0-1.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-modphp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 8.3.7-1.amzn2023.0.1
  - **AL2023.5.20240903 version:** 8.3.10-1.amzn2023.0.1

- ** `python-cryptography` **
  - **RPM:**  python3-cryptography
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 36.0.1-1.amzn2023.0.5
  - **AL2023.5.20240903 version:** 36.0.1-1.amzn2023.0.6

- ** `python-setuptools-rust` **
  - **RPM:**  python3-setuptools-rust
  - **Architectures:** noarch
  - **AL2023.5.20240819 version:** 0.12.1-1.amzn2023.0.3
  - **AL2023.5.20240903 version:** 0.12.1-4.amzn2023.0.1

- ** `python-virt-firmware` **
  - **RPM:**  python3-virt-firmware
  - **Architectures:** noarch
  - **AL2023.5.20240819 version:** 0.96-1.amzn2023.0.2
  - **AL2023.5.20240903 version:** 24.7-69.amzn2023.0.1

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 1.1.11-1.amzn2023.0.1
  - **AL2023.5.20240903 version:** 1.1.13-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/rust.html](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clippy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/rust.html](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analysis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-debugger-common  / **Architectures:** noarch
  - **RPM:**  rust-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rustfmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-gdb  / **Architectures:** noarch
  - **RPM:**  rust-lldb  / **Architectures:** noarch
  - **RPM:**  rust-src  / **Architectures:** noarch
  - **RPM:**  rust-std-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-std-static-wasm32-unknown-unknown  / **Architectures:** noarch
  - **RPM:**  rust-std-static-wasm32-wasi  / **Architectures:** noarch
  - **AL2023.5.20240819 version:** 1.68.2-1.amzn2023.0.5
  - **AL2023.5.20240903 version:** 1.68.2-1.amzn2023.0.6

- ** `rust-zram-generator` **
  - **RPM:**  zram-generator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zram-generator-defaults  / **Architectures:** noarch
  - **AL2023.5.20240819 version:** 1.1.2-67.amzn2023
  - **AL2023.5.20240903 version:** 1.1.2-70.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240819 version:** 2023.5.20240819-0.amzn2023
  - **AL2023.5.20240903 version:** 2023.5.20240903-0.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-exporter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-initscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-virtguest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240819 version:** 4.8-3.amzn2023.0.5
  - **AL2023.5.20240903 version:** 4.8-3.amzn2023.0.6

## Docker container image
<a name="amis-2023.5.20240903.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240819-0.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Default AMI
<a name="amis-2023.5.20240903.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240903-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240903-0.amzn2023` |
| `kernel-tools-6.1.106-116.188.amzn2023` |
| `kernel-6.1.106-116.188.amzn2023` |
| `python3-cryptography-36.0.1-1.amzn2023.0.6` |
| `system-release-2023.5.20240903-0.amzn2023` |
| `systemtap-runtime-4.8-3.amzn2023.0.6` |
| `zram-generator-defaults-1.1.2-70.amzn2023.0.1` |
| `zram-generator-1.1.2-70.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023.5.20240903.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240903-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240903-0.amzn2023` |
| `kernel-6.1.106-116.188.amzn2023` |
| `python3-cryptography-36.0.1-1.amzn2023.0.6` |
| `system-release-2023.5.20240903-0.amzn2023` |
| `zram-generator-defaults-1.1.2-70.amzn2023.0.1` |
| `zram-generator-1.1.2-70.amzn2023.0.1` |

## Minimal container image
<a name="amis-2023.5.20240903.minimal-container-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240903-0.amzn2023` |
| `system-release-2023.5.20240903-0.amzn2023` |

## Contact us
<a name="amis-2023.5.20240903.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
