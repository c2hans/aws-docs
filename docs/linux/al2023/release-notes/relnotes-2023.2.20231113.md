---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231113.html
---

# Amazon Linux 2023 version 2023.2.20231113 release notes
<a name="relnotes-2023.2.20231113"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231113 release

## Major updates
<a name="major-updates-2023.2.20231113"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ AL2023 virtual machine images are available for KVM and VMware environments. For more information, see [Using AL2023 outside of Amazon EC2](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html).

**Security Updates**
+ For information about the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231113)
+ [Repository](#amis-2023.2.20231113.repository)
+ [Docker container image](#amis-2023.2.20231113.container-image)
+ [Default AMI](#amis-2023.2.20231113.default-ami)
+ [Minimal AMI](#amis-2023.2.20231113.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231113.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231113.repository"></a>

### AL2023.2.20231113 upgrades from AL2023.2.20231030
<a name="vercmp-AL2023.2.20231030-AL2023.2.20231113"></a>

 Comparing [2023.2.20231030](relnotes-2023.2.20231030.md) to [2023.2.20231113](#relnotes-2023.2.20231113).

| Package Type | Count |
| --- | --- |
| Source | 15 |
| Total Binary | 145 |
|  noarch binary RPMs | 56 |
|  x86\_64 binary RPMs | 45 |
|  aarch64 binary RPMs | 44 |

The full comparison of RPM package versions is below.

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 1.2.0-1.amzn2023.0.1
  - **AL2023.2.20231113 version:** 1.3.0-0.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 1.78.1-1.amzn2023
  - **AL2023.2.20231113 version:** 1.79.0-1.amzn2023

- ** `gperftools` **
  - **RPM:**  gperftools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gperftools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gperftools-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pprof  / **Architectures:** noarch
  - **AL2023.2.20231030 version:** 2.9.1-1.amzn2023.0.2
  - **AL2023.2.20231113 version:** 2.9.1-1.amzn2023.0.3

- ** `httpd` **
  - **RPM:**  httpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-filesystem  / **Architectures:** noarch
  - **RPM:**  httpd-manual  / **Architectures:** noarch
  - **RPM:**  httpd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_proxy\_html  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ssl  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 2.4.56-1.amzn2023
  - **AL2023.2.20231113 version:** 2.4.58-1.amzn2023

- ** `iputils` **
  - **RPM:**  iputils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iputils-ninfod  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 20210202-2.amzn2023.0.3
  - **AL2023.2.20231113 version:** 20210202-2.amzn2023.0.4

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 21.0.1\+12-1.amzn2023.1
  - **AL2023.2.20231113 version:** 21.0.1\+12-1.amzn2023.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 6.1.59-84.139.amzn2023
  - **AL2023.2.20231113 version:** 6.1.61-85.141.amzn2023

- ** `kpatch` **
  - **RPM:**  kpatch-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-dnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-runtime  / **Architectures:** noarch
  - **AL2023.2.20231030 version:** 0.9.7-12.amzn2023.0.3
  - **AL2023.2.20231113 version:** 0.9.7-13.amzn2023.0.1

- ** `librsvg2` **
  - **RPM:**  librsvg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 2.50.7-1.amzn2023.0.3
  - **AL2023.2.20231113 version:** 2.54.6-1.amzn2023.0.1

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.2.20231030 version:** 2.1-53.amzn2023.0.2
  - **AL2023.2.20231113 version:** 2.1-53.amzn2023.0.3

- ** `python-twisted` **
  - **RPM:**  python3-twisted  / **Architectures:** noarch
  - **RPM:**  python3-twisted\+tls  / **Architectures:** noarch
  - **AL2023.2.20231030 version:** 22.4.0-125.amzn2023.0.2
  - **AL2023.2.20231113 version:** 22.4.0-126.amzn2023.0.3

- ** `re2c` **
  - **RPM:**  re2c
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 2.1.1-1.amzn2023.0.2
  - **AL2023.2.20231113 version:** 3.1-1.amzn2023.0.1

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 5.8-1.amzn2023.0.1
  - **AL2023.2.20231113 version:** 5.8-1.amzn2023.0.2

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231030 version:** 2023.2.20231030-1.amzn2023
  - **AL2023.2.20231113 version:** 2023.2.20231113-1.amzn2023

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231030 version:** 9.0.2010-1.amzn2023
  - **AL2023.2.20231113 version:** 9.0.2081-1.amzn2023

## Docker container image
<a name="amis-2023.2.20231113.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231113-1.amzn2023`
+ `system-release-2023.2.20231113-1.amzn2023`

## Default AMI
<a name="amis-2023.2.20231113.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.2.20231113-1.amzn2023` |
| `iputils-20210202-2.amzn2023.0.4` |
| `kernel-6.1.61-85.141.amzn2023` |
| `kernel-livepatch-repo-s3-2023.2.20231113-1.amzn2023` |
| `kernel-tools-6.1.61-85.141.amzn2023` |
| `kpatch-runtime-0.9.7-13.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.3` |
| `system-release-2023.2.20231113-1.amzn2023` |
| `vim-common-2:9.0.2081-1.amzn2023` |
| `vim-data-2:9.0.2081-1.amzn2023` |
| `vim-enhanced-2:9.0.2081-1.amzn2023` |
| `vim-filesystem-2:9.0.2081-1.amzn2023` |
| `vim-minimal-2:9.0.2081-1.amzn2023` |
| `xxd-2:9.0.2081-1.amzn2023` |

## Minimal AMI
<a name="amis-2023.2.20231113.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231113-1.amzn2023`
+ `iputils-20210202-2.amzn2023.0.4`
+ `kernel-6.1.61-85.141.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231113-1.amzn2023`
+ `system-release-2023.2.20231113-1.amzn2023`
+ `vim-data-2:9.0.2081-1.amzn2023`
+ `vim-minimal-2:9.0.2081-1.amzn2023`

## Minimal container image
<a name="amis-2023.2.20231113.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231113-1.amzn2023`
+ `system-release-2023.2.20231113-1.amzn2023`
