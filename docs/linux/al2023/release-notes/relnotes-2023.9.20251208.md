---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20251208.html
---

# Amazon Linux 2023 version 2023.9.20251208 release notes
<a name="relnotes-2023.9.20251208"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.9.20251208.

**Contents**
+ [Release Summary](#release-summary-2023.9.20251208)
+ [Repository Updates](#repository-updates-2023.9.20251208)
  + [Core New Packages](#amis-2023.9.20251208.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.9.20251208.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.9.20251208)
  + [Default Kernel 6.1 AMI](#amis-2023.9.20251208.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.9.20251208.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.9.20251208.Default-Kernel-6-12-AMI)
  + [Minimal Container](#amis-2023.9.20251208.Minimal-Container)
+ [Contact us](#amis-2023.9.20251208.contact-us)

## Release Summary
<a name="release-summary-2023.9.20251208"></a>

This release represents an update to the 9th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ Al2023 minimal container images now fixes the use of dnf flag `--releasever` which was broken in the past. This update also removes `/etc/dnf/vars/releasever` which is made obsolete after this update. Customers are recommended to update to the latest minimal container image with at least system-release-2023.9.20251208-2.amzn2023 to avoid this issue.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.9.20251208"></a>

### Core New Packages
<a name="amis-2023.9.20251208.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  lsscsi-0.32-2.amzn2023.0.1  |
|  nodejs24-typescript-5.9.3-1.amzn2023.0.1  |
|  pyparted-3.13.0-8.amzn2023.0.1  |
|  x265-4.1-2.amzn2023  |
|  yq-4.47.1-11.amzn2023  |

### Core Updated Packages
<a name="amis-2023.9.20251208.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  acpid-2.0.32-4.amzn2023.0.3  |
|  amazon-ecr-credential-helper-0.11.0-1.amzn2023  |
|  amazon-efs-utils-2.4.1-1.amzn2023  |
|  atop-2.12.1-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-37.amzn2023  |
|  aws-nitro-tpm-tools-1.1.0-1.amzn2023  |
|  awscli-2-2.32.1-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.5  |
|  cni-plugins-1.7.1-1.amzn2023.0.3  |
|  containerd-2.1.5-1.amzn2023.0.1  |
|  cups-filters-1.28.16-3.amzn2023.0.5  |
|  curl-8.11.1-4.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.10-0.amzn2023  |
|  ecs-init-1.101.0-1.amzn2023  |
|  exiv2-0.28.5-129.amzn2023  |
|  fetchmail-6.5.7-1.amzn2023  |
|  firefox-140.5.0-1.amzn2023.0.2  |
|  glib2-2.82.2-767.amzn2023  |
|  java-21-amazon-corretto-21.0.9\+11-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.1\+9-1.amzn2023.1  |
|  kernel-6.1.158-180.294.amzn2023  |
|  kernel6.12-6.12.58-82.121.amzn2023  |
|  libheif-1.19.8-1.amzn2023.0.2  |
|  libpng-1.6.37-10.amzn2023.0.7  |
|  libpq-17.7-1.amzn2023.0.1  |
|  libsoup-2.72.0-6.amzn2023.0.8  |
|  libsoup3-3.6.5-53.amzn2023  |
|  linux-firmware-20210208-117.amzn2023.0.7  |
|  llvm19-19.1.7-13.amzn2023.0.2  |
|  lustre-client-2.15.6-25.amzn2023  |
|  nodejs20-typescript-5.9.3-1.amzn2023.0.1  |
|  nodejs22-22.21.1-1.amzn2023.0.1  |
|  nodejs22-typescript-5.9.3-1.amzn2023.0.1  |
|  nodejs24-24.11.1-1.amzn2023.0.1  |
|  nvme-cli-2.13-1.amzn2023.0.3  |
|  openvpn-2.6.12-1.amzn2023.0.3  |
|  postgresql15-15.15-1.amzn2023.0.1  |
|  postgresql16-16.11-1.amzn2023.0.1  |
|  postgresql17-17.7-1.amzn2023.0.1  |
|  pyproject-rpm-macros-1.16.1-1.amzn2023.0.1  |
|  python-awscrt-0.28.4-1.amzn2023.0.1  |
|  python3.11-3.11.14-1.amzn2023.0.2  |
|  python3.12-3.12.12-2.amzn2023.0.2  |
|  python3.13-3.13.3-3.amzn2023.0.8  |
|  python3.9-3.9.25-1.amzn2023.0.1  |
|  rsync-3.4.0-1.amzn2023.0.3  |
|  rust-1.91.0-1.amzn2023.0.1  |
|  soci-snapshotter-0.12.0-1.amzn2023.0.1  |
|  spal-release-2023-4.amzn2023  |
|  sqlite-3.40.0-1.amzn2023.0.7  |
|  system-release-2023.9.20251208-2.amzn2023  |
|  systemd-252.23-10.amzn2023  |
|  unbound-1.17.1-1.amzn2023.0.10  |
|  w3m-0.5.3-66.git20230121.amzn2023.0.2  |

## Image Updates
<a name="ami-updates-2023.9.20251208"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.9.20251208.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  acpid-2.0.32-4.amzn2023.0.3  |
|  amazon-linux-repo-s3-2023.9.20251208-2.amzn2023  |
|  amd-ucode-firmware-20210208-117.amzn2023.0.7  |
|  aws-cfn-bootstrap-2.0-37.amzn2023  |
|  awscli-2-2.32.1-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.5  |
|  curl-minimal-8.11.1-4.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.10-0.amzn2023  |
|  glib2-2.82.2-767.amzn2023  |
|  kernel-libbpf-1:6.1.158-180.294.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251208-2.amzn2023  |
|  kernel-tools-1:6.1.158-180.294.amzn2023  |
|  kernel-1:6.1.158-180.294.amzn2023  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.3  |
|  linux-firmware-whence-20210208-117.amzn2023.0.7  |
|  python3-awscrt-0.28.4-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.1  |
|  python3-3.9.25-1.amzn2023.0.1  |
|  rsync-3.4.0-1.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.91.0-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.7  |
|  system-release-2023.9.20251208-2.amzn2023  |
|  systemd-libs-252.23-10.amzn2023  |
|  systemd-networkd-252.23-10.amzn2023  |
|  systemd-pam-252.23-10.amzn2023  |
|  systemd-resolved-252.23-10.amzn2023  |
|  systemd-udev-252.23-10.amzn2023  |
|  systemd-252.23-10.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.9.20251208.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.9.20251208-2.amzn2023  |
|  amd-ucode-firmware-20210208-117.amzn2023.0.7  |
|  awscli-2-2.32.1-1.amzn2023.0.1  |
|  curl-minimal-8.11.1-4.amzn2023.0.3  |
|  glib2-2.82.2-767.amzn2023  |
|  kernel-libbpf-1:6.1.158-180.294.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251208-2.amzn2023  |
|  kernel-1:6.1.158-180.294.amzn2023  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.3  |
|  linux-firmware-whence-20210208-117.amzn2023.0.7  |
|  python3-awscrt-0.28.4-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.1  |
|  python3-3.9.25-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.7  |
|  system-release-2023.9.20251208-2.amzn2023  |
|  systemd-libs-252.23-10.amzn2023  |
|  systemd-networkd-252.23-10.amzn2023  |
|  systemd-pam-252.23-10.amzn2023  |
|  systemd-resolved-252.23-10.amzn2023  |
|  systemd-udev-252.23-10.amzn2023  |
|  systemd-252.23-10.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.9.20251208.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  acpid-2.0.32-4.amzn2023.0.3  |
|  amazon-linux-repo-s3-2023.9.20251208-2.amzn2023  |
|  amd-ucode-firmware-20210208-117.amzn2023.0.7  |
|  aws-cfn-bootstrap-2.0-37.amzn2023  |
|  awscli-2-2.32.1-1.amzn2023.0.1  |
|  binutils-2.41-50.amzn2023.0.5  |
|  curl-minimal-8.11.1-4.amzn2023.0.3  |
|  ec2-hibinit-agent-1.0.10-0.amzn2023  |
|  glib2-2.82.2-767.amzn2023  |
|  kernel-livepatch-repo-s3-2023.9.20251208-2.amzn2023  |
|  kernel6.12-libbpf-1:6.12.58-82.121.amzn2023  |
|  kernel6.12-tools-1:6.12.58-82.121.amzn2023  |
|  kernel6.12-1:6.12.58-82.121.amzn2023  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.3  |
|  linux-firmware-whence-20210208-117.amzn2023.0.7  |
|  python3-awscrt-0.28.4-1.amzn2023.0.1  |
|  python3-libs-3.9.25-1.amzn2023.0.1  |
|  python3-3.9.25-1.amzn2023.0.1  |
|  rsync-3.4.0-1.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.91.0-1.amzn2023.0.1  |
|  sqlite-libs-3.40.0-1.amzn2023.0.7  |
|  system-release-2023.9.20251208-2.amzn2023  |
|  systemd-libs-252.23-10.amzn2023  |
|  systemd-networkd-252.23-10.amzn2023  |
|  systemd-pam-252.23-10.amzn2023  |
|  systemd-resolved-252.23-10.amzn2023  |
|  systemd-udev-252.23-10.amzn2023  |
|  systemd-252.23-10.amzn2023  |

### Minimal Container
<a name="amis-2023.9.20251208.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.9.20251208-2.amzn2023  |
|  curl-minimal-8.11.1-4.amzn2023.0.3  |
|  glib2-2.82.2-767.amzn2023  |
|  libcurl-minimal-8.11.1-4.amzn2023.0.3  |
|  sqlite-libs-3.40.0-1.amzn2023.0.7  |
|  system-release-2023.9.20251208-2.amzn2023  |

## Contact us
<a name="amis-2023.9.20251208.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
