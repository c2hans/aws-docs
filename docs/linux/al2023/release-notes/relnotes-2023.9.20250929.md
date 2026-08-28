---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20250929.html
---

# Amazon Linux 2023 version 2023.9.20250929 release notes
<a name="relnotes-2023.9.20250929"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.9.20250929.

**Contents**
+ [Release Summary](#release-summary-2023.9.20250929)
+ [Repository Updates](#repository-updates-2023.9.20250929)
  + [Core New Packages](#amis-2023.9.20250929.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.9.20250929.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.9.20250929.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.9.20250929.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.9.20250929)
  + [Default Kernel 6.1 AMI](#amis-2023.9.20250929.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.9.20250929.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.9.20250929.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.9.20250929.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.9.20250929.Default-Container)
  + [Minimal Container](#amis-2023.9.20250929.Minimal-Container)
+ [Contact us](#amis-2023.9.20250929.contact-us)

## Release Summary
<a name="release-summary-2023.9.20250929"></a>

This release represents an update to the 9th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  The Desktop now officially supports `Touchpads/Touchscreens and Magnification.` Furthermore, remote access is now also possible via `RDP` in addition to the previously supported VNC and Amazon DCV. Decibels, the Gnome audio player was added to AL2023 desktop along with support for decoding mp3 files.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.9.20250929"></a>

### Core New Packages
<a name="amis-2023.9.20250929.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  java-25-amazon-corretto-25.0.0\+36-2.amzn2023.1  |
|  libomp18-18.1.8-4.amzn2023.0.1  |
|  lldb18-18.1.8-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.9.20250929.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  GraphicsMagick-1.3.45-1.amzn2023.0.1  |
|  ImageMagick-6.9.13.29-1.amzn2023.0.1  |
|  amazon-rpm-config-228-10.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.3050.0-1.amzn2023  |
|  awscli-2-2.30.4-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.4  |
|  container-selinux-2.242.0-1.amzn2023  |
|  coreutils-8.32-30.amzn2023.0.4  |
|  cups-2.4.14-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.8-1.amzn2023  |
|  ecs-init-1.99.1-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  firefox-140.3.0-1.amzn2023.0.1  |
|  gcc14-14.2.1-7.amzn2023.0.2  |
|  glycin-1.1.2-9.amzn2023  |
|  iperf3-3.19.1-1.amzn2023  |
|  kernel-6.1.153-175.280.amzn2023  |
|  kernel6.12-6.12.46-66.121.amzn2023  |
|  kiwi-image-descriptions-examples-1.0.2-1.amzn2023  |
|  libclc-18.1.8-1.amzn2023.0.1  |
|  libvpx-1.11.0-1.amzn2023.0.5  |
|  loupe-47.4-33.amzn2023  |
|  microcode\_ctl-2.1-53.amzn2023.0.14  |
|  network-flow-monitor-agent-0.2.1-1.amzn2023.0.1  |
|  nodejs20-typescript-5.9.2-1.amzn2023.0.1  |
|  nodejs22-typescript-5.9.2-1.amzn2023.0.1  |
|  openjpeg2-2.5.2-5.amzn2023.0.1  |
|  perl-Cpanel-JSON-XS-4.25-2.amzn2023.0.7  |
|  perl-JSON-XS-4.03-3.amzn2023.0.3  |
|  php8.3-8.3.25-1.amzn2023.0.1  |
|  python-awscrt-0.27.6-1.amzn2023.0.1  |
|  redis6-6.2.14-2.amzn2023.0.7  |
|  ruby3.2-3.2.8-184.amzn2023.0.6  |
|  rust-1.90.0-1.amzn2023.0.1  |
|  selinux-policy-38.1.65-1.amzn2023.0.1  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.9.20250929.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.147-172.266-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.148-173.267-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.150-174.273-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.40-63.114-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.40-64.114-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.9.20250929.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.141-165.249-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.141-167.250-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.144-170.251-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.147-172.259-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.31-35.92-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.35-55.103-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.37-61.105-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.40-63.107-1.0-2.amzn2023  |

## Image Updates
<a name="ami-updates-2023.9.20250929"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.9.20250929.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20250929-0.amzn2023  |
|  amazon-rpm-config-228-10.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.3050.0-1.amzn2023  |
|  awscli-2-2.30.4-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.4  |
|  coreutils-common-8.32-30.amzn2023.0.4  |
|  coreutils-8.32-30.amzn2023.0.4  |
|  dnf-plugin-support-info-1.8-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  kernel-libbpf-1:6.1.153-175.280.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20250929-0.amzn2023  |
|  kernel-tools-1:6.1.153-175.280.amzn2023  |
|  kernel-1:6.1.153-175.280.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libgomp-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.14  |
|  python3-awscrt-0.27.6-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.90.0-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.65-1.amzn2023.0.1  |
|  selinux-policy-38.1.65-1.amzn2023.0.1  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.9.20250929.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20250929-0.amzn2023  |
|  awscli-2-2.30.4-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.4  |
|  coreutils-8.32-30.amzn2023.0.4  |
|  dnf-plugin-support-info-1.8-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  kernel-libbpf-1:6.1.153-175.280.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20250929-0.amzn2023  |
|  kernel-1:6.1.153-175.280.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libgomp-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.14  |
|  python3-awscrt-0.27.6-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.65-1.amzn2023.0.1  |
|  selinux-policy-38.1.65-1.amzn2023.0.1  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.9.20250929.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20250929-0.amzn2023  |
|  amazon-rpm-config-228-10.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.3050.0-1.amzn2023  |
|  awscli-2-2.30.4-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.4  |
|  coreutils-common-8.32-30.amzn2023.0.4  |
|  coreutils-8.32-30.amzn2023.0.4  |
|  dnf-plugin-support-info-1.8-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.9.20250929-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.46-66.121.amzn2023  |
|  kernel6.12-tools-1:6.12.46-66.121.amzn2023  |
|  kernel6.12-1:6.12.46-66.121.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libgomp-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.14  |
|  python3-awscrt-0.27.6-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.90.0-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.65-1.amzn2023.0.1  |
|  selinux-policy-38.1.65-1.amzn2023.0.1  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.9.20250929.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20250929-0.amzn2023  |
|  awscli-2-2.30.4-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.4  |
|  coreutils-8.32-30.amzn2023.0.4  |
|  dnf-plugin-support-info-1.8-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.9.20250929-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.46-66.121.amzn2023  |
|  kernel6.12-1:6.12.46-66.121.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libgomp-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.14  |
|  python3-awscrt-0.27.6-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.65-1.amzn2023.0.1  |
|  selinux-policy-38.1.65-1.amzn2023.0.1  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Default Container
<a name="amis-2023.9.20250929.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20250929-0.amzn2023  |
|  coreutils-single-8.32-30.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.3  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libgomp-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  system-release-2023.9.20250929-0.amzn2023  |

### Minimal Container
<a name="amis-2023.9.20250929.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20250929-0.amzn2023  |
|  coreutils-single-8.32-30.amzn2023.0.4  |
|  libgcc-14.2.1-7.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.2  |
|  system-release-2023.9.20250929-0.amzn2023  |

## Contact us
<a name="amis-2023.9.20250929.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
