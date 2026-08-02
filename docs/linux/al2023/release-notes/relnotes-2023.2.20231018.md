---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231018.html
---

# Amazon Linux 2023 version 2023.2.20231018 release notes
<a name="relnotes-2023.2.20231018"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231018 release

## Major updates
<a name="major-updates-2023.2.20231018"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ This release contains the Amazon Corretto Q4 release. For more information, see the following:
  + [Change log for Amazon Corretto 8](https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md)
  + [Change log for Amazon Corretto 11](https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md)
  + [Change log for Amazon Corretto 17](https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md)
  + [Change log for Amazon Corretto 21](https://github.com/corretto/corretto-21/blob/develop/CHANGELOG.md)
+ The kernel package now provides a number of modules that aren't usually needed on Amazon EC2 as an optional `kerne-modules-extra` package. This package includes the EFI Framebuffer for Amazon EC2 instances built on the Nitro System along with other modules.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231018)
+ [Repository](#amis-2023.2.20231018.repository)
+ [Docker container image](#amis-2023.2.20231018.container-image)
+ [Default AMI](#amis-2023.2.20231018.default-ami)
+ [Minimal AMI](#amis-2023.2.20231018.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231018.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231018.repository"></a>

### New packages in AL2023.2.20231018 since AL2023.2.20231016
<a name="new-AL2023.2.20231016-AL2023.2.20231018"></a>

 Comparing AL2023.2.20231016 version 2023.2.20231016 to AL2023.2.20231018 version [2023.2.20231018](#relnotes-2023.2.20231018).

| Package Type | Number of new packages in AL2023.2.20231018 compared to AL2023.2.20231016 |
| --- | --- |
| Source RPMs | 0 |
| Total Binary RPMs | 4 |
|  x86\_64 binary RPMs | 2 |
|  aarch64 binary RPMs | 2 |

New packages in AL2023.2.20231018:

- ** `kernel` **
  - **RPM:**  kernel-modules-extra
  - **Architectures:** aarch64, x86\_64
  - **Version:** 6.1.56-82.125.amzn2023

- ** `openssl` **
  - **RPM:**  openssl-snapsafe-libs
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.0.8-1.amzn2023.0.8

### AL2023.2.20231018 upgrades from AL2023.2.20231016
<a name="vercmp-AL2023.2.20231016-AL2023.2.20231018"></a>

 Comparing [2023.2.20231016](relnotes-2023.2.20231016.md) to [2023.2.20231018](#relnotes-2023.2.20231018).

| Package Type | Count |
| --- | --- |
| Source | 22 |
| Total Binary | 222 |
|  noarch binary RPMs | 76 |
|  x86\_64 binary RPMs | 73 |
|  aarch64 binary RPMs | 73 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 3.2.1630.0-1.amzn2023
  - **AL2023.2.20231018 version:** 3.2.1705.0-1.amzn2023

- ** `composer` **
  - **RPM:**  composer
  - **Architectures:** noarch
  - **AL2023.2.20231016 version:** 2.5.8-2.amzn2023
  - **AL2023.2.20231018 version:** 2.5.8-2.amzn2023.0.1

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 1.7.2-1.amzn2023.0.3
  - **AL2023.2.20231018 version:** 1.7.2-1.amzn2023.0.4

- ** `container-selinux` **
  - **RPM:**  container-selinux
  - **Architectures:** noarch
  - **AL2023.2.20231016 version:** 2.189.0-289.amzn2023.0.2
  - **AL2023.2.20231018 version:** 2.222.0-325.amzn2023

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 24.0.5-1.amzn2023.0.1
  - **AL2023.2.20231018 version:** 24.0.5-1.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 1.76.0-1.amzn2023
  - **AL2023.2.20231018 version:** 1.77.0-1.amzn2023

- ** `giflib` **
  - **RPM:**  giflib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  giflib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  giflib-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 5.2.1-9.amzn2023
  - **AL2023.2.20231018 version:** 5.2.1-9.amzn2023.0.1

- ** `haproxy` **
  - **RPM:**  haproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 2.8.0-1.amzn2023.0.2
  - **AL2023.2.20231018 version:** 2.8.3-1.amzn2023

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 6.9.12.82-1.amzn2023.0.6
  - **AL2023.2.20231018 version:** 6.9.12.82-1.amzn2023.0.7

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 1.8.0\_382.b05-1.amzn2023
  - **AL2023.2.20231018 version:** 1.8.0\_392.b08-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 11.0.20\+9-1.amzn2023
  - **AL2023.2.20231018 version:** 11.0.21\+9-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 17.0.8\+8-1.amzn2023.1
  - **AL2023.2.20231018 version:** 17.0.9\+8-1.amzn2023.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 21.0.0\+35-1.amzn2023.1
  - **AL2023.2.20231018 version:** 21.0.1\+12-1.amzn2023.1

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 6.1.55-75.123.amzn2023
  - **AL2023.2.20231018 version:** 6.1.56-82.125.amzn2023

- ** `libX11` **
  - **RPM:**  libX11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-common  / **Architectures:** noarch
  - **RPM:**  libX11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-xcb  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 1.7.2-3.amzn2023.0.3
  - **AL2023.2.20231018 version:** 1.7.2-3.amzn2023.0.4

- ** `libXpm` **
  - **RPM:**  libXpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXpm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 3.5.15-2.amzn2023.0.1
  - **AL2023.2.20231018 version:** 3.5.15-2.amzn2023.0.3

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 3.0.8-1.amzn2023.0.7
  - **AL2023.2.20231018 version:** 3.0.8-1.amzn2023.0.8

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
  - **AL2023.2.20231016 version:** 15.0-1.amzn2023.0.4
  - **AL2023.2.20231018 version:** 15.4-1.amzn2023.0.1

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 1.1.7-1.amzn2023.0.2
  - **AL2023.2.20231018 version:** 1.1.7-1.amzn2023.0.3

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.2.20231016 version:** 36.18-1.amzn2023.0.1
  - **AL2023.2.20231018 version:** 37.22-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231016 version:** 2023.2.20231016-0.amzn2023
  - **AL2023.2.20231018 version:** 2023.2.20231018-0.amzn2023

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231016 version:** 9.0.1882-1.amzn2023.0.1
  - **AL2023.2.20231018 version:** 9.0.1882-1.amzn2023.0.2

## Docker container image
<a name="amis-2023.2.20231018.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231018-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.8`
+ `system-release-2023.2.20231018-0.amzn2023`

## Default AMI
<a name="amis-2023.2.20231018.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.2.20231018-0.amzn2023` |
| `amazon-ssm-agent-3.2.1705.0-1.amzn2023` |
| `kernel-6.1.56-82.125.amzn2023` |
| `kernel-livepatch-repo-s3-2023.2.20231018-0.amzn2023` |
| `kernel-tools-6.1.56-82.125.amzn2023` |
| `openssl-1:3.0.8-1.amzn2023.0.8` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.8` |
| `selinux-policy-37.22-1.amzn2023.0.1` |
| `selinux-policy-targeted-37.22-1.amzn2023.0.1` |
| `system-release-2023.2.20231018-0.amzn2023` |
| `vim-common-2:9.0.1882-1.amzn2023.0.2` |
| `vim-data-2:9.0.1882-1.amzn2023.0.2` |
| `vim-enhanced-2:9.0.1882-1.amzn2023.0.2` |
| `vim-filesystem-2:9.0.1882-1.amzn2023.0.2` |
| `vim-minimal-2:9.0.1882-1.amzn2023.0.2` |
| `xxd-2:9.0.1882-1.amzn2023.0.2` |

## Minimal AMI
<a name="amis-2023.2.20231018.minimal-ami"></a>
+ `amazon-linux-repo-s3-2023.2.20231018-0.amzn2023`
+ `kernel-6.1.56-82.125.amzn2023`
+ `kernel-livepatch-repo-s3-2023.2.20231018-0.amzn2023`
+ `openssl-1:3.0.8-1.amzn2023.0.8`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.8`
+ `selinux-policy-37.22-1.amzn2023.0.1`
+ `selinux-policy-targeted-37.22-1.amzn2023.0.1`
+ `system-release-2023.2.20231018-0.amzn2023`
+ `vim-data-2:9.0.1882-1.amzn2023.0.2`
+ `vim-minimal-2:9.0.1882-1.amzn2023.0.2`

## Minimal container image
<a name="amis-2023.2.20231018.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231018-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.8`
+ `system-release-2023.2.20231018-0.amzn2023`
