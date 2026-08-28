---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250808.html
---

# Amazon Linux 2023 version 2023.8.20250808 release notes
<a name="relnotes-2023.8.20250808"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250808.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250808)
+ [Repository Updates](#repository-updates-2023.8.20250808)
  + [Core Updated Packages](#amis-2023.8.20250808.Core-Updated-Packages)
  + [Nvidia Updated Packages](#amis-2023.8.20250808.Nvidia-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250808)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250808.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250808.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250808.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250808.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250808.Default-Container)
  + [Minimal Container](#amis-2023.8.20250808.Minimal-Container)
+ [Contact us](#amis-2023.8.20250808.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250808"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `This release fixes the kernel soft lockup issues encountered in version [2023.8.20250804].`

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250808"></a>

### Core Updated Packages
<a name="amis-2023.8.20250808.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.12.82-1.amzn2023.0.9  |
|  aws-kinesis-agent-2.0.13-1.amzn2023  |
|  awscli-2-2.27.57-1.amzn2023.0.1  |
|  cni-plugins-1.7.1-1.amzn2023.0.2  |
|  ecs-init-1.97.0-1.amzn2023  |
|  fasterxml-oss-parent-58-2.amzn2023.0.1  |
|  ghostscript-9.56.1-7.amzn2023.0.18  |
|  google-noto-fonts-20240401-1.amzn2023.0.2  |
|  httpd-2.4.64-1.amzn2023.0.1  |
|  jackson-annotations-2.16.1-3.amzn2023.0.1  |
|  jackson-bom-2.16.1-3.amzn2023.0.1  |
|  jackson-core-2.16.1-4.amzn2023.0.1  |
|  jackson-databind-2.16.1-4.amzn2023.0.1  |
|  jackson-parent-2.16-4.amzn2023.0.1  |
|  jakarta-mail-1.6.5-8.amzn2023.0.2  |
|  kernel-6.1.147-172.266.amzn2023  |
|  kernel6.12-6.12.40-63.114.amzn2023  |
|  libmicrohttpd-0.9.73-1.amzn2023.0.4  |
|  libsoup3-3.6.5-50.amzn2023  |
|  libxslt-1.1.43-1.amzn2023.0.2  |
|  memcached-1.6.38-2.amzn2023.0.1  |
|  microcode\_ctl-2.1-53.amzn2023.0.13  |
|  network-flow-monitor-agent-0.2.0-1.amzn2023.0.1  |
|  nodejs-18.20.8-1.amzn2023.0.2  |
|  pam-1.5.1-8.amzn2023.0.6  |
|  python-awscrt-0.26.1-1.amzn2023.0.1  |
|  ruby3.2-3.2.8-184.amzn2023.0.4  |
|  runfinch-finch-1.10.0-1.amzn2023.0.2  |
|  samba-4.17.12-1.amzn2023.0.2  |
|  seahorse-47.0.1-1.amzn2023.0.1  |
|  selinux-policy-38.1.50-1.amzn2023.0.2  |
|  system-release-2023.8.20250808-0.amzn2023  |
|  systemd-252.23-6.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.8  |

### Nvidia Updated Packages
<a name="amis-2023.8.20250808.Nvidia-Updated-Packages"></a>

This section provides details about nvidia updated packages.

|  |
| --- |
|  cuda-compat-12-8-570.172.08-1.amzn2023  |
|  cuda-drivers-570.172.08-1.amzn2023  |
|  kmod-nvidia-latest-dkms-570.172.08-1.amzn2023  |
|  kmod-nvidia-open-dkms-570.172.08-1.amzn2023  |
|  libnvidia-cfg-570.172.08-1.amzn2023  |
|  libnvidia-ml-570.172.08-1.amzn2023  |
|  libnvidia-nscq-570-570.172.08-1  |
|  libnvsdm-570-570.172.08-1  |
|  nvidia-driver-cuda-570.172.08-1.amzn2023  |
|  nvidia-driver-cuda-libs-570.172.08-1.amzn2023  |
|  nvidia-fabric-manager-570.172.08-1  |
|  nvidia-fabric-manager-devel-570.172.08-1  |
|  nvidia-imex-570-570.172.08-1  |
|  nvidia-kmod-common-570.172.08-1.amzn2023  |
|  nvidia-modprobe-570.172.08-1.amzn2023  |
|  nvidia-open-570.172.08-1.amzn2023  |
|  nvidia-persistenced-570.172.08-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.8.20250808"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250808.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-libbpf-1:6.1.147-172.266.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-tools-1:6.1.147-172.266.amzn2023  |
|  kernel-1:6.1.147-172.266.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250808.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-libbpf-1:6.1.147-172.266.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-1:6.1.147-172.266.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250808.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-63.114.amzn2023  |
|  kernel6.12-tools-1:6.12.40-63.114.amzn2023  |
|  kernel6.12-1:6.12.40-63.114.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250808.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250808-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-63.114.amzn2023  |
|  kernel6.12-1:6.12.40-63.114.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

### Default Container
<a name="amis-2023.8.20250808.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250808-0.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250808.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250808-0.amzn2023  |
|  system-release-2023.8.20250808-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250808.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
