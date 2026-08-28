---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260316.html
---

# Amazon Linux 2023 version 2023.10.20260316 release notes
<a name="relnotes-2023.10.20260316"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260316.

**Contents**
+ [Important: This release was recalled](#cdn-availability-issues-2023.10.20260316)
+ [Release Summary](#release-summary-2023.10.20260316)
+ [Repository Updates](#repository-updates-2023.10.20260316)
  + [Core New Packages](#amis-2023.10.20260316.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260316.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.10.20260316.Kernel-livepatch-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.10.20260316.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.10.20260316)
  + [Default Kernel 6.18 AMI](#amis-2023.10.20260316.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.10.20260316.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260316.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260316.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260316.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260316.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.10.20260316.Default-Container)
  + [Minimal Container](#amis-2023.10.20260316.Minimal-Container)
+ [Contact us](#amis-2023.10.20260316.contact-us)

## Important: This release was recalled
<a name="cdn-availability-issues-2023.10.20260316"></a>

**Warning**
Due to reported availability issues, this release is being recalled. The root cause has been identified and addressed.

## Release Summary
<a name="release-summary-2023.10.20260316"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ **AL2023 kernel-headers \| kernel6.12-headers \| kernel6.18-headers: **A bug in the kernel-headers package was fixed where it included extra files `(/usr/include/bpf/*` and `/usr/include/cpufreq.h)` that already existed in kernel-libbpf-devel and kernel-tools-devel. This overlap caused kernel namespace upgrades to fail. The conflicting files have been removed from kernel-headers to resolve the issue.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260316"></a>

### Core New Packages
<a name="amis-2023.10.20260316.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  gnome-app-list-3.0-1.amzn2023  |
|  gnome-software-47.5-1.amzn2023  |
|  rclone-1.73.0-73.amzn2023  |

### Core Updated Packages
<a name="amis-2023.10.20260316.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.40-1.amzn2023.0.1  |
|  amazon-efs-utils-2.4.2-1.amzn2023  |
|  amazon-ssm-agent-3.3.3883.0-1.amzn2023  |
|  appstream-data-2023-103.amzn2023  |
|  exiv2-0.28.5-132.amzn2023  |
|  firefox-140.8.0-1.amzn2023.0.1  |
|  freerdp-3.6.3-1.amzn2023.0.5  |
|  freetype-2.13.2-5.amzn2023.0.2  |
|  golang-1.25.8-1.amzn2023.0.1  |
|  gvfs-1.56.1-1.amzn2023.0.2  |
|  kernel-6.1.164-196.303.amzn2023  |
|  kernel6.12-6.12.74-98.124.amzn2023  |
|  kernel6.18-6.18.15-14.217.amzn2023  |
|  kiwi-10.2.38-1.amzn2023  |
|  lcms2-2.16-74.amzn2023  |
|  libde265-1.0.16-1.amzn2023.0.2  |
|  libsodium-1.0.19-5.amzn2023  |
|  libssh-0.10.6-1.amzn2023.0.5  |
|  libtiff-4.4.0-4.amzn2023.0.25  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  nodejs20-20.20.1-1.amzn2023.0.2  |
|  nodejs22-22.22.1-1.amzn2023.0.1  |
|  nvidia-release-2023-5.amzn2023  |
|  ocaml-4.13.1-4.amzn2023.0.3  |
|  openexr-3.1.5-1.amzn2023.0.7  |
|  perl-B-COW-0.007-12.amzn2023.0.1  |
|  perl-CGI-4.71-1.amzn2023.0.1  |
|  perl-Capture-Tiny-0.50-4.amzn2023.0.1  |
|  perl-Class-Data-Inheritable-0.10-4.amzn2023.0.1  |
|  perl-Config-General-2.64-1.amzn2023.0.1  |
|  perl-Convert-ASN1-0.34-7.amzn2023.0.1  |
|  perl-Encode-3.21-520.amzn2023.0.1  |
|  perl-Error-0.17030-2.amzn2023.0.1  |
|  perl-JSON-4.10-9.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.1  |
|  python-flask-1.1.4-5.amzn2023.0.1  |
|  python3.11-3.11.14-1.amzn2023.0.5  |
|  python3.13-pip-24.2-259.amzn2023.0.4  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  sscg-3.0.3-77.amzn2023  |
|  swig-4.1.1-4.amzn2023.0.5  |
|  system-release-2023.10.20260316-0.amzn2023  |
|  systemtap-5.4-1.amzn2023.0.2  |
|  tomcat10-10.1.52-1.amzn2023.0.1  |
|  tomcat9-9.0.115-1.amzn2023.0.1  |

### Kernel-livepatch New Packages
<a name="amis-2023.10.20260316.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.12.58-82.121-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.63-84.121-1.0-3.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.10.20260316.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  corelib-1.0.0.1772474517-1  |
|  cuda-compat-13-0-580.126.20-1.amzn2023  |
|  cuda-drivers-580.126.20-1.amzn2023  |
|  kmod-nvidia-latest-dkms-580.126.20-1.amzn2023  |
|  kmod-nvidia-open-dkms-580.126.20-1.amzn2023  |
|  libcorelib1-1.0.0.1772474517-1  |
|  libcorelib1-devel-1.0.0.1772474517-1  |
|  libnvat-1.2.0.1772475102-1  |
|  libnvat-devel-1.2.0.1772475102-1  |
|  libnvidia-cfg-580.126.20-1.amzn2023  |
|  libnvidia-fbc-580.126.20-1.amzn2023  |
|  libnvidia-gpucomp-580.126.20-1.amzn2023  |
|  libnvidia-ml-580.126.20-1.amzn2023  |
|  libnvidia-nscq-580.126.20-1  |
|  libnvsdm-580.126.20-1  |
|  libnvsdm-devel-580.126.20-1  |
|  nvattest-1.2.0.1772475102-1  |
|  nvidia-driver-580.126.20-1.amzn2023  |
|  nvidia-driver-assistant-0.46.126.20-1  |
|  nvidia-driver-cuda-580.126.20-1.amzn2023  |
|  nvidia-driver-cuda-libs-580.126.20-1.amzn2023  |
|  nvidia-driver-libs-580.126.20-1.amzn2023  |
|  nvidia-fabric-manager-devel-580.126.20-1  |
|  nvidia-fabricmanager-580.126.20-1  |
|  nvidia-imex-580.126.20-1  |
|  nvidia-kmod-common-580.126.20-1.amzn2023  |
|  nvidia-libXNVCtrl-580.126.20-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-580.126.20-1.amzn2023  |
|  nvidia-modprobe-580.126.20-1.amzn2023  |
|  nvidia-open-580.126.20-1.amzn2023  |
|  nvidia-persistenced-580.126.20-1.amzn2023  |
|  nvidia-settings-580.126.20-1.amzn2023  |
|  nvidia-xconfig-580.126.20-1.amzn2023  |
|  nvlink5-580.126.20-1  |
|  nvlink5-580-580.126.20-1  |
|  xorg-x11-nvidia-580.126.20-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.10.20260316"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.10.20260316.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  amazon-ssm-agent-3.3.3883.0-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel6.18-libbpf-1:6.18.15-14.217.amzn2023  |
|  kernel6.18-tools-1:6.18.15-14.217.amzn2023  |
|  kernel6.18-1:6.18.15-14.217.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  perl-Encode-4:3.21-520.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |
|  systemtap-runtime-5.4-1.amzn2023.0.2  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.10.20260316.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel6.18-libbpf-1:6.18.15-14.217.amzn2023  |
|  kernel6.18-1:6.18.15-14.217.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260316.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  amazon-ssm-agent-3.3.3883.0-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.74-98.124.amzn2023  |
|  kernel6.12-tools-1:6.12.74-98.124.amzn2023  |
|  kernel6.12-1:6.12.74-98.124.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  perl-Encode-4:3.21-520.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |
|  systemtap-runtime-5.4-1.amzn2023.0.2  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260316.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.74-98.124.amzn2023  |
|  kernel6.12-1:6.12.74-98.124.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260316.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  amazon-ssm-agent-3.3.3883.0-1.amzn2023  |
|  kernel-libbpf-1:6.1.164-196.303.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel-tools-1:6.1.164-196.303.amzn2023  |
|  kernel-1:6.1.164-196.303.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  perl-Encode-4:3.21-520.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |
|  systemtap-runtime-5.4-1.amzn2023.0.2  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260316.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel-libbpf-1:6.1.164-196.303.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260316-0.amzn2023  |
|  kernel-1:6.1.164-196.303.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  ncurses-6.6-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.73-1.amzn2023.0.2  |
|  selinux-policy-38.1.73-1.amzn2023.0.2  |
|  system-release-2023.10.20260316-0.amzn2023  |

### Default Container
<a name="amis-2023.10.20260316.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260316-0.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  system-release-2023.10.20260316-0.amzn2023  |

### Minimal Container
<a name="amis-2023.10.20260316.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260316-0.amzn2023  |
|  ncurses-base-6.6-1.amzn2023.0.1  |
|  ncurses-libs-6.6-1.amzn2023.0.1  |
|  system-release-2023.10.20260316-0.amzn2023  |

## Contact us
<a name="amis-2023.10.20260316.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
