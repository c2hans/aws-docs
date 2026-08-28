---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260803.html
---

# Amazon Linux 2023 version 2023.12.20260803 release notes
<a name="relnotes-2023.12.20260803"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260803.

**Contents**
+ [Release Summary](#release-summary-2023.12.20260803)
+ [Repository Updates](#repository-updates-2023.12.20260803)
  + [Core New Packages](#amis-2023.12.20260803.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260803.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.12.20260803.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.12.20260803.Kernel-livepatch-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.12.20260803.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.12.20260803.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260803)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260803.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260803.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260803.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260803.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260803.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260803.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260803.Default-Container)
  + [Minimal Container](#amis-2023.12.20260803.Minimal-Container)
+ [Contact us](#amis-2023.12.20260803.contact-us)

## Release Summary
<a name="release-summary-2023.12.20260803"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ OpenSSH has been rebased to version 9.9. This release adds support for post-quantum cryptography algorithms as well as many other fixes and improvements. The most notable changes are as follows:
  + The sshd server is split into a listener binary `sshd` and a per-session binary `sshd-session`. Some log message formats are changed to be tagged as originating from a process named `sshd-session` rather than `sshd`.
  + `sshd` no longer uses `argv[0]` as the PAM service name. A new `PAMServiceName` directive allows selecting the service name at runtime which defaults to `sshd`.
  + `SetEnv` directives become first-match-wins in both `ssh_config` and `sshd_config`. Previously if an environment variable was multiply specified the last set value would have been used.
  + `ssh-keygen -A` which generates all default host key types no longer generates DSA keys. `ssh-keygen -t dsa` will still generate DSA keys.
  + `ssh-keyscan` writes banner lines to standard output instead of stderr. A new `-q` flag is added to silence them altogether.
  + `crypto-policies` enables `mlkem768x25519-sha256` for OpenSSH in the PQ sub-policy. To enable the PQ sub-policy on AL2023, see [Enable Post-Quantum Cryptography (PQC) on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/crypto-policies-pq.html).
+ Upcoming default kernel change: On August 17, 2026, the default kernel for AL2023 will change from 6.1 to 6.18. The `al2023-ami-{minimal}-kernel-default-{x86_64, arm64}` SSM parameters will then resolve to kernel 6.18 AMIs. Already running instances will not be affected; only new instances launched from the default parameter after the change will boot kernel 6.18. Customers who want to remain on kernel 6.1 should switch to the version-specific `al2023-ami-{minimal}-kernel-6.1-{x86_64, arm64}` SSM parameter before that date. If your environment requires FIPS validated cryptography, pin to kernel 6.1 as it is the only FIPS 140-3 validated kernel today. For more information, see [Updating the Linux Kernel on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html).

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260803"></a>

### Core New Packages
<a name="amis-2023.12.20260803.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  aws-workload-credentials-provider-3.1.1-1.amzn2023  |
|  nagios-plugins-2.4.12-4.amzn2023.0.1  |
|  tomcat11-11.0.24-1.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.12.20260803.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  7zip-26.02-17.amzn2023.0.1  |
|  amazon-cloudwatch-agent-1.300069.1-1.amzn2023  |
|  amazon-efs-utils-3.2.0-2.amzn2023  |
|  ansible-core-2.15.3-1.amzn2023.0.13  |
|  aws-nitro-enclaves-cli-1.4.5-0.amzn2023  |
|  bind-9.18.50-1.amzn2023.0.2  |
|  cifs-utils-7.7-144.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  dotnet10.0-10.0.110-1.amzn2023.0.1  |
|  dotnet8.0-8.0.129-1.amzn2023.0.1  |
|  ec2rl-1.1.7-1.amzn2023  |
|  ecs-init-1.106.0-1.amzn2023  |
|  fail2ban-1.1.0-1.amzn2023.0.2  |
|  freerdp-3.6.3-1.amzn2023.0.13  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.8  |
|  java-1.8.0-amazon-corretto-1.8.0\_502.b07-1.amzn2023  |
|  java-11-amazon-corretto-11.0.32\+9-1.amzn2023  |
|  java-17-amazon-corretto-17.0.20\+8-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.12\+8-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.4\+7-1.amzn2023.1  |
|  java-26-amazon-corretto-26.0.2\+10-1.amzn2023.1  |
|  jbig2dec-0.19-4.amzn2023.0.3  |
|  kernel-6.1.177-224.371.amzn2023  |
|  kernel6.12-6.12.95-124.187.amzn2023  |
|  kernel6.18-6.18.39-79.141.amzn2023  |
|  libreswan-4.12-3.amzn2023.0.3  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  mount-s3-1.23.0-1.amzn2023  |
|  nftables-1.0.4-3.amzn2023.0.3  |
|  nginx-1.30.4-1.amzn2023.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2023.0.9  |
|  nginx-mod-njs-0.9.9-1.amzn2023.0.3  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-3.5.7-2.amzn2023.0.1  |
|  openvpn-2.6.12-1.amzn2023.0.7  |
|  perl-DBI-1.651-1.amzn2023.0.1  |
|  perl-YAML-Syck-1.37-1.amzn2023.0.4  |
|  php8.2-8.2.33-1.amzn2023.0.1  |
|  php8.3-8.3.33-1.amzn2023.0.1  |
|  php8.4-8.4.24-1.amzn2023.0.1  |
|  php8.5-8.5.9-1.amzn2023.0.1  |
|  pipewire-1.2.7-4.amzn2023.0.5  |
|  python-dulwich-0.20.18-1.amzn2023.0.3  |
|  python-pillow-9.4.0-2.amzn2023.0.10  |
|  python-pyasn1-0.4.8-4.amzn2023.0.5  |
|  python-tornado-6.1.0-2.amzn2023.0.9  |
|  python3.11-3.11.15-1.amzn2023.0.5  |
|  python3.12-3.12.13-2.amzn2023.0.5  |
|  python3.13-3.13.14-1.amzn2023.0.3  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.4  |
|  python3.14-3.14.6-1.amzn2023.0.3  |
|  python3.9-3.9.25-1.amzn2023.0.9  |
|  rclone-1.74.3-83.amzn2023  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  ruby4.0-4.0.1-32.amzn2023.0.3  |
|  runfinch-finch-1.17.2-1.amzn2023.0.3  |
|  rust-cargo-c-0.10.19-1.amzn2023.0.4  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.13  |
|  valkey-9.0.5-1.amzn2023.0.1  |
|  vim-9.2.780-1.amzn2023.0.1  |

### Kernel-livepatch New Packages
<a name="amis-2023.12.20260803.Kernel-livepatch-New-Packages"></a>

This section provides details about Kernel-livepatch New Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.176-220.360-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.176-221.360-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.176-221.367-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.94-123.176-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.94-123.180-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.94-123.190-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.36-69.136-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.36-69.138-1.0-2.amzn2023  |
|  kernel-livepatch-6.18.38-73.137-1.0-2.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.12.20260803.Kernel-livepatch-Updated-Packages"></a>

This section provides details about Kernel-livepatch Updated Packages.

| Package |
| --- |
|  kernel-livepatch-6.1.168-203.330-1.0-9.amzn2023  |
|  kernel-livepatch-6.1.170-208.319-1.0-9.amzn2023  |
|  kernel-livepatch-6.1.170-210.320-1.0-8.amzn2023  |
|  kernel-livepatch-6.1.170-213.321-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.172-216.329-1.0-6.amzn2023  |
|  kernel-livepatch-6.1.172-216.339-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.174-217.345-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.175-219.357-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.175-219.359-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.176-220.358-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.80-106.156-1.0-11.amzn2023  |
|  kernel-livepatch-6.12.83-111.159-1.0-11.amzn2023  |
|  kernel-livepatch-6.12.83-113.160-1.0-10.amzn2023  |
|  kernel-livepatch-6.12.83-115.161-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.88-119.157-1.0-8.amzn2023  |
|  kernel-livepatch-6.12.88-119.160-1.0-5.amzn2023  |
|  kernel-livepatch-6.12.90-120.164-1.0-5.amzn2023  |
|  kernel-livepatch-6.12.92-122.166-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.92-122.168-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.94-123.174-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.20-41.237-1.0-11.amzn2023  |
|  kernel-livepatch-6.18.25-52.107-1.0-11.amzn2023  |
|  kernel-livepatch-6.18.25-55.108-1.0-10.amzn2023  |
|  kernel-livepatch-6.18.25-57.109-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.30-61.116-1.0-8.amzn2023  |
|  kernel-livepatch-6.18.30-61.119-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.33-63.124-1.0-5.amzn2023  |
|  kernel-livepatch-6.18.35-68.127-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.35-68.129-1.0-3.amzn2023  |
|  kernel-livepatch-6.18.36-69.134-1.0-3.amzn2023  |

### Nvidia New Packages
<a name="amis-2023.12.20260803.Nvidia-New-Packages"></a>

This section provides details about Nvidia New Packages.

| Package |
| --- |
|  nsight-compute-2026.1.1-2026.1.1.2-1  |

### Nvidia Updated Packages
<a name="amis-2023.12.20260803.Nvidia-Updated-Packages"></a>

This section provides details about Nvidia Updated Packages.

| Package |
| --- |
|  cuda-13-2-13.2.2-1  |
|  cuda-cccl-13-2-13.2.86-1  |
|  cuda-command-line-tools-13-2-13.2.2-1  |
|  cuda-compiler-13-2-13.2.2-1  |
|  cuda-crt-13-2-13.2.86-1  |
|  cuda-ctadvisor-13-2-13.2.86-1  |
|  cuda-cudart-13-2-13.2.86-1  |
|  cuda-cudart-devel-13-2-13.2.86-1  |
|  cuda-culibos-devel-13-2-13.2.86-1  |
|  cuda-cuobjdump-13-2-13.2.86-1  |
|  cuda-cupti-13-2-13.2.86-1  |
|  cuda-cuxxfilt-13-2-13.2.86-1  |
|  cuda-documentation-13-2-13.2.86-1  |
|  cuda-driver-devel-13-2-13.2.86-1  |
|  cuda-gdb-13-2-13.2.86-1  |
|  cuda-gdb-src-13-2-13.2.86-1  |
|  cuda-libraries-13-2-13.2.2-1  |
|  cuda-libraries-devel-13-2-13.2.2-1  |
|  cuda-minimal-build-13-2-13.2.2-1  |
|  cuda-nsight-13-2-13.2.86-1  |
|  cuda-nsight-compute-13-2-13.2.2-1  |
|  cuda-nsight-systems-13-2-13.2.2-1  |
|  cuda-nvcc-13-2-13.2.86-1  |
|  cuda-nvdisasm-13-2-13.2.86-1  |
|  cuda-nvml-devel-13-2-13.2.86-1  |
|  cuda-nvprune-13-2-13.2.86-1  |
|  cuda-nvrtc-13-2-13.2.86-1  |
|  cuda-nvrtc-devel-13-2-13.2.86-1  |
|  cuda-nvtx-13-2-13.2.86-1  |
|  cuda-opencl-13-2-13.2.86-1  |
|  cuda-opencl-devel-13-2-13.2.86-1  |
|  cuda-profiler-api-13-2-13.2.86-1  |
|  cuda-runtime-13-2-13.2.2-1  |
|  cuda-sandbox-devel-13-2-13.2.86-1  |
|  cuda-sanitizer-13-2-13.2.87-1  |
|  cuda-tileiras-13-2-13.2.86-1  |
|  cuda-toolkit-13-2-13.2.2-1  |
|  cuda-toolkit-13-2-config-common-13.2.86-1  |
|  cuda-tools-13-2-13.2.2-1  |
|  cuda-visual-tools-13-2-13.2.2-1  |
|  datacenter-gpu-manager-4-core-4.6.1-1  |
|  datacenter-gpu-manager-4-cuda-all-4.6.1-1  |
|  datacenter-gpu-manager-4-cuda11-4.6.1-1  |
|  datacenter-gpu-manager-4-cuda12-4.6.1-1  |
|  datacenter-gpu-manager-4-cuda13-4.6.1-1  |
|  datacenter-gpu-manager-4-devel-4.6.1-1  |
|  datacenter-gpu-manager-4-multinode-4.6.1-1  |
|  datacenter-gpu-manager-4-multinode-cuda12-4.6.1-1  |
|  datacenter-gpu-manager-4-multinode-cuda13-4.6.1-1  |
|  datacenter-gpu-manager-4-proprietary-4.6.1-1  |
|  datacenter-gpu-manager-4-proprietary-cuda11-4.6.1-1  |
|  datacenter-gpu-manager-4-proprietary-cuda12-4.6.1-1  |
|  datacenter-gpu-manager-4-proprietary-cuda13-4.6.1-1  |
|  gds-tools-13-2-1.17.1.22-1  |
|  libcublas-13-2-13.4.1.3-1  |
|  libcublas-devel-13-2-13.4.1.3-1  |
|  libcufft-13-2-12.2.0.57-1  |
|  libcufft-devel-13-2-12.2.0.57-1  |
|  libcufile-13-2-1.17.1.22-1  |
|  libcufile-devel-13-2-1.17.1.22-1  |
|  libcuobjclient-13-2-1.1.1.22-1  |
|  libcuobjclient-devel-13-2-1.1.1.22-1  |
|  libcurand-13-2-10.4.2.66-1  |
|  libcurand-devel-13-2-10.4.2.66-1  |
|  libcusolver-13-2-12.2.0.11-1  |
|  libcusolver-devel-13-2-12.2.0.11-1  |
|  libcusparse-13-2-12.7.10.12-1  |
|  libcusparse-devel-13-2-12.7.10.12-1  |
|  libnpp-13-2-13.1.0.59-1  |
|  libnpp-devel-13-2-13.1.0.59-1  |
|  libnvfatbin-13-2-13.2.86-1  |
|  libnvfatbin-devel-13-2-13.2.86-1  |
|  libnvjitlink-13-2-13.2.86-1  |
|  libnvjitlink-devel-13-2-13.2.86-1  |
|  libnvjpeg-13-2-13.1.0.59-1  |
|  libnvjpeg-devel-13-2-13.1.0.59-1  |
|  libnvptxcompiler-13-2-13.2.86-1  |
|  libnvvm-13-2-13.2.86-1  |
|  nsight-systems-2025.6.3-2025.6.3.541\_256337736014v0-0  |
|  nvidia-gds-13-2-13.2.2-1  |
|  nvlink5-595.71.05-2  |

## Image Updates
<a name="ami-updates-2023.12.20260803"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260803.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.2  |
|  bind-license-32:9.18.50-1.amzn2023.0.2  |
|  bind-utils-32:9.18.50-1.amzn2023.0.2  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.6  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel6.18-tools-1:6.18.39-79.141.amzn2023  |
|  kernel6.18-1:6.18.39-79.141.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-common-2:9.2.780-1.amzn2023.0.1  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.780-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |
|  xxd-2:9.2.780-1.amzn2023.0.1  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260803.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel6.18-1:6.18.39-79.141.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260803.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.2  |
|  bind-license-32:9.18.50-1.amzn2023.0.2  |
|  bind-utils-32:9.18.50-1.amzn2023.0.2  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.6  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel6.12-tools-1:6.12.95-124.187.amzn2023  |
|  kernel6.12-1:6.12.95-124.187.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-common-2:9.2.780-1.amzn2023.0.1  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.780-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |
|  xxd-2:9.2.780-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260803.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel6.12-1:6.12.95-124.187.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260803.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  bind-libs-32:9.18.50-1.amzn2023.0.2  |
|  bind-license-32:9.18.50-1.amzn2023.0.2  |
|  bind-utils-32:9.18.50-1.amzn2023.0.2  |
|  crypto-policies-scripts-20260224-1.gitea0f072.amzn2023.0.6  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel-tools-1:6.1.177-224.371.amzn2023  |
|  kernel-1:6.1.177-224.371.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-common-2:9.2.780-1.amzn2023.0.1  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.780-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |
|  xxd-2:9.2.780-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260803.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260803-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  dnf-plugin-support-info-2.0.0-231.amzn2023  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  kernel-livepatch-repo-s3-2023.12.20260803-0.amzn2023  |
|  kernel-1:6.1.177-224.371.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssh-clients-9.9p1-10.amzn2023.0.1  |
|  openssh-server-9.9p1-10.amzn2023.0.1  |
|  openssh-9.9p1-10.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  openssl-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-selinux-4.16.1.3-29.amzn2023.0.7  |
|  rpm-plugin-systemd-inhibit-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |
|  vim-data-2:9.2.780-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.780-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.12.20260803.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260803-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.9  |
|  python3-rpm-4.16.1.3-29.amzn2023.0.7  |
|  python3-3.9.25-1.amzn2023.0.9  |
|  rpm-build-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-sign-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260803.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260803-0.amzn2023  |
|  crypto-policies-20260224-1.gitea0f072.amzn2023.0.6  |
|  gawk-5.1.0-3.amzn2023.0.4  |
|  glib2-2.82.2-771.amzn2023  |
|  libxml2-2.10.4-1.amzn2023.0.20  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.1  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.1  |
|  rpm-libs-4.16.1.3-29.amzn2023.0.7  |
|  rpm-4.16.1.3-29.amzn2023.0.7  |
|  system-release-2023.12.20260803-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260803.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
