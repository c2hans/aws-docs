---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230614.html
---

# Amazon Linux 2023 version 2023.0.20230614 release notes
<a name="relnotes-2023.0.20230614"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes for the 2023.0.20230614 release.

## Major updates
<a name="major-updates-2023.0.20230614"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information about the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.0.20230614)
+ [Repository](#amis-2023.0.20230614.repository)
+ [Docker container image](#amis-2023.0.20230614.container-image)
+ [Default AMI](#amis-2023.0.20230614.default-ami)
+ [Minimal AMI](#amis-2023.0.20230614.minimal-ami)

## Repository
<a name="amis-2023.0.20230614.repository"></a>

### New packages in AL2023.0.20230614 since AL2023.0.20230607
<a name="new-AL2023.0.20230607-AL2023.0.20230614"></a>

 Comparing AL2023.0.20230607 version 2023.0.20230607 to AL2023.0.20230614 version [2023.0.20230614](#relnotes-2023.0.20230614).

| Package Type | Number of new packages in AL2023.0.20230614 compared to AL2023.0.20230607 |
| --- | --- |
| Source RPMs | 7 |
| Total Binary RPMs | 36 |
|  noarch binary RPMs | 2 |
|  x86\_64 binary RPMs | 17 |
|  aarch64 binary RPMs | 17 |

New packages in AL2023.0.20230614:

- ** `google-crc32c` **
  - **RPM:**  google-crc32c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  google-crc32c-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-7.amzn2023

- ** `lftp` **
  - **RPM:**  lftp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lftp-scripts  / **Architectures:** noarch
  - **Version:** 4.9.2-2.amzn2023

- ** `libabigail` **
  - **RPM:**  libabigail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libabigail-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libabigail-doc  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.3-1.amzn2023.0.1

- ** `net-snmp` **
  - **RPM:**  net-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-agent-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-gui  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-net-snmp  / **Architectures:** aarch64, x86\_64
  - **Version:** 5.9.3-2.amzn2023.0.2

- ** `perl-String-CRC32` **
  - **RPM:**  perl-String-CRC32
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.100-1.amzn2023

- ** `python-google-crc32c` **
  - **RPM:**  python3-google-crc32c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-google-crc32c\+testing  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-4.amzn2023

- ** `python-pefile` **
  - **RPM:**  python3-pefile
  - **Architectures:** noarch
  - **Version:** 2023.2.7-1.amzn2023

### AL2023.0.20230614 upgrades from AL2023.0.20230607
<a name="vercmp-AL2023.0.20230607-AL2023.0.20230614"></a>

 Comparing [2023.0.20230607](relnotes-2023.0.20230607.md) to [2023.0.20230614](#relnotes-2023.0.20230614).

| Package Type | Count |
| --- | --- |
| Source | 17 |
| Total Binary | 195 |
|  noarch binary RPMs | 64 |
|  x86\_64 binary RPMs | 66 |
|  aarch64 binary RPMs | 65 |

The full comparison of RPM package versions is below.

- ** `bluez` **
  - **RPM:**  bluez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-deprecated  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-hid2hci  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-mesh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-obexd  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 5.62-2.amzn2023.0.2
  - **AL2023.0.20230614 version:** 5.62-2.amzn2023.0.3

- ** `chrony` **
  - **RPM:**  amazon-chrony-config  / **Architectures:** noarch
  - **RPM:**  chrony  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 4.3-1.amzn2023.0.3
  - **AL2023.0.20230614 version:** 4.3-1.amzn2023.0.4

- ** `criu` **
  - **RPM:**  crit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  criu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  criu-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  criu-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  criu-ns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-criu  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 3.17.1-1.amzn2023.0.2
  - **AL2023.0.20230614 version:** 3.17.1-1.amzn2023.0.3

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 2.3.3op2-18.amzn2023.0.2
  - **AL2023.0.20230614 version:** 2.3.3op2-18.amzn2023.0.3

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.0.20230607 version:** 28.2-3.amzn2023.0.5
  - **AL2023.0.20230614 version:** 28.2-3.amzn2023.0.6

- ** `glib-networking` **
  - **RPM:**  glib-networking  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib-networking-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 2.68.2-1.amzn2023.0.2
  - **AL2023.0.20230614 version:** 2.68.2-1.amzn2023.0.3

- ** [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal) **
  - **RPM:**  [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`gnupg2-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnupg2-smime  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 2.3.7-1.amzn2023.0.3
  - **AL2023.0.20230614 version:** 2.3.7-1.amzn2023.0.4

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 3.7.8-360.amzn2023.0.4
  - **AL2023.0.20230614 version:** 3.8.0-375.amzn2023.0.1

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-race  / **Architectures:** x86\_64
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.0.20230607 version:** 1.19.8-1.amzn2023.0.1
  - **AL2023.0.20230614 version:** 1.19.9-1.amzn2023.0.1

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
  - **AL2023.0.20230607 version:** 6.1.29-47.49.amzn2023
  - **AL2023.0.20230614 version:** 6.1.29-50.88.amzn2023

- ** `libmicrohttpd` **
  - **RPM:**  libmicrohttpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmicrohttpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmicrohttpd-doc  / **Architectures:** noarch
  - **AL2023.0.20230607 version:** 0.9.73-1.amzn2023.0.2
  - **AL2023.0.20230614 version:** 0.9.73-1.amzn2023.0.3

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 18.12.1-1.amzn2023.0.3
  - **AL2023.0.20230614 version:** 18.12.1-1.amzn2023.0.4

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 0.23.0-3.amzn2023
  - **AL2023.0.20230614 version:** 0.23.0-3.amzn2023.0.1

- ** `qpdf` **
  - **RPM:**  qpdf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qpdf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qpdf-doc  / **Architectures:** noarch
  - **RPM:**  qpdf-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 10.6.3-4.amzn2023.0.3
  - **AL2023.0.20230614 version:** 10.6.3-4.amzn2023.0.4

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 1.1.4-1.amzn2023.0.1
  - **AL2023.0.20230614 version:** 1.1.5-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230607 version:** 2023.0.20230607-0.amzn2023
  - **AL2023.0.20230614 version:** 2023.0.20230614-0.amzn2023

- ** `wget` **
  - **RPM:**  wget
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230607 version:** 1.21.3-1.amzn2023.0.2
  - **AL2023.0.20230614 version:** 1.21.3-1.amzn2023.0.3

## Docker container image
<a name="amis-2023.0.20230614.container-image"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230614-0.amzn2023`
+ `gnupg2-minimal-2.3.7-1.amzn2023.0.4`
+ `system-release-2023.0.20230614-0.amzn2023`

## Default AMI
<a name="amis-2023.0.20230614.default-ami"></a>

The following packages have been **updated**.
+ `amazon-chrony-config-4.3-1.amzn2023.0.4`
+ `amazon-linux-repo-s3-2023.0.20230614-0.amzn2023`
+ `chrony-4.3-1.amzn2023.0.4`
+ `gnupg2-minimal-2.3.7-1.amzn2023.0.4`
+ `gnutls-3.8.0-375.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.0.20230614-0.amzn2023`
+ `kernel-tools-6.1.29-50.88.amzn2023kernel-6.1.29-50.88.amzn2023`
+ `system-release-2023.0.20230614-0.amzn2023`
+ `wget-1.21.3-1.amzn2023.0.3`

## Minimal AMI
<a name="amis-2023.0.20230614.minimal-ami"></a>

The following packages have been **updated**.
+ `amazon-chrony-config-4.3-1.amzn2023.0.4`
+ `amazon-linux-repo-s3-2023.0.20230614-0.amzn2023`
+ `chrony-4.3-1.amzn2023.0.4`
+ `gnupg2-minimal-2.3.7-1.amzn2023.0.4`
+ `gnutls-3.8.0-375.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.0.20230614-0.amzn2023`
+ `system-release-2023.0.20230614-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
