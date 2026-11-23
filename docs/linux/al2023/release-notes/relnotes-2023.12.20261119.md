---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261119.html
---

# Amazon Linux 2023 version 2023.12.20261119 release notes

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.12.20261119.

**Contents**
+ [Release Summary](#release-summary-2023.12.20261119)
+ [Repository Updates](#repository-updates-2023.12.20261119)
  + [Core New Packages](#amis-2023.12.20261119.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.12.20261119.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2023.12.20261119)
  + [Default Kernel 6.18 AMI](#amis-2023.12.20261119.Default-Kernel-6-18-AMI)
  + [Minimal Kernel 6.18 AMI](#amis-2023.12.20261119.Minimal-Kernel-6-18-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.12.20261119.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.12.20261119.Minimal-Kernel-6-12-AMI)
  + [Default Kernel 6.1 AMI](#amis-2023.12.20261119.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.12.20261119.Minimal-Kernel-6-1-AMI)
  + [Default Container](#amis-2023.12.20261119.Default-Container)
  + [Minimal Container](#amis-2023.12.20261119.Minimal-Container)
+ [Contact us](#amis-2023.12.20261119.contact-us)

## Release Summary
<a name="release-summary-2023.12.20261119"></a>

This release represents an update to the 12th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+  The PostgreSQL packages have been updated to the latest upstream release. After updating, you may need to rebuild C-language extensions against the updated PostgreSQL packages. Extensions in `postgresql-contrib` subpackages have already been built against the latest release. For full list of post-update steps, see the [PostgreSQL release notes](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/).

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.12.20261119"></a>

### Core New Packages
<a name="amis-2023.12.20261119.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  rust-ripgrep-15.2.0-2.amzn2023  |

### Core Updated Packages
<a name="amis-2023.12.20261119.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  ImageMagick-6.9.13.60-1.amzn2023  |
|  aardvark-dns-1.17.1-1.amzn2023.0.2  |
|  amazon-ecr-credential-helper-0.13.0-2.amzn2023  |
|  amazon-efs-utils-4.0.0-1.amzn2023  |
|  aws-nitro-enclaves-cli-1.5.3-0.amzn2023  |
|  elfutils-0.188-3.amzn2023.0.4  |
|  gcc14-14.2.1-7.amzn2023.0.3  |
|  gstreamer1-1.24.10-1.amzn2023.0.2  |
|  gstreamer1-plugins-bad-free-1.24.10-1.amzn2023.0.12  |
|  gstreamer1-plugins-base-1.24.10-1.amzn2023.0.8  |
|  java-1.8.0-amazon-corretto-1.8.0\_514.b01-1.amzn2023  |
|  java-11-amazon-corretto-11.0.33.1.1-1.amzn2023  |
|  libXfont2-2.0.7-1.amzn2023.0.4  |
|  libfontenc-1.1.7-3.amzn2023.0.2  |
|  php8.2-8.2.36-1.amzn2023.0.1  |
|  php8.3-8.3.37-1.amzn2023.0.1  |
|  php8.4-8.4.28-1.amzn2023.0.1  |
|  php8.5-8.5.13-1.amzn2023.0.1  |
|  postgresql15-15.20-1.amzn2023.0.1  |
|  postgresql16-16.16-1.amzn2023.0.1  |
|  postgresql17-17.12-1.amzn2023.0.1  |
|  postgresql18-18.7-1.amzn2023.0.1  |
|  python-dulwich-0.20.18-1.amzn2023.0.4  |
|  python-oauthlib-3.0.2-9.amzn2023.0.4  |
|  python-tornado-6.1.0-2.amzn2023.0.13  |
|  rclone-1.75.2-2.amzn2023  |
|  swiftlang-6.3-1.amzn2023.0.3  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  tomcat11-11.0.29-1.amzn2023.0.1  |
|  update-motd-2.3-1.amzn2023.0.2  |

## Image Updates
<a name="ami-updates-2023.12.20261119"></a>

### Default Kernel 6.18 AMI
<a name="amis-2023.12.20261119.Default-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-debuginfod-client-0.188-3.amzn2023.0.4  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Minimal Kernel 6.18 AMI
<a name="amis-2023.12.20261119.Minimal-Kernel-6-18-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.18 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Default Kernel 6.12 AMI
<a name="amis-2023.12.20261119.Default-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-debuginfod-client-0.188-3.amzn2023.0.4  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.12.20261119.Minimal-Kernel-6-12-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.12 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Default Kernel 6.1 AMI
<a name="amis-2023.12.20261119.Default-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Default Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-debuginfod-client-0.188-3.amzn2023.0.4  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.12.20261119.Minimal-Kernel-6-1-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 6.1 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2023.12.20261119-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  kernel-livepatch-repo-s3-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  python3-oauthlib-3.0.2-9.amzn2023.0.4  |
|  system-release-2023.12.20261119-0.amzn2023  |
|  update-motd-2.3-1.amzn2023.0.2  |

### Default Container
<a name="amis-2023.12.20261119.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261119-0.amzn2023  |
|  elfutils-default-yama-scope-0.188-3.amzn2023.0.4  |
|  elfutils-libelf-0.188-3.amzn2023.0.4  |
|  elfutils-libs-0.188-3.amzn2023.0.4  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libgomp-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  system-release-2023.12.20261119-0.amzn2023  |

### Minimal Container
<a name="amis-2023.12.20261119.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2023.12.20261119-0.amzn2023  |
|  libgcc-14.2.1-7.amzn2023.0.3  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.3  |
|  system-release-2023.12.20261119-0.amzn2023  |

## Contact us
<a name="amis-2023.12.20261119.contact-us"></a>

If you find a security issue, see [the Amazon Linux security policy on GitHub](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
