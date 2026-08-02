---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240528.html
---

# Amazon Linux 2023 version 2023.4.20240528 release notes
<a name="relnotes-2023.4.20240528"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240528 release

## Major updates
<a name="major-updates-2023.4.20240528"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240528)
+ [Repository](#amis-2023.4.20240528.repository)
+ [Docker container image](#amis-2023.4.20240528.container-image)
+ [Default AMI](#amis-2023.4.20240528.default-ami)
+ [Minimal AMI](#amis-2023.4.20240528.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240528.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240528.repository"></a>

### AL2023.4.20240528 upgrades from AL2023.4.20240513
<a name="vercmp-AL2023.4.20240513-AL2023.4.20240528"></a>

 Comparing [2023.4.20240513](relnotes-2023.4.20240513.md) to [2023.4.20240528](#relnotes-2023.4.20240528).

| Package Type | Count |
| --- | --- |
| Source | 17 |
| Total Binary | 242 |
|  noarch binary RPMs | 100 |
|  x86\_64 binary RPMs | 71 |
|  aarch64 binary RPMs | 71 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 1.300033.0-1.amzn2023
  - **AL2023.4.20240528 version:** 1.300039.0-1.amzn2023

- ** `amazon-ecr-credential-helper` **
  - **RPM:**  amazon-ecr-credential-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 0.7.1-2.amzn2023
  - **AL2023.4.20240528 version:** 0.7.1-4.amzn2023

- ** `BabelfishDump` **
  - **RPM:**  BabelfishDump
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 16.1-1.amzn2023.0.2
  - **AL2023.4.20240528 version:** 16.3-1.amzn2023.0.1

- ** `bcc` **
  - **RPM:**  bcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bcc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bcc-doc  / **Architectures:** noarch
  - **RPM:**  bcc-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbpf-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bcc  / **Architectures:** noarch
  - **AL2023.4.20240513 version:** 0.26.0-1.amzn2023.0.1
  - **AL2023.4.20240528 version:** 0.26.0-1.amzn2023.0.2

- ** `bpftrace` **
  - **RPM:**  bpftrace
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 0.17.0-1.amzn2023
  - **AL2023.4.20240528 version:** 0.17.0-1.amzn2023.0.1

- ** `cni-plugins` **
  - **RPM:**  cni-plugins
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 1.2.0-1.amzn2023.0.4
  - **AL2023.4.20240528 version:** 1.2.0-1.amzn2023.0.5

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 1.82.3-1.amzn2023
  - **AL2023.4.20240528 version:** 1.82.4-1.amzn2023

- ** `fdupes` **
  - **RPM:**  fdupes
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 2.1.1-2.amzn2023.0.2
  - **AL2023.4.20240528 version:** 2.3.0-1.amzn2023

- ** `ghostscript` **
  - **RPM:**  ghostscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-doc  / **Architectures:** noarch
  - **RPM:**  ghostscript-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-dvipdf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-fonts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-tools-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 9.56.1-7.amzn2023.0.5
  - **AL2023.4.20240528 version:** 9.56.1-7.amzn2023.0.6

- ** `git` **
  - **RPM:**  git  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-all  / **Architectures:** noarch
  - **RPM:**  git-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-core-doc  / **Architectures:** noarch
  - **RPM:**  git-credential-libsecret  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-cvs  / **Architectures:** noarch
  - **RPM:**  git-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-email  / **Architectures:** noarch
  - **RPM:**  git-gui  / **Architectures:** noarch
  - **RPM:**  git-instaweb  / **Architectures:** noarch
  - **RPM:**  gitk  / **Architectures:** noarch
  - **RPM:**  git-p4  / **Architectures:** noarch
  - **RPM:**  git-subtree  / **Architectures:** noarch
  - **RPM:**  git-svn  / **Architectures:** noarch
  - **RPM:**  gitweb  / **Architectures:** noarch
  - **RPM:**  perl-Git  / **Architectures:** noarch
  - **RPM:**  perl-Git-SVN  / **Architectures:** noarch
  - **AL2023.4.20240513 version:** 2.40.1-1.amzn2023.0.2
  - **AL2023.4.20240528 version:** 2.40.1-1.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.4.20240513 version:** 1.20.12-1.amzn2023.0.2
  - **AL2023.4.20240528 version:** 1.22.3-1.amzn2023.0.1

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
  - **AL2023.4.20240513 version:** 6.1.90-99.173.amzn2023
  - **AL2023.4.20240528 version:** 6.1.91-99.172.amzn2023

- ** `less` **
  - **RPM:**  less
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 608-2.amzn2023.0.1
  - **AL2023.4.20240528 version:** 608-2.amzn2023.0.2

- ** `libreswan` **
  - **RPM:**  libreswan
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 4.12-3.amzn2023.0.1
  - **AL2023.4.20240528 version:** 4.12-3.amzn2023.0.2

- ** `oci-add-hooks` **
  - **RPM:**  oci-add-hooks
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 0-0.1.20200504git268e3bb.amzn2023.0.2
  - **AL2023.4.20240528 version:** 0-0.1.20200504git268e3bb.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240513 version:** 8.2.15-1.amzn2023.0.2
  - **AL2023.4.20240528 version:** 8.2.18-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240513 version:** 2023.4.20240513-1.amzn2023
  - **AL2023.4.20240528 version:** 2023.4.20240528-0.amzn2023

## Docker container image
<a name="amis-2023.4.20240528.container-image"></a>
+ `amazon-linux-repo-cdn-2023.4.20240528-0.amzn2023`
+ `system-release-2023.4.20240528-0.amzn202`

## Default AMI
<a name="amis-2023.4.20240528.default-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240528-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240528-0.amzn2023`
+ `kernel-tools-6.1.91-99.172.amzn2023`
+ `kernel-6.1.91-99.172.amzn2023`
+ `less-608-2.amzn2023.0.2`
+ `system-release-2023.4.20240528-0.amzn2023`

## Minimal AMI
<a name="amis-2023.4.20240528.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240528-0.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240528-0.amzn2023`
+ `kernel-6.1.91-99.172.amzn2023`
+ `less-608-2.amzn2023.0.2`
+ `system-release-2023.4.20240528-0.amzn2023`

## Minimal container image
<a name="amis-2023.4.20240528.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240528-0.amzn2023`
+ `system-release-2023.4.20240528-0.amzn2023`
