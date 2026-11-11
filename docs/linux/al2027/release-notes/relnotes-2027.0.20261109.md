---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20261109.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20261109 release notes
<a name="relnotes-2027.0.20261109"></a>

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20261109.

**Contents**
+ [Release summary](#release-summary-2027.0.20261109)
+ [Repository Updates](#repository-updates-2027.0.20261109)
  + [Core New Packages](#amis-2027.0.20261109.Core-New-Packages)
  + [Core Updated Packages](#amis-2027.0.20261109.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20261109)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20261109.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20261109.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20261109.Default-Container)
  + [Minimal Container](#amis-2027.0.20261109.Minimal-Container)
+ [Contact us](#amis-2027.0.20261109.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

## Release summary
<a name="release-summary-2027.0.20261109"></a>

This release is an update to the AL2027 preview.

**Notable updates**
+ `rclone` has been updated to version `1.75.2`. When authentication is configured, ordinary HTTP `OPTIONS` requests and remote-control `job/status` and `job/list` calls now require credentials. Browser CORS preflight requests remain supported when `allow-origin` is configured. Remote-control calls with out-of-range integer arguments are now rejected. Update any clients or scripts that rely on the previous behavior.
+ The `postgresql16`, `postgresql17`, and `postgresql18` packages are now built against AWS-LC instead of OpenSSL.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2027.0.20261109"></a>

### Core New Packages
<a name="amis-2027.0.20261109.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  catatonit-0.2.1-1.amzn2027  |
|  conmon-2.2.1-1.amzn2027  |
|  podman-6.1.4-1.amzn2027  |

### Core Updated Packages
<a name="amis-2027.0.20261109.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  ant-1.10.18-1.amzn2027.0.1  |
|  aws-lc-5.12.0-1.amzn2027  |
|  bcel-6.13.0-1.amzn2027.0.1  |
|  containerd-2.3.7-1.amzn2027.0.3  |
|  dotnet10.0-10.0.114-1.amzn2027.0.1  |
|  git-lfs-3.8.1-1.amzn2027  |
|  glib-networking-2.80.0-6.amzn2027.0.2  |
|  glibc-2.44-2.amzn2027.0.4  |
|  gnome-remote-desktop-50.2-2.amzn2027  |
|  grpc-1.60.2-10.amzn2027.0.3  |
|  gstreamer1-plugins-good-1.28.6-1.amzn2027.0.2  |
|  guava-33.7.2-1.amzn2027.0.1  |
|  haproxy-3.4.7-1.amzn2027.0.1  |
|  httpd-2.4.69-1.amzn2027.0.2  |
|  jackson-bom-2.21.8-1.amzn2027.0.1  |
|  jackson-core-2.21.8-1.amzn2027.0.1  |
|  jackson-databind-2.21.8-1.amzn2027.0.1  |
|  javapackages-bootstrap-1.27.0-4.amzn2027.0.3  |
|  kernel7.2-7.2.13-17.148.amzn2027  |
|  libXi-1.8.4-1.amzn2027.0.1  |
|  libcap-2.78-1.amzn2027.0.1  |
|  librsvg2-2.62.4-1.amzn2027  |
|  loupe-50.0-2.amzn2027  |
|  nautilus-50.2.2-2.amzn2027  |
|  nss-3.124.0-6.amzn2027  |
|  openssl-3.5.8-4.amzn2027  |
|  perl-DBI-1.656-1.amzn2027.0.1  |
|  perl-URI-5.37-1.amzn2027.0.1  |
|  perl-podlators-6.1.1-1.amzn2027.0.1  |
|  postgresql16-16.15-1.amzn2027.0.2  |
|  postgresql17-17.11-1.amzn2027.0.2  |
|  postgresql18-18.6-1.amzn2027.0.2  |
|  python-virtualenv-20.35.4-1.amzn2027.0.7  |
|  python3.14-3.14.10-1.amzn2027.0.1  |
|  rclone-1.75.2-1.amzn2027  |
|  rpm-6.0.0-1.amzn2027.0.8  |
|  runfinch-finch-1.19.0-1.amzn2027.0.4  |
|  rust-1.99.1-1.amzn2027  |
|  rust-cargo-c-0.10.25-2.amzn2027  |
|  rust-clock-bound-3.0.0\~rc.0-1.amzn2027  |
|  selinux-policy-45.23-2.amzn2027  |
|  sssd-2.13.1-1.amzn2027.0.5  |
|  system-release-2027.0.20261109-0.amzn2027  |
|  systemd-262.1-1.amzn2027  |
|  util-linux-2.42.4-13.amzn2027  |

## Image Updates
<a name="ami-updates-2027.0.20261109"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20261109.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261109-0.amzn2027  |
|  aws-lc-libs-5.12.0-1.amzn2027  |
|  glibc-common-2.44-2.amzn2027.0.4  |
|  glibc-minimal-langpack-2.44-2.amzn2027.0.4  |
|  glibc-2.44-2.amzn2027.0.4  |
|  kernel7.2-tools-1:7.2.13-17.148.amzn2027  |
|  kernel7.2-1:7.2.13-17.148.amzn2027  |
|  libblkid-2.42.4-13.amzn2027  |
|  libcap-2.78-1.amzn2027.0.1  |
|  libfdisk-2.42.4-13.amzn2027  |
|  liblastlog2-2.42.4-13.amzn2027  |
|  libmount-2.42.4-13.amzn2027  |
|  libsmartcols-2.42.4-13.amzn2027  |
|  libsss\_certmap-2.13.1-1.amzn2027.0.5  |
|  libsss\_idmap-2.13.1-1.amzn2027.0.5  |
|  libsss\_nss\_idmap-2.13.1-1.amzn2027.0.5  |
|  libsss\_sudo-2.13.1-1.amzn2027.0.5  |
|  libuuid-2.42.4-13.amzn2027  |
|  openssl-fips-provider-latest-1:3.5.8-4.amzn2027  |
|  openssl-libs-1:3.5.8-4.amzn2027  |
|  openssl-1:3.5.8-4.amzn2027  |
|  python3-libs-3.14.10-1.amzn2027.0.1  |
|  python3-3.14.10-1.amzn2027.0.1  |
|  rpm-build-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-plugin-selinux-6.0.0-1.amzn2027.0.8  |
|  rpm-plugin-systemd-inhibit-6.0.0-1.amzn2027.0.8  |
|  rpm-sign-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-6.0.0-1.amzn2027.0.8  |
|  selinux-policy-targeted-45.23-2.amzn2027  |
|  selinux-policy-45.23-2.amzn2027  |
|  sssd-client-2.13.1-1.amzn2027.0.5  |
|  sssd-common-2.13.1-1.amzn2027.0.5  |
|  sssd-kcm-2.13.1-1.amzn2027.0.5  |
|  sssd-krb5-common-2.13.1-1.amzn2027.0.5  |
|  system-release-2027.0.20261109-0.amzn2027  |
|  systemd-libs-262.1-1.amzn2027  |
|  systemd-networkd-262.1-1.amzn2027  |
|  systemd-pam-262.1-1.amzn2027  |
|  systemd-resolved-262.1-1.amzn2027  |
|  systemd-shared-262.1-1.amzn2027  |
|  systemd-sysusers-262.1-1.amzn2027  |
|  systemd-udev-262.1-1.amzn2027  |
|  systemd-262.1-1.amzn2027  |
|  util-linux-core-2.42.4-13.amzn2027  |
|  util-linux-2.42.4-13.amzn2027  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20261109.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261109-0.amzn2027  |
|  aws-lc-libs-5.12.0-1.amzn2027  |
|  glibc-common-2.44-2.amzn2027.0.4  |
|  glibc-minimal-langpack-2.44-2.amzn2027.0.4  |
|  glibc-2.44-2.amzn2027.0.4  |
|  kernel7.2-1:7.2.13-17.148.amzn2027  |
|  libblkid-2.42.4-13.amzn2027  |
|  libcap-2.78-1.amzn2027.0.1  |
|  libfdisk-2.42.4-13.amzn2027  |
|  liblastlog2-2.42.4-13.amzn2027  |
|  libmount-2.42.4-13.amzn2027  |
|  libsmartcols-2.42.4-13.amzn2027  |
|  libusb1-1.0.30-1.amzn2027  |
|  libuuid-2.42.4-13.amzn2027  |
|  openssl-fips-provider-latest-1:3.5.8-4.amzn2027  |
|  openssl-libs-1:3.5.8-4.amzn2027  |
|  openssl-1:3.5.8-4.amzn2027  |
|  python3-libs-3.14.10-1.amzn2027.0.1  |
|  python3-3.14.10-1.amzn2027.0.1  |
|  rpm-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-plugin-selinux-6.0.0-1.amzn2027.0.8  |
|  rpm-plugin-systemd-inhibit-6.0.0-1.amzn2027.0.8  |
|  rpm-6.0.0-1.amzn2027.0.8  |
|  selinux-policy-targeted-45.23-2.amzn2027  |
|  selinux-policy-45.23-2.amzn2027  |
|  system-release-2027.0.20261109-0.amzn2027  |
|  systemd-libs-262.1-1.amzn2027  |
|  systemd-networkd-262.1-1.amzn2027  |
|  systemd-resolved-262.1-1.amzn2027  |
|  systemd-shared-262.1-1.amzn2027  |
|  systemd-sysusers-262.1-1.amzn2027  |
|  systemd-udev-262.1-1.amzn2027  |
|  systemd-262.1-1.amzn2027  |
|  tpm2-tss-4.1.3-10.amzn2027  |
|  util-linux-core-2.42.4-13.amzn2027  |
|  util-linux-2.42.4-13.amzn2027  |

### Default Container
<a name="amis-2027.0.20261109.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261109-0.amzn2027  |
|  glibc-common-2.44-2.amzn2027.0.4  |
|  glibc-minimal-langpack-2.44-2.amzn2027.0.4  |
|  glibc-2.44-2.amzn2027.0.4  |
|  libblkid-2.42.4-13.amzn2027  |
|  libcap-2.78-1.amzn2027.0.1  |
|  libmount-2.42.4-13.amzn2027  |
|  libsmartcols-2.42.4-13.amzn2027  |
|  libuuid-2.42.4-13.amzn2027  |
|  openssl-fips-provider-latest-1:3.5.8-4.amzn2027  |
|  openssl-libs-1:3.5.8-4.amzn2027  |
|  rpm-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-6.0.0-1.amzn2027.0.8  |
|  system-release-2027.0.20261109-0.amzn2027  |
|  systemd-libs-262.1-1.amzn2027  |
|  systemd-standalone-sysusers-262.1-1.amzn2027  |

### Minimal Container
<a name="amis-2027.0.20261109.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261109-0.amzn2027  |
|  glibc-common-2.44-2.amzn2027.0.4  |
|  glibc-minimal-langpack-2.44-2.amzn2027.0.4  |
|  glibc-2.44-2.amzn2027.0.4  |
|  libblkid-2.42.4-13.amzn2027  |
|  libcap-2.78-1.amzn2027.0.1  |
|  libmount-2.42.4-13.amzn2027  |
|  libsmartcols-2.42.4-13.amzn2027  |
|  libuuid-2.42.4-13.amzn2027  |
|  openssl-fips-provider-latest-1:3.5.8-4.amzn2027  |
|  openssl-libs-1:3.5.8-4.amzn2027  |
|  rpm-libs-6.0.0-1.amzn2027.0.8  |
|  rpm-6.0.0-1.amzn2027.0.8  |
|  system-release-2027.0.20261109-0.amzn2027  |
|  systemd-libs-262.1-1.amzn2027  |
|  systemd-standalone-sysusers-262.1-1.amzn2027  |

## Contact us
<a name="amis-2027.0.20261109.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
