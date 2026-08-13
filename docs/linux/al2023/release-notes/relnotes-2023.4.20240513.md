---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240513.html
---

# Amazon Linux 2023 version 2023.4.20240513 release notes
<a name="relnotes-2023.4.20240513"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240513 release.

## Major updates
<a name="major-updates-2023.4.20240513"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240513)
+ [Repository](#amis-2023.4.20240513.repository)
+ [Docker container image](#amis-2023.4.20240513.container-image)
+ [Default AMI](#amis-2023.4.20240513.default-ami)
+ [Minimal AMI](#amis-2023.4.20240513.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240513.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240513.repository"></a>

### AL2023.4.20240513 upgrades from AL2023.4.20240429
<a name="vercmp-AL2023.4.20240429-AL2023.4.20240513"></a>

 Comparing [2023.4.20240429](relnotes-2023.4.20240429.md) to [2023.4.20240513](#relnotes-2023.4.20240513).

| Package Type | Count |
| --- | --- |
| Source | 14 |
| Total Binary | 210 |
|  noarch binary RPMs | 48 |
|  x86\_64 binary RPMs | 81 |
|  aarch64 binary RPMs | 81 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 3.3.131.0-1.amzn2023
  - **AL2023.4.20240513 version:** 3.3.380.0-1.amzn2023

- ** `awscli-2` **
  - **RPM:**  awscli-2
  - **Architectures:** noarch
  - **AL2023.4.20240429 version:** 2.14.5-1.amzn2023.0.1
  - **AL2023.4.20240513 version:** 2.15.30-1.amzn2023.0.1

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 1.2.3-0.amzn2023
  - **AL2023.4.20240513 version:** 1.3.0-0.amzn2023

- ** `clamav` **
  - **RPM:**  clamav  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-data  / **Architectures:** noarch
  - **RPM:**  clamav-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-doc  / **Architectures:** noarch
  - **RPM:**  clamav-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-update  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 0.103.9-1.amzn2023.0.2
  - **AL2023.4.20240513 version:** 0.103.11-1.amzn2023.0.1

- ** `cni-plugins` **
  - **RPM:**  cni-plugins
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 1.2.0-1.amzn2023.0.3
  - **AL2023.4.20240513 version:** 1.2.0-1.amzn2023.0.4

- ** `debugedit` **
  - **RPM:**  debugedit
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 5.0-2.amzn2023.0.2
  - **AL2023.4.20240513 version:** 5.0-2.amzn2023.0.3

- ** `flatpak` **
  - **RPM:**  flatpak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-selinux  / **Architectures:** noarch
  - **RPM:**  flatpak-session-helper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 1.15.4-3.amzn2023.0.1
  - **AL2023.4.20240513 version:** 1.15.4-3.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 6.1.87-99.174.amzn2023
  - **AL2023.4.20240513 version:** 6.1.90-99.173.amzn2023

- ** [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 8.1.27-1.amzn2023.0.2
  - **AL2023.4.20240513 version:** 8.1.28-1.amzn2023.0.1

- ** [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 3.11.6-1.amzn2023.0.2
  - **AL2023.4.20240513 version:** 3.11.6-1.amzn2023.0.3

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.4.20240429 version:** 3.9.16-1.amzn2023.0.7
  - **AL2023.4.20240513 version:** 3.9.16-1.amzn2023.0.8

- ** `python-pymongo` **
  - **RPM:**  python3-bson  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pymongo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pymongo-gridfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-pymongo-doc  / **Architectures:** noarch
  - **AL2023.4.20240429 version:** 3.10.1-5.amzn2023.0.2
  - **AL2023.4.20240513 version:** 3.10.1-5.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240429 version:** 2023.4.20240429-0.amzn2023
  - **AL2023.4.20240513 version:** 2023.4.20240513-1.amzn2023

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240429 version:** 1.17.1-1.amzn2023.0.3
  - **AL2023.4.20240513 version:** 1.17.1-1.amzn2023.0.5

## Docker container image
<a name="amis-2023.4.20240513.container-image"></a>
+ `amazon-linux-repo-cdn-2023.4.20240513-1.amzn2023`
+ `python3-libs-3.9.16-1.amzn2023.0.8`
+ `python3-3.9.16-1.amzn2023.0.8`
+ `system-release-2023.4.20240513-1.amzn2023`

## Default AMI
<a name="amis-2023.4.20240513.default-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240513-1.amzn2023`
+ `amazon-ssm-agent-3.3.380.0-1.amzn2023 `
+ `awscli-2-2.15.30-1.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.4.20240513-1.amzn2023`
+ `kernel-tools-6.1.90-99.173.amzn2023`
+ `kernel-6.1.90-99.173.amzn2023`
+ `python3-libs-3.9.16-1.amzn2023.0.8`
+ `python3-3.9.16-1.amzn2023.0.8`
+ `system-release-2023.4.20240513-1.amzn2023`

## Minimal AMI
<a name="amis-2023.4.20240513.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240513-1.amzn2023`
+ `awscli-2-2.15.30-1.amzn2023.0.1`
+ `kernel-livepatch-repo-s3-2023.4.20240513-1.amzn2023`
+ `kernel-6.1.90-99.173.amzn2023`
+ `python3-libs-3.9.16-1.amzn2023.0.8`
+ `python3-3.9.16-1.amzn2023.0.8`
+ `system-release-2023.4.20240513-1.amzn2023`

## Minimal container image
<a name="amis-2023.4.20240513.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240513-1.amzn2023`
+ `system-release-2023.4.20240513-1.amzn2023`
