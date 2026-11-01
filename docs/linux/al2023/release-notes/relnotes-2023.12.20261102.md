---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261102.html
---

# Amazon Linux 2023 version 2023.12.20261102 release notes
<a name="relnotes-2023.12.20261102"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261102.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261102)
+ [Repository Updates](#repository-updates-2023.12.20261102)
  + [Core Updated Packages](#amis-2023.12.20261102.Core-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20261102.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261102)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261102.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261102.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261102.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261102.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261102.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261102.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261102.Default-Container)
  + [Minimal Container](#amis-2023.12.20261102.Minimal-Container)
+ [Contact us](#amis-2023.12.20261102.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261102"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261102"></a>

### Core Updated Packages
<a name="amis-2023.12.20261102.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  amazon-cloudwatch-agent-1.300073.2-1.amzn2023  |
|  amazon-ecr-credential-helper-0.12.0-6.amzn2023  |
|  amazon-ssm-agent-3.3.5700.0-1.amzn2023  |
|  cni-plugins-1.7.1-1.amzn2023.0.9  |
|  containerd-2.3.7-1.amzn2023.0.2  |
|  dotnet10.0-10.0.114-1.amzn2023.0.1  |
|  dotnet8.0-8.0.133-1.amzn2023.0.1  |
|  dotnet9.0-9.0.123-1.amzn2023.0.1  |
|  ecs-init-1.108.2-1.amzn2023  |
|  ecs-service-connect-agent-v1.39.4.0-1.amzn2023  |
|  emacs-28.2-3.amzn2023.0.13  |
|  firefox-153.5.1-1.amzn2023.0.2  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.11  |
|  java-1.8.0-amazon-corretto-1.8.0\_512.b09-1.amzn2023  |
|  java-11-amazon-corretto-11.0.33.0.10-1.amzn2023  |
|  java-17-amazon-corretto-17.0.21.0.11-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.13.0.11-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.5.0.10-1.amzn2023.1  |
|  java-27-amazon-corretto-27.0.1.0.11-1.amzn2023.1  |
|  kernel-6.1.189-236.400.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  nerdctl-2.3.5-1.amzn2023.0.3  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.14  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  perl-Cpanel-JSON-XS-4.25-2.amzn2023.0.10  |
|  perl-Text-CSV\_XS-1.65-1.amzn2023.0.1  |
|  python-dns-2.1.0-3.amzn2023.0.5  |
|  python3.11-3.11.18-1.amzn2023.0.1  |
|  rclone-1.75.1-2.amzn2023  |
|  rsyslog-8.2204.0-3.amzn2023.0.9  |
|  runfinch-finch-1.19.0-1.amzn2023.0.3  |
|  soci-snapshotter-0.16.1-1.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |
|  valkey-9.0.7-1.amzn2023.0.1  |
|  yq-4.53.3-16.amzn2023  |

### Nvidia Updated Packages
<a name="amis-2023.12.20261102.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cublas-13.8.2-1  |
|  cublas-cuda-13-13.8.2.12-1  |
|  cublas13-13.8.2-1  |
|  cuda-compat-13-2-595.112.07-1.amzn2023  |
|  cuda-drivers-595.112.07-1.amzn2023  |
|  datacenter-gpu-manager-4-core-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda-all-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda11-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda11-cublas-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-cublas-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-curand-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-cusparselt-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-nccl-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda12-ubergemm2-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-cublas-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-curand-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-cusparselt-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-nccl-4.7.1-2  |
|  datacenter-gpu-manager-4-cuda13-ubergemm2-4.7.1-2  |
|  datacenter-gpu-manager-4-dcgmproftesterkernels-4.7.1-2  |
|  datacenter-gpu-manager-4-devel-4.7.1-2  |
|  datacenter-gpu-manager-4-module-config-4.7.1-2  |
|  datacenter-gpu-manager-4-module-diag-4.7.1-2  |
|  datacenter-gpu-manager-4-module-health-4.7.1-2  |
|  datacenter-gpu-manager-4-module-introspect-4.7.1-2  |
|  datacenter-gpu-manager-4-module-nvswitch-4.7.1-2  |
|  datacenter-gpu-manager-4-module-policy-4.7.1-2  |
|  datacenter-gpu-manager-4-module-sysmon-4.7.1-2  |
|  datacenter-gpu-manager-4-multinode-4.7.1-2  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.7.1-2  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.7.1-2  |
|  datacenter-gpu-manager-4-proprietary-4.7.1-2  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.7.1-2  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.7.1-2  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.7.1-2  |
|  datacenter-gpu-manager-4-python3-4.7.1-2  |
|  dcgmi-4.7.1-2  |
|  kmod-nvidia-latest-dkms-595.112.07-1.amzn2023  |
|  kmod-nvidia-open-dkms-595.112.07-1.amzn2023  |
|  libcublas13-cuda-13-13.8.2.12-1  |
|  libcublas13-devel-cuda-13-13.8.2.12-1  |
|  libdcgm-4.7.1-2  |
|  libnvidia-cfg-595.112.07-1.amzn2023  |
|  libnvidia-fbc-595.112.07-1.amzn2023  |
|  libnvidia-gpucomp-595.112.07-1.amzn2023  |
|  libnvidia-ml-595.112.07-1.amzn2023  |
|  libnvidia-nscq-595.112.07-1.amzn2023  |
|  libnvsdm-595.112.07-1.amzn2023  |
|  libnvsdm-devel-595.112.07-1.amzn2023  |
|  nv-hostengine-4.7.1-2  |
|  nvidia-driver-595.112.07-1.amzn2023  |
|  nvidia-driver-cuda-595.112.07-1.amzn2023  |
|  nvidia-driver-cuda-libs-595.112.07-1.amzn2023  |
|  nvidia-driver-libs-595.112.07-1.amzn2023  |
|  nvidia-fabric-manager-devel-595.112.07-1.amzn2023  |
|  nvidia-fabricmanager-595.112.07-1.amzn2023  |
|  nvidia-imex-595.112.07-1.amzn2023  |
|  nvidia-kmod-common-595.112.07-1.amzn2023  |
|  nvidia-libXNVCtrl-595.112.07-1.amzn2023  |
|  nvidia-libXNVCtrl-devel-595.112.07-1.amzn2023  |
|  nvidia-modprobe-595.112.07-1.amzn2023  |
|  nvidia-open-595.112.07-1.amzn2023  |
|  nvidia-persistenced-595.112.07-1.amzn2023  |
|  nvidia-settings-595.112.07-1.amzn2023  |
|  nvidia-xconfig-595.112.07-1.amzn2023  |
|  nvlink5-595.112.07-1  |
|  nvlink5-580-580.196.07-1  |
|  nvlsm-2025.12.211-1  |
|  xorg-x11-nvidia-595.112.07-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.12.20261102"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261102.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  amazon-ssm-agent-3.3.5700.0-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261102.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261102.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  amazon-ssm-agent-3.3.5700.0-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261102.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261102.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  amazon-ssm-agent-3.3.5700.0-1.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  kernel-tools-1:6.1.189-236.400.amzn2023  |
|  kernel-1:6.1.189-236.400.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261102.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261102-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20261102-0.amzn2023  |
|  kernel-1:6.1.189-236.400.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  openssh-clients-9.9p1-16.amzn2023.0.1  |
|  openssh-server-9.9p1-16.amzn2023.0.1  |
|  openssh-9.9p1-16.amzn2023.0.1  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20261102.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  system-release-2023.12.20261102-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20261102.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261102-0.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.22  |
|  system-release-2023.12.20261102-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261102.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
