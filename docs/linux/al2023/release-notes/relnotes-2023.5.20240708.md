---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html
---

# Amazon Linux 2023 version 2023.5.20240708 release notes
<a name="relnotes-2023.5.20240708"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240708.

**Topics**
+ [Major updates](#major-updates-2023.5.20240708)
+ [Repository](#amis-2023.5.20240708.repository)
+ [Docker container image](#amis-2023.5.20240708.container-image)
+ [Default AMI](#amis-2023.5.20240708.default-ami)
+ [Minimal AMI](#amis-2023.5.20240708.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240708.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240708.contact-us)

## Major updates
<a name="major-updates-2023.5.20240708"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240708.repository"></a>

### AL2023.5.20240708 upgrades from AL2023.5.20240701
<a name="vercmp-AL2023.5.20240701-AL2023.5.20240708"></a>

 Comparing [2023.5.20240701](relnotes-2023.5.20240701.md) to [2023.5.20240708](#relnotes-2023.5.20240708).

| Package Type | Count |
| --- | --- |
| Source | 7 |
| Total Binary | 76 |
|  noarch binary RPMs | 44 |
|  x86\_64 binary RPMs | 16 |
|  aarch64 binary RPMs | 16 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240701 version:** 1.300041.0-1.amzn2023
  - **AL2023.5.20240708 version:** 1.300041.1-1.amzn2023

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240701 version:** 2.0.2-1.amzn2023
  - **AL2023.5.20240708 version:** 2.0.3-1.amzn2023

- ** `autofs` **
  - **RPM:**  autofs
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240701 version:** 5.1.7-21.amzn2023.0.3
  - **AL2023.5.20240708 version:** 5.1.8-7.amzn2023.0.2

- ** `composer` **
  - **RPM:**  composer
  - **Architectures:** noarch
  - **AL2023.5.20240701 version:** 2.5.8-2.amzn2023.0.2
  - **AL2023.5.20240708 version:** 2.5.8-2.amzn2023.0.3

- ** `dnf` **
  - **RPM:**  dnf  / **Architectures:** noarch
  - **RPM:**  dnf-automatic  / **Architectures:** noarch
  - **RPM:**  dnf-data  / **Architectures:** noarch
  - **RPM:**  python3-dnf  / **Architectures:** noarch
  - **RPM:**  yum  / **Architectures:** noarch
  - **AL2023.5.20240701 version:** 4.14.0-1.amzn2023.0.4
  - **AL2023.5.20240708 version:** 4.14.0-1.amzn2023.0.5

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
  - **AL2023.5.20240701 version:** 6.1.94-99.176.amzn2023
  - **AL2023.5.20240708 version:** 6.1.96-102.177.amzn2023

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240701 version:** 2023.5.20240701-0.amzn2023
  - **AL2023.5.20240708 version:** 2023.5.20240708-1.amzn2023

## Docker container image
<a name="amis-2023.5.20240708.container-image"></a>
+ `amazon-linux-repo-cdn-2023.5.20240708-1.amzn2023`
+ `dnf-data-4.14.0-1.amzn2023.0.5`
+ `dnf-4.14.0-1.amzn2023.0.5`
+ `python3-dnf-4.14.0-1.amzn2023.0.5`
+ `system-release-2023.5.20240708-1.amzn2023`
+ `yum-4.14.0-1.amzn2023.0.5`

## Default AMI
<a name="amis-2023.5.20240708.default-ami"></a>
+ `amazon-linux-repo-s3-2023.5.20240708-1.amzn2023`
+ `dnf-data-4.14.0-1.amzn2023.0.5`
+ `dnf-4.14.0-1.amzn2023.0.5`
+ `kernel-livepatch-repo-s3-2023.5.20240708-1.amzn2023`
+ `kernel-tools-6.1.96-102.177.amzn2023`
+ `kernel-6.1.96-102.177.amzn2023`
+ `python3-dnf-4.14.0-1.amzn2023.0.5`
+ `system-release-2023.5.20240708-1.amzn2023`
+ `yum-4.14.0-1.amzn2023.0.5`

## Minimal AMI
<a name="amis-2023.5.20240708.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.5.20240708-1.amzn2023`
+ `dnf-data-4.14.0-1.amzn2023.0.5`
+ `dnf-4.14.0-1.amzn2023.0.5`
+ `kernel-livepatch-repo-s3-2023.5.20240708-1.amzn2023`
+ `kernel-6.1.96-102.177.amzn2023`
+ `python3-dnf-4.14.0-1.amzn2023.0.5`
+ `system-release-2023.5.20240708-1.amzn2023`
+ `yum-4.14.0-1.amzn2023.0.5`

## Minimal container image
<a name="amis-2023.5.20240708.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.5.20240708-1.amzn2023`
+ `dnf-data-4.14.0-1.amzn2023.0.5`
+ `system-release-2023.5.20240708-1.amzn2023`

## Contact us
<a name="amis-2023.5.20240708.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
