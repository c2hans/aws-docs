---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250721.html
---

# Amazon Linux 2023 version 2023.8.20250721 release notes
<a name="relnotes-2023.8.20250721"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250721.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250721)
+ [Important Advisory Notice](#important-advisory-notice-2023.8.20250721)
  + [AL2023 Core](#al2023-core-advisories-2023.8.20250721)
  + [AL2023 Kernel-Livepatch](#al2023-kernel-livepatch-advisories-2023.8.20250721)
+ [Repository Updates](#repository-updates-2023.8.20250721)
  + [Core New Packages](#amis-2023.8.20250721.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.8.20250721.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.8.20250721.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.8.20250721.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250721)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250721.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250721.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250721.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250721.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250721.Default-Container)
  + [Minimal Container](#amis-2023.8.20250721.Minimal-Container)
+ [Contact us](#amis-2023.8.20250721.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250721"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  **kernel6.12 package renaming:** `kernel6.12` subpackages have been renamed and the RPM epoch for the 6.1 `kernel` and `kernel6.12` have been increased to 1. This has an effect on the update process for customers of the 6.12 kernel. Kernel subpackages need to be explicitly swapped to their corresponding 6.12 packages that now carry a different name which includes the major version `6.12`. Please refer to the [update documentation for kernel6.12](https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html).
**Note**
 From now on customers that need the kernel development package for `kernel6.12` need to install `kernel6.12-devel`.
+  AL2023 kernel-6.1 and kernel-6.12 enabled with CONFIG\_LRU\_GEN feature

**Security updates**
+ For information on the CVEs addressed in the previous release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Important Advisory Notice
<a name="important-advisory-notice-2023.8.20250721"></a>

The security advisories associated with the packages in this release are missing from the repository metadata and ALAS website. As a result, systems relying on repository metadata to track or apply security updates (ie: "dnf/yum update --security") will not be aware of the new updates available in this release. Systems leveraging the latest AMIs will have the latest updates.

We understand the importance of security visibility and compliance, and we are actively working to resolve this issue. A follow-up release that includes the repository metadata will be published during the week of July 28, 2025.

The full list of CVEs that are fixed with this release include:

### AL2023 Core
<a name="al2023-core-advisories-2023.8.20250721"></a>

| New Package NVR | Old Package NVR | CVE(s) |
| --- | --- | --- |
| bind-9.18.33-1.amzn2023.0.3 | bind-9.18.33-1.amzn2023.0.2 | CVE-2025-40777 |
| ecs-init-1.96.0-1.amzn2023 | ecs-init-1.95.0-1.amzn2023 | CVE-2025-22874, CVE-2025-4673 |
| git-2.50.1-1.amzn2023.0.1 | git-2.47.1-1.amzn2023.0.3 | CVE-2025-27613, CVE-2025-27614, CVE-2025-46835, CVE-2025-48384, CVE-2025-48385 |
| gnupg2-2.3.7-1.amzn2023.0.5 | gnupg2-2.3.7-1.amzn2023.0.4 | CVE-2025-30258 |
| golang-1.24.5-1.amzn2023.0.1 | golang-1.24.4-1.amzn2023.0.1 | CVE-2025-4674 |
| java-1.8.0-amazon-corretto-1.8.0\_462.b08-1.amzn2023 | java-1.8.0-amazon-corretto-1.8.0\_452.b09-2.amzn2023 | CVE-2025-30749, CVE-2025-30754, CVE-2025-30761, CVE-2025-50106 |
| java-11-amazon-corretto-11.0.28\+6-1.amzn2023 | java-11-amazon-corretto-11.0.27\+6-1.amzn2023 | CVE-2025-30749, CVE-2025-30754, CVE-2025-30761, CVE-2025-50059, CVE-2025-50106 |
| java-17-amazon-corretto-17.0.16\+8-1.amzn2023.1 | java-17-amazon-corretto-17.0.15\+6-1.amzn2023.1 | CVE-2025-30749, CVE-2025-30754, CVE-2025-50059, CVE-2025-50106 |
| java-21-amazon-corretto-21.0.8\+9-1.amzn2023.1 | java-21-amazon-corretto-21.0.7\+6-1.amzn2023.1 | CVE-2025-30749, CVE-2025-30754, CVE-2025-50059, CVE-2025-50106 |
| java-24-amazon-corretto-24.0.2\+12-1.amzn2023.1 | java-24-amazon-corretto-24.0.1\+9-1.amzn2023.1 | CVE-2025-30749, CVE-2025-30754, CVE-2025-50059, CVE-2025-50106 |
| jq-1.7.1-50.amzn2023 | jq-1.7.1-49.amzn2023.0.2 | CVE-2024-23337 |
| kernel-6.1.144-170.251.amzn2023 | kernel-6.1.141-165.249.amzn2023 | CVE-2024-36913, CVE-2024-41013, CVE-2024-57883, CVE-2025-37807, CVE-2025-37958 |
| libarchive-3.7.4-2.amzn2023.0.4 | libarchive-3.7.4-2.amzn2023.0.3 | CVE-2025-5915, CVE-2025-5917 |
| libxml2-2.10.4-1.amzn2023.0.12 | libxml2-2.10.4-1.amzn2023.0.11 | CVE-2025-49794, CVE-2025-49795, CVE-2025-49796 |
| mtr-0.95-3.amzn2023.0.2 | mtr-0.95-3.amzn2023.0.1 | CVE-2025-49809 |
| php8.1-8.1.33-1.amzn2023.0.1 | php8.1-8.1.32-1.amzn2023.0.1 | CVE-2025-1220, CVE-2025-1735, CVE-2025-6491 |
| php8.2-8.2.29-1.amzn2023.0.1 | php8.2-8.2.28-1.amzn2023.0.1 | CVE-2025-1220, CVE-2025-1735, CVE-2025-6491 |
| php8.3-8.3.23-1.amzn2023.0.1 | php8.3-8.3.22-1.amzn2023.0.1 | CVE-2025-1220, CVE-2025-1735, CVE-2025-6491 |
| php8.4-8.4.10-1.amzn2023.0.1 | php8.4-8.4.8-1.amzn2023.0.1 | CVE-2025-1220, CVE-2025-1735, CVE-2025-6491 |
| python-pip-21.3.1-2.amzn2023.0.13 | python-pip-21.3.1-2.amzn2023.0.12 | CVE-2025-50181 |
| python-requests-2.25.1-1.amzn2023.0.6 | python-requests-2.25.1-1.amzn2023.0.5 | CVE-2024-47081 |
| python3.11-3.11.13-1.amzn2023.0.2 | python3.11-3.11.12-2.amzn2023.0.2 | CVE-2025-6069 |
| python3.11-pip-22.3.1-2.amzn2023.0.7 | python3.11-pip-22.3.1-2.amzn2023.0.6 | CVE-2024-47081, CVE-2025-50181 |
| python3.12-pip-23.2.1-4.amzn2023.0.5 | python3.12-pip-23.2.1-4.amzn2023.0.3 | CVE-2025-50181 |
| python3.9-3.9.23-1.amzn2023.0.2 | python3.9-3.9.22-1.amzn2023.0.2 | CVE-2025-6069 |
| ruby3.2-3.2.8-184.amzn2023.0.2 | ruby3.2-3.2.8-184.amzn2023.0.1 | CVE-2025-6442 |
| rust-1.88.0-1.amzn2023.0.2 | rust-1.87.0-1.amzn2023.0.1 | CVE-2025-53605 |
| tomcat10-10.1.43-1.amzn2023.0.1 | tomcat10-10.1.42-1.amzn2023.0.1 | CVE-2025-53506 |
| tomcat9-9.0.107-1.amzn2023.0.1 | tomcat9-9.0.106-1.amzn2023.0.1 | CVE-2025-52434, CVE-2025-53506 |

### AL2023 Kernel-Livepatch
<a name="al2023-kernel-livepatch-advisories-2023.8.20250721"></a>

| New Package NVR | Old Package NVR | CVE(s) |
| --- | --- | --- |
| kernel-livepatch-6.1.140-154.222-1.0-1.amzn2023 | This is a new addition | CVE-2025-38000, CVE-2025-38003 |
| kernel-livepatch-6.12.25-32.101-1.0-1.amzn2023 | This is a new addition | CVE-2025-38037 |
| kernel-livepatch-6.12.29-33.102-1.0-1.amzn2023 | This is a new addition | CVE-2025-38037 |
| kernel-livepatch-6.12.30-34.92-1.0-1.amzn2023 | This is a new addition | CVE-2025-38037 |
| kernel-livepatch-6.1.134-150.224-1.0-3.amzn2023 | kernel-livepatch-6.1.134-150.224-1.0-2.amzn2023 | CVE-2025-38000, CVE-2025-38003 |
| kernel-livepatch-6.1.134-152.225-1.0-3.amzn2023 | kernel-livepatch-6.1.134-152.225-1.0-2.amzn2023 | CVE-2025-38000, CVE-2025-38003 |

## Repository Updates
<a name="repository-updates-2023.8.20250721"></a>

### Core New Packages
<a name="amis-2023.8.20250721.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  python3.13-3.13.3-3.amzn2023.0.4  |
|  python3.13-flit-core-3.9.0-9.amzn2023.0.3  |
|  python3.13-packaging-24.2-92.amzn2023  |
|  python3.13-pip-24.2-259.amzn2023.0.1  |
|  python3.13-setuptools-69.2.0-382.amzn2023  |
|  python3.13-wheel-0.43.0-103.amzn2023  |

### Core Updated Packages
<a name="amis-2023.8.20250721.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.0-1.amzn2023.0.1  |
|  aws-cfn-bootstrap-2.0-35.amzn2023  |
|  bind-9.18.33-1.amzn2023.0.3  |
|  ecs-init-1.96.0-1.amzn2023  |
|  git-2.50.1-1.amzn2023.0.1  |
|  gnome-control-center-47.3-196.amzn2023  |
|  gnupg2-2.3.7-1.amzn2023.0.5  |
|  golang-1.24.5-1.amzn2023.0.1  |
|  java-1.8.0-amazon-corretto-1.8.0\_462.b08-1.amzn2023  |
|  java-11-amazon-corretto-11.0.28\+6-1.amzn2023  |
|  java-17-amazon-corretto-17.0.16\+8-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.8\+9-1.amzn2023.1  |
|  java-24-amazon-corretto-24.0.2\+12-1.amzn2023.1  |
|  jq-1.7.1-50.amzn2023  |
|  kernel-6.1.144-170.251.amzn2023  |
|  kernel6.12-6.12.37-61.105.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libsigc\+\+30-3.6.0-3.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  mtr-0.95-3.amzn2023.0.2  |
|  nerdctl-2.1.3-1.amzn2023.0.1  |
|  php8.1-8.1.33-1.amzn2023.0.1  |
|  php8.2-8.2.29-1.amzn2023.0.1  |
|  php8.3-8.3.23-1.amzn2023.0.1  |
|  php8.4-8.4.10-1.amzn2023.0.1  |
|  python-pip-21.3.1-2.amzn2023.0.13  |
|  python-requests-2.25.1-1.amzn2023.0.6  |
|  python3.11-3.11.13-1.amzn2023.0.2  |
|  python3.11-pip-22.3.1-2.amzn2023.0.7  |
|  python3.12-pip-23.2.1-4.amzn2023.0.5  |
|  python3.9-3.9.23-1.amzn2023.0.2  |
|  ruby3.2-3.2.8-184.amzn2023.0.2  |
|  runfinch-finch-1.10.0-1.amzn2023.0.1  |
|  rust-1.88.0-1.amzn2023.0.2  |
|  showtime-48.1-10.amzn2023  |
|  soci-snapshotter-0.11.1-1.amzn2023.0.1  |
|  system-release-2023.8.20250721-0.amzn2023  |
|  systemtap-5.2-1.amzn2023.0.5  |
|  tomcat10-10.1.43-1.amzn2023.0.1  |
|  tomcat9-9.0.107-1.amzn2023.0.1  |

### Kernel-livepatch New Packages
<a name="amis-2023.8.20250721.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.140-154.222-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.25-32.101-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.29-33.102-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.30-34.92-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.8.20250721.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.134-150.224-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.134-152.225-1.0-3.amzn2023  |

## Image Updates
<a name="ami-updates-2023.8.20250721"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250721.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.8.20250721-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-35.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.3  |
|  bind-license-32:9.18.33-1.amzn2023.0.3  |
|  bind-utils-32:9.18.33-1.amzn2023.0.3  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  jq-1.7.1-50.amzn2023  |
|  kernel-libbpf-1:6.1.144-170.251.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250721-0.amzn2023  |
|  kernel-tools-1:6.1.144-170.251.amzn2023  |
|  kernel-1:6.1.144-170.251.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  python3-libs-3.9.23-1.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.13  |
|  python3-requests-2.25.1-1.amzn2023.0.6  |
|  python3-3.9.23-1.amzn2023.0.2  |
|  rust-toolset-srpm-macros-1.88.0-1.amzn2023.0.2  |
|  system-release-2023.8.20250721-0.amzn2023  |
|  systemtap-runtime-5.2-1.amzn2023.0.5  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250721.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.8.20250721-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  jq-1.7.1-50.amzn2023  |
|  kernel-libbpf-1:6.1.144-170.251.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250721-0.amzn2023  |
|  kernel-1:6.1.144-170.251.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  python3-libs-3.9.23-1.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.13  |
|  python3-requests-2.25.1-1.amzn2023.0.6  |
|  python3-3.9.23-1.amzn2023.0.2  |
|  system-release-2023.8.20250721-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250721.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.8.20250721-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-35.amzn2023  |
|  bind-libs-32:9.18.33-1.amzn2023.0.3  |
|  bind-license-32:9.18.33-1.amzn2023.0.3  |
|  bind-utils-32:9.18.33-1.amzn2023.0.3  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  jq-1.7.1-50.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250721-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.37-61.105.amzn2023  |
|  kernel6.12-tools-1:6.12.37-61.105.amzn2023  |
|  kernel6.12-1:6.12.37-61.105.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  python3-libs-3.9.23-1.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.13  |
|  python3-requests-2.25.1-1.amzn2023.0.6  |
|  python3-3.9.23-1.amzn2023.0.2  |
|  rust-toolset-srpm-macros-1.88.0-1.amzn2023.0.2  |
|  system-release-2023.8.20250721-0.amzn2023  |
|  systemtap-runtime-5.2-1.amzn2023.0.5  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250721.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.8.20250721-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  jq-1.7.1-50.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250721-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.37-61.105.amzn2023  |
|  kernel6.12-1:6.12.37-61.105.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  python3-libs-3.9.23-1.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.13  |
|  python3-requests-2.25.1-1.amzn2023.0.6  |
|  python3-3.9.23-1.amzn2023.0.2  |
|  system-release-2023.8.20250721-0.amzn2023  |

### Default Container
<a name="amis-2023.8.20250721.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250721-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  python3-libs-3.9.23-1.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.13  |
|  python3-3.9.23-1.amzn2023.0.2  |
|  system-release-2023.8.20250721-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250721.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250721-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.5  |
|  libarchive-3.7.4-2.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.12  |
|  system-release-2023.8.20250721-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250721.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
