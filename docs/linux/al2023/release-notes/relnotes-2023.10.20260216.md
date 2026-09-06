---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260216.html
---

# Amazon Linux 2023 version 2023.10.20260216 release notes
<a name="relnotes-2023.10.20260216"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260216.

**Contents**
+ [Release Summary](#release-summary-2023.10.20260216)
+ [Repository Updates](#repository-updates-2023.10.20260216)
  + [Core New Packages](#amis-2023.10.20260216.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260216.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.10.20260216.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.10.20260216.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.10.20260216)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260216.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260216.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260216.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260216.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.10.20260216.Default-Container)
  + [Minimal Container](#amis-2023.10.20260216.Minimal-Container)
+ [Contact us](#amis-2023.10.20260216.contact-us)

## Release Summary
<a name="release-summary-2023.10.20260216"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260216"></a>

### Core New Packages
<a name="amis-2023.10.20260216.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  php8.1-pecl-memcached-3.4.0-1.amzn2023.0.1  |
|  php8.2-pecl-memcached-3.4.0-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.10.20260216.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  7zip-25.01-9.amzn2023.0.2  |
|  alsa-lib-1.2.7.2-1.amzn2023.0.3  |
|  amazon-cloudwatch-agent-1.300064.1-1.amzn2023  |
|  amazon-ssm-agent-3.3.3598.0-1.amzn2023  |
|  awscli-2-2.33.15-1.amzn2023.0.1  |
|  containerd-2.2.1-1.amzn2023.0.1  |
|  coreutils-8.32-30.amzn2023.0.5  |
|  credentials-fetcher-2.0.0-1.amzn2023.0.1  |
|  curl-8.17.0-1.amzn2023.0.1  |
|  docker-25.0.14-1.amzn2023.0.2  |
|  ecs-init-1.101.3-1.amzn2023  |
|  ecs-service-connect-agent-v1.34.12.0-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  firefox-140.7.0-1.amzn2023.0.3  |
|  fontforge-20201107-3.amzn2023.0.6  |
|  freerdp-3.6.3-1.amzn2023.0.3  |
|  gnupg2-2.3.7-1.amzn2023.0.7  |
|  golang-1.24.13-1.amzn2023.0.1  |
|  kernel6.12-6.12.68-92.122.amzn2023  |
|  libpng-1.6.37-10.amzn2023.0.10  |
|  libsoup-2.72.0-6.amzn2023.0.11  |
|  log4j-2.17.2-1.amzn2023.0.5  |
|  munge-0.5.14-7.amzn2023.0.5  |
|  nginx-1.28.2-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.3  |
|  nvidia-release-2023-4.amzn2023  |
|  openscap-1.3.13-1.amzn2023.0.1  |
|  openssh-8.7p1-8.amzn2023.0.16  |
|  openssl-3.2.2-1.amzn2023.0.5  |
|  protobuf-3.19.6-1.amzn2023.0.3  |
|  publicsuffix-list-20260116-1.amzn2023.0.1  |
|  python-awscrt-0.31.1-1.amzn2023.0.1  |
|  python3.12-3.12.12-2.amzn2023.0.4  |
|  python3.12-wheel-0.45.1-1.amzn2023.0.1  |
|  python3.13-3.13.12-1.amzn2023.0.1  |
|  python3.13-filelock-3.18.0-1.amzn2023.0.1  |
|  python3.13-virtualenv-20.21.1-1.amzn2023.0.2  |
|  runc-1.3.4-1.amzn2023.0.2  |
|  rust-1.93.0-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  vsftpd-3.0.5-1.amzn2023.0.3  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Nvidia New Packages
<a name="amis-2023.10.20260216.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  corelib-1.0.0.1770072670-1  |
|  cuquantum-26.01.0-1  |
|  cuquantum-cuda-12-26.01.0.4-1  |
|  cuquantum-cuda-13-26.01.0.4-1  |
|  cuquantum0-26.01.0-1  |
|  cutensor-2.5.0-1  |
|  cutensor-cuda-12-2.5.0.2-1  |
|  cutensor-cuda-13-2.5.0.2-1  |
|  cutensor2-2.5.0-1  |
|  libcorelib1-1.0.0.1770072670-1  |
|  libcorelib1-devel-1.0.0.1770072670-1  |
|  libcuobjclient-13-1-1.0.0.26-1  |
|  libcuobjclient-devel-13-1-1.0.0.26-1  |
|  libcuquantum0-cuda-12-26.01.0.4-1  |
|  libcuquantum0-cuda-13-26.01.0.4-1  |
|  libcuquantum0-devel-cuda-12-26.01.0.4-1  |
|  libcuquantum0-devel-cuda-13-26.01.0.4-1  |
|  libcuquantum0-static-cuda-12-26.01.0.4-1  |
|  libcuquantum0-static-cuda-13-26.01.0.4-1  |
|  libcutensor2-cuda-12-2.5.0.2-1  |
|  libcutensor2-cuda-13-2.5.0.2-1  |
|  libcutensor2-devel-cuda-12-2.5.0.2-1  |
|  libcutensor2-devel-cuda-13-2.5.0.2-1  |
|  libnvat-1.1.1.1770245582-1  |
|  libnvat-devel-1.1.1.1770245582-1  |
|  nsight-compute-2025.4.1-2025.4.1.2-1  |
|  nvattest-1.1.1.1770245582-1  |

### Nvidia Updated Packages
<a name="amis-2023.10.20260216.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-13.1.1-1  |
|  cuda-13-1-13.1.1-1  |
|  cuda-cccl-13-1-13.1.115-1  |
|  cuda-command-line-tools-13-1-13.1.1-1  |
|  cuda-compiler-13-1-13.1.1-1  |
|  cuda-crt-13-1-13.1.115-1  |
|  cuda-ctadvisor-13-1-13.1.115-1  |
|  cuda-culibos-devel-13-1-13.1.115-1  |
|  cuda-cuobjdump-13-1-13.1.115-1  |
|  cuda-cupti-13-1-13.1.115-1  |
|  cuda-cuxxfilt-13-1-13.1.115-1  |
|  cuda-documentation-13-1-13.1.115-1  |
|  cuda-gdb-13-1-13.1.115-1  |
|  cuda-gdb-src-13-1-13.1.115-1  |
|  cuda-libraries-13-1-13.1.1-1  |
|  cuda-libraries-devel-13-1-13.1.1-1  |
|  cuda-minimal-build-13-1-13.1.1-1  |
|  cuda-nsight-13-1-13.1.115-1  |
|  cuda-nsight-compute-13-1-13.1.1-1  |
|  cuda-nsight-systems-13-1-13.1.1-1  |
|  cuda-nvcc-13-1-13.1.115-1  |
|  cuda-nvdisasm-13-1-13.1.115-1  |
|  cuda-nvml-devel-13-1-13.1.115-1  |
|  cuda-nvprune-13-1-13.1.115-1  |
|  cuda-nvrtc-13-1-13.1.115-1  |
|  cuda-nvrtc-devel-13-1-13.1.115-1  |
|  cuda-nvtx-13-1-13.1.115-1  |
|  cuda-opencl-13-1-13.1.115-1  |
|  cuda-opencl-devel-13-1-13.1.115-1  |
|  cuda-profiler-api-13-1-13.1.115-1  |
|  cuda-runtime-13-1-13.1.1-1  |
|  cuda-sandbox-devel-13-1-13.1.115-1  |
|  cuda-sanitizer-13-1-13.1.118-1  |
|  cuda-toolkit-13.1.1-1  |
|  cuda-toolkit-13-13.1.1-1  |
|  cuda-toolkit-13-1-13.1.1-1  |
|  cuda-tools-13-1-13.1.1-1  |
|  cuda-visual-tools-13-1-13.1.1-1  |
|  datacenter-gpu-manager-4-core-4.5.2-1  |
|  datacenter-gpu-manager-4-cuda-all-4.5.2-1  |
|  datacenter-gpu-manager-4-cuda11-4.5.2-1  |
|  datacenter-gpu-manager-4-cuda12-4.5.2-1  |
|  datacenter-gpu-manager-4-cuda13-4.5.2-1  |
|  datacenter-gpu-manager-4-devel-4.5.2-1  |
|  datacenter-gpu-manager-4-multinode-4.5.2-1  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.5.2-1  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.5.2-1  |
|  datacenter-gpu-manager-4-proprietary-4.5.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.5.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.5.2-1  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.5.2-1  |
|  egl-wayland2-1.0.1\~20251124git3e5b643-7.amzn2023  |
|  gds-tools-13-1-1.16.1.26-1  |
|  libcublas-13-1-13.2.1.1-1  |
|  libcublas-devel-13-1-13.2.1.1-1  |
|  libcufft-13-1-12.1.0.78-1  |
|  libcufft-devel-13-1-12.1.0.78-1  |
|  libcufile-13-1-1.16.1.26-1  |
|  libcufile-devel-13-1-1.16.1.26-1  |
|  libcurand-13-1-10.4.1.81-1  |
|  libcurand-devel-13-1-10.4.1.81-1  |
|  libcusolver-13-1-12.0.9.81-1  |
|  libcusolver-devel-13-1-12.0.9.81-1  |
|  libcusparse-13-1-12.7.3.1-1  |
|  libcusparse-devel-13-1-12.7.3.1-1  |
|  libnpp-13-1-13.0.3.3-1  |
|  libnpp-devel-13-1-13.0.3.3-1  |
|  libnvfatbin-13-1-13.1.115-1  |
|  libnvfatbin-devel-13-1-13.1.115-1  |
|  libnvidia-container-devel-1.18.2-1  |
|  libnvidia-container-static-1.18.2-1  |
|  libnvidia-container-tools-1.18.2-1  |
|  libnvidia-container1-1.18.2-1  |
|  libnvjitlink-13-1-13.1.115-1  |
|  libnvjitlink-devel-13-1-13.1.115-1  |
|  libnvjpeg-13-1-13.0.3.75-1  |
|  libnvjpeg-devel-13-1-13.0.3.75-1  |
|  libnvptxcompiler-13-1-13.1.115-1  |
|  libnvvm-13-1-13.1.115-1  |
|  nvidia-container-toolkit-1.18.2-1  |
|  nvidia-container-toolkit-base-1.18.2-1  |
|  nvidia-gds-13.1.1-1  |
|  nvidia-gds-13-1-13.1.1-1  |

## Image Updates
<a name="ami-updates-2023.10.20260216"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260216.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260216-0.amzn2023  |
|  amazon-ssm-agent-3.3.3598.0-1.amzn2023  |
|  awscli-2-2.33.15-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.5  |
|  coreutils-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.10.20260216-0.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssh-clients-8.7p1-8.amzn2023.0.16  |
|  openssh-server-8.7p1-8.amzn2023.0.16  |
|  openssh-8.7p1-8.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  openssl-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  python3-awscrt-0.31.1-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.93.0-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260216.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260216-0.amzn2023  |
|  awscli-2-2.33.15-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.5  |
|  coreutils-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.10.20260216-0.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssh-clients-8.7p1-8.amzn2023.0.16  |
|  openssh-server-8.7p1-8.amzn2023.0.16  |
|  openssh-8.7p1-8.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  openssl-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  python3-awscrt-0.31.1-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260216.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260216-0.amzn2023  |
|  amazon-ssm-agent-3.3.3598.0-1.amzn2023  |
|  awscli-2-2.33.15-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.5  |
|  coreutils-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.10.20260216-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.68-92.122.amzn2023  |
|  kernel6.12-tools-1:6.12.68-92.122.amzn2023  |
|  kernel6.12-1:6.12.68-92.122.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssh-clients-8.7p1-8.amzn2023.0.16  |
|  openssh-server-8.7p1-8.amzn2023.0.16  |
|  openssh-8.7p1-8.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  openssl-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  python3-awscrt-0.31.1-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.93.0-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260216.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260216-0.amzn2023  |
|  awscli-2-2.33.15-1.amzn2023.0.1  |
|  coreutils-common-8.32-30.amzn2023.0.5  |
|  coreutils-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  kernel-livepatch-repo-s3-2023.10.20260216-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.68-92.122.amzn2023  |
|  kernel6.12-1:6.12.68-92.122.amzn2023  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssh-clients-8.7p1-8.amzn2023.0.16  |
|  openssh-server-8.7p1-8.amzn2023.0.16  |
|  openssh-8.7p1-8.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  openssl-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  python3-awscrt-0.31.1-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Default Container
<a name="amis-2023.10.20260216.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260216-0.amzn2023  |
|  coreutils-single-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  expat-2.6.3-1.amzn2023.0.4  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

### Minimal Container
<a name="amis-2023.10.20260216.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260216-0.amzn2023  |
|  coreutils-single-8.32-30.amzn2023.0.5  |
|  curl-minimal-8.17.0-1.amzn2023.0.1  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.7  |
|  libcurl-minimal-8.17.0-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.5  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.5  |
|  publicsuffix-list-dafsa-20260116-1.amzn2023.0.1  |
|  system-release-2023.10.20260216-0.amzn2023  |
|  zlib-1.2.11-33.amzn2023.0.6  |

## Contact us
<a name="amis-2023.10.20260216.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
