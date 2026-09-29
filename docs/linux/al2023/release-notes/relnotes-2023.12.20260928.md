---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260928.html
---

# Amazon Linux 2023 version 2023.12.20260928 release notes
<a name="relnotes-2023.12.20260928"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260928.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260928)
+ [Repository Updates](#repository-updates-2023.12.20260928)
  + [Core Updated Packages](#amis-2023.12.20260928.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260928.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260928.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260928)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260928.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260928.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260928.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260928.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260928.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260928.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260928.Default-Container)
  + [Minimal Container](#amis-2023.12.20260928.Minimal-Container)
+ [Contact us](#amis-2023.12.20260928.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260928"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ Starting with kernel version `kernel6.18-6.18.51-120.162.amzn2023`, Amazon Linux ships kernel modules in `zstd`-compressed format with a `.ko.zst` file extension, instead of the previous uncompressed `.ko` format. The kernel decompresses modules at load time. Validate workloads that use kernel modules against the affected kernel. If needed, switch to tooling that doesn't depend on the module's compression format, such as `modprobe`. This is included in the `kmod-29-2.amzn2023.0.6` release.
+ This release updates `rsync` to version `3.5.1` with security and compatibility fixes, including stricter validation of symlink ownership, daemon access controls, and TLS hostnames. Protocol 33 remains interoperable with protocol 32; some privileged jobs that traverse symlinks owned by another user may now fail, and fixed-format `--stats` parsers should allow the additional logical-block field.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260928"></a>

### Core Updated Packages
<a name="amis-2023.12.20260928.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  ImageMagick-6.9.13.54-1.amzn2023  |
|  amazon-cloudwatch-agent-1.300071.0-1.amzn2023  |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-efs-utils-3.3.2-1.amzn2023  |
|  amazon-ssm-agent-3.3.5226.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-41.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  bind-9.18.50-1.amzn2023.0.3  |
|  bluez-5.62-2.amzn2023.0.7  |
|  brotli-1.1.0-1.amzn2023.0.1  |
|  bubblewrap-0.12.0-1.amzn2023.0.1  |
|  cjose-0.6.2.2-7.amzn2023  |
|  corosync-3.1.9-3.amzn2023.0.3  |
|  crash-8.0.5-5.amzn2023.0.2  |
|  curl-8.21.0-5.amzn2023.0.2  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dotnet10.0-10.0.112-1.amzn2023.0.2  |
|  dotnet8.0-8.0.131-1.amzn2023.0.2  |
|  dotnet9.0-9.0.121-1.amzn2023.0.3  |
|  dovecot-2.3.20-1.amzn2023.0.4  |
|  ecs-init-1.107.0-1.amzn2023  |
|  environment-modules-4.8.0-1.amzn2023.0.3  |
|  firefox-140.16.0-1.amzn2023.0.1  |
|  freeipmi-1.6.19-1.amzn2023  |
|  gdb-16.3-1.amzn2023.0.2  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.5  |
|  gvfs-1.56.1-1.amzn2023.0.3  |
|  kernel-6.1.188-233.385.amzn2023  |
|  kernel6.12-6.12.110-135.201.amzn2023  |
|  kernel6.18-6.18.51-120.162.amzn2023  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-1.21.3-8.amzn2023.0.2  |
|  libheif-1.23.4-1.amzn2023  |
|  libpcap-1.10.7-1.amzn2023.0.1  |
|  libsoup3-3.7.2-1.amzn2023  |
|  libssh-0.10.6-1.amzn2023.0.9  |
|  libvirt-12.0.0-3.amzn2023.0.3  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  network-flow-monitor-agent-1.1.8-1.amzn2023.0.1  |
|  nginx-1.30.5-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.10  |
|  nginx-mod-njs-1.0.1-1.amzn2023.0.2  |
|  nodejs22-22.23.2-1.amzn2023.0.3  |
|  nodejs24-24.21.0-1.amzn2023.0.1  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  perl-Authen-SASL-2.16-23.amzn2023.0.4  |
|  perl-Net-DNS-1.57-1.amzn2023.0.1  |
|  python-awscrt-0.36.4-1.amzn2023.0.2  |
|  python-pymongo-3.10.1-5.amzn2023.0.4  |
|  python-tornado-6.1.0-2.amzn2023.0.10  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.5  |
|  qemu-11.0.0-3.amzn2023  |
|  rclone-1.75.1-1.amzn2023  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  rsync-3.5.1-1.amzn2023.0.1  |
|  rsyslog-8.2204.0-3.amzn2023.0.7  |
|  runfinch-finch-1.19.0-1.amzn2023.0.1  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  squid-6.13-1.amzn2023.0.6  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.15  |

### Nvidia New Packages
<a name="amis-2023.12.20260928.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  cccl-13-4-13.3.4.3.1-1  |
|  cuda-13-4-13.4.2-1  |
|  cuda-command-line-tools-13-4-13.4.2-1  |
|  cuda-compat-13-4-615.71.09-1.amzn2023  |
|  cuda-compiler-13-4-13.4.2-1  |
|  cuda-crt-13-4-13.4.92-1  |
|  cuda-ctadvisor-13-4-13.4.92-1  |
|  cuda-cudart-13-4-13.4.92-1  |
|  cuda-cudart-devel-13-4-13.4.92-1  |
|  cuda-culibos-devel-13-4-13.4.92-1  |
|  cuda-cuobjdump-13-4-13.4.92-1  |
|  cuda-cupti-13-4-13.4.92-1  |
|  cuda-cuxxfilt-13-4-13.4.92-1  |
|  cuda-documentation-13-4-13.4.92-1  |
|  cuda-driver-devel-13-4-13.4.92-1  |
|  cuda-gdb-13-4-13.4.92-1  |
|  cuda-gdb-src-13-4-13.4.92-1  |
|  cuda-libraries-13-4-13.4.2-1  |
|  cuda-libraries-devel-13-4-13.4.2-1  |
|  cuda-minimal-build-13-4-13.4.2-1  |
|  cuda-nsight-compute-13-4-13.4.2-1  |
|  cuda-nsight-systems-13-4-13.4.2-1  |
|  cuda-nvcc-13-4-13.4.92-1  |
|  cuda-nvdisasm-13-4-13.4.92-1  |
|  cuda-nvml-devel-13-4-13.4.92-1  |
|  cuda-nvprune-13-4-13.4.92-1  |
|  cuda-nvrtc-13-4-13.4.92-1  |
|  cuda-nvrtc-devel-13-4-13.4.92-1  |
|  cuda-nvtx-13-4-13.4.92-1  |
|  cuda-opencl-13-4-13.4.92-1  |
|  cuda-opencl-devel-13-4-13.4.92-1  |
|  cuda-profiler-api-13-4-13.4.92-1  |
|  cuda-runtime-13-4-13.4.2-1  |
|  cuda-sandbox-devel-13-4-13.4.92-1  |
|  cuda-sanitizer-13-4-13.4.92-1  |
|  cuda-tileiras-13-4-13.4.92-1  |
|  cuda-toolkit-13-4-13.4.2-1  |
|  cuda-toolkit-13-4-config-common-13.4.92-1  |
|  cuda-tools-13-4-13.4.2-1  |
|  cuda-visual-tools-13-4-13.4.2-1  |
|  datacenter-gpu-manager-4-cuda11-cublas-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-cublas-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-curand-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-cusparselt-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-nccl-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-ubergemm2-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-cublas-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-curand-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-cusparselt-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-nccl-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-ubergemm2-4.7.0-1  |
|  datacenter-gpu-manager-4-dcgmproftesterkernels-4.7.0-1  |
|  datacenter-gpu-manager-4-module-config-4.7.0-1  |
|  datacenter-gpu-manager-4-module-diag-4.7.0-1  |
|  datacenter-gpu-manager-4-module-health-4.7.0-1  |
|  datacenter-gpu-manager-4-module-introspect-4.7.0-1  |
|  datacenter-gpu-manager-4-module-nvswitch-4.7.0-1  |
|  datacenter-gpu-manager-4-module-policy-4.7.0-1  |
|  datacenter-gpu-manager-4-module-sysmon-4.7.0-1  |
|  datacenter-gpu-manager-4-python3-4.7.0-1  |
|  dcgmi-4.7.0-1  |
|  gds-tools-13-4-1.19.1.55-1  |
|  libcublas-13-4-13.8.0.4-1  |
|  libcublas-devel-13-4-13.8.0.4-1  |
|  libcufft-13-4-12.4.0.43-1  |
|  libcufft-devel-13-4-12.4.0.43-1  |
|  libcufile-13-4-1.19.1.55-1  |
|  libcufile-devel-13-4-1.19.1.55-1  |
|  libcuobjclient-13-4-1.3.1.55-1  |
|  libcuobjclient-devel-13-4-1.3.1.55-1  |
|  libcurand-13-4-10.4.4.72-1  |
|  libcurand-devel-13-4-10.4.4.72-1  |
|  libcusolver-13-4-12.3.4.7-1  |
|  libcusolver-devel-13-4-12.3.4.7-1  |
|  libcusparse-13-4-12.8.6.72-1  |
|  libcusparse-devel-13-4-12.8.6.72-1  |
|  libdcgm-4.7.0-1  |
|  libnccl-2.32.3-1\+cuda13.4  |
|  libnccl-devel-2.32.3-1\+cuda13.4  |
|  libnccl-static-2.32.3-1\+cuda13.4  |
|  libnpp-13-4-13.2.0.58-1  |
|  libnpp-devel-13-4-13.2.0.58-1  |
|  libnvfatbin-13-4-13.4.92-1  |
|  libnvfatbin-devel-13-4-13.4.92-1  |
|  libnvjitlink-13-4-13.4.92-1  |
|  libnvjitlink-devel-13-4-13.4.92-1  |
|  libnvjpeg-13-4-13.2.3.58-1  |
|  libnvjpeg-devel-13-4-13.2.3.58-1  |
|  libnvptxcompiler-13-4-13.4.92-1  |
|  libnvvm-13-4-13.4.92-1  |
|  nsight-compute-2026.3.0-2026.3.0.13-1  |
|  nsight-compute-2026.3.1-2026.3.1.2-1  |
|  nsight-systems-2026.3.2-2026.3.2.476\_263238834031v0-0  |
|  nv-hostengine-4.7.0-1  |
|  nvidia-gds-13-4-13.4.2-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260928.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cublas-13.6.2-1  |
|  cublas-cuda-13-13.6.2.16-1  |
|  cublas13-13.6.2-1  |
|  cuda-13.4.2-1  |
|  cuda-toolkit-13.4.2-1  |
|  cuda-toolkit-13-13.4.2-1  |
|  cuda-toolkit-13-config-common-13.4.92-1  |
|  cuda-toolkit-config-common-13.4.92-1  |
|  cudnn-9.26.0-1  |
|  cudnn-jit-9.26.0-1  |
|  cudnn9-9.26.0-1  |
|  cudnn9-cuda-12-9.26.0.51-1  |
|  cudnn9-cuda-12-9-9.26.0.51-1  |
|  cudnn9-cuda-13-9.26.0.51-1  |
|  cudnn9-cuda-13-4-9.26.0.51-1  |
|  cudnn9-jit-9.26.0-1  |
|  cudnn9-jit-cuda-12-9.26.0.51-1  |
|  cudnn9-jit-cuda-12-9-9.26.0.51-1  |
|  cudnn9-jit-cuda-13-9.26.0.51-1  |
|  cudnn9-jit-cuda-13-4-9.26.0.51-1  |
|  cuquantum-26.09.0-1  |
|  cuquantum-cuda-12-26.09.0.8-1  |
|  cuquantum-cuda-13-26.09.0.8-1  |
|  cuquantum0-26.09.0-1  |
|  cutensor-2.8.1-1  |
|  cutensor-cuda-12-2.8.1.0-1  |
|  cutensor-cuda-13-2.8.1.0-1  |
|  cutensor2-2.8.1-1  |
|  datacenter-gpu-manager-4-core-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda-all-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda11-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda12-4.7.0-1  |
|  datacenter-gpu-manager-4-cuda13-4.7.0-1  |
|  datacenter-gpu-manager-4-devel-4.7.0-1  |
|  datacenter-gpu-manager-4-multinode-4.7.0-1  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.7.0-1  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.7.0-1  |
|  datacenter-gpu-manager-4-proprietary-4.7.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.7.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.7.0-1  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.7.0-1  |
|  egl-gbm-1.1.4-1.amzn2023  |
|  egl-wayland2-1.0.2-1.amzn2023  |
|  egl-x11-1.0.6-1.amzn2023  |
|  libcublas13-cuda-13-13.6.2.16-1  |
|  libcublas13-devel-cuda-13-13.6.2.16-1  |
|  libcudnn9-cuda-12-9.26.0.51-1  |
|  libcudnn9-cuda-13-9.26.0.51-1  |
|  libcudnn9-devel-cuda-12-9.26.0.51-1  |
|  libcudnn9-devel-cuda-13-9.26.0.51-1  |
|  libcudnn9-headers-cuda-12-9.26.0.51-1  |
|  libcudnn9-headers-cuda-13-9.26.0.51-1  |
|  libcudnn9-jit-cuda-12-9.26.0.51-1  |
|  libcudnn9-jit-cuda-13-9.26.0.51-1  |
|  libcudnn9-jit-devel-cuda-12-9.26.0.51-1  |
|  libcudnn9-jit-devel-cuda-13-9.26.0.51-1  |
|  libcudnn9-samples-9.26.0.51-1  |
|  libcudnn9-static-cuda-12-9.26.0.51-1  |
|  libcudnn9-static-cuda-13-9.26.0.51-1  |
|  libcuquantum0-cuda-12-26.09.0.8-1  |
|  libcuquantum0-cuda-13-26.09.0.8-1  |
|  libcuquantum0-devel-cuda-12-26.09.0.8-1  |
|  libcuquantum0-devel-cuda-13-26.09.0.8-1  |
|  libcuquantum0-static-cuda-12-26.09.0.8-1  |
|  libcuquantum0-static-cuda-13-26.09.0.8-1  |
|  libcutensor2-cuda-12-2.8.1.0-1  |
|  libcutensor2-cuda-13-2.8.1.0-1  |
|  libcutensor2-devel-cuda-12-2.8.1.0-1  |
|  libcutensor2-devel-cuda-13-2.8.1.0-1  |
|  nvidia-gds-13.4.2-1  |

## Image Updates
<a name="ami-updates-2023.12.20260928"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260928.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  amazon-ssm-agent-3.3.5226.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-41.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.3  |
|  bind-license-32:9.18.50-1.amzn2023.0.3  |
|  bind-utils-32:9.18.50-1.amzn2023.0.3  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-utils-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel6.18-tools-1:6.18.51-120.162.amzn2023  |
|  kernel6.18-1:6.18.51-120.162.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libpcap-14:1.10.7-1.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  rsync-3.5.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260928.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel6.18-1:6.18.51-120.162.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260928.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  amazon-ssm-agent-3.3.5226.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-41.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.3  |
|  bind-license-32:9.18.50-1.amzn2023.0.3  |
|  bind-utils-32:9.18.50-1.amzn2023.0.3  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-utils-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel6.12-tools-1:6.12.110-135.201.amzn2023  |
|  kernel6.12-1:6.12.110-135.201.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libpcap-14:1.10.7-1.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  rsync-3.5.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260928.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel6.12-1:6.12.110-135.201.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260928.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  amazon-ssm-agent-3.3.5226.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-41.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.3  |
|  bind-license-32:9.18.50-1.amzn2023.0.3  |
|  bind-utils-32:9.18.50-1.amzn2023.0.3  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-utils-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel-tools-1:6.1.188-233.385.amzn2023  |
|  kernel-1:6.1.188-233.385.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libpcap-14:1.10.7-1.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  rsync-3.5.1-1.amzn2023.0.1  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260928.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-ec2-net-utils-2.7.7-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260928-0.amzn2023  |
|  awscli-2-2.36.47-4.amzn2023.0.1  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  kernel-livepatch-repo-s3-2023.12.20260928-0.amzn2023  |
|  kernel-1:6.1.188-233.385.amzn2023  |
|  kmod-libs-29-2.amzn2023.0.6  |
|  kmod-29-2.amzn2023.0.6  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-awscrt-0.36.4-1.amzn2023.0.2  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.7  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.8  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  selinux-policy-targeted-38.1.76-1.amzn2023.0.3  |
|  selinux-policy-38.1.76-1.amzn2023.0.3  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  systemd-libs-252.23-14.amzn2023  |
|  systemd-networkd-252.23-14.amzn2023  |
|  systemd-pam-252.23-14.amzn2023  |
|  systemd-resolved-252.23-14.amzn2023  |
|  systemd-udev-252.23-14.amzn2023  |
|  systemd-252.23-14.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Default Container
<a name="amis-2023.12.20260928.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260928-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  dnf-4.14.0-1.amzn2023.0.8  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  python3-dnf-4.14.0-1.amzn2023.0.8  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.8  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  system-release-2023.12.20260928-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.8  |

### Minimal Container
<a name="amis-2023.12.20260928.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260928-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.2  |
|  dnf-data-4.14.0-1.amzn2023.0.8  |
|  krb5-libs-1.21.3-8.amzn2023.0.2  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.2  |
|  libxml2-2.10.4-1.amzn2023.0.21  |
|  pcre2-syntax-10.40-1.amzn2023.0.4  |
|  pcre2-10.40-1.amzn2023.0.4  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.8  |
|  rpm-4.16.1.3-29.amzn2023.0.8  |
|  system-release-2023.12.20260928-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260928.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
