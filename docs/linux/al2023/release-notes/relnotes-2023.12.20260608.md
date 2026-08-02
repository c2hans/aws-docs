---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260608.html
---

# Amazon Linux 2023 version 2023.12.20260608 release notes
<a name="relnotes-2023.12.20260608"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260608.

**Contents**
+ [Known issue: Docker networking regression](#docker-regression-warning-2023.12.20260608)
  + [Solution and Mitigation](#docker-regression-mitigation-2023.12.20260608)
+ [Release Summary](#release-summary-2023.12.20260608)
+ [Repository Updates](#repository-updates-2023.12.20260608)
  + [Core New Packages](#amis-2023.12.20260608.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260608.Core-Updated-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260608.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260608)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260608.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260608.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260608.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260608.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260608.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260608.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260608.Default-Container)
  + [Minimal Container](#amis-2023.12.20260608.Minimal-Container)
+ [Contact us](#amis-2023.12.20260608.contact-us)

## Known issue: Docker networking regression
<a name="docker-regression-warning-2023.12.20260608"></a>

**Warning**
 The `docker-25.0.16-1.amzn2023.0.1` package included in this release contains a regression in libnetwork sandbox route conflict validation. When a container already connected to the default bridge network is connected to a second bridge network, Docker incorrectly rejects it with a route conflict error.

### Solution and Mitigation
<a name="docker-regression-mitigation-2023.12.20260608"></a>

If you are affected by this issue, you can downgrade to the previous docker version:

1. Downgrade docker:

   ```
   sudo dnf downgrade docker-25.0.14-1.amzn2023.0.4
   ```

1. Restart the docker service:

   ```
   sudo systemctl restart docker
   ```

## Release Summary
<a name="release-summary-2023.12.20260608"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `python3.14-pip`: We ship pip 26.1 for python 3.14. This tool version now allows you to configure update delays for package installations, which is useful to avoid supply chain risks. The delay can be set to delay updates by for example one day via the `--uploaded-prior-to="P1D"` flag, or in the configuration file `/etc/pip.conf` via `uploaded-prior-to = P1D`.
+  MariaDB 11.8 has been added. See official [MariaDB documentation](https://mariadb.com/docs/release-notes/community-server/11.8/what-is-mariadb-118) for a list of changes and improvements in this version.
+  NSS has been rebased to version 3.112. This release adds new support for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA), and hybrid support for MLKEM1024 key encapsulation mechanism.
+  GnuTLS has been rebased to version 3.8.10. This release adds a number of features including support for new post-quantum cryptography (PQC) standards:
  + Support for ML-KEM hybrid key exchange algorithms
  + Support for ML-DSA-44, ML-DSA-65, and ML-DSA-87 signature algorithms for TLS communications
+  crypto-policies now supports enabling post-quantum cryptography in LEGACY, DEFAULT, FUTURE, and FIPS cryptographic policies. Apply the PQ sub-policy to enable post-quantum cryptography, for example: `sudo update-crypto-policies --set DEFAULT:PQ`

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260608"></a>

### Core New Packages
<a name="amis-2023.12.20260608.Core-New-Packages"></a>

This section provides details about Core New Packages.

|  |
| --- |
|  autoconf-latest-2.71-8.amzn2023.0.1  |
|  mariadb118-11.8.8-1.amzn2023.0.1  |
|  perl-Crypt-URandom-0.55-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.12.20260608.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

|  |
| --- |
|  7zip-26.01-14.amzn2023.0.1  |
|  R-4.5.3-1.amzn2023.0.1  |
|  amazon-efs-utils-3.1.2-1.amzn2023  |
|  amazon-ssm-agent-3.3.4515.0-1.amzn2023  |
|  bcc-0.35.0-4.amzn2023.0.2  |
|  bouncycastle-1.70-4.amzn2023.0.7  |
|  capstone-4.0.2-9.amzn2023.0.5  |
|  composer-2.9.8-1.amzn2023.0.1  |
|  containerd-2.2.4-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.2-1.amzn2023.0.1  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  device-mapper-persistent-data-0.9.0-7.amzn2023.0.4  |
|  docker-25.0.16-1.amzn2023.0.1  |
|  dotnet10.0-10.0.108-1.amzn2023.0.1  |
|  dotnet8.0-8.0.127-1.amzn2023.0.1  |
|  dotnet9.0-9.0.117-1.amzn2023.0.2  |
|  ecs-init-1.103.2-1.amzn2023  |
|  enchant-1.6.0-27.amzn2023.0.2  |
|  enchant2-2.8.1-2.amzn2023.0.2  |
|  firefox-140.11.0-1.amzn2023.0.1  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-2.06-61.amzn2023.0.22  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.6  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-6.1.174-217.345.amzn2023  |
|  kernel6.12-6.12.90-120.164.amzn2023  |
|  kernel6.18-6.18.33-63.124.amzn2023  |
|  libheif-1.19.8-1.amzn2023.0.5  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  libsoup3-3.6.6-58.amzn2023  |
|  libssh-0.10.6-1.amzn2023.0.7  |
|  libssh2-1.10.0-1.amzn2023.0.4  |
|  libvoikko-4.3.3-1.amzn2023.0.1  |
|  mariadb1011-10.11.18-1.amzn2023.0.1  |
|  mariadb114-11.4.12-1.amzn2023.0.1  |
|  memcached-1.6.42-2.amzn2023.0.1  |
|  mysql-selinux-1.0.14-2.amzn2023.0.1  |
|  nerdctl-2.2.2-1.amzn2023.0.3  |
|  nginx-1.30.2-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.7  |
|  nodejs22-22.22.3-1.amzn2023.0.1  |
|  nodejs24-24.16.0-1.amzn2023.0.1  |
|  nss-3.112.0-8.amzn2023.0.2  |
|  papers-47.0-12.amzn2023  |
|  perl-5.32.1-477.amzn2023.0.9  |
|  perl-Archive-Tar-3.04-522.amzn2023.0.3  |
|  perl-Crypt-PasswdMD5-1.4.1-1.amzn2023.0.3  |
|  perl-HTTP-Daemon-6.16-1.amzn2023.0.1  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.2  |
|  perl-Template-Toolkit-3.009-3.amzn2023.0.4  |
|  perl-XML-LibXML-2.0210-7.amzn2023.0.3  |
|  perl-YAML-Syck-1.37-1.amzn2023.0.3  |
|  perl-libwww-perl-6.58-1.amzn2023.0.3  |
|  pigz-2.5-1.amzn2023.0.4  |
|  postgresql15-15.18-1.amzn2023.0.1  |
|  postgresql16-16.14-1.amzn2023.0.1  |
|  postgresql17-17.10-1.amzn2023.0.1  |
|  postgresql18-18.4-1.amzn2023.0.1  |
|  python3.12-3.12.13-2.amzn2023.0.2  |
|  python3.13-3.13.13-1.amzn2023.0.3  |
|  python3.14-3.14.5-1.amzn2023.0.1  |
|  python3.14-pip-26.1.1-1.amzn2023.0.1  |
|  python3.9-3.9.25-1.amzn2023.0.6  |
|  radvd-2.19-2.amzn2023.0.3  |
|  rclone-1.74.2-80.amzn2023  |
|  rsync-3.4.0-1.amzn2023.0.4  |
|  ruby3.4-3.4.8-27.amzn2023.0.6  |
|  ruby4.0-4.0.1-32.amzn2023.0.2  |
|  runc-1.3.5-1.amzn2023.0.2  |
|  runfinch-finch-1.17.1-1.amzn2023.0.2  |
|  sendmail-8.18.2-2.amzn2023.0.1  |
|  system-release-2023.12.20260608-0.amzn2023  |
|  tomcat10-10.1.55-1.amzn2023.0.1  |
|  tomcat9-9.0.118-1.amzn2023.0.1  |
|  voikko-fi-2.4-3.amzn2023.0.3  |
|  vorbis-tools-1.4.2-2.amzn2023.0.4  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.10  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.5  |
|  zip-3.0-28.amzn2023.0.3  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260608.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

|  |
| --- |
|  kernel-livepatch-6.18.25-57.109-1.0-3.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20260608"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260608.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  amazon-ssm-agent-3.3.4515.0-1.amzn2023  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.4  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel6.18-tools-1:6.18.33-63.124.amzn2023  |
|  kernel6.18-1:6.18.33-63.124.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  nspr-4.36.0-8.amzn2023.0.2  |
|  nss-softokn-freebl-3.112.0-8.amzn2023.0.2  |
|  nss-softokn-3.112.0-8.amzn2023.0.2  |
|  nss-sysinit-3.112.0-8.amzn2023.0.2  |
|  nss-util-3.112.0-8.amzn2023.0.2  |
|  nss-3.112.0-8.amzn2023.0.2  |
|  perl-AutoLoader-5.74-477.amzn2023.0.9  |
|  perl-B-1.80-477.amzn2023.0.9  |
|  perl-Class-Struct-0.66-477.amzn2023.0.9  |
|  perl-DynaLoader-1.47-477.amzn2023.0.9  |
|  perl-Errno-1.30-477.amzn2023.0.9  |
|  perl-Fcntl-1.13-477.amzn2023.0.9  |
|  perl-File-Basename-2.85-477.amzn2023.0.9  |
|  perl-File-stat-1.09-477.amzn2023.0.9  |
|  perl-FileHandle-2.03-477.amzn2023.0.9  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.9  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.2  |
|  perl-IO-1.43-477.amzn2023.0.9  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.9  |
|  perl-POSIX-1.94-477.amzn2023.0.9  |
|  perl-SelectSaver-1.02-477.amzn2023.0.9  |
|  perl-Symbol-1.08-477.amzn2023.0.9  |
|  perl-base-2.27-477.amzn2023.0.9  |
|  perl-if-0.60.800-477.amzn2023.0.9  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.9  |
|  perl-libs-4:5.32.1-477.amzn2023.0.9  |
|  perl-mro-1.23-477.amzn2023.0.9  |
|  perl-overload-1.31-477.amzn2023.0.9  |
|  perl-overloading-0.02-477.amzn2023.0.9  |
|  perl-subs-1.03-477.amzn2023.0.9  |
|  perl-vars-1.05-477.amzn2023.0.9  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  rsync-3.4.0-1.amzn2023.0.4  |
|  system-release-2023.12.20260608-0.amzn2023  |
|  zip-3.0-28.amzn2023.0.3  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260608.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel6.18-1:6.18.33-63.124.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  system-release-2023.12.20260608-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260608.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  amazon-ssm-agent-3.3.4515.0-1.amzn2023  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.4  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel6.12-tools-1:6.12.90-120.164.amzn2023  |
|  kernel6.12-1:6.12.90-120.164.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  nspr-4.36.0-8.amzn2023.0.2  |
|  nss-softokn-freebl-3.112.0-8.amzn2023.0.2  |
|  nss-softokn-3.112.0-8.amzn2023.0.2  |
|  nss-sysinit-3.112.0-8.amzn2023.0.2  |
|  nss-util-3.112.0-8.amzn2023.0.2  |
|  nss-3.112.0-8.amzn2023.0.2  |
|  perl-AutoLoader-5.74-477.amzn2023.0.9  |
|  perl-B-1.80-477.amzn2023.0.9  |
|  perl-Class-Struct-0.66-477.amzn2023.0.9  |
|  perl-DynaLoader-1.47-477.amzn2023.0.9  |
|  perl-Errno-1.30-477.amzn2023.0.9  |
|  perl-Fcntl-1.13-477.amzn2023.0.9  |
|  perl-File-Basename-2.85-477.amzn2023.0.9  |
|  perl-File-stat-1.09-477.amzn2023.0.9  |
|  perl-FileHandle-2.03-477.amzn2023.0.9  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.9  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.2  |
|  perl-IO-1.43-477.amzn2023.0.9  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.9  |
|  perl-POSIX-1.94-477.amzn2023.0.9  |
|  perl-SelectSaver-1.02-477.amzn2023.0.9  |
|  perl-Symbol-1.08-477.amzn2023.0.9  |
|  perl-base-2.27-477.amzn2023.0.9  |
|  perl-if-0.60.800-477.amzn2023.0.9  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.9  |
|  perl-libs-4:5.32.1-477.amzn2023.0.9  |
|  perl-mro-1.23-477.amzn2023.0.9  |
|  perl-overload-1.31-477.amzn2023.0.9  |
|  perl-overloading-0.02-477.amzn2023.0.9  |
|  perl-subs-1.03-477.amzn2023.0.9  |
|  perl-vars-1.05-477.amzn2023.0.9  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  rsync-3.4.0-1.amzn2023.0.4  |
|  system-release-2023.12.20260608-0.amzn2023  |
|  zip-3.0-28.amzn2023.0.3  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260608.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel6.12-1:6.12.90-120.164.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  system-release-2023.12.20260608-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260608.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  amazon-ssm-agent-3.3.4515.0-1.amzn2023  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.4  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel-tools-1:6.1.174-217.345.amzn2023  |
|  kernel-1:6.1.174-217.345.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  nspr-4.36.0-8.amzn2023.0.2  |
|  nss-softokn-freebl-3.112.0-8.amzn2023.0.2  |
|  nss-softokn-3.112.0-8.amzn2023.0.2  |
|  nss-sysinit-3.112.0-8.amzn2023.0.2  |
|  nss-util-3.112.0-8.amzn2023.0.2  |
|  nss-3.112.0-8.amzn2023.0.2  |
|  perl-AutoLoader-5.74-477.amzn2023.0.9  |
|  perl-B-1.80-477.amzn2023.0.9  |
|  perl-Class-Struct-0.66-477.amzn2023.0.9  |
|  perl-DynaLoader-1.47-477.amzn2023.0.9  |
|  perl-Errno-1.30-477.amzn2023.0.9  |
|  perl-Fcntl-1.13-477.amzn2023.0.9  |
|  perl-File-Basename-2.85-477.amzn2023.0.9  |
|  perl-File-stat-1.09-477.amzn2023.0.9  |
|  perl-FileHandle-2.03-477.amzn2023.0.9  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.9  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.2  |
|  perl-IO-1.43-477.amzn2023.0.9  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.9  |
|  perl-POSIX-1.94-477.amzn2023.0.9  |
|  perl-SelectSaver-1.02-477.amzn2023.0.9  |
|  perl-Symbol-1.08-477.amzn2023.0.9  |
|  perl-base-2.27-477.amzn2023.0.9  |
|  perl-if-0.60.800-477.amzn2023.0.9  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.9  |
|  perl-libs-4:5.32.1-477.amzn2023.0.9  |
|  perl-mro-1.23-477.amzn2023.0.9  |
|  perl-overload-1.31-477.amzn2023.0.9  |
|  perl-overloading-0.02-477.amzn2023.0.9  |
|  perl-subs-1.03-477.amzn2023.0.9  |
|  perl-vars-1.05-477.amzn2023.0.9  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  rsync-3.4.0-1.amzn2023.0.4  |
|  system-release-2023.12.20260608-0.amzn2023  |
|  zip-3.0-28.amzn2023.0.3  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260608.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

|  |
| --- |
|  amazon-linux-repo-s3-2023.12.20260608-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  gnutls-3.8.10-4.amzn2023.0.2  |
|  grub2-common-1:2.06-61.amzn2023.0.22  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.22  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.22  |
|  grub2-tools-1:2.06-61.amzn2023.0.22  |
|  jq-1.8.1-59.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260608-0.amzn2023  |
|  kernel-1:6.1.174-217.345.amzn2023  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  system-release-2023.12.20260608-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20260608.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260608-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  python3-libs-3.9.25-1.amzn2023.0.6  |
|  python3-3.9.25-1.amzn2023.0.6  |
|  system-release-2023.12.20260608-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260608.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260608-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.4  |
|  libsolv-0.7.22-1.amzn2023.0.4  |
|  system-release-2023.12.20260608-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260608.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
