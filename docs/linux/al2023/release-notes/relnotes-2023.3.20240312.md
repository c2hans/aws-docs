---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240312.html
---

# Amazon Linux 2023 version 2023.3.20240312 release notes
<a name="relnotes-2023.3.20240312"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240312 release

## Major updates
<a name="major-updates-2023.3.20240312"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20240312)
+ [Repository](#amis-2023.3.20240312.repository)
+ [Docker container image](#amis-2023.3.20240312.container-image)
+ [Default AMI](#amis-2023.3.20240312.default-ami)
+ [Minimal AMI](#amis-2023.3.20240312.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240312.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240312.repository"></a>

### AL2023.3.20240312 upgrades from AL2023.3.20240304
<a name="vercmp-AL2023.3.20240304-AL2023.3.20240312"></a>

 Comparing [2023.3.20240304](relnotes-2023.3.20240304.md) to [2023.3.20240312](#relnotes-2023.3.20240312).

| Package Type | Count |
| --- | --- |
| Source | 1 |
| Total Binary | 20 |
|  noarch binary RPMs | 20 |

The full comparison of RPM package versions is below.

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240304 version:** 2023.3.20240304-0.amzn2023
  - **AL2023.3.20240312 version:** 2023.3.20240312-0.amzn2023

## Docker container image
<a name="amis-2023.3.20240312.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240312-0.amzn2023`
+ `system-release-2023.3.20240312-0.amzn2023`

## Default AMI
<a name="amis-2023.3.20240312.default-ami"></a>
+ `amazon-linux-repo-s3-2023.3.20240312-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.3.20240312-0.amzn2023`
+ `system-release-2023.3.20240312-0.amzn2023`

## Minimal AMI
<a name="amis-2023.3.20240312.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.3.20240312-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.3.20240312-0.amzn2023`
+ `system-release-2023.3.20240312-0.amzn2023`

## Minimal container image
<a name="amis-2023.3.20240312.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240312-0.amzn2023`
+ `system-release-2023.3.20240312-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
