---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20260831.html
---

# Amazon Linux 2023 version 2023.12.20260831 release notes
<a name="relnotes-2023.12.20260831"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20260831.

**Contents**
+ [Special Announcements](#announcements-2023.12.20260831)
+ [Release Summary](#release-summary-2023.12.20260831)
+ [Repository Updates](#repository-updates-2023.12.20260831)
  + [Core New Packages](#amis-2023.12.20260831.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20260831.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20260831)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20260831.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20260831.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20260831.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20260831.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20260831.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20260831.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20260831.Default-Container)
  + [Minimal Container](#amis-2023.12.20260831.Minimal-Container)
+ [Contact us](#amis-2023.12.20260831.contact-us)

## Special Announcements
<a name="announcements-2023.12.20260831"></a>

**Note**
Amazon Linux now includes a curated virtualization stack for development, testing, and CI use cases. This stack includes QEMU (system and userspace emulation for x86\_64 and aarch64), libvirt for VM lifecycle management, and boot firmware (SeaBIOS, EDK2 UEFI). It ships with modern virtio devices for storage and networking, with passt for unprivileged user-mode networking.
This is not a production hypervisor. Features such as live migration, suspend/resume across QEMU versions, and legacy device emulation are not supported. We recommend Amazon EC2 for production virtualization workloads.
Security patches are provided for all included components.
The Amazon Linux team plans to update FreeRDP from version 3.6.3 to 3.31.0 in the next release. Plan to upgrade to FreeRDP 3.31 and recompile software that is bound to the old ABI. For a full list of changes, see the [FreeRDP releases page](https://github.com/FreeRDP/FreeRDP/releases) on the GitHub website.

## Release Summary
<a name="release-summary-2023.12.20260831"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ `btrfs-progs` has been promoted from SPAL to the core repository and updated to version 7.1. This release is experimental. Before running production workloads, thoroughly test `btrfs-progs` and the btrfs filesystem in a non-production environment to confirm it meets your requirements. For usage and configuration, see the [official btrfs documentation](https://btrfs.readthedocs.io).
+ In FreeRDP, the embedded CLI and parsing of CLI options in `.rdp` files have been disabled. Update existing `.rdp` files to not use "/" options. For more information, see the official advisory.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20260831"></a>

### Core New Packages
<a name="amis-2023.12.20260831.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  btrfs-progs-7.1-1.amzn2023  |
|  edk2-20260508-1.amzn2023  |
|  isa-l-2.32.1-2.amzn2023.0.1  |
|  libvirt-12.0.0-3.amzn2023.0.1  |
|  libvirt-python-12.0.0-1.amzn2023.0.2  |
|  passt-0^20260716.g090d739-2.amzn2023  |
|  python-qemu-qmp-0.0.5-2.amzn2023  |
|  seabios-1.17.0-1.amzn2023  |

### Core Updated Packages
<a name="amis-2023.12.20260831.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  alsa-lib-1.2.7.2-1.amzn2023.0.4  |
|  amazon-efs-utils-3.3.1-1.amzn2023  |
|  apr-util-1.6.5-1.amzn2023.0.1  |
|  aws-nitro-enclaves-cli-1.5.0-0.amzn2023  |
|  clamav1.4-1.4.6-1.amzn2023.0.1  |
|  clamav1.5-1.5.4-1.amzn2023.0.1  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.5  |
|  criu-3.17.1-1.amzn2023.0.4  |
|  dotnet10.0-10.0.111-1.amzn2023.0.1  |
|  dotnet8.0-8.0.130-1.amzn2023.0.1  |
|  dotnet9.0-9.0.120-1.amzn2023.0.1  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-hibinit-agent-1.0.12-0.amzn2023  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  ecs-init-1.106.1-1.amzn2023  |
|  firefox-140.14.0-1.amzn2023.0.1  |
|  flatpak-1.18.1-1.amzn2023  |
|  freerdp-3.6.3-1.amzn2023.0.15  |
|  gd-2.3.3-5.amzn2023.0.5  |
|  golang-1.26.7-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.6  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.8  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.12  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.5  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2023.0.6  |
|  golist-0.10.4-12.amzn2023.0.14  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.9  |
|  gstreamer1-plugins-good-1.24.10-1.amzn2023.0.8  |
|  iperf3-3.19.1-1.amzn2023.0.1  |
|  iscsi-initiator-utils-6.2.1.4-10.git2a8f9d8.amzn2023.0.4  |
|  jackson-databind-2.21.5-2.amzn2023.0.1  |
|  java-1.8.0-amazon-corretto-1.8.0\_504.b01-1.amzn2023  |
|  java-11-amazon-corretto-11.0.32\+10-1.amzn2023  |
|  java-17-amazon-corretto-17.0.20\+10-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.12\+9-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.4\+8-1.amzn2023.1  |
|  java-26-amazon-corretto-26.0.2\+11-1.amzn2023.1  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-6.1.182-227.379.amzn2023  |
|  kernel6.12-6.12.103-127.188.amzn2023  |
|  kernel6.18-6.18.44-99.149.amzn2023  |
|  libXfont2-2.0.7-1.amzn2023.0.3  |
|  libgit2-1.6.4-116.amzn2023  |
|  libsoup-2.72.0-6.amzn2023.0.13  |
|  libsoup3-3.6.6-59.amzn2023  |
|  log4j-2.17.2-1.amzn2023.0.6  |
|  microcode\_ctl-2.1-53.amzn2023.0.16  |
|  openssl-3.5.7-2.amzn2023.0.2  |
|  perl-DBI-1.652-1.amzn2023.0.1  |
|  postgresql15-15.19-1.amzn2023.0.1  |
|  postgresql16-16.15-1.amzn2023.0.1  |
|  postgresql17-17.11-1.amzn2023.0.1  |
|  postgresql18-18.6-1.amzn2023.0.1  |
|  python-pip-21.3.1-2.amzn2023.0.21  |
|  python3.11-3.11.16-1.amzn2023.0.1  |
|  python3.11-pip-22.3.1-2.amzn2023.0.14  |
|  python3.12-3.12.14-2.amzn2023.0.1  |
|  python3.12-pip-23.2.1-4.amzn2023.0.11  |
|  python3.13-3.13.15-1.amzn2023.0.1  |
|  python3.13-pip-24.2-259.amzn2023.0.8  |
|  python3.14-3.14.7-1.amzn2023.0.1  |
|  python3.14-pip-26.1.1-1.amzn2023.0.3  |
|  qemu-11.0.0-1.amzn2023  |
|  rsyslog-8.2204.0-3.amzn2023.0.5  |
|  rust-cargo-c-0.10.21-1.amzn2023.0.2  |
|  swiftlang-6.3-1.amzn2023.0.2  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  tomcat10-10.1.59-1.amzn2023.0.1  |
|  tomcat9-9.0.121-1.amzn2023.0.1  |
|  udisks2-2.10.1-6.amzn2023.0.4  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-9.2.920-1.amzn2023.0.1  |
|  wireshark-4.6.8-1.amzn2023.0.1  |
|  zip-3.0-28.amzn2023.0.4  |

## Image Updates
<a name="ami-updates-2023.12.20260831"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20260831.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-hibinit-agent-1.0.12-0.amzn2023  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel6.18-tools-1:6.18.44-99.149.amzn2023  |
|  kernel6.18-1:6.18.44-99.149.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-common-2:9.2.920-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.920-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |
|  xxd-2:9.2.920-1.amzn2023.0.1  |
|  zip-3.0-28.amzn2023.0.4  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20260831.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel6.18-1:6.18.44-99.149.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20260831.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-hibinit-agent-1.0.12-0.amzn2023  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel6.12-tools-1:6.12.103-127.188.amzn2023  |
|  kernel6.12-1:6.12.103-127.188.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-common-2:9.2.920-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.920-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |
|  xxd-2:9.2.920-1.amzn2023.0.1  |
|  zip-3.0-28.amzn2023.0.4  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20260831.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel6.12-1:6.12.103-127.188.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20260831.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-hibinit-agent-1.0.12-0.amzn2023  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel-tools-1:6.1.182-227.379.amzn2023  |
|  kernel-1:6.1.182-227.379.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-common-2:9.2.920-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-enhanced-2:9.2.920-1.amzn2023.0.1  |
|  vim-filesystem-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |
|  xxd-2:9.2.920-1.amzn2023.0.1  |
|  zip-3.0-28.amzn2023.0.4  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20260831.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20260831-0.amzn2023  |
|  dracut-config-generic-102-3.amzn2023.0.4  |
|  dracut-102-3.amzn2023.0.4  |
|  ec2-utils-2.3.0-1.amzn2023.0.1  |
|  kbd-misc-2.4.0-2.amzn2023.0.4  |
|  kbd-2.4.0-2.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20260831-0.amzn2023  |
|  kernel-1:6.1.182-227.379.amzn2023  |
|  microcode\_ctl-2:2.1-53.amzn2023.0.16  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  openssl-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.1  |
|  vim-data-2:9.2.920-1.amzn2023.0.1  |
|  vim-minimal-2:9.2.920-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.12.20260831.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260831-0.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.21  |
|  system-release-2023.12.20260831-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20260831.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20260831-0.amzn2023  |
|  openssl-fips-provider-latest-1:3.5.7-2.amzn2023.0.2  |
|  openssl-libs-1:3.5.7-2.amzn2023.0.2  |
|  system-release-2023.12.20260831-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20260831.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
