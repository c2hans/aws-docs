---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20251110.html
---

# Amazon Linux 2023 version 2023.9.20251110 release notes
<a name="relnotes-2023.9.20251110"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.9.20251110.

**Contents**
+ [Release Summary](#release-summary-2023.9.20251110)
+ [Repository Updates](#repository-updates-2023.9.20251110)
  + [Core New Packages](#amis-2023.9.20251110.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.9.20251110.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.9.20251110.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.9.20251110.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.9.20251110)
  + [Default Kernel 6.1 AMI](#amis-2023.9.20251110.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.9.20251110.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.9.20251110.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.9.20251110.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.9.20251110.Default-Container)
  + [Minimal Container](#amis-2023.9.20251110.Minimal-Container)
+ [Contact us](#amis-2023.9.20251110.contact-us)

## Release Summary
<a name="release-summary-2023.9.20251110"></a>

This release represents an update to the 9th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ AL2023 now supports Swift 6.2.1. You can install Swift 6.2.1 using `sudo dnf install swiftlang`.
+ Node.js v24 LTS `(nodejs24-24.11.0-1.amzn2023.0.1)` is now available in AL2023. Note that unlike Node's official binaries, these are linked against the system OpenSSL 3.2 and honor its policies.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.9.20251110"></a>

### Core New Packages
<a name="amis-2023.9.20251110.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  mount-s3-1.21.0-1.amzn2023  |
|  nodejs24-24.11.0-1.amzn2023.0.1  |
|  swiftlang-6.2.1-3.amzn2023.0.2  |

### Core Updated Packages
<a name="amis-2023.9.20251110.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-cloudwatch-agent-1.300060.1-1.amzn2023  |
|  amazon-ecr-credential-helper-0.10.1-3.amzn2023  |
|  amazon-efs-utils-2.4.0-1.amzn2023  |
|  containerd-2.1.4-1.amzn2023.0.2  |
|  dkms-3.3.0-183.amzn2023  |
|  dnf-plugin-support-info-1.9-1.amzn2023  |
|  docker-25.0.13-1.amzn2023.0.2  |
|  dwz-0.16-2.amzn2023.0.1  |
|  ecs-init-1.100.1-1.amzn2023  |
|  firefox-140.4.0-1.amzn2023.0.4  |
|  fontforge-20201107-3.amzn2023.0.4  |
|  git-lfs-3.7.1-79.amzn2023  |
|  golang-1.24.9-1.amzn2023.0.1  |
|  golist-0.10.1-11.amzn2023.0.5  |
|  kernel-6.1.158-178.288.amzn2023  |
|  kernel6.12-6.12.55-74.119.amzn2023  |
|  lasso-2.9.0-1.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  libssh-0.10.6-1.amzn2023.0.3  |
|  lustre-client-2.15.6-23.amzn2023  |
|  lz4-1.9.4-1.amzn2023.0.3  |
|  nerdctl-2.1.5-1.amzn2023.0.2  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.6  |
|  pam-1.5.1-8.amzn2023.0.7  |
|  php8.3-8.3.27-1.amzn2023.0.1  |
|  php8.4-8.4.14-1.amzn2023.0.1  |
|  python3.9-3.9.24-1.amzn2023.0.4  |
|  runc-1.3.3-2.amzn2023.0.1  |
|  runfinch-finch-1.10.0-1.amzn2023.0.5  |
|  soci-snapshotter-0.11.1-1.amzn2023.0.3  |
|  spirv-llvm-translator-15.0.5-2.amzn2023.0.1  |
|  system-release-2023.9.20251110-0.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.3  |
|  tomcat10-10.1.48-1.amzn2023.0.1  |
|  tomcat9-9.0.111-1.amzn2023.0.1  |
|  wireshark-4.4.2-1.amzn2023.0.3  |
|  xmlunit-2.8.2-6.amzn2023.0.4  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.7  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.3  |

### Kernel-livepatch New Packages
<a name="amis-2023.9.20251110.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.153-175.280-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.48-67.114-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.9.20251110.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.147-172.266-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.148-173.267-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.150-174.273-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.40-63.114-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.40-64.114-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.46-66.121-1.0-2.amzn2023  |

## Image Updates
<a name="ami-updates-2023.9.20251110"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.9.20251110.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251110-0.amzn2023  |
|  dnf-plugin-support-info-1.9-1.amzn2023  |
|  dwz-0.16-2.amzn2023.0.1  |
|  kernel-libbpf-1:6.1.158-178.288.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251110-0.amzn2023  |
|  kernel-tools-1:6.1.158-178.288.amzn2023  |
|  kernel-1:6.1.158-178.288.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.7  |
|  python3-libs-3.9.24-1.amzn2023.0.4  |
|  python3-3.9.24-1.amzn2023.0.4  |
|  system-release-2023.9.20251110-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.9.20251110.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251110-0.amzn2023  |
|  dnf-plugin-support-info-1.9-1.amzn2023  |
|  kernel-libbpf-1:6.1.158-178.288.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251110-0.amzn2023  |
|  kernel-1:6.1.158-178.288.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.7  |
|  python3-libs-3.9.24-1.amzn2023.0.4  |
|  python3-3.9.24-1.amzn2023.0.4  |
|  system-release-2023.9.20251110-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.9.20251110.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251110-0.amzn2023  |
|  dnf-plugin-support-info-1.9-1.amzn2023  |
|  dwz-0.16-2.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.9.20251110-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.55-74.119.amzn2023  |
|  kernel6.12-tools-1:6.12.55-74.119.amzn2023  |
|  kernel6.12-1:6.12.55-74.119.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.7  |
|  python3-libs-3.9.24-1.amzn2023.0.4  |
|  python3-3.9.24-1.amzn2023.0.4  |
|  system-release-2023.9.20251110-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.9.20251110.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251110-0.amzn2023  |
|  dnf-plugin-support-info-1.9-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251110-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.55-74.119.amzn2023  |
|  kernel6.12-1:6.12.55-74.119.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.7  |
|  python3-libs-3.9.24-1.amzn2023.0.4  |
|  python3-3.9.24-1.amzn2023.0.4  |
|  system-release-2023.9.20251110-0.amzn2023  |

### Default Container
<a name="amis-2023.9.20251110.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251110-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  python3-libs-3.9.24-1.amzn2023.0.4  |
|  python3-3.9.24-1.amzn2023.0.4  |
|  system-release-2023.9.20251110-0.amzn2023  |

### Minimal Container
<a name="amis-2023.9.20251110.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251110-0.amzn2023  |
|  libcap-2.73-1.amzn2023.0.4  |
|  lz4-libs-1.9.4-1.amzn2023.0.3  |
|  system-release-2023.9.20251110-0.amzn2023  |

## Contact us
<a name="amis-2023.9.20251110.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
