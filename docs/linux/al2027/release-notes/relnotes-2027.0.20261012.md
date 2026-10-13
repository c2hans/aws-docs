---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20261012.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20261012 release notes
<a name="relnotes-2027.0.20261012"></a>

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20261012.

**Contents**
+ [Release summary](#release-summary-2027.0.20261012)
+ [Repository Updates](#repository-updates-2027.0.20261012)
  + [Core New Packages](#amis-2027.0.20261012.Core-New-Packages)
  + [Core Removed Packages](#amis-2027.0.20261012.Core-Removed-Packages)
  + [Core Updated Packages](#amis-2027.0.20261012.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20261012)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20261012.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20261012.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20261012.Default-Container)
  + [Minimal Container](#amis-2027.0.20261012.Minimal-Container)
+ [Contact us](#amis-2027.0.20261012.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

**AL2027 Preview AMI SSM Parameters**
 During the AL2027 preview, only SSM parameters that use the `kernel-default` alias (for example, `al2027-preview-ami-kernel-default-x86_64`) are supported. SSM parameters that reference a specific kernel version, such as `kernel-7.1` and `kernel-7.2`, will be deleted on October 31, 2026. Use `kernel-default` to always resolve the latest preview AMI with the current default kernel; version-specific kernel SSM parameters will become available when AL2027 reaches general availability (GA).

## Release summary
<a name="release-summary-2027.0.20261012"></a>

This release is an update to the AL2027 preview.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2027.0.20261012"></a>

### Core New Packages
<a name="amis-2027.0.20261012.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  edk2-20260508-9.amzn2027  |
|  libvirt-12.0.0-3.amzn2027.0.4  |
|  libvirt-python-12.0.0-1.amzn2027.0.3  |
|  passt-0^20260716.g090d739-2.amzn2027.0.1  |
|  python-qemu-qmp-0.0.5-2.amzn2027.0.1  |
|  seabios-1.17.0-9.amzn2027  |

### Core Removed Packages
<a name="amis-2027.0.20261012.Core-Removed-Packages"></a>

This section provides details about Core Removed Packages.

| Package |
| --- |
|  spal-release-2023-4.amzn2027  |

### Core Updated Packages
<a name="amis-2027.0.20261012.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  PackageKit-1.4.0-1.amzn2027  |
|  cjose-0.6.2.2-11.amzn2027  |
|  corosync-3.1.10-8.amzn2027.0.1  |
|  cups-2.4.19-1.amzn2027.0.5  |
|  curl-8.22.0-1.amzn2027.0.1  |
|  device-mapper-persistent-data-1.3.3-1.amzn2027.0.2  |
|  dovecot-2.4.5-1.amzn2027.0.1  |
|  emacs-30.2-3.amzn2027  |
|  fetchmail-6.6.8-1.amzn2027  |
|  firefox-153.4.0-1.amzn2027.0.1  |
|  flatpak-builder-1.4.4-1.amzn2027.0.2  |
|  freerdp-3.32.1-1.amzn2027.0.1  |
|  gdb-17.1-5.amzn2027.0.3  |
|  httpd-2.4.69-1.amzn2027.0.1  |
|  jackson-bom-2.21.7-1.amzn2027.0.1  |
|  jackson-core-2.21.7-1.amzn2027.0.1  |
|  jackson-databind-2.21.7-1.amzn2027.0.1  |
|  java-1.8.0-amazon-corretto-1.8.0\_504.b04-1.amzn2027  |
|  java-11-amazon-corretto-11.0.32\+12-1.amzn2027  |
|  java-17-amazon-corretto-17.0.20\+12-1.amzn2027.1  |
|  java-21-amazon-corretto-21.0.12\+12-1.amzn2027.1  |
|  java-25-amazon-corretto-25.0.4\+10-1.amzn2027.1  |
|  kernel7.2-7.2.8-7.108.amzn2027  |
|  libX11-1.8.13-1.amzn2027.0.1  |
|  libXfont2-2.0.8-1.amzn2027.0.1  |
|  libXrender-0.9.12-3.amzn2027.0.1  |
|  libxml2-2.12.10-5.amzn2027.0.1  |
|  mariadb1011-10.11.19-1.amzn2027.0.1  |
|  mariadb114-11.4.13-1.amzn2027.0.1  |
|  mariadb118-11.8.9-1.amzn2027.0.1  |
|  mariadb123-12.3.3-2.amzn2027.0.1  |
|  mdevctl-1.4.0-2.amzn2027.0.1  |
|  mount-s3-1.24.0-1.amzn2027  |
|  network-flow-monitor-agent-1.1.8-1.amzn2027.0.5  |
|  opendkim-2.11.0-0.43.amzn2027.0.2  |
|  openssl-3.5.8-3.amzn2027  |
|  parted-3.6-13.amzn2027.0.1  |
|  perl-5.42.2-523.amzn2027.0.6  |
|  perl-DBI-1.653-1.amzn2027.0.1  |
|  perl-HTTP-Date-6.08-2.amzn2027.0.1  |
|  perl-HTTP-Tiny-0.096-528.amzn2027.0.1  |
|  perl-Mojolicious-9.48-2.amzn2027.0.1  |
|  perl-Net-IDN-Encode-2.590-1.amzn2027.0.1  |
|  php8.5-8.5.11-1.amzn2027.0.1  |
|  python-jwcrypto-1.6.1-1.amzn2027.0.1  |
|  python-pip-26.2.1-2.amzn2027.0.1  |
|  python-pymongo-4.18.2-1.amzn2027.0.1  |
|  python-tornado-6.5.10-1.amzn2027.0.1  |
|  python-urllib3-2.6.3-1.amzn2027.0.3  |
|  qemu-11.0.4-1.amzn2027  |
|  rpcbind-1.3.1-1.amzn2027  |
|  rsyslog-8.2608.0-1.amzn2027  |
|  runfinch-finch-1.19.0-1.amzn2027.0.1  |
|  rust-1.98.1-1.amzn2027  |
|  rust-askalono-cli-0.5.0-1.amzn2027.0.3  |
|  rust-cargo-c-0.10.25-1.amzn2027  |
|  sudo-1.9.17-1.p2.amzn2027.0.4  |
|  system-release-2027.0.20261012-0.amzn2027  |
|  tomcat-native-2.0.16-1.amzn2027.0.1  |
|  tomcat10-10.1.60-1.amzn2027.0.1  |
|  tomcat9-9.0.122-1.amzn2027.0.1  |
|  util-linux-2.42.4-1.amzn2027  |
|  xdg-dbus-proxy-0.1.9-1.amzn2027.0.1  |

## Image Updates
<a name="ami-updates-2027.0.20261012"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20261012.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261012-0.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.1  |
|  kernel7.2-tools-1:7.2.8-7.108.amzn2027  |
|  kernel7.2-1:7.2.8-7.108.amzn2027  |
|  libblkid-2.42.4-1.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.1  |
|  libfdisk-2.42.4-1.amzn2027  |
|  liblastlog2-2.42.4-1.amzn2027  |
|  libmount-2.42.4-1.amzn2027  |
|  libsmartcols-2.42.4-1.amzn2027  |
|  libuuid-2.42.4-1.amzn2027  |
|  libxml2-2.12.10-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-3.amzn2027  |
|  openssl-libs-1:3.5.8-3.amzn2027  |
|  openssl-1:3.5.8-3.amzn2027  |
|  python3-pip-wheel-26.2.1-2.amzn2027.0.1  |
|  python3-urllib3-2.6.3-1.amzn2027.0.3  |
|  sudo-1.9.17-1.p2.amzn2027.0.4  |
|  system-release-2027.0.20261012-0.amzn2027  |
|  util-linux-core-2.42.4-1.amzn2027  |
|  util-linux-2.42.4-1.amzn2027  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20261012.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261012-0.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.1  |
|  kernel7.2-1:7.2.8-7.108.amzn2027  |
|  libblkid-2.42.4-1.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.1  |
|  libfdisk-2.42.4-1.amzn2027  |
|  liblastlog2-2.42.4-1.amzn2027  |
|  libmount-2.42.4-1.amzn2027  |
|  libsmartcols-2.42.4-1.amzn2027  |
|  libuuid-2.42.4-1.amzn2027  |
|  libxml2-2.12.10-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-3.amzn2027  |
|  openssl-libs-1:3.5.8-3.amzn2027  |
|  openssl-1:3.5.8-3.amzn2027  |
|  python3-pip-wheel-26.2.1-2.amzn2027.0.1  |
|  python3-urllib3-2.6.3-1.amzn2027.0.3  |
|  sudo-1.9.17-1.p2.amzn2027.0.4  |
|  system-release-2027.0.20261012-0.amzn2027  |
|  util-linux-core-2.42.4-1.amzn2027  |
|  util-linux-2.42.4-1.amzn2027  |

### Default Container
<a name="amis-2027.0.20261012.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261012-0.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.1  |
|  libblkid-2.42.4-1.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.1  |
|  libmount-2.42.4-1.amzn2027  |
|  libsmartcols-2.42.4-1.amzn2027  |
|  libuuid-2.42.4-1.amzn2027  |
|  libxml2-2.12.10-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-3.amzn2027  |
|  openssl-libs-1:3.5.8-3.amzn2027  |
|  system-release-2027.0.20261012-0.amzn2027  |

### Minimal Container
<a name="amis-2027.0.20261012.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261012-0.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.1  |
|  libblkid-2.42.4-1.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.1  |
|  libmount-2.42.4-1.amzn2027  |
|  libsmartcols-2.42.4-1.amzn2027  |
|  libuuid-2.42.4-1.amzn2027  |
|  libxml2-2.12.10-5.amzn2027.0.1  |
|  openssl-fips-provider-latest-1:3.5.8-3.amzn2027  |
|  openssl-libs-1:3.5.8-3.amzn2027  |
|  system-release-2027.0.20261012-0.amzn2027  |

## Contact us
<a name="amis-2027.0.20261012.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
