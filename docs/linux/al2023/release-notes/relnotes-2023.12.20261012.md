---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261012.html
---

# Amazon Linux 2023 version 2023.12.20261012 release notes
<a name="relnotes-2023.12.20261012"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261012.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261012)
+ [Repository Updates](#repository-updates-2023.12.20261012)
  + [Core Updated Packages](#amis-2023.12.20261012.Core-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20261012.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261012)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261012.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261012.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261012.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261012.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261012.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261012.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261012.Default-Container)
  + [Minimal Container](#amis-2023.12.20261012.Minimal-Container)
+ [Contact us](#amis-2023.12.20261012.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261012"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261012"></a>

### Core Updated Packages
<a name="amis-2023.12.20261012.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  amazon-ecr-credential-helper-0.12.0-4.amzn2023  |
|  amazon-efs-utils-3.3.3-1.amzn2023  |
|  amazon-ssm-agent-3.3.5390.0-1.amzn2023  |
|  apache-ivy-2.5.1-1.amzn2023.0.3  |
|  containerd-2.3.5-1.amzn2023.0.1  |
|  device-mapper-persistent-data-0.9.0-7.amzn2023.0.5  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  docker-25.0.16-1.amzn2023.0.5  |
|  ecs-init-1.108.0-1.amzn2023  |
|  emacs-28.2-3.amzn2023.0.12  |
|  fetchmail-6.5.7-1.amzn2023.0.1  |
|  firefox-140.17.0-1.amzn2023.0.1  |
|  flatpak-builder-1.4.4-1.amzn2023.0.2  |
|  freerdp-3.32.1-1.amzn2023.0.1  |
|  glycin-1.1.2-12.amzn2023  |
|  hiredis-1.2.0-8.amzn2023.0.2  |
|  httpd-2.4.69-1.amzn2023.0.2  |
|  jackson-bom-2.21.7-1.amzn2023.0.1  |
|  jackson-core-2.21.7-1.amzn2023.0.1  |
|  jackson-databind-2.21.7-1.amzn2023.0.1  |
|  java-1.8.0-amazon-corretto-1.8.0\_504.b04-1.amzn2023  |
|  java-11-amazon-corretto-11.0.32\+12-1.amzn2023  |
|  java-17-amazon-corretto-17.0.20\+12-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.12\+12-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.4\+10-1.amzn2023.1  |
|  kernel-6.1.188-233.393.amzn2023  |
|  kernel6.12-6.12.111-136.204.amzn2023  |
|  kernel6.18-6.18.54-121.166.amzn2023  |
|  libX11-1.8.10-2.amzn2023.0.2  |
|  libXrender-0.9.11-6.amzn2023.0.2  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  libsoup-2.72.0-6.amzn2023.0.16  |
|  loupe-47.4-36.amzn2023  |
|  mariadb1011-10.11.19-1.amzn2023.0.1  |
|  mariadb114-11.4.13-1.amzn2023.0.1  |
|  mariadb118-11.8.9-1.amzn2023.0.1  |
|  mariadb123-12.3.3-2.amzn2023.0.1  |
|  mdevctl-1.1.0-4.amzn2023.0.5  |
|  mock-core-configs-39.2-1.amzn2023.0.3  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.12  |
|  opendkim-2.11.0-0.42.amzn2023  |
|  openssl-3.5.8-1.amzn2023.0.3  |
|  parted-3.4-2.amzn2023.0.3  |
|  perl-5.32.1-477.amzn2023.0.10  |
|  perl-DBI-1.653-1.amzn2023.0.1  |
|  perl-HTTP-Date-6.08-2.amzn2023.0.1  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.3  |
|  perl-Mojolicious-9.48-2.amzn2023.0.1  |
|  perl-Net-IDN-Encode-2.590-1.amzn2023.0.1  |
|  perl-Storable-3.37-522.amzn2023.0.3  |
|  php8.2-8.2.34-1.amzn2023.0.1  |
|  php8.3-8.3.35-1.amzn2023.0.1  |
|  php8.4-8.4.26-1.amzn2023.0.1  |
|  php8.5-8.5.11-1.amzn2023.0.1  |
|  python-hpack-4.0.0-2.amzn2023.0.3  |
|  python-jwcrypto-1.4.2-46.amzn2023.0.2  |
|  python-pip-21.3.1-2.amzn2023.0.22  |
|  python-pymongo-3.10.1-5.amzn2023.0.5  |
|  python-tornado-6.1.0-2.amzn2023.0.11  |
|  python-urllib3-1.25.10-5.amzn2023.0.9  |
|  python3.11-pip-22.3.1-2.amzn2023.0.15  |
|  python3.12-pip-23.2.1-4.amzn2023.0.12  |
|  python3.13-pip-24.2-259.amzn2023.0.9  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.6  |
|  python3.14-pip-26.1.1-1.amzn2023.0.4  |
|  rpcbind-1.2.6-0.amzn2023.0.3  |
|  rsyslog-8.2204.0-3.amzn2023.0.8  |
|  runc-1.4.3-1.amzn2023.0.1  |
|  rust-1.98.1-1.amzn2023  |
|  rust-askalono-cli-0.5.0-1.amzn2023.0.3  |
|  rust-below-0.11.0-1.amzn2023.0.4  |
|  rust-cargo-c-0.10.25-1.amzn2023.0.1  |
|  soci-snapshotter-0.16.0-1.amzn2023.0.1  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  tomcat-native-2.0.16-1.amzn2023.0.1  |
|  tomcat10-10.1.60-1.amzn2023.0.1  |
|  tomcat11-11.0.26-1.amzn2023.0.1  |
|  tomcat9-9.0.122-1.amzn2023.0.1  |
|  xdg-dbus-proxy-0.1.9-1.amzn2023.0.1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20261012.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cublas-13.8.1-1  |
|  cublas-cuda-13-13.8.1.7-1  |
|  cublas13-13.8.1-1  |
|  cudnn-9.27.0-1  |
|  cudnn-jit-9.27.0-1  |
|  cudnn9-9.27.0-1  |
|  cudnn9-cuda-12-9.27.0.42-1  |
|  cudnn9-cuda-12-9-9.27.0.42-1  |
|  cudnn9-cuda-13-9.27.0.42-1  |
|  cudnn9-cuda-13-4-9.27.0.42-1  |
|  cudnn9-jit-9.27.0-1  |
|  cudnn9-jit-cuda-12-9.27.0.42-1  |
|  cudnn9-jit-cuda-12-9-9.27.0.42-1  |
|  cudnn9-jit-cuda-13-9.27.0.42-1  |
|  cudnn9-jit-cuda-13-4-9.27.0.42-1  |
|  libcublas13-cuda-13-13.8.1.7-1  |
|  libcublas13-devel-cuda-13-13.8.1.7-1  |
|  libcudnn9-cuda-12-9.27.0.42-1  |
|  libcudnn9-cuda-13-9.27.0.42-1  |
|  libcudnn9-devel-cuda-12-9.27.0.42-1  |
|  libcudnn9-devel-cuda-13-9.27.0.42-1  |
|  libcudnn9-headers-cuda-12-9.27.0.42-1  |
|  libcudnn9-headers-cuda-13-9.27.0.42-1  |
|  libcudnn9-jit-cuda-12-9.27.0.42-1  |
|  libcudnn9-jit-cuda-13-9.27.0.42-1  |
|  libcudnn9-jit-devel-cuda-12-9.27.0.42-1  |
|  libcudnn9-jit-devel-cuda-13-9.27.0.42-1  |
|  libcudnn9-samples-9.27.0.42-1  |
|  libcudnn9-static-cuda-12-9.27.0.42-1  |
|  libcudnn9-static-cuda-13-9.27.0.42-1  |

## Image Updates
<a name="ami-updates-2023.12.20261012"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261012.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  amazon-ssm-agent-3.3.5390.0-1.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel6.18-tools-1:6.18.54-121.166.amzn2023  |
|  kernel6.18-1:6.18.54-121.166.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  parted-3.4-2.amzn2023.0.3  |
|  perl-AutoLoader-5.74-477.amzn2023.0.10  |
|  perl-B-1.80-477.amzn2023.0.10  |
|  perl-Class-Struct-0.66-477.amzn2023.0.10  |
|  perl-DynaLoader-1.47-477.amzn2023.0.10  |
|  perl-Errno-1.30-477.amzn2023.0.10  |
|  perl-Fcntl-1.13-477.amzn2023.0.10  |
|  perl-File-Basename-2.85-477.amzn2023.0.10  |
|  perl-File-stat-1.09-477.amzn2023.0.10  |
|  perl-FileHandle-2.03-477.amzn2023.0.10  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.10  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.3  |
|  perl-IO-1.43-477.amzn2023.0.10  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.10  |
|  perl-POSIX-1.94-477.amzn2023.0.10  |
|  perl-SelectSaver-1.02-477.amzn2023.0.10  |
|  perl-Storable-1:3.37-522.amzn2023.0.3  |
|  perl-Symbol-1.08-477.amzn2023.0.10  |
|  perl-base-2.27-477.amzn2023.0.10  |
|  perl-if-0.60.800-477.amzn2023.0.10  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.10  |
|  perl-libs-4:5.32.1-477.amzn2023.0.10  |
|  perl-mro-1.23-477.amzn2023.0.10  |
|  perl-overload-1.31-477.amzn2023.0.10  |
|  perl-overloading-0.02-477.amzn2023.0.10  |
|  perl-subs-1.03-477.amzn2023.0.10  |
|  perl-vars-1.05-477.amzn2023.0.10  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  rpcbind-1.2.6-0.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.98.1-1.amzn2023  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261012.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel6.18-1:6.18.54-121.166.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261012.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  amazon-ssm-agent-3.3.5390.0-1.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel6.12-tools-1:6.12.111-136.204.amzn2023  |
|  kernel6.12-1:6.12.111-136.204.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  parted-3.4-2.amzn2023.0.3  |
|  perl-AutoLoader-5.74-477.amzn2023.0.10  |
|  perl-B-1.80-477.amzn2023.0.10  |
|  perl-Class-Struct-0.66-477.amzn2023.0.10  |
|  perl-DynaLoader-1.47-477.amzn2023.0.10  |
|  perl-Errno-1.30-477.amzn2023.0.10  |
|  perl-Fcntl-1.13-477.amzn2023.0.10  |
|  perl-File-Basename-2.85-477.amzn2023.0.10  |
|  perl-File-stat-1.09-477.amzn2023.0.10  |
|  perl-FileHandle-2.03-477.amzn2023.0.10  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.10  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.3  |
|  perl-IO-1.43-477.amzn2023.0.10  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.10  |
|  perl-POSIX-1.94-477.amzn2023.0.10  |
|  perl-SelectSaver-1.02-477.amzn2023.0.10  |
|  perl-Storable-1:3.37-522.amzn2023.0.3  |
|  perl-Symbol-1.08-477.amzn2023.0.10  |
|  perl-base-2.27-477.amzn2023.0.10  |
|  perl-if-0.60.800-477.amzn2023.0.10  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.10  |
|  perl-libs-4:5.32.1-477.amzn2023.0.10  |
|  perl-mro-1.23-477.amzn2023.0.10  |
|  perl-overload-1.31-477.amzn2023.0.10  |
|  perl-overloading-0.02-477.amzn2023.0.10  |
|  perl-subs-1.03-477.amzn2023.0.10  |
|  perl-vars-1.05-477.amzn2023.0.10  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  rpcbind-1.2.6-0.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.98.1-1.amzn2023  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261012.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel6.12-1:6.12.111-136.204.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261012.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  amazon-ssm-agent-3.3.5390.0-1.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel-tools-1:6.1.188-233.393.amzn2023  |
|  kernel-1:6.1.188-233.393.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  parted-3.4-2.amzn2023.0.3  |
|  perl-AutoLoader-5.74-477.amzn2023.0.10  |
|  perl-B-1.80-477.amzn2023.0.10  |
|  perl-Class-Struct-0.66-477.amzn2023.0.10  |
|  perl-DynaLoader-1.47-477.amzn2023.0.10  |
|  perl-Errno-1.30-477.amzn2023.0.10  |
|  perl-Fcntl-1.13-477.amzn2023.0.10  |
|  perl-File-Basename-2.85-477.amzn2023.0.10  |
|  perl-File-stat-1.09-477.amzn2023.0.10  |
|  perl-FileHandle-2.03-477.amzn2023.0.10  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.10  |
|  perl-HTTP-Tiny-0.092-2.amzn2023.0.3  |
|  perl-IO-1.43-477.amzn2023.0.10  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.10  |
|  perl-POSIX-1.94-477.amzn2023.0.10  |
|  perl-SelectSaver-1.02-477.amzn2023.0.10  |
|  perl-Storable-1:3.37-522.amzn2023.0.3  |
|  perl-Symbol-1.08-477.amzn2023.0.10  |
|  perl-base-2.27-477.amzn2023.0.10  |
|  perl-if-0.60.800-477.amzn2023.0.10  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.10  |
|  perl-libs-4:5.32.1-477.amzn2023.0.10  |
|  perl-mro-1.23-477.amzn2023.0.10  |
|  perl-overload-1.31-477.amzn2023.0.10  |
|  perl-overloading-0.02-477.amzn2023.0.10  |
|  perl-subs-1.03-477.amzn2023.0.10  |
|  perl-vars-1.05-477.amzn2023.0.10  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  rpcbind-1.2.6-0.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.98.1-1.amzn2023  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261012.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261012-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  kernel-livepatch-repo-s3-2023.12.20261012-0.amzn2023  |
|  kernel-1:6.1.188-233.393.amzn2023  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  openssl-1:3.5.8-1.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  python3-urllib3-1.25.10-5.amzn2023.0.9  |
|  sudo-1.9.15-1.p5.amzn2023.0.4  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Default Container
<a name="amis-2023.12.20261012.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261012-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  dnf-4.14.0-1.amzn2023.0.9  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  python3-dnf-4.14.0-1.amzn2023.0.9  |
|  python3-hawkey-0.69.0-8.amzn2023.0.9  |
|  python3-libdnf-0.69.0-8.amzn2023.0.9  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.22  |
|  system-release-2023.12.20261012-0.amzn2023  |
|  yum-4.14.0-1.amzn2023.0.9  |

### Minimal Container
<a name="amis-2023.12.20261012.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261012-0.amzn2023  |
|  dnf-data-4.14.0-1.amzn2023.0.9  |
|  libdnf-0.69.0-8.amzn2023.0.9  |
|  libsolv-0.7.22-1.amzn2023.0.5  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.3  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.3  |
|  system-release-2023.12.20261012-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261012.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
