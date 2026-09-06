---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250804.html
---

# Amazon Linux 2023 version 2023.8.20250804 release notes
<a name="relnotes-2023.8.20250804"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250804.

**Contents**
+ [Important: This release was recalled](#kernel-soft-lockup-warning-2023.8.20250804)
  + [Solution and Mitigation](#kernel-soft-lockup-mitigation-2023.8.20250804)
+ [Release Summary](#release-summary-2023.8.20250804)
+ [Repository Updates](#repository-updates-2023.8.20250804)
  + [Core Updated Packages](#amis-2023.8.20250804.Core-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.8.20250804.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250804)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250804.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250804.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250804.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250804.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250804.Default-Container)
  + [Minimal Container](#amis-2023.8.20250804.Minimal-Container)
+ [Contact us](#amis-2023.8.20250804.contact-us)

## Important: This release was recalled
<a name="kernel-soft-lockup-warning-2023.8.20250804"></a>

**Warning**
Versions of Amazon Linux released on August 6, 2025 may experience soft lockup issues and instance launch failures when using `auditd`. Customers are recommended to avoid using the affected AMI versions or updating to the affected kernels while also running `auditd`. Amazon is working on providing an update that addresses this issue.
This issue affects AL2023 version 2023.8.20250804 with the following kernel versions:
`kernel-6.1.147-172.259.amzn2023`
`kernel6.12-6.12.40-63.107.amzn2023`
To check if your instance is running an affected kernel version, use the `uname -r` command.

### Solution and Mitigation
<a name="kernel-soft-lockup-mitigation-2023.8.20250804"></a>

To downgrade to the previous version you can run these commands:

If your system is running kernel version `kernel-6.1.147-172.259.amzn2023`:

1. Install the previous kernel:

   ```
   sudo dnf -y install kernel-6.1.144-170.251.amzn2023 --releasever=2023.8.20250721 && sudo dnf -y reinstall kernel-6.1.144-170.251.amzn2023
   ```

1. Reboot to the installed kernel:

   ```
   sudo reboot
   ```

If your system is running kernel version `kernel6.12-6.12.40-63.107.amzn2023`:

1. Install the previous stable kernel:

   ```
   sudo dnf -y install kernel6.12-6.12.37-61.105.amzn2023 --releasever=2023.8.20250721 && sudo dnf -y reinstall kernel6.12-6.12.37-61.105.amzn2023
   ```

1. Reboot to the installed kernel:

   ```
   sudo reboot
   ```

The Amazon Linux team is actively working on this kernel issue and customers can expect the updated kernel in the week of August 11, 2025.

## Release Summary
<a name="release-summary-2023.8.20250804"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  The Landlock feature `CONFIG_SECURITY_LANDLOCK` is now enabled for kernel 6.1 & 6.12

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250804"></a>

### Core Updated Packages
<a name="amis-2023.8.20250804.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.12.82-1.amzn2023.0.9  |
|  aws-kinesis-agent-2.0.13-1.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  cni-plugins-1.7.1-1.amzn2023.0.2  |
|  ecs-init-1.97.0-1.amzn2023  |
|  fasterxml-oss-parent-58-2.amzn2023.0.1  |
|  ghostscript-9.56.1-7.amzn2023.0.18  |
|  google-noto-fonts-20240401-1.amzn2023.0.2  |
|  httpd-2.4.64-1.amzn2023.0.1  |
|  jackson-annotations-2.16.1-3.amzn2023.0.1  |
|  jackson-bom-2.16.1-3.amzn2023.0.1  |
|  jackson-core-2.16.1-4.amzn2023.0.1  |
|  jackson-databind-2.16.1-4.amzn2023.0.1  |
|  jackson-parent-2.16-4.amzn2023.0.1  |
|  jakarta-mail-1.6.5-8.amzn2023.0.2  |
|  kernel-6.1.147-172.259.amzn2023  |
|  kernel6.12-6.12.40-63.107.amzn2023  |
|  libmicrohttpd-0.9.73-1.amzn2023.0.4  |
|  libsoup3-3.6.5-50.amzn2023  |
|  libxslt-1.1.43-1.amzn2023.0.2  |
|  memcached-1.6.38-2.amzn2023.0.1  |
|  microcode\_ctl-2.1-53.amzn2023.0.13  |
|  network-flow-monitor-agent-0.2.0-1.amzn2023.0.1  |
|  nodejs-18.20.8-1.amzn2023.0.2  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python-awscrt-0.26.1-1.amzn2023.0.1  |
|  ruby3.2-3.2.8-184.amzn2023.0.4  |
|  runfinch-finch-1.10.0-1.amzn2023.0.2  |
|  samba-4.17.12-1.amzn2023.0.2  |
|  seahorse-47.0.1-1.amzn2023.0.1  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250804-0.amzn2023  |
|  systemd-252.23-6.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.8  |

### Nvidia Updated Packages
<a name="amis-2023.8.20250804.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-compat-12-8-570.172.08-1.amzn2023  |
|  cuda-drivers-570.172.08-1.amzn2023  |
|  kmod-nvidia-latest-dkms-570.172.08-1.amzn2023  |
|  kmod-nvidia-open-dkms-570.172.08-1.amzn2023  |
|  libnvidia-cfg-570.172.08-1.amzn2023  |
|  libnvidia-ml-570.172.08-1.amzn2023  |
|  libnvidia-nscq-570-570.172.08-1  |
|  libnvsdm-570-570.172.08-1  |
|  nvidia-driver-cuda-570.172.08-1.amzn2023  |
|  nvidia-driver-cuda-libs-570.172.08-1.amzn2023  |
|  nvidia-fabric-manager-570.172.08-1  |
|  nvidia-fabric-manager-devel-570.172.08-1  |
|  nvidia-imex-570-570.172.08-1  |
|  nvidia-kmod-common-570.172.08-1.amzn2023  |
|  nvidia-modprobe-570.172.08-1.amzn2023  |
|  nvidia-open-570.172.08-1.amzn2023  |
|  nvidia-persistenced-570.172.08-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.8.20250804"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250804.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250804-0.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  kernel-libbpf-1:6.1.147-172.259.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250804-0.amzn2023  |
|  kernel-tools-1:6.1.147-172.259.amzn2023  |
|  kernel-1:6.1.147-172.259.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.13  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python3-awscrt-0.26.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.50-1.amzn2023.0.2  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250804-0.amzn2023  |
|  systemd-libs-252.23-6.amzn2023  |
|  systemd-networkd-252.23-6.amzn2023  |
|  systemd-pam-252.23-6.amzn2023  |
|  systemd-resolved-252.23-6.amzn2023  |
|  systemd-udev-252.23-6.amzn2023  |
|  systemd-252.23-6.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250804.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250804-0.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  kernel-libbpf-1:6.1.147-172.259.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250804-0.amzn2023  |
|  kernel-1:6.1.147-172.259.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.13  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python3-awscrt-0.26.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.50-1.amzn2023.0.2  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250804-0.amzn2023  |
|  systemd-libs-252.23-6.amzn2023  |
|  systemd-networkd-252.23-6.amzn2023  |
|  systemd-pam-252.23-6.amzn2023  |
|  systemd-resolved-252.23-6.amzn2023  |
|  systemd-udev-252.23-6.amzn2023  |
|  systemd-252.23-6.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250804.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250804-0.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250804-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-63.107.amzn2023  |
|  kernel6.12-tools-1:6.12.40-63.107.amzn2023  |
|  kernel6.12-1:6.12.40-63.107.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.13  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python3-awscrt-0.26.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.50-1.amzn2023.0.2  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250804-0.amzn2023  |
|  systemd-libs-252.23-6.amzn2023  |
|  systemd-networkd-252.23-6.amzn2023  |
|  systemd-pam-252.23-6.amzn2023  |
|  systemd-resolved-252.23-6.amzn2023  |
|  systemd-udev-252.23-6.amzn2023  |
|  systemd-252.23-6.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250804.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250804-0.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250804-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-63.107.amzn2023  |
|  kernel6.12-1:6.12.40-63.107.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.13  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python3-awscrt-0.26.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.50-1.amzn2023.0.2  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250804-0.amzn2023  |
|  systemd-libs-252.23-6.amzn2023  |
|  systemd-networkd-252.23-6.amzn2023  |
|  systemd-pam-252.23-6.amzn2023  |
|  systemd-resolved-252.23-6.amzn2023  |
|  systemd-udev-252.23-6.amzn2023  |
|  systemd-252.23-6.amzn2023  |

### Default Container
<a name="amis-2023.8.20250804.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250804-0.amzn2023  |
|  system-release-2023.8.20250804-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250804.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250804-0.amzn2023  |
|  system-release-2023.8.20250804-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250804.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
