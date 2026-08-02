---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250623.html
---

# Amazon Linux 2023 version 2023.7.20250623 release notes
<a name="relnotes-2023.7.20250623"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250623.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250623)
+ [Repository Updates](#repository-updates-2023.7.20250623)
  + [Core New Packages](#amis-2023.7.20250623.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.7.20250623.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.7.20250623)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250623.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250623.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250623.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250623.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.7.20250623.Default-Container)
  + [Minimal Container](#amis-2023.7.20250623.Minimal-Container)
+ [Contact us](#amis-2023.7.20250623.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250623"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  AL2023 is now FIPS certified. [Learn more](https://aws.amazon.com/blogs/compute/amazon-linux-2023-achieves-fips-140-3-validation/).
+  compat-poppler22-22.08.0-3.amzn2023.0.1 :The core Poppler library has been updated from version `22.08 to 24.08.` To ensure a smooth transition for packages from the old version of Poppler to the newer one, we have introduced compat-poppler22 for packages depending on the older library versions. This compatibility package provides only the necessary shared libraries from Poppler 22.08 to maintain functionality for packages that still require these older versions. This only serves as a transitional package to prevent disruption of PDF-related functionalities in existing applications, customers should focus on using the main poppler-24.08 package for any new installations or development. We strongly recommend customers to upgrade their existing application dependency to use the newer version of poppler as well.
**Note**
 Note: `compat-poppler22` will be maintained for 6 months, during this period, we will work on updating all dependent packages to use the newer Poppler 24.08 libraries. Once this transition is complete, the compatibility package will be deprecated.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250623"></a>

### Core New Packages
<a name="amis-2023.7.20250623.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  blueprint-compiler-0.16.0-15.amzn2023  |
|  clang18-18.1.8-6.amzn2023.0.3  |
|  compat-poppler22-22.08.0-3.amzn2023.0.1  |
|  compiler-rt18-18.1.8-4.amzn2023.0.1  |
|  dav1d-1.5.1-50.amzn2023  |
|  gnome-common-3.18.0-20.amzn2023  |
|  libXpresent-1.0.0-27.amzn2023  |
|  lld18-18.1.8-7.amzn2023.0.1  |
|  llvm18-18.1.8-6.amzn2023.0.1  |
|  metacity-3.54.0-334.amzn2023  |
|  openh264-2.6.0-2.amzn2023  |
|  papers-47.0-11.amzn2023  |
|  rust-gst-plugin-dav1d-0.13.6-8.amzn2023  |
|  rust-gst-plugin-gtk4-0.13.6-21.amzn2023  |
|  showtime-48.1-8.amzn2023  |
|  svt-av1-2.3.0-46.amzn2023  |
|  zenity-4.0.5-1.amzn2023  |

### Core Updated Packages
<a name="amis-2023.7.20250623.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  BabelfishDump-17.5-1.amzn2023.0.1  |
|  abseil-cpp-20220623.1-4.amzn2023.0.2  |
|  amazon-cloudwatch-agent-1.300055.3-1.amzn2023  |
|  amazon-ecr-credential-helper-0.10.0-1.amzn2023  |
|  aws-kinesis-agent-2.0.12-1.amzn2023  |
|  awscli-2-2.25.0-1.amzn2023.0.1  |
|  containerd-2.0.5-1.amzn2023.0.1  |
|  curl-8.11.1-4.amzn2023.0.1  |
|  debugedit-5.0-10.amzn2023.0.1  |
|  ecs-init-1.95.0-1.amzn2023  |
|  firefox-128.11.0-1.amzn2023.0.3  |
|  freerdp-3.6.3-1.amzn2023.0.1  |
|  gdb-16.3-1.amzn2023.0.1  |
|  gnu-efi-3.0.11-9.amzn2023.0.2  |
|  golang-1.24.4-1.amzn2023.0.1  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.4  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.6  |
|  kernel-6.1.141-155.222.amzn2023  |
|  kernel6.12-6.12.31-35.92.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libblockdev-3.2.1-1.amzn2023.0.3  |
|  libvpx-1.11.0-1.amzn2023.0.4  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  mod\_security-2.9.10-1.amzn2023.0.1  |
|  nginx-1.28.0-1.amzn2023.0.1  |
|  nvidia-release-2023-2.amzn2023  |
|  openssh-8.7p1-8.amzn2023.0.15  |
|  perl-CryptX-0.080-1.amzn2023.0.1  |
|  perl-File-Find-Rule-0.34-17.amzn2023.0.3  |
|  perl-File-Find-Rule-Perl-1.15-19.amzn2023.0.3  |
|  perl-YAML-LibYAML-0.82-4.amzn2023.0.3  |
|  php8.3-8.3.22-1.amzn2023.0.1  |
|  php8.4-8.4.8-1.amzn2023.0.1  |
|  poppler-24.08.0-1.amzn2023  |
|  python3.11-3.11.13-1.amzn2023.0.1  |
|  python3.12-3.12.10-2.amzn2023.0.2  |
|  python3.9-3.9.23-1.amzn2023.0.1  |
|  runc-1.2.4-2.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |
|  tomcat10-10.1.41-1.amzn2023.0.1  |
|  tomcat9-9.0.105-1.amzn2023.0.1  |
|  udisks2-2.10.1-6.amzn2023.0.2  |
|  valkey-8.0.3-3.amzn2023.0.2  |

## Image Updates
<a name="ami-updates-2023.7.20250623"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250623.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250623-0.amzn2023  |
|  awscli-2-2.25.0-1.amzn2023.0.1  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  kernel-libbpf-6.12.31-35.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250623-0.amzn2023  |
|  kernel-tools-6.12.31-35.92.amzn2023  |
|  kernel-6.1.141-155.222.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  openssh-clients-8.7p1-8.amzn2023.0.15  |
|  openssh-server-8.7p1-8.amzn2023.0.15  |
|  openssh-8.7p1-8.amzn2023.0.15  |
|  python3-libs-3.9.23-1.amzn2023.0.1  |
|  python3-3.9.23-1.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250623.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250623-0.amzn2023  |
|  awscli-2-2.25.0-1.amzn2023.0.1  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  kernel-libbpf-6.12.31-35.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250623-0.amzn2023  |
|  kernel-6.1.141-155.222.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  openssh-clients-8.7p1-8.amzn2023.0.15  |
|  openssh-server-8.7p1-8.amzn2023.0.15  |
|  openssh-8.7p1-8.amzn2023.0.15  |
|  python3-libs-3.9.23-1.amzn2023.0.1  |
|  python3-3.9.23-1.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250623.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250623-0.amzn2023  |
|  awscli-2-2.25.0-1.amzn2023.0.1  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  kernel-libbpf-6.12.31-35.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250623-0.amzn2023  |
|  kernel-tools-6.12.31-35.92.amzn2023  |
|  kernel6.12-6.12.31-35.92.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  openssh-clients-8.7p1-8.amzn2023.0.15  |
|  openssh-server-8.7p1-8.amzn2023.0.15  |
|  openssh-8.7p1-8.amzn2023.0.15  |
|  python3-libs-3.9.23-1.amzn2023.0.1  |
|  python3-3.9.23-1.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250623.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250623-0.amzn2023  |
|  awscli-2-2.25.0-1.amzn2023.0.1  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  kernel-libbpf-6.12.31-35.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250623-0.amzn2023  |
|  kernel6.12-6.12.31-35.92.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  openssh-clients-8.7p1-8.amzn2023.0.15  |
|  openssh-server-8.7p1-8.amzn2023.0.15  |
|  openssh-8.7p1-8.amzn2023.0.15  |
|  python3-libs-3.9.23-1.amzn2023.0.1  |
|  python3-3.9.23-1.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |

### Default Container
<a name="amis-2023.7.20250623.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250623-0.amzn2023  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  python3-libs-3.9.23-1.amzn2023.0.1  |
|  python3-3.9.23-1.amzn2023.0.1  |
|  system-release-2023.7.20250623-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250623.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250623-0.amzn2023  |
|  curl-minimal-8.11.1-4.amzn2023.0.1  |
|  libarchive-3.7.4-2.amzn2023.0.3  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.11  |
|  system-release-2023.7.20250623-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250623.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
