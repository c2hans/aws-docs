---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.11.20260413.html
---

# Amazon Linux 2023 version 2023.11.20260413 release notes
<a name="relnotes-2023.11.20260413"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.11.20260413.

**Contents**
+ [Release Summary](#release-summary-2023.11.20260413)
+ [Repository Updates](#repository-updates-2023.11.20260413)
  + [Core New Packages](#amis-2023.11.20260413.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.11.20260413.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.11.20260413.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.11.20260413.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.11.20260413)
  + [Default Kernel 6.18 AMI](#amis-2023.11.20260413.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.11.20260413.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.11.20260413.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.11.20260413.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.11.20260413.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.11.20260413.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.11.20260413.Default-Container)
  + [Minimal Container](#amis-2023.11.20260413.Minimal-Container)
+ [Contact us](#amis-2023.11.20260413.contact-us)

## Release Summary
<a name="release-summary-2023.11.20260413"></a>

This release represents an update to the 11th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ New `libbpf` package is added which obsoletes kernel namespaced libbpf packages namely `kernel-libbpf{static,devel}`, `kernel6.12-libbpf{static,devel}` and `kernel6.18-libbpf{static,devel}`.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.11.20260413"></a>

### Core New Packages
<a name="amis-2023.11.20260413.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  java-26-amazon-corretto-26.0.0\+35-2.amzn2023.1  |
|  libbpf-1.6.1-3.amzn2023  |
|  sedutil-1.49.13-3.amzn2023  |

### Core Updated Packages
<a name="amis-2023.11.20260413.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.43-1.amzn2023.0.1  |
|  amazon-cloudwatch-agent-1.300064.2-1.amzn2023  |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-ecr-credential-helper-0.12.0-1.amzn2023  |
|  amazon-efs-utils-3.0.1-1.amzn2023  |
|  bcc-0.35.0-4.amzn2023.0.1  |
|  bpftrace-0.17.0-1.amzn2023.0.2  |
|  clamav1.5-1.5.1-1.amzn2023.0.5  |
|  containerd-2.2.1-1.amzn2023.0.2  |
|  corosync-3.1.9-3.amzn2023.0.2  |
|  credentials-fetcher-2.0.1-1.amzn2023.0.2  |
|  decibels-48.0-8.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  docker-25.0.14-1.amzn2023.0.3  |
|  dotnet10.0-10.0.105-1.amzn2023.0.2  |
|  dovecot-2.3.20-1.amzn2023.0.3  |
|  ecs-init-1.102.2-1.amzn2023  |
|  firefox-140.9.0-1.amzn2023.0.2  |
|  freerdp-3.6.3-1.amzn2023.0.10  |
|  gdk-pixbuf2-2.42.12-185.amzn2023  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.5  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.9  |
|  kernel6.12-6.12.79-101.147.amzn2023  |
|  kernel6.18-6.18.20-20.229.amzn2023  |
|  ldns-1.8.3-2.amzn2023.0.2  |
|  libde265-1.0.18-1.amzn2023.0.1  |
|  libpng-1.6.37-10.amzn2023.0.12  |
|  libtiff-4.4.0-4.amzn2023.0.26  |
|  mod\_security\_crs-4.2.0-1.amzn2023.0.3  |
|  nerdctl-2.2.1-1.amzn2023.0.3  |
|  nghttp2-1.59.0-3.amzn2023.0.2  |
|  nginx-1.28.3-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.4  |
|  nodejs20-20.20.2-1.amzn2023.0.1  |
|  nodejs22-22.22.2-1.amzn2023.0.1  |
|  nodejs24-24.14.1-1.amzn2023.0.1  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.9  |
|  openexr-3.1.5-1.amzn2023.0.8  |
|  openssl-3.5.5-1.amzn2023.0.4  |
|  perl-ExtUtils-CBuilder-0.280236-2.amzn2023.0.3  |
|  perl-ExtUtils-Install-2.22-521.amzn2023.0.1  |
|  perl-ExtUtils-LibBuilder-0.09-27.amzn2023.0.1  |
|  perl-ExtUtils-Manifest-1.75-521.amzn2023.0.1  |
|  perl-ExtUtils-ParseXS-3.61-2.amzn2023.0.1  |
|  perl-File-Fetch-1.08-4.amzn2023.0.1  |
|  perl-GD-2.80-1.amzn2023.0.1  |
|  perl-HTTP-Date-6.06-8.amzn2023.0.1  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.1  |
|  perl-LaTeX-ToUnicode-1.93-2.amzn2023.0.1  |
|  perl-Net-DNS-1.53-2.amzn2023.0.1  |
|  perl-XML-LibXML-2.0210-7.amzn2023.0.1  |
|  perl-XML-Parser-2.51-1.amzn2023.0.1  |
|  perl-YAML-1.31-7.amzn2023.0.1  |
|  php8.4-8.4.19-1.amzn2023.0.1  |
|  php8.5-8.5.4-1.amzn2023.0.1  |
|  plexus-utils-3.3.0-9.amzn2023.0.5  |
|  polkit-125-1.amzn2023.0.3  |
|  python-pyasn1-0.4.8-4.amzn2023.0.4  |
|  python3.11-3.11.14-1.amzn2023.0.6  |
|  python3.12-3.12.12-2.amzn2023.0.5  |
|  python3.13-3.13.12-1.amzn2023.0.2  |
|  python3.14-3.14.2-2.amzn2023.0.4  |
|  python3.9-3.9.25-1.amzn2023.0.4  |
|  runc-1.3.4-3.amzn2023.0.2  |
|  runfinch-finch-1.15.1-1.amzn2023.0.2  |
|  rust-1.94.0-1.amzn2023.0.2  |
|  rust-below-0.11.0-1.amzn2023.0.3  |
|  rust-cargo-c-0.10.19-1.amzn2023.0.2  |
|  soci-snapshotter-0.13.0-1.amzn2023.0.1  |
|  spal-release-2023-5.amzn2023  |
|  squid-6.13-1.amzn2023.0.4  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.4  |
|  tracker-miners-3.7.4-2.amzn2023.0.2  |
|  vim-9.2.240-1.amzn2023.0.2  |
|  yq-4.47.1-12.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.11.20260413.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  cuda-compat-13-2-595.58.03-1.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.11.20260413.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-drivers-595.58.03-1.amzn2023  |
|  egl-wayland2-1.0.1-10.amzn2023  |
|  egl-x11-1.0.5-1.amzn2023  |
|  kmod-nvidia-latest-dkms-595.58.03-1.amzn2023  |
|  kmod-nvidia-open-dkms-595.58.03-1.amzn2023  |
|  libnvidia-cfg-595.58.03-1.amzn2023  |
|  libnvidia-fbc-595.58.03-1.amzn2023  |
|  libnvidia-gpucomp-595.58.03-1.amzn2023  |
|  libnvidia-ml-595.58.03-1.amzn2023  |
|  libnvidia-nscq-595.58.03-1.amzn2023  |
|  libnvsdm-595.58.03-1.amzn2023  |
|  libnvsdm-devel-595.58.03-1.amzn2023  |
|  mft-4.34.1.12-1  |
|  mft-autocomplete-4.34.1.12-1  |
|  mft-oem-4.34.1.12-1  |
|  nvidia-driver-595.58.03-1.amzn2023  |
|  nvidia-driver-cuda-595.58.03-1.amzn2023  |
|  nvidia-driver-cuda-libs-595.58.03-1.amzn2023  |
|  nvidia-driver-libs-595.58.03-1.amzn2023  |
|  nvidia-fabric-manager-devel-595.58.03-1.amzn2023  |
|  nvidia-fabricmanager-595.58.03-1.amzn2023  |
|  nvidia-imex-595.58.03-1.amzn2023  |
|  nvidia-kmod-common-595.58.03-1.amzn2023  |
|  nvidia-libXNVCtrl-595.58.03-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-595.58.03-1.amzn2023  |
|  nvidia-modprobe-595.58.03-1.amzn2023  |
|  nvidia-open-595.58.03-1.amzn2023  |
|  nvidia-persistenced-595.58.03-1.amzn2023  |
|  nvidia-settings-595.58.03-1.amzn2023  |
|  nvidia-xconfig-595.58.03-1.amzn2023  |
|  nvlink5-595.58.03-1  |
|  nvlsm-2025.10.11-1  |
|  xorg-x11-nvidia-595.58.03-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.11.20260413"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.11.20260413.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  kernel6.18-tools-1:6.18.20-20.229.amzn2023  |
|  kernel6.18-1:6.18.20-20.229.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  perl-AutoLoader-5.74-477.amzn2023.0.7  |
|  perl-B-1.80-477.amzn2023.0.7  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.2  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.1  |
|  perl-Digest-1.20-1.amzn2023.0.2  |
|  perl-FileHandle-2.03-477.amzn2023.0.7  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.1  |
|  perl-IO-Socket-IP-0.41-3.amzn2023.0.2  |
|  perl-IO-Socket-SSL-2.075-1.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.2  |
|  perl-URI-5.09-1.amzn2023.0.2  |
|  perl-libnet-3.13-2.amzn2023.0.2  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.94.0-1.amzn2023.0.2  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-common-2:9.2.240-1.amzn2023.0.2  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.2  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |
|  xxd-2:9.2.240-1.amzn2023.0.2  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.11.20260413.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  kernel6.18-1:6.18.20-20.229.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |

### Default Kernel 6.12 AMI
<a name="amis-2023.11.20260413.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  kernel6.12-tools-1:6.12.79-101.147.amzn2023  |
|  kernel6.12-1:6.12.79-101.147.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  perl-AutoLoader-5.74-477.amzn2023.0.7  |
|  perl-B-1.80-477.amzn2023.0.7  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.2  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.1  |
|  perl-Digest-1.20-1.amzn2023.0.2  |
|  perl-FileHandle-2.03-477.amzn2023.0.7  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.1  |
|  perl-IO-Socket-IP-0.41-3.amzn2023.0.2  |
|  perl-IO-Socket-SSL-2.075-1.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.2  |
|  perl-URI-5.09-1.amzn2023.0.2  |
|  perl-libnet-3.13-2.amzn2023.0.2  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.94.0-1.amzn2023.0.2  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-common-2:9.2.240-1.amzn2023.0.2  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.2  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |
|  xxd-2:9.2.240-1.amzn2023.0.2  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.11.20260413.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  kernel6.12-1:6.12.79-101.147.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |

### Default Kernel 6.1 AMI
<a name="amis-2023.11.20260413.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  perl-AutoLoader-5.74-477.amzn2023.0.7  |
|  perl-B-1.80-477.amzn2023.0.7  |
|  perl-Data-Dumper-2.191-522.amzn2023.0.2  |
|  perl-Digest-MD5-2.59-521.amzn2023.0.1  |
|  perl-Digest-1.20-1.amzn2023.0.2  |
|  perl-FileHandle-2.03-477.amzn2023.0.7  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.1  |
|  perl-IO-Socket-IP-0.41-3.amzn2023.0.2  |
|  perl-IO-Socket-SSL-2.075-1.amzn2023.0.3  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.2  |
|  perl-Time-HiRes-4:1.9764-460.amzn2023.0.2  |
|  perl-URI-5.09-1.amzn2023.0.2  |
|  perl-libnet-3.13-2.amzn2023.0.2  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.94.0-1.amzn2023.0.2  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-common-2:9.2.240-1.amzn2023.0.2  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-enhanced-2:9.2.240-1.amzn2023.0.2  |
|  vim-filesystem-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |
|  xxd-2:9.2.240-1.amzn2023.0.2  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.11.20260413.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.1-1.amzn2023.0.2  |
|  amazon-linux-repo-s3-2023.11.20260413-0.amzn2023  |
|  dnf-plugin-support-info-1.12-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.11.20260413-0.amzn2023  |
|  libbpf-2:1.6.1-3.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  openssl-1:3.5.5-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  sudo-1.9.15-1.p5.amzn2023.0.3  |
|  system-release-2023.11.20260413-0.amzn2023  |
|  vim-data-2:9.2.240-1.amzn2023.0.2  |
|  vim-minimal-2:9.2.240-1.amzn2023.0.2  |

### Default Container
<a name="amis-2023.11.20260413.Default-Container"></a>

This section provides details about new/updated packages in Default Container

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260413-0.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.4  |
|  python3-3.9.25-1.amzn2023.0.4  |
|  system-release-2023.11.20260413-0.amzn2023  |

### Minimal Container
<a name="amis-2023.11.20260413.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.11.20260413-0.amzn2023  |
|  libnghttp2-1.59.0-3.amzn2023.0.2  |
|  openssl-fips-provider-latest-1:3.5.5-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.5-1.amzn2023.0.4  |
|  system-release-2023.11.20260413-0.amzn2023  |

## Contact us
<a name="amis-2023.11.20260413.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
