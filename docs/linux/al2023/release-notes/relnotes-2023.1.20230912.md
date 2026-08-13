---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230912.html
---

# Amazon Linux 2023 version 2023.1.20230912 release notes
<a name="relnotes-2023.1.20230912"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230912 release

## Major updates
<a name="major-updates-2023.1.20230912"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ This release contains an updated `gcc` which addresses [CVE-2023-4039](https://alas.aws.amazon.com/cve/html/CVE-2023-4039.html). For more information see, [ALAS2023-2023-342](https://alas.aws.amazon.com/AL2023/ALAS-2023-342.html).
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230912)
+ [Repository](#amis-2023.1.20230912.repository)
+ [Docker container image](#amis-2023.1.20230912.container-image)
+ [Default AMI](#amis-2023.1.20230912.default-ami)
+ [Minimal AMI](#amis-2023.1.20230912.minimal-ami)

## Repository
<a name="amis-2023.1.20230912.repository"></a>

### New packages in AL2023.1.20230912 since AL2023.1.20230906
<a name="new-AL2023.1.20230906-AL2023.1.20230912"></a>

 Comparing AL2023.1.20230906 version 2023.1.20230906 to AL2023.1.20230912 version [2023.1.20230912](#relnotes-2023.1.20230912).

| Package Type | Number of new packages in AL2023.1.20230912 compared to AL2023.1.20230906 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.1.20230912:

- ** `git-lfs` **
  - **RPM:**  git-lfs
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.4.0-77.amzn2023.0.3

### AL2023.1.20230912 upgrades from AL2023.1.20230906
<a name="vercmp-AL2023.1.20230906-AL2023.1.20230912"></a>

 Comparing [2023.1.20230906](relnotes-2023.1.20230906.md) to [2023.1.20230912](#relnotes-2023.1.20230912).

| Package Type | Count |
| --- | --- |
| Source | 18 |
| Total Binary | 701 |
|  noarch binary RPMs | 68 |
|  x86\_64 binary RPMs | 319 |
|  aarch64 binary RPMs | 314 |

The full comparison of RPM package versions is below.

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-sqlite3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-doc  / **Architectures:** noarch
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-pkcs11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bind  / **Architectures:** noarch
  - **AL2023.1.20230906 version:** 9.16.42-1.amzn2023.0.3
  - **AL2023.1.20230912 version:** 9.16.42-1.amzn2023.0.4

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 8.2.1-1.amzn2023.0.2
  - **AL2023.1.20230912 version:** 8.2.1-1.amzn2023.0.3

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  gcc-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  libitm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libquadmath  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-devel  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-static  / **Architectures:** x86\_64
  - **RPM:**  libstdc\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 11.3.1-4.amzn2023.0.3
  - **AL2023.1.20230912 version:** 11.4.1-2.amzn2023.0.2

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
  - **AL2023.1.20230906 version:** 2.34-52.amzn2023.0.3
  - **AL2023.1.20230912 version:** 2.34-52.amzn2023.0.5

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
  - **AL2023.1.20230906 version:** 6.1.49-69.116.amzn2023
  - **AL2023.1.20230912 version:** 6.1.49-70.116.amzn2023

- ** `libidn` **
  - **RPM:**  libidn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn-java  / **Architectures:** noarch
  - **RPM:**  libidn-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230906 version:** 1.38-4.amzn2023.0.5
  - **AL2023.1.20230912 version:** 1.38-4.amzn2023.0.6

- ** `libidn2` **
  - **RPM:**  idn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 2.3.2-1.amzn2023.0.4
  - **AL2023.1.20230912 version:** 2.3.2-1.amzn2023.0.5

- ** `libjpeg-turbo` **
  - **RPM:**  libjpeg-turbo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 2.1.4-2.amzn2023.0.4
  - **AL2023.1.20230912 version:** 2.1.4-2.amzn2023.0.5

- ** `libpng` **
  - **RPM:**  libpng  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 1.6.37-10.amzn2023.0.4
  - **AL2023.1.20230912 version:** 1.6.37-10.amzn2023.0.6

- ** `libssh` **
  - **RPM:**  libssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh-config  / **Architectures:** noarch
  - **RPM:**  libssh-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 0.10.5-1.amzn2023.0.1
  - **AL2023.1.20230912 version:** 0.10.5-1.amzn2023.0.2

- ** `libssh2` **
  - **RPM:**  libssh2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh2-docs  / **Architectures:** noarch
  - **AL2023.1.20230906 version:** 1.10.0-1.amzn2023.0.2
  - **AL2023.1.20230912 version:** 1.10.0-1.amzn2023.0.3

- ** `libtasn1` **
  - **RPM:**  libtasn1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 4.19.0-1.amzn2023.0.3
  - **AL2023.1.20230912 version:** 4.19.0-1.amzn2023.0.4

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 2.10.4-1.amzn2023.0.3
  - **AL2023.1.20230912 version:** 2.10.4-1.amzn2023.0.5

- ** `nghttp2` **
  - **RPM:**  libnghttp2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnghttp2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nghttp2  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 1.55.1-1.amzn2023.0.1
  - **AL2023.1.20230912 version:** 1.55.1-1.amzn2023.0.4

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 8.7p1-8.amzn2023.0.7
  - **AL2023.1.20230912 version:** 8.7p1-8.amzn2023.0.8

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 3.0.8-1.amzn2023.0.4
  - **AL2023.1.20230912 version:** 3.0.8-1.amzn2023.0.7

- ** `sudo` **
  - **RPM:**  sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-logsrvd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-python-plugin  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230906 version:** 1.9.13-1.p2.amzn2023.0.3
  - **AL2023.1.20230912 version:** 1.9.13-1.p2.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230906 version:** 2023.1.20230906-0.amzn2023
  - **AL2023.1.20230912 version:** 2023.1.20230912-0.amzn2023

## Docker container image
<a name="amis-2023.1.20230912.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230912-0.amzn2023` |
| `bind-libs-32:9.16.42-1.amzn2023.0.4` |
| `bind-license-32:9.16.42-1.amzn2023.0.4.noarch` |
| `bind-utils-32:9.16.42-1.amzn2023.0.4` |
| `curl-minimal-8.2.1-1.amzn2023.0.3glibc-all-langpacks-2.34-52.amzn2023.0.5` |
| `glibc-common-2.34-52.amzn2023.0.5` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.5` |
| `glibc-locale-source-2.34-52.amzn2023.0.5` |
| `glibc-2.34-52.amzn2023.0.5` |
| `kernel-livepatch-repo-s3-2023.1.20230912-0.amzn2023` |
| `kernel-tools-6.1.49-70.116.amzn2023` |
| `kernel-6.1.49-70.116.amzn2023` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.3` |
| `libgcc-11.4.1-2.amzn2023.0.2` |
| `libgomp-11.4.1-2.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.5` |
| `libnghttp2-1.55.1-1.amzn2023.0.4` |
| `libstdc-11.4.1-2.amzn2023.0.2` |
| `libtasn1-4.19.0-1.amzn2023.0.4` |
| `libxml2-2.10.4-1.amzn2023.0.5` |
| `openssh-clients-8.7p1-8.amzn2023.0.8` |
| `openssh-server-8.7p1-8.amzn2023.0.8` |
| `openssh-8.7p1-8.amzn2023.0.8` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.7` |
| `openssl-1:3.0.8-1.amzn2023.0.7` |
| `sudo-1.9.13-1.p2.amzn2023.0.4` |
| `system-release-2023.1.20230912-0` |

## Default AMI
<a name="amis-2023.1.20230912.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.1.20230912-0.amzn2023` |
| `curl-minimal-8.2.1-1.amzn2023.0.3` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.5` |
| `glibc-common-2.34-52.amzn2023.0.5` |
| `glibc-locale-source-2.34-52.amzn2023.0.5` |
| `glibc-2.34-52.amzn2023.0.5` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.3` |
| `libgcc-11.4.1-2.amzn2023.0.2` |
| `libgomp-11.4.1-2.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.5` |
| `libnghttp2-1.55.1-1.amzn2023.0.4` |
| `libstdc-11.4.1-2.amzn2023.0.2` |
| `libtasn1-4.19.0-1.amzn2023.0.4` |
| `libxml2-2.10.4-1.amzn2023.0.5` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.7` |
| `system-release-2023.1.20230912-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.1.20230912.minimal-ami"></a>

|  |
| --- |
| `curl-minimal-8.2.1-1.amzn2023.0.3` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.5` |
| `glibc-common-2.34-52.amzn2023.0.5` |
| `glibc-locale-source-2.34-52.amzn2023.0.5` |
| `glibc-2.34-52.amzn2023.0.5` |
| `kernel-livepatch-repo-s3-2023.1.20230912-0.amzn2023` |
| `kernel-6.1.49-70.116.amzn2023` |
| `libcurl-minimal-8.2.1-1.amzn2023.0.3` |
| `libgcc-11.4.1-2.amzn2023.0.2` |
| `libgomp-11.4.1-2.amzn2023.0.2` |
| `libidn2-2.3.2-1.amzn2023.0.5` |
| `libnghttp2-1.55.1-1.amzn2023.0.4` |
| `libstdc-11.4.1-2.amzn2023.0.2` |
| `libtasn1-4.19.0-1.amzn2023.0.4` |
| `libxml2-2.10.4-1.amzn2023.0.5` |
| `openssh-clients-8.7p1-8.amzn2023.0.8` |
| `openssh-server-8.7p1-8.amzn2023.0.8` |
| `openssh-8.7p1-8.amzn2023.0.8` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.7` |
| `openssl-1:3.0.8-1.amzn2023.0.7` |
| `sudo-1.9.13-1.p2.amzn2023.0.4` |
| `system-release-2023.1.20230912-0.amzn2023` |
