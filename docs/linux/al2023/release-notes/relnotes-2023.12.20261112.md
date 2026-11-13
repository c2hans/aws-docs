---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261112.html
---

# Amazon Linux 2023 version 2023.12.20261112 release notes
<a name="relnotes-2023.12.20261112"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261112.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261112)
+ [Repository Updates](#repository-updates-2023.12.20261112)
  + [Core Updated Packages](#amis-2023.12.20261112.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20261112.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20261112.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20261112.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20261112.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261112)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261112.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261112.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261112.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261112.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261112.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261112.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261112.Default-Container)
  + [Minimal Container](#amis-2023.12.20261112.Minimal-Container)
+ [Contact us](#amis-2023.12.20261112.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261112"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261112"></a>

### Core Updated Packages
<a name="amis-2023.12.20261112.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  alsa-lib-1.2.7.2-1.amzn2023.0.5  |
|  amazon-ssm-agent-3.3.5828.0-1.amzn2023  |
|  ant-1.10.12-5.amzn2023.0.6  |
|  bcel-6.13.0-1.amzn2023.0.1  |
|  buildah-1.43.1-1.amzn2023.0.4  |
|  c-ares-1.19.1-1.amzn2023.0.2  |
|  curl-8.21.0-5.amzn2023.0.5  |
|  ecs-service-connect-agent-v1.40.2.1-1.amzn2023  |
|  exiv2-0.28.5-133.amzn2023  |
|  firefox-153.6.0-1.amzn2023.0.1  |
|  fltk-1.3.6-1.amzn2023.0.3  |
|  freerdp-3.33.0-3.amzn2023  |
|  gdk-pixbuf2-2.42.12-186.amzn2023  |
|  git-2.50.1-1.amzn2023.0.2  |
|  gnome-shell-47.3-706.amzn2023  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.11  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.7  |
|  httpd-2.4.71-1.amzn2023.0.1  |
|  kernel-6.1.190-237.442.amzn2023  |
|  kernel6.12-6.12.115-140.210.amzn2023  |
|  kernel6.18-6.18.62-127.179.amzn2023  |
|  libheif-1.23.7-1.amzn2023  |
|  libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  nodejs22-22.23.5-1.amzn2023.0.1  |
|  nodejs24-24.22.3-1.amzn2023.0.1  |
|  ostree-2024.8-307.amzn2023  |
|  perl-CGI-5.02-1.amzn2023.0.1  |
|  perl-MIME-tools-5.522-1.amzn2023.0.1  |
|  postgresql-odbc-18.00.0006-1.amzn2023.0.1  |
|  python-pillow-9.4.0-2.amzn2023.0.13  |
|  python-pyasn1-0.4.8-4.amzn2023.0.6  |
|  qemu-11.0.0-5.amzn2023  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  rsyslog-8.2204.0-3.amzn2023.0.10  |
|  skopeo-1.22.2-1.amzn2023.0.4  |
|  speex-1.2.0-8.amzn2023.0.3  |
|  sqlite-3.40.0-1.amzn2023.0.9  |
|  squid-6.13-1.amzn2023.0.7  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  texlive-base-20210325-52.amzn2023.0.4  |
|  tomcat10-10.1.61-1.amzn2023.0.1  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.13  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.8  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20261112.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.189-236.400-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.190-237.431-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.113-138.209-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.114-139.210-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.56-125.164-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.56-126.188-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20261112.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.182-227.379-1.0-8.amzn2023  |
|  kernel-livepatch-6.1.186-228.374-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.186-228.376-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.188-233.385-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.188-233.386-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.188-233.393-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.189-236.399-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.103-127.188-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.103-129.197-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.110-135.201-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.110-135.202-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.111-136.204-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.44-99.149-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.48-107.148-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.48-109.150-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.51-120.162-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.51-120.163-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.54-121.166-1.0-2.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20261112.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  cccl-13-5-13.3.5.0.6-1  |
|  cuda-13-5-13.5.0-1  |
|  cuda-command-line-tools-13-5-13.5.0-1  |
|  cuda-compat-13-5-620.70.06-1.amzn2023  |
|  cuda-compiler-13-5-13.5.0-1  |
|  cuda-crt-13-5-13.5.37-1  |
|  cuda-ctadvisor-13-5-13.5.37-1  |
|  cuda-cudart-13-5-13.5.37-1  |
|  cuda-cudart-devel-13-5-13.5.37-1  |
|  cuda-culibos-devel-13-5-13.5.25-1  |
|  cuda-cuobjdump-13-5-13.5.37-1  |
|  cuda-cupti-13-5-13.5.25-1  |
|  cuda-cuxxfilt-13-5-13.5.37-1  |
|  cuda-driver-devel-13-5-13.5.37-1  |
|  cuda-gdb-13-5-13.5.25-1  |
|  cuda-gdb-src-13-5-13.5.25-1  |
|  cuda-libraries-13-5-13.5.0-1  |
|  cuda-libraries-devel-13-5-13.5.0-1  |
|  cuda-minimal-build-13-5-13.5.0-1  |
|  cuda-nsight-compute-13-5-13.5.0-1  |
|  cuda-nsight-systems-13-5-13.5.0-1  |
|  cuda-nvcc-13-5-13.5.37-1  |
|  cuda-nvdisasm-13-5-13.5.37-1  |
|  cuda-nvml-devel-13-5-13.5.37-1  |
|  cuda-nvprune-13-5-13.5.37-1  |
|  cuda-nvrtc-13-5-13.5.37-1  |
|  cuda-nvrtc-devel-13-5-13.5.37-1  |
|  cuda-nvtx-13-5-13.5.25-1  |
|  cuda-opencl-13-5-13.5.25-1  |
|  cuda-opencl-devel-13-5-13.5.25-1  |
|  cuda-profiler-api-13-5-13.5.25-1  |
|  cuda-runtime-13-5-13.5.0-1  |
|  cuda-sandbox-devel-13-5-13.5.25-1  |
|  cuda-sanitizer-13-5-13.5.25-1  |
|  cuda-tileiras-13-5-13.5.37-1  |
|  cuda-toolkit-13-5-13.5.0-1  |
|  cuda-toolkit-13-5-config-common-13.5.37-1  |
|  cuda-tools-13-5-13.5.0-1  |
|  cuda-visual-tools-13-5-13.5.0-1  |
|  cudnn9-cuda-13-5-9.28.1.4-1  |
|  cudnn9-jit-cuda-13-5-9.28.1.4-1  |
|  gds-tools-13-5-1.20.0.107-1  |
|  libcublas-13-5-13.10.0.20-1  |
|  libcublas-devel-13-5-13.10.0.20-1  |
|  libcufft-13-5-12.5.0.14-1  |
|  libcufft-devel-13-5-12.5.0.14-1  |
|  libcufile-13-5-1.20.0.107-1  |
|  libcufile-devel-13-5-1.20.0.107-1  |
|  libcuobjclient-13-5-1.4.0.107-1  |
|  libcuobjclient-devel-13-5-1.4.0.107-1  |
|  libcurand-13-5-10.4.5.25-1  |
|  libcurand-devel-13-5-10.4.5.25-1  |
|  libcusolver-13-5-12.4.1.2-1  |
|  libcusolver-devel-13-5-12.4.1.2-1  |
|  libcusparse-13-5-12.9.4.2-1  |
|  libcusparse-devel-13-5-12.9.4.2-1  |
|  libnpp-13-5-13.2.0.93-1  |
|  libnpp-devel-13-5-13.2.0.93-1  |
|  libnvfatbin-13-5-13.5.37-1  |
|  libnvfatbin-devel-13-5-13.5.37-1  |
|  libnvidia-fmdrv-620.70.06-1.amzn2023  |
|  libnvidia-imex-620.70.06-1.amzn2023  |
|  libnvimgcodec0-cuda-12-0.10.0.9-1  |
|  libnvimgcodec0-cuda-13-0.10.0.9-1  |
|  libnvimgcodec0-devel-cuda-12-0.10.0.9-1  |
|  libnvimgcodec0-devel-cuda-13-0.10.0.9-1  |
|  libnvimgcodec0-static-cuda-12-0.10.0.9-1  |
|  libnvimgcodec0-static-cuda-13-0.10.0.9-1  |
|  libnvjitlink-13-5-13.5.37-1  |
|  libnvjitlink-devel-13-5-13.5.37-1  |
|  libnvjpeg-13-5-13.3.2.43-1  |
|  libnvjpeg-devel-13-5-13.3.2.43-1  |
|  libnvptxcompiler-13-5-13.5.37-1  |
|  libnvptxcompiler-devel-13-5-13.5.37-1  |
|  libnvvm-13-5-13.5.37-1  |
|  nsight-compute-2026.4.0-2026.4.0.10-1  |
|  nsight-systems-2026.5.2-2026.5.2.323\_265239015215v0-0  |
|  nvidia-driver-common-620.70.06-1.amzn2023  |
|  nvidia-fabricmanager-direct-2.0.0.rel106-1  |
|  nvidia-fabricmanager-direct-devel-2.0.0.rel106-1  |
|  nvidia-gds-13-5-13.5.0-1  |
|  nvidia-imex-direct-2.0.0.rel49-1  |
|  nvimgcodec-0.10.0-1  |
|  nvimgcodec-cuda-12-0.10.0.9-1  |
|  nvimgcodec-cuda-13-0.10.0.9-1  |
|  nvimgcodec0-0.10.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20261112.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cuda-13.5.0-1  |
|  cuda-toolkit-13.5.0-1  |
|  cuda-toolkit-13-13.5.0-1  |
|  cuda-toolkit-13-config-common-13.5.37-1  |
|  cuda-toolkit-config-common-13.5.37-1  |
|  cudnn-9.28.1-1  |
|  cudnn-jit-9.28.1-1  |
|  cudnn9-9.28.1-1  |
|  cudnn9-cuda-12-9.28.1.4-1  |
|  cudnn9-cuda-12-9-9.28.1.4-1  |
|  cudnn9-cuda-13-9.28.1.4-1  |
|  cudnn9-jit-9.28.1-1  |
|  cudnn9-jit-cuda-12-9.28.1.4-1  |
|  cudnn9-jit-cuda-12-9-9.28.1.4-1  |
|  cudnn9-jit-cuda-13-9.28.1.4-1  |
|  cuquantum-26.11.0-1  |
|  cuquantum-cuda-12-26.11.0.4-1  |
|  cuquantum-cuda-13-26.11.0.4-1  |
|  cuquantum0-26.11.0-1  |
|  kmod-nvidia-open-dkms-620.70.06-1.amzn2023  |
|  libcudnn9-cuda-12-9.28.1.4-1  |
|  libcudnn9-cuda-13-9.28.1.4-1  |
|  libcudnn9-devel-cuda-12-9.28.1.4-1  |
|  libcudnn9-devel-cuda-13-9.28.1.4-1  |
|  libcudnn9-headers-cuda-12-9.28.1.4-1  |
|  libcudnn9-headers-cuda-13-9.28.1.4-1  |
|  libcudnn9-jit-cuda-12-9.28.1.4-1  |
|  libcudnn9-jit-cuda-13-9.28.1.4-1  |
|  libcudnn9-jit-devel-cuda-12-9.28.1.4-1  |
|  libcudnn9-jit-devel-cuda-13-9.28.1.4-1  |
|  libcudnn9-samples-9.28.1.4-1  |
|  libcudnn9-static-cuda-12-9.28.1.4-1  |
|  libcudnn9-static-cuda-13-9.28.1.4-1  |
|  libcuquantum0-cuda-12-26.11.0.4-1  |
|  libcuquantum0-cuda-13-26.11.0.4-1  |
|  libcuquantum0-devel-cuda-12-26.11.0.4-1  |
|  libcuquantum0-devel-cuda-13-26.11.0.4-1  |
|  libcuquantum0-static-cuda-12-26.11.0.4-1  |
|  libcuquantum0-static-cuda-13-26.11.0.4-1  |
|  libnccl-2.32.6-1\+cuda13.5  |
|  libnccl-devel-2.32.6-1\+cuda13.5  |
|  libnccl-static-2.32.6-1\+cuda13.5  |
|  libnvidia-fbc-620.70.06-1.amzn2023  |
|  libnvidia-nscq-620.70.06-1.amzn2023  |
|  libnvsdm-620.70.06-1.amzn2023  |
|  libnvsdm-devel-620.70.06-1.amzn2023  |
|  nvidia-driver-620.70.06-1.amzn2023  |
|  nvidia-driver-assistant-0.68.70.06-1  |
|  nvidia-driver-cuda-620.70.06-1.amzn2023  |
|  nvidia-driver-cuda-libs-620.70.06-1.amzn2023  |
|  nvidia-driver-libs-620.70.06-1.amzn2023  |
|  nvidia-gds-13.5.0-1  |
|  nvidia-kmod-common-620.70.06-1.amzn2023  |
|  nvidia-libXNVCtrl-620.70.06-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-620.70.06-1.amzn2023  |
|  nvidia-modprobe-620.70.06-1.amzn2023  |
|  nvidia-open-620.70.06-1.amzn2023  |
|  nvidia-persistenced-620.70.06-1.amzn2023  |
|  nvidia-settings-620.70.06-1.amzn2023  |
|  nvidia-xconfig-620.70.06-1.amzn2023  |
|  xorg-x11-nvidia-620.70.06-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20261112"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261112.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  amazon-ssm-agent-3.3.5828.0-1.amzn2023  |
|  c-ares-1.19.1-1.amzn2023.0.2  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel6.18-tools-1:6.18.62-127.179.amzn2023  |
|  kernel6.18-1:6.18.62-127.179.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261112.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel6.18-1:6.18.62-127.179.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261112.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  amazon-ssm-agent-3.3.5828.0-1.amzn2023  |
|  c-ares-1.19.1-1.amzn2023.0.2  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel6.12-tools-1:6.12.115-140.210.amzn2023  |
|  kernel6.12-1:6.12.115-140.210.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261112.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel6.12-1:6.12.115-140.210.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261112.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  amazon-ssm-agent-3.3.5828.0-1.amzn2023  |
|  c-ares-1.19.1-1.amzn2023.0.2  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel-tools-1:6.1.190-237.442.amzn2023  |
|  kernel-1:6.1.190-237.442.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-libstoragemgmt-1.9.4-5.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261112.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261112-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20261112-0.amzn2023  |
|  kernel-1:6.1.190-237.442.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.10  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023.0.3  |

### Default Container
<a name="amis-2023.12.20261112.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261112-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.10  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20261112.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261112-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.5  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.10  |
|  rpm-4.16.1.3-29.amzn2023.0.10  |
|  sqlite-libs-3.40.0-1.amzn2023.0.9  |
|  system-release-2023.12.20261112-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261112.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
