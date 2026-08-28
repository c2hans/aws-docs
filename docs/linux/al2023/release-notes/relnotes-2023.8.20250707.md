---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250707.html
---

# Amazon Linux 2023 version 2023.8.20250707 release notes
<a name="relnotes-2023.8.20250707"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250707.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250707)
+ [Repository Updates](#repository-updates-2023.8.20250707)
  + [Core New Packages](#amis-2023.8.20250707.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.8.20250707.Core-Updated-Packages)
  + [Nvidia New Packages](#amis-2023.8.20250707.Nvidia-New-Packages)
  + [Nvidia Updated Packages](#amis-2023.8.20250707.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250707)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250707.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250707.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250707.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250707.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250707.Default-Container)
  + [Minimal Container](#amis-2023.8.20250707.Minimal-Container)
+ [Contact us](#amis-2023.8.20250707.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250707"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  **Enhanced Graphical Desktop features:** AL2023 Desktop now includes comprehensive multi-language support, a complete multimedia stack featuring gstreamer framework and ShowTime player, and enhanced input support including on-screen keyboard. Additional improvements include USB Smart card device integration, standard desktop utilities such as PDF viewer and calculator applications, and monitor management capabilities. For more information, see: [AL2023 Graphical Desktop](https://docs.aws.amazon.com/linux/al2023/ug/graphical-desktop-al2023.html).
+  **High-availability Seamless Redundancy (HSR & PRP) module** was disabled on kernels: `kernel-6.1.141-165.249.amzn2023` & `kernel6.12-6.12.35-55.103.amzn2023`
+  Amazon Linux 2023 AMIs with the 6.12 kernel are now listed in the EC2 Launch Instance Wizard on the AWS Console.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250707"></a>

### Core New Packages
<a name="amis-2023.8.20250707.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  kiwi-10.2.26-3.amzn2023  |
|  tuna-0.19-4.amzn2023.0.1  |
|  tuned-2.25.1-2.amzn2023.0.2  |

### Core Updated Packages
<a name="amis-2023.8.20250707.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  blueprint-compiler-0.16.0-16.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  cairo-1.18.0-4.amzn2023.0.2  |
|  cairomm-1.14.5-141.amzn2023  |
|  cairomm1.16-1.18.0-37.amzn2023  |
|  clamav1.4-1.4.3-1.amzn2023.0.1  |
|  cloud-init-22.2.2-1.amzn2023.1.14  |
|  containerd-2.0.5-1.amzn2023.0.2  |
|  dav1d-1.5.1-51.amzn2023  |
|  dkms-3.2.1-182.amzn2023  |
|  docker-25.0.8-1.amzn2023.0.5  |
|  dotnet8.0-8.0.117-1.amzn2023.0.1  |
|  efitools-1.9.2-7.amzn2023.0.3  |
|  fasterxml-oss-parent-49-3.amzn2023.0.1  |
|  firefox-128.12.0-1.amzn2023.0.1  |
|  geocode-glib-3.26.4-1.amzn2023.0.2  |
|  glib2-2.82.2-766.amzn2023  |
|  glibmm2.4-2.66.7-2.amzn2023.0.1  |
|  glibmm2.68-2.82.0-20.amzn2023  |
|  google-noto-cjk-fonts-20230817-2.amzn2023.0.1  |
|  google-noto-fonts-20240401-1.amzn2023.0.1  |
|  graphene-1.10.6-9.amzn2023.0.1  |
|  icu-67.1-7.amzn2023.0.4  |
|  jackson-annotations-2.14.2-1.amzn2023.0.1  |
|  jackson-bom-2.14.2-1.amzn2023.0.1  |
|  jackson-core-2.14.2-1.amzn2023.0.1  |
|  jackson-databind-2.14.2-1.amzn2023.0.1  |
|  jackson-parent-2.14-2.amzn2023.0.1  |
|  kernel-6.1.141-165.249.amzn2023  |
|  kernel6.12-6.12.35-55.103.amzn2023  |
|  mariadb1011-10.11.13-1.amzn2023.0.1  |
|  nerdctl-2.1.2-1.amzn2023.0.1  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.5  |
|  pangomm-2.46.4-101.amzn2023  |
|  pangomm2.48-2.54.0-16.amzn2023  |
|  python-pip-21.3.1-2.amzn2023.0.12  |
|  python-urllib3-1.25.10-5.amzn2023.0.5  |
|  python3.12-3.12.11-2.amzn2023.0.1  |
|  python3.12-pip-23.2.1-4.amzn2023.0.3  |
|  redis6-6.2.14-2.amzn2023.0.6  |
|  runc-1.2.6-1.amzn2023.0.1  |
|  runfinch-finch-1.8.3-1.amzn2023.0.1  |
|  rust-1.87.0-1.amzn2023.0.1  |
|  rust-cargo-c-0.9.32-3.amzn2023.0.3  |
|  soci-snapshotter-0.9.0-1.amzn2023.0.4  |
|  spirv-tools-2024.3-91.amzn2023  |
|  sudo-1.9.15-1.p5.amzn2023.0.2  |
|  svt-av1-2.3.0-47.amzn2023  |
|  system-release-2023.8.20250707-0.amzn2023  |
|  systemd-252.23-4.amzn2023  |
|  tigervnc-1.14.1-3.amzn2023.0.2  |
|  tomcat10-10.1.42-1.amzn2023.0.1  |
|  tomcat9-9.0.106-1.amzn2023.0.1  |
|  valkey-8.0.3-3.amzn2023.0.4  |
|  vim-9.1.1484-1.amzn2023.0.1  |
|  wayland-1.23.0-2.amzn2023.0.2  |
|  xorg-x11-server-21.1.13-5.amzn2023.0.6  |
|  xorg-x11-server-Xwayland-24.1.3-1.amzn2023.0.2  |

### Nvidia New Packages
<a name="amis-2023.8.20250707.Nvidia-New-Packages"></a>

This section provides details about nvidia new packages.

|  |
| --- |
|  nsight-compute-2025.2.1-2025.2.1.3-1  |

### Nvidia Updated Packages
<a name="amis-2023.8.20250707.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-12.9.1-1  |
|  cuda-12-9-12.9.1-1  |
|  cuda-command-line-tools-12-9-12.9.1-1  |
|  cuda-compiler-12-9-12.9.1-1  |
|  cuda-crt-12-9-12.9.86-1  |
|  cuda-cudart-12-9-12.9.79-1  |
|  cuda-cudart-devel-12-9-12.9.79-1  |
|  cuda-cuobjdump-12-9-12.9.82-1  |
|  cuda-cupti-12-9-12.9.79-1  |
|  cuda-cuxxfilt-12-9-12.9.82-1  |
|  cuda-demo-suite-12-9-12.9.79-1  |
|  cuda-documentation-12-9-12.9.88-1  |
|  cuda-driver-devel-12-9-12.9.79-1  |
|  cuda-gdb-12-9-12.9.79-1  |
|  cuda-gdb-src-12-9-12.9.79-1  |
|  cuda-libraries-12-9-12.9.1-1  |
|  cuda-libraries-devel-12-9-12.9.1-1  |
|  cuda-minimal-build-12-9-12.9.1-1  |
|  cuda-nsight-12-9-12.9.79-1  |
|  cuda-nsight-compute-12-9-12.9.1-1  |
|  cuda-nsight-systems-12-9-12.9.1-1  |
|  cuda-nvcc-12-9-12.9.86-1  |
|  cuda-nvdisasm-12-9-12.9.88-1  |
|  cuda-nvml-devel-12-9-12.9.79-1  |
|  cuda-nvprof-12-9-12.9.79-1  |
|  cuda-nvprune-12-9-12.9.82-1  |
|  cuda-nvrtc-12-9-12.9.86-1  |
|  cuda-nvrtc-devel-12-9-12.9.86-1  |
|  cuda-nvtx-12-9-12.9.79-1  |
|  cuda-nvvm-12-9-12.9.86-1  |
|  cuda-nvvp-12-9-12.9.79-1  |
|  cuda-profiler-api-12-9-12.9.79-1  |
|  cuda-runtime-12-9-12.9.1-1  |
|  cuda-sanitizer-12-9-12.9.79-1  |
|  cuda-toolkit-12.9.1-1  |
|  cuda-toolkit-12-12.9.1-1  |
|  cuda-toolkit-12-9-12.9.1-1  |
|  cuda-toolkit-12-9-config-common-12.9.79-1  |
|  cuda-toolkit-12-config-common-12.9.79-1  |
|  cuda-toolkit-config-common-12.9.79-1  |
|  cuda-tools-12-9-12.9.1-1  |
|  cuda-visual-tools-12-9-12.9.1-1  |
|  gds-tools-12-9-1.14.1.1-1  |
|  libcublas-12-9-12.9.1.4-1  |
|  libcublas-devel-12-9-12.9.1.4-1  |
|  libcufft-12-9-11.4.1.4-1  |
|  libcufft-devel-12-9-11.4.1.4-1  |
|  libcufile-12-9-1.14.1.1-1  |
|  libcufile-devel-12-9-1.14.1.1-1  |
|  libcusolver-12-9-11.7.5.82-1  |
|  libcusolver-devel-12-9-11.7.5.82-1  |
|  libcusparse-12-9-12.5.10.65-1  |
|  libcusparse-devel-12-9-12.5.10.65-1  |
|  libnpp-12-9-12.4.1.87-1  |
|  libnpp-devel-12-9-12.4.1.87-1  |
|  libnvfatbin-12-9-12.9.82-1  |
|  libnvfatbin-devel-12-9-12.9.82-1  |
|  libnvidia-container-devel-1.17.8-1  |
|  libnvidia-container-libseccomp2-1.17.8-1  |
|  libnvidia-container-static-1.17.8-1  |
|  libnvidia-container-tools-1.17.8-1  |
|  libnvidia-container1-1.17.8-1  |
|  libnvjitlink-12-9-12.9.86-1  |
|  libnvjitlink-devel-12-9-12.9.86-1  |
|  libnvjpeg-12-9-12.4.0.76-1  |
|  libnvjpeg-devel-12-9-12.4.0.76-1  |
|  nvidia-container-toolkit-1.17.8-1  |
|  nvidia-container-toolkit-base-1.17.8-1  |
|  nvidia-fs-2.25.7-1  |
|  nvidia-fs-dkms-2.25.7-1  |
|  nvidia-gds-12.9.1-1  |
|  nvidia-gds-12-9-12.9.1-1  |

## Image Updates
<a name="ami-updates-2023.8.20250707"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250707.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.14  |
|  cloud-init-22.2.2-1.amzn2023.1.14  |
|  glib2-2.82.2-766.amzn2023  |
|  kernel-libbpf-6.12.35-55.103.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250707-0.amzn2023  |
|  kernel-tools-6.12.35-55.103.amzn2023  |
|  kernel-6.1.141-165.249.amzn2023  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.12  |
|  python3-urllib3-1.25.10-5.amzn2023.0.5  |
|  rust-toolset-srpm-macros-1.87.0-1.amzn2023.0.1  |
|  sudo-1.9.15-1.p5.amzn2023.0.2  |
|  system-release-2023.8.20250707-0.amzn2023  |
|  systemd-libs-252.23-4.amzn2023  |
|  systemd-networkd-252.23-4.amzn2023  |
|  systemd-pam-252.23-4.amzn2023  |
|  systemd-resolved-252.23-4.amzn2023  |
|  systemd-udev-252.23-4.amzn2023  |
|  systemd-252.23-4.amzn2023  |
|  vim-common-2:9.1.1484-1.amzn2023.0.1  |
|  vim-data-2:9.1.1484-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1484-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1484-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1484-1.amzn2023.0.1  |
|  xxd-2:9.1.1484-1.amzn2023.0.1  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250707.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.14  |
|  cloud-init-22.2.2-1.amzn2023.1.14  |
|  glib2-2.82.2-766.amzn2023  |
|  kernel-libbpf-6.12.35-55.103.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250707-0.amzn2023  |
|  kernel-6.1.141-165.249.amzn2023  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.12  |
|  python3-urllib3-1.25.10-5.amzn2023.0.5  |
|  sudo-1.9.15-1.p5.amzn2023.0.2  |
|  system-release-2023.8.20250707-0.amzn2023  |
|  systemd-libs-252.23-4.amzn2023  |
|  systemd-networkd-252.23-4.amzn2023  |
|  systemd-pam-252.23-4.amzn2023  |
|  systemd-resolved-252.23-4.amzn2023  |
|  systemd-udev-252.23-4.amzn2023  |
|  systemd-252.23-4.amzn2023  |
|  vim-data-2:9.1.1484-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1484-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250707.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.14  |
|  cloud-init-22.2.2-1.amzn2023.1.14  |
|  glib2-2.82.2-766.amzn2023  |
|  kernel-libbpf-6.12.35-55.103.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250707-0.amzn2023  |
|  kernel-tools-6.12.35-55.103.amzn2023  |
|  kernel6.12-6.12.35-55.103.amzn2023  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.12  |
|  python3-urllib3-1.25.10-5.amzn2023.0.5  |
|  rust-toolset-srpm-macros-1.87.0-1.amzn2023.0.1  |
|  sudo-1.9.15-1.p5.amzn2023.0.2  |
|  system-release-2023.8.20250707-0.amzn2023  |
|  systemd-libs-252.23-4.amzn2023  |
|  systemd-networkd-252.23-4.amzn2023  |
|  systemd-pam-252.23-4.amzn2023  |
|  systemd-resolved-252.23-4.amzn2023  |
|  systemd-udev-252.23-4.amzn2023  |
|  systemd-252.23-4.amzn2023  |
|  vim-common-2:9.1.1484-1.amzn2023.0.1  |
|  vim-data-2:9.1.1484-1.amzn2023.0.1  |
|  vim-enhanced-2:9.1.1484-1.amzn2023.0.1  |
|  vim-filesystem-2:9.1.1484-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1484-1.amzn2023.0.1  |
|  xxd-2:9.1.1484-1.amzn2023.0.1  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250707.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.14  |
|  cloud-init-22.2.2-1.amzn2023.1.14  |
|  glib2-2.82.2-766.amzn2023  |
|  kernel-libbpf-6.12.35-55.103.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250707-0.amzn2023  |
|  kernel6.12-6.12.35-55.103.amzn2023  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.12  |
|  python3-urllib3-1.25.10-5.amzn2023.0.5  |
|  sudo-1.9.15-1.p5.amzn2023.0.2  |
|  system-release-2023.8.20250707-0.amzn2023  |
|  systemd-libs-252.23-4.amzn2023  |
|  systemd-networkd-252.23-4.amzn2023  |
|  systemd-pam-252.23-4.amzn2023  |
|  systemd-resolved-252.23-4.amzn2023  |
|  systemd-udev-252.23-4.amzn2023  |
|  systemd-252.23-4.amzn2023  |
|  vim-data-2:9.1.1484-1.amzn2023.0.1  |
|  vim-minimal-2:9.1.1484-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.8.20250707.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  glib2-2.82.2-766.amzn2023  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.12  |
|  system-release-2023.8.20250707-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250707.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250707-0.amzn2023  |
|  ca-certificates-2025.2.76-1.0.amzn2023.0.2  |
|  glib2-2.82.2-766.amzn2023  |
|  system-release-2023.8.20250707-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250707.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
