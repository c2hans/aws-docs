---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20260928.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20260928 release notes
<a name="relnotes-2027.0.20260928"></a>

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20260928.

**Contents**
+ [Special Announcements](#announcements-2027.0.20260928)
+ [Release summary](#release-summary-2027.0.20260928)
+ [Repository Updates](#repository-updates-2027.0.20260928)
  + [Core New Packages](#amis-2027.0.20260928.Core-New-Packages)
  + [Core Updated Packages](#amis-2027.0.20260928.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20260928)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20260928.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20260928.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20260928.Default-Container)
  + [Minimal Container](#amis-2027.0.20260928.Minimal-Container)
+ [Contact us](#amis-2027.0.20260928.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

## Special Announcements
<a name="announcements-2027.0.20260928"></a>
+ On-premises images are now available in the AL2027 public preview. You can download images in VMware OVA, KVM/QEMU qcow2, Hyper-V VHDx, and raw formats from [https://cdn-al2027.amazonlinux.com/os-images/latest/](https://cdn-al2027.amazonlinux.com/os-images/latest/) to run AL2027 on your own virtualization platforms.

  As with all preview components, these images are pre-release, aren't covered by AWS Support, and should be used only for evaluation and validation, not production. For production workloads, continue to run AL2023 until AL2027 reaches general availability.
+ AL2027 now ships NVIDIA repositories, which include the NVIDIA Linux GPU driver and CUDA. AL2027 will add more NVIDIA packages to these repositories in future releases. For more information, see [NVIDIA drivers](https://docs.aws.amazon.com/linux/al2027/ug/nvidia-drivers.html).

## Release summary
<a name="release-summary-2027.0.20260928"></a>

This release is an update to the AL2027 preview.

**Notable updates**
+ By default, we reduce the scope of ptrace for processes to their own sub-processes only. `kernel.yama.ptrace_scope` now defaults to `1` by removing the hard requirement on `elfutils-default-yama-scope` in the `elfutils-libs` package. Developer and debugging tools that need unrestricted ptrace can install the opt-in enabler package `elfutils-yama-ptrace-enable`. This package also provides `default-yama-scope` for backward compatibility.
+ The `mariadb1011`, `mariadb114`, `mariadb118`, `mariadb123`, and `mariadb-connector-c` packages are now built against AWS-LC instead of OpenSSL.
+ Starting with kernel version `kernel7.2-7.2.4-4.107.amzn2027`, AL2027 ships kernel modules in zstd-compressed format with a `.ko.zst` file extension, instead of the previous uncompressed `.ko` format. The kernel decompresses modules at load time. We recommend that you test any workloads that use kernel modules on this kernel and switch to compression-agnostic tooling such as `modprobe`. This is included in the `kmod-34.2-2.amzn2027.0.1` release.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

**Known issues**
+ The NVIDIA repositories do not yet support repository metadata signing. Signing support will be added in an upcoming release. For more information, see [Repository metadata signing in AL2027](https://docs.aws.amazon.com/linux/al2027/ug/repo-metadata-signing.html).
+ The `systemtap` package does not function on kernel 7.2 because of a kernel function signature change. If you need to use `systemtap`, remain on kernel 7.1. This issue will be fixed in the next release, which updates `systemtap` to version 5.6.

## Repository Updates
<a name="repository-updates-2027.0.20260928"></a>

### Core New Packages
<a name="amis-2027.0.20260928.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  adwaita-fonts-50.0-1.amzn2027  |
|  btrfs-progs-7.1-1.amzn2027  |
|  kernel7.2-7.2.4-4.107.amzn2027  |
|  nvidia-release-2027-1.amzn2027  |
|  python-async-generator-1.10-9.amzn2027.0.2  |
|  python-atomicwrites-1.4.0-6.amzn2027  |
|  python-fs-2.4.16-17.amzn2027.0.1  |
|  python-impacket-0.12.0-1.amzn2027  |
|  python-ldap3-2.9.1-15.amzn2027  |
|  python-parameterized-0.9.0-1.amzn2027.0.2  |
|  python-pycryptodomex-3.23.0-4.amzn2027.0.1  |
|  python-pyrsistent-0.20.0-1.amzn2027  |
|  python-pytest-runner-4.0-31.amzn2027.0.2  |
|  python-text-unidecode-1.3-24.amzn2027.0.2  |

### Core Updated Packages
<a name="amis-2027.0.20260928.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  autotrace-0.31.9-18.amzn2027  |
|  bind-9.18.50-1.amzn2027.0.6  |
|  bison-3.8.2-11.amzn2027.0.3  |
|  c-ares-1.34.8-1.amzn2027.0.1  |
|  cloud-init-26.1-250.amzn2027.0.7  |
|  composer-2.10.3-1.amzn2027  |
|  crash-9.0.2-2.amzn2027.0.2  |
|  credentials-fetcher-2.0.3-1.amzn2027.0.5  |
|  curl-8.21.0-5.amzn2027.0.1  |
|  dnsmasq-2.93-2.amzn2027  |
|  dotnet10.0-10.0.112-1.amzn2027.0.1  |
|  elfutils-0.195-1.amzn2027.0.1  |
|  environment-modules-5.6.1-4.amzn2027  |
|  expat-2.8.3-1.amzn2027  |
|  freeipmi-1.6.19-1.amzn2027  |
|  freerdp-3.31.0-1.amzn2027  |
|  freetype-2.14.3-1.amzn2027.0.3  |
|  gawk-5.4.1-1.amzn2027  |
|  gdm-50.1-2.amzn2027  |
|  gnome-control-center-50.3-2.amzn2027  |
|  golang-1.26.8-1.amzn2027.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2027.0.6  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2027.0.8  |
|  golang-github-cpuguy83-md2man-2.0.7-38.amzn2027.0.3  |
|  golang-github-urfave-cli-1.22.10-2.amzn2027.0.5  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2027.0.7  |
|  golist-0.10.4-12.amzn2027.0.14  |
|  grub2-2.12-58.amzn2027.0.3  |
|  gstreamer1-plugins-base-1.28.6-1.amzn2027.0.1  |
|  gvfs-1.60.2-2.amzn2027  |
|  jsoup-1.23.2-1.amzn2027  |
|  kernel7.1-7.1.13-89.102.amzn2027  |
|  kmod-34.2-2.amzn2027.0.1  |
|  krb5-1.22.2-7.amzn2027  |
|  libheif-1.23.4-1.amzn2027  |
|  libsoup3-3.7.3-1.amzn2027  |
|  mariadb-connector-c-3.4.8-3.amzn2027.0.3  |
|  mariadb1011-10.11.18-1.amzn2027.0.2  |
|  mariadb114-11.4.12-1.amzn2027.0.2  |
|  mariadb118-11.8.8-1.amzn2027.0.2  |
|  mariadb123-12.3.2-2.amzn2027.0.2  |
|  mock-core-configs-44.4-2.amzn2027  |
|  nagios-plugins-2.4.12-4.amzn2027.0.2  |
|  nginx-mod-njs-1.0.1-1.amzn2027.0.1  |
|  nodejs24-24.21.0-1.amzn2027.0.1  |
|  openexr-3.2.4-7.amzn2027.0.1  |
|  openssl-3.5.8-2.amzn2027  |
|  pcre2-10.48-1.amzn2027.0.1  |
|  perl-Authen-SASL-2.2100-1.amzn2027.0.1  |
|  perl-DBD-MariaDB-1.24-4.amzn2027.0.3  |
|  perl-Net-DNS-1.57-1.amzn2027.0.1  |
|  perl-YAML-1.32.1-1.amzn2027  |
|  php8.5-8.5.10-1.amzn2027.0.1  |
|  python-mistune-3.3.0-1.amzn2027.0.2  |
|  python-pymongo-4.13.2-4.amzn2027.0.2  |
|  python-tornado-6.5.8-1.amzn2027.0.1  |
|  python3.14-3.14.7-1.amzn2027.0.7  |
|  rclone-1.75.1-82.amzn2027  |
|  rpm-6.0.0-1.amzn2027.0.6  |
|  rsync-3.5.1-1.amzn2027.0.1  |
|  rsyslog-8.2604.0-3.amzn2027.0.1  |
|  sssd-2.13.1-1.amzn2027.0.2  |
|  system-release-2027.0.20260928-0.amzn2027  |
|  tomcat-native-2.0.15-1.amzn2027.0.1  |
|  tomcat10-10.1.59-1.amzn2027.0.1  |
|  tomcat9-9.0.121-1.amzn2027.0.1  |
|  unbound-1.26.0-1.amzn2027  |
|  valkey-9.0.6-1.amzn2027.0.1  |
|  wget1-1.25.0-5.amzn2027  |
|  yelp-tools-42.1-2.amzn2027.0.1  |
|  zip-3.0-44.amzn2027.0.3  |

## Image Updates
<a name="ami-updates-2027.0.20260928"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20260928.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20260928-0.amzn2027  |
|  c-ares-1.34.8-1.amzn2027.0.1  |
|  cloud-init-cfg-ec2-26.1-250.amzn2027.0.7  |
|  cloud-init-26.1-250.amzn2027.0.7  |
|  curl-8.21.0-5.amzn2027.0.1  |
|  elfutils-libelf-0.195-1.amzn2027.0.1  |
|  elfutils-libs-0.195-1.amzn2027.0.1  |
|  expat-2.8.3-1.amzn2027  |
|  gawk-5.4.1-1.amzn2027  |
|  grub2-common-1:2.12-58.amzn2027.0.3  |
|  grub2-efi-x64-ec2-1:2.12-58.amzn2027.0.3  |
|  grub2-pc-modules-1:2.12-58.amzn2027.0.3  |
|  grub2-tools-minimal-1:2.12-58.amzn2027.0.3  |
|  grub2-tools-1:2.12-58.amzn2027.0.3  |
|  kernel7.2-tools-1:7.2.4-4.107.amzn2027  |
|  kernel7.2-1:7.2.4-4.107.amzn2027  |
|  kmod-libs-34.2-2.amzn2027.0.1  |
|  kmod-34.2-2.amzn2027.0.1  |
|  krb5-libs-1.22.2-7.amzn2027  |
|  libcurl-minimal-8.21.0-5.amzn2027.0.1  |
|  libsss\_certmap-2.13.1-1.amzn2027.0.2  |
|  libsss\_idmap-2.13.1-1.amzn2027.0.2  |
|  libsss\_nss\_idmap-2.13.1-1.amzn2027.0.2  |
|  libsss\_sudo-2.13.1-1.amzn2027.0.2  |
|  openssl-fips-provider-latest-1:3.5.8-2.amzn2027  |
|  openssl-libs-1:3.5.8-2.amzn2027  |
|  openssl-1:3.5.8-2.amzn2027  |
|  pcre2-syntax-10.48-1.amzn2027.0.1  |
|  pcre2-10.48-1.amzn2027.0.1  |
|  python3-libs-3.14.7-1.amzn2027.0.7  |
|  python3-3.14.7-1.amzn2027.0.7  |
|  rpm-build-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-plugin-selinux-6.0.0-1.amzn2027.0.6  |
|  rpm-plugin-systemd-inhibit-6.0.0-1.amzn2027.0.6  |
|  rpm-sign-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-6.0.0-1.amzn2027.0.6  |
|  sssd-client-2.13.1-1.amzn2027.0.2  |
|  sssd-common-2.13.1-1.amzn2027.0.2  |
|  sssd-kcm-2.13.1-1.amzn2027.0.2  |
|  sssd-krb5-common-2.13.1-1.amzn2027.0.2  |
|  system-release-2027.0.20260928-0.amzn2027  |
|  zip-3.0-44.amzn2027.0.3  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20260928.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20260928-0.amzn2027  |
|  cloud-init-cfg-ec2-26.1-250.amzn2027.0.7  |
|  cloud-init-26.1-250.amzn2027.0.7  |
|  curl-8.21.0-5.amzn2027.0.1  |
|  elfutils-libelf-0.195-1.amzn2027.0.1  |
|  expat-2.8.3-1.amzn2027  |
|  gawk-5.4.1-1.amzn2027  |
|  grub2-common-1:2.12-58.amzn2027.0.3  |
|  grub2-efi-x64-ec2-1:2.12-58.amzn2027.0.3  |
|  grub2-pc-modules-1:2.12-58.amzn2027.0.3  |
|  grub2-tools-minimal-1:2.12-58.amzn2027.0.3  |
|  grub2-tools-1:2.12-58.amzn2027.0.3  |
|  kernel7.2-1:7.2.4-4.107.amzn2027  |
|  kmod-libs-34.2-2.amzn2027.0.1  |
|  kmod-34.2-2.amzn2027.0.1  |
|  krb5-libs-1.22.2-7.amzn2027  |
|  libcurl-minimal-8.21.0-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-2.amzn2027  |
|  openssl-libs-1:3.5.8-2.amzn2027  |
|  openssl-1:3.5.8-2.amzn2027  |
|  pcre2-syntax-10.48-1.amzn2027.0.1  |
|  pcre2-10.48-1.amzn2027.0.1  |
|  python3-libs-3.14.7-1.amzn2027.0.7  |
|  python3-3.14.7-1.amzn2027.0.7  |
|  rpm-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-plugin-selinux-6.0.0-1.amzn2027.0.6  |
|  rpm-plugin-systemd-inhibit-6.0.0-1.amzn2027.0.6  |
|  rpm-6.0.0-1.amzn2027.0.6  |
|  system-release-2027.0.20260928-0.amzn2027  |

### Default Container
<a name="amis-2027.0.20260928.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20260928-0.amzn2027  |
|  curl-8.21.0-5.amzn2027.0.1  |
|  gawk-5.4.1-1.amzn2027  |
|  krb5-libs-1.22.2-7.amzn2027  |
|  libcurl-minimal-8.21.0-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-2.amzn2027  |
|  openssl-libs-1:3.5.8-2.amzn2027  |
|  pcre2-syntax-10.48-1.amzn2027.0.1  |
|  pcre2-10.48-1.amzn2027.0.1  |
|  rpm-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-6.0.0-1.amzn2027.0.6  |
|  system-release-2027.0.20260928-0.amzn2027  |

### Minimal Container
<a name="amis-2027.0.20260928.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20260928-0.amzn2027  |
|  curl-8.21.0-5.amzn2027.0.1  |
|  krb5-libs-1.22.2-7.amzn2027  |
|  libcurl-minimal-8.21.0-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-2.amzn2027  |
|  openssl-libs-1:3.5.8-2.amzn2027  |
|  pcre2-syntax-10.48-1.amzn2027.0.1  |
|  pcre2-10.48-1.amzn2027.0.1  |
|  rpm-libs-6.0.0-1.amzn2027.0.6  |
|  rpm-6.0.0-1.amzn2027.0.6  |
|  system-release-2027.0.20260928-0.amzn2027  |

## Contact us
<a name="amis-2027.0.20260928.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
