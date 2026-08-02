---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240916.html
---

# Amazon Linux 2023 version 2023.5.20240916 release notes
<a name="relnotes-2023.5.20240916"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240916.

**Topics**
+ [Major updates](#major-updates-2023.5.20240916)
+ [Repository](#amis-2023.5.20240916.repository)
+ [Docker container image](#amis-2023.5.20240916.container-image)
+ [Default AMI](#amis-2023.5.20240916.default-ami)
+ [Minimal AMI](#amis-2023.5.20240916.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240916.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240916.contact-us)

## Major updates
<a name="major-updates-2023.5.20240916"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Notable updates**
+  The crash package was updated to version 8.0.4-2 to address an incompatibility with kernel-6.1.109-118.189 and newer. Customers using recommended options to update Amazon Linux 2023, such as booting into an updated AMI or using the dnf upgrade feature, will automatically receive an updated, compatible crash packages. Customers installing security updates only and wishing to continue to use the crash utility need to upgrade it to crash-8.0.4-2 or later.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240916.repository"></a>

### AL2023.5.20240916 upgrades from AL2023.5.20240903
<a name="vercmp-AL2023.5.20240903-AL2023.5.20240916"></a>

 Comparing [2023.5.20240903](relnotes-2023.5.20240903.md) to [2023.5.20240916](#relnotes-2023.5.20240916).

| Package Type | Count |
| --- | --- |
| Source | 8 |
| Total Binary | 88 |
|  noarch binary RPMs | 32 |
|  x86\_64 binary RPMs | 28 |
|  aarch64 binary RPMs | 28 |

The full comparison of RPM package versions is below.

- ** `appstream-data` **
  - **RPM:**  appstream-data
  - **Architectures:** noarch
  - **AL2023.5.20240903 version:** 34-3.amzn2023.0.2
  - **AL2023.5.20240916 version:** 2023-1.amzn2023

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240903 version:** 1.3.2-0.amzn2023
  - **AL2023.5.20240916 version:** 1.3.3-0.amzn2023

- ** `crash` **
  - **RPM:**  crash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  crash-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240903 version:** 8.0.2-3.amzn2023.0.1
  - **AL2023.5.20240916 version:** 8.0.4-2.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240903 version:** 1.86.2-1.amzn2023
  - **AL2023.5.20240916 version:** 1.86.3-1.amzn2023

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
  - **AL2023.5.20240903 version:** 6.1.106-116.188.amzn2023
  - **AL2023.5.20240916 version:** 6.1.109-118.189.amzn2023

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240903 version:** 1.7.6-1.amzn2023.0.1
  - **AL2023.5.20240916 version:** 1.7.6-1.amzn2023.0.2

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
  - **AL2023.5.20240903 version:** 1.24.0-1.amzn2023.0.3
  - **AL2023.5.20240916 version:** 1.24.0-1.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240903 version:** 2023.5.20240903-0.amzn2023
  - **AL2023.5.20240916 version:** 2023.5.20240916-0.amzn2023

## Docker container image
<a name="amis-2023.5.20240916.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240819-0.amzn2023` |
| `libarchive-3.7.4-2.amzn2023.0.1` |
| `system-release-2023.5.20240819-0.amzn2023` |

## Default AMI
<a name="amis-2023.5.20240916.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240916-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240916-0.amzn2023` |
| `kernel-tools-6.1.109-118.189.amzn2023` |
| `kernel-6.1.109-118.189.amzn2023` |
| `system-release-2023.5.20240916-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.5.20240916.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240916-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240916-0.amzn2023` |
| `kernel-6.1.109-118.189.amzn2023` |
| `system-release-2023.5.20240916-0.amzn2023` |

## Minimal container image
<a name="amis-2023.5.20240916.minimal-container-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240916-0.amzn2023` |
| `system-release-2023.5.20240916-0.amzn2023` |

## Contact us
<a name="amis-2023.5.20240916.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
