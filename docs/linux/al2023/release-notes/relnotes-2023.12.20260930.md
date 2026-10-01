---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260930.html
---

# Amazon Linux 2023 version 2023.12.20260930 release notes
<a name="relnotes-2023.12.20260930"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260930.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260930)
+ [Repository Updates](#repository-updates-2023.12.20260930)
  + [Core Updated Packages](#amis-2023.12.20260930.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20260930.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260930.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260930)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260930.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260930.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260930.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260930.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260930.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260930.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260930.Default-Container)
  + [Minimal Container](#amis-2023.12.20260930.Minimal-Container)
+ [Contact us](#amis-2023.12.20260930.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260930"></a>

This release updates the 12th quarterly release of AL2023. AL2023 is the newest major version of Amazon Linux, with five years of support, deterministic updates, and optimizations for Graviton processors.

AL2023 is ready for production workloads, and you can migrate from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260930"></a>

### Core Updated Packages
<a name="amis-2023.12.20260930.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  kernel-6.1.188-233.386.amzn2023  |
|  kernel6.12-6.12.110-135.202.amzn2023  |
|  kernel6.18-6.18.51-120.163.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20260930.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.186-228.376-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.188-233.385-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.103-129.197-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.110-135.201-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.48-109.150-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.51-120.162-1.0-2.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260930.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.175-219.359-1.0-9.amzn2023  |
|  kernel-livepatch-6.1.176-220.358-1.0-9.amzn2023  |
|  kernel-livepatch-6.1.176-220.360-1.0-8.amzn2023  |
|  kernel-livepatch-6.1.176-221.360-1.0-8.amzn2023  |
|  kernel-livepatch-6.1.176-221.367-1.0-8.amzn2023  |
|  kernel-livepatch-6.1.176-223.369-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.177-224.371-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.180-225.360-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.182-227.379-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.186-228.374-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.100-125.179-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.103-127.188-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.92-122.168-1.0-9.amzn2023  |
|  kernel-livepatch-6.12.94-123.174-1.0-9.amzn2023  |
|  kernel-livepatch-6.12.94-123.176-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.94-123.180-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.94-123.190-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.94-123.192-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.95-124.187-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.35-68.129-1.0-9.amzn2023  |
|  kernel-livepatch-6.18.36-69.134-1.0-9.amzn2023  |
|  kernel-livepatch-6.18.36-69.136-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.36-69.138-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.38-73.137-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.38-76.139-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.39-79.141-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.41-94.142-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.44-99.149-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.48-107.148-1.0-4.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20260930"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260930.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel6.18-tools-1:6.18.51-120.163.amzn2023  |
|  kernel6.18-1:6.18.51-120.163.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260930.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel6.18-1:6.18.51-120.163.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260930.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel6.12-tools-1:6.12.110-135.202.amzn2023  |
|  kernel6.12-1:6.12.110-135.202.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260930.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel6.12-1:6.12.110-135.202.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260930.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-tools-1:6.1.188-233.386.amzn2023  |
|  kernel-1:6.1.188-233.386.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260930.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260930-0.amzn2023  |
|  kernel-1:6.1.188-233.386.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20260930.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260930-0.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260930.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260930-0.amzn2023  |
|  system-release-2023.12.20260930-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260930.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
