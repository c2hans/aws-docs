---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250428.html
---

# Amazon Linux 2023 version 2023.7.20250428 release notes
<a name="relnotes-2023.7.20250428"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250428.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250428)
+ [Repository Updates](#repository-updates-2023.7.20250428)
  + [Core New Packages](#amis-2023.7.20250428.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.7.20250428.Core-Updated-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.7.20250428.Kernel-livepatch-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.7.20250428.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.7.20250428)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250428.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250428.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250428.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250428.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.7.20250428.Default-Container)
  + [Minimal Container](#amis-2023.7.20250428.Minimal-Container)
+ [Contact us](#amis-2023.7.20250428.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250428"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250428"></a>

### Core New Packages
<a name="amis-2023.7.20250428.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  composer-generators-0.1.2-1.amzn2023.0.1  |
|  gnome-calculator-47.2-1.amzn2023.0.1  |
|  libgee-0.20.6-7.amzn2023.0.1  |
|  mariadb1011-10.11.11-1.amzn2023.0.1  |
|  network-flow-monitor-agent-0.1.3-1.amzn2023.0.1  |
|  python-docker-6.1.3-3.amzn2023.0.2  |
|  python-websocket-client-1.7.0-4.amzn2023  |
|  python-websockets-12.0-5.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.7.20250428.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-efs-utils-2.3.0-1.amzn2023  |
|  amazon-rpm-config-228-9.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.1957.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-34.amzn2023  |
|  binutils-2.41-50.amzn2023.0.3  |
|  curl-8.5.0-1.amzn2023.0.5  |
|  debugedit-5.0-7.amzn2023.0.1  |
|  docker-25.0.8-1.amzn2023.0.3  |
|  ecs-init-1.92.0-1.amzn2023  |
|  firefox-128.9.0-1.amzn2023.0.1  |
|  gcc-11.5.0-5.amzn2023.0.4  |
|  java-11-amazon-corretto-11.0.27\+6-1.amzn2023  |
|  java-17-amazon-corretto-17.0.15\+6-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.7\+6-1.amzn2023.1  |
|  java-24-amazon-corretto-24.0.1\+9-1.amzn2023.1  |
|  kernel-6.1.134-150.224.amzn2023  |
|  kernel6.12-6.12.23-29.97.amzn2023  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libsoup-2.72.0-6.amzn2023.0.4  |
|  libsoup3-3.6.5-47.amzn2023  |
|  nodejs20-20.19.0-1.amzn2023.0.1  |
|  perl-Math-BigRat-0.2624-500.amzn2023.0.2  |
|  perl-bignum-0.66-501.amzn2023.0.1  |
|  postgresql-odbc-17.00.0004-1.amzn2023.0.1  |
|  python3.12-pip-23.2.1-4.amzn2023.0.2  |
|  redis6-6.2.14-2.amzn2023.0.4  |
|  ruby3.2-3.2.7-183.amzn2023.0.6  |
|  runfinch-finch-1.7.2-1.amzn2023.0.1  |
|  system-release-2023.7.20250428-0.amzn2023  |
|  valkey-8.0.2-3.amzn2023.0.1  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.7.20250428.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.127-135.201-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.128-136.201-1.0-5.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.7.20250428.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-compat-12-8-570.133.20-1.amzn2023  |
|  cuda-drivers-570.133.20-1.amzn2023  |
|  kmod-nvidia-latest-dkms-570.133.20-1.amzn2023  |
|  kmod-nvidia-open-dkms-570.133.20-1.amzn2023  |
|  libnvidia-cfg-570.133.20-1.amzn2023  |
|  libnvidia-ml-570.133.20-1.amzn2023  |
|  libnvidia-nscq-570-570.133.20-1  |
|  libnvsdm-570-570.133.20-1  |
|  nvidia-driver-assistant-0.20.133.20-1  |
|  nvidia-driver-cuda-570.133.20-1.amzn2023  |
|  nvidia-driver-cuda-libs-570.133.20-1.amzn2023  |
|  nvidia-fabric-manager-570.133.20-1  |
|  nvidia-fabric-manager-devel-570.133.20-1  |
|  nvidia-imex-570-570.133.20-1  |
|  nvidia-kmod-common-570.133.20-1.amzn2023  |
|  nvidia-modprobe-570.133.20-1.amzn2023  |
|  nvidia-open-570.133.20-1.amzn2023  |
|  nvidia-persistenced-570.133.20-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.7.20250428"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250428.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250428-0.amzn2023  |
|  amazon-rpm-config-228-9.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.1957.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-34.amzn2023  |
|  binutils-2.41-50.amzn2023.0.3  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  kernel-libbpf-6.12.23-29.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250428-0.amzn2023  |
|  kernel-tools-6.12.23-29.97.amzn2023  |
|  kernel-6.1.134-150.224.amzn2023  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250428.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250428-0.amzn2023  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  kernel-libbpf-6.12.23-29.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250428-0.amzn2023  |
|  kernel-6.1.134-150.224.amzn2023  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250428.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250428-0.amzn2023  |
|  amazon-rpm-config-228-9.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.1957.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-34.amzn2023  |
|  binutils-2.41-50.amzn2023.0.3  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  kernel-libbpf-6.12.23-29.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250428-0.amzn2023  |
|  kernel-tools-6.12.23-29.97.amzn2023  |
|  kernel6.12-6.12.23-29.97.amzn2023  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250428.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250428-0.amzn2023  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  kernel-libbpf-6.12.23-29.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250428-0.amzn2023  |
|  kernel6.12-6.12.23-29.97.amzn2023  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

### Default Container
<a name="amis-2023.7.20250428.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250428-0.amzn2023  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250428.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250428-0.amzn2023  |
|  curl-minimal-8.5.0-1.amzn2023.0.5  |
|  libcap-2.73-1.amzn2023.0.2  |
|  libcurl-minimal-8.5.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250428-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250428.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
