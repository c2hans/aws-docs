---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250527.html
---

# Amazon Linux 2023 version 2023.7.20250527 release notes
<a name="relnotes-2023.7.20250527"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250527.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250527)
+ [Repository Updates](#repository-updates-2023.7.20250527)
  + [Core Updated Packages](#amis-2023.7.20250527.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.7.20250527.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.7.20250527.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.7.20250527)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250527.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250527.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250527.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250527.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.7.20250527.Default-Container)
  + [Minimal Container](#amis-2023.7.20250527.Minimal-Container)
+ [Contact us](#amis-2023.7.20250527.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250527"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Notable updates**
+  perl-Mojolicious-9.40-3.amzn2023.0.1 : Perl-Mojolicious has been updated to latest 9.40 and removes some included fonts and the `Mojo::IOLoop::Delay module`. `Mojo::IOLoop::Delay` is a Perl module that helps manage callbacks and control the flow of events in asynchronous programming, particularly for the Mojo::IOLoop event loop, it's recommended to use `Mojo::Promise` or other asynchronous patterns supported by the current version of Mojolicious.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250527"></a>

### Core Updated Packages
<a name="amis-2023.7.20250527.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.12.82-1.amzn2023.0.8  |
|  amazon-ec2-net-utils-2.5.5-1.amzn2023.0.1  |
|  apache-commons-io-2.8.0-7.amzn2023.0.5  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  composer-2.8.8-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.6-1.amzn2023  |
|  docker-25.0.8-1.amzn2023.0.4  |
|  ecs-init-1.93.1-1.amzn2023  |
|  exiv2-0.28.5-128.amzn2023  |
|  firefox-128.10.0-1.amzn2023.0.2  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gnome-tweaks-46.1-3.amzn2023.0.1  |
|  golang-1.24.3-1.amzn2023.0.1  |
|  golang-github-cpuguy83-md2man-2.0.2-23.amzn2023.0.3  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  gsettings-desktop-schemas-47.1-206.amzn2023  |
|  gtk4-4.16.13-175.amzn2023  |
|  kernel6.12-6.12.29-33.102.amzn2023  |
|  libnvme-1.13-1.amzn2023.0.1  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  lsof-4.94.0-1.amzn2023.0.3  |
|  mariadb105-10.5.29-1.amzn2023.0.1  |
|  nerdctl-2.0.5-1.amzn2023.0.1  |
|  nvme-cli-2.13-1.amzn2023.0.1  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.4  |
|  open-vm-tools-12.3.0-1.amzn2023.0.2  |
|  perl-Mojolicious-9.40-3.amzn2023.0.1  |
|  pipewire-1.2.7-4.amzn2023.0.4  |
|  postgresql15-15.13-1.amzn2023.0.1  |
|  postgresql16-16.9-1.amzn2023.0.1  |
|  postgresql17-17.5-1.amzn2023.0.1  |
|  python-poetry-core-1.6.1-1.amzn2023.0.1  |
|  runfinch-finch-1.8.1-1.amzn2023.0.1  |
|  soci-snapshotter-0.9.0-1.amzn2023.0.3  |
|  system-release-2023.7.20250527-0.amzn2023  |
|  valkey-8.0.3-3.amzn2023.0.1  |

### Nvidia New Packages
<a name="amis-2023.7.20250527.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  cuda-12-9-12.9.0-1  |
|  cuda-cccl-12-9-12.9.27-1  |
|  cuda-command-line-tools-12-9-12.9.0-1  |
|  cuda-compiler-12-9-12.9.0-1  |
|  cuda-crt-12-9-12.9.41-1  |
|  cuda-cudart-12-9-12.9.37-1  |
|  cuda-cudart-devel-12-9-12.9.37-1  |
|  cuda-cuobjdump-12-9-12.9.26-1  |
|  cuda-cupti-12-9-12.9.19-1  |
|  cuda-cuxxfilt-12-9-12.9.19-1  |
|  cuda-demo-suite-12-9-12.9.19-1  |
|  cuda-documentation-12-9-12.9.43-1  |
|  cuda-driver-devel-12-9-12.9.37-1  |
|  cuda-gdb-12-9-12.9.19-1  |
|  cuda-gdb-src-12-9-12.9.19-1  |
|  cuda-libraries-12-9-12.9.0-1  |
|  cuda-libraries-devel-12-9-12.9.0-1  |
|  cuda-minimal-build-12-9-12.9.0-1  |
|  cuda-nsight-12-9-12.9.19-1  |
|  cuda-nsight-compute-12-9-12.9.0-1  |
|  cuda-nsight-systems-12-9-12.9.0-1  |
|  cuda-nvcc-12-9-12.9.41-1  |
|  cuda-nvdisasm-12-9-12.9.19-1  |
|  cuda-nvml-devel-12-9-12.9.40-1  |
|  cuda-nvprof-12-9-12.9.19-1  |
|  cuda-nvprune-12-9-12.9.19-1  |
|  cuda-nvrtc-12-9-12.9.41-1  |
|  cuda-nvrtc-devel-12-9-12.9.41-1  |
|  cuda-nvtx-12-9-12.9.19-1  |
|  cuda-nvvm-12-9-12.9.41-1  |
|  cuda-nvvp-12-9-12.9.19-1  |
|  cuda-opencl-12-9-12.9.19-1  |
|  cuda-opencl-devel-12-9-12.9.19-1  |
|  cuda-profiler-api-12-9-12.9.19-1  |
|  cuda-runtime-12-9-12.9.0-1  |
|  cuda-sandbox-devel-12-9-12.9.19-1  |
|  cuda-sanitizer-12-9-12.9.27-1  |
|  cuda-toolkit-12-9-12.9.0-1  |
|  cuda-toolkit-12-9-config-common-12.9.37-1  |
|  cuda-tools-12-9-12.9.0-1  |
|  cuda-visual-tools-12-9-12.9.0-1  |
|  gds-tools-12-9-1.14.0.30-1  |
|  libcublas-12-9-12.9.0.13-1  |
|  libcublas-devel-12-9-12.9.0.13-1  |
|  libcufft-12-9-11.4.0.6-1  |
|  libcufft-devel-12-9-11.4.0.6-1  |
|  libcufile-12-9-1.14.0.30-1  |
|  libcufile-devel-12-9-1.14.0.30-1  |
|  libcurand-12-9-10.3.10.19-1  |
|  libcurand-devel-12-9-10.3.10.19-1  |
|  libcusolver-12-9-11.7.4.40-1  |
|  libcusolver-devel-12-9-11.7.4.40-1  |
|  libcusparse-12-9-12.5.9.5-1  |
|  libcusparse-devel-12-9-12.5.9.5-1  |
|  libnpp-12-9-12.4.0.27-1  |
|  libnpp-devel-12-9-12.4.0.27-1  |
|  libnvfatbin-12-9-12.9.19-1  |
|  libnvfatbin-devel-12-9-12.9.19-1  |
|  libnvjitlink-12-9-12.9.41-1  |
|  libnvjitlink-devel-12-9-12.9.41-1  |
|  libnvjpeg-12-9-12.4.0.16-1  |
|  libnvjpeg-devel-12-9-12.4.0.16-1  |
|  nsight-compute-2025.2.0-2025.2.0.11-1  |
|  nsight-systems-2025.1.3-2025.1.3.140\_251335620677v0-0  |
|  nvidia-gds-12-9-12.9.0-1  |
|  nvlsm-2025.03.1-1  |

### Nvidia Updated Packages
<a name="amis-2023.7.20250527.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-12.9.0-1  |
|  cuda-toolkit-12.9.0-1  |
|  cuda-toolkit-12-12.9.0-1  |
|  cuda-toolkit-12-config-common-12.9.37-1  |
|  cuda-toolkit-config-common-12.9.37-1  |
|  nvidia-fs-2.25.6-1  |
|  nvidia-fs-dkms-2.25.6-1  |
|  nvidia-gds-12.9.0-1  |

## Image Updates
<a name="ami-updates-2023.7.20250527"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250527.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.5.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  dnf-plugin-support-info-1.6-1.amzn2023  |
|  glibc-all-langpacks-2.34-181.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-181.amzn2023.0.1  |
|  glibc-locale-source-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  kernel-libbpf-6.12.29-33.102.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250527-0.amzn2023  |
|  kernel-tools-6.12.29-33.102.amzn2023  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  lsof-4.94.0-1.amzn2023.0.3  |
|  python3-gpg-1.23.2-182.amzn2023.0.1  |
|  system-release-2023.7.20250527-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250527.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.5.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  dnf-plugin-support-info-1.6-1.amzn2023  |
|  glibc-all-langpacks-2.34-181.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-locale-source-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  kernel-libbpf-6.12.29-33.102.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250527-0.amzn2023  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  python3-gpg-1.23.2-182.amzn2023.0.1  |
|  system-release-2023.7.20250527-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250527.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.5.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  dnf-plugin-support-info-1.6-1.amzn2023  |
|  glibc-all-langpacks-2.34-181.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-181.amzn2023.0.1  |
|  glibc-locale-source-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  kernel-libbpf-6.12.29-33.102.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250527-0.amzn2023  |
|  kernel-tools-6.12.29-33.102.amzn2023  |
|  kernel6.12-6.12.29-33.102.amzn2023  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  lsof-4.94.0-1.amzn2023.0.3  |
|  python3-gpg-1.23.2-182.amzn2023.0.1  |
|  system-release-2023.7.20250527-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250527.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.5.5-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  dnf-plugin-support-info-1.6-1.amzn2023  |
|  glibc-all-langpacks-2.34-181.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-locale-source-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  kernel-libbpf-6.12.29-33.102.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250527-0.amzn2023  |
|  kernel6.12-6.12.29-33.102.amzn2023  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  python3-gpg-1.23.2-182.amzn2023.0.1  |
|  system-release-2023.7.20250527-0.amzn2023  |

### Default Container
<a name="amis-2023.7.20250527.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  python3-gpg-1.23.2-182.amzn2023.0.1  |
|  system-release-2023.7.20250527-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250527.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250527-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.1  |
|  glibc-common-2.34-181.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-181.amzn2023.0.1  |
|  glibc-2.34-181.amzn2023.0.1  |
|  gpgme-1.23.2-182.amzn2023.0.1  |
|  libtasn1-4.19.0-1.amzn2023.0.5  |
|  system-release-2023.7.20250527-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250527.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
