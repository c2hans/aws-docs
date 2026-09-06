---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260202.html
---

# Amazon Linux 2023 version 2023.10.20260202 release notes
<a name="relnotes-2023.10.20260202"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260202.

**Contents**
+ [Release Summary](#release-summary-2023.10.20260202)
+ [Repository Updates](#repository-updates-2023.10.20260202)
  + [Core New Packages](#amis-2023.10.20260202.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260202.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.10.20260202.Kernel-livepatch-New-Packages)
+ [Image Updates](#ami-updates-2023.10.20260202)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260202.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260202.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260202.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260202.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.10.20260202.Default-Container)
  + [Minimal Container](#amis-2023.10.20260202.Minimal-Container)
+ [Contact us](#amis-2023.10.20260202.contact-us)

## Release Summary
<a name="release-summary-2023.10.20260202"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ Node.js 20 will reach its **End-of-Life in three months**, on 30 April 2026. After this date, no security updates will be provided for it. Customers are advised to migrate to either Node.js version 22 or 24. Information about package names and run-time version management can be found in the documentation, [Managing Node.js on Amazon Linux 2023]( https://docs.aws.amazon.com/linux/al2023/ug/nodejs.html).
+ Due to a tooling regression, AL2023 AMIs for releases `2023.10.20260105` and `2023.10.20260120` had `reflink` disabled on the root xfs file system. This has been fixed in the current release.
+ With glibc version `glibc-2.34-231.amzn2023.0.3`, we bring support for enabling transparent huge pages via the glibc tunable framework from glibc v2.35 to AL2023. For some workloads, specifically those with a large memory working set and frequent random memory accesses, performance improvements of up to 10% can be achieved. This feature is not enabled by default because other workloads, such as some databases, see slowdowns when using it. The feature can be enabled by setting the environment variable `GLIBC_TUNABLES=glibc.malloc.hugetlb=1`.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260202"></a>

### Core New Packages
<a name="amis-2023.10.20260202.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.2  |
|  php8.3-pecl-memcached-3.4.0-1.amzn2023.0.1  |
|  php8.4-pecl-memcached-3.4.0-1.amzn2023.0.1  |
|  php8.5-pecl-apcu-5.1.28-1.amzn2023.0.1  |
|  php8.5-pecl-igbinary-3.2.16-4.amzn2023.0.1  |
|  php8.5-pecl-memcached-3.4.0-1.amzn2023.0.1  |
|  php8.5-pecl-msgpack-3.0.0-3.amzn2023.0.1  |
|  php8.5-pecl-redis6-6.3.0-1.amzn2023.0.1  |
|  python3.13-importlib-metadata-8.6.1-1.amzn2023.0.2  |
|  python3.13-tomli-2.2.1-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.10.20260202.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.13.29-1.amzn2023.0.5  |
|  amazon-ecr-credential-helper-0.11.0-3.amzn2023  |
|  appstream-data-2023-102.amzn2023  |
|  capstone-4.0.2-9.amzn2023.0.4  |
|  chrony-4.3-1.amzn2023.0.6  |
|  cmake-3.22.2-1.amzn2023.0.6  |
|  cni-plugins-1.7.1-1.amzn2023.0.5  |
|  containerd-2.1.5-1.amzn2023.0.5  |
|  firefox-140.7.0-1.amzn2023.0.1  |
|  freerdp-3.6.3-1.amzn2023.0.2  |
|  glibc-2.34-231.amzn2023.0.3  |
|  gnulib-0-43.20220212git.amzn2023.0.3  |
|  golang-1.24.12-1.amzn2023.0.1  |
|  golist-0.10.1-11.amzn2023.0.6  |
|  java-1.8.0-amazon-corretto-1.8.0\_482.b08-1.amzn2023  |
|  java-11-amazon-corretto-11.0.30\+7-1.amzn2023  |
|  java-17-amazon-corretto-17.0.18\+9-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.10\+7-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.2\+10-1.amzn2023.1  |
|  kernel-6.1.161-183.298.amzn2023  |
|  kernel6.12-6.12.66-88.122.amzn2023  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libplist-2.2.0-3.amzn2023.0.3  |
|  libpng-1.6.37-10.amzn2023.0.9  |
|  libsoup-2.72.0-6.amzn2023.0.10  |
|  libsoup3-3.6.5-55.amzn2023  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  mount-s3-1.22.0-1.amzn2023  |
|  nerdctl-2.2.1-1.amzn2023.0.2  |
|  nodejs20-20.20.0-1.amzn2023.0.1  |
|  nodejs22-22.22.0-1.amzn2023.0.1  |
|  nodejs24-24.13.0-1.amzn2023.0.1  |
|  nvidia-release-2023-3.amzn2023  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.8  |
|  openssl-3.2.2-1.amzn2023.0.4  |
|  python-filelock-3.3.1-1.amzn2023.0.2  |
|  python-pip-21.3.1-2.amzn2023.0.16  |
|  python-pyasn1-0.4.8-4.amzn2023.0.3  |
|  python-urllib3-1.25.10-5.amzn2023.0.6  |
|  python3.11-pip-22.3.1-2.amzn2023.0.10  |
|  python3.12-pip-23.2.1-4.amzn2023.0.7  |
|  python3.13-pip-24.2-259.amzn2023.0.3  |
|  python3.13-wheel-0.43.0-104.amzn2023  |
|  python3.13-zipp-3.21.0-1.amzn2023.0.2  |
|  qpdf-10.6.3-4.amzn2023.0.5  |
|  runfinch-finch-1.14.1-1.amzn2023.0.1  |
|  soci-snapshotter-0.12.0-1.amzn2023.0.3  |
|  system-release-2023.10.20260202-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.1  |

### Kernel-livepatch New Packages
<a name="amis-2023.10.20260202.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.158-178.288-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.158-180.294-1.0-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.10.20260202"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260202.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-chrony-config-4.3-1.amzn2023.0.6  |
|  amazon-linux-repo-s3-2023.10.20260202-0.amzn2023  |
|  chrony-4.3-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.3  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.3  |
|  glibc-locale-source-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  kernel-libbpf-1:6.1.161-183.298.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260202-0.amzn2023  |
|  kernel-tools-1:6.1.161-183.298.amzn2023  |
|  kernel-1:6.1.161-183.298.amzn2023  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  openssl-1:3.2.2-1.amzn2023.0.4  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.16  |
|  python3-urllib3-1.25.10-5.amzn2023.0.6  |
|  system-release-2023.10.20260202-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260202.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-chrony-config-4.3-1.amzn2023.0.6  |
|  amazon-linux-repo-s3-2023.10.20260202-0.amzn2023  |
|  chrony-4.3-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.3  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-locale-source-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  kernel-libbpf-1:6.1.161-183.298.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260202-0.amzn2023  |
|  kernel-1:6.1.161-183.298.amzn2023  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  openssl-1:3.2.2-1.amzn2023.0.4  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.16  |
|  python3-urllib3-1.25.10-5.amzn2023.0.6  |
|  system-release-2023.10.20260202-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260202.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-chrony-config-4.3-1.amzn2023.0.6  |
|  amazon-linux-repo-s3-2023.10.20260202-0.amzn2023  |
|  chrony-4.3-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.3  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-gconv-extra-2.34-231.amzn2023.0.3  |
|  glibc-locale-source-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.10.20260202-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.66-88.122.amzn2023  |
|  kernel6.12-tools-1:6.12.66-88.122.amzn2023  |
|  kernel6.12-1:6.12.66-88.122.amzn2023  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  openssl-1:3.2.2-1.amzn2023.0.4  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.16  |
|  python3-urllib3-1.25.10-5.amzn2023.0.6  |
|  system-release-2023.10.20260202-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260202.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-chrony-config-4.3-1.amzn2023.0.6  |
|  amazon-linux-repo-s3-2023.10.20260202-0.amzn2023  |
|  chrony-4.3-1.amzn2023.0.6  |
|  glibc-all-langpacks-2.34-231.amzn2023.0.3  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-locale-source-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.10.20260202-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.66-88.122.amzn2023  |
|  kernel6.12-1:6.12.66-88.122.amzn2023  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  openssl-1:3.2.2-1.amzn2023.0.4  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.16  |
|  python3-urllib3-1.25.10-5.amzn2023.0.6  |
|  system-release-2023.10.20260202-0.amzn2023  |

### Default Container
<a name="amis-2023.10.20260202.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260202-0.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.16  |
|  system-release-2023.10.20260202-0.amzn2023  |

### Minimal Container
<a name="amis-2023.10.20260202.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260202-0.amzn2023  |
|  glibc-common-2.34-231.amzn2023.0.3  |
|  glibc-minimal-langpack-2.34-231.amzn2023.0.3  |
|  glibc-2.34-231.amzn2023.0.3  |
|  libcap-2.73-1.amzn2023.0.6  |
|  libtasn1-4.19.0-1.amzn2023.0.6  |
|  libxml2-2.10.4-1.amzn2023.0.17  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.4  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.4  |
|  system-release-2023.10.20260202-0.amzn2023  |

## Contact us
<a name="amis-2023.10.20260202.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
