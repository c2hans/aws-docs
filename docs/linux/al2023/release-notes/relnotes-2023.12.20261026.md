---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261026.html
---

# Amazon Linux 2023 version 2023.12.20261026 release notes
<a name="relnotes-2023.12.20261026"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261026.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261026)
+ [Repository Updates](#repository-updates-2023.12.20261026)
  + [Core Updated Packages](#amis-2023.12.20261026.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20261026.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20261026.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261026)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261026.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261026.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261026.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261026.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261026.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261026.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261026.Default-Container)
  + [Minimal Container](#amis-2023.12.20261026.Minimal-Container)
+ [Contact us](#amis-2023.12.20261026.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261026"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261026"></a>

### Core Updated Packages
<a name="amis-2023.12.20261026.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  amazon-ecr-credential-helper-0.12.0-5.amzn2023  |
|  amazon-efs-utils-3.3.4-1.amzn2023  |
|  ant-1.10.12-5.amzn2023.0.5  |
|  aspell-0.60.8-7.amzn2023.0.3  |
|  aws-cfn-bootstrap-2.0-42.amzn2023  |
|  aws-kinesis-agent-2.0.14-1.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  bind-9.18.50-1.amzn2023.0.5  |
|  brotli-1.1.0-1.amzn2023.0.2  |
|  buildah-1.43.1-1.amzn2023.0.3  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  cifs-utils-7.7-145.amzn2023.0.1  |
|  cni-plugins-1.7.1-1.amzn2023.0.8  |
|  containerd-2.3.7-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.8  |
|  curl-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-2.1.27-18.amzn2023.0.4  |
|  docker-25.0.18-1.amzn2023.0.2  |
|  ecs-init-1.108.1-1.amzn2023  |
|  edk2-20260508-2.amzn2023  |
|  firefox-153.5.1-1.amzn2023.0.1  |
|  freerdp-3.32.2-1.amzn2023  |
|  ghostscript-9.56.1-7.amzn2023.0.20  |
|  git-lfs-3.7.1-82.amzn2023  |
|  golang-1.26.10-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.9  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.11  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.15  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.8  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2023.0.9  |
|  golist-0.10.4-12.amzn2023.0.17  |
|  grub2-2.06-61.amzn2023.0.24  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.10  |
|  haproxy-3.0.30-1.amzn2023.0.1  |
|  iperf3-3.22-1.amzn2023.0.1  |
|  java-1.8.0-amazon-corretto-1.8.0\_512.b08-1.amzn2023  |
|  java-11-amazon-corretto-11.0.33.0.9-1.amzn2023  |
|  java-17-amazon-corretto-17.0.21.0.10-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.13.0.10-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.5.0.9-1.amzn2023.1  |
|  java-27-amazon-corretto-27.0.1.0.10-1.amzn2023.1  |
|  kernel-6.1.189-236.399.amzn2023  |
|  kernel6.12-6.12.113-138.209.amzn2023  |
|  kernel6.18-6.18.56-125.164.amzn2023  |
|  kiwi-10.3.0-2.amzn2023  |
|  libXtst-1.2.5-1.amzn2023.0.2  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libheif-1.23.6-1.amzn2023  |
|  libreswan-4.12-3.amzn2023.0.4  |
|  libsoup3-3.7.3-1.amzn2023  |
|  lustre-client-2.15.6-35.amzn2023  |
|  mariadb1011-10.11.19-1.amzn2023.0.2  |
|  mariadb114-11.4.13-1.amzn2023.0.2  |
|  mariadb118-11.8.9-1.amzn2023.0.2  |
|  mariadb123-12.3.3-2.amzn2023.0.2  |
|  mod\_security-2.9.15-1.amzn2023.0.1  |
|  nerdctl-2.3.5-1.amzn2023.0.2  |
|  nginx-1.30.6-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.11  |
|  nginx-mod-njs-1.0.2-1.amzn2023.0.1  |
|  nodejs22-22.23.4-1.amzn2023.0.1  |
|  nodejs24-24.22.1-1.amzn2023.0.1  |
|  nss-3.124.0-1.amzn2023.0.2  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.13  |
|  openvpn-2.6.12-1.amzn2023.0.8  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  perl-5.32.1-477.amzn2023.0.11  |
|  python-awscrt-0.37.0-1.amzn2023.0.1  |
|  python-jwt-2.4.0-1.amzn2023.0.6  |
|  python-tornado-6.1.0-2.amzn2023.0.12  |
|  python-virtualenv-20.4.0-3.amzn2023.0.5  |
|  python3.11-3.11.17-1.amzn2023.0.1  |
|  python3.12-3.12.15-2.amzn2023.0.1  |
|  python3.13-3.13.16-1.amzn2023.0.1  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.7  |
|  python3.13-virtualenv-20.21.1-1.amzn2023.0.4  |
|  python3.14-3.14.8-1.amzn2023.0.1  |
|  python3.9-3.9.25-1.amzn2023.0.11  |
|  qemu-11.0.0-4.amzn2023  |
|  runc-1.4.3-1.amzn2023.0.3  |
|  runfinch-finch-1.19.0-1.amzn2023.0.2  |
|  rust-1.99.0-1.amzn2023  |
|  skopeo-1.22.2-1.amzn2023.0.3  |
|  soci-snapshotter-0.16.0-1.amzn2023.0.2  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.7  |
|  unbound-1.17.1-1.amzn2023.0.17  |
|  util-linux-2.37.4-1.amzn2023.0.7  |
|  valkey-9.0.6-1.amzn2023.0.2  |
|  wireshark-4.6.9-1.amzn2023.0.2  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.12  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.7  |
|  yq-4.53.3-15.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20261026.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  open-nvdebug-2.2.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20261026.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  collectx-bringup-1.26.0-1  |
|  cuda-compat-13-0-580.196.07-1.amzn2023  |
|  cuda-compat-13-4-615.71.10-1.amzn2023  |
|  datacenter-gpu-manager-4-core-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda-all-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda11-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda11-cublas-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-cublas-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-curand-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-cusparselt-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-nccl-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda12-ubergemm2-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-cublas-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-curand-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-cusparselt-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-nccl-4.7.0-2  |
|  datacenter-gpu-manager-4-cuda13-ubergemm2-4.7.0-2  |
|  datacenter-gpu-manager-4-dcgmproftesterkernels-4.7.0-2  |
|  datacenter-gpu-manager-4-devel-4.7.0-2  |
|  datacenter-gpu-manager-4-module-config-4.7.0-2  |
|  datacenter-gpu-manager-4-module-diag-4.7.0-2  |
|  datacenter-gpu-manager-4-module-health-4.7.0-2  |
|  datacenter-gpu-manager-4-module-introspect-4.7.0-2  |
|  datacenter-gpu-manager-4-module-nvswitch-4.7.0-2  |
|  datacenter-gpu-manager-4-module-policy-4.7.0-2  |
|  datacenter-gpu-manager-4-module-sysmon-4.7.0-2  |
|  datacenter-gpu-manager-4-multinode-4.7.0-2  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.7.0-2  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.7.0-2  |
|  datacenter-gpu-manager-4-proprietary-4.7.0-2  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.7.0-2  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.7.0-2  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.7.0-2  |
|  datacenter-gpu-manager-4-python3-4.7.0-2  |
|  dcgmi-4.7.0-2  |
|  egl-gbm-1.1.4-2.amzn2023  |
|  egl-wayland-1.1.23-1.amzn2023  |
|  egl-wayland-devel-1.1.23-1.amzn2023  |
|  libdcgm-4.7.0-2  |
|  libnvat-2.0.0.1790976895-1  |
|  libnvat-devel-2.0.0.1790976895-1  |
|  libnvidia-container-devel-1.20.1-1  |
|  libnvidia-container-static-1.20.1-1  |
|  libnvidia-container-tools-1.20.1-1  |
|  libnvidia-container1-1.20.1-1  |
|  nv-hostengine-4.7.0-2  |
|  nvattest-2.0.0.1790976895-1  |
|  nvidia-container-toolkit-1.20.1-1  |
|  nvidia-container-toolkit-base-1.20.1-1  |
|  nvidia-driver-assistant-0.62.71.10-1  |
|  nvidia-driver-selinux-0.1-3.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20261026"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261026.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-42.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.5  |
|  bind-license-32:9.18.50-1.amzn2023.0.5  |
|  bind-utils-32:9.18.50-1.amzn2023.0.5  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  cyrus-sasl-plain-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel6.18-tools-1:6.18.56-125.164.amzn2023  |
|  kernel6.18-1:6.18.56-125.164.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  nspr-4.39.0-1.amzn2023.0.2  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.2  |
|  nss-softokn-3.124.0-1.amzn2023.0.2  |
|  nss-sysinit-3.124.0-1.amzn2023.0.2  |
|  nss-util-3.124.0-1.amzn2023.0.2  |
|  nss-3.124.0-1.amzn2023.0.2  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  perl-AutoLoader-5.74-477.amzn2023.0.11  |
|  perl-B-1.80-477.amzn2023.0.11  |
|  perl-Class-Struct-0.66-477.amzn2023.0.11  |
|  perl-DynaLoader-1.47-477.amzn2023.0.11  |
|  perl-Errno-1.30-477.amzn2023.0.11  |
|  perl-Fcntl-1.13-477.amzn2023.0.11  |
|  perl-File-Basename-2.85-477.amzn2023.0.11  |
|  perl-File-stat-1.09-477.amzn2023.0.11  |
|  perl-FileHandle-2.03-477.amzn2023.0.11  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.11  |
|  perl-IO-1.43-477.amzn2023.0.11  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.11  |
|  perl-POSIX-1.94-477.amzn2023.0.11  |
|  perl-SelectSaver-1.02-477.amzn2023.0.11  |
|  perl-Symbol-1.08-477.amzn2023.0.11  |
|  perl-base-2.27-477.amzn2023.0.11  |
|  perl-if-0.60.800-477.amzn2023.0.11  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.11  |
|  perl-libs-4:5.32.1-477.amzn2023.0.11  |
|  perl-mro-1.23-477.amzn2023.0.11  |
|  perl-overload-1.31-477.amzn2023.0.11  |
|  perl-overloading-0.02-477.amzn2023.0.11  |
|  perl-subs-1.03-477.amzn2023.0.11  |
|  perl-vars-1.05-477.amzn2023.0.11  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  rust-toolset-srpm-macros-1.99.0-1.amzn2023  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261026.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel6.18-1:6.18.56-125.164.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261026.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-42.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.5  |
|  bind-license-32:9.18.50-1.amzn2023.0.5  |
|  bind-utils-32:9.18.50-1.amzn2023.0.5  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  cyrus-sasl-plain-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel6.12-tools-1:6.12.113-138.209.amzn2023  |
|  kernel6.12-1:6.12.113-138.209.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  nspr-4.39.0-1.amzn2023.0.2  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.2  |
|  nss-softokn-3.124.0-1.amzn2023.0.2  |
|  nss-sysinit-3.124.0-1.amzn2023.0.2  |
|  nss-util-3.124.0-1.amzn2023.0.2  |
|  nss-3.124.0-1.amzn2023.0.2  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  perl-AutoLoader-5.74-477.amzn2023.0.11  |
|  perl-B-1.80-477.amzn2023.0.11  |
|  perl-Class-Struct-0.66-477.amzn2023.0.11  |
|  perl-DynaLoader-1.47-477.amzn2023.0.11  |
|  perl-Errno-1.30-477.amzn2023.0.11  |
|  perl-Fcntl-1.13-477.amzn2023.0.11  |
|  perl-File-Basename-2.85-477.amzn2023.0.11  |
|  perl-File-stat-1.09-477.amzn2023.0.11  |
|  perl-FileHandle-2.03-477.amzn2023.0.11  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.11  |
|  perl-IO-1.43-477.amzn2023.0.11  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.11  |
|  perl-POSIX-1.94-477.amzn2023.0.11  |
|  perl-SelectSaver-1.02-477.amzn2023.0.11  |
|  perl-Symbol-1.08-477.amzn2023.0.11  |
|  perl-base-2.27-477.amzn2023.0.11  |
|  perl-if-0.60.800-477.amzn2023.0.11  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.11  |
|  perl-libs-4:5.32.1-477.amzn2023.0.11  |
|  perl-mro-1.23-477.amzn2023.0.11  |
|  perl-overload-1.31-477.amzn2023.0.11  |
|  perl-overloading-0.02-477.amzn2023.0.11  |
|  perl-subs-1.03-477.amzn2023.0.11  |
|  perl-vars-1.05-477.amzn2023.0.11  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  rust-toolset-srpm-macros-1.99.0-1.amzn2023  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261026.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel6.12-1:6.12.113-138.209.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261026.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-42.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  bind-libs-32:9.18.50-1.amzn2023.0.5  |
|  bind-license-32:9.18.50-1.amzn2023.0.5  |
|  bind-utils-32:9.18.50-1.amzn2023.0.5  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  cyrus-sasl-plain-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel-tools-1:6.1.189-236.399.amzn2023  |
|  kernel-1:6.1.189-236.399.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  nspr-4.39.0-1.amzn2023.0.2  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.2  |
|  nss-softokn-3.124.0-1.amzn2023.0.2  |
|  nss-sysinit-3.124.0-1.amzn2023.0.2  |
|  nss-util-3.124.0-1.amzn2023.0.2  |
|  nss-3.124.0-1.amzn2023.0.2  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  perl-AutoLoader-5.74-477.amzn2023.0.11  |
|  perl-B-1.80-477.amzn2023.0.11  |
|  perl-Class-Struct-0.66-477.amzn2023.0.11  |
|  perl-DynaLoader-1.47-477.amzn2023.0.11  |
|  perl-Errno-1.30-477.amzn2023.0.11  |
|  perl-Fcntl-1.13-477.amzn2023.0.11  |
|  perl-File-Basename-2.85-477.amzn2023.0.11  |
|  perl-File-stat-1.09-477.amzn2023.0.11  |
|  perl-FileHandle-2.03-477.amzn2023.0.11  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.11  |
|  perl-IO-1.43-477.amzn2023.0.11  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.11  |
|  perl-POSIX-1.94-477.amzn2023.0.11  |
|  perl-SelectSaver-1.02-477.amzn2023.0.11  |
|  perl-Symbol-1.08-477.amzn2023.0.11  |
|  perl-base-2.27-477.amzn2023.0.11  |
|  perl-if-0.60.800-477.amzn2023.0.11  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.11  |
|  perl-libs-4:5.32.1-477.amzn2023.0.11  |
|  perl-mro-1.23-477.amzn2023.0.11  |
|  perl-overload-1.31-477.amzn2023.0.11  |
|  perl-overloading-0.02-477.amzn2023.0.11  |
|  perl-subs-1.03-477.amzn2023.0.11  |
|  perl-vars-1.05-477.amzn2023.0.11  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  rust-toolset-srpm-macros-1.99.0-1.amzn2023  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261026.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261026-0.amzn2023  |
|  awscli-2-2.38.0-1.amzn2023.0.1  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  cyrus-sasl-lib-2.1.27-18.amzn2023.0.4  |
|  grub2-common-1:2.06-61.amzn2023.0.24  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.24  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.24  |
|  grub2-tools-1:2.06-61.amzn2023.0.24  |
|  kernel-livepatch-repo-s3-2023.12.20261026-0.amzn2023  |
|  kernel-1:6.1.189-236.399.amzn2023  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libfdisk-2.37.4-1.amzn2023.0.7  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  python3-awscrt-0.37.0-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  system-release-2023.12.20261026-0.amzn2023  |
|  util-linux-core-2.37.4-1.amzn2023.0.7  |
|  util-linux-2.37.4-1.amzn2023.0.7  |

### Default Container
<a name="amis-2023.12.20261026.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261026-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  python3-libs-3.9.25-1.amzn2023.0.11  |
|  python3-3.9.25-1.amzn2023.0.11  |
|  system-release-2023.12.20261026-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20261026.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261026-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.4  |
|  curl-minimal-8.21.0-5.amzn2023.0.3  |
|  libblkid-2.37.4-1.amzn2023.0.7  |
|  libcap-2.73-1.amzn2023.0.8  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.3  |
|  libmount-2.37.4-1.amzn2023.0.7  |
|  libsmartcols-2.37.4-1.amzn2023.0.7  |
|  libuuid-2.37.4-1.amzn2023.0.7  |
|  pcre2-syntax-10.40-1.amzn2023.0.5  |
|  pcre2-10.40-1.amzn2023.0.5  |
|  system-release-2023.12.20261026-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261026.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
