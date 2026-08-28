---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240401.html
---

# Amazon Linux 2023 version 2023.4.20240401 release notes
<a name="relnotes-2023.4.20240401"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.4.20240401 release

## Major updates
<a name="major-updates-2023.4.20240401"></a>

This release represents an update to the fourth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.4.20240401)
+ [Repository](#amis-2023.4.20240401.repository)
+ [Docker container image](#amis-2023.4.20240401.container-image)
+ [Default AMI](#amis-2023.4.20240401.default-ami)
+ [Minimal AMI](#amis-2023.4.20240401.minimal-ami)
+ [Minimal container image](#amis-2023.4.20240401.minimal-container-ami)

## Repository
<a name="amis-2023.4.20240401.repository"></a>

### New packages in AL2023.4.20240401 since AL2023.4.20240319
<a name="new-AL2023.4.20240319-AL2023.4.20240401"></a>

 Comparing AL2023.4.20240319 version 2023.4.20240319 to AL2023.4.20240401 version [2023.4.20240401](#relnotes-2023.4.20240401).

| Package Type | Number of new packages in AL2023.4.20240401 compared to AL2023.4.20240319 |
| --- | --- |
| Source RPMs | 3 |
| Total Binary RPMs | 18 |
|  x86\_64 binary RPMs | 9 |
|  aarch64 binary RPMs | 9 |

New packages in AL2023.4.20240401:

- ** [`java-22-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-22-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **Version:** 22.0.0\+37-1.amzn2023.1

- ** `libecpg` **
  - **RPM:**  libecpg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libecpg-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpgtypes  / **Architectures:** aarch64, x86\_64
  - **Version:** 16.1-2.amzn2023

- ** `spamassassin` **
  - **RPM:**  spamassassin
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.0.0-6.amzn2023.0.1

### AL2023.4.20240401 upgrades from AL2023.4.20240319
<a name="vercmp-AL2023.4.20240319-AL2023.4.20240401"></a>

 Comparing [2023.4.20240319](relnotes-2023.4.20240319.md) to [2023.4.20240401](#relnotes-2023.4.20240401).

| Package Type | Count |
| --- | --- |
| Source | 13 |
| Total Binary | 622 |
|  noarch binary RPMs | 84 |
|  x86\_64 binary RPMs | 270 |
|  aarch64 binary RPMs | 268 |

The full comparison of RPM package versions is below.

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 8.5.0-1.amzn2023.0.2
  - **AL2023.4.20240401 version:** 8.5.0-1.amzn2023.0.3

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 1.82.0-1.amzn2023
  - **AL2023.4.20240401 version:** 1.82.1-1.amzn2023

- ** `expat` **
  - **RPM:**  expat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 2.5.0-1.amzn2023.0.3
  - **AL2023.4.20240401 version:** 2.5.0-1.amzn2023.0.4

- ** [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html) **
  - **RPM:**  compat-libpthread-nonshared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  / **Architectures:** aarch64, x86\_64
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
  - **AL2023.4.20240319 version:** 2.34-52.amzn2023.0.8
  - **AL2023.4.20240401 version:** 2.34-52.amzn2023.0.9

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
  - **AL2023.4.20240319 version:** 2.06-61.amzn2023.0.11
  - **AL2023.4.20240401 version:** 2.06-61.amzn2023.0.12

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
  - **AL2023.4.20240319 version:** 6.1.79-99.167.amzn2023
  - **AL2023.4.20240401 version:** 6.1.82-99.168.amzn2023

- ** `libdwarf` **
  - **RPM:**  libdwarf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 0.5.0-1.amzn2023.0.2
  - **AL2023.4.20240401 version:** 0.5.0-1.amzn2023.0.3

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 0.23.0-3.amzn2023.0.2
  - **AL2023.4.20240401 version:** 0.24.0-1.amzn2023.0.3

- ** `python-pillow` **
  - **RPM:**  python3-pillow  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-tk  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 9.4.0-2.amzn2023.0.4
  - **AL2023.4.20240401 version:** 9.4.0-2.amzn2023.0.5

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 5.8-1.amzn2023.0.4
  - **AL2023.4.20240401 version:** 6.6-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240319 version:** 2023.4.20240319-1.amzn2023
  - **AL2023.4.20240401 version:** 2023.4.20240401-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.4.20240319 version:** 9.0.83-1.amzn2023.0.1
  - **AL2023.4.20240401 version:** 9.0.87-1.amzn2023.0.2

- ** `util-linux` **
  - **RPM:**  libblkid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblkid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfdisk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfdisk-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmount  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmount-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmartcols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmartcols-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuuid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuuid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libmount  / **Architectures:** aarch64, x86\_64
  - **RPM:**  util-linux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  util-linux-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  util-linux-user  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuidd  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240319 version:** 2.37.4-1.amzn2023.0.3
  - **AL2023.4.20240401 version:** 2.37.4-1.amzn2023.0.4

## Docker container image
<a name="amis-2023.4.20240401.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.4.20240401-0.amzn2023` |
| `curl-minimal-8.5.0-1.amzn2023.0.3` |
| `expat-2.5.0-1.amzn2023.0.4` |
| `glibc-common-2.34-52.amzn2023.0.9` |
| `glibc-minimal-langpack-2.34-52.amzn2023.0.9` |
| `glibc-2.34-52.amzn2023.0.9` |
| `libblkid-2.37.4-1.amzn2023.0.4` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.3` |
| `libmount-2.37.4-1.amzn2023.0.4` |
| `libsmartcols-2.37.4-1.amzn2023.0.4` |
| `libuuid-2.37.4-1.amzn2023.0.4` |
| `system-release-2023.4.20240401-0.amzn2023` |

## Default AMI
<a name="amis-2023.4.20240401.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.4.20240401-0.amzn2023` |
| `curl-minimal-8.5.0-1.amzn2023.0.3` |
| `expat-2.5.0-1.amzn2023.0.4` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.9` |
| `glibc-common-2.34-52.amzn2023.0.9` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.9` |
| `glibc-locale-source-2.34-52.amzn2023.0.9` |
| `glibc-2.34-52.amzn2023.0.9` |
| `grub2-common-1:2.06-61.amzn2023.0.12` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.12` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.12` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.12` |
| `grub2-tools-1:2.06-61.amzn2023.0.12` |
| `kernel-livepatch-repo-s3-2023.4.20240401-0.amzn2023` |
| `kernel-tools-6.1.82-99.168.amzn2023` |
| `kernel-6.1.82-99.168.amzn2023` |
| `libblkid-2.37.4-1.amzn2023.0.4` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.3` |
| `libfdisk-2.37.4-1.amzn2023.0.4` |
| `libmount-2.37.4-1.amzn2023.0.4` |
| `libsmartcols-2.37.4-1.amzn2023.0.4` |
| `libuuid-2.37.4-1.amzn2023.0.4` |
| `system-release-2023.4.20240401-0.amzn2023` |
| `util-linux-core-2.37.4-1.amzn2023.0.4` |
| `util-linux-2.37.4-1.amzn2023.0.4` |

## Minimal AMI
<a name="amis-2023.4.20240401.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.4.20240401-0.amzn2023` |
| `curl-minimal-8.5.0-1.amzn2023.0.3` |
| `expat-2.5.0-1.amzn2023.0.4` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.9` |
| `glibc-common-2.34-52.amzn2023.0.9` |
| `glibc-locale-source-2.34-52.amzn2023.0.9` |
| `glibc-2.34-52.amzn2023.0.9` |
| `grub2-common-1:2.06-61.amzn2023.0.12` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.12` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.12` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.12` |
| `grub2-tools-1:2.06-61.amzn2023.0.12` |
| `kernel-livepatch-repo-s3-2023.4.20240401-0.amzn2023` |
| `kernel-6.1.82-99.168.amzn2023` |
| `libblkid-2.37.4-1.amzn2023.0.4` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.3` |
| `libfdisk-2.37.4-1.amzn2023.0.4` |
| `libmount-2.37.4-1.amzn2023.0.4` |
| `libsmartcols-2.37.4-1.amzn2023.0.4` |
| `libuuid-2.37.4-1.amzn2023.0.4` |
| `system-release-2023.4.20240401-0.amzn2023` |
| `util-linux-core-2.37.4-1.amzn2023.0.4` |
| `util-linux-2.37.4-1.amzn2023.0.4` |

## Minimal container image
<a name="amis-2023.4.20240401.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.4.20240401-0.amzn2023`
+ `curl-minimal-8.5.0-1.amzn2023.0.3`
+ `glibc-common-2.34-52.amzn2023.0.9`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.9`
+ `glibc-2.34-52.amzn2023.0.9`
+ `libblkid-2.37.4-1.amzn2023.0.4`
+ `libcurl-minimal-8.5.0-1.amzn2023.0.3`
+ `libmount-2.37.4-1.amzn2023.0.4`
+ `libsmartcols-2.37.4-1.amzn2023.0.4`
+ `libuuid-2.37.4-1.amzn2023.0.4`
+ `system-release-2023.4.20240401-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
