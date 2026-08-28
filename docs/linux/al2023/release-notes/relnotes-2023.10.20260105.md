---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.10.20260105.html
---

# Amazon Linux 2023 version 2023.10.20260105 release notes
<a name="relnotes-2023.10.20260105"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.10.20260105.

**Contents**
+ [Release Summary](#release-summary-2023.10.20260105)
+ [Repository Updates](#repository-updates-2023.10.20260105)
  + [Core New Packages](#amis-2023.10.20260105.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.10.20260105.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.10.20260105.Kernel-livepatch-New-Packages)
+ [Image Updates](#ami-updates-2023.10.20260105)
  + [Default Kernel 6.1 AMI](#amis-2023.10.20260105.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.10.20260105.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.10.20260105.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.10.20260105.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.10.20260105.Default-Container)
  + [Minimal Container](#amis-2023.10.20260105.Minimal-Container)
+ [Contact us](#amis-2023.10.20260105.contact-us)

## Release Summary
<a name="release-summary-2023.10.20260105"></a>

This release represents an update to the 10th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable Updates**
+ systemd-resolved: Fixed an issue where duplicate `nameserver` entries could be emitted into `/etc/resolv.conf` under multi-interface DHCP configurations. This aligns the file with the effective set of upstream DNS servers and may slightly change resolver ordering when duplicates were previously present.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.10.20260105"></a>

### Core New Packages
<a name="amis-2023.10.20260105.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  Cython3.13-3.0.12-2.amzn2023.0.1  |
|  clamav1.5-1.5.1-1.amzn2023.0.4  |
|  corosync-3.1.9-3.amzn2023.0.1  |
|  kronosnet-1.22-1.amzn2023.0.2  |
|  pacemaker-3.0.1-0.4.rc2.amzn2023.0.1  |
|  pcs-0.12.1-1.amzn2023.0.1  |
|  python3.13-cachetools-5.4.0-2.amzn2023.0.1  |
|  python3.13-cffi-1.17.0-1.amzn2023.0.1  |
|  python3.13-chardet-5.2.0-1.amzn2023.0.1  |
|  python3.13-colorama-0.4.6-1.amzn2023.0.1  |
|  python3.13-cryptography-36.0.1-1.amzn2023.0.1  |
|  python3.13-dacite-1.9.2-1.amzn2023.0.1  |
|  python3.13-dateutil-2.8.2-16.amzn2023.0.1  |
|  python3.13-distlib-0.3.8-3.amzn2023.0.1  |
|  python3.13-filelock-3.15.4-1.amzn2023.0.1  |
|  python3.13-hatch-vcs-0.4.0-1.amzn2023.0.1  |
|  python3.13-hatchling-1.27.0-1.amzn2023.0.1  |
|  python3.13-lxml-5.3.2-2.amzn2023.0.1  |
|  python3.13-pathspec-0.12.1-1.amzn2023.0.1  |
|  python3.13-platformdirs-4.2.2-1.amzn2023.0.1  |
|  python3.13-pluggy-1.5.0-1.amzn2023.0.2  |
|  python3.13-pycparser-2.20-1.amzn2023.0.1  |
|  python3.13-pycurl-7.45.4-2.amzn2023.0.1  |
|  python3.13-pyparsing-2.4.7-6.amzn2023.0.1  |
|  python3.13-pyproject-api-1.6.1-1.amzn2023.0.1  |
|  python3.13-semantic\_version-2.10.0-1.amzn2023.0.1  |
|  python3.13-setuptools-rust-1.7.0-1.amzn2023.0.1  |
|  python3.13-setuptools\_scm-8.0.4-109.amzn2023.0.2  |
|  python3.13-six-1.17.0-1.amzn2023.0.1  |
|  python3.13-toml-0.10.2-1.amzn2023.0.1  |
|  python3.13-tornado-6.4.2-1.amzn2023.0.1  |
|  python3.13-tox-4.25.0-1.amzn2023.0.1  |
|  python3.13-tox-current-env-0.0.16-1.amzn2023.0.1  |
|  python3.13-trove-classifiers-2025.3.13.13-1.amzn2023.0.2  |
|  python3.13-typing-extensions-4.12.2-3.amzn2023.0.2  |
|  python3.13-virtualenv-20.21.1-1.amzn2023.0.1  |
|  pytz3.13-2025.2-1.amzn2023.0.1  |
|  resource-agents-4.16.0-2.amzn2023.0.1  |

### Core Updated Packages
<a name="amis-2023.10.20260105.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  BabelfishDump-17.7-1.amzn2023.0.1  |
|  ImageMagick-6.9.13.29-1.amzn2023.0.3  |
|  Xaw3d-1.6.3-5.amzn2023.0.3  |
|  amazon-cloudwatch-agent-1.300062.1-1.amzn2023  |
|  amazon-ecr-credential-helper-0.11.0-2.amzn2023  |
|  amazon-ssm-agent-3.3.3572.0-1.amzn2023  |
|  ansible-8.3.0-1.amzn2023.0.2  |
|  aws-cfn-bootstrap-2.0-38.amzn2023  |
|  awscli-2-2.32.22-1.amzn2023.0.1  |
|  certmonger-0.79.18-2.amzn2023.0.2  |
|  cni-plugins-1.7.1-1.amzn2023.0.4  |
|  containerd-2.1.5-1.amzn2023.0.3  |
|  crash-8.0.5-5.amzn2023.0.1  |
|  cups-2.4.14-1.amzn2023.0.2  |
|  curl-8.15.0-4.amzn2023.0.1  |
|  dnf-plugin-support-info-1.10-1.amzn2023  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  docker-25.0.14-1.amzn2023.0.1  |
|  dracut-102-3.amzn2023.0.2  |
|  ecs-init-1.101.1-1.amzn2023  |
|  ecs-service-connect-agent-v1.34.4.2-1.amzn2023  |
|  firefox-140.6.0-1.amzn2023.0.1  |
|  glib2-2.82.2-769.amzn2023  |
|  golang-1.24.11-1.amzn2023.0.1  |
|  grub2-2.06-61.amzn2023.0.21  |
|  httpd-2.4.66-1.amzn2023.0.1  |
|  kernel-6.1.159-181.297.amzn2023  |
|  kernel6.12-6.12.63-84.121.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libeconf-0.7.9-1.amzn2023.0.1  |
|  libpciaccess-0.16-4.amzn2023.0.3  |
|  libpng-1.6.37-10.amzn2023.0.8  |
|  makedumpfile-1.7.6-1.amzn2023.0.1  |
|  mariadb1011-10.11.15-1.amzn2023.0.1  |
|  nerdctl-2.1.5-1.amzn2023.0.3  |
|  nodejs20-20.19.5-1.amzn2023.0.2  |
|  nodejs22-22.21.1-1.amzn2023.0.2  |
|  nodejs24-24.11.1-1.amzn2023.0.2  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2023.0.7  |
|  openssl-3.2.2-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.8  |
|  perl-IO-Socket-SSL-2.075-1.amzn2023.0.3  |
|  php8.1-8.1.34-1.amzn2023.0.1  |
|  php8.2-8.2.30-1.amzn2023.0.1  |
|  php8.3-8.3.29-1.amzn2023.0.1  |
|  php8.4-8.4.16-1.amzn2023.0.1  |
|  python-awscrt-0.29.1-1.amzn2023.0.1  |
|  python-tornado-6.1.0-2.amzn2023.0.6  |
|  python3.11-3.11.14-1.amzn2023.0.3  |
|  python3.12-3.12.12-2.amzn2023.0.3  |
|  python3.13-3.13.11-1.amzn2023.0.1  |
|  python3.9-3.9.25-1.amzn2023.0.3  |
|  rhino-1.7.14.1-3.amzn2023.0.1  |
|  rng-tools-6.17-1.amzn2023.0.1  |
|  runc-1.3.4-1.amzn2023.0.1  |
|  runfinch-finch-1.10.0-1.amzn2023.0.6  |
|  rust-1.92.0-1.amzn2023.0.1  |
|  soci-snapshotter-0.12.0-1.amzn2023.0.2  |
|  strace-6.12-1.amzn2023.0.1  |
|  system-release-2023.10.20260105-0.amzn2023  |
|  systemd-252.23-11.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.10.20260105.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.155-176.282-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.156-177.286-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.53-69.119-1.0-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.10.20260105"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.10.20260105.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260105-0.amzn2023  |
|  amazon-ssm-agent-3.3.3572.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-38.amzn2023  |
|  awscli-2-2.32.22-1.amzn2023.0.1  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  dnf-plugin-support-info-1.10-1.amzn2023  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  dnf-utils-4.3.0-13.amzn2023.0.6  |
|  dracut-config-generic-102-3.amzn2023.0.2  |
|  dracut-102-3.amzn2023.0.2  |
|  glib2-2.82.2-769.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.21  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.21  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-1:2.06-61.amzn2023.0.21  |
|  kernel-libbpf-1:6.1.159-181.297.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260105-0.amzn2023  |
|  kernel-tools-1:6.1.159-181.297.amzn2023  |
|  kernel-1:6.1.159-181.297.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  libeconf-0.7.9-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  openssl-1:3.2.2-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.8  |
|  python3-awscrt-0.29.1-1.amzn2023.0.1  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  python3-libs-3.9.25-1.amzn2023.0.3  |
|  python3-3.9.25-1.amzn2023.0.3  |
|  rng-tools-6.17-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.92.0-1.amzn2023.0.1  |
|  strace-6.12-1.amzn2023.0.1  |
|  system-release-2023.10.20260105-0.amzn2023  |
|  systemd-libs-252.23-11.amzn2023  |
|  systemd-networkd-252.23-11.amzn2023  |
|  systemd-pam-252.23-11.amzn2023  |
|  systemd-resolved-252.23-11.amzn2023  |
|  systemd-udev-252.23-11.amzn2023  |
|  systemd-252.23-11.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.10.20260105.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260105-0.amzn2023  |
|  awscli-2-2.32.22-1.amzn2023.0.1  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  dnf-plugin-support-info-1.10-1.amzn2023  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  dracut-config-generic-102-3.amzn2023.0.2  |
|  dracut-102-3.amzn2023.0.2  |
|  glib2-2.82.2-769.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.21  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.21  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-1:2.06-61.amzn2023.0.21  |
|  kernel-libbpf-1:6.1.159-181.297.amzn2023  |
|  kernel-livepatch-repo-s3-2023.10.20260105-0.amzn2023  |
|  kernel-1:6.1.159-181.297.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  libeconf-0.7.9-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  openssl-1:3.2.2-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.8  |
|  python3-awscrt-0.29.1-1.amzn2023.0.1  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  python3-libs-3.9.25-1.amzn2023.0.3  |
|  python3-3.9.25-1.amzn2023.0.3  |
|  rng-tools-6.17-1.amzn2023.0.1  |
|  system-release-2023.10.20260105-0.amzn2023  |
|  systemd-libs-252.23-11.amzn2023  |
|  systemd-networkd-252.23-11.amzn2023  |
|  systemd-pam-252.23-11.amzn2023  |
|  systemd-resolved-252.23-11.amzn2023  |
|  systemd-udev-252.23-11.amzn2023  |
|  systemd-252.23-11.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.10.20260105.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260105-0.amzn2023  |
|  amazon-ssm-agent-3.3.3572.0-1.amzn2023  |
|  aws-cfn-bootstrap-2.0-38.amzn2023  |
|  awscli-2-2.32.22-1.amzn2023.0.1  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  dnf-plugin-support-info-1.10-1.amzn2023  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  dnf-utils-4.3.0-13.amzn2023.0.6  |
|  dracut-config-generic-102-3.amzn2023.0.2  |
|  dracut-102-3.amzn2023.0.2  |
|  glib2-2.82.2-769.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.21  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.21  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-1:2.06-61.amzn2023.0.21  |
|  kernel-livepatch-repo-s3-2023.10.20260105-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.63-84.121.amzn2023  |
|  kernel6.12-tools-1:6.12.63-84.121.amzn2023  |
|  kernel6.12-1:6.12.63-84.121.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  libeconf-0.7.9-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  openssl-1:3.2.2-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.8  |
|  python3-awscrt-0.29.1-1.amzn2023.0.1  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  python3-libs-3.9.25-1.amzn2023.0.3  |
|  python3-3.9.25-1.amzn2023.0.3  |
|  rng-tools-6.17-1.amzn2023.0.1  |
|  rust-toolset-srpm-macros-1.92.0-1.amzn2023.0.1  |
|  strace-6.12-1.amzn2023.0.1  |
|  system-release-2023.10.20260105-0.amzn2023  |
|  systemd-libs-252.23-11.amzn2023  |
|  systemd-networkd-252.23-11.amzn2023  |
|  systemd-pam-252.23-11.amzn2023  |
|  systemd-resolved-252.23-11.amzn2023  |
|  systemd-udev-252.23-11.amzn2023  |
|  systemd-252.23-11.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.10.20260105.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.10.20260105-0.amzn2023  |
|  awscli-2-2.32.22-1.amzn2023.0.1  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  dnf-plugin-support-info-1.10-1.amzn2023  |
|  dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  dracut-config-generic-102-3.amzn2023.0.2  |
|  dracut-102-3.amzn2023.0.2  |
|  glib2-2.82.2-769.amzn2023  |
|  grub2-common-1:2.06-61.amzn2023.0.21  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.21  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.21  |
|  grub2-tools-1:2.06-61.amzn2023.0.21  |
|  kernel-livepatch-repo-s3-2023.10.20260105-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.63-84.121.amzn2023  |
|  kernel6.12-1:6.12.63-84.121.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  libeconf-0.7.9-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  openssl-1:3.2.2-1.amzn2023.0.3  |
|  pam-1.5.1-8.amzn2023.0.8  |
|  python3-awscrt-0.29.1-1.amzn2023.0.1  |
|  python3-dnf-plugins-core-4.3.0-13.amzn2023.0.6  |
|  python3-libs-3.9.25-1.amzn2023.0.3  |
|  python3-3.9.25-1.amzn2023.0.3  |
|  rng-tools-6.17-1.amzn2023.0.1  |
|  system-release-2023.10.20260105-0.amzn2023  |
|  systemd-libs-252.23-11.amzn2023  |
|  systemd-networkd-252.23-11.amzn2023  |
|  systemd-pam-252.23-11.amzn2023  |
|  systemd-resolved-252.23-11.amzn2023  |
|  systemd-udev-252.23-11.amzn2023  |
|  systemd-252.23-11.amzn2023  |

### Default Container
<a name="amis-2023.10.20260105.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260105-0.amzn2023  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  glib2-2.82.2-769.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  python3-libs-3.9.25-1.amzn2023.0.3  |
|  python3-3.9.25-1.amzn2023.0.3  |
|  system-release-2023.10.20260105-0.amzn2023  |

### Minimal Container
<a name="amis-2023.10.20260105.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.10.20260105-0.amzn2023  |
|  curl-minimal-8.15.0-4.amzn2023.0.1  |
|  glib2-2.82.2-769.amzn2023  |
|  libcap-2.73-1.amzn2023.0.5  |
|  libcurl-minimal-8.15.0-4.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.3  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.3  |
|  system-release-2023.10.20260105-0.amzn2023  |

## Contact us
<a name="amis-2023.10.20260105.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
