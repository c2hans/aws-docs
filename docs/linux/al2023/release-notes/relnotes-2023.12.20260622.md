---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260622.html
---

# Amazon Linux 2023 version 2023.12.20260622 release notes
<a name="relnotes-2023.12.20260622"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260622.

**Contents**
+ [Announcements](#announcements-2023.12.20260622)
+ [Release Summary](#release-summary-2023.12.20260622)
+ [Repository Updates](#repository-updates-2023.12.20260622)
  + [Core New Packages](#amis-2023.12.20260622.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260622.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20260622.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260622.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260622.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260622.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260622)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260622.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260622.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260622.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260622.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260622.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260622.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260622.Default-Container)
  + [Minimal Container](#amis-2023.12.20260622.Minimal-Container)
+ [Contact us](#amis-2023.12.20260622.contact-us)

## Announcements
<a name="announcements-2023.12.20260622"></a>

**Note**
The Amazon Linux team will update the Samba package from version 4.17 to 4.24. This update will be included in a regular AL2023 release in mid-August 2026. Customers are requested to plan to upgrade to Samba 4.24 in Aug 2026. Please be aware of this change and review any changes to samba from [https://www.samba.org/samba/history/](https://www.samba.org/samba/history/).

## Release Summary
<a name="release-summary-2023.12.20260622"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260622"></a>

### Core New Packages
<a name="amis-2023.12.20260622.Core-New-Packages"></a>

This section provides details about Core New Packages.

|  |
| --- |
|  nginx-mod-njs-0.9.9-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.12.20260622.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

|  |
| --- |
|  BabelfishDump-18.3-1.amzn2023.0.1  |
|  ImageMagick-6.9.13.50-1.amzn2023.0.1  |
|  amazon-cloudwatch-agent-1.300067.1-1.amzn2023  |
|  amazon-ssm-agent-3.3.4624.0-1.amzn2023  |
|  ansible-core-2.15.3-1.amzn2023.0.12  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  clamav1.5-1.5.2-1.amzn2023.0.2  |
|  cni-plugins-1.7.1-1.amzn2023.0.7  |
|  compat-poppler22-22.08.0-3.amzn2023.0.6  |
|  containerd-2.2.4-1.amzn2023.0.3  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  dotnet10.0-10.0.109-1.amzn2023.0.1  |
|  dotnet8.0-8.0.128-1.amzn2023.0.1  |
|  dotnet9.0-9.0.118-1.amzn2023.0.2  |
|  ecs-init-1.104.0-1.amzn2023  |
|  ecs-service-connect-agent-v1.34.13.2-1.amzn2023  |
|  freerdp-3.6.3-1.amzn2023.0.12  |
|  gdal310-3.10.3-3.amzn2023.0.2  |
|  giflib-5.2.1-9.amzn2023.0.4  |
|  git-lfs-3.7.1-81.amzn2023  |
|  golang-1.25.11-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.2  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.4  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.8  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.1  |
|  golist-0.10.4-12.amzn2023.0.10  |
|  graphite2-1.3.14-7.amzn2023.0.3  |
|  httpd-2.4.68-1.amzn2023.0.1  |
|  jpegxl-0.10.3-56.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-6.1.175-219.357.amzn2023  |
|  kernel6.12-6.12.92-122.166.amzn2023  |
|  kernel6.18-6.18.35-68.127.amzn2023  |
|  libinput-1.26.2-1.amzn2023.0.2  |
|  libnfs-4.0.0-4.amzn2023.0.3  |
|  libssh-0.10.6-1.amzn2023.0.8  |
|  libusbx-1.0.24-2.amzn2023.0.3  |
|  loupe-47.4-34.amzn2023  |
|  mariadb-connector-c-3.3.10-1.amzn2023.0.2  |
|  mod\_http2-2.0.42-1.amzn2023.0.1  |
|  openssl-3.5.5-1.amzn2023.0.5  |
|  pcs-0.12.1-1.amzn2023.0.2  |
|  perl-Cpanel-JSON-XS-4.25-2.amzn2023.0.9  |
|  perl-Crypt-PBKDF2-0.261630-1.amzn2023.0.1  |
|  perl-CryptX-0.088-2.amzn2023.0.3  |
|  perl-DBI-1.648-1.amzn2023.0.1  |
|  perl-GD-2.80-1.amzn2023.0.3  |
|  perl-HTML-Parser-3.76-1.amzn2023.0.4  |
|  perl-IO-Compress-2.217-1.amzn2023.0.2  |
|  perl-Sereal-Decoder-4.018-2.amzn2023.0.4  |
|  perl-Unicode-LineBreak-2019.001-9.amzn2023.0.4  |
|  php8.4-8.4.22-1.amzn2023.0.1  |
|  php8.5-8.5.7-1.amzn2023.0.1  |
|  poppler-24.08.0-1.amzn2023.0.1  |
|  postfix-3.7.2-4.amzn2023.0.6  |
|  python-click-7.1.2-5.amzn2023.0.3  |
|  python-jwt-2.4.0-1.amzn2023.0.4  |
|  python-mako-1.1.4-3.amzn2023.0.4  |
|  python-pip-21.3.1-2.amzn2023.0.20  |
|  python-urllib3-1.25.10-5.amzn2023.0.7  |
|  python3.11-3.11.15-1.amzn2023.0.2  |
|  python3.11-pip-22.3.1-2.amzn2023.0.13  |
|  python3.12-pip-23.2.1-4.amzn2023.0.10  |
|  python3.13-pip-24.2-259.amzn2023.0.7  |
|  python3.14-pip-26.1.1-1.amzn2023.0.2  |
|  rrdtool-1.7.2-16.amzn2023.0.4  |
|  runfinch-finch-1.17.1-1.amzn2023.0.3  |
|  rust-1.96.0-1.amzn2023.0.2  |
|  rust-cargo-c-0.10.19-1.amzn2023.0.3  |
|  samba-4.17.12-1.amzn2023.0.4  |
|  soci-snapshotter-0.14.1-1.amzn2023.0.1  |
|  squid-6.13-1.amzn2023.0.5  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.6  |
|  vim-9.2.597-1.amzn2023.0.1  |
|  yq-4.53.3-14.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20260622.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

|  |
| --- |
|  kernel-livepatch-6.1.172-216.329-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.88-119.157-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.88-119.160-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.90-120.164-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.30-61.116-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.30-61.119-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.33-63.124-1.0-2.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260622.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

|  |
| --- |
|  kernel-livepatch-6.1.164-196.303-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.166-197.305-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.168-202.320-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.168-203.330-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.170-208.319-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.170-210.320-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.170-213.321-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.74-98.124-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.77-99.140-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.79-101.147-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.80-105.147-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.80-106.156-1.0-7.amzn2023  |
|  kernel-livepatch-6.12.83-111.159-1.0-7.amzn2023  |
|  kernel-livepatch-6.12.83-113.160-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.83-115.161-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.15-14.217-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.16-18.222-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.20-20.229-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.20-41.237-1.0-7.amzn2023  |
|  kernel-livepatch-6.18.25-52.107-1.0-7.amzn2023  |
|  kernel-livepatch-6.18.25-55.108-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.25-57.109-1.0-5.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20260622.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

|  |
| --- |
|  cccl-13-3-13.3.3.3.1-1  |
|  cuda-13-3-13.3.0-1  |
|  cuda-command-line-tools-13-3-13.3.0-1  |
|  cuda-compiler-13-3-13.3.0-1  |
|  cuda-crt-13-3-13.3.33-1  |
|  cuda-ctadvisor-13-3-13.3.33-1  |
|  cuda-cudart-13-3-13.3.29-1  |
|  cuda-cudart-devel-13-3-13.3.29-1  |
|  cuda-culibos-devel-13-3-13.3.33-1  |
|  cuda-cuobjdump-13-3-13.3.29-1  |
|  cuda-cupti-13-3-13.3.35-1  |
|  cuda-cuxxfilt-13-3-13.3.29-1  |
|  cuda-documentation-13-3-13.3.40-1  |
|  cuda-driver-devel-13-3-13.3.29-1  |
|  cuda-gdb-13-3-13.3.27-1  |
|  cuda-gdb-src-13-3-13.3.27-1  |
|  cuda-libraries-13-3-13.3.0-1  |
|  cuda-libraries-devel-13-3-13.3.0-1  |
|  cuda-minimal-build-13-3-13.3.0-1  |
|  cuda-nsight-compute-13-3-13.3.0-1  |
|  cuda-nsight-systems-13-3-13.3.0-1  |
|  cuda-nvcc-13-3-13.3.33-1  |
|  cuda-nvdisasm-13-3-13.3.29-1  |
|  cuda-nvml-devel-13-3-13.3.29-1  |
|  cuda-nvprune-13-3-13.3.29-1  |
|  cuda-nvrtc-13-3-13.3.33-1  |
|  cuda-nvrtc-devel-13-3-13.3.33-1  |
|  cuda-nvtx-13-3-13.3.29-1  |
|  cuda-opencl-13-3-13.3.27-1  |
|  cuda-opencl-devel-13-3-13.3.27-1  |
|  cuda-profiler-api-13-3-13.3.27-1  |
|  cuda-runtime-13-3-13.3.0-1  |
|  cuda-sandbox-devel-13-3-13.3.29-1  |
|  cuda-sanitizer-13-3-13.3.27-1  |
|  cuda-tileiras-13-3-13.3.36-1  |
|  cuda-toolkit-13-3-13.3.0-1  |
|  cuda-toolkit-13-3-config-common-13.3.29-1  |
|  cuda-tools-13-3-13.3.0-1  |
|  cuda-visual-tools-13-3-13.3.0-1  |
|  gds-tools-13-3-1.18.0.66-1  |
|  libcublas-13-3-13.5.1.27-1  |
|  libcublas-devel-13-3-13.5.1.27-1  |
|  libcufft-13-3-12.3.0.29-1  |
|  libcufft-devel-13-3-12.3.0.29-1  |
|  libcufile-13-3-1.18.0.66-1  |
|  libcufile-devel-13-3-1.18.0.66-1  |
|  libcuobjclient-13-3-1.2.0.59-1  |
|  libcuobjclient-devel-13-3-1.2.0.59-1  |
|  libcurand-13-3-10.4.3.29-1  |
|  libcurand-devel-13-3-10.4.3.29-1  |
|  libcusolver-13-3-12.2.2.18-1  |
|  libcusolver-devel-13-3-12.2.2.18-1  |
|  libcusparse-13-3-12.8.1.7-1  |
|  libcusparse-devel-13-3-12.8.1.7-1  |
|  libnpp-13-3-13.1.2.48-1  |
|  libnpp-devel-13-3-13.1.2.48-1  |
|  libnvfatbin-13-3-13.3.29-1  |
|  libnvfatbin-devel-13-3-13.3.29-1  |
|  libnvjitlink-13-3-13.3.33-1  |
|  libnvjitlink-devel-13-3-13.3.33-1  |
|  libnvjpeg-13-3-13.2.0.21-1  |
|  libnvjpeg-devel-13-3-13.2.0.21-1  |
|  libnvptxcompiler-13-3-13.3.33-1  |
|  libnvvm-13-3-13.3.33-1  |
|  nsight-compute-2026.2.0-2026.2.0.7-1  |
|  nsight-systems-2026.1.3-2026.1.3.243\_261337792075v0-0  |
|  nvidia-gds-13-3-13.3.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260622.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

|  |
| --- |
|  cuda-13.3.0-1  |
|  cuda-compat-13-0-580.167.08-1.amzn2023  |
|  cuda-toolkit-13.3.0-1  |
|  cuda-toolkit-13-13.3.0-1  |
|  cuda-toolkit-13-config-common-13.3.29-1  |
|  cuda-toolkit-config-common-13.3.29-1  |
|  cutensor-2.7.0-1  |
|  cutensor-cuda-12-2.7.0.5-1  |
|  cutensor-cuda-13-2.7.0.5-1  |
|  cutensor2-2.7.0-1  |
|  libcutensor2-cuda-12-2.7.0.5-1  |
|  libcutensor2-cuda-13-2.7.0.5-1  |
|  libcutensor2-devel-cuda-12-2.7.0.5-1  |
|  libcutensor2-devel-cuda-13-2.7.0.5-1  |
|  libnvat-1.2.2.1780962352-1  |
|  libnvat-devel-1.2.2.1780962352-1  |
|  nvattest-1.2.2.1780962352-1  |
|  nvidia-fs-2.29.4-1  |
|  nvidia-fs-dkms-2.29.4-1  |
|  nvidia-gds-13.3.0-1  |
|  nvlink5-580-580.167.08-1  |
|  nvlsm-2025.10.14-1  |

## Image Updates
<a name="ami-updates-2023.12.20260622"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260622.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  amazon-ssm-agent-3.3.4624.0-1.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel6.18-tools-1:6.18.35-68.127.amzn2023  |
|  kernel6.18-1:6.18.35-68.127.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  rust-toolset-srpm-macros-1.96.0-1.amzn2023.0.2  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-common-2:9.2.597-1.amzn2023.0.1  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.597-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |
|  xxd-2:9.2.597-1.amzn2023.0.1  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260622.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel6.18-1:6.18.35-68.127.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260622.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  amazon-ssm-agent-3.3.4624.0-1.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel6.12-tools-1:6.12.92-122.166.amzn2023  |
|  kernel6.12-1:6.12.92-122.166.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  rust-toolset-srpm-macros-1.96.0-1.amzn2023.0.2  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-common-2:9.2.597-1.amzn2023.0.1  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.597-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |
|  xxd-2:9.2.597-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260622.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel6.12-1:6.12.92-122.166.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260622.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  amazon-ssm-agent-3.3.4624.0-1.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel-tools-1:6.1.175-219.357.amzn2023  |
|  kernel-1:6.1.175-219.357.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  rust-toolset-srpm-macros-1.96.0-1.amzn2023.0.2  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-common-2:9.2.597-1.amzn2023.0.1  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.597-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |
|  xxd-2:9.2.597-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260622.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260622-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  dnf-plugin-support-info-1.14-1.amzn2023  |
|  jq-1.8.1-60.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260622-0.amzn2023  |
|  kernel-1:6.1.175-219.357.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  openssl-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  python3-urllib3-1.25.10-5.amzn2023.0.7  |
|  system-release-2023.12.20260622-0.amzn2023  |
|  systemd-libs-252.23-12.amzn2023  |
|  systemd-networkd-252.23-12.amzn2023  |
|  systemd-pam-252.23-12.amzn2023  |
|  systemd-resolved-252.23-12.amzn2023  |
|  systemd-udev-252.23-12.amzn2023  |
|  systemd-252.23-12.amzn2023  |
|  vim-data-2:9.2.597-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.597-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.12.20260622.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260622-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.20  |
|  system-release-2023.12.20260622-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260622.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260622-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.3  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.5  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.5  |
|  system-release-2023.12.20260622-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260622.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
