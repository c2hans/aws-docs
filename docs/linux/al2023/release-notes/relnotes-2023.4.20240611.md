---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240611.html
---

# Amazon Linux 2023 version 2023.4.20240611 release notes
<a name="relnotes-2023.4.20240611"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240611 release

## Major updates
<a name="major-updates-2023.4.20240611"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240611)
+ [Repository](#amis-2023.4.20240611.repository)
+ [Docker container image](#amis-2023.4.20240611.container-image)
+ [Default AMI](#amis-2023.4.20240611.default-ami)
+ [Minimal AMI](#amis-2023.4.20240611.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240611.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240611.repository"></a>

### AL2023.4.20240611 upgrades from AL2023.4.20240528
<a name="vercmp-AL2023.4.20240528-AL2023.4.20240611"></a>

 Comparing [2023.4.20240528](relnotes-2023.4.20240528.md) to [2023.4.20240611](#relnotes-2023.4.20240611).

| Package Type | Count |
| --- | --- |
| Source | 15 |
| Total Binary | 184 |
|  noarch binary RPMs | 64 |
|  x86\_64 binary RPMs | 60 |
|  aarch64 binary RPMs | 60 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 1.300039.0-1.amzn2023
  - **AL2023.4.20240611 version:** 1.300041.0-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/efs.html](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/efs.html](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 2.0.1-1.amzn2023
  - **AL2023.4.20240611 version:** 2.0.2-1.amzn2023

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2023.4.20240528 version:** 2.0-29.amzn2023
  - **AL2023.4.20240611 version:** 2.0-30.amzn2023

- ** `bouncycastle` **
  - **RPM:**  bouncycastle  / **Architectures:** noarch
  - **RPM:**  bouncycastle-javadoc  / **Architectures:** noarch
  - **RPM:**  bouncycastle-mail  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pg  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pkix  / **Architectures:** noarch
  - **RPM:**  bouncycastle-tls  / **Architectures:** noarch
  - **RPM:**  bouncycastle-util  / **Architectures:** noarch
  - **AL2023.4.20240528 version:** 1.70-4.amzn2023.0.4
  - **AL2023.4.20240611 version:** 1.70-4.amzn2023.0.5

- ** `dmidecode` **
  - **RPM:**  dmidecode
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 3.5-1.amzn2023.0.2
  - **AL2023.4.20240611 version:** 3.6-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 1.82.4-1.amzn2023
  - **AL2023.4.20240611 version:** 1.83.0-1.amzn2023

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
  - **AL2023.4.20240528 version:** 9.56.1-7.amzn2023.0.6
  - **AL2023.4.20240611 version:** 9.56.1-7.amzn2023.0.7

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
  - **AL2023.4.20240528 version:** 6.1.91-99.172.amzn2023
  - **AL2023.4.20240611 version:** 6.1.92-99.174.amzn2023

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 15.0-2.amzn2023.0.1
  - **AL2023.4.20240611 version:** 15.7-1.amzn2023.0.1

- ** `nasm` **
  - **RPM:**  nasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nasm-doc  / **Architectures:** noarch
  - **RPM:**  nasm-rdoff  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 2.15.05-1.amzn2023.0.5
  - **AL2023.4.20240611 version:** 2.15.05-1.amzn2023.0.6

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 3.0.8-1.amzn2023.0.11
  - **AL2023.4.20240611 version:** 3.0.8-1.amzn2023.0.12

- ** `postgresql15` **
  - **RPM:**  postgresql15  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql15-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 15.6-1.amzn2023.0.1
  - **AL2023.4.20240611 version:** 15.7-1.amzn2023.0.1

- ** `R` **
  - **RPM:**  libRmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 4.3.2-1.amzn2023.0.1
  - **AL2023.4.20240611 version:** 4.3.2-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240528 version:** 2023.4.20240528-0.amzn2023
  - **AL2023.4.20240611 version:** 2023.4.20240611-1.amzn2023

- ** `unixODBC` **
  - **RPM:**  unixODBC  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unixODBC-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240528 version:** 2.3.9-3.amzn2023.0.2
  - **AL2023.4.20240611 version:** 2.3.9-3.amzn2023.0.3

## Docker container image
<a name="amis-2023.4.20240611.container-image"></a>
+ `amazon-linux-repo-cdn-2023.4.20240611-1.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.12`
+ `system-release-2023.4.20240611-1.amzn2023`

## Default AMI
<a name="amis-2023.4.20240611.default-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240611-1.amzn2023`
+ `aws-cfn-bootstrap-2.0-30.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240611-1.amzn2023`
+ `kernel-tools-6.1.92-99.174.amzn2023`
+ `kernel-6.1.92-99.174.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.12`
+ `openssl-1:3.0.8-1.amzn2023.0.12`
+ `system-release-2023.4.20240611-1.amzn2023`

## Minimal AMI
<a name="amis-2023.4.20240611.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.4.20240611-1.amzn2023`
+ `kernel-livepatch-repo-s3-2023.4.20240611-1.amzn2023`
+ `kernel-6.1.92-99.174.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.12`
+ `openssl-1:3.0.8-1.amzn2023.0.12`
+ `system-release-2023.4.20240611-1.amzn2023`

## Minimal container image
<a name="amis-2023.4.20240611.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240611-1.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.12`
+ `system-release-2023.4.20240611-1.amzn2023`
