---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20251027.html
---

# Amazon Linux 2023 version 2023.9.20251027 release notes
<a name="relnotes-2023.9.20251027"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.9.20251027.

**Contents**
+ [Release Summary](#release-summary-2023.9.20251027)
+ [Repository Updates](#repository-updates-2023.9.20251027)
  + [Core New Packages](#amis-2023.9.20251027.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.9.20251027.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.9.20251027.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.9.20251027.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.9.20251027)
  + [Default Kernel 6.1 AMI](#amis-2023.9.20251027.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.9.20251027.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.9.20251027.Default-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.9.20251027.Default-Container)
  + [Minimal Container](#amis-2023.9.20251027.Minimal-Container)
+ [Contact us](#amis-2023.9.20251027.contact-us)

## Release Summary
<a name="release-summary-2023.9.20251027"></a>

This release represents an update to the 9th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `sssd-2.9.4-1.amzn2023.0.3` will now disable the `an2ln` Kerberos plugin in SSSD localauth configuration to prevent unexpected principal mappings (CVE-2025-11561)
+  p7zip is no longer maintained upstream and has been replaced by 7zip to mitigate several high importance CVEs. Upgrading to the latest version of p7zip will replace it with 7zip-standalone which provides the same functionality.
+  The package apr-util-lmdb has been added as a replacement for the package apr-util-bdb.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.9.20251027"></a>

### Core New Packages
<a name="amis-2023.9.20251027.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  7zip-25.01-8.amzn2023.0.1  |
|  libheif-1.19.8-1.amzn2023.0.1  |
|  llvm20-20.1.8-4.amzn2023.0.1  |
|  rust-below-0.11.0-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.9.20251027.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  GraphicsMagick-1.3.45-1.amzn2023.0.2  |
|  ImageMagick-6.9.13.29-1.amzn2023.0.2  |
|  apr-util-1.6.3-1.amzn2023.0.2  |
|  audit-3.1.5-1.amzn2023.0.2  |
|  boost-1.75.0-4.amzn2023.0.4  |
|  ecs-init-1.100.0-1.amzn2023  |
|  firefox-140.4.0-1.amzn2023.0.2  |
|  gi-docgen-2024.1-44.amzn2023  |
|  go-rpm-macros-3.8.0-1.amzn2023.0.1  |
|  golang-1.24.8-1.amzn2023.0.1  |
|  grub2-2.06-61.amzn2023.0.20  |
|  httpd-2.4.65-1.amzn2023.0.2  |
|  java-1.8.0-amazon-corretto-1.8.0\_472.b08-1.amzn2023  |
|  java-11-amazon-corretto-11.0.29\+7-1.amzn2023  |
|  java-17-amazon-corretto-17.0.17\+10-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.9\+10-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.1\+8-1.amzn2023.1  |
|  kernel-6.1.156-177.286.amzn2023  |
|  kernel6.12-6.12.53-69.119.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  libsoup3-3.6.5-52.amzn2023  |
|  libxslt-1.1.43-1.amzn2023.0.3  |
|  maven-shared-utils-3.3.4-4.amzn2023.0.4  |
|  mod\_auth\_openidc-2.4.16.11-1.amzn2023.0.1  |
|  p7zip-16.02-30.amzn2023.0.2  |
|  perl-Math-BigInt-FastCalc-0.501.400-3.amzn2023.0.1  |
|  perl-YAML-Syck-1.36-1.amzn2023.0.1  |
|  php8.3-pecl-apcu-5.1.27-1.amzn2023.0.1  |
|  php8.4-pecl-apcu-5.1.27-1.amzn2023.0.1  |
|  python-markdown-3.3.4-2.amzn2023.0.4  |
|  python-psycopg2-2.9.10-8.amzn2023.0.1  |
|  python3.11-3.11.14-1.amzn2023.0.1  |
|  python3.12-3.12.12-2.amzn2023  |
|  python3.13-3.13.3-3.amzn2023.0.7  |
|  python3.9-3.9.24-1.amzn2023.0.3  |
|  samba-4.17.12-1.amzn2023.0.3  |
|  squid-6.13-1.amzn2023.0.3  |
|  sssd-2.9.4-1.amzn2023.0.3  |
|  system-release-2023.9.20251027-0.amzn2023  |
|  xmlrpc-c-1.51.08-2.amzn2023.0.2  |

### Kernel-livepatch New Packages
<a name="amis-2023.9.20251027.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.12.46-66.121-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.9.20251027.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.141-167.250-1.0-7.amzn2023  |
|  kernel-livepatch-6.1.144-170.251-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.147-172.259-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.147-172.266-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.148-173.267-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.150-174.273-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.37-61.105-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.40-63.107-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.40-63.114-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.40-64.114-1.0-2.amzn2023  |

## Image Updates
<a name="ami-updates-2023.9.20251027"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.9.20251027.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251027-0.amzn2023  |
|  audit-libs-3.1.5-1.amzn2023.0.2  |
|  audit-3.1.5-1.amzn2023.0.2  |
|  boost-filesystem-1.75.0-4.amzn2023.0.4  |
|  boost-system-1.75.0-4.amzn2023.0.4  |
|  boost-thread-1.75.0-4.amzn2023.0.4  |
|  go-srpm-macros-3.8.0-1.amzn2023.0.1  |
|  grub2-common-1:2.06-61.amzn2023.0.20  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.20  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-1:2.06-61.amzn2023.0.20  |
|  kernel-libbpf-1:6.1.156-177.286.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251027-0.amzn2023  |
|  kernel-tools-1:6.1.156-177.286.amzn2023  |
|  kernel-1:6.1.156-177.286.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.3  |
|  python3-audit-3.1.5-1.amzn2023.0.2  |
|  python3-hawkey-0.69.0-8.amzn2023.0.6  |
|  python3-libdnf-0.69.0-8.amzn2023.0.6  |
|  python3-libs-3.9.24-1.amzn2023.0.3  |
|  python3-3.9.24-1.amzn2023.0.3  |
|  sssd-client-2.9.4-1.amzn2023.0.3  |
|  sssd-common-2.9.4-1.amzn2023.0.3  |
|  sssd-kcm-2.9.4-1.amzn2023.0.3  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.3  |
|  system-release-2023.9.20251027-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.9.20251027.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251027-0.amzn2023  |
|  audit-libs-3.1.5-1.amzn2023.0.2  |
|  audit-3.1.5-1.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.20  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.20  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-1:2.06-61.amzn2023.0.20  |
|  kernel-libbpf-1:6.1.156-177.286.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251027-0.amzn2023  |
|  kernel-1:6.1.156-177.286.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  python3-audit-3.1.5-1.amzn2023.0.2  |
|  python3-hawkey-0.69.0-8.amzn2023.0.6  |
|  python3-libdnf-0.69.0-8.amzn2023.0.6  |
|  python3-libs-3.9.24-1.amzn2023.0.3  |
|  python3-3.9.24-1.amzn2023.0.3  |
|  system-release-2023.9.20251027-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.9.20251027.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251027-0.amzn2023  |
|  audit-libs-3.1.5-1.amzn2023.0.2  |
|  audit-3.1.5-1.amzn2023.0.2  |
|  boost-filesystem-1.75.0-4.amzn2023.0.4  |
|  boost-system-1.75.0-4.amzn2023.0.4  |
|  boost-thread-1.75.0-4.amzn2023.0.4  |
|  go-srpm-macros-3.8.0-1.amzn2023.0.1  |
|  grub2-common-1:2.06-61.amzn2023.0.20  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.20  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.20  |
|  grub2-tools-1:2.06-61.amzn2023.0.20  |
|  kernel-livepatch-repo-s3-2023.9.20251027-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.53-69.119.amzn2023  |
|  kernel6.12-tools-1:6.12.53-69.119.amzn2023  |
|  kernel6.12-1:6.12.53-69.119.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  libsss\_certmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_idmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_nss\_idmap-2.9.4-1.amzn2023.0.3  |
|  libsss\_sudo-2.9.4-1.amzn2023.0.3  |
|  python3-audit-3.1.5-1.amzn2023.0.2  |
|  python3-hawkey-0.69.0-8.amzn2023.0.6  |
|  python3-libdnf-0.69.0-8.amzn2023.0.6  |
|  python3-libs-3.9.24-1.amzn2023.0.3  |
|  python3-3.9.24-1.amzn2023.0.3  |
|  sssd-client-2.9.4-1.amzn2023.0.3  |
|  sssd-common-2.9.4-1.amzn2023.0.3  |
|  sssd-kcm-2.9.4-1.amzn2023.0.3  |
|  sssd-nfs-idmap-2.9.4-1.amzn2023.0.3  |
|  system-release-2023.9.20251027-0.amzn2023  |

### Default Container
<a name="amis-2023.9.20251027.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251027-0.amzn2023  |
|  audit-libs-3.1.5-1.amzn2023.0.2  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  python3-hawkey-0.69.0-8.amzn2023.0.6  |
|  python3-libdnf-0.69.0-8.amzn2023.0.6  |
|  python3-libs-3.9.24-1.amzn2023.0.3  |
|  python3-3.9.24-1.amzn2023.0.3  |
|  system-release-2023.9.20251027-0.amzn2023  |

### Minimal Container
<a name="amis-2023.9.20251027.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251027-0.amzn2023  |
|  audit-libs-3.1.5-1.amzn2023.0.2  |
|  libdnf-0.69.0-8.amzn2023.0.6  |
|  librepo-1.14.5-2.amzn2023.0.2  |
|  system-release-2023.9.20251027-0.amzn2023  |

## Contact us
<a name="amis-2023.9.20251027.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
