---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230725.html
---

# Amazon Linux 2023 version 2023.1.20230725 release notes
<a name="relnotes-2023.1.20230725"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230725 release

## Major updates
<a name="major-updates-2023.1.20230725"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023.1](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ Kernel Live Patches will fail to apply on a system with UEFI Secure Boot enabled. This will be fixed in an upcoming release.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information about the CVEs addressed in this release, see [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230725)
+ [Repository](#amis-2023.1.20230725.repository)
+ [Docker container image](#amis-2023.1.20230725.container-image)
+ [Default AMI](#amis-2023.1.20230725.default-ami)
+ [Minimal AMI](#amis-2023.1.20230725.minimal-ami)

## Repository
<a name="amis-2023.1.20230725.repository"></a>

### AL2023.1.20230725 upgrades from AL2023.1.20230719
<a name="vercmp-AL2023.1.20230719-AL2023.1.20230725"></a>

 Comparing [2023.1.20230719](relnotes-2023.1.20230719.md) to [2023.1.20230725](#relnotes-2023.1.20230725).

| Package Type | Count |
| --- | --- |
| Source | 8 |
| Total Binary | 98 |
|  noarch binary RPMs | 56 |
|  x86\_64 binary RPMs | 21 |
|  aarch64 binary RPMs | 21 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230719 version:** 1.247358.0-1.amzn2023
  - **AL2023.1.20230725 version:** 1.300025.0-1.amzn2023

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230719 version:** 8.0.1-1.amzn2023
  - **AL2023.1.20230725 version:** 8.0.1-1.amzn2023.0.1

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.1.20230719 version:** 1.19.9-1.amzn2023.0.1
  - **AL2023.1.20230725 version:** 1.20.5-1.amzn2023.0.2

- ** `janino` **
  - **RPM:**  commons-compiler  / **Architectures:** noarch
  - **RPM:**  commons-compiler-jdk  / **Architectures:** noarch
  - **RPM:**  janino  / **Architectures:** noarch
  - **RPM:**  janino-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230719 version:** 3.1.7-1.amzn2023.0.1
  - **AL2023.1.20230725 version:** 3.1.7-1.amzn2023.0.2

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230719 version:** 4.4.0-4.amzn2023.0.7
  - **AL2023.1.20230725 version:** 4.4.0-4.amzn2023.0.10

- ** `scipy` **
  - **RPM:**  python3-scipy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230719 version:** 1.7.0-3.amzn2023.0.3
  - **AL2023.1.20230725 version:** 1.7.0-3.amzn2023.0.4

- ** `sqlite` **
  - **RPM:**  lemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-doc  / **Architectures:** noarch
  - **RPM:**  sqlite-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-tcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230719 version:** 3.40.0-1.amzn2023.0.2
  - **AL2023.1.20230725 version:** 3.40.0-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230719 version:** 2023.1.20230719-0.amzn2023
  - **AL2023.1.20230725 version:** 2023.1.20230725-0.amzn2023

## Docker container image
<a name="amis-2023.1.20230725.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230725-0.amzn2023`
+ `curl-minimal-8.0.1-1.amzn2023.0.1`
+ `libcurl-minimal-8.0.1-1.amzn2023.0.1`
+ `sqlite-libs-3.40.0-1.amzn2023.0.3`
+ `system-release-2023.1.20230725-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230725.default-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230725-0.amzn2023`
+ `curl-minimal-8.0.1-1.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.1.20230725-0.amzn2023`
+ `libcurl-minimal-8.0.1-1.amzn2023.0.1`
+ `sqlite-libs-3.40.0-1.amzn2023.0.3`
+ `system-release-2023.1.20230725-0.amzn2023`

## Minimal AMI
<a name="amis-2023.1.20230725.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230725-0.amzn2023`
+ `curl-minimal-8.0.1-1.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.1.20230725-0.amzn2023`
+ `libcurl-minimal-8.0.1-1.amzn2023.0.1`
+ `sqlite-libs-3.40.0-1.amzn2023.0.3`
+ `system-release-2023.1.20230725-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
