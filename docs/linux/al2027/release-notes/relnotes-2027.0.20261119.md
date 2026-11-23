---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20261119.html
---

# Amazon Linux 2027 (AL2027) preview version 2027.0.20261119 release notes

These are the release notes for Amazon Linux 2027 (AL2027) preview version 2027.0.20261119.

**Contents**
+ [Release summary](#release-summary-2027.0.20261119)
+ [Repository Updates](#repository-updates-2027.0.20261119)
  + [Core New Packages](#amis-2027.0.20261119.Core-New-Packages)
  + [Core Updated Packages](#amis-2027.0.20261119.Core-Updated-Packages)
+ [Image Updates](#ami-updates-2027.0.20261119)
  + [Default Kernel 7.2 AMI](#amis-2027.0.20261119.Default-Kernel-7-2-AMI)
  + [Minimal Kernel 7.2 AMI](#amis-2027.0.20261119.Minimal-Kernel-7-2-AMI)
  + [Default Container](#amis-2027.0.20261119.Default-Container)
  + [Minimal Container](#amis-2027.0.20261119.Minimal-Container)
+ [Contact us](#amis-2027.0.20261119.contact-us)

**AL2027 Preview**
 AL2027 is currently available for preview, for more information see the [ AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/what-is.html). It is intended for evaluation and testing only and is not recommended for production workloads.

## Release summary
<a name="release-summary-2027.0.20261119"></a>

This release is an update to the AL2027 preview.

**Notable updates**
+ The PostgreSQL packages have been updated to the latest upstream release. After updating, you may need to rebuild C-language extensions against the updated PostgreSQL packages. Extensions in `postgresql-contrib` subpackages have already been built against the latest release. For full list of post-update steps, see the [PostgreSQL release notes](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/).
+ The AL2027 preview now uses ClockBound as the NTP client. This improves system clock accuracy and exposes an API for a true time error bound. For more information, see [ClockBound](https://aws.github.io/clock-bound/).

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center CVE Explorer](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2027.0.20261119"></a>

### Core New Packages
<a name="amis-2027.0.20261119.Core-New-Packages"></a>

This section provides details about Core New Packages.

| Package |
| --- |
|  cloudformation-validate-1.16.0-1.amzn2027.0.1  |
|  rust-ripgrep-15.2.0-2.amzn2027  |

### Core Updated Packages
<a name="amis-2027.0.20261119.Core-Updated-Packages"></a>

This section provides details about Core Updated Packages.

| Package |
| --- |
|  aardvark-dns-2.1.0-1.amzn2027.0.2  |
|  amazon-ecr-credential-helper-0.13.0-2.amzn2027  |
|  amazon-efs-utils-4.0.0-1.amzn2027  |
|  buildah-1.45.1-1.amzn2027.0.3  |
|  firefox-153.7.0-1.amzn2027.0.2  |
|  ghostscript-10.08.0-1.amzn2027.0.2  |
|  java-1.8.0-amazon-corretto-1.8.0\_514.b01-1.amzn2027  |
|  java-11-amazon-corretto-11.0.33.1.1-1.amzn2027  |
|  kiwi-image-descriptions-examples-1.0.3-1.amzn2027  |
|  krb5-1.22.2-8.amzn2027.0.1  |
|  libXfont2-2.0.8-1.amzn2027.0.2  |
|  libfontenc-1.1.7-3.amzn2027.0.2  |
|  openjpeg-2.5.4-4.amzn2027.0.3  |
|  php8.5-8.5.13-1.amzn2027.0.1  |
|  podman-6.1.4-2.amzn2027  |
|  postgresql16-16.16-1.amzn2027.0.1  |
|  postgresql17-17.12-1.amzn2027.0.1  |
|  postgresql18-18.7-1.amzn2027.0.1  |
|  rclone-1.75.2-2.amzn2027  |
|  ruby3.4-3.4.12-27.amzn2027.0.8  |
|  selinux-policy-45.23-4.amzn2027  |
|  skopeo-1.24.1-1.amzn2027.0.3  |
|  swiftlang-6.3.2-3.amzn2027  |
|  system-release-2027.0.20261119-0.amzn2027  |

## Image Updates
<a name="ami-updates-2027.0.20261119"></a>

### Default Kernel 7.2 AMI
<a name="amis-2027.0.20261119.Default-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Default Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261119-0.amzn2027  |
|  krb5-libs-1.22.2-8.amzn2027.0.1  |
|  selinux-policy-targeted-45.23-4.amzn2027  |
|  selinux-policy-45.23-4.amzn2027  |
|  system-release-2027.0.20261119-0.amzn2027  |

### Minimal Kernel 7.2 AMI
<a name="amis-2027.0.20261119.Minimal-Kernel-7-2-AMI"></a>

This section provides details about new/updated packages in Minimal Kernel 7.2 AMI.

| Package |
| --- |
|  amazon-linux-repo-s3-2027.0.20261119-0.amzn2027  |
|  krb5-libs-1.22.2-8.amzn2027.0.1  |
|  selinux-policy-targeted-45.23-4.amzn2027  |
|  selinux-policy-45.23-4.amzn2027  |
|  system-release-2027.0.20261119-0.amzn2027  |

### Default Container
<a name="amis-2027.0.20261119.Default-Container"></a>

This section provides details about new/updated packages in Default Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261119-0.amzn2027  |
|  krb5-libs-1.22.2-8.amzn2027.0.1  |
|  system-release-2027.0.20261119-0.amzn2027  |

### Minimal Container
<a name="amis-2027.0.20261119.Minimal-Container"></a>

This section provides details about new/updated packages in Minimal Container.

| Package |
| --- |
|  amazon-linux-repo-cdn-2027.0.20261119-0.amzn2027  |
|  krb5-libs-1.22.2-8.amzn2027.0.1  |
|  system-release-2027.0.20261119-0.amzn2027  |

## Contact us
<a name="amis-2027.0.20261119.contact-us"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

We use GitHub issues to gather feedback about AL2027 and to track bug reports and feature requests. You can look at [existing issues on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues) to see whether your concern is already known. If it is not, open a [new issue on GitHub](https://github.com/amazonlinux/amazon-linux-2027/issues/new/choose).

If you only have questions about AL2027, start or join a [discussion on GitHub](https://github.com/amazonlinux/amazon-linux-2027/discussions). Feedback on AL2027 can also be provided through your designated AWS representative.
