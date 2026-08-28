---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250512.html
---

# Amazon Linux 2023 version 2023.7.20250512 release notes
<a name="relnotes-2023.7.20250512"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250512.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250512)
+ [Repository Updates](#repository-updates-2023.7.20250512)
  + [Core New Packages](#amis-2023.7.20250512.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.7.20250512.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.7.20250512)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250512.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250512.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250512.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250512.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.7.20250512.Default-Container)
  + [Minimal Container](#amis-2023.7.20250512.Minimal-Container)
+ [Contact us](#amis-2023.7.20250512.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250512"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Notable updates**
+  nodejs-18.20.8-1.amzn2023.0.1: A priority in `alternatives` has been dropped to be similar with `nodejs20` and `nodejs22`, so all three NodeJS packages have the same priority.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250512"></a>

### Core New Packages
<a name="amis-2023.7.20250512.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  erofs-utils-1.8.6-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.7.20250512.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-cloudwatch-agent-1.300054.1-2.amzn2023  |
|  clang-15.0.7-3.amzn2023.0.4  |
|  ecs-init-1.93.0-1.amzn2023  |
|  elfutils-0.188-3.amzn2023.0.3  |
|  gnuplot-5.4.3-3.amzn2023.0.4  |
|  golist-0.10.1-11.amzn2023.0.4  |
|  grub2-2.06-61.amzn2023.0.18  |
|  ibus-1.5.31-1.amzn2023.0.2  |
|  java-1.8.0-amazon-corretto-1.8.0\_452.b09-2.amzn2023  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.5  |
|  kernel-6.1.134-152.225.amzn2023  |
|  kernel6.12-6.12.25-32.101.amzn2023  |
|  libsoup-2.72.0-6.amzn2023.0.5  |
|  libsoup3-3.6.5-48.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  nodejs-18.20.8-1.amzn2023.0.1  |
|  nodejs20-20.19.1-1.amzn2023.0.1  |
|  nodejs22-22.14.0-1.amzn2023.0.2  |
|  openvpn-2.6.12-1.amzn2023.0.2  |
|  php8.3-8.3.20-1.amzn2023.0.1  |
|  php8.4-8.4.6-1.amzn2023.0.1  |
|  python-lit-18.1.8-1.amzn2023.0.1  |
|  python3.11-3.11.12-2.amzn2023.0.1  |
|  python3.12-3.12.10-2.amzn2023.0.1  |
|  python3.9-3.9.22-1.amzn2023.0.1  |
|  ruby3.2-3.2.8-184.amzn2023.0.1  |
|  sqlite-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |
|  tomcat10-10.1.40-1.amzn2023.0.1  |
|  tomcat9-9.0.104-1.amzn2023.0.1  |

## Image Updates
<a name="ami-updates-2023.7.20250512"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250512.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250512-0.amzn2023  |
|  elfutils-debuginfod-client-0.188-3.amzn2023.0.3  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.3  |
|  elfutils-libelf-0.188-3.amzn2023.0.3  |
|  elfutils-libs-0.188-3.amzn2023.0.3  |
|  grub2-common-1:2.06-61.amzn2023.0.18  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.18  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-1:2.06-61.amzn2023.0.18  |
|  kernel-libbpf-6.12.25-32.101.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250512-0.amzn2023  |
|  kernel-tools-6.12.25-32.101.amzn2023  |
|  kernel-6.1.134-152.225.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  python3-libs-3.9.22-1.amzn2023.0.1  |
|  python3-3.9.22-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250512.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250512-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.3  |
|  elfutils-libelf-0.188-3.amzn2023.0.3  |
|  elfutils-libs-0.188-3.amzn2023.0.3  |
|  grub2-common-1:2.06-61.amzn2023.0.18  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.18  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-1:2.06-61.amzn2023.0.18  |
|  kernel-libbpf-6.12.25-32.101.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250512-0.amzn2023  |
|  kernel-6.1.134-152.225.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  python3-libs-3.9.22-1.amzn2023.0.1  |
|  python3-3.9.22-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250512.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250512-0.amzn2023  |
|  elfutils-debuginfod-client-0.188-3.amzn2023.0.3  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.3  |
|  elfutils-libelf-0.188-3.amzn2023.0.3  |
|  elfutils-libs-0.188-3.amzn2023.0.3  |
|  grub2-common-1:2.06-61.amzn2023.0.18  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.18  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-1:2.06-61.amzn2023.0.18  |
|  kernel-libbpf-6.12.25-32.101.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250512-0.amzn2023  |
|  kernel-tools-6.12.25-32.101.amzn2023  |
|  kernel6.12-6.12.25-32.101.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  python3-libs-3.9.22-1.amzn2023.0.1  |
|  python3-3.9.22-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250512.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250512-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.3  |
|  elfutils-libelf-0.188-3.amzn2023.0.3  |
|  elfutils-libs-0.188-3.amzn2023.0.3  |
|  grub2-common-1:2.06-61.amzn2023.0.18  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.18  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.18  |
|  grub2-tools-1:2.06-61.amzn2023.0.18  |
|  kernel-libbpf-6.12.25-32.101.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250512-0.amzn2023  |
|  kernel6.12-6.12.25-32.101.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  python3-libs-3.9.22-1.amzn2023.0.1  |
|  python3-3.9.22-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

### Default Container
<a name="amis-2023.7.20250512.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250512-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.3  |
|  elfutils-libelf-0.188-3.amzn2023.0.3  |
|  elfutils-libs-0.188-3.amzn2023.0.3  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  python3-libs-3.9.22-1.amzn2023.0.1  |
|  python3-3.9.22-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250512.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250512-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250512-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250512.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
