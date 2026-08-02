---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231030.html
---

# Amazon Linux 2023 version 2023.2.20231030 release notes
<a name="relnotes-2023.2.20231030"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231030 release

## Major updates
<a name="major-updates-2023.2.20231030"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information about CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231030)
+ [Repository](#amis-2023.2.20231030.repository)
+ [Docker container image](#amis-2023.2.20231030.container-image)
+ [Default AMI](#amis-2023.2.20231030.default-ami)
+ [Minimal AMI](#amis-2023.2.20231030.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231030.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231030.repository"></a>

### New packages in AL2023.2.20231030 since AL2023.2.20231026
<a name="new-AL2023.2.20231026-AL2023.2.20231030"></a>

 Comparing AL2023.2.20231026 version 2023.2.20231026 to AL2023.2.20231030 version [2023.2.20231030](#relnotes-2023.2.20231030).

| Package Type | Number of new packages in AL2023.2.20231030 compared to AL2023.2.20231026 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 9 |
|  noarch binary RPMs | 3 |
|  x86\_64 binary RPMs | 3 |
|  aarch64 binary RPMs | 3 |

New packages in AL2023.2.20231030:

- ** `cloud-init` **
  - **RPM:**  cloud-init-cfg-ec2  / **Architectures:** noarch
  - **RPM:**  cloud-init-cfg-onprem  / **Architectures:** noarch
  - **Version:** 22.2.2-1.amzn2023.1.12

- ** `libisoburn` **
  - **RPM:**  libisoburn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libisoburn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libisoburn-doc  / **Architectures:** noarch
  - **RPM:**  xorriso  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.5.4-6.amzn2023.0.1

### AL2023.2.20231030 upgrades from AL2023.2.20231026
<a name="vercmp-AL2023.2.20231026-AL2023.2.20231030"></a>

 Comparing [2023.2.20231026](relnotes-2023.2.20231026.md) to [2023.2.20231030](#relnotes-2023.2.20231030).

| Package Type | Count |
| --- | --- |
| Source | 30 |
| Total Binary | 787 |
|  noarch binary RPMs | 144 |
|  x86\_64 binary RPMs | 323 |
|  aarch64 binary RPMs | 320 |

The full comparison of RPM package versions is below.

- ** [https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)
  - **Architectures:** noarch
  - **AL2023.2.20231026 version:** 2.4.0-1.amzn2023.0.1
  - **AL2023.2.20231030 version:** 2.4.1-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)  / **Architectures:** noarch
  - **AL2023.2.20231026 version:** 1.1-0.amzn2023
  - **AL2023.2.20231030 version:** 1.2-0.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 2.39-6.amzn2023.0.9
  - **AL2023.2.20231030 version:** 2.39-6.amzn2023.0.10

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2023.2.20231026 version:** 2023.2.60-1.0.amzn2023.0.3
  - **AL2023.2.20231030 version:** 2023.2.62-1.0.amzn2023.0.1

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2023.2.20231026 version:** 22.2.2-1.amzn2023.1.11
  - **AL2023.2.20231030 version:** 22.2.2-1.amzn2023.1.12

- ** `cni-plugins` **
  - **RPM:**  cni-plugins
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.2.0-1.amzn2023.0.2
  - **AL2023.2.20231030 version:** 1.2.0-1.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.77.0-1.amzn2023
  - **AL2023.2.20231030 version:** 1.78.1-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** v1.27.0.0-1.amzn2023
  - **AL2023.2.20231030 version:** v1.27.2.0-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html) **
  - **RPM:**  compat-libpthread-nonshared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-all-langpacks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-benchtests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-doc  / **Architectures:** noarch
  - **RPM:**  glibc-gconv-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-headers-x86  / **Architectures:** noarch
  - **RPM:**  glibc-langpack-aa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-af  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-agr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-am  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-an  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-anp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-as  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ast  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ayc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-az  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-be  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bhb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bho  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-br  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-brx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-byn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ca  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-chr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ckb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cmn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-crh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-csb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-da  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-de  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-doi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dsb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-dz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-el  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-en  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-eo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-es  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-et  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-eu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fil  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-fy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ga  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-gv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ha  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-he  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hif  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hne  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hsb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ht  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-hy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ia  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-id  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ik  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-is  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-it  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-iu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ja  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ka  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kab  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-km  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ko  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kok  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ku  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-kw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ky  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-li  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lij  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ln  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-lzh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mag  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mai  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mfe  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mhr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-miq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mjw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mni  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mnw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ms  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-my  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nds  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ne  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nhn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-niu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-nso  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-oc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-om  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-or  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-os  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-pt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-quz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-raj  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ro  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ru  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-rw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sah  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-se  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-shn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-shs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-si  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-so  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-st  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-szl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ta  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tcy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-te  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-th  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-the  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ti  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-to  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tpi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-tt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-uk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-unm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-uz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ve  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-vi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wae  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-wo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-xh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-yuw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-zh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-zu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-locale-source  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-minimal-langpack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nscd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_db  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_hesiod  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sysroot-aarch64-fc34-glibc  / **Architectures:** noarch
  - **RPM:**  sysroot-x86\_64-fc34-glibc  / **Architectures:** noarch
  - **AL2023.2.20231026 version:** 2.34-52.amzn2023.0.6
  - **AL2023.2.20231030 version:** 2.34-52.amzn2023.0.7

- ** `grub2` **
  - **RPM:**  grub2-common  / **Architectures:** noarch
  - **RPM:**  grub2-efi-aa64  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-cdboot  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-ec2  / **Architectures:** aarch64
  - **RPM:**  grub2-efi-aa64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-efi-x64  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-cdboot  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-ec2  / **Architectures:** x86\_64
  - **RPM:**  grub2-efi-x64-modules  / **Architectures:** noarch
  - **RPM:**  grub2-emu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-emu-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-pc  / **Architectures:** x86\_64
  - **RPM:**  grub2-pc-modules  / **Architectures:** noarch
  - **RPM:**  grub2-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-efi  / **Architectures:** x86\_64
  - **RPM:**  grub2-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grub2-tools-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 2.06-61.amzn2023.0.7
  - **AL2023.2.20231030 version:** 2.06-61.amzn2023.0.9

- ** `jackson-databind` **
  - **RPM:**  jackson-databind
  - **Architectures:** noarch
  - **AL2023.2.20231026 version:** 2.11.4-6.amzn2023.0.1
  - **AL2023.2.20231030 version:** 2.11.4-6.amzn2023.0.2

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
  - **AL2023.2.20231026 version:** 6.1.56-82.125.amzn2023
  - **AL2023.2.20231030 version:** 6.1.59-84.139.amzn2023

- ** `libvpx` **
  - **RPM:**  libvpx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvpx-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvpx-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.11.0-1.amzn2023.0.2
  - **AL2023.2.20231030 version:** 1.11.0-1.amzn2023.0.3

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 2.10.4-1.amzn2023.0.5
  - **AL2023.2.20231030 version:** 2.10.4-1.amzn2023.0.6

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 18.18.0-1.amzn2023.0.1
  - **AL2023.2.20231030 version:** 18.18.2-1.amzn2023.0.1

- ** `oci-add-hooks` **
  - **RPM:**  oci-add-hooks
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 0-0.1.20200504git268e3bb.amzn2023.0.1
  - **AL2023.2.20231030 version:** 0-0.1.20200504git268e3bb.amzn2023.0.2

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 0.23.0-3.amzn2023.0.1
  - **AL2023.2.20231030 version:** 0.23.0-3.amzn2023.0.2

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 3.0.8-1.amzn2023.0.8
  - **AL2023.2.20231030 version:** 3.0.8-1.amzn2023.0.9

- ** `open-vm-tools` **
  - **RPM:**  open-vm-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-salt-minion  / **Architectures:** x86\_64
  - **RPM:**  open-vm-tools-sdmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 12.3.0-1.amzn2023
  - **AL2023.2.20231030 version:** 12.3.0-1.amzn2023.0.1

- ** `plexus-archiver` **
  - **RPM:**  plexus-archiver  / **Architectures:** noarch
  - **RPM:**  plexus-archiver-javadoc  / **Architectures:** noarch
  - **AL2023.2.20231026 version:** 4.2.4-5.amzn2023.0.3
  - **AL2023.2.20231030 version:** 4.2.7-4.amzn2023.0.1

- ** `realmd` **
  - **RPM:**  realmd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  realmd-devel-docs  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 0.17.0-9.amzn2023.0.3
  - **AL2023.2.20231030 version:** 0.17.0-9.amzn2023.0.4

- ** `samba` **
  - **RPM:**  libnetapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetapi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-dc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-samba-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common  / **Architectures:** noarch
  - **RPM:**  samba-common-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-dcerpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-dc-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-krb5-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-ldb-ldap-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-pidl  / **Architectures:** noarch
  - **RPM:**  samba-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-test-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-usershares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-vfs-iouring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-krb5-locator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-modules  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 4.17.10-0.amzn2023.0.1
  - **AL2023.2.20231030 version:** 4.17.12-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231026 version:** 2023.2.20231026-0.amzn2023
  - **AL2023.2.20231030 version:** 2023.2.20231030-1.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.2.20231026 version:** 9.0.71-1.amzn2023.0.6
  - **AL2023.2.20231030 version:** 9.0.82-1.amzn2023.0.1

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 9.0.1882-1.amzn2023.0.2
  - **AL2023.2.20231030 version:** 9.0.2010-1.amzn2023

- ** `vorbis-tools` **
  - **RPM:**  vorbis-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.4.2-2.amzn2023.0.2
  - **AL2023.2.20231030 version:** 1.4.2-2.amzn2023.0.3

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 4.0.8-2.amzn2023.0.1
  - **AL2023.2.20231030 version:** 4.0.8-2.amzn2023.0.2

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.20.14-18.amzn2023.0.1
  - **AL2023.2.20231030 version:** 1.20.14-26.amzn2023.0.1

- ** `zlib` **
  - **RPM:**  minizip-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  minizip-compat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zlib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zlib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zlib-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.2.11-33.amzn2023.0.4
  - **AL2023.2.20231030 version:** 1.2.11-33.amzn2023.0.5

- ** `zstd` **
  - **RPM:**  libzstd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zstd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231026 version:** 1.5.2-1.amzn2023.0.3
  - **AL2023.2.20231030 version:** 1.5.5-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.2.20231030.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231030-1.amzn2023`
+ `ca-certificates-2023.2.62-1.0.amzn2023.0.1`
+ `glibc-2.34-52.amzn2023.0.7`
+ `glibc-common-2.34-52.amzn2023.0.7`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.7`
+ `libxml2-2.10.4-1.amzn2023.0.6`
+ `libzstd-1.5.5-1.amzn2023.0.1`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.9`
+ `system-release-2023.2.20231030-1.amzn2023`
+ `zlib-1.2.11-33.amzn2023.0.5`

## Default AMI
<a name="amis-2023.2.20231030.default-ami"></a>

|  |
| --- |
| `amazon-ec2-net-utils-2.4.1-1.amzn2023.0.1` |
| `amazon-linux-repo-s3-2023.2.20231030-1.amzn2023` |
| `binutils-2.39-6.amzn2023.0.10` |
| `ca-certificates-2023.2.62-1.0.amzn2023.0.1` |
| `cloud-init-22.2.2-1.amzn2023.1.12` |
| `cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.12` |
| `glibc-2.34-52.amzn2023.0.7` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.7` |
| `glibc-common-2.34-52.amzn2023.0.7` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.7` |
| `glibc-locale-source-2.34-52.amzn2023.0.7` |
| `grub2-common-1:2.06-61.amzn2023.0.9` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.9` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.9` |
| `grub2-tools-1:2.06-61.amzn2023.0.9` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.9` |
| `kernel-6.1.59-84.139.amzn2023` |
| `kernel-livepatch-repo-s3-2023.2.20231030-1.amzn2023` |
| `kernel-tools-6.1.59-84.139.amzn2023` |
| `libxml2-2.10.4-1.amzn2023.0.6` |
| `libzstd-1.5.5-1.amzn2023.0.1` |
| `openssl-1:3.0.8-1.amzn2023.0.9` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.9` |
| `system-release-2023.2.20231030-1.amzn2023` |
| `vim-common-2:9.0.2010-1.amzn2023` |
| `vim-data-2:9.0.2010-1.amzn2023` |
| `vim-enhanced-2:9.0.2010-1.amzn2023` |
| `vim-filesystem-2:9.0.2010-1.amzn2023` |
| `vim-minimal-2:9.0.2010-1.amzn2023` |
| `xxd-2:9.0.2010-1.amzn2023` |
| `zlib-1.2.11-33.amzn2023.0.5` |
| `zstd-1.5.5-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023.2.20231030.minimal-ami"></a>

|  |
| --- |
| `amazon-ec2-net-utils-2.4.1-1.amzn2023.0.1` |
| `amazon-linux-repo-s3-2023.2.20231030-1.amzn2023` |
| `ca-certificates-2023.2.62-1.0.amzn2023.0.1` |
| `cloud-init-22.2.2-1.amzn2023.1.12` |
| `cloud-init-cfg-ec2-22.2.2-1.amzn2023.1.12` |
| `glibc-2.34-52.amzn2023.0.7` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.7` |
| `glibc-common-2.34-52.amzn2023.0.7` |
| `glibc-locale-source-2.34-52.amzn2023.0.7` |
| `grub2-common-1:2.06-61.amzn2023.0.9` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.9` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.9` |
| `grub2-tools-1:2.06-61.amzn2023.0.9` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.9` |
| `kernel-6.1.59-84.139.amzn2023` |
| `kernel-livepatch-repo-s3-2023.2.20231030-1.amzn2023` |
| `libxml2-2.10.4-1.amzn2023.0.6` |
| `libzstd-1.5.5-1.amzn2023.0.1` |
| `openssl-1:3.0.8-1.amzn2023.0.9` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.9` |
| `system-release-2023.2.20231030-1.amzn2023` |
| `vim-data-2:9.0.2010-1.amzn2023` |
| `vim-minimal-2:9.0.2010-1.amzn2023` |
| `zlib-1.2.11-33.amzn2023.0.5` |
| `zstd-1.5.5-1.amzn2023.0.1` |

## Minimal container image
<a name="amis-2023.2.20231030.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231030-1.amzn2023`
+ `ca-certificates-2023.2.62-1.0.amzn2023.0.1`
+ `glibc-2.34-52.amzn2023.0.7`
+ `glibc-common-2.34-52.amzn2023.0.7`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.7`
+ `libxml2-2.10.4-1.amzn2023.0.6`
+ `libzstd-1.5.5-1.amzn2023.0.1`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.9`
+ `system-release-2023.2.20231030-1.amzn2023`
+ `zlib-1.2.11-33.amzn2023.0.5`
