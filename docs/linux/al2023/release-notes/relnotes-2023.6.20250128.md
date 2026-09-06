---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250128.html
---

# Amazon Linux 2023 version 2023.6.20250128 release notes
<a name="relnotes-2023.6.20250128"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250128.

**Topics**
+ [Major updates](#major-updates-2023.6.20250128)
+ [Repository](#amis-2023.6.20250128.repository)
+ [Docker container image](#amis-2023.6.20250128.container-image)
+ [Default AMI](#amis-2023.6.20250128.default-ami)
+ [Minimal AMI](#amis-2023.6.20250128.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250128.minimal-container-ami)
+ [Contact us](#amis-2023.6.20250128.contact-us)

## Major updates
<a name="major-updates-2023.6.20250128"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250128.repository"></a>

### AL2023.6.20250128 upgrades from AL2023.6.20250123
<a name="vercmp-AL2023.6.20250123-AL2023.6.20250128"></a>

 Comparing [2023.6.20250123](relnotes-2023.6.20250123.md) to [2023.6.20250128](#relnotes-2023.6.20250128).

| Package Type | Count |
| --- | --- |
| Source | 2 |
| Total Binary | 24 |
|  noarch binary RPMs | 20 |
|  x86\_64 binary RPMs | 2 |
|  aarch64 binary RPMs | 2 |

The full comparison of RPM package versions is below.

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250123 version:** 2.15.3-1.amzn2023.0.6
  - **AL2023.6.20250128 version:** 2.15.3-1.amzn2023.0.7

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250123 version:** 2023.6.20250123-0.amzn2023
  - **AL2023.6.20250128 version:** 2023.6.20250128-0.amzn2023

## Docker container image
<a name="amis-2023.6.20250128.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250128-0.amzn2023 |
| system-release-2023.6.20250128-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20250128.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250128-0.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250128-0.amzn2023 |
| system-release-2023.6.20250128-0.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20250128.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250128-0.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250128-0.amzn2023 |
| system-release-2023.6.20250128-0.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20250128.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250128-0.amzn2023 |
| system-release-2023.6.20250128-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20250128.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
