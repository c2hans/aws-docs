---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240117.html
---

# Amazon Linux 2023 version 2023.3.20240117 release notes
<a name="relnotes-2023.3.20240117"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240117 release

## Major updates
<a name="major-updates-2023.3.20240117"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20240117)
+ [Repository](#amis-2023.3.20240117.repository)
+ [Docker container image](#amis-2023.3.20240117.container-image)
+ [Default AMI](#amis-2023.3.20240117.default-ami)
+ [Minimal AMI](#2023.3.20240117.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240117.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240117.repository"></a>

### New packages in AL2023.3.20240117 since AL2023.3.20240108
<a name="new-AL2023.3.20240108-AL2023.3.20240117"></a>

 Comparing AL2023.3.20240108 version 2023.3.20240108 to AL2023.3.20240117 version [2023.3.20240117](#relnotes-2023.3.20240117).

| Package Type | Number of new packages in AL2023.3.20240117 compared to AL2023.3.20240108 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.3.20240117:

- ** `BabelfishDump` **
  - **RPM:**  BabelfishDump
  - **Architectures:** aarch64, x86\_64
  - **Version:** 15.5-1.amzn2023.0.1

### AL2023.3.20240117 upgrades from AL2023.3.20240108
<a name="vercmp-AL2023.3.20240108-AL2023.3.20240117"></a>

 Comparing [2023.3.20240108](relnotes-2023.3.20240108.md) to [2023.3.20240117](#relnotes-2023.3.20240117).

| Package Type | Count |
| --- | --- |
| Source | 5 |
| Total Binary | 54 |
|  noarch binary RPMs | 20 |
|  x86\_64 binary RPMs | 17 |
|  aarch64 binary RPMs | 17 |

The full comparison of RPM package versions is below.

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240108 version:** 1.8.0\_392.b08-1.amzn2023
  - **AL2023.3.20240117 version:** 1.8.0\_402.b06-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240108 version:** 11.0.21\+9-1.amzn2023
  - **AL2023.3.20240117 version:** 11.0.22\+7-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240108 version:** 17.0.9\+8-1.amzn2023.1
  - **AL2023.3.20240117 version:** 17.0.10\+7-1.amzn2023.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240108 version:** 21.0.1\+12-1.amzn2023.2
  - **AL2023.3.20240117 version:** 21.0.2\+13-1.amzn2023.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240108 version:** 2023.3.20240108-0.amzn2023
  - **AL2023.3.20240117 version:** 2023.3.20240117-0.amzn2023

## Docker container image
<a name="amis-2023.3.20240117.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240117-0.amzn2023.noarch`
+ `system-release-2023.3.20240117-0.amzn2023.noarch`

## Default AMI
<a name="amis-2023.3.20240117.default-ami"></a>
+ `amazon-linux-repo-s3-2023.3.20240117-0.amzn2023.noarch`
+ `kernel-livepatch-repo-s3-2023.3.20240117-0.amzn2023.noarch`
+ `system-release-2023.3.20240117-0.amzn2023.noarch`

## Minimal AMI
<a name="2023.3.20240117.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.3.20240117-0.amzn2023.noarch`
+ `kernel-livepatch-repo-s3-2023.3.20240117-0.amzn2023.noarch`
+ `system-release-2023.3.20240117-0.amzn2023.noarch`

## Minimal container image
<a name="amis-2023.3.20240117.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240117-0.amzn2023.noarch`
+ `system-release-2023.3.20240117-0.amzn2023.noarch`
