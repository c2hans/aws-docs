---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261109.html
---

# Amazon Linux 2023 version 2023.12.20261109 release notes
<a name="relnotes-2023.12.20261109"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261109.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261109)
+ [Repository Updates](#repository-updates-2023.12.20261109)
  + [Core New Packages](#amis-2023.12.20261109.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20261109.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20261109.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20261109.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20261109.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20261109.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261109)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261109.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261109.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261109.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261109.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261109.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261109.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261109.Default-Container)
  + [Minimal Container](#amis-2023.12.20261109.Minimal-Container)
+ [Contact us](#amis-2023.12.20261109.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261109"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `rclone` has been updated to version 1.75.2. When authentication is configured, ordinary HTTP `OPTIONS` requests and remote-control `job/status` and `job/list` calls now require credentials. Browser CORS preflight requests remain supported when `allow-origin` is configured. Remote-control calls with out-of-range integer arguments are now rejected. Update any clients or scripts that rely on the previous behavior.
+  `python3.15-3.15.2` has been added. Python 3.15 is the newest major release of the Python programming language, and it contains many new features and optimizations. It is a namespaced package that can be installed alongside the system Python (Python 3.9).

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261109"></a>

### Core New Packages
<a name="amis-2023.12.20261109.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  python3.15-3.15.2-1.amzn2023.0.2  |
|  python3.15-flit-core-4.0.2-1.amzn2023.0.2  |
|  python3.15-packaging-26.3-1.amzn2023.0.2  |
|  python3.15-pip-26.2.1-1.amzn2023.0.2  |
|  python3.15-setuptools-84.0.0-1.amzn2023.0.2  |
|  python3.15-wheel-0.48.0-1.amzn2023.0.3  |

### Core Updated Packages
<a name="amis-2023.12.20261109.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  amazon-efs-utils-3.3.5-1.amzn2023  |
|  aws-workload-credentials-provider-3.1.2-1.amzn2023  |
|  bouncycastle-1.70-4.amzn2023.0.9  |
|  containerd-2.3.7-1.amzn2023.0.3  |
|  cups-2.4.20-1.amzn2023.0.1  |
|  curl-8.21.0-5.amzn2023.0.4  |
|  docker-25.0.18-1.amzn2023.0.3  |
|  glib-networking-2.80.0-187.amzn2023.0.2  |
|  glibc-2.34-231.amzn2023.0.6  |
|  gnome-remote-desktop-47.3-1.amzn2023.0.5  |
|  grpc-1.60.2-10.amzn2023.0.2  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.6  |
|  guava-31.0.1-3.amzn2023.0.7  |
|  ibus-anthy-1.5.18-1.amzn2023.0.2  |
|  jackson-bom-2.21.8-1.amzn2023.0.1  |
|  jackson-core-2.21.8-1.amzn2023.0.1  |
|  jackson-databind-2.21.8-1.amzn2023.0.1  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.11  |
|  kernel-6.1.190-237.431.amzn2023  |
|  kernel6.12-6.12.114-139.210.amzn2023  |
|  kernel6.18-6.18.56-126.188.amzn2023  |
|  libX11-1.8.10-2.amzn2023.0.3  |
|  libXi-1.8.4-1.amzn2023.0.1  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libreswan-4.12-3.amzn2023.0.5  |
|  librsvg2-2.59.2-320.amzn2023  |
|  lvm2-2.03.16-1.amzn2023.0.6  |
|  nautilus-47.1-720.amzn2023  |
|  nss-3.124.0-1.amzn2023.0.3  |
|  openssl-3.5.8-1.amzn2023.0.4  |
|  perl-Archive-Tar-3.04-522.amzn2023.0.4  |
|  perl-CPAN-Meta-Check-0.018-7.amzn2023.0.2  |
|  perl-Compress-Raw-Bzip2-2.217-1.amzn2023.0.3  |
|  perl-Compress-Raw-Zlib-2.221-1.amzn2023.0.3  |
|  perl-DBI-1.656-1.amzn2023.0.1  |
|  perl-DB\_File-1.860-1.amzn2023.0.3  |
|  perl-Digest-SHA-6.04-522.amzn2023.0.3  |
|  perl-Filter-1.65-2.amzn2023.0.3  |
|  perl-HTML-Tagset-3.24-5.amzn2023.0.2  |
|  perl-URI-5.18-1.amzn2023.0.2  |
|  perl-podlators-4.14-458.amzn2023.0.3  |
|  polkit-125-1.amzn2023.0.4  |
|  python-mistune-0.8.3-14.amzn2023.0.5  |
|  python-pillow-9.4.0-2.amzn2023.0.12  |
|  python-twisted-22.4.0-129.amzn2023.0.7  |
|  python-virtualenv-20.4.0-3.amzn2023.0.6  |
|  python3.12-3.12.16-2.amzn2023.0.1  |
|  python3.13-3.13.18-1.amzn2023.0.1  |
|  python3.13-tox-4.25.0-1.amzn2023.0.2  |
|  python3.13-virtualenv-20.21.1-1.amzn2023.0.5  |
|  python3.14-3.14.10-1.amzn2023.0.1  |
|  rclone-1.75.2-1.amzn2023  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  ruby3.4-3.4.12-27.amzn2023.0.8  |
|  ruby4.0-4.0.1-32.amzn2023.0.5  |
|  runfinch-finch-1.19.0-1.amzn2023.0.4  |
|  rust-1.99.1-1.amzn2023  |
|  rust-cargo-c-0.10.25-1.amzn2023.0.2  |
|  sssd-2.9.4-1.amzn2023.0.5  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |
|  xdg-desktop-portal-1.18.4-108.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20261109.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.188-233.386-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.188-233.393-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.189-236.399-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.110-135.202-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.111-136.204-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.51-120.163-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.54-121.166-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20261109.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.180-225.360-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.182-227.379-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.186-228.374-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.186-228.376-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.188-233.385-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.100-125.179-1.0-7.amzn2023  |
|  kernel-livepatch-6.12.103-127.188-1.0-5.amzn2023  |
|  kernel-livepatch-6.12.103-129.197-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.110-135.201-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.41-94.142-1.0-7.amzn2023  |
|  kernel-livepatch-6.18.44-99.149-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.48-107.148-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.48-109.150-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.51-120.162-1.0-3.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20261109.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  libnvcomp6-cuda-12-6.0.0.12-1  |
|  libnvcomp6-cuda-13-6.0.0.12-1  |
|  libnvcomp6-devel-cuda-12-6.0.0.12-1  |
|  libnvcomp6-devel-cuda-13-6.0.0.12-1  |
|  libnvjpeg2k0-cuda-12-0.12.0.58-1  |
|  libnvjpeg2k0-cuda-13-0.12.0.58-1  |
|  libnvjpeg2k0-devel-cuda-12-0.12.0.58-1  |
|  libnvjpeg2k0-devel-cuda-13-0.12.0.58-1  |
|  libnvtiff0-cuda-12-0.9.0.86-1  |
|  libnvtiff0-cuda-13-0.9.0.86-1  |
|  libnvtiff0-devel-cuda-12-0.9.0.86-1  |
|  libnvtiff0-devel-cuda-13-0.9.0.86-1  |
|  libnvtiff0-static-cuda-12-0.9.0.86-1  |
|  libnvtiff0-static-cuda-13-0.9.0.86-1  |
|  nvcomp-6.0.0-1  |
|  nvcomp-cuda-12-6.0.0.12-1  |
|  nvcomp-cuda-13-6.0.0.12-1  |
|  nvcomp0-6.0.0-1  |
|  nvjpeg2k-0.12.0-1  |
|  nvjpeg2k-cuda-12-0.12.0.58-1  |
|  nvjpeg2k-cuda-13-0.12.0.58-1  |
|  nvjpeg2k0-0.12.0-1  |
|  nvtiff-0.9.0-1  |
|  nvtiff-cuda-12-0.9.0.86-1  |
|  nvtiff-cuda-13-0.9.0.86-1  |
|  nvtiff0-0.9.0-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20261109.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cublas-cuda-12-12.9.3.13-1  |
|  cuda-13.4.3-1  |
|  cuda-13-4-13.4.3-1  |
|  cuda-command-line-tools-13-4-13.4.3-1  |
|  cuda-compiler-13-4-13.4.3-1  |
|  cuda-libraries-13-4-13.4.3-1  |
|  cuda-libraries-devel-13-4-13.4.3-1  |
|  cuda-minimal-build-13-4-13.4.3-1  |
|  cuda-nsight-compute-13-4-13.4.3-1  |
|  cuda-nsight-systems-13-4-13.4.3-1  |
|  cuda-runtime-13-4-13.4.3-1  |
|  cuda-toolkit-13.4.3-1  |
|  cuda-toolkit-13-13.4.3-1  |
|  cuda-toolkit-13-4-13.4.3-1  |
|  cuda-tools-13-4-13.4.3-1  |
|  cuda-visual-tools-13-4-13.4.3-1  |
|  libcublas12-cuda-12-12.9.3.13-1  |
|  libcublas12-devel-cuda-12-12.9.3.13-1  |
|  libcusolver-13-4-12.3.5.3-1  |
|  libcusolver-devel-13-4-12.3.5.3-1  |
|  nvidia-gds-13.4.3-1  |
|  nvidia-gds-13-4-13.4.3-1  |

## Image Updates
<a name="ami-updates-2023.12.20261109"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261109.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel6.18-tools-1:6.18.56-126.188.amzn2023  |
|  kernel6.18-1:6.18.56-126.188.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.5  |
|  nspr-4.39.0-1.amzn2023.0.3  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.3  |
|  nss-softokn-3.124.0-1.amzn2023.0.3  |
|  nss-sysinit-3.124.0-1.amzn2023.0.3  |
|  nss-util-3.124.0-1.amzn2023.0.3  |
|  nss-3.124.0-1.amzn2023.0.3  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  perl-URI-5.18-1.amzn2023.0.2  |
|  perl-Unicode-Normalize-1.27-459.amzn2023.0.3  |
|  perl-podlators-1:4.14-458.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  rust-toolset-srpm-macros-1.99.1-1.amzn2023  |
|  sssd-client-2.9.4-1.amzn2023.0.5  |
|  sssd-common-2.9.4-1.amzn2023.0.5  |
|  sssd-kcm-2.9.4-1.amzn2023.0.5  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.5  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261109.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel6.18-1:6.18.56-126.188.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261109.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel6.12-tools-1:6.12.114-139.210.amzn2023  |
|  kernel6.12-1:6.12.114-139.210.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.5  |
|  nspr-4.39.0-1.amzn2023.0.3  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.3  |
|  nss-softokn-3.124.0-1.amzn2023.0.3  |
|  nss-sysinit-3.124.0-1.amzn2023.0.3  |
|  nss-util-3.124.0-1.amzn2023.0.3  |
|  nss-3.124.0-1.amzn2023.0.3  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  perl-URI-5.18-1.amzn2023.0.2  |
|  perl-Unicode-Normalize-1.27-459.amzn2023.0.3  |
|  perl-podlators-1:4.14-458.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  rust-toolset-srpm-macros-1.99.1-1.amzn2023  |
|  sssd-client-2.9.4-1.amzn2023.0.5  |
|  sssd-common-2.9.4-1.amzn2023.0.5  |
|  sssd-kcm-2.9.4-1.amzn2023.0.5  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.5  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261109.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel6.12-1:6.12.114-139.210.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261109.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel-tools-1:6.1.190-237.431.amzn2023  |
|  kernel-1:6.1.190-237.431.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.5  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.5  |
|  nspr-4.39.0-1.amzn2023.0.3  |
|  nss-softokn-freebl-3.124.0-1.amzn2023.0.3  |
|  nss-softokn-3.124.0-1.amzn2023.0.3  |
|  nss-sysinit-3.124.0-1.amzn2023.0.3  |
|  nss-util-3.124.0-1.amzn2023.0.3  |
|  nss-3.124.0-1.amzn2023.0.3  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  perl-URI-5.18-1.amzn2023.0.2  |
|  perl-Unicode-Normalize-1.27-459.amzn2023.0.3  |
|  perl-podlators-1:4.14-458.amzn2023.0.3  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  rust-toolset-srpm-macros-1.99.1-1.amzn2023  |
|  sssd-client-2.9.4-1.amzn2023.0.5  |
|  sssd-common-2.9.4-1.amzn2023.0.5  |
|  sssd-kcm-2.9.4-1.amzn2023.0.5  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.5  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261109.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  device-mapper-libs-1.02.185-1.amzn2023.0.6  |
|  device-mapper-1.02.185-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.6  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-locale-source-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  kernel-livepatch-repo-s3-2023.12.20261109-0.amzn2023  |
|  kernel-1:6.1.190-237.431.amzn2023  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  openssl-1:3.5.8-1.amzn2023.0.4  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.9  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.12.20261109.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

### Minimal Container
<a name="amis-2023.12.20261109.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261109-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.4  |
|  glibc-common-2.34-231.amzn2023.0.6  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.6  |
|  glibc-2.34-231.amzn2023.0.6  |
|  libarchive-3.7.4-2.amzn2023.0.5  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.4  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.4  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.9  |
|  rpm-4.16.1.3-29.amzn2023.0.9  |
|  system-release-2023.12.20261109-0.amzn2023  |
|  tzdata-2026f-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.12.20261109.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
