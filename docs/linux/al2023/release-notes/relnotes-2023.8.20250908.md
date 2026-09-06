---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.8.20250908.html
---

# Amazon Linux 2023 version 2023.8.20250908 release notes
<a name="relnotes-2023.8.20250908"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.8.20250908.

**Contents**
+ [Release Summary](#release-summary-2023.8.20250908)
+ [Repository Updates](#repository-updates-2023.8.20250908)
  + [Core New Packages](#amis-2023.8.20250908.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.8.20250908.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.8.20250908.Kernel-livepatch-New-Packages)
  + [Kernel-livepatch Updated Packages](#amis-2023.8.20250908.Kernel-livepatch-Updated-Packages)
+ [Image Updates](#ami-updates-2023.8.20250908)
  + [Default Kernel 6.1 AMI](#amis-2023.8.20250908.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.8.20250908.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.8.20250908.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.8.20250908.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.8.20250908.Default-Container)
  + [Minimal Container](#amis-2023.8.20250908.Minimal-Container)
+ [Contact us](#amis-2023.8.20250908.contact-us)

## Release Summary
<a name="release-summary-2023.8.20250908"></a>

This release represents an update to the 8th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Notable updates**
+ The `nodejs20-typescript-5.7.3-1.amzn2023.0.1` and `nodejs22-typescript-5.7.3-1.amzn2023.0.1` packages bring the TypeScript compiler as globally installed node modules to the Node.js 20 and 22 runtimes respectively. Both packages support simultaneous installation. The default name of the tsc executable uses the Node.js runtime selected with the `alternatives` tool. The current configuration can be viewed with the `"alternatives --display tsc"` command. However, the namespaced executables `(e.g., tsc-20 or tsc-22)` will always use the corresponding Node.js runtime and can be run independently of the current alternatives selection.
+ Following the mitigation of CVE-2025-23048 in `Apache httpd`, some websites may experience a "Misdirected Request" error, especially if a web server operates behind a load balancer. Currently, this issue is particularly noticeable with Application Load Balancers, which, at this time, do not relay SNI data to the target server. Apache httpd used to allow clients to send requests without setting a server name in the SNI because the check wasn't accurate. However, this behavior changed in version 2.4.64. There are several known solutions and/or workarounds depending on the load balancer and its configuration. For more information, see the [Apache bug tracker](https://bz.apache.org/bugzilla/show_bug.cgi?id=69743).
+ `haproxy` updated from `2.8.3 to 3.0.5 (LTS)`. Configuration remains broadly backward-compatible. Notable deltas in 3.0 include stricter HTTP/1 request-target parsing, a runtime API single-command requirement, rejection of the enabled keyword on dynamic servers, and the rename tune.ssl.oscp-update → tune.oscp-update. For more information, see the [HAProxy 3.0 release notes](https://www.haproxy.com/blog/announcing-haproxy-3-0#breaking-changes).
+ Amazon Linux will stop evaluating and fixing CVEs for the redis6 package in Amazon Linux 2023 on `2026-01-31`. This is an extension from the previous [package support statement](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html) which stated that support for Redis 6 ends on `2025-08-31`. With the release of Redis 8, upstream security support for Redis 6.2 will be ending in 2025. For migration instructions, see the [migration guide](https://docs.aws.amazon.com/linux/al2023/ug/redis6-to-valkey-al2023.html).
+ krb5: The KDC will not issue tickets with RC4 session keys unless explicitly configured using the new `allow_rc4` variable in `[libdefaults]`. This change resolves CVE-2025-3576.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.8.20250908"></a>

### Core New Packages
<a name="amis-2023.8.20250908.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  aws-nitro-tpm-tools-1.0.0-2.amzn2023  |
|  dotnet9.0-9.0.107-1.amzn2023.0.1  |
|  kiwi-image-descriptions-examples-1.0.1-1.amzn2023  |
|  ladspa-1.17-1.amzn2023  |
|  libid3tag-0.16.3-1.amzn2023  |
|  libsamplerate-0.2.2-1.amzn2023  |
|  nodejs20-typescript-5.7.3-1.amzn2023.0.1  |
|  nodejs22-typescript-5.7.3-1.amzn2023.0.1  |
|  perl-Class-Std-Utils-0.0.3-1.amzn2023.0.1  |
|  perl-Crypt-Blowfish\_PP-1.12-37.amzn2023.0.1  |
|  perl-Crypt-PBKDF2-0.161520-22.amzn2023.0.1  |
|  perl-Net-Domain-TLD-1.75-25.amzn2023.0.1  |
|  perl-Net-SFTP-Foreign-1.93-13.amzn2023.0.1  |
|  perl-Proc-ProcessTable-0.636-5.amzn2023.0.1  |
|  perl-String-Scanf-2.1-1.amzn2023.0.1  |
|  perl-String-ShellQuote-1.04-44.amzn2023.0.1  |
|  python-asn1crypto-1.5.1-11.amzn2023  |
|  sox-14.4.2.0-1.amzn2023  |
|  tpm2-abrmd-3.0.0-7.amzn2023  |
|  tpm2-abrmd-selinux-2.3.1-13.amzn2023  |

### Core Updated Packages
<a name="amis-2023.8.20250908.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  ImageMagick-6.9.12.82-1.amzn2023.0.10  |
|  aws-cfn-bootstrap-2.0-36.amzn2023  |
|  cairo-1.18.0-4.amzn2023.0.3  |
|  ecs-init-1.98.0-1.amzn2023  |
|  firefox-140.2.0-1.amzn2023.0.1  |
|  gnome-remote-desktop-47.3-1.amzn2023.0.1  |
|  golang-1.24.6-1.amzn2023.0.1  |
|  haproxy-3.0.5-1.amzn2023.0.1  |
|  jq-1.7.1-51.amzn2023  |
|  kernel-6.1.148-173.267.amzn2023  |
|  kernel6.12-6.12.40-64.114.amzn2023  |
|  krb5-1.21.3-6.amzn2023.0.1  |
|  libpq-17.6-1.amzn2023.0.1  |
|  libssh-0.10.6-1.amzn2023.0.2  |
|  libtiff-4.4.0-4.amzn2023.0.21  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  mod\_security-2.9.12-1.amzn2023.0.1  |
|  perl-Authen-SASL-2.16-23.amzn2023.0.3  |
|  postgresql15-15.14-1.amzn2023.0.1  |
|  postgresql17-17.6-1.amzn2023.0.1  |
|  ruby3.2-3.2.8-184.amzn2023.0.5  |
|  runfinch-finch-1.10.0-1.amzn2023.0.3  |
|  rust-1.89.0-1.amzn2023.0.2  |
|  showtime-48.1-11.amzn2023  |
|  system-release-2023.8.20250908-0.amzn2023  |
|  taglib-1.12-4.amzn2023.0.3  |
|  tomcat10-10.1.44-1.amzn2023.0.1  |
|  tomcat9-9.0.108-1.amzn2023.0.1  |
|  udisks2-2.10.1-6.amzn2023.0.3  |
|  xfsprogs-6.12.0-3.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.8.20250908.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.141-155.222-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.141-165.249-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.141-167.250-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.144-170.251-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.147-172.259-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.31-35.92-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.35-55.103-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.37-61.105-1.0-1.amzn2023  |
|  kernel-livepatch-6.12.40-63.107-1.0-1.amzn2023  |

### Kernel-livepatch Updated Packages
<a name="amis-2023.8.20250908.Kernel-livepatch-Updated-Packages"></a>

This section provides details about kernel-livepatch updated packages.

|  |
| --- |
|  kernel-livepatch-6.1.140-154.222-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.25-32.101-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.29-33.102-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.30-34.92-1.0-3.amzn2023  |

## Image Updates
<a name="ami-updates-2023.8.20250908"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.8.20250908.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250908-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-36.amzn2023  |
|  jq-1.7.1-51.amzn2023  |
|  kernel-libbpf-1:6.1.148-173.267.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250908-0.amzn2023  |
|  kernel-tools-1:6.1.148-173.267.amzn2023  |
|  kernel-1:6.1.148-173.267.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.2  |
|  system-release-2023.8.20250908-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.8.20250908.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250908-0.amzn2023  |
|  jq-1.7.1-51.amzn2023  |
|  kernel-libbpf-1:6.1.148-173.267.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250908-0.amzn2023  |
|  kernel-1:6.1.148-173.267.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  system-release-2023.8.20250908-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.8.20250908.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250908-0.amzn2023  |
|  aws-cfn-bootstrap-2.0-36.amzn2023  |
|  jq-1.7.1-51.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250908-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-64.114.amzn2023  |
|  kernel6.12-tools-1:6.12.40-64.114.amzn2023  |
|  kernel6.12-1:6.12.40-64.114.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  rust-toolset-srpm-macros-1.89.0-1.amzn2023.0.2  |
|  system-release-2023.8.20250908-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.8.20250908.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.8.20250908-0.amzn2023  |
|  jq-1.7.1-51.amzn2023  |
|  kernel-livepatch-repo-s3-2023.8.20250908-0.amzn2023  |
|  kernel6.12-libbpf-1:6.12.40-64.114.amzn2023  |
|  kernel6.12-1:6.12.40-64.114.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  system-release-2023.8.20250908-0.amzn2023  |
|  xfsprogs-6.12.0-3.amzn2023  |

### Default Container
<a name="amis-2023.8.20250908.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250908-0.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  system-release-2023.8.20250908-0.amzn2023  |

### Minimal Container
<a name="amis-2023.8.20250908.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.8.20250908-0.amzn2023  |
|  krb5-libs-1.21.3-6.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.13  |
|  system-release-2023.8.20250908-0.amzn2023  |

## Contact us
<a name="amis-2023.8.20250908.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
