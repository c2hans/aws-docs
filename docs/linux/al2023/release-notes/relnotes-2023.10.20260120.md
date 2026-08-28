---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260120.html
---

# Amazon Linux 2023 version 2023.10.20260120 release notes
<a name="relnotes-2023.10.20260120"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260120.

**Contents**
+ [Release Summary](#release-summary-2023.10.20260120)
+ [Repository Updates](#repository-updates-2023.10.20260120)
  + [Core New Packages](#amis-2023.10.20260120.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260120.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.10.20260120.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.10.20260120.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.10.20260120)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260120.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260120.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260120.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260120.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.10.20260120.Default-Container)
  + [Minimal Container](#amis-2023.10.20260120.Minimal-Container)
+ [Contact us](#amis-2023.10.20260120.contact-us)

## Release Summary
<a name="release-summary-2023.10.20260120"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260120"></a>

### Core New Packages
<a name="amis-2023.10.20260120.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  drbd-9.33.0-1.amzn2023.0.1  |
|  maven3.9-3.9.9-3.amzn2023.0.1  |
|  php8.5-8.5.1-1.amzn2023.0.1  |
|  python3.13-zipp-3.21.0-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.10.20260120.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.29-1.amzn2023.0.4  |
|  aws-nitro-enclaves-cli-1.4.4-0.amzn2023  |
|  cmake-3.22.2-1.amzn2023.0.5  |
|  composer-2.9.3-1.amzn2023.0.1  |
|  containerd-2.1.5-1.amzn2023.0.4  |
|  decibels-48.0-7.amzn2023  |
|  dnf-plugin-release-notification-1.3-1.amzn2023.0.1  |
|  ec2-hibinit-agent-1.0.10-1.amzn2023  |
|  ecs-init-1.101.2-1.amzn2023  |
|  flexiblas-3.0.4-3.amzn2023.0.3  |
|  fontforge-20201107-3.amzn2023.0.5  |
|  gnupg2-2.3.7-1.amzn2023.0.6  |
|  highway-1.2.0-31.amzn2023.0.2  |
|  kernel-6.1.159-182.297.amzn2023  |
|  kernel6.12-6.12.64-87.122.amzn2023  |
|  libheif-1.19.8-1.amzn2023.0.3  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  mod\_security\_crs-4.2.0-1.amzn2023.0.2  |
|  nerdctl-2.2.1-1.amzn2023.0.1  |
|  net-snmp-5.9.3-2.amzn2023.0.4  |
|  nginx-1.28.1-1.amzn2023.0.1  |
|  openexr-3.1.5-1.amzn2023.0.6  |
|  python-pip-21.3.1-2.amzn2023.0.15  |
|  python3.11-pip-22.3.1-2.amzn2023.0.9  |
|  python3.12-pip-23.2.1-4.amzn2023.0.6  |
|  python3.13-pip-24.2-259.amzn2023.0.2  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Nvidia New Packages
<a name="amis-2023.10.20260120.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  cuda-13-1-13.1.0-1  |
|  cuda-cccl-13-1-13.1.78-1  |
|  cuda-command-line-tools-13-1-13.1.0-1  |
|  cuda-compiler-13-1-13.1.0-1  |
|  cuda-crt-13-1-13.1.80-1  |
|  cuda-ctadvisor-13-1-13.1.80-1  |
|  cuda-cudart-13-1-13.1.80-1  |
|  cuda-cudart-devel-13-1-13.1.80-1  |
|  cuda-culibos-devel-13-1-13.1.68-1  |
|  cuda-cuobjdump-13-1-13.1.80-1  |
|  cuda-cupti-13-1-13.1.75-1  |
|  cuda-cuxxfilt-13-1-13.1.80-1  |
|  cuda-documentation-13-1-13.1.80-1  |
|  cuda-driver-devel-13-1-13.1.80-1  |
|  cuda-gdb-13-1-13.1.68-1  |
|  cuda-gdb-src-13-1-13.1.68-1  |
|  cuda-libraries-13-1-13.1.0-1  |
|  cuda-libraries-devel-13-1-13.1.0-1  |
|  cuda-minimal-build-13-1-13.1.0-1  |
|  cuda-nsight-13-1-13.1.68-1  |
|  cuda-nsight-compute-13-1-13.1.0-1  |
|  cuda-nsight-systems-13-1-13.1.0-1  |
|  cuda-nvcc-13-1-13.1.80-1  |
|  cuda-nvdisasm-13-1-13.1.80-1  |
|  cuda-nvml-devel-13-1-13.1.68-1  |
|  cuda-nvprune-13-1-13.1.80-1  |
|  cuda-nvrtc-13-1-13.1.80-1  |
|  cuda-nvrtc-devel-13-1-13.1.80-1  |
|  cuda-nvtx-13-1-13.1.68-1  |
|  cuda-opencl-13-1-13.1.80-1  |
|  cuda-opencl-devel-13-1-13.1.80-1  |
|  cuda-profiler-api-13-1-13.1.80-1  |
|  cuda-runtime-13-1-13.1.0-1  |
|  cuda-sandbox-devel-13-1-13.1.68-1  |
|  cuda-sanitizer-13-1-13.1.75-1  |
|  cuda-tileiras-13-1-13.1.80-1  |
|  cuda-toolkit-13-1-13.1.0-1  |
|  cuda-toolkit-13-1-config-common-13.1.80-1  |
|  cuda-tools-13-1-13.1.0-1  |
|  cuda-visual-tools-13-1-13.1.0-1  |
|  egl-wayland2-1.0.1\~20251112git0c15809-6.amzn2023  |
|  gds-tools-13-1-1.16.0.49-1  |
|  libcublas-13-1-13.2.0.9-1  |
|  libcublas-devel-13-1-13.2.0.9-1  |
|  libcufft-13-1-12.1.0.31-1  |
|  libcufft-devel-13-1-12.1.0.31-1  |
|  libcufile-13-1-1.16.0.49-1  |
|  libcufile-devel-13-1-1.16.0.49-1  |
|  libcurand-13-1-10.4.1.34-1  |
|  libcurand-devel-13-1-10.4.1.34-1  |
|  libcusolver-13-1-12.0.7.41-1  |
|  libcusolver-devel-13-1-12.0.7.41-1  |
|  libcusparse-13-1-12.7.2.19-1  |
|  libcusparse-devel-13-1-12.7.2.19-1  |
|  libnpp-13-1-13.0.2.21-1  |
|  libnpp-devel-13-1-13.0.2.21-1  |
|  libnvfatbin-13-1-13.1.80-1  |
|  libnvfatbin-devel-13-1-13.1.80-1  |
|  libnvjitlink-13-1-13.1.80-1  |
|  libnvjitlink-devel-13-1-13.1.80-1  |
|  libnvjpeg-13-1-13.0.2.28-1  |
|  libnvjpeg-devel-13-1-13.0.2.28-1  |
|  libnvptxcompiler-13-1-13.1.80-1  |
|  libnvvm-13-1-13.1.80-1  |
|  nsight-compute-2025.4.0-2025.4.0.12-1  |
|  nsight-systems-2025.5.2-2025.5.2.266\_255236693005v0-0  |
|  nvidia-gds-13-1-13.1.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.10.20260120.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-13.1.0-1  |
|  cuda-compat-12-8-570.211.01-1.amzn2023  |
|  cuda-compat-13-0-580.126.09-1.amzn2023  |
|  cuda-drivers-580.126.09-1.amzn2023  |
|  cuda-toolkit-13.1.0-1  |
|  cuda-toolkit-13-13.1.0-1  |
|  cuda-toolkit-13-config-common-13.1.80-1  |
|  cuda-toolkit-config-common-13.1.80-1  |
|  datacenter-gpu-manager-4-core-4.4.2-1  |
|  datacenter-gpu-manager-4-cuda-all-4.4.2-1  |
|  datacenter-gpu-manager-4-cuda11-4.4.2-1  |
|  datacenter-gpu-manager-4-cuda12-4.4.2-1  |
|  datacenter-gpu-manager-4-cuda13-4.4.2-1  |
|  datacenter-gpu-manager-4-devel-4.4.2-1  |
|  datacenter-gpu-manager-4-multinode-4.4.2-1  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.4.2-1  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.4.2-1  |
|  datacenter-gpu-manager-4-proprietary-4.4.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.4.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.4.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.4.2-1  |
|  egl-wayland-1.1.21-1.amzn2023  |
|  egl-wayland-devel-1.1.21-1.amzn2023  |
|  egl-x11-1.0.4-1.amzn2023  |
|  kmod-nvidia-latest-dkms-580.126.09-1.amzn2023  |
|  kmod-nvidia-open-dkms-580.126.09-1.amzn2023  |
|  libnvidia-cfg-580.126.09-1.amzn2023  |
|  libnvidia-container-devel-1.18.1-1  |
|  libnvidia-container-static-1.18.1-1  |
|  libnvidia-container-tools-1.18.1-1  |
|  libnvidia-container1-1.18.1-1  |
|  libnvidia-fbc-580.126.09-1.amzn2023  |
|  libnvidia-gpucomp-580.126.09-1.amzn2023  |
|  libnvidia-ml-580.126.09-1.amzn2023  |
|  libnvidia-nscq-580.126.09-1  |
|  libnvidia-nscq-570-570.211.01-1  |
|  libnvsdm-580.126.09-1  |
|  libnvsdm-570-570.211.01-1  |
|  libnvsdm-devel-580.126.09-1  |
|  mft-4.34.1.10-1  |
|  mft-autocomplete-4.34.1.10-1  |
|  mft-oem-4.34.1.10-1  |
|  nvidia-container-toolkit-1.18.1-1  |
|  nvidia-container-toolkit-base-1.18.1-1  |
|  nvidia-driver-580.126.09-1.amzn2023  |
|  nvidia-driver-assistant-0.22.126.09-1  |
|  nvidia-driver-cuda-580.126.09-1.amzn2023  |
|  nvidia-driver-cuda-libs-580.126.09-1.amzn2023  |
|  nvidia-driver-libs-580.126.09-1.amzn2023  |
|  nvidia-fabric-manager-570.211.01-1  |
|  nvidia-fabric-manager-devel-580.126.09-1  |
|  nvidia-fabricmanager-580.126.09-1  |
|  nvidia-fs-2.27.3-1  |
|  nvidia-fs-dkms-2.27.3-1  |
|  nvidia-gds-13.1.0-1  |
|  nvidia-imex-580.126.09-1  |
|  nvidia-imex-570-570.211.01-1  |
|  nvidia-kmod-common-580.126.09-1.amzn2023  |
|  nvidia-libXNVCtrl-580.126.09-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-580.126.09-1.amzn2023  |
|  nvidia-modprobe-580.126.09-1.amzn2023  |
|  nvidia-open-580.126.09-1.amzn2023  |
|  nvidia-persistenced-580.126.09-1.amzn2023  |
|  nvidia-settings-580.126.09-1.amzn2023  |
|  nvidia-xconfig-580.126.09-1.amzn2023  |
|  nvlink5-580.126.09-1  |
|  nvlink5-570-570.211.01-1  |
|  nvlink5-580-580.126.09-1  |
|  nvlsm-2025.06.11-1  |
|  xorg-x11-nvidia-580.126.09-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.10.20260120"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260120.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260120-0.amzn2023  |
|  dnf-plugin-release-notification-1.3-1.amzn2023.0.1  |
|  ec2-hibinit-agent-1.0.10-1.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  kernel-libbpf-1:6.1.159-182.297.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260120-0.amzn2023  |
|  kernel-tools-1:6.1.159-182.297.amzn2023  |
|  kernel-1:6.1.159-182.297.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260120.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260120-0.amzn2023  |
|  dnf-plugin-release-notification-1.3-1.amzn2023.0.1  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  kernel-libbpf-1:6.1.159-182.297.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260120-0.amzn2023  |
|  kernel-1:6.1.159-182.297.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260120.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260120-0.amzn2023  |
|  dnf-plugin-release-notification-1.3-1.amzn2023.0.1  |
|  ec2-hibinit-agent-1.0.10-1.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.10.20260120-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.64-87.122.amzn2023  |
|  kernel6.12-tools-1:6.12.64-87.122.amzn2023  |
|  kernel6.12-1:6.12.64-87.122.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260120.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260120-0.amzn2023  |
|  dnf-plugin-release-notification-1.3-1.amzn2023.0.1  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.10.20260120-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.64-87.122.amzn2023  |
|  kernel6.12-1:6.12.64-87.122.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.10.20260120.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260120-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

### Minimal Container
<a name="amis-2023.10.20260120.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260120-0.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.15  |
|  system-release-2023.10.20260120-0.amzn2023  |
|  tzdata-2025c-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.10.20260120.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
