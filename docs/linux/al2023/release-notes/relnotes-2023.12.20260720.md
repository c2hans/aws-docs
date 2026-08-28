---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260720.html
---

# Amazon Linux 2023 version 2023.12.20260720 release notes
<a name="relnotes-2023.12.20260720"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260720.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260720)
+ [Repository Updates](#repository-updates-2023.12.20260720)
  + [Core New Packages](#amis-2023.12.20260720.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260720.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20260720.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260720.Kernel-livepatch-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260720.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260720)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260720.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260720.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260720.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260720.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260720.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260720.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260720.Default-Container)
  + [Minimal Container](#amis-2023.12.20260720.Minimal-Container)
+ [Contact us](#amis-2023.12.20260720.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260720"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ `MariaDB12.3` has been added. For information about changes and improvements in this version, see the [ official MariaDB documentation](https://mariadb.com/docs/release-notes/community-server/12.3/mariadb-12.3-changes-and-improvements.html).

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260720"></a>

### Core New Packages
<a name="amis-2023.12.20260720.Core-New-Packages"></a>

This section provides details about Core New Packages.

|  |
| --- |
|  gdrcopy-2.5.2-2.amzn2023  |
|  llvm21-21.1.8-7.amzn2023  |
|  llvm22-22.1.8-1131.amzn2023  |
|  mariadb123-12.3.2-2.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.12.20260720.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

|  |
| --- |
|  GraphicsMagick-1.3.45-1.amzn2023.0.3  |
|  acl-2.4.0-1.amzn2023.0.1  |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  aws-cfn-bootstrap-2.0-40.amzn2023  |
|  bind-9.18.50-1.amzn2023.0.1  |
|  clamav1.4-1.4.5-1.amzn2023.0.1  |
|  clamav1.5-1.5.3-1.amzn2023.0.1  |
|  composer-2.10.2-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.2  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-102-3.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.11-0.amzn2023  |
|  ecs-init-1.105.1-1.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-2.34-231.amzn2023.0.5  |
|  golang-1.25.12-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.3  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.5  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.9  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.2  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2023.0.3  |
|  golist-0.10.4-12.amzn2023.0.11  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.7  |
|  httpcomponents-core-4.4.13-6.amzn2023.0.4  |
|  jackson-databind-2.16.1-4.amzn2023.0.2  |
|  kernel-6.1.176-221.367.amzn2023  |
|  kernel6.12-6.12.94-123.190.amzn2023  |
|  kernel6.18-6.18.38-73.137.amzn2023  |
|  krb5-1.21.3-8.amzn2023.0.1  |
|  libXfont2-2.0.7-1.amzn2023.0.2  |
|  libde265-1.0.18-1.amzn2023.0.3  |
|  libheif-1.19.8-1.amzn2023.0.7  |
|  libssh2-1.10.0-1.amzn2023.0.5  |
|  libtiff-4.4.0-4.amzn2023.0.27  |
|  nodejs22-22.23.1-1.amzn2023.0.2  |
|  nodejs24-24.18.0-1.amzn2023.0.2  |
|  opensc-0.24.0-1.amzn2023.0.6  |
|  openvpn-2.6.12-1.amzn2023.0.5  |
|  perl-DBI-1.650-1.amzn2023.0.1  |
|  php8.2-8.2.32-1.amzn2023.0.1  |
|  php8.3-8.3.32-1.amzn2023.0.1  |
|  php8.4-8.4.23-1.amzn2023.0.1  |
|  php8.5-8.5.8-1.amzn2023.0.1  |
|  python-pillow-9.4.0-2.amzn2023.0.9  |
|  python-pygments-2.7.4-1.amzn2023.0.3  |
|  python3.11-3.11.15-1.amzn2023.0.4  |
|  python3.12-3.12.13-2.amzn2023.0.4  |
|  python3.13-3.13.14-1.amzn2023.0.2  |
|  python3.14-3.14.6-1.amzn2023.0.2  |
|  python3.9-3.9.25-1.amzn2023.0.8  |
|  runfinch-finch-1.17.2-1.amzn2023.0.1  |
|  rust-1.97.0-1.amzn2023.0.1  |
|  sssd-2.9.4-1.amzn2023.0.4  |
|  swiftlang-6.3-1.amzn2023.0.1  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tomcat-native-2.0.15-1.amzn2023.0.2  |
|  tomcat10-10.1.57-1.amzn2023.0.1  |
|  tomcat9-9.0.120-1.amzn2023.0.1  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-9.2.725-1.amzn2023.0.1  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.11  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.6  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20260720.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

|  |
| --- |
|  kernel-livepatch-6.1.172-216.339-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.174-217.345-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.175-219.357-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.175-219.359-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.176-220.358-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.92-122.166-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.92-122.168-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.94-123.174-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.35-68.127-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.35-68.129-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.36-69.134-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260720.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

|  |
| --- |
|  kernel-livepatch-6.1.168-202.320-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.168-203.330-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.170-208.319-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.170-210.320-1.0-5.amzn2023  |
|  kernel-livepatch-6.1.170-213.321-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.172-216.329-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.80-105.147-1.0-9.amzn2023  |
|  kernel-livepatch-6.12.80-106.156-1.0-9.amzn2023  |
|  kernel-livepatch-6.12.83-111.159-1.0-9.amzn2023  |
|  kernel-livepatch-6.12.83-113.160-1.0-7.amzn2023  |
|  kernel-livepatch-6.12.83-115.161-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.88-119.157-1.0-5.amzn2023  |
|  kernel-livepatch-6.12.88-119.160-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.90-120.164-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.20-41.237-1.0-9.amzn2023  |
|  kernel-livepatch-6.18.25-52.107-1.0-9.amzn2023  |
|  kernel-livepatch-6.18.25-55.108-1.0-7.amzn2023  |
|  kernel-livepatch-6.18.25-57.109-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.30-61.116-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.30-61.119-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.33-63.124-1.0-3.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260720.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

|  |
| --- |
|  libnvidia-container-devel-1.19.1-1  |
|  libnvidia-container-static-1.19.1-1  |
|  libnvidia-container-tools-1.19.1-1  |
|  libnvidia-container1-1.19.1-1  |
|  nvidia-container-toolkit-1.19.1-1  |
|  nvidia-container-toolkit-base-1.19.1-1  |

## Image Updates
<a name="ami-updates-2023.12.20260720"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260720.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  acl-2.4.0-1.amzn2023.0.1  |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-40.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.1  |
|  bind-license-32:9.18.50-1.amzn2023.0.1  |
|  bind-utils-32:9.18.50-1.amzn2023.0.1  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.11-0.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel6.18-tools-1:6.18.38-73.137.amzn2023  |
|  kernel6.18-1:6.18.38-73.137.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.4  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  rust-toolset-srpm-macros-1.97.0-1.amzn2023.0.1  |
|  sssd-client-2.9.4-1.amzn2023.0.4  |
|  sssd-common-2.9.4-1.amzn2023.0.4  |
|  sssd-kcm-2.9.4-1.amzn2023.0.4  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.4  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-common-2:9.2.725-1.amzn2023.0.1  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.725-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |
|  xxd-2:9.2.725-1.amzn2023.0.1  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260720.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel6.18-1:6.18.38-73.137.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260720.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  acl-2.4.0-1.amzn2023.0.1  |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-40.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.1  |
|  bind-license-32:9.18.50-1.amzn2023.0.1  |
|  bind-utils-32:9.18.50-1.amzn2023.0.1  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.11-0.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel6.12-tools-1:6.12.94-123.190.amzn2023  |
|  kernel6.12-1:6.12.94-123.190.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.4  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  rust-toolset-srpm-macros-1.97.0-1.amzn2023.0.1  |
|  sssd-client-2.9.4-1.amzn2023.0.4  |
|  sssd-common-2.9.4-1.amzn2023.0.4  |
|  sssd-kcm-2.9.4-1.amzn2023.0.4  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.4  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-common-2:9.2.725-1.amzn2023.0.1  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.725-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |
|  xxd-2:9.2.725-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260720.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel6.12-1:6.12.94-123.190.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260720.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  acl-2.4.0-1.amzn2023.0.1  |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-40.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.1  |
|  bind-license-32:9.18.50-1.amzn2023.0.1  |
|  bind-utils-32:9.18.50-1.amzn2023.0.1  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.11-0.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel-tools-1:6.1.176-221.367.amzn2023  |
|  kernel-1:6.1.176-221.367.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.4  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.4  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  rust-toolset-srpm-macros-1.97.0-1.amzn2023.0.1  |
|  sssd-client-2.9.4-1.amzn2023.0.4  |
|  sssd-common-2.9.4-1.amzn2023.0.4  |
|  sssd-kcm-2.9.4-1.amzn2023.0.4  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.4  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-common-2:9.2.725-1.amzn2023.0.1  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.725-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |
|  xxd-2:9.2.725-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260720.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-ec2-net-utils-2.7.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.12.20260720-0.amzn2023  |
|  dnf-plugin-support-info-2.0.0-1.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.3  |
|  dracut-102-3.amzn2023.0.3  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.5  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-locale-source-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  kernel-livepatch-repo-s3-2023.12.20260720-0.amzn2023  |
|  kernel-1:6.1.176-221.367.amzn2023  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libfdisk-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  python3-elementpath-2.3.2-2.amzn2023  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-lxml-4.7.1-3.amzn2023.0.3  |
|  python3-supportinfo-1.0.0-1.amzn2023  |
|  python3-xmlschema-1.4.2-1.amzn2023.0.2  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |
|  util-linux-core-2.37.4-1.amzn2023.0.6  |
|  util-linux-2.37.4-1.amzn2023.0.6  |
|  vim-data-2:9.2.725-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.725-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.12.20260720.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260720-0.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  python3-libs-3.9.25-1.amzn2023.0.8  |
|  python3-3.9.25-1.amzn2023.0.8  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |

### Minimal Container
<a name="amis-2023.12.20260720.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260720-0.amzn2023  |
|  glib2-2.82.2-770.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.5  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.5  |
|  glibc-2.34-231.amzn2023.0.5  |
|  krb5-libs-1.21.3-8.amzn2023.0.1  |
|  libacl-2.4.0-1.amzn2023.0.1  |
|  libblkid-2.37.4-1.amzn2023.0.6  |
|  libmount-2.37.4-1.amzn2023.0.6  |
|  libsmartcols-2.37.4-1.amzn2023.0.6  |
|  libuuid-2.37.4-1.amzn2023.0.6  |
|  system-release-2023.12.20260720-0.amzn2023  |
|  tzdata-2026c-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.12.20260720.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
