---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20251105.html
---

# Amazon Linux 2023 version 2023.9.20251105 release notes
<a name="relnotes-2023.9.20251105"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.9.20251105.

**Contents**
+ [Release Summary](#release-summary-2023.9.20251105)
+ [Repository Updates](#repository-updates-2023.9.20251105)
  + [Core Updated Packages](#amis-2023.9.20251105.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.9.20251105)
  + [Default Kernel 6.1 AMI](#amis-2023.9.20251105.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.9.20251105.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.9.20251105.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.9.20251105.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.9.20251105.Default-Container)
  + [Minimal Container](#amis-2023.9.20251105.Minimal-Container)
+ [Contact us](#amis-2023.9.20251105.contact-us)

## Release Summary
<a name="release-summary-2023.9.20251105"></a>

This release represents an update to the 9th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Known Issues**
+ A change introduced in `runc-1.3.2-2.amzn2023.0.1` that changed the default tmpfs directory permissions may cause issues when launching containers. This issue has been addressed in `runc-1.3.3-2.amzn2023.0.1` released in AL2023 version `2023.9.20251110`.

## Repository Updates
<a name="repository-updates-2023.9.20251105"></a>

### Core Updated Packages
<a name="amis-2023.9.20251105.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  bind-9.18.33-1.amzn2023.0.4  |
|  runc-1.3.2-2.amzn2023.0.1  |
|  system-release-2023.9.20251105-0.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.9  |

## Image Updates
<a name="ami-updates-2023.9.20251105"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.9.20251105.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251105-0.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.4  |
|  bind-license-32:9.18.33-1.amzn2023.0.4  |
|  bind-utils-32:9.18.33-1.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.9.20251105.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251105-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.9.20251105.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251105-0.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.4  |
|  bind-license-32:9.18.33-1.amzn2023.0.4  |
|  bind-utils-32:9.18.33-1.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.9.20251105.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251105-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

### Default Container
<a name="amis-2023.9.20251105.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

### Minimal Container
<a name="amis-2023.9.20251105.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251105-0.amzn2023  |
|  system-release-2023.9.20251105-0.amzn2023  |

## Contact us
<a name="amis-2023.9.20251105.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
