---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261117.html
---

# Amazon Linux 2023 version 2023.12.20261117 release notes

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261117.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261117)
+ [Repository Updates](#repository-updates-2023.12.20261117)
  + [Core Updated Packages](#amis-2023.12.20261117.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261117)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261117.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261117.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261117.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261117.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261117.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261117.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261117.Default-Container)
  + [Minimal Container](#amis-2023.12.20261117.Minimal-Container)
+ [Contact us](#amis-2023.12.20261117.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261117"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  `rsync` has been updated to version `3.5.2`. Progress and human-readable size formats have changed, and control characters in displayed filenames and logs are now escaped. Password files with an empty first line are rejected, and hostname-based daemon access rules now match IPv6 addresses. Update affected scripts and review password files and daemon access rules before upgrading.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261117"></a>

### Core Updated Packages
<a name="amis-2023.12.20261117.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  composer-2.11.2-1.amzn2023.0.1  |
|  containerd-2.3.7-1.amzn2023.0.4  |
|  credentials-fetcher-2.0.3-1.amzn2023.0.9  |
|  docker-25.0.18-1.amzn2023.0.4  |
|  ecs-init-1.108.3-1.amzn2023  |
|  ghostscript-9.56.1-7.amzn2023.0.21  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  golang-1.26.11-1.amzn2023.0.1  |
|  golang-github-burntsushi-toml-1.5.0-1.amzn2023.0.10  |
|  golang-github-burntsushi-toml-test-0.2.0-8.amzn2023.0.12  |
|  golang-github-cpuguy83-md2man-2.0.2-24.amzn2023.0.16  |
|  golang-github-urfave-cli-1.22.10-2.amzn2023.0.9  |
|  golang-gopkg-yaml-2-2.4.0-2.amzn2023.0.10  |
|  golist-0.10.4-12.amzn2023.0.18  |
|  java-17-amazon-corretto-17.0.21.1.2-1.amzn2023.1  |
|  java-21-amazon-corretto-21.0.13.1.2-1.amzn2023.1  |
|  java-25-amazon-corretto-25.0.5.1.2-1.amzn2023.1  |
|  java-27-amazon-corretto-27.0.1.1.4-1.amzn2023.1  |
|  libtiff-4.4.0-4.amzn2023.0.29  |
|  nerdctl-2.3.5-1.amzn2023.0.4  |
|  netpbm-10.96.00-1.amzn2023.0.4  |
|  objenesis-3.6-1.amzn2023.0.1  |
|  pcs-0.12.1-1.amzn2023.0.3  |
|  rapidjson-1.1.0-16.amzn2023.0.4  |
|  rsync-3.5.2-1.amzn2023.0.1  |
|  runfinch-finch-1.19.0-1.amzn2023.0.5  |
|  soci-snapshotter-0.16.1-1.amzn2023.0.2  |
|  system-release-2023.12.20261117-0.amzn2023  |
|  tomcat9-9.0.123-1.amzn2023.0.1  |

## Image Updates
<a name="ami-updates-2023.12.20261117"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261117.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  rsync-3.5.2-1.amzn2023.0.1  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261117.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261117.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  rsync-3.5.2-1.amzn2023.0.1  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261117.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261117.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  rsync-3.5.2-1.amzn2023.0.1  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261117.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261117-0.amzn2023  |
|  gnutls-3.8.10-4.amzn2023.0.3  |
|  kernel-livepatch-repo-s3-2023.12.20261117-0.amzn2023  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Default Container
<a name="amis-2023.12.20261117.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261117-0.amzn2023  |
|  system-release-2023.12.20261117-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20261117.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261117-0.amzn2023  |
|  system-release-2023.12.20261117-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261117.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
