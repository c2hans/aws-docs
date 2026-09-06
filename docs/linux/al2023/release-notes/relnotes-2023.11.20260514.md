---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.11.20260514.html
---

# Amazon Linux 2023 version 2023.11.20260514 release notes
<a name="relnotes-2023.11.20260514"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.11.20260514.

**Contents**
+ [Release Summary](#release-summary-2023.11.20260514)
+ [Repository Updates](#repository-updates-2023.11.20260514)
  + [Core New Packages](#amis-2023.11.20260514.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.11.20260514.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.11.20260514)
  + [Default Kernel 6.18 AMI](#amis-2023.11.20260514.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.11.20260514.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.11.20260514.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.11.20260514.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.11.20260514.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.11.20260514.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.11.20260514.Default-Container)
  + [Minimal Container](#amis-2023.11.20260514.Minimal-Container)
+ [Contact us](#amis-2023.11.20260514.contact-us)

## Release Summary
<a name="release-summary-2023.11.20260514"></a>

This release represents an update to the 11th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.11.20260514"></a>

### Core New Packages
<a name="amis-2023.11.20260514.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  ruby4.0-4.0.1-32.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.11.20260514.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.44-1.amzn2023.0.3  |
|  aws-cfn-bootstrap-2.0-39.amzn2023  |
|  curl-8.17.0-1.amzn2023.0.3  |
|  ecs-init-1.103.1-1.amzn2023  |
|  firefox-140.10.1-1.amzn2023.0.2  |
|  glslang-15.0.0-88.amzn2023  |
|  kernel-6.1.170-213.321.amzn2023  |
|  kernel6.12-6.12.83-115.161.amzn2023  |
|  kernel6.18-6.18.25-57.109.amzn2023  |
|  kpatch-0.9.10-1.amzn2023.0.5  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  lustre-client-2.15.6-30.amzn2023  |
|  nss-3.90.0-7.amzn2023.0.1  |
|  perl-5.32.1-477.amzn2023.0.8  |
|  perl-Crypt-DES-2.07-30.amzn2023.0.3  |
|  perl-Text-CSV\_XS-1.62-1.amzn2023.0.1  |
|  python-pip-21.3.1-2.amzn2023.0.19  |
|  ruby3.4-3.4.8-27.amzn2023.0.5  |
|  socat-1.7.4.2-1.amzn2023.0.3  |
|  soci-snapshotter-0.13.0-1.amzn2023.0.2  |
|  system-release-2023.11.20260514-0.amzn2023  |
|  tmux-3.6a-1.amzn2023.0.1  |

## Image Updates
<a name="ami-updates-2023.11.20260514"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.11.20260514.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-39.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel6.18-tools-1:6.18.25-57.109.amzn2023  |
|  kernel6.18-1:6.18.25-57.109.amzn2023  |
|  kpatch-runtime-0.9.10-1.amzn2023.0.5  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  nspr-4.35.0-7.amzn2023.0.1  |
|  nss-softokn-freebl-3.90.0-7.amzn2023.0.1  |
|  nss-softokn-3.90.0-7.amzn2023.0.1  |
|  nss-sysinit-3.90.0-7.amzn2023.0.1  |
|  nss-util-3.90.0-7.amzn2023.0.1  |
|  nss-3.90.0-7.amzn2023.0.1  |
|  perl-AutoLoader-5.74-477.amzn2023.0.8  |
|  perl-B-1.80-477.amzn2023.0.8  |
|  perl-Class-Struct-0.66-477.amzn2023.0.8  |
|  perl-DynaLoader-1.47-477.amzn2023.0.8  |
|  perl-Errno-1.30-477.amzn2023.0.8  |
|  perl-Fcntl-1.13-477.amzn2023.0.8  |
|  perl-File-Basename-2.85-477.amzn2023.0.8  |
|  perl-File-stat-1.09-477.amzn2023.0.8  |
|  perl-FileHandle-2.03-477.amzn2023.0.8  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.8  |
|  perl-IO-1.43-477.amzn2023.0.8  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.8  |
|  perl-POSIX-1.94-477.amzn2023.0.8  |
|  perl-SelectSaver-1.02-477.amzn2023.0.8  |
|  perl-Symbol-1.08-477.amzn2023.0.8  |
|  perl-base-2.27-477.amzn2023.0.8  |
|  perl-if-0.60.800-477.amzn2023.0.8  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.8  |
|  perl-libs-4:5.32.1-477.amzn2023.0.8  |
|  perl-mro-1.23-477.amzn2023.0.8  |
|  perl-overload-1.31-477.amzn2023.0.8  |
|  perl-overloading-0.02-477.amzn2023.0.8  |
|  perl-subs-1.03-477.amzn2023.0.8  |
|  perl-vars-1.05-477.amzn2023.0.8  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.11.20260514.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel6.18-1:6.18.25-57.109.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.11.20260514.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-39.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel6.12-tools-1:6.12.83-115.161.amzn2023  |
|  kernel6.12-1:6.12.83-115.161.amzn2023  |
|  kpatch-runtime-0.9.10-1.amzn2023.0.5  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  nspr-4.35.0-7.amzn2023.0.1  |
|  nss-softokn-freebl-3.90.0-7.amzn2023.0.1  |
|  nss-softokn-3.90.0-7.amzn2023.0.1  |
|  nss-sysinit-3.90.0-7.amzn2023.0.1  |
|  nss-util-3.90.0-7.amzn2023.0.1  |
|  nss-3.90.0-7.amzn2023.0.1  |
|  perl-AutoLoader-5.74-477.amzn2023.0.8  |
|  perl-B-1.80-477.amzn2023.0.8  |
|  perl-Class-Struct-0.66-477.amzn2023.0.8  |
|  perl-DynaLoader-1.47-477.amzn2023.0.8  |
|  perl-Errno-1.30-477.amzn2023.0.8  |
|  perl-Fcntl-1.13-477.amzn2023.0.8  |
|  perl-File-Basename-2.85-477.amzn2023.0.8  |
|  perl-File-stat-1.09-477.amzn2023.0.8  |
|  perl-FileHandle-2.03-477.amzn2023.0.8  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.8  |
|  perl-IO-1.43-477.amzn2023.0.8  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.8  |
|  perl-POSIX-1.94-477.amzn2023.0.8  |
|  perl-SelectSaver-1.02-477.amzn2023.0.8  |
|  perl-Symbol-1.08-477.amzn2023.0.8  |
|  perl-base-2.27-477.amzn2023.0.8  |
|  perl-if-0.60.800-477.amzn2023.0.8  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.8  |
|  perl-libs-4:5.32.1-477.amzn2023.0.8  |
|  perl-mro-1.23-477.amzn2023.0.8  |
|  perl-overload-1.31-477.amzn2023.0.8  |
|  perl-overloading-0.02-477.amzn2023.0.8  |
|  perl-subs-1.03-477.amzn2023.0.8  |
|  perl-vars-1.05-477.amzn2023.0.8  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.11.20260514.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel6.12-1:6.12.83-115.161.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.11.20260514.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-39.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel-tools-1:6.1.170-213.321.amzn2023  |
|  kernel-1:6.1.170-213.321.amzn2023  |
|  kpatch-runtime-0.9.10-1.amzn2023.0.5  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  nspr-4.35.0-7.amzn2023.0.1  |
|  nss-softokn-freebl-3.90.0-7.amzn2023.0.1  |
|  nss-softokn-3.90.0-7.amzn2023.0.1  |
|  nss-sysinit-3.90.0-7.amzn2023.0.1  |
|  nss-util-3.90.0-7.amzn2023.0.1  |
|  nss-3.90.0-7.amzn2023.0.1  |
|  perl-AutoLoader-5.74-477.amzn2023.0.8  |
|  perl-B-1.80-477.amzn2023.0.8  |
|  perl-Class-Struct-0.66-477.amzn2023.0.8  |
|  perl-DynaLoader-1.47-477.amzn2023.0.8  |
|  perl-Errno-1.30-477.amzn2023.0.8  |
|  perl-Fcntl-1.13-477.amzn2023.0.8  |
|  perl-File-Basename-2.85-477.amzn2023.0.8  |
|  perl-File-stat-1.09-477.amzn2023.0.8  |
|  perl-FileHandle-2.03-477.amzn2023.0.8  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.8  |
|  perl-IO-1.43-477.amzn2023.0.8  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.8  |
|  perl-POSIX-1.94-477.amzn2023.0.8  |
|  perl-SelectSaver-1.02-477.amzn2023.0.8  |
|  perl-Symbol-1.08-477.amzn2023.0.8  |
|  perl-base-2.27-477.amzn2023.0.8  |
|  perl-if-0.60.800-477.amzn2023.0.8  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.8  |
|  perl-libs-4:5.32.1-477.amzn2023.0.8  |
|  perl-mro-1.23-477.amzn2023.0.8  |
|  perl-overload-1.31-477.amzn2023.0.8  |
|  perl-overloading-0.02-477.amzn2023.0.8  |
|  perl-subs-1.03-477.amzn2023.0.8  |
|  perl-vars-1.05-477.amzn2023.0.8  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.11.20260514.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260514-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.11.20260514-0.amzn2023  |
|  kernel-1:6.1.170-213.321.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Default Container
<a name="amis-2023.11.20260514.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260514-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.19  |
|  system-release-2023.11.20260514-0.amzn2023  |

### Minimal Container
<a name="amis-2023.11.20260514.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260514-0.amzn2023  |
|  curl-minimal-8.17.0-1.amzn2023.0.3  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.3  |
|  libgcrypt-1.10.2-1.amzn2023.0.3  |
|  system-release-2023.11.20260514-0.amzn2023  |

## Contact us
<a name="amis-2023.11.20260514.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
