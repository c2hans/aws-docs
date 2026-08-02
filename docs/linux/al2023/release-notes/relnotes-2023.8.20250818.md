---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250818.html
---

# Amazon Linux 2023 version 2023.8.20250818 release notes
<a name="relnotes-2023.8.20250818"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250818.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250818)
+ [Repository Updates](#repository-updates-2023.8.20250818)
  + [Core New Packages](#amis-2023.8.20250818.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.8.20250818.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250818)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250818.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250818.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250818.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250818.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250818.Default-Container)
  + [Minimal Container](#amis-2023.8.20250818.Minimal-Container)
+ [Contact us](#amis-2023.8.20250818.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250818"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `espeak1.48.04` added. espeak is a compact, open-source software speech synthesizer that converts text into spoken voice for multiple languages.
+  `zeromq-4.3.5-1` added. ZeroMQ (also known as ØMQ, 0MQ, or zmq) is a high-performance asynchronous messaging library aimed at use in distributed or concurrent applications.
+  Javdoc sub package has been removed from `apache-commons-lang3-3.18.0` package in this release following fedora upstream.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250818"></a>

### Core New Packages
<a name="amis-2023.8.20250818.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  espeak-1.48.04-32.amzn2023  |
|  gdal310-3.10.3-3.amzn2023.0.1  |
|  geos-3.13.0-2.amzn2023.0.1  |
|  libgeotiff-1.7.3-4.amzn2023.0.1  |
|  php8.1-pecl-apcu-5.1.24-3.amzn2023.0.1  |
|  php8.1-pecl-igbinary-3.2.16-4.amzn2023.0.1  |
|  php8.1-pecl-msgpack-3.0.0-3.amzn2023.0.1  |
|  php8.1-pecl-redis6-6.2.0-1.amzn2023.0.1  |
|  php8.2-pecl-apcu-5.1.24-3.amzn2023.0.1  |
|  php8.2-pecl-igbinary-3.2.16-4.amzn2023.0.1  |
|  php8.2-pecl-msgpack-3.0.0-3.amzn2023.0.1  |
|  php8.2-pecl-redis6-6.2.0-1.amzn2023.0.1  |
|  php8.3-pecl-apcu-5.1.24-3.amzn2023.0.1  |
|  php8.3-pecl-igbinary-3.2.16-4.amzn2023.0.1  |
|  php8.3-pecl-msgpack-3.0.0-3.amzn2023.0.1  |
|  php8.3-pecl-redis6-6.2.0-1.amzn2023.0.1  |
|  php8.4-pecl-apcu-5.1.24-3.amzn2023.0.1  |
|  php8.4-pecl-igbinary-3.2.16-4.amzn2023.0.1  |
|  php8.4-pecl-msgpack-3.0.0-3.amzn2023.0.1  |
|  php8.4-pecl-redis6-6.2.0-1.amzn2023.0.1  |
|  proj-9.6.2-1.amzn2023.0.1  |
|  udunits2-2.2.28-11.amzn2023.0.1  |
|  zeromq-4.3.5-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.8.20250818.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-cloudwatch-agent-1.300057.2-1.amzn2023  |
|  apache-commons-lang3-3.18.0-1.amzn2023.0.1  |
|  cloud-init-22.2.2-1.amzn2023.1.15  |
|  ecs-init-1.97.1-1.amzn2023  |
|  firefox-140.1.0-1.amzn2023.0.2  |
|  gcc-11.5.0-5.amzn2023.0.5  |
|  gnutls-3.8.3-8.amzn2023.0.1  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.3  |
|  lustre-client-2.15.6-19.amzn2023  |
|  mod\_security-2.9.11-1.amzn2023.0.1  |
|  nginx-1.28.0-1.amzn2023.0.2  |
|  nodejs20-20.19.4-1.amzn2023.0.1  |
|  nodejs22-22.18.0-1.amzn2023.0.1  |
|  open-vm-tools-12.3.0-1.amzn2023.0.3  |
|  openexr-3.1.5-1.amzn2023.0.5  |
|  python3.11-3.11.13-1.amzn2023.0.3  |
|  python3.12-3.12.11-2.amzn2023.0.2  |
|  python3.13-3.13.3-3.amzn2023.0.6  |
|  python3.9-3.9.23-1.amzn2023.0.3  |
|  rust-1.89.0-1.amzn2023.0.1  |
|  soci-snapshotter-0.11.1-1.amzn2023.0.2  |
|  sqlite-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |
|  vim-9.1.1591-1.amzn2023.0.1  |

## Image Updates
<a name="ami-updates-2023.8.20250818"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250818.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250818-0.amzn2023  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.15  |
|  cloud-init-22.2.2-1.amzn2023.1.15  |
|  gnutls-3.8.3-8.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  python3-libs-3.9.23-1.amzn2023.0.3  |
|  python3-3.9.23-1.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |
|  vim-common-2:9.1.1591-1.amzn2023.0.1  |
|  vim-data-2:9.1.1591-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1591-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1591-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1591-1.amzn2023.0.1  |
|  xxd-2:9.1.1591-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250818.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250818-0.amzn2023  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.15  |
|  cloud-init-22.2.2-1.amzn2023.1.15  |
|  gnutls-3.8.3-8.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  python3-libs-3.9.23-1.amzn2023.0.3  |
|  python3-3.9.23-1.amzn2023.0.3  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |
|  vim-data-2:9.1.1591-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1591-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250818.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250818-0.amzn2023  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.15  |
|  cloud-init-22.2.2-1.amzn2023.1.15  |
|  gnutls-3.8.3-8.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  python3-libs-3.9.23-1.amzn2023.0.3  |
|  python3-3.9.23-1.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |
|  vim-common-2:9.1.1591-1.amzn2023.0.1  |
|  vim-data-2:9.1.1591-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1591-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1591-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1591-1.amzn2023.0.1  |
|  xxd-2:9.1.1591-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250818.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250818-0.amzn2023  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.15  |
|  cloud-init-22.2.2-1.amzn2023.1.15  |
|  gnutls-3.8.3-8.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  python3-libs-3.9.23-1.amzn2023.0.3  |
|  python3-3.9.23-1.amzn2023.0.3  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |
|  vim-data-2:9.1.1591-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1591-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.8.20250818.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  python3-libs-3.9.23-1.amzn2023.0.3  |
|  python3-3.9.23-1.amzn2023.0.3  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250818.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250818-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.3  |
|  sqlite-libs-3.40.0-1.amzn2023.0.6  |
|  system-release-2023.8.20250818-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250818.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
