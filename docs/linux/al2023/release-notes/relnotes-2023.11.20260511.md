---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.11.20260511.html
---

# Amazon Linux 2023 version 2023.11.20260511 release notes
<a name="relnotes-2023.11.20260511"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.11.20260511.

**Contents**
+ [Release Summary](#release-summary-2023.11.20260511)
+ [Repository Updates](#repository-updates-2023.11.20260511)
  + [Core New Packages](#amis-2023.11.20260511.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.11.20260511.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.11.20260511.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.11.20260511.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.11.20260511)
  + [Default Kernel 6.18 AMI](#amis-2023.11.20260511.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.11.20260511.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.11.20260511.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.11.20260511.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.11.20260511.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.11.20260511.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.11.20260511.Default-Container)
  + [Minimal Container](#amis-2023.11.20260511.Minimal-Container)
+ [Contact us](#amis-2023.11.20260511.contact-us)

## Release Summary
<a name="release-summary-2023.11.20260511"></a>

This release represents an update to the 11th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.11.20260511"></a>

### Core New Packages
<a name="amis-2023.11.20260511.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  gnome-user-docs-47.6-1.amzn2023  |
|  rust-askalono-cli-0.5.0-1.amzn2023.0.2  |

### Core Updated Packages
<a name="amis-2023.11.20260511.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  PackageKit-1.2.8-2.amzn2023.0.2  |
|  amazon-ecr-credential-helper-0.12.0-2.amzn2023  |
|  amazon-efs-utils-3.1.1-1.amzn2023  |
|  bouncycastle-1.70-4.amzn2023.0.6  |
|  cups-2.4.19-1.amzn2023.0.1  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  dnsmasq-2.90-1.amzn2023.0.2  |
|  docker-25.0.14-1.amzn2023.0.5  |
|  ecs-init-1.103.0-1.amzn2023  |
|  editorconfig-0.12.11-2.amzn2023.0.1  |
|  firefox-140.10.1-1.amzn2023.0.1  |
|  firewalld-1.2.3-1.amzn2023.0.2  |
|  freerdp-3.6.3-1.amzn2023.0.11  |
|  krb5-1.21.3-7.amzn2023.0.1  |
|  lcms2-2.19-75.amzn2023.0.1  |
|  libXpm-3.5.17-3.amzn2023.0.2  |
|  libabigail-2.3-1.amzn2023.0.2  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  libpng-1.6.37-10.amzn2023.0.13  |
|  microcode\_ctl-2.1-53.amzn2023.0.15  |
|  mount-s3-1.22.3-1.amzn2023  |
|  nginx-1.30.0-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.5  |
|  nodejs22-22.22.2-1.amzn2023.0.3  |
|  nodejs24-24.15.0-1.amzn2023.0.2  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.10  |
|  openvpn-2.6.12-1.amzn2023.0.4  |
|  perl-CryptX-0.088-2.amzn2023.0.1  |
|  php8.4-8.4.20-1.amzn2023.0.1  |
|  php8.5-8.5.5-1.amzn2023.0.1  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python-lxml-4.7.1-3.amzn2023.0.3  |
|  python3.11-pip-22.3.1-2.amzn2023.0.12  |
|  python3.12-pip-23.2.1-4.amzn2023.0.9  |
|  python3.13-3.13.13-1.amzn2023.0.2  |
|  python3.13-lxml-5.3.2-3.amzn2023.0.2  |
|  python3.13-pip-24.2-259.amzn2023.0.5  |
|  python3.14-3.14.4-2.amzn2023.0.1  |
|  python3.14-pip-25.1.1-1.amzn2023.0.2  |
|  rclone-1.73.5-75.amzn2023  |
|  runc-1.3.4-4.amzn2023.0.2  |
|  runfinch-finch-1.17.0-1.amzn2023.0.1  |
|  rust-1.95.0-1.amzn2023.0.2  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tomcat10-10.1.54-1.amzn2023.0.1  |
|  tomcat9-9.0.117-1.amzn2023.0.1  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-9.2.240-1.amzn2023.0.3  |
|  wireshark-4.4.2-1.amzn2023.0.5  |
|  xdg-desktop-portal-1.18.4-107.amzn2023  |
|  yelp-tools-42.1-6.amzn2023.0.2  |

### Nvidia New Packages
<a name="amis-2023.11.20260511.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  nsight-compute-2025.1.1-2025.1.1.2-1  |

### Nvidia Updated Packages
<a name="amis-2023.11.20260511.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cublas-13.4.1-1  |
|  cublas-cuda-13-13.4.1.2-1  |
|  cublas13-13.4.1-1  |
|  cuda-12-8-12.8.2-1  |
|  cuda-13-1-13.1.2-1  |
|  cuda-cccl-12-8-12.8.90-1  |
|  cuda-command-line-tools-12-8-12.8.2-1  |
|  cuda-command-line-tools-13-1-13.1.2-1  |
|  cuda-compat-13-0-580.159.03-1.amzn2023  |
|  cuda-compat-13-2-595.71.05-1.amzn2023  |
|  cuda-compiler-12-8-12.8.2-1  |
|  cuda-compiler-13-1-13.1.2-1  |
|  cuda-crt-12-8-12.8.93-1  |
|  cuda-cudart-12-8-12.8.90-1  |
|  cuda-cudart-devel-12-8-12.8.90-1  |
|  cuda-cuobjdump-12-8-12.8.90-1  |
|  cuda-cupti-12-8-12.8.90-1  |
|  cuda-cuxxfilt-12-8-12.8.90-1  |
|  cuda-demo-suite-12-8-12.8.90-1  |
|  cuda-documentation-12-8-12.8.90-1  |
|  cuda-driver-devel-12-8-12.8.90-1  |
|  cuda-drivers-595.71.05-1.amzn2023  |
|  cuda-gdb-12-8-12.8.90-1  |
|  cuda-gdb-src-12-8-12.8.90-1  |
|  cuda-libraries-12-8-12.8.2-1  |
|  cuda-libraries-13-1-13.1.2-1  |
|  cuda-libraries-devel-12-8-12.8.2-1  |
|  cuda-libraries-devel-13-1-13.1.2-1  |
|  cuda-minimal-build-12-8-12.8.2-1  |
|  cuda-minimal-build-13-1-13.1.2-1  |
|  cuda-nsight-12-8-12.8.90-1  |
|  cuda-nsight-compute-12-8-12.8.2-1  |
|  cuda-nsight-compute-13-1-13.1.2-1  |
|  cuda-nsight-systems-12-8-12.8.2-1  |
|  cuda-nsight-systems-13-1-13.1.2-1  |
|  cuda-nvcc-12-8-12.8.93-1  |
|  cuda-nvdisasm-12-8-12.8.90-1  |
|  cuda-nvml-devel-12-8-12.8.90-1  |
|  cuda-nvprof-12-8-12.8.90-1  |
|  cuda-nvprune-12-8-12.8.90-1  |
|  cuda-nvrtc-12-8-12.8.93-1  |
|  cuda-nvrtc-devel-12-8-12.8.93-1  |
|  cuda-nvtx-12-8-12.8.90-1  |
|  cuda-nvvm-12-8-12.8.93-1  |
|  cuda-nvvp-12-8-12.8.93-1  |
|  cuda-opencl-12-8-12.8.90-1  |
|  cuda-opencl-devel-12-8-12.8.90-1  |
|  cuda-profiler-api-12-8-12.8.90-1  |
|  cuda-runtime-12-8-12.8.2-1  |
|  cuda-runtime-13-1-13.1.2-1  |
|  cuda-sandbox-devel-12-8-12.8.90-1  |
|  cuda-sanitizer-12-8-12.8.93-1  |
|  cuda-toolkit-12-8-12.8.2-1  |
|  cuda-toolkit-12-8-config-common-12.8.90-1  |
|  cuda-toolkit-13-1-13.1.2-1  |
|  cuda-tools-12-8-12.8.2-1  |
|  cuda-tools-13-1-13.1.2-1  |
|  cuda-visual-tools-12-8-12.8.2-1  |
|  cuda-visual-tools-13-1-13.1.2-1  |
|  cuquantum-26.03.2-1  |
|  cuquantum-cuda-12-26.03.2.11-1  |
|  cuquantum-cuda-13-26.03.2.11-1  |
|  cuquantum0-26.03.2-1  |
|  gds-tools-12-8-1.13.1.3-1  |
|  kmod-nvidia-latest-dkms-595.71.05-1.amzn2023  |
|  kmod-nvidia-open-dkms-595.71.05-1.amzn2023  |
|  libcublas-12-8-12.8.5.5-1  |
|  libcublas-13-1-13.2.2.2-1  |
|  libcublas-devel-12-8-12.8.5.5-1  |
|  libcublas-devel-13-1-13.2.2.2-1  |
|  libcublas13-cuda-13-13.4.1.2-1  |
|  libcublas13-devel-cuda-13-13.4.1.2-1  |
|  libcufft-12-8-11.3.3.83-1  |
|  libcufft-devel-12-8-11.3.3.83-1  |
|  libcufile-12-8-1.13.1.3-1  |
|  libcufile-devel-12-8-1.13.1.3-1  |
|  libcuquantum0-cuda-12-26.03.2.11-1  |
|  libcuquantum0-cuda-13-26.03.2.11-1  |
|  libcuquantum0-devel-cuda-12-26.03.2.11-1  |
|  libcuquantum0-devel-cuda-13-26.03.2.11-1  |
|  libcuquantum0-static-cuda-12-26.03.2.11-1  |
|  libcuquantum0-static-cuda-13-26.03.2.11-1  |
|  libcurand-12-8-10.3.9.90-1  |
|  libcurand-devel-12-8-10.3.9.90-1  |
|  libcusolver-12-8-11.7.3.90-1  |
|  libcusolver-devel-12-8-11.7.3.90-1  |
|  libcusparse-12-8-12.5.8.93-1  |
|  libcusparse-devel-12-8-12.5.8.93-1  |
|  libnpp-12-8-12.3.3.100-1  |
|  libnpp-devel-12-8-12.3.3.100-1  |
|  libnvat-1.2.1.1777487608-1  |
|  libnvat-devel-1.2.1.1777487608-1  |
|  libnvfatbin-12-8-12.8.90-1  |
|  libnvfatbin-devel-12-8-12.8.90-1  |
|  libnvidia-cfg-595.71.05-1.amzn2023  |
|  libnvidia-fbc-595.71.05-1.amzn2023  |
|  libnvidia-gpucomp-595.71.05-1.amzn2023  |
|  libnvidia-ml-595.71.05-1.amzn2023  |
|  libnvidia-nscq-595.71.05-1.amzn2023  |
|  libnvjitlink-12-8-12.8.93-1  |
|  libnvjitlink-devel-12-8-12.8.93-1  |
|  libnvjpeg-12-8-12.3.5.92-1  |
|  libnvjpeg-devel-12-8-12.3.5.92-1  |
|  libnvsdm-595.71.05-1.amzn2023  |
|  libnvsdm-devel-595.71.05-1.amzn2023  |
|  mft-4.35.0.159-1  |
|  mft-autocomplete-4.35.0.159-1  |
|  mft-oem-4.35.0.159-1  |
|  nvattest-1.2.1.1777487608-1  |
|  nvidia-driver-595.71.05-1.amzn2023  |
|  nvidia-driver-assistant-0.51.71.05-1  |
|  nvidia-driver-cuda-595.71.05-1.amzn2023  |
|  nvidia-driver-cuda-libs-595.71.05-1.amzn2023  |
|  nvidia-driver-libs-595.71.05-1.amzn2023  |
|  nvidia-fabric-manager-devel-595.71.05-1.amzn2023  |
|  nvidia-fabricmanager-595.71.05-1.amzn2023  |
|  nvidia-gds-12-8-12.8.2-1  |
|  nvidia-gds-13-1-13.1.2-1  |
|  nvidia-imex-595.71.05-1.amzn2023  |
|  nvidia-kmod-common-595.71.05-1.amzn2023  |
|  nvidia-libXNVCtrl-595.71.05-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-595.71.05-1.amzn2023  |
|  nvidia-modprobe-595.71.05-1.amzn2023  |
|  nvidia-open-595.71.05-1.amzn2023  |
|  nvidia-persistenced-595.71.05-1.amzn2023  |
|  nvidia-settings-595.71.05-1.amzn2023  |
|  nvidia-xconfig-595.71.05-1.amzn2023  |
|  nvlink5-595.71.05-1  |
|  nvlink5-580-580.159.03-1  |
|  nvlsm-2025.10.12-1  |
|  xorg-x11-nvidia-595.71.05-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.11.20260511"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.11.20260511.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-python-utils-3.4-6.amzn2023.0.3  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.2  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-common-2:9.2.240-1.amzn2023.0.3  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.3  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  xxd-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.11.20260511.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Default Kernel 6.12 AMI
<a name="amis-2023.11.20260511.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-python-utils-3.4-6.amzn2023.0.3  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.2  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-common-2:9.2.240-1.amzn2023.0.3  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.3  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  xxd-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.11.20260511.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Default Kernel 6.1 AMI
<a name="amis-2023.11.20260511.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-python-utils-3.4-6.amzn2023.0.3  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.95.0-1.amzn2023.0.2  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-common-2:9.2.240-1.amzn2023.0.3  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.3  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  xxd-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.11.20260511.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.11.20260511-0.amzn2023  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.15  |
|  policycoreutils-3.4-6.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-policycoreutils-3.4-6.amzn2023.0.3  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  vim-data-2:9.2.240-1.amzn2023.0.3  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.3  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Default Container
<a name="amis-2023.11.20260511.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.7  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  python3-dnf-4.14.0-1.amzn2023.0.7  |
|  python3-hawkey-0.69.0-8.amzn2023.0.8  |
|  python3-libdnf-0.69.0-8.amzn2023.0.8  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |
|  yum-4.14.0-1.amzn2023.0.7  |

### Minimal Container
<a name="amis-2023.11.20260511.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260511-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.7  |
|  krb5-libs-1.21.3-7.amzn2023.0.1  |
|  libdnf-0.69.0-8.amzn2023.0.8  |
|  system-release-2023.11.20260511-0.amzn2023  |
|  tzdata-2026b-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.11.20260511.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
