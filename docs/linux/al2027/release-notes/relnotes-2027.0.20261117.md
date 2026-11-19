---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20261117.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20261117 release notes

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20261117.

**Contents**
+ [Release summary](#release-summary-2027.0.20261117)
+ [Repository Updates](#repository-updates-2027.0.20261117)
  + [Core Updated Packages](#amis-2027.0.20261117.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20261117)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20261117.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20261117.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20261117.Default-Container)
  + [Minimal Container](#amis-2027.0.20261117.Minimal-Container)
+ [Contact us](#amis-2027.0.20261117.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

## Release summary
<a name="release-summary-2027.0.20261117"></a>

This release is an update to the AL2027 preview.

**Notable updates**
+ `rsync` has been updated to version `3.5.2`. Progress and human-readable size formats have changed, and control characters in displayed filenames and logs are now escaped. Password files with an empty first line are rejected, and hostname-based daemon access rules now match IPv6 addresses. Update affected scripts and review password files and daemon access rules before upgrading.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2027.0.20261117"></a>

### Core Updated Packages
<a name="amis-2027.0.20261117.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  ImageMagick-7.1.2.35-2.amzn2027  |
|  composer-2.11.2-1.amzn2027  |
|  containerd-2.3.7-1.amzn2027.0.4  |
|  credentials-fetcher-2.0.3-1.amzn2027.0.8  |
|  docker-29.10.0-1.amzn2027.0.1  |
|  git-lfs-3.8.1-2.amzn2027  |
|  gnutls-3.8.10-48.amzn2027  |
|  golang-1.26.11-1.amzn2027.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2027.0.9  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2027.0.11  |
|  golang-github-cpuguy83-md2man-2.0.7-38.amzn2027.0.6  |
|  golang-github-urfave-cli-1.22.10-2.amzn2027.0.8  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2027.0.10  |
|  golist-0.10.4-12.amzn2027.0.17  |
|  java-17-amazon-corretto-17.0.21.1.2-1.amzn2027.1  |
|  java-21-amazon-corretto-21.0.13.1.2-1.amzn2027.1  |
|  java-25-amazon-corretto-25.0.5.1.2-1.amzn2027.1  |
|  java-27-amazon-corretto-27.0.1.1.4-1.amzn2027.1  |
|  mount-s3-1.25.0-1.amzn2027  |
|  nerdctl-2.3.5-2.amzn2027.0.5  |
|  netpbm-11.13.00-2.amzn2027.0.4  |
|  objenesis-3.6-1.amzn2027.0.1  |
|  openssh-9.9p1-34.amzn2027  |
|  python-mistune-3.4.0-1.amzn2027.0.1  |
|  python-tornado-6.6.1-1.amzn2027.0.1  |
|  rapidjson-1.1.0^20241222git24b5e7a-1.amzn2027.0.4  |
|  rsync-3.5.2-1.amzn2027.0.1  |
|  runfinch-finch-1.19.0-1.amzn2027.0.5  |
|  soci-snapshotter-0.16.1-1.amzn2027.0.2  |
|  spal-release-2027-2.amzn2027  |
|  sqlite-3.54.1-1.amzn2027.0.1  |
|  system-release-2027.0.20261117-0.amzn2027  |

## Image Updates
<a name="ami-updates-2027.0.20261117"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20261117.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261117-0.amzn2027  |
|  clock-bound-3.0.0\~rc.0-1.amzn2027  |
|  gnutls-3.8.10-48.amzn2027  |
|  openssh-clients-9.9p1-34.amzn2027  |
|  openssh-server-9.9p1-34.amzn2027  |
|  openssh-9.9p1-34.amzn2027  |
|  sqlite-libs-3.54.1-1.amzn2027.0.1  |
|  system-release-2027.0.20261117-0.amzn2027  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20261117.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261117-0.amzn2027  |
|  clock-bound-3.0.0\~rc.0-1.amzn2027  |
|  openssh-clients-9.9p1-34.amzn2027  |
|  openssh-server-9.9p1-34.amzn2027  |
|  openssh-9.9p1-34.amzn2027  |
|  sqlite-libs-3.54.1-1.amzn2027.0.1  |
|  system-release-2027.0.20261117-0.amzn2027  |

### Default Container
<a name="amis-2027.0.20261117.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261117-0.amzn2027  |
|  sqlite-libs-3.54.1-1.amzn2027.0.1  |
|  system-release-2027.0.20261117-0.amzn2027  |

### Minimal Container
<a name="amis-2027.0.20261117.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261117-0.amzn2027  |
|  sqlite-libs-3.54.1-1.amzn2027.0.1  |
|  system-release-2027.0.20261117-0.amzn2027  |

## Contact us
<a name="amis-2027.0.20261117.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
