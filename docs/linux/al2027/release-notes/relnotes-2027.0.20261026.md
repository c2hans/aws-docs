---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20261026.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20261026 release notes
<a name="relnotes-2027.0.20261026"></a>

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20261026.

**Contents**
+ [Release summary](#release-summary-2027.0.20261026)
+ [Repository Updates](#repository-updates-2027.0.20261026)
  + [Core New Packages](#amis-2027.0.20261026.Core-New-Packages)
  + [Core Updated Packages](#amis-2027.0.20261026.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20261026)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20261026.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20261026.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20261026.Default-Container)
  + [Minimal Container](#amis-2027.0.20261026.Minimal-Container)
+ [Contact us](#amis-2027.0.20261026.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

## Release summary
<a name="release-summary-2027.0.20261026"></a>

This release is an update to the AL2027 preview.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2027.0.20261026"></a>

### Core New Packages
<a name="amis-2027.0.20261026.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  java-27-amazon-corretto-27.0.1.0.10-1.amzn2027.1  |
|  rust-clock-bound-3.0.0\~beta.1-1.amzn2027  |

### Core Updated Packages
<a name="amis-2027.0.20261026.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  aardvark-dns-2.1.0-1.amzn2027.0.1  |
|  amazon-ecr-credential-helper-0.12.0-5.amzn2027  |
|  apache-ivy-2.6.0-9.amzn2027.0.1  |
|  aspell-0.60.8.1-7.amzn2027.0.3  |
|  aws-lc-5.11.0-2.amzn2027  |
|  awscli-2-2.36.47-1.amzn2027.0.2  |
|  bind-9.18.50-1.amzn2027.0.7  |
|  brotli-1.2.1-1.amzn2027  |
|  buildah-1.45.1-1.amzn2027.0.2  |
|  ca-certificates-2026.2.90\_v9.0.316-100.0.amzn2027  |
|  cifs-utils-7.7-2.amzn2027.0.1  |
|  containerd-2.3.7-1.amzn2027.0.1  |
|  containers-common-0.69.2-1.amzn2027.0.1  |
|  credentials-fetcher-2.0.3-1.amzn2027.0.7  |
|  crypto-policies-20260811-1.git4dcd294.amzn2027  |
|  cups-2.4.20-1.amzn2027.0.1  |
|  curl-8.22.0-1.amzn2027.0.2  |
|  cyrus-sasl-2.1.28-35.amzn2027.0.2  |
|  docker-29.9.1-1.amzn2027.0.2  |
|  firefox-153.5.1-1.amzn2027.0.1  |
|  freerdp-3.32.2-1.amzn2027  |
|  gd-2.3.3-19.amzn2027.0.1  |
|  git-lfs-3.7.1-2.amzn2027  |
|  golang-1.26.10-1.amzn2027.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2027.0.8  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2027.0.10  |
|  golang-github-cpuguy83-md2man-2.0.7-38.amzn2027.0.5  |
|  golang-github-urfave-cli-1.22.10-2.amzn2027.0.7  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2027.0.9  |
|  golist-0.10.4-12.amzn2027.0.16  |
|  haproxy-3.0.30-1.amzn2027.0.1  |
|  iperf3-3.22-1.amzn2027.0.1  |
|  iproute-7.2.0-1.amzn2027  |
|  java-1.8.0-amazon-corretto-1.8.0\_512.b08-1.amzn2027  |
|  java-11-amazon-corretto-11.0.33.0.9-1.amzn2027  |
|  java-17-amazon-corretto-17.0.21.0.10-1.amzn2027.1  |
|  java-21-amazon-corretto-21.0.13.0.10-1.amzn2027.1  |
|  java-25-amazon-corretto-25.0.5.0.9-1.amzn2027.1  |
|  javapackages-tools-6.5.1-1.amzn2027.0.1  |
|  jline-3.30.15-1.amzn2027.0.1  |
|  jpegxl-0.11.2-3.amzn2027  |
|  kernel7.2-7.2.8-14.137.amzn2027  |
|  libXtst-1.2.5-3.amzn2027.0.1  |
|  libheif-1.23.6-1.amzn2027  |
|  libreswan-5.3.3-1.amzn2027  |
|  libsoup3-3.7.3-2.amzn2027  |
|  mariadb1011-10.11.19-1.amzn2027.0.2  |
|  mariadb114-11.4.13-1.amzn2027.0.2  |
|  mariadb118-11.8.9-1.amzn2027.0.2  |
|  mariadb123-12.3.3-2.amzn2027.0.2  |
|  mod\_security-2.9.15-1.amzn2027  |
|  nerdctl-2.3.5-2.amzn2027.0.3  |
|  netavark-2.1.0-1.amzn2027.0.1  |
|  nginx-1.30.6-1.amzn2027.0.1  |
|  nginx-awslc-1.30.6-1.amzn2027.0.1  |
|  nginx-mod-headers-more-0.39-1.amzn2027.0.11  |
|  nginx-mod-njs-1.0.2-1.amzn2027.0.1  |
|  nodejs24-24.22.1-1.amzn2027.0.1  |
|  oci-add-hooks-0-0.1.20200504git268e3bb.amzn2027.0.11  |
|  openvpn-2.7.6-2.amzn2027  |
|  pcre2-10.49-1.amzn2027.0.1  |
|  perl-5.42.2-523.amzn2027.0.7  |
|  python-awscrt-0.36.4-1.amzn2027.0.2  |
|  python-jwt-2.15.1-1.amzn2027.0.1  |
|  python-virtualenv-20.35.4-1.amzn2027.0.6  |
|  python3.14-3.14.8-1.amzn2027.0.1  |
|  runc-1.5.2-1.amzn2027.0.1  |
|  runfinch-finch-1.19.0-1.amzn2027.0.2  |
|  rust-1.99.0-1.amzn2027  |
|  skopeo-1.24.1-1.amzn2027.0.2  |
|  soci-snapshotter-0.16.0-1.amzn2027.0.2  |
|  system-release-2027.0.20261026-0.amzn2027  |
|  systemtap-5.6-1.amzn2027.0.2  |
|  tzdata-2026e-1.amzn2027.0.1  |
|  unbound-1.26.1-1.amzn2027  |
|  valkey-9.0.6-1.amzn2027.0.2  |
|  wireshark-4.6.9-1.amzn2027  |
|  xorg-x11-server-Xwayland-24.1.13-1.amzn2027.0.1  |

## Image Updates
<a name="ami-updates-2027.0.20261026"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20261026.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261026-0.amzn2027  |
|  aws-lc-libs-5.11.0-2.amzn2027  |
|  awscli-2-2.36.47-1.amzn2027.0.2  |
|  ca-certificates-2026.2.90\_v9.0.316-100.0.amzn2027  |
|  crypto-policies-20260811-1.git4dcd294.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.2  |
|  cyrus-sasl-gssapi-2.1.28-35.amzn2027.0.2  |
|  cyrus-sasl-lib-2.1.28-35.amzn2027.0.2  |
|  iproute-7.2.0-1.amzn2027  |
|  kernel7.2-tools-1:7.2.8-14.137.amzn2027  |
|  kernel7.2-1:7.2.8-14.137.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.2  |
|  pcre2-syntax-10.49-1.amzn2027.0.1  |
|  pcre2-10.49-1.amzn2027.0.1  |
|  python3-awscrt-0.36.4-1.amzn2027.0.2  |
|  python3-libs-3.14.8-1.amzn2027.0.1  |
|  python3-3.14.8-1.amzn2027.0.1  |
|  system-release-2027.0.20261026-0.amzn2027  |
|  tzdata-2026e-1.amzn2027.0.1  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20261026.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261026-0.amzn2027  |
|  aws-lc-libs-5.11.0-2.amzn2027  |
|  awscli-2-2.36.47-1.amzn2027.0.2  |
|  ca-certificates-2026.2.90\_v9.0.316-100.0.amzn2027  |
|  crypto-policies-20260811-1.git4dcd294.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.2  |
|  cyrus-sasl-lib-2.1.28-35.amzn2027.0.2  |
|  iproute-7.2.0-1.amzn2027  |
|  kernel7.2-1:7.2.8-14.137.amzn2027  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.2  |
|  pcre2-syntax-10.49-1.amzn2027.0.1  |
|  pcre2-10.49-1.amzn2027.0.1  |
|  python3-awscrt-0.36.4-1.amzn2027.0.2  |
|  python3-libs-3.14.8-1.amzn2027.0.1  |
|  python3-3.14.8-1.amzn2027.0.1  |
|  system-release-2027.0.20261026-0.amzn2027  |
|  tzdata-2026e-1.amzn2027.0.1  |

### Default Container
<a name="amis-2027.0.20261026.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261026-0.amzn2027  |
|  ca-certificates-2026.2.90\_v9.0.316-100.0.amzn2027  |
|  crypto-policies-20260811-1.git4dcd294.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.2  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.2  |
|  pcre2-syntax-10.49-1.amzn2027.0.1  |
|  pcre2-10.49-1.amzn2027.0.1  |
|  system-release-2027.0.20261026-0.amzn2027  |
|  tzdata-2026e-1.amzn2027.0.1  |

### Minimal Container
<a name="amis-2027.0.20261026.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261026-0.amzn2027  |
|  ca-certificates-2026.2.90\_v9.0.316-100.0.amzn2027  |
|  crypto-policies-20260811-1.git4dcd294.amzn2027  |
|  curl-8.22.0-1.amzn2027.0.2  |
|  libcurl-minimal-8.22.0-1.amzn2027.0.2  |
|  pcre2-syntax-10.49-1.amzn2027.0.1  |
|  pcre2-10.49-1.amzn2027.0.1  |
|  system-release-2027.0.20261026-0.amzn2027  |
|  tzdata-2026e-1.amzn2027.0.1  |

## Contact us
<a name="amis-2027.0.20261026.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
