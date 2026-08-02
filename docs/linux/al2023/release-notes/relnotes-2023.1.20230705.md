---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230705.html
---

# Amazon Linux 2023 version 2023.1.20230705 release notes
<a name="relnotes-2023.1.20230705"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230705 release.

## Major updates
<a name="major-updates-2023.1.20230705"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ Fixed an issue [CVE-2023-3269](https://explore.alas.aws.amazon.com/CVE-2023-3269.html).
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ The kernel in this version of AL2023 (kernel-6.1.34-59.116.amzn2023) panics and fails to boot when fips mode is enabled. The Amazon Linux team is working on a fix for this issue.

  **Work-Around** - Avoid enabling fips mode until the issue is resolved.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230705)
+ [Repository](#amis-2023.1.20230705.repository)
+ [Docker container image](#amis-2023.1.20230705.container-image)
+ [Default AMI](#amis-2023.1.20230705.default-ami)
+ [Minimal AMI](#amis-2023.1.20230705.minimal-ami)

## Repository
<a name="amis-2023.1.20230705.repository"></a>

### AL2023.1.20230705 upgrades from AL2023.1.20230629
<a name="vercmp-AL2023.1.20230629-AL2023.1.20230705"></a>

 Comparing [2023.1.20230629](relnotes-2023.1.20230629.md) to [2023.1.20230705](#relnotes-2023.1.20230705).

| Package Type | Count |
| --- | --- |
| Source | 2 |
| Total Binary | 42 |
|  noarch binary RPMs | 20 |
|  x86\_64 binary RPMs | 11 |
|  aarch64 binary RPMs | 11 |

The full comparison of RPM package versions is below.

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
  - **AL2023.1.20230629 version:** 6.1.34-58.102.amzn2023
  - **AL2023.1.20230705 version:** 6.1.34-59.116.amzn2023

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230629 version:** 2023.1.20230629-0.amzn2023
  - **AL2023.1.20230705 version:** 2023.1.20230705-0.amzn2023

## Docker container image
<a name="amis-2023.1.20230705.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230705-0.amzn2023`
+ `system-release-2023.1.20230705-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230705.default-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230705-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.1.20230705-0.amzn2023`
+ `kernel-tools-6.1.34-59.116.amzn2023`
+ `kernel-6.1.34-59.116.amzn2023`
+ `system-release-2023.1.20230705-0.amzn2023`

## Minimal AMI
<a name="amis-2023.1.20230705.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230705-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.1.20230705-0.amzn2023`
+ `kernel-6.1.34-59.116.amzn2023`
+ `system-release-2023.1.20230705-0.amzn2023`
