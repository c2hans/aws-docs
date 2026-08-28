---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.11.20260427.html
---

# Amazon Linux 2023 version 2023.11.20260427 release notes
<a name="relnotes-2023.11.20260427"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.11.20260427.

**Contents**
+ [Release Summary](#release-summary-2023.11.20260427)
+ [Repository Updates](#repository-updates-2023.11.20260427)
  + [Core New Packages](#amis-2023.11.20260427.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.11.20260427.Core-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.11.20260427.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.11.20260427)
  + [Default Kernel 6.18 AMI](#amis-2023.11.20260427.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.11.20260427.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.11.20260427.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.11.20260427.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.11.20260427.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.11.20260427.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.11.20260427.Default-Container)
  + [Minimal Container](#amis-2023.11.20260427.Minimal-Container)
+ [Contact us](#amis-2023.11.20260427.contact-us)

## Release Summary
<a name="release-summary-2023.11.20260427"></a>

This release represents an update to the 11th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ SPAL now ships a debuginfo repository that contains both `debuginfo` and `debugsource` packages. These packages provide debug symbols and source files useful for debugging and profiling. For details, see [Installing SPAL debuginfo packages](https://docs.aws.amazon.com/linux/al2023/ug/configure-spal-repository.html#configure-spal-debuginfo-pkgs).
+ The `valkey` package has been updated to version `9.0.3` for AL2023. This is a major version upgrade from version `8.0.6` No known incompatibilities have been identified, but as with any major version upgrade, we recommend reviewing the official `Valkey release notes` before performing the upgrade.
  + [Release Blog](https://valkey.io/blog/introducing-valkey-9/)
  + [Release Notes](https://github.com/valkey-io/valkey/blob/9.0/00-RELEASENOTES)

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.11.20260427"></a>

### Core New Packages
<a name="amis-2023.11.20260427.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  libsrtp-2.6.0-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.11.20260427.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.44-1.amzn2023.0.2  |
|  amazon-efs-utils-3.1.0-1.amzn2023  |
|  aws-nitro-tpm-tools-1.1.1-1.amzn2023  |
|  cifs-utils-7.5-1.amzn2023.0.3  |
|  clamav1.4-1.4.4-1.amzn2023.0.1  |
|  clamav1.5-1.5.2-1.amzn2023.0.1  |
|  composer-2.9.7-1.amzn2023.0.1  |
|  containerd-2.2.3-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.1-1.amzn2023.0.3  |
|  cups-2.4.16-1.amzn2023.0.3  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  docker-25.0.14-1.amzn2023.0.4  |
|  dotnet10.0-10.0.107-1.amzn2023.0.1  |
|  dotnet8.0-8.0.126-1.amzn2023.0.1  |
|  dotnet9.0-9.0.116-1.amzn2023.0.1  |
|  ecs-service-connect-agent-v1.34.13.1-1.amzn2023  |
|  firefox-140.9.1-1.amzn2023.0.1  |
|  flatpak-1.16.6-1.amzn2023  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-2.3.7-1.amzn2023.0.8  |
|  golang-1.25.9-1.amzn2023.0.1  |
|  golist-0.10.4-12.amzn2023.0.8  |
|  java-1.8.0-amazon-corretto-1.8.0\_492.b09-1.amzn2023  |
|  java-11-amazon-corretto-11.0.31\+11-1.amzn2023  |
|  java-17-amazon-corretto-17.0.19\+10-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.11\+10-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.3\+9-1.amzn2023.1  |
|  java-26-amazon-corretto-26.0.1\+8-1.amzn2023.1  |
|  kernel-6.1.168-202.320.amzn2023  |
|  kernel6.12-6.12.80-105.147.amzn2023  |
|  librsvg2-2.59.2-318.amzn2023  |
|  libssh-0.10.6-1.amzn2023.0.6  |
|  maven3.9-3.9.14-3.amzn2023.0.1  |
|  mesa-24.2.6-1268.amzn2023.0.1  |
|  nerdctl-2.2.2-1.amzn2023.0.1  |
|  ngtcp2-1.21.0-1.amzn2023.0.2  |
|  nodejs20-20.20.2-1.amzn2023.0.2  |
|  nodejs22-22.22.2-1.amzn2023.0.2  |
|  nodejs24-24.15.0-1.amzn2023.0.1  |
|  openexr-3.1.5-1.amzn2023.0.9  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  perl-CPAN-2.38-521.amzn2023.0.1  |
|  perl-DBI-1.647-1.amzn2023.0.1  |
|  perl-DB\_File-1.860-1.amzn2023.0.1  |
|  perl-ExtUtils-InstallPaths-0.015-2.amzn2023.0.1  |
|  perl-Getopt-Long-Descriptive-0.117-1.amzn2023.0.1  |
|  perl-IO-Compress-2.217-1.amzn2023.0.1  |
|  perl-IO-Socket-IP-0.43-522.amzn2023.0.1  |
|  perl-JSON-Any-1.40-7.amzn2023.0.1  |
|  perl-Net-CIDR-Lite-0.22-8.amzn2023.0.1  |
|  perl-Specio-0.50-1.amzn2023.0.1  |
|  perl-Storable-3.37-522.amzn2023.0.1  |
|  perl-URI-5.18-1.amzn2023.0.1  |
|  python-jwcrypto-1.4.2-46.amzn2023.0.1  |
|  python-pip-21.3.1-2.amzn2023.0.17  |
|  python-tornado-6.1.0-2.amzn2023.0.8  |
|  python3.11-3.11.15-1.amzn2023.0.1  |
|  python3.12-3.12.13-2.amzn2023.0.1  |
|  python3.13-3.13.13-1.amzn2023.0.1  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.3  |
|  python3.14-3.14.3-2.amzn2023.0.1  |
|  python3.9-3.9.25-1.amzn2023.0.5  |
|  rclone-1.73.4-74.amzn2023  |
|  ruby3.4-3.4.8-27.amzn2023.0.4  |
|  rust-1.95.0-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.5  |
|  tomcat-native-2.0.14-4.amzn2023.0.1  |
|  valkey-9.0.3-1.amzn2023.0.1  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.9  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.4  |

### Nvidia Updated Packages
<a name="amis-2023.11.20260427.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-13-0-13.0.2-1  |
|  cuda-command-line-tools-13-0-13.0.2-1  |
|  cuda-compiler-13-0-13.0.2-1  |
|  cuda-cudart-13-0-13.0.96-1  |
|  cuda-cudart-devel-13-0-13.0.96-1  |
|  cuda-driver-devel-13-0-13.0.96-1  |
|  cuda-libraries-13-0-13.0.2-1  |
|  cuda-libraries-devel-13-0-13.0.2-1  |
|  cuda-minimal-build-13-0-13.0.2-1  |
|  cuda-nsight-compute-13-0-13.0.2-1  |
|  cuda-nsight-systems-13-0-13.0.2-1  |
|  cuda-runtime-13-0-13.0.2-1  |
|  cuda-toolkit-13-0-13.0.2-1  |
|  cuda-toolkit-13-0-config-common-13.0.96-1  |
|  cuda-tools-13-0-13.0.2-1  |
|  cuda-visual-tools-13-0-13.0.2-1  |
|  libcublas-13-0-13.1.0.3-1  |
|  libcublas-devel-13-0-13.1.0.3-1  |
|  nvidia-gds-13-0-13.0.2-1  |

## Image Updates
<a name="ami-updates-2023.11.20260427"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.11.20260427.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  perl-IO-Socket-IP-0.43-522.amzn2023.0.1  |
|  perl-Storable-1:3.37-522.amzn2023.0.1  |
|  perl-URI-5.18-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.11.20260427.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.11.20260427.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  kernel6.12-tools-1:6.12.80-105.147.amzn2023  |
|  kernel6.12-1:6.12.80-105.147.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  perl-IO-Socket-IP-0.43-522.amzn2023.0.1  |
|  perl-Storable-1:3.37-522.amzn2023.0.1  |
|  perl-URI-5.18-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.11.20260427.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  kernel6.12-1:6.12.80-105.147.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.11.20260427.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  kernel-tools-1:6.1.168-202.320.amzn2023  |
|  kernel-1:6.1.168-202.320.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  perl-IO-Socket-IP-0.43-522.amzn2023.0.1  |
|  perl-Storable-1:3.37-522.amzn2023.0.1  |
|  perl-URI-5.18-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.11.20260427.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260427-1.amzn2023  |
|  dnf-plugin-release-notification-1.4-1.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-locale-source-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.11.20260427-1.amzn2023  |
|  kernel-1:6.1.168-202.320.amzn2023  |
|  openssh-clients-8.7p1-8.amzn2023.0.17  |
|  openssh-server-8.7p1-8.amzn2023.0.17  |
|  openssh-8.7p1-8.amzn2023.0.17  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.1  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Default Container
<a name="amis-2023.11.20260427.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260427-1.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  python3-libs-3.9.25-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.17  |
|  python3-3.9.25-1.amzn2023.0.5  |
|  system-release-2023.11.20260427-1.amzn2023  |

### Minimal Container
<a name="amis-2023.11.20260427.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260427-1.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.4  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.4  |
|  glibc-2.34-231.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.8  |
|  system-release-2023.11.20260427-1.amzn2023  |

## Contact us
<a name="amis-2023.11.20260427.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
