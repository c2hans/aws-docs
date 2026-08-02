---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260706.html
---

# Amazon Linux 2023 version 2023.12.20260706 release notes
<a name="relnotes-2023.12.20260706"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260706.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260706)
+ [Repository Updates](#repository-updates-2023.12.20260706)
  + [Core New Packages](#amis-2023.12.20260706.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260706.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260706.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260706.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260706)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260706.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260706.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260706.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260706.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260706.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260706.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260706.Default-Container)
  + [Minimal Container](#amis-2023.12.20260706.Minimal-Container)
+ [Contact us](#amis-2023.12.20260706.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260706"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260706"></a>

### Core New Packages
<a name="amis-2023.12.20260706.Core-New-Packages"></a>

This section provides details about Core New Packages.

|  |
| --- |
|  python-supportinfo-1.0.0-1.amzn2023  |

### Core Updated Packages
<a name="amis-2023.12.20260706.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

|  |
| --- |
|  ImageMagick-6.9.13.50-1.amzn2023.0.2  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  amazon-rpm-config-228-11.amzn2023.0.1  |
|  ansible-8.3.0-1.amzn2023.0.3  |
|  aws-nitro-tpm-tools-1.1.2-1.amzn2023  |
|  cifs-utils-7.5-1.amzn2023.0.4  |
|  cloud-utils-0.31-8.amzn2023.0.4  |
|  composer-2.10.1-1.amzn2023.0.1  |
|  containerd-2.2.5-1.amzn2023.0.1  |
|  docker-25.0.16-1.amzn2023.0.3  |
|  ecs-init-1.105.0-1.amzn2023  |
|  ecs-service-connect-agent-v1.34.13.3-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  firefox-140.12.0-1.amzn2023.0.1  |
|  gnupg2-2.3.7-1.amzn2023.0.9  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.6  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.7  |
|  haproxy-3.0.23-2.amzn2023.0.1  |
|  kernel-6.1.176-220.358.amzn2023  |
|  kernel6.12-6.12.94-123.174.amzn2023  |
|  kernel6.18-6.18.36-69.134.amzn2023  |
|  libde265-1.0.18-1.amzn2023.0.2  |
|  libheif-1.19.8-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  lustre-client-2.15.6-32.amzn2023  |
|  mock-core-configs-39.2-1.amzn2023.0.1  |
|  nautilus-47.1-719.amzn2023  |
|  nerdctl-2.2.2-1.amzn2023.0.4  |
|  nginx-1.30.3-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.8  |
|  nginx-mod-njs-0.9.9-1.amzn2023.0.2  |
|  nodejs22-22.23.1-1.amzn2023.0.1  |
|  nodejs24-24.18.0-1.amzn2023.0.1  |
|  opensc-0.24.0-1.amzn2023.0.5  |
|  python3.11-3.11.15-1.amzn2023.0.3  |
|  python3.12-3.12.13-2.amzn2023.0.3  |
|  python3.13-3.13.14-1.amzn2023.0.1  |
|  python3.14-3.14.6-1.amzn2023.0.1  |
|  python3.9-3.9.25-1.amzn2023.0.7  |
|  rclone-1.74.3-82.amzn2023  |
|  samba-4.17.12-1.amzn2023.0.5  |
|  sqlite-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-2.37.4-1.amzn2023.0.5  |
|  wireshark-4.6.6-1.amzn2023.0.1  |

### Nvidia New Packages
<a name="amis-2023.12.20260706.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

|  |
| --- |
|  nsight-compute-2026.2.1-2026.2.1.5-1  |
|  nvidia-driver-selinux-0.1-2.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260706.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

|  |
| --- |
|  cccl-13-3-13.3.3.4.1-1  |
|  cuda-13.3.1-1  |
|  cuda-13-3-13.3.1-1  |
|  cuda-command-line-tools-13-3-13.3.1-1  |
|  cuda-compat-13-0-580.173.02-1.amzn2023  |
|  cuda-compiler-13-3-13.3.1-1  |
|  cuda-crt-13-3-13.3.73-1  |
|  cuda-cuobjdump-13-3-13.3.73-1  |
|  cuda-cupti-13-3-13.3.75-1  |
|  cuda-documentation-13-3-13.3.73-1  |
|  cuda-gdb-13-3-13.3.73-1  |
|  cuda-gdb-src-13-3-13.3.73-1  |
|  cuda-libraries-13-3-13.3.1-1  |
|  cuda-libraries-devel-13-3-13.3.1-1  |
|  cuda-minimal-build-13-3-13.3.1-1  |
|  cuda-nsight-compute-13-3-13.3.1-1  |
|  cuda-nsight-systems-13-3-13.3.1-1  |
|  cuda-nvcc-13-3-13.3.73-1  |
|  cuda-nvdisasm-13-3-13.3.73-1  |
|  cuda-runtime-13-3-13.3.1-1  |
|  cuda-sanitizer-13-3-13.3.75-1  |
|  cuda-toolkit-13.3.1-1  |
|  cuda-toolkit-13-13.3.1-1  |
|  cuda-toolkit-13-3-13.3.1-1  |
|  cuda-tools-13-3-13.3.1-1  |
|  cuda-visual-tools-13-3-13.3.1-1  |
|  cuquantum-26.06.0-1  |
|  cuquantum-cuda-12-26.06.0.17-1  |
|  cuquantum-cuda-13-26.06.0.17-1  |
|  cuquantum0-26.06.0-1  |
|  datacenter-gpu-manager-4-core-4.6.0-1  |
|  datacenter-gpu-manager-4-cuda-all-4.6.0-1  |
|  datacenter-gpu-manager-4-cuda11-4.6.0-1  |
|  datacenter-gpu-manager-4-cuda12-4.6.0-1  |
|  datacenter-gpu-manager-4-cuda13-4.6.0-1  |
|  datacenter-gpu-manager-4-devel-4.6.0-1  |
|  datacenter-gpu-manager-4-multinode-4.6.0-1  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.6.0-1  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.6.0-1  |
|  datacenter-gpu-manager-4-proprietary-4.6.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.6.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.6.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.6.0-1  |
|  gds-tools-13-3-1.18.1.6-1  |
|  libcublas-13-3-13.6.0.2-1  |
|  libcublas-devel-13-3-13.6.0.2-1  |
|  libcufile-13-3-1.18.1.6-1  |
|  libcufile-devel-13-3-1.18.1.6-1  |
|  libcuobjclient-13-3-1.2.0.68-1  |
|  libcuobjclient-devel-13-3-1.2.0.68-1  |
|  libcuquantum0-cuda-12-26.06.0.17-1  |
|  libcuquantum0-cuda-13-26.06.0.17-1  |
|  libcuquantum0-devel-cuda-12-26.06.0.17-1  |
|  libcuquantum0-devel-cuda-13-26.06.0.17-1  |
|  libcuquantum0-static-cuda-12-26.06.0.17-1  |
|  libcuquantum0-static-cuda-13-26.06.0.17-1  |
|  libcusolver-13-3-12.2.6.9-1  |
|  libcusolver-devel-13-3-12.2.6.9-1  |
|  libcusparse-13-3-12.8.2.51-1  |
|  libcusparse-devel-13-3-12.8.2.51-1  |
|  libnpp-13-3-13.1.2.81-1  |
|  libnpp-devel-13-3-13.1.2.81-1  |
|  libnvjpeg-13-3-13.2.1.68-1  |
|  libnvjpeg-devel-13-3-13.2.1.68-1  |
|  libnvptxcompiler-13-3-13.3.73-1  |
|  libnvvm-13-3-13.3.73-1  |
|  nsight-systems-2026.1.3-2026.1.3.425\_261338342291v0-0  |
|  nvidia-driver-assistant-0.53.44-1  |
|  nvidia-gds-13.3.1-1  |
|  nvidia-gds-13-3-13.3.1-1  |
|  nvlink5-580-580.173.02-1  |

## Image Updates
<a name="ami-updates-2023.12.20260706"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260706.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  amazon-rpm-config-228-11.amzn2023.0.1  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel6.18-tools-1:6.18.36-69.136.amzn2023  |
|  kernel6.18-1:6.18.36-69.136.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260706.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel6.18-1:6.18.36-69.136.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260706.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  amazon-rpm-config-228-11.amzn2023.0.1  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel6.12-tools-1:6.12.94-123.176.amzn2023  |
|  kernel6.12-1:6.12.94-123.176.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260706.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel6.12-1:6.12.94-123.176.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260706.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  amazon-rpm-config-228-11.amzn2023.0.1  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel-tools-1:6.1.176-220.360.amzn2023  |
|  kernel-1:6.1.176-220.360.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260706.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260706-1.amzn2023  |
|  amazon-linux-sb-keys-2023.1-1.amzn2023.0.6  |
|  cloud-utils-growpart-0.31-8.amzn2023.0.4  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20260706-1.amzn2023  |
|  kernel-1:6.1.176-220.360.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libfdisk-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.5  |
|  util-linux-2.37.4-1.amzn2023.0.5  |

### Default Container
<a name="amis-2023.12.20260706.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260706-1.amzn2023  |
|  expat-2.6.3-1.amzn2023.0.6  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  python3-libs-3.9.25-1.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.7  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260706.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260706-1.amzn2023  |
|  gnupg2-minimal-2.3.7-1.amzn2023.0.9  |
|  libblkid-2.37.4-1.amzn2023.0.5  |
|  libmount-2.37.4-1.amzn2023.0.5  |
|  libsmartcols-2.37.4-1.amzn2023.0.5  |
|  libuuid-2.37.4-1.amzn2023.0.5  |
|  libxml2-2.10.4-1.amzn2023.0.19  |
|  sqlite-libs-3.40.0-1.amzn2023.0.8  |
|  system-release-2023.12.20260706-1.amzn2023  |

## Contact us
<a name="amis-2023.12.20260706.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
