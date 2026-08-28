---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250915.html
---

# Amazon Linux 2023 version 2023.8.20250915 release notes
<a name="relnotes-2023.8.20250915"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250915.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250915)
+ [Repository Updates](#repository-updates-2023.8.20250915)
  + [Core New Packages](#amis-2023.8.20250915.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.8.20250915.Core-Updated-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.8.20250915.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.8.20250915.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.8.20250915.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250915)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250915.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250915.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250915.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250915.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250915.Default-Container)
  + [Minimal Container](#amis-2023.8.20250915.Minimal-Container)
+ [Contact us](#amis-2023.8.20250915.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250915"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ CUDA 13.0 does not have support for P3 instance family. If you are running workloads on P3 instances, ensure you use a compatible CUDA version that supports the Tesla V100 GPUs available in P3 instances.
+ NVIDIA removed the dependency for `nvidia-driver-cuda` from the `nvidia-driver` meta-package. Starting with CUDA 13.0, the version provided in this release, customers need to include `nvidia-driver-cuda` in their install scripts to get the same experience as before.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250915"></a>

### Core New Packages
<a name="amis-2023.8.20250915.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  decibels-48.0-6.amzn2023  |
|  llvm19-19.1.7-13.amzn2023.0.1  |
|  mpg123-1.32.10-54.amzn2023  |
|  perl-Crypt-Blowfish-2.14-33.amzn2023.0.2  |
|  perl-Crypt-CBC-3.04-16.amzn2023.0.1  |
|  perl-Crypt-DES-2.07-30.amzn2023.0.2  |
|  perl-Crypt-IDEA-1.10-26.amzn2023.0.1  |
|  perl-Crypt-Rijndael-1.16-7.amzn2023.0.1  |
|  perl-Email-Valid-1.204-2.amzn2023.0.2  |
|  perl-Net-SNMP-6.0.1-42.amzn2023.0.1  |
|  python-tpm2-pytss-2.3.0-4.amzn2023.0.1  |
|  tpm2-pkcs11-1.9.1-2.amzn2023  |

### Core Updated Packages
<a name="amis-2023.8.20250915.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.12.82-1.amzn2023.0.11  |
|  containerd-2.0.6-1.amzn2023.0.1  |
|  docker-25.0.8-1.amzn2023.0.6  |
|  ecs-init-1.99.0-1.amzn2023  |
|  glibc-2.34-231.amzn2023.0.1  |
|  golang-1.24.7-1.amzn2023.0.1  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.2  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.3  |
|  httpd-2.4.65-1.amzn2023.0.1  |
|  kernel-6.1.150-174.273.amzn2023  |
|  libsoup-2.72.0-6.amzn2023.0.7  |
|  libtiff-4.4.0-4.amzn2023.0.22  |
|  libunwind-1.4.0-5.amzn2023.0.3  |
|  lustre-client-2.15.6-21.amzn2023  |
|  mod\_auth\_openidc-2.4.16.11-1.amzn2023  |
|  net-snmp-5.9.3-2.amzn2023.0.3  |
|  nodejs20-20.19.5-1.amzn2023.0.1  |
|  nodejs20-typescript-5.8.3-1.amzn2023.0.1  |
|  nodejs22-22.19.0-1.amzn2023.0.1  |
|  nodejs22-typescript-5.8.3-1.amzn2023.0.1  |
|  nvme-cli-2.13-1.amzn2023.0.2  |
|  postgresql16-16.10-1.amzn2023.0.1  |
|  python-h2-4.0.0-2.amzn2023.0.4  |
|  runfinch-finch-1.10.0-1.amzn2023.0.4  |
|  rust-1.89.0-1.amzn2023.0.3  |
|  rust-cargo-c-0.9.32-3.amzn2023.0.4  |
|  system-release-2023.8.20250915-0.amzn2023  |
|  tpm2-tss-4.0.2-1.amzn2023.0.1  |
|  wireshark-4.4.2-1.amzn2023.0.2  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.8.20250915.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.140-154.222-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.141-155.222-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.141-165.249-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.141-167.250-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.30-34.92-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.31-35.92-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.35-55.103-1.0-2.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.8.20250915.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  collectx-bringup-1.20.3-1  |
|  cuda-13-0-13.0.0-1  |
|  cuda-cccl-13-0-13.0.50-1  |
|  cuda-command-line-tools-13-0-13.0.0-1  |
|  cuda-compat-13-0-580.65.06-1.amzn2023  |
|  cuda-compiler-13-0-13.0.0-1  |
|  cuda-crt-13-0-13.0.48-1  |
|  cuda-ctadvisor-13-0-13.0.39-1  |
|  cuda-cudart-13-0-13.0.48-1  |
|  cuda-cudart-devel-13-0-13.0.48-1  |
|  cuda-culibos-devel-13-0-13.0.39-1  |
|  cuda-cuobjdump-13-0-13.0.39-1  |
|  cuda-cupti-13-0-13.0.48-1  |
|  cuda-cuxxfilt-13-0-13.0.39-1  |
|  cuda-documentation-13-0-13.0.39-1  |
|  cuda-driver-devel-13-0-13.0.48-1  |
|  cuda-gdb-13-0-13.0.39-1  |
|  cuda-gdb-src-13-0-13.0.39-1  |
|  cuda-libraries-13-0-13.0.0-1  |
|  cuda-libraries-devel-13-0-13.0.0-1  |
|  cuda-minimal-build-13-0-13.0.0-1  |
|  cuda-nsight-13-0-13.0.39-1  |
|  cuda-nsight-compute-13-0-13.0.0-1  |
|  cuda-nsight-systems-13-0-13.0.0-1  |
|  cuda-nvcc-13-0-13.0.48-1  |
|  cuda-nvdisasm-13-0-13.0.39-1  |
|  cuda-nvml-devel-13-0-13.0.39-1  |
|  cuda-nvprune-13-0-13.0.39-1  |
|  cuda-nvrtc-13-0-13.0.48-1  |
|  cuda-nvrtc-devel-13-0-13.0.48-1  |
|  cuda-nvtx-13-0-13.0.39-1  |
|  cuda-opencl-13-0-13.0.39-1  |
|  cuda-opencl-devel-13-0-13.0.39-1  |
|  cuda-profiler-api-13-0-13.0.39-1  |
|  cuda-runtime-13-0-13.0.0-1  |
|  cuda-sandbox-devel-13-0-13.0.39-1  |
|  cuda-sanitizer-13-0-13.0.48-1  |
|  cuda-toolkit-13-13.0.0-1  |
|  cuda-toolkit-13-0-13.0.0-1  |
|  cuda-toolkit-13-0-config-common-13.0.48-1  |
|  cuda-toolkit-13-config-common-13.0.48-1  |
|  cuda-tools-13-0-13.0.0-1  |
|  cuda-visual-tools-13-0-13.0.0-1  |
|  egl-gbm-1.1.2.1-1.amzn2023  |
|  egl-wayland-1.1.19-3.amzn2023  |
|  egl-wayland-devel-1.1.19-3.amzn2023  |
|  egl-x11-1.0.2-1.amzn2023  |
|  eglexternalplatform-devel-1.2.1-1.amzn2023  |
|  gds-tools-13-0-1.15.0.42-1  |
|  libcublas-13-0-13.0.0.19-1  |
|  libcublas-devel-13-0-13.0.0.19-1  |
|  libcufft-13-0-12.0.0.15-1  |
|  libcufft-devel-13-0-12.0.0.15-1  |
|  libcufile-13-0-1.15.0.42-1  |
|  libcufile-devel-13-0-1.15.0.42-1  |
|  libcurand-13-0-10.4.0.35-1  |
|  libcurand-devel-13-0-10.4.0.35-1  |
|  libcusolver-13-0-12.0.3.29-1  |
|  libcusolver-devel-13-0-12.0.3.29-1  |
|  libcusparse-13-0-12.6.2.49-1  |
|  libcusparse-devel-13-0-12.6.2.49-1  |
|  libnpp-13-0-13.0.0.50-1  |
|  libnpp-devel-13-0-13.0.0.50-1  |
|  libnvfatbin-13-0-13.0.39-1  |
|  libnvfatbin-devel-13-0-13.0.39-1  |
|  libnvidia-fbc-580.65.06-1.amzn2023  |
|  libnvidia-gpucomp-580.65.06-1.amzn2023  |
|  libnvidia-nscq-580.65.06-1  |
|  libnvjitlink-13-0-13.0.39-1  |
|  libnvjitlink-devel-13-0-13.0.39-1  |
|  libnvjpeg-13-0-13.0.0.40-1  |
|  libnvjpeg-devel-13-0-13.0.0.40-1  |
|  libnvptxcompiler-13-0-13.0.48-1  |
|  libnvsdm-580.65.06-1  |
|  libnvsdm-devel-580.65.06-1  |
|  libnvvm-13-0-13.0.48-1  |
|  mft-4.32.0.6004-1  |
|  mft-autocomplete-4.32.0.6004-1  |
|  mft-oem-4.32.0.6004-1  |
|  nsight-compute-2025.3.0-2025.3.0.19-1  |
|  nsight-systems-2025.3.2-2025.3.2.367\_253236224375v0-0  |
|  nvidia-fabricmanager-580.65.06-1  |
|  nvidia-fabricmanager-devel-580.65.06-1  |
|  nvidia-gds-13-0-13.0.0-1  |
|  nvlink5-580.65.06-1  |
|  nvlink5-580-580.65.06-1  |
|  xorg-x11-nvidia-580.65.06-1.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.8.20250915.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-13.0.0-1  |
|  cuda-drivers-580.65.06-1.amzn2023  |
|  cuda-toolkit-13.0.0-1  |
|  cuda-toolkit-config-common-13.0.48-1  |
|  kmod-nvidia-latest-dkms-580.65.06-1.amzn2023  |
|  kmod-nvidia-open-dkms-580.65.06-1.amzn2023  |
|  libnvidia-cfg-580.65.06-1.amzn2023  |
|  libnvidia-ml-580.65.06-1.amzn2023  |
|  nvidia-driver-580.65.06-1.amzn2023  |
|  nvidia-driver-assistant-0.22.65.06-1  |
|  nvidia-driver-cuda-580.65.06-1.amzn2023  |
|  nvidia-driver-cuda-libs-580.65.06-1.amzn2023  |
|  nvidia-driver-libs-580.65.06-1.amzn2023  |
|  nvidia-fs-2.26.6-1  |
|  nvidia-fs-dkms-2.26.6-1  |
|  nvidia-gds-13.0.0-1  |
|  nvidia-imex-580.65.06-1  |
|  nvidia-kmod-common-580.65.06-1.amzn2023  |
|  nvidia-libXNVCtrl-580.65.06-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-580.65.06-1.amzn2023  |
|  nvidia-modprobe-580.65.06-1.amzn2023  |
|  nvidia-open-580.65.06-1.amzn2023  |
|  nvidia-persistenced-580.65.06-1.amzn2023  |
|  nvidia-settings-580.65.06-1.amzn2023  |
|  nvidia-xconfig-580.65.06-1.amzn2023  |
|  nvlsm-2025.06.5-1  |

## Image Updates
<a name="ami-updates-2023.8.20250915"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250915.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250915-0.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.1  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.1  |
|  glibc-locale-source-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  kernel-libbpf-1:6.1.150-174.273.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250915-0.amzn2023  |
|  kernel-tools-1:6.1.150-174.273.amzn2023  |
|  kernel-1:6.1.150-174.273.amzn2023  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.3  |
|  system-release-2023.8.20250915-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250915.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250915-0.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.1  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-locale-source-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  kernel-libbpf-1:6.1.150-174.273.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250915-0.amzn2023  |
|  kernel-1:6.1.150-174.273.amzn2023  |
|  system-release-2023.8.20250915-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250915.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250915-0.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.1  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.1  |
|  glibc-locale-source-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250915-0.amzn2023  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.3  |
|  system-release-2023.8.20250915-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250915.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250915-0.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.1  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-locale-source-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.8.20250915-0.amzn2023  |
|  system-release-2023.8.20250915-0.amzn2023  |

### Default Container
<a name="amis-2023.8.20250915.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250915-0.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  system-release-2023.8.20250915-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250915.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250915-0.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.1  |
|  glibc-2.34-231.amzn2023.0.1  |
|  system-release-2023.8.20250915-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250915.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
