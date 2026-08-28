---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241212.html
---

# Amazon Linux 2023 version 2023.6.20241212 release notes
<a name="relnotes-2023.6.20241212"></a>

**Note**
 This release fixes a bug introduced in the recalled [AL2023.6.20241209](relnotes-2023.6.20241209.md) release. The bug was introduced in an update to the `python3.9` package which prevented the use of `venv` as described in [this GitHub issue](https://github.com/amazonlinux/amazon-linux-2023/issues/861).
 Customers who updated to the [AL2023.6.20241209](relnotes-2023.6.20241209.md) release are advised to update to this release to resolve the issue.
 This release contains all other changes present in the [AL2023.6.20241209](relnotes-2023.6.20241209.md) release.

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20241212.

**Topics**
+ [Major updates](#major-updates-2023.6.20241212)
+ [Repository](#amis-2023.6.20241212.repository)
+ [Docker container image](#amis-2023.6.20241212.container-image)
+ [Default AMI](#amis-2023.6.20241212.default-ami)
+ [Minimal AMI](#amis-2023.6.20241212.minimal-ami)
+ [Minimal container image](#amis-2023.6.20241212.minimal-container-ami)
+ [Contact us](#amis-2023.6.20241212.contact-us)

## Major updates
<a name="major-updates-2023.6.20241212"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ This release fixes a bug introduced in the recalled [AL2023.6.20241209](relnotes-2023.6.20241209.md) release. The bug was introduced in an update to the `python3.9` package which prevented the use of `venv` as described in [this GitHub issue](https://github.com/amazonlinux/amazon-linux-2023/issues/861).
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20241212.repository"></a>

### AL2023.6.20241212 upgrades from AL2023.6.20241209
<a name="vercmp-AL2023.6.20241209-AL2023.6.20241212"></a>

 Comparing [2023.6.20241209](relnotes-2023.6.20241209.md) to [2023.6.20241212](#relnotes-2023.6.20241212).

| Package Type | Count |
| --- | --- |
| Source | 2 |
| Total Binary | 38 |
|  noarch binary RPMs | 24 |
|  x86\_64 binary RPMs | 7 |
|  aarch64 binary RPMs | 7 |

The full comparison of RPM package versions is below.

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.6.20241209 version:** 3.9.20-1.amzn2023.0.1
  - **AL2023.6.20241212 version:** 3.9.20-1.amzn2023.0.2

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20241209 version:** 2023.6.20241209-0.amzn2023
  - **AL2023.6.20241212 version:** 2023.6.20241212-0.amzn2023

## Docker container image
<a name="amis-2023.6.20241212.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241209-0.amzn2023 |
| glib2-2.82.2-764.amzn2023  |
| libxml2-2.10.4-1.amzn2023.0.7  |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-3.9.20-1.amzn2023.0.1  |
| system-release-2023.6.20241209-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20241212.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241209-0.amzn2023 |
| awscli-2-2.17.18-1.amzn2023.0.1 |
| cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.13 |
| cloud-init-22.2.2-1.amzn2023.1.13 |
| dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| dnf-utils-4.3.0-13.amzn2023.0.5 |
| glib2-2.82.2-764.amzn2023 |
| kernel-libbpf-6.1.119-129.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241209-0.amzn2023 |
| kernel-tools-6.1.119-129.201.amzn2023 |
| kernel-6.1.119-129.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| microcode\_ctl-2:2.1-53.amzn2023.0.10 |
| python3-dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-requests-2.25.1-1.amzn2023.0.4  |
| python3-3.9.20-1.amzn2023.0.1 |
| system-release-2023.6.20241209-0.amzn2023 |
| update-motd-2.3-1.amzn2023 |

## Minimal AMI
<a name="amis-2023.6.20241212.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241209-0.amzn2023 |
| awscli-2-2.17.18-1.amzn2023.0.1 |
| cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.13 |
| cloud-init-22.2.2-1.amzn2023.1.13 |
| dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| glib2-2.82.2-764.amzn2023 |
| kernel-libbpf-6.1.119-129.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20241209-0.amzn2023 |
| kernel-6.1.119-129.201.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| python3-dnf-plugins-core-4.3.0-13.amzn2023.0.5 |
| python3-libs-3.9.20-1.amzn2023.0.1  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.10  |
| python3-requests-2.25.1-1.amzn2023.0.4  |
| python3-3.9.20-1.amzn2023.0.1 |
| system-release-2023.6.20241209-0.amzn2023 |
| update-motd-2.3-1.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20241212.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241209-0.amzn2023 |
| glib2-2.82.2-764.amzn2023 |
| gobject-introspection-1.82.0-1.amzn2023 |
| libxml2-2.10.4-1.amzn2023.0.7 |
| system-release-2023.6.20241209-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20241212.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
