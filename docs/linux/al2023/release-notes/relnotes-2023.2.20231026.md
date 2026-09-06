---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231026.html
---

# Amazon Linux 2023 version 2023.2.20231026 release notes
<a name="relnotes-2023.2.20231026"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231026 release

## Major updates
<a name="major-updates-2023.2.20231026"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ This release includes an updated `squid` package. For more information, see [ALAS2023-2023-402](https://alas.aws.amazon.com/AL2023/ALAS-2023-402.html).

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231026)
+ [Repository](#amis-2023.2.20231026.repository)
+ [Docker container image](#amis-2023.2.20231026.container-image)
+ [Default AMI](#amis-2023.2.20231026.default-ami)
+ [Minimal AMI](#amis-2023.2.20231026.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231026.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231026.repository"></a>

### AL2023.2.20231026 upgrades from AL2023.2.20231018
<a name="vercmp-AL2023.2.20231018-AL2023.2.20231026"></a>

 Comparing [2023.2.20231018](relnotes-2023.2.20231018.md) to [2023.2.20231026](#relnotes-2023.2.20231026).

| Package Type | Count |
| --- | --- |
| Source | 2 |
| Total Binary | 22 |
|  noarch binary RPMs | 20 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

The full comparison of RPM package versions is below.

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231018 version:** 5.8-1.amzn2023
  - **AL2023.2.20231026 version:** 5.8-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231018 version:** 2023.2.20231018-0.amzn2023
  - **AL2023.2.20231026 version:** 2023.2.20231026-0.amzn2023

## Docker container image
<a name="amis-2023.2.20231026.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231026-0.amzn2023`
+ `system-release-2023.2.20231026-0.amzn2023`

## Default AMI
<a name="amis-2023.2.20231026.default-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231026-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231026-0.amzn2023`
+ `system-release-2023.2.20231026-0.amzn2023`

## Minimal AMI
<a name="amis-2023.2.20231026.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231026-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231026-0.amzn2023`
+ `system-release-2023.2.20231026-0.amzn2023`

## Minimal container image
<a name="amis-2023.2.20231026.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231026-0.amzn2023`
+ `system-release-2023.2.20231026-0.amzn2023`
