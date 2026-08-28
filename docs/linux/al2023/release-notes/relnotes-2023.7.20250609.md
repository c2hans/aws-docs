---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250609.html
---

# Amazon Linux 2023 version 2023.7.20250609 release notes
<a name="relnotes-2023.7.20250609"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250609.

**Contents**
+ [Release Summary](#release-summary-2023.7.20250609)
+ [Repository Updates](#repository-updates-2023.7.20250609)
  + [Core New Packages](#amis-2023.7.20250609.Core-New-Packages)
  + [Core Updated Packages](#amis-2023.7.20250609.Core-Updated-Packages)
  + [Kernel-livepatch New Packages](#amis-2023.7.20250609.Kernel-livepatch-New-Packages)
+ [Image Updates](#ami-updates-2023.7.20250609)
  + [Default Kernel 6.1 AMI](#amis-2023.7.20250609.Default-Kernel-6-1-AMI)
  + [Minimal Kernel 6.1 AMI](#amis-2023.7.20250609.Minimal-Kernel-6-1-AMI)
  + [Default Kernel 6.12 AMI](#amis-2023.7.20250609.Default-Kernel-6-12-AMI)
  + [Minimal Kernel 6.12 AMI](#amis-2023.7.20250609.Minimal-Kernel-6-12-AMI)
  + [Default Container](#amis-2023.7.20250609.Default-Container)
  + [Minimal Container](#amis-2023.7.20250609.Minimal-Container)
+ [Contact us](#amis-2023.7.20250609.contact-us)

## Release Summary
<a name="release-summary-2023.7.20250609"></a>

This release represents an update to the 7th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository Updates
<a name="repository-updates-2023.7.20250609"></a>

### Core New Packages
<a name="amis-2023.7.20250609.Core-New-Packages"></a>

This section provides details about core new packages.

|  |
| --- |
|  qemu-9.2.3-1082.amzn2023  |

### Core Updated Packages
<a name="amis-2023.7.20250609.Core-Updated-Packages"></a>

This section provides details about core updated packages.

|  |
| --- |
|  amazon-ec2-net-utils-2.6.0-1.amzn2023.0.1  |
|  amazon-ssm-agent-3.3.2299.0-1.amzn2023  |
|  apache-commons-beanutils-1.11.0-10.amzn2023.0.1  |
|  cni-plugins-1.7.1-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.7-1.amzn2023  |
|  dotnet8.0-8.0.116-1.amzn2023.0.1  |
|  ecs-init-1.94.0-1.amzn2023  |
|  firefox-128.11.0-1.amzn2023.0.2  |
|  ghostscript-9.56.1-7.amzn2023.0.17  |
|  git-2.47.1-1.amzn2023.0.3  |
|  glibc-2.34-196.amzn2023.0.1  |
|  gnome-control-center-47.3-195.amzn2023  |
|  json-glib-1.10.0-1.amzn2023.0.2  |
|  kernel-6.1.140-154.222.amzn2023  |
|  kernel6.12-6.12.30-34.92.amzn2023  |
|  libsoup-2.72.0-6.amzn2023.0.6  |
|  libsoup3-3.6.5-49.amzn2023  |
|  libuv-1.51.0-1.amzn2023.0.1  |
|  mariadb1011-10.11.11-1.amzn2023.0.2  |
|  network-flow-monitor-agent-0.1.4-1.amzn2023.0.1  |
|  nodejs20-20.19.2-1.amzn2023.0.1  |
|  nodejs22-22.16.0-1.amzn2023.0.1  |
|  perl-5.32.1-477.amzn2023.0.7  |
|  python-setuptools-59.6.0-2.amzn2023.0.6  |
|  python-tornado-6.1.0-2.amzn2023.0.5  |
|  python3.11-setuptools-65.5.1-2.amzn2023.0.7  |
|  python3.12-setuptools-68.2.2-4.amzn2023.0.3  |
|  screen-4.8.0-5.amzn2023.0.4  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Kernel-livepatch New Packages
<a name="amis-2023.7.20250609.Kernel-livepatch-New-Packages"></a>

This section provides details about kernel-livepatch new packages.

|  |
| --- |
|  kernel-livepatch-6.1.130-139.222-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.131-143.221-1.0-3.amzn2023  |
|  kernel-livepatch-6.1.132-147.221-1.0-1.amzn2023  |
|  kernel-livepatch-6.1.134-150.224-1.0-2.amzn2023  |
|  kernel-livepatch-6.1.134-152.225-1.0-2.amzn2023  |
|  kernel-livepatch-6.12.20-23.97-1.0-3.amzn2023  |
|  kernel-livepatch-6.12.22-27.96-1.0-1.amzn2023  |

## Image Updates
<a name="ami-updates-2023.7.20250609"></a>

### Default Kernel 6.1 AMI
<a name="amis-2023.7.20250609.Default-Kernel-6-1-AMI"></a>

This section provides details about default kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.6.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250609-0.amzn2023  |
|  amazon-ssm-agent-3.3.2299.0-1.amzn2023  |
|  dnf-plugin-support-info-1.7-1.amzn2023  |
|  glibc-all-langpacks-2.34-196.amzn2023.0.1  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-196.amzn2023.0.1  |
|  glibc-locale-source-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  kernel-libbpf-6.12.30-34.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250609-0.amzn2023  |
|  kernel-tools-6.12.30-34.92.amzn2023  |
|  kernel-6.1.140-154.222.amzn2023  |
|  libuv-1:1.51.0-1.amzn2023.0.1  |
|  perl-Class-Struct-0.66-477.amzn2023.0.7  |
|  perl-DynaLoader-1.47-477.amzn2023.0.7  |
|  perl-Errno-1.30-477.amzn2023.0.7  |
|  perl-Fcntl-1.13-477.amzn2023.0.7  |
|  perl-File-Basename-2.85-477.amzn2023.0.7  |
|  perl-File-stat-1.09-477.amzn2023.0.7  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.7  |
|  perl-IO-1.43-477.amzn2023.0.7  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.7  |
|  perl-POSIX-1.94-477.amzn2023.0.7  |
|  perl-SelectSaver-1.02-477.amzn2023.0.7  |
|  perl-Symbol-1.08-477.amzn2023.0.7  |
|  perl-if-0.60.800-477.amzn2023.0.7  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.7  |
|  perl-libs-4:5.32.1-477.amzn2023.0.7  |
|  perl-mro-1.23-477.amzn2023.0.7  |
|  perl-overload-1.31-477.amzn2023.0.7  |
|  perl-overloading-0.02-477.amzn2023.0.7  |
|  perl-subs-1.03-477.amzn2023.0.7  |
|  perl-vars-1.05-477.amzn2023.0.7  |
|  python3-setuptools-wheel-59.6.0-2.amzn2023.0.6  |
|  python3-setuptools-59.6.0-2.amzn2023.0.6  |
|  screen-4.8.0-5.amzn2023.0.4  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Minimal Kernel 6.1 AMI
<a name="amis-2023.7.20250609.Minimal-Kernel-6-1-AMI"></a>

This section provides details about minimal kernel 6.1 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.6.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250609-0.amzn2023  |
|  dnf-plugin-support-info-1.7-1.amzn2023  |
|  glibc-all-langpacks-2.34-196.amzn2023.0.1  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-locale-source-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  kernel-libbpf-6.12.30-34.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250609-0.amzn2023  |
|  kernel-6.1.140-154.222.amzn2023  |
|  python3-setuptools-wheel-59.6.0-2.amzn2023.0.6  |
|  python3-setuptools-59.6.0-2.amzn2023.0.6  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Default Kernel 6.12 AMI
<a name="amis-2023.7.20250609.Default-Kernel-6-12-AMI"></a>

This section provides details about default kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.6.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250609-0.amzn2023  |
|  amazon-ssm-agent-3.3.2299.0-1.amzn2023  |
|  dnf-plugin-support-info-1.7-1.amzn2023  |
|  glibc-all-langpacks-2.34-196.amzn2023.0.1  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-gconv-extra-2.34-196.amzn2023.0.1  |
|  glibc-locale-source-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  kernel-libbpf-6.12.30-34.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250609-0.amzn2023  |
|  kernel-tools-6.12.30-34.92.amzn2023  |
|  kernel6.12-6.12.30-34.92.amzn2023  |
|  libuv-1:1.51.0-1.amzn2023.0.1  |
|  perl-Class-Struct-0.66-477.amzn2023.0.7  |
|  perl-DynaLoader-1.47-477.amzn2023.0.7  |
|  perl-Errno-1.30-477.amzn2023.0.7  |
|  perl-Fcntl-1.13-477.amzn2023.0.7  |
|  perl-File-Basename-2.85-477.amzn2023.0.7  |
|  perl-File-stat-1.09-477.amzn2023.0.7  |
|  perl-Getopt-Std-1.12-477.amzn2023.0.7  |
|  perl-IO-1.43-477.amzn2023.0.7  |
|  perl-IPC-Open3-1.21-477.amzn2023.0.7  |
|  perl-POSIX-1.94-477.amzn2023.0.7  |
|  perl-SelectSaver-1.02-477.amzn2023.0.7  |
|  perl-Symbol-1.08-477.amzn2023.0.7  |
|  perl-if-0.60.800-477.amzn2023.0.7  |
|  perl-interpreter-4:5.32.1-477.amzn2023.0.7  |
|  perl-libs-4:5.32.1-477.amzn2023.0.7  |
|  perl-mro-1.23-477.amzn2023.0.7  |
|  perl-overload-1.31-477.amzn2023.0.7  |
|  perl-overloading-0.02-477.amzn2023.0.7  |
|  perl-subs-1.03-477.amzn2023.0.7  |
|  perl-vars-1.05-477.amzn2023.0.7  |
|  python3-setuptools-wheel-59.6.0-2.amzn2023.0.6  |
|  python3-setuptools-59.6.0-2.amzn2023.0.6  |
|  screen-4.8.0-5.amzn2023.0.4  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Minimal Kernel 6.12 AMI
<a name="amis-2023.7.20250609.Minimal-Kernel-6-12-AMI"></a>

This section provides details about minimal kernel 6.12 ami.

|  |
| --- |
|  amazon-ec2-net-utils-2.6.0-1.amzn2023.0.1  |
|  amazon-linux-repo-s3-2023.7.20250609-0.amzn2023  |
|  dnf-plugin-support-info-1.7-1.amzn2023  |
|  glibc-all-langpacks-2.34-196.amzn2023.0.1  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-locale-source-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  kernel-libbpf-6.12.30-34.92.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250609-0.amzn2023  |
|  kernel6.12-6.12.30-34.92.amzn2023  |
|  python3-setuptools-wheel-59.6.0-2.amzn2023.0.6  |
|  python3-setuptools-59.6.0-2.amzn2023.0.6  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Default Container
<a name="amis-2023.7.20250609.Default-Container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250609-0.amzn2023  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  python3-setuptools-wheel-59.6.0-2.amzn2023.0.6  |
|  system-release-2023.7.20250609-0.amzn2023  |

### Minimal Container
<a name="amis-2023.7.20250609.Minimal-Container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250609-0.amzn2023  |
|  glibc-common-2.34-196.amzn2023.0.1  |
|  glibc-minimal-langpack-2.34-196.amzn2023.0.1  |
|  glibc-2.34-196.amzn2023.0.1  |
|  system-release-2023.7.20250609-0.amzn2023  |

## Contact us
<a name="amis-2023.7.20250609.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
