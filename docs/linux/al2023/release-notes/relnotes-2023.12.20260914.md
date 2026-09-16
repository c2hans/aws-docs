---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260914.html
---

# Amazon Linux 2023 version 2023.12.20260914 release notes
<a name="relnotes-2023.12.20260914"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260914.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260914)
+ [Repository Updates](#repository-updates-2023.12.20260914)
  + [Core Updated Packages](#amis-2023.12.20260914.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20260914.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260914.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260914.Nvidia-New-Packages)
+ [Image Updates](#ami-updates-2023.12.20260914)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260914.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260914.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260914.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260914.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260914.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260914.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260914.Default-Container)
  + [Minimal Container](#amis-2023.12.20260914.Minimal-Container)
+ [Contact us](#amis-2023.12.20260914.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260914"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260914"></a>

### Core Updated Packages
<a name="amis-2023.12.20260914.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  aws-nitro-enclaves-acm-1.5.0-1.amzn2023  |
|  bluez-5.62-2.amzn2023.0.6  |
|  bouncycastle-1.70-4.amzn2023.0.8  |
|  composer-2.10.3-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.6  |
|  cups-filters-1.28.16-3.amzn2023.0.6  |
|  curl-8.21.0-5.amzn2023.0.1  |
|  distribution-gpg-keys-1.104-1.amzn2023.0.2  |
|  ecs-init-1.106.2-1.amzn2023  |
|  ecs-service-connect-agent-v1.39.1.0-1.amzn2023  |
|  emacs-28.2-3.amzn2023.0.11  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  freerdp-3.31.0-1.amzn2023  |
|  gnome-remote-desktop-47.3-1.amzn2023.0.4  |
|  golang-1.26.8-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.7  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.9  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.13  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.6  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2023.0.7  |
|  golist-0.10.4-12.amzn2023.0.15  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.4  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.9  |
|  jsoup-1.23.2-1.amzn2023.0.1  |
|  kernel-6.1.186-228.374.amzn2023  |
|  kernel6.18-6.18.48-107.148.amzn2023  |
|  libevent-2.1.12-3.amzn2023.0.4  |
|  libheif-1.19.8-1.amzn2023.0.8  |
|  libsoup-2.72.0-6.amzn2023.0.14  |
|  libsoup3-3.6.6-60.amzn2023  |
|  libtiff-4.4.0-4.amzn2023.0.28  |
|  libvirt-12.0.0-3.amzn2023.0.2  |
|  mock-core-configs-39.2-1.amzn2023.0.2  |
|  mod\_auth\_openidc-2.4.16.11-1.amzn2023.0.2  |
|  mount-s3-1.24.0-1.amzn2023  |
|  nerdctl-2.3.5-1.amzn2023.0.1  |
|  nodejs24-24.20.0-1.amzn2023.0.1  |
|  openexr-3.1.5-1.amzn2023.0.12  |
|  openssl-3.5.8-1.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.5  |
|  perl-Socket-2.032-1.amzn2023.0.4  |
|  perl-YAML-1.31-7.amzn2023.0.2  |
|  php8.4-8.4.25-1.amzn2023.0.1  |
|  php8.5-8.5.10-1.amzn2023.0.1  |
|  python-mistune-0.8.3-14.amzn2023.0.4  |
|  rsyslog-8.2204.0-3.amzn2023.0.6  |
|  ruby3.4-3.4.8-27.amzn2023.0.7  |
|  ruby4.0-4.0.1-32.amzn2023.0.4  |
|  runc-1.3.6-1.amzn2023.0.1  |
|  rust-1.98.0-1.amzn2023  |
|  samba-4.17.12-1.amzn2023.0.7  |
|  system-release-2023.12.20260914-0.amzn2023  |
|  valkey-9.0.6-1.amzn2023.0.1  |
|  weston-13.0.3-2.amzn2023.0.3  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20260914.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.176-223.369-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.177-224.371-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.180-225.360-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.182-227.378-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.100-125.179-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.94-123.192-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.95-124.187-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.38-76.139-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.39-79.141-1.0-1.amzn2023  |
|  kernel-livepatch-6.18.41-94.142-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260914.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.172-216.339-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.174-217.345-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.175-219.357-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.175-219.359-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.176-220.358-1.0-4.amzn2023  |
|  kernel-livepatch-6.1.176-220.360-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.176-221.360-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.176-221.367-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.88-119.160-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.90-120.164-1.0-6.amzn2023  |
|  kernel-livepatch-6.12.92-122.166-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.92-122.168-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.94-123.174-1.0-4.amzn2023  |
|  kernel-livepatch-6.12.94-123.176-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.94-123.180-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.94-123.190-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.30-61.119-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.33-63.124-1.0-6.amzn2023  |
|  kernel-livepatch-6.18.35-68.127-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.35-68.129-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.36-69.134-1.0-4.amzn2023  |
|  kernel-livepatch-6.18.36-69.136-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.36-69.138-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.38-73.137-1.0-3.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20260914.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  cudnn-9.25.1-1  |
|  cudnn-jit-9.25.1-1  |
|  cudnn9-9.25.1-1  |
|  cudnn9-cuda-12-9.25.1.1-1  |
|  cudnn9-cuda-12-9-9.25.1.1-1  |
|  cudnn9-cuda-13-9.25.1.1-1  |
|  cudnn9-cuda-13-4-9.25.1.1-1  |
|  cudnn9-jit-9.25.1-1  |
|  cudnn9-jit-cuda-12-9.25.1.1-1  |
|  cudnn9-jit-cuda-12-9-9.25.1.1-1  |
|  cudnn9-jit-cuda-13-9.25.1.1-1  |
|  cudnn9-jit-cuda-13-4-9.25.1.1-1  |
|  libcudnn9-cuda-12-9.25.1.1-1  |
|  libcudnn9-cuda-13-9.25.1.1-1  |
|  libcudnn9-devel-cuda-12-9.25.1.1-1  |
|  libcudnn9-devel-cuda-13-9.25.1.1-1  |
|  libcudnn9-headers-cuda-12-9.25.1.1-1  |
|  libcudnn9-headers-cuda-13-9.25.1.1-1  |
|  libcudnn9-jit-cuda-12-9.25.1.1-1  |
|  libcudnn9-jit-cuda-13-9.25.1.1-1  |
|  libcudnn9-jit-devel-cuda-12-9.25.1.1-1  |
|  libcudnn9-jit-devel-cuda-13-9.25.1.1-1  |
|  libcudnn9-samples-9.25.1.1-1  |
|  libcudnn9-static-cuda-12-9.25.1.1-1  |
|  libcudnn9-static-cuda-13-9.25.1.1-1  |

## Image Updates
<a name="ami-updates-2023.12.20260914"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260914.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  kernel6.18-tools-1:6.18.48-107.148.amzn2023  |
|  kernel6.18-1:6.18.48-107.148.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  libevent-2.1.12-3.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.5  |
|  perl-Socket-4:2.032-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.98.0-1.amzn2023  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260914.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  kernel6.18-1:6.18.48-107.148.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260914.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  libevent-2.1.12-3.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.5  |
|  perl-Socket-4:2.032-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.98.0-1.amzn2023  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260914.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260914.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  kernel-tools-1:6.1.186-228.374.amzn2023  |
|  kernel-1:6.1.186-228.374.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  libevent-2.1.12-3.amzn2023.0.4  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.5  |
|  perl-Socket-4:2.032-1.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.98.0-1.amzn2023  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260914.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  kernel-livepatch-repo-s3-2023.12.20260914-0.amzn2023  |
|  kernel-1:6.1.186-228.374.amzn2023  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  openssl-1:3.5.8-1.amzn2023.0.1  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20260914.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  expat-2.8.3-1.amzn2023.0.1  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  system-release-2023.12.20260914-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260914.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260914-0.amzn2023  |
|  curl-minimal-8.21.0-5.amzn2023.0.1  |
|  libcurl-minimal-8.21.0-5.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-1.amzn2023.0.1  |
|  openssl-libs-1:3.5.8-1.amzn2023.0.1  |
|  system-release-2023.12.20260914-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260914.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
