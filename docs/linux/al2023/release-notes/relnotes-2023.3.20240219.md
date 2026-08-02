---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240219.html
---

# Amazon Linux 2023 version 2023.3.20240219 release notes
<a name="relnotes-2023.3.20240219"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240219 release

## Major updates
<a name="major-updates2023.3.20240219"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates2023.3.20240219)
+ [Repository](#amis-2023.3.20240219.repository)
+ [Docker container image](#amis-2023.3.20240219.container-image)
+ [Default AMI](#amis-2023.3.20240219.default-ami)
+ [Minimal AMI](#amis-2023.3.20240219.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240219.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240219.repository"></a>

### AL2023.3.20240219 upgrades from AL2023.3.20240205
<a name="vercmp-AL2023.3.20240205-AL2023.3.20240219"></a>

 Comparing [2023.3.20240205](relnotes-2023.3.20240205.md) to [2023.3.20240219](#relnotes-2023.3.20240219).

| Package Type | Count |
| --- | --- |
| Source | 21 |
| Total Binary | 227 |
|  noarch binary RPMs | 72 |
|  x86\_64 binary RPMs | 78 |
|  aarch64 binary RPMs | 77 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 3.2.1705.0-1.amzn2023
  - **AL2023.3.20240219 version:** 3.2.2222.0-1.amzn2023

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2023.3.20240205 version:** 2.0-23.amzn2023
  - **AL2023.3.20240219 version:** 2.0-29.amzn2023

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 1.2.2-0.amzn2023
  - **AL2023.3.20240219 version:** 1.2.3-0.amzn2023

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2023.3.20240205 version:** 2023.2.62-1.0.amzn2023.0.1
  - **AL2023.3.20240219 version:** 2023.2.64-1.0.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 1.80.0-1.amzn2023
  - **AL2023.3.20240219 version:** 1.81.0-1.amzn2023

- ** `expat` **
  - **RPM:**  expat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 2.5.0-1.amzn2023.0.2
  - **AL2023.3.20240219 version:** 2.5.0-1.amzn2023.0.3

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 3.8.0-377.amzn2023.0.3
  - **AL2023.3.20240219 version:** 3.8.0-378.amzn2023.0.4

- ** `graphviz` **
  - **RPM:**  graphviz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-graphs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-ocaml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-tcl  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 2.44.0-25.amzn2023.0.6
  - **AL2023.3.20240219 version:** 2.44.0-25.amzn2023.0.7

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 17.0.10\+7-1.amzn2023.1
  - **AL2023.3.20240219 version:** 17.0.10\+8-1.amzn2023.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 21.0.2\+13-1.amzn2023.1
  - **AL2023.3.20240219 version:** 21.0.2\+14-1.amzn2023.1

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
  - **AL2023.3.20240205 version:** 6.1.75-99.163.amzn2023
  - **AL2023.3.20240219 version:** 6.1.77-99.164.amzn2023

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 4.4.0-4.amzn2023.0.17
  - **AL2023.3.20240219 version:** 4.4.0-4.amzn2023.0.18

- ** `mailx` **
  - **RPM:**  mailx
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 12.5-37.amzn2023.0.4
  - **AL2023.3.20240219 version:** 12.5-43.amzn2023.0.1

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.3.20240205 version:** 2.1-53.amzn2023.0.3
  - **AL2023.3.20240219 version:** 2.1-53.amzn2023.0.5

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 1.1.0-1.amzn2023.0.4
  - **AL2023.3.20240219 version:** 1.7.2-1.amzn2023.0.1

- ** `nss` **
  - **RPM:**  nspr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nspr-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-sysinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 4.35.0-5.amzn2023.0.5
  - **AL2023.3.20240219 version:** 4.35.0-6.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 3.0.8-1.amzn2023.0.10
  - **AL2023.3.20240219 version:** 3.0.8-1.amzn2023.0.11

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240205 version:** 2023.3.20240205-0.amzn2023
  - **AL2023.3.20240219 version:** 2023.3.20240219-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.3.20240205 version:** 9.0.82-1.amzn2023.0.2
  - **AL2023.3.20240219 version:** 9.0.83-1.amzn2023.0.1

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2023.3.20240205 version:** 2023d-1.amzn2023.0.1
  - **AL2023.3.20240219 version:** 2024a-1.amzn2023.0.1

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240205 version:** 1.20.14-26.amzn2023.0.2
  - **AL2023.3.20240219 version:** 1.20.14-30.amzn2023.0.1

## Docker container image
<a name="amis-2023.3.20240219.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240219-0.amzn2023`
+ `ca-certificates-2023.2.64-1.0.amzn2023.0.1`
+ `expat-2.5.0-1.amzn2023.0.3`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.11`
+ `system-release-2023.3.20240219-0.amzn2023`
+ `tzdata-2024a-1.amzn2023.0.1`

## Default AMI
<a name="amis-2023.3.20240219.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240219-0.amzn2023` |
| `amazon-ssm-agent-3.2.2222.0-1.amzn2023` |
| `aws-cfn-bootstrap-2.0-29.amzn2023` |
| `ca-certificates-2023.2.64-1.0.amzn2023.0.1` |
| `expat-2.5.0-1.amzn2023.0.3` |
| `gnutls-3.8.0-378.amzn2023.0.4` |
| `kernel-livepatch-repo-s3-2023.3.20240219-0.amzn2023` |
| `kernel-tools-6.1.77-99.164.amzn2023` |
| `kernel-6.1.77-99.164.amzn2023` |
| `microcode_ctl-2:2.1-53.amzn2023.0.5` |
| `nspr-4.35.0-6.amzn2023.0.1` |
| `nss-softokn-freebl-3.90.0-6.amzn2023.0.1` |
| `nss-softokn-3.90.0-6.amzn2023.0.1` |
| `nss-sysinit-3.90.0-6.amzn2023.0.1` |
| `nss-util-3.90.0-6.amzn2023.0.1` |
| `nss-3.90.0-6.amzn2023.0.1` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.11` |
| `openssl-1:3.0.8-1.amzn2023.0.11` |
| `system-release-2023.3.20240219-0.amzn2023` |
| `tzdata-2024a-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023.3.20240219.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240219-0.amzn2023` |
| `ca-certificates-2023.2.64-1.0.amzn2023.0.1` |
| `expat-2.5.0-1.amzn2023.0.3` |
| `gnutls-3.8.0-378.amzn2023.0.4` |
| `kernel-livepatch-repo-s3-2023.3.20240219-0.amzn2023` |
| `kernel-6.1.77-99.164.amzn2023` |
| `microcode_ctl-2:2.1-53.amzn2023.0.5` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.11` |
| `openssl-1:3.0.8-1.amzn2023.0.11` |
| `system-release-2023.3.20240219-0.amzn2023` |
| `tzdata-2024a-1.amzn2023.0.1` |

## Minimal container image
<a name="amis-2023.3.20240219.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240219-0.amzn2023`
+ `ca-certificates-2023.2.64-1.0.amzn2023.0.1`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.11`
+ `system-release-2023.3.20240219-0.amzn2023`
