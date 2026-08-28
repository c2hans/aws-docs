---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250414.html
---

# Amazon Linux 2023 version 2023.7.20250414 release notes
<a name="relnotes-2023.7.20250414"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250414.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250414)
+ [Repository Updates](#repository-updates-2023.7.20250414)
  + [Core New Packages](#amis-2023.7.20250414.core-new-packages)
  + [Core Updated Packages](#amis-2023.7.20250414.core-updated-packages)
  + [Kernel-livepatch New Packages](#amis-2023.7.20250414.kernel-livepatch-new-packages)
  + [Nvidia New Packages](#amis-2023.7.20250414.nvidia-new-packages)
  + [Nvidia Updated Packages](#amis-2023.7.20250414.nvidia-updated-packages)
+ [Image Updates](#ami-updates-2023.7.20250414)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250414.default-kernel-6.1-ami)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250414.minimal-kernel-6.1-ami)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250414.default-kernel-6.12-ami)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250414.minimal-kernel-6.12-ami)
  + [Default Container](#amis-2023.7.20250414.default-container)
  + [Minimal Container](#amis-2023.7.20250414.minimal-container)
+ [Contact us](#amis-2023.7.20250414.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250414"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Notable updates**
+  nodejs22-22.14.0-1.amzn2023.0.1: NodeJS 22 is now available in the `nodejs22` package. It uses the `alternatives` tool to select an active version and can be installed simultaneously with the `nodejs` and `nodejs20` packages in any combination. Resolves (partially) [Github issue \#725](https://github.com/amazonlinux/amazon-linux-2023/issues/725)

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250414"></a>

### Core New Packages
<a name="amis-2023.7.20250414.core-new-packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  nodejs22-22.14.0-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.7.20250414.core-updated-packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  clang-15.0.7-3.amzn2023.0.3  |
|  containerd-1.7.27-1.amzn2023.0.2  |
|  docker-25.0.8-1.amzn2023.0.2  |
|  ecs-service-connect-agent-v1.29.12.1-1.amzn2023  |
|  ghostscript-9.56.1-7.amzn2023.0.16  |
|  golang-1.24.2-1.amzn2023.0.1  |
|  grub2-2.06-61.amzn2023.0.17  |
|  kernel-6.1.132-147.221.amzn2023  |
|  kernel-srpm-macros-1.0-14.amzn2023.0.3  |
|  kernel6.12-6.12.22-27.96.amzn2023  |
|  microcode\_ctl-2.1-53.amzn2023.0.12  |
|  nerdctl-2.0.4-1.amzn2023.0.1  |
|  php8.2-8.2.28-1.amzn2023.0.1  |
|  python-requests-2.25.1-1.amzn2023.0.5  |
|  redis6-6.2.14-2.amzn2023.0.3  |
|  ruby3.2-3.2.7-183.amzn2023.0.4  |
|  system-release-2023.7.20250414-0.amzn2023  |
|  systemd-252.23-3.amzn2023  |
|  vim-9.1.1202-1.amzn2023.0.1  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.5  |

### Kernel-livepatch New Packages
<a name="amis-2023.7.20250414.kernel-livepatch-new-packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.127-135.201-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.128-136.201-1.0-2.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.7.20250414.nvidia-new-packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  cuda-12-8-12.8.0-1  |
|  cuda-cccl-12-8-12.8.55-1  |
|  cuda-command-line-tools-12-8-12.8.0-1  |
|  cuda-compat-12-8-570.86.15-1.amzn2023  |
|  cuda-compiler-12-8-12.8.0-1  |
|  cuda-crt-12-8-12.8.61-1  |
|  cuda-cudart-12-8-12.8.57-1  |
|  cuda-cudart-devel-12-8-12.8.57-1  |
|  cuda-cuobjdump-12-8-12.8.55-1  |
|  cuda-cupti-12-8-12.8.57-1  |
|  cuda-cuxxfilt-12-8-12.8.55-1  |
|  cuda-demo-suite-12-8-12.8.55-1  |
|  cuda-documentation-12-8-12.8.55-1  |
|  cuda-driver-devel-12-8-12.8.57-1  |
|  cuda-gdb-12-8-12.8.55-1  |
|  cuda-gdb-src-12-8-12.8.55-1  |
|  cuda-libraries-12-8-12.8.0-1  |
|  cuda-libraries-devel-12-8-12.8.0-1  |
|  cuda-minimal-build-12-8-12.8.0-1  |
|  cuda-nsight-12-8-12.8.55-1  |
|  cuda-nsight-compute-12-8-12.8.0-1  |
|  cuda-nsight-systems-12-8-12.8.0-1  |
|  cuda-nvcc-12-8-12.8.61-1  |
|  cuda-nvdisasm-12-8-12.8.55-1  |
|  cuda-nvml-devel-12-8-12.8.55-1  |
|  cuda-nvprof-12-8-12.8.57-1  |
|  cuda-nvprune-12-8-12.8.55-1  |
|  cuda-nvrtc-12-8-12.8.61-1  |
|  cuda-nvrtc-devel-12-8-12.8.61-1  |
|  cuda-nvtx-12-8-12.8.55-1  |
|  cuda-nvvm-12-8-12.8.61-1  |
|  cuda-nvvp-12-8-12.8.57-1  |
|  cuda-opencl-12-8-12.8.55-1  |
|  cuda-opencl-devel-12-8-12.8.55-1  |
|  cuda-profiler-api-12-8-12.8.55-1  |
|  cuda-runtime-12-8-12.8.0-1  |
|  cuda-sandbox-devel-12-8-12.8.55-1  |
|  cuda-sanitizer-12-8-12.8.55-1  |
|  cuda-toolkit-12-8-12.8.0-1  |
|  cuda-toolkit-12-8-config-common-12.8.57-1  |
|  cuda-tools-12-8-12.8.0-1  |
|  cuda-visual-tools-12-8-12.8.0-1  |
|  gds-tools-12-8-1.13.0.11-1  |
|  libcublas-12-8-12.8.3.14-1  |
|  libcublas-devel-12-8-12.8.3.14-1  |
|  libcufft-12-8-11.3.3.41-1  |
|  libcufft-devel-12-8-11.3.3.41-1  |
|  libcufile-12-8-1.13.0.11-1  |
|  libcufile-devel-12-8-1.13.0.11-1  |
|  libcurand-12-8-10.3.9.55-1  |
|  libcurand-devel-12-8-10.3.9.55-1  |
|  libcusolver-12-8-11.7.2.55-1  |
|  libcusolver-devel-12-8-11.7.2.55-1  |
|  libcusparse-12-8-12.5.7.53-1  |
|  libcusparse-devel-12-8-12.5.7.53-1  |
|  libnpp-12-8-12.3.3.65-1  |
|  libnpp-devel-12-8-12.3.3.65-1  |
|  libnvfatbin-12-8-12.8.55-1  |
|  libnvfatbin-devel-12-8-12.8.55-1  |
|  libnvidia-nscq-570-570.86.15-1  |
|  libnvjitlink-12-8-12.8.61-1  |
|  libnvjitlink-devel-12-8-12.8.61-1  |
|  libnvjpeg-12-8-12.3.5.57-1  |
|  libnvjpeg-devel-12-8-12.3.5.57-1  |
|  libnvsdm-570-570.86.15-1  |
|  nsight-compute-2025.1.0-2025.1.0.14-1  |
|  nsight-systems-2024.6.2-2024.6.2.225\_246235244400v0-0  |
|  nvidia-gds-12-8-12.8.0-1  |
|  nvidia-imex-570-570.86.15-1  |

### Nvidia Updated Packages
<a name="amis-2023.7.20250414.nvidia-updated-packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-12.8.0-1  |
|  cuda-drivers-570.86.15-1.amzn2023  |
|  cuda-toolkit-12.8.0-1  |
|  cuda-toolkit-12-12.8.0-1  |
|  cuda-toolkit-12-config-common-12.8.57-1  |
|  cuda-toolkit-config-common-12.8.57-1  |
|  kmod-nvidia-latest-dkms-570.86.15-1.amzn2023  |
|  kmod-nvidia-open-dkms-570.86.15-1.amzn2023  |
|  libnvidia-cfg-570.86.15-1.amzn2023  |
|  libnvidia-ml-570.86.15-1.amzn2023  |
|  nvidia-driver-assistant-0.18.86.15-1  |
|  nvidia-driver-cuda-570.86.15-1.amzn2023  |
|  nvidia-driver-cuda-libs-570.86.15-1.amzn2023  |
|  nvidia-fs-2.24.2-1  |
|  nvidia-fs-dkms-2.24.2-1  |
|  nvidia-gds-12.8.0-1  |
|  nvidia-kmod-common-570.86.15-1.amzn2023  |
|  nvidia-modprobe-570.86.15-1.amzn2023  |
|  nvidia-open-570.86.15-1.amzn2023  |
|  nvidia-persistenced-570.86.15-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.7.20250414"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250414.default-kernel-6.1-ami"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250414-0.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.17  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.17  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-1:2.06-61.amzn2023.0.17  |
|  kernel-libbpf-6.12.22-27.96.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250414-0.amzn2023  |
|  kernel-srpm-macros-1.0-14.amzn2023.0.3  |
|  kernel-tools-6.12.22-27.96.amzn2023  |
|  kernel-6.1.132-147.221.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.12  |
|  python3-requests-2.25.1-1.amzn2023.0.5  |
|  system-release-2023.7.20250414-0.amzn2023  |
|  systemd-libs-252.23-3.amzn2023  |
|  systemd-networkd-252.23-3.amzn2023  |
|  systemd-pam-252.23-3.amzn2023  |
|  systemd-resolved-252.23-3.amzn2023  |
|  systemd-udev-252.23-3.amzn2023  |
|  systemd-252.23-3.amzn2023  |
|  vim-common-2:9.1.1202-1.amzn2023.0.1  |
|  vim-data-2:9.1.1202-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1202-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1202-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1202-1.amzn2023.0.1  |
|  xxd-2:9.1.1202-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250414.minimal-kernel-6.1-ami"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250414-0.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.17  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.17  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-1:2.06-61.amzn2023.0.17  |
|  kernel-libbpf-6.12.22-27.96.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250414-0.amzn2023  |
|  kernel-6.1.132-147.221.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.12  |
|  python3-requests-2.25.1-1.amzn2023.0.5  |
|  system-release-2023.7.20250414-0.amzn2023  |
|  systemd-libs-252.23-3.amzn2023  |
|  systemd-networkd-252.23-3.amzn2023  |
|  systemd-pam-252.23-3.amzn2023  |
|  systemd-resolved-252.23-3.amzn2023  |
|  systemd-udev-252.23-3.amzn2023  |
|  systemd-252.23-3.amzn2023  |
|  vim-data-2:9.1.1202-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1202-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250414.default-kernel-6.12-ami"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250414-0.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.17  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.17  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-1:2.06-61.amzn2023.0.17  |
|  kernel-libbpf-6.12.22-27.96.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250414-0.amzn2023  |
|  kernel-srpm-macros-1.0-14.amzn2023.0.3  |
|  kernel-tools-6.12.22-27.96.amzn2023  |
|  kernel6.12-6.12.22-27.96.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.12  |
|  python3-requests-2.25.1-1.amzn2023.0.5  |
|  system-release-2023.7.20250414-0.amzn2023  |
|  systemd-libs-252.23-3.amzn2023  |
|  systemd-networkd-252.23-3.amzn2023  |
|  systemd-pam-252.23-3.amzn2023  |
|  systemd-resolved-252.23-3.amzn2023  |
|  systemd-udev-252.23-3.amzn2023  |
|  systemd-252.23-3.amzn2023  |
|  vim-common-2:9.1.1202-1.amzn2023.0.1  |
|  vim-data-2:9.1.1202-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1202-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1202-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1202-1.amzn2023.0.1  |
|  xxd-2:9.1.1202-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250414.minimal-kernel-6.12-ami"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250414-0.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.17  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.17  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.17  |
|  grub2-tools-1:2.06-61.amzn2023.0.17  |
|  kernel-libbpf-6.12.22-27.96.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250414-0.amzn2023  |
|  kernel6.12-6.12.22-27.96.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.12  |
|  python3-requests-2.25.1-1.amzn2023.0.5  |
|  system-release-2023.7.20250414-0.amzn2023  |
|  systemd-libs-252.23-3.amzn2023  |
|  systemd-networkd-252.23-3.amzn2023  |
|  systemd-pam-252.23-3.amzn2023  |
|  systemd-resolved-252.23-3.amzn2023  |
|  systemd-udev-252.23-3.amzn2023  |
|  systemd-252.23-3.amzn2023  |
|  vim-data-2:9.1.1202-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1202-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.7.20250414.default-container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250414-0.amzn2023  |
|  system-release-2023.7.20250414-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250414.minimal-container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250414-0.amzn2023  |
|  system-release-2023.7.20250414-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250414.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
