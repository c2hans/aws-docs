---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260817.html
---

# Amazon Linux 2023 version 2023.12.20260817 release notes
<a name="relnotes-2023.12.20260817"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260817.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260817)
+ [Repository Updates](#repository-updates-2023.12.20260817)
  + [Core New Packages](#amis-2023.12.20260817.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260817.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260817.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260817.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260817)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260817.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260817.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260817.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260817.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260817.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260817.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260817.Default-Container)
  + [Minimal Container](#amis-2023.12.20260817.Minimal-Container)
+ [Contact us](#amis-2023.12.20260817.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260817"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `buildah` has been added. This package enables daemonless creation of OCI-compliant container images, including rootless builds. For information about usage and configuration, see the [official buildah documentation](https://buildah.io).
+  `skopeo` has been added. This package provides management and distribution of container images across registries without a container engine daemon. For information about usage and configuration, see the [official skopeo documentation](https://github.com/containers/skopeo).
+  With the addition of `buildah` and `skopeo`, `kiwi-cli` can now build container images from kiwi-ng image description files. For information about container image builds, see the [official kiwi-ng documentation](https://osinside.github.io/kiwi/).

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260817"></a>

### Core New Packages
<a name="amis-2023.12.20260817.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  aardvark-dns-1.17.1-1.amzn2023.0.1  |
|  buildah-1.43.1-1.amzn2023.0.1  |
|  containers-common-0.67.0-1.amzn2023.0.2  |
|  libtalloc-latest-2.4.4-1.amzn2023.0.1  |
|  libtdb-latest-1.4.15-1.amzn2023.0.1  |
|  libtevent-latest-0.17.1-1.amzn2023.0.1  |
|  netavark-1.17.2-1.amzn2023.0.1  |
|  samba-latest-4.24.5-1.amzn2023.0.1  |
|  skopeo-1.22.2-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.12.20260817.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  containerd-2.2.5-1.amzn2023.0.2  |
|  docker-25.0.16-1.amzn2023.0.4  |
|  dotnet9.0-9.0.119-1.amzn2023.0.1  |
|  fasterxml-oss-parent-75-2.amzn2023.0.1  |
|  firefox-140.13.0-1.amzn2023.0.1  |
|  freerdp-3.6.3-1.amzn2023.0.14  |
|  gnome-remote-desktop-47.3-1.amzn2023.0.3  |
|  iscsi-initiator-utils-6.2.1.4-10.git2a8f9d8.amzn2023.0.3  |
|  isns-utils-0.101-6.amzn2023.0.1  |
|  jackson-annotations-2.21-7.amzn2023.0.1  |
|  jackson-bom-2.21.5-3.amzn2023.0.1  |
|  jackson-core-2.21.5-2.amzn2023.0.1  |
|  jackson-parent-2.21-2.amzn2023.0.1  |
|  javapackages-bootstrap-1.5.0^20220105.git9f283b7-3.amzn2023.0.10  |
|  kernel-6.1.180-225.360.amzn2023  |
|  kernel6.12-6.12.100-125.179.amzn2023  |
|  kernel6.18-6.18.41-94.142.amzn2023  |
|  kiwi-10.3.0-1.amzn2023  |
|  libssh2-1.10.0-1.amzn2023.0.6  |
|  nodejs22-22.23.2-1.amzn2023.0.2  |
|  nodejs24-24.18.1-1.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  openssl-fips-provider-certified-3.2.2-1.amzn2023  |
|  perl-Date-Manip-6.85-1.amzn2023.0.3  |
|  perl-Net-DNS-1.56-1.amzn2023.0.1  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.4  |
|  python-idna-2.10-3.amzn2023.0.4  |
|  python-jwt-2.4.0-1.amzn2023.0.5  |
|  python-urwid-2.1.2-5.amzn2023.0.1  |
|  rust-1.97.0-2.amzn2023  |
|  rust-cargo-c-0.10.21-1.amzn2023.0.1  |
|  spice-vdagent-0.22.1-7.amzn2023.0.1  |
|  system-release-2023.12.20260817-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.2  |
|  wget-1.21.3-1.amzn2023.0.5  |

### Nvidia New Packages
<a name="amis-2023.12.20260817.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  cuda-compat-13-3-610.57.04-1.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260817.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cublas-13.6.1-1  |
|  cublas-cuda-13-13.6.1.10-1  |
|  cublas13-13.6.1-1  |
|  cuda-compat-13-0-580.178.04-1.amzn2023  |
|  cuda-compat-13-2-595.91.07-1.amzn2023  |
|  cuda-drivers-595.91.07-1.amzn2023  |
|  kmod-nvidia-latest-dkms-595.91.07-1.amzn2023  |
|  kmod-nvidia-open-dkms-595.91.07-1.amzn2023  |
|  libcublas13-cuda-13-13.6.1.10-1  |
|  libcublas13-devel-cuda-13-13.6.1.10-1  |
|  libnvidia-cfg-595.91.07-1.amzn2023  |
|  libnvidia-fbc-595.91.07-1.amzn2023  |
|  libnvidia-gpucomp-595.91.07-1.amzn2023  |
|  libnvidia-ml-595.91.07-1.amzn2023  |
|  libnvidia-nscq-595.91.07-1.amzn2023  |
|  libnvsdm-595.91.07-1.amzn2023  |
|  libnvsdm-devel-595.91.07-1.amzn2023  |
|  nvidia-driver-595.91.07-1.amzn2023  |
|  nvidia-driver-assistant-0.59.91.07-1  |
|  nvidia-driver-cuda-595.91.07-1.amzn2023  |
|  nvidia-driver-cuda-libs-595.91.07-1.amzn2023  |
|  nvidia-driver-libs-595.91.07-1.amzn2023  |
|  nvidia-fabric-manager-devel-595.91.07-1.amzn2023  |
|  nvidia-fabricmanager-595.91.07-1.amzn2023  |
|  nvidia-imex-595.91.07-1.amzn2023  |
|  nvidia-kmod-common-595.91.07-1.amzn2023  |
|  nvidia-libXNVCtrl-595.91.07-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-595.91.07-1.amzn2023  |
|  nvidia-modprobe-595.91.07-1.amzn2023  |
|  nvidia-open-595.91.07-1.amzn2023  |
|  nvidia-persistenced-595.91.07-1.amzn2023  |
|  nvidia-settings-595.91.07-1.amzn2023  |
|  nvidia-xconfig-595.91.07-1.amzn2023  |
|  nvlink5-595.91.07-1  |
|  nvlink5-580-580.178.04-1  |
|  xorg-x11-nvidia-595.91.07-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20260817"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260817.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel6.18-tools-1:6.18.41-94.142.amzn2023  |
|  kernel6.18-1:6.18.41-94.142.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.4  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.97.0-2.amzn2023  |
|  system-release-2023.12.20260817-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.2  |
|  wget-1.21.3-1.amzn2023.0.5  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260817.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel6.18-1:6.18.41-94.142.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  system-release-2023.12.20260817-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260817.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel6.12-tools-1:6.12.100-125.179.amzn2023  |
|  kernel6.12-1:6.12.100-125.179.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.4  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.97.0-2.amzn2023  |
|  system-release-2023.12.20260817-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.2  |
|  wget-1.21.3-1.amzn2023.0.5  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260817.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel6.12-1:6.12.100-125.179.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  system-release-2023.12.20260817-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260817.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-tools-1:6.1.180-225.360.amzn2023  |
|  kernel-1:6.1.180-225.360.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  perl-Net-SSLeay-1.94-3.amzn2023.0.4  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  rust-toolset-srpm-macros-1.97.0-2.amzn2023  |
|  system-release-2023.12.20260817-0.amzn2023  |
|  unzip-6.0-68.amzn2023.0.2  |
|  wget-1.21.3-1.amzn2023.0.5  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260817.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260817-0.amzn2023  |
|  kernel-1:6.1.180-225.360.amzn2023  |
|  openssh-clients-9.9p1-10.amzn2023.0.2  |
|  openssh-server-9.9p1-10.amzn2023.0.2  |
|  openssh-9.9p1-10.amzn2023.0.2  |
|  python3-idna-2.10-3.amzn2023.0.4  |
|  system-release-2023.12.20260817-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20260817.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260817-0.amzn2023  |
|  system-release-2023.12.20260817-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260817.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260817-0.amzn2023  |
|  system-release-2023.12.20260817-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260817.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
