---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230825.html
---

# Amazon Linux 2023 version 2023.1.20230825 release notes
<a name="relnotes-2023.1.20230825"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230825 release

## Major updates
<a name="major-updates-2023.1.20230825"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ Kernel Live Patches will fail to apply on a system where UEFI Secure Boot is enabled. This will be fixed on an upcoming release.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230825)
+ [Repository](#amis-2023.1.20230825.repository)
+ [Docker container image](#amis-2023.1.20230825.container-image)
+ [Default AMI](#amis-2023.1.20230825.default-ami)
+ [Minimal AMI](#amis-2023.1.20230825.minimal-ami)

## Repository
<a name="amis-2023.1.20230825.repository"></a>

### AL2023.1.20230825 upgrades from AL2023.1.20230823
<a name="vercmp-AL2023.1.20230823-AL2023.1.20230825"></a>

 Comparing [2023.1.20230823](relnotes-2023.1.20230823.md) to [2023.1.20230825](#relnotes-2023.1.20230825).

| Package Type | Count |
| --- | --- |
| Source | 2 |
| Total Binary | 24 |
|  noarch binary RPMs | 24 |

The full comparison of RPM package versions is below.

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2023.1.20230823 version:** 22.2.2-1.amzn2023.1.10
  - **AL2023.1.20230825 version:** 22.2.2-1.amzn2023.1.8

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230823 version:** 2023.1.20230823-0.amzn2023
  - **AL2023.1.20230825 version:** 2023.1.20230825-0.amzn2023

## Docker container image
<a name="amis-2023.1.20230825.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230825-0.amzn2023`
+ `ca-certificates-2023.2.60-1.0.amzn2023.0.3`
+ `gawk-5.1.0-3.amzn2023.0.3`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.4`
+ `system-release-2023.1.20230825-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230825.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230825-0.amzn2023` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.3` |
| `gawk-5.1.0-3.amzn2023.0.3` |
| `kernel-livepatch-repo-s3-2023.1.20230825-0.amzn2023` |
| `nspr-4.35.0-5.amzn2023.0.2` |
| `nss-softokn-freebl-3.90.0-3.amzn2023.0.2` |
| `nss-softokn-3.90.0-3.amzn2023.0.2` |
| `nss-sysinit-3.90.0-3.amzn2023.0.2` |
| `nss-util-3.90.0-3.amzn2023.0.2` |
| `nss-3.90.0-3.amzn2023.0.2` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.4` |
| `openssl-1:3.0.8-1.amzn2023.0.4` |
| `selinux-policy-targeted-36.18-1.amzn2023.0.1` |
| `selinux-policy-36.18-1.amzn2023.0.1` |
| `system-release-2023.1.20230825-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.1.20230825.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.1.20230825-0.amzn2023`
+ `ca-certificates-2023.2.60-1.0.amzn2023.0.3`
+ `gawk-5.1.0-3.amzn2023.0.3`
+ `kernel-livepatch-repo-s3-2023.1.20230825-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.4`
+ `openssl-1:3.0.8-1.amzn2023.0.4`
+ `selinux-policy-targeted-36.18-1.amzn2023.0.1`
+ `selinux-policy-36.18-1.amzn2023.0.1`
+ `system-release-2023.1.20230825-0.amzn2023`
