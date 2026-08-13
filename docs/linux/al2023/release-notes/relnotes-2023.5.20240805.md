---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240805.html
---

# Amazon Linux 2023 version 2023.5.20240805 release notes
<a name="relnotes-2023.5.20240805"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240805.

**Topics**
+ [Major updates](#major-updates-2023.5.20240805)
+ [Repository](#amis-2023.5.20240805.repository)
+ [Docker container image](#amis-2023.5.20240805.container-image)
+ [Default AMI](#amis-2023.5.20240805.default-ami)
+ [Minimal AMI](#amis-2023.5.20240805.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240805.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240805.contact-us)

## Major updates
<a name="major-updates-2023.5.20240805"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240805.repository"></a>

### New packages in AL2023.5.20240805 since AL2023.5.20240730
<a name="new-AL2023.5.20240730-AL2023.5.20240805"></a>

 Comparing AL2023.5.20240730 version 2023.5.20240730 to AL2023.5.20240805 version [2023.5.20240805](#relnotes-2023.5.20240805).

| Package Type | Number of new packages in AL2023.5.20240805 compared to AL2023.5.20240730 |
| --- | --- |
| Source RPMs | 4 |
| Total Binary RPMs | 10 |
|  noarch binary RPMs | 6 |
|  x86\_64 binary RPMs | 2 |
|  aarch64 binary RPMs | 2 |

New packages in AL2023.5.20240805:

- ** `duktape` **
  - **RPM:**  duktape  / **Architectures:** aarch64, x86\_64
  - **RPM:**  duktape-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.7.0-21.amzn2023

- ** `gi-docgen` **
  - **RPM:**  gi-docgen  / **Architectures:** noarch
  - **RPM:**  gi-docgen-doc  / **Architectures:** noarch
  - **RPM:**  gi-docgen-fonts  / **Architectures:** noarch
  - **Version:** 2024.1-43.amzn2023.0.1

- ** `python-smartypants` **
  - **RPM:**  python3-smartypants  / **Architectures:** noarch
  - **RPM:**  python-smartypants-doc  / **Architectures:** noarch
  - **Version:** 2.0.1-17.amzn2023.0.1

- ** `python-typogrify` **
  - **RPM:**  python3-typogrify
  - **Architectures:** noarch
  - **Version:** 2.0.7-17.amzn2023.0.1

### AL2023.5.20240805 upgrades from AL2023.5.20240730
<a name="vercmp-AL2023.5.20240730-AL2023.5.20240805"></a>

 Comparing [2023.5.20240730](relnotes-2023.5.20240730.md) to [2023.5.20240805](#relnotes-2023.5.20240805).

| Package Type | Count |
| --- | --- |
| Source | 35 |
| Total Binary | 1006 |
|  noarch binary RPMs | 220 |
|  x86\_64 binary RPMs | 394 |
|  aarch64 binary RPMs | 392 |

The full comparison of RPM package versions is below.

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.3.1-0.amzn2023
  - **AL2023.5.20240805 version:** 1.3.2-0.amzn2023

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dlz-sqlite3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 9.16.48-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 9.18.28-1.amzn2023.0.1

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2023.5.20240730 version:** 2023.2.64-1.0.amzn2023.0.1
  - **AL2023.5.20240805 version:** 2023.2.68-1.0.amzn2023.0.1

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.7.11-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 1.7.20-1.amzn2023.0.1

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 6.0.29-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 6.0.32-1.amzn2023.0.1

- ** `dotnet8.0` **
  - **RPM:**  aspnetcore-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 8.0.5-1.amzn2023
  - **AL2023.5.20240805 version:** 8.0.7-1.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.85.1-1.amzn2023
  - **AL2023.5.20240805 version:** 1.85.3-1.amzn2023

- ** `freetype` **
  - **RPM:**  freetype  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-demos  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 2.13.0-2.amzn2023.0.1
  - **AL2023.5.20240805 version:** 2.13.2-5.amzn2023.0.1

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
  - **AL2023.5.20240730 version:** 9.56.1-7.amzn2023.0.8
  - **AL2023.5.20240805 version:** 9.56.1-7.amzn2023.0.10

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
  - **AL2023.5.20240730 version:** 2.34-52.amzn2023.0.10
  - **AL2023.5.20240805 version:** 2.34-52.amzn2023.0.11

- ** `gtk3` **
  - **RPM:**  gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-devel-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-immodules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-immodule-xim  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk-update-icon-cache  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 3.24.30-4.amzn2023.0.4
  - **AL2023.5.20240805 version:** 3.24.43-1.amzn2023.0.1

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
  - **AL2023.5.20240730 version:** 2.4.61-1.amzn2023
  - **AL2023.5.20240805 version:** 2.4.62-1.amzn2023

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
  - **AL2023.5.20240730 version:** 6.1.97-104.177.amzn2023
  - **AL2023.5.20240805 version:** 6.1.102-108.177.amzn2023

- ** `krb5` **
  - **RPM:**  krb5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-pkinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-workstation  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libkadm5  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.21-3.amzn2023.0.4
  - **AL2023.5.20240805 version:** 1.21.3-1.amzn2023.0.1

- ** `libproxy` **
  - **RPM:**  libproxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libproxy-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libproxy-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 0.4.15-30.amzn2023.0.5
  - **AL2023.5.20240805 version:** 0.5.7-3.amzn2023.0.1

- ** `libsndfile` **
  - **RPM:**  libsndfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.2.2-3.amzn2023.0.1
  - **AL2023.5.20240805 version:** 1.2.2-3.amzn2023.0.2

- ** `libxmlb` **
  - **RPM:**  libxmlb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxmlb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxmlb-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 0.3.11-42.amzn2023
  - **AL2023.5.20240805 version:** 0.3.19-59.amzn2023.0.1

- ** `linux-firmware` **
  - **RPM:**  iwl1000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl100-firmware  / **Architectures:** noarch
  - **RPM:**  iwl105-firmware  / **Architectures:** noarch
  - **RPM:**  iwl135-firmware  / **Architectures:** noarch
  - **RPM:**  iwl2000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl2030-firmware  / **Architectures:** noarch
  - **RPM:**  iwl3160-firmware  / **Architectures:** noarch
  - **RPM:**  iwl3945-firmware  / **Architectures:** noarch
  - **RPM:**  iwl4965-firmware  / **Architectures:** noarch
  - **RPM:**  iwl5000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl5150-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000g2a-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6000g2b-firmware  / **Architectures:** noarch
  - **RPM:**  iwl6050-firmware  / **Architectures:** noarch
  - **RPM:**  iwl7260-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-sd8686-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-sd8787-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-usb8388-firmware  / **Architectures:** noarch
  - **RPM:**  libertas-usb8388-olpc-firmware  / **Architectures:** noarch
  - **RPM:**  linux-firmware  / **Architectures:** noarch
  - **RPM:**  linux-firmware-whence  / **Architectures:** noarch
  - **RPM:**  liquidio-firmware  / **Architectures:** noarch
  - **RPM:**  netronome-firmware  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 39.31.5.1-117.amzn2023.0.4
  - **AL2023.5.20240805 version:** 39.31.5.1-117.amzn2023.0.5

- ** `lvm2` **
  - **RPM:**  device-mapper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-dbusd  / **Architectures:** noarch
  - **RPM:**  lvm2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-lockd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.02.185-1.amzn2023.0.4
  - **AL2023.5.20240805 version:** 1.02.185-1.amzn2023.0.5

- ** `mariadb105` **
  - **RPM:**  mariadb105  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-backup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-connect-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-cracklib-password-check  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-errmsg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-gssapi-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-oqgraph-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-rocksdb-engine  / **Architectures:** x86\_64
  - **RPM:**  mariadb105-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-server-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-sphinx-engine  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 10.5.23-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 10.5.25-1.amzn2023.0.1

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.5.20240730 version:** 2.1-53.amzn2023.0.5
  - **AL2023.5.20240805 version:** 2.1-53.amzn2023.0.7

- ** `mod_http2` **
  - **RPM:**  mod\_http2
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 2.0.27-1.amzn2023.0.2
  - **AL2023.5.20240805 version:** 2.0.27-1.amzn2023.0.3

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 1.7.2-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 1.7.6-1.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 18.18.2-1.amzn2023.0.5
  - **AL2023.5.20240805 version:** 18.20.2-1.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 3.0.8-1.amzn2023.0.12
  - **AL2023.5.20240805 version:** 3.0.8-1.amzn2023.0.14

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
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
  - **AL2023.5.20240730 version:** 8.2.18-1.amzn2023.0.1
  - **AL2023.5.20240805 version:** 8.2.21-1.amzn2023.0.1

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 3.9.16-1.amzn2023.0.8
  - **AL2023.5.20240805 version:** 3.9.16-1.amzn2023.0.9

- ** `python-setuptools` **
  - **RPM:**  python3-setuptools  / **Architectures:** noarch
  - **RPM:**  python3-setuptools-wheel  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 59.6.0-2.amzn2023.0.4
  - **AL2023.5.20240805 version:** 59.6.0-2.amzn2023.0.5

- ** `python-tqdm` **
  - **RPM:**  python3-tqdm
  - **Architectures:** noarch
  - **AL2023.5.20240730 version:** 4.61.1-1.amzn2023.0.2
  - **AL2023.5.20240805 version:** 4.61.1-1.amzn2023.0.3

- ** `rapidjson` **
  - **RPM:**  rapidjson-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rapidjson-doc  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 1.1.0-16.amzn2023.0.2
  - **AL2023.5.20240805 version:** 1.1.0-16.amzn2023.0.3

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 6.6-1.amzn2023.0.3
  - **AL2023.5.20240805 version:** 6.6-1.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 2023.5.20240730-0.amzn2023
  - **AL2023.5.20240805 version:** 2023.5.20240805-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.5.20240730 version:** 9.0.90-1.amzn2023.0.2
  - **AL2023.5.20240805 version:** 9.0.91-1.amzn2023.0.1

- ** `tpm2-tools` **
  - **RPM:**  tpm2-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 5.5-4.amzn2023.0.1
  - **AL2023.5.20240805 version:** 5.5-4.amzn2023.0.2

- ** `vala` **
  - **RPM:**  libvala  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvala-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vala  / **Architectures:** aarch64, x86\_64
  - **RPM:**  valadoc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vala-doc  / **Architectures:** noarch
  - **RPM:**  valadoc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240730 version:** 0.48.19-1.amzn2023.0.3
  - **AL2023.5.20240805 version:** 0.56.17-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.5.20240805.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240805-0.amzn2023` |
| `ca-certificates-2023.2.68-1.0.amzn2023.0.1` |
| `glibc-common-2.34-52.amzn2023.0.11` |
| `glibc-minimal-langpack-2.34-52.amzn2023.0.11` |
| `glibc-2.34-52.amzn2023.0.11` |
| `krb5-libs-1.21.3-1.amzn2023.0.1` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.14` |
| `python3-libs-3.9.16-1.amzn2023.0.9` |
| `python3-setuptools-wheel-59.6.0-2.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.9` |
| `system-release-2023.5.20240805-0.amzn2023` |

## Default AMI
<a name="amis-2023.5.20240805.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240805-0.amzn2023` |
| `bind-libs-32:9.18.28-1.amzn2023.0.1` |
| `bind-license-32:9.18.28-1.amzn2023.0.1` |
| `bind-utils-32:9.18.28-1.amzn2023.0.1` |
| `ca-certificates-2023.2.68-1.0.amzn2023.0.1` |
| `device-mapper-libs-1.02.185-1.amzn2023.0.5` |
| `device-mapper-1.02.185-1.amzn2023.0.5` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.11` |
| `glibc-common-2.34-52.amzn2023.0.11` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.11` |
| `glibc-locale-source-2.34-52.amzn2023.0.11` |
| `glibc-2.34-52.amzn2023.0.11` |
| `jemalloc-5.2.1-7.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240805-0.amzn2023` |
| `kernel-tools-6.1.102-108.177.amzn2023` |
| `kernel-6.1.102-108.177.amzn2023` |
| `krb5-libs-1.21.3-1.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.7` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.14` |
| `openssl-1:3.0.8-1.amzn2023.0.14` |
| `python3-libs-3.9.16-1.amzn2023.0.9` |
| `python3-setuptools-wheel-59.6.0-2.amzn2023.0.5` |
| `python3-setuptools-59.6.0-2.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.9` |
| `system-release-2023.5.20240805-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.5.20240805.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240805-0.amzn2023` |
| `ca-certificates-2023.2.68-1.0.amzn2023.0.1` |
| `device-mapper-libs-1.02.185-1.amzn2023.0.5` |
| `device-mapper-1.02.185-1.amzn2023.0.5` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.11` |
| `glibc-common-2.34-52.amzn2023.0.11` |
| `glibc-locale-source-2.34-52.amzn2023.0.11` |
| `glibc-2.34-52.amzn2023.0.11` |
| `kernel-livepatch-repo-s3-2023.5.20240805-0.amzn2023` |
| `kernel-6.1.102-108.177.amzn2023` |
| `krb5-libs-1.21.3-1.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.7` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.14` |
| `openssl-1:3.0.8-1.amzn2023.0.14` |
| `python3-libs-3.9.16-1.amzn2023.0.9` |
| `python3-setuptools-wheel-59.6.0-2.amzn2023.0.5` |
| `python3-setuptools-59.6.0-2.amzn2023.0.5` |
| `python3-3.9.16-1.amzn2023.0.9` |
| `system-release-2023.5.20240805-0.amzn2023` |

## Minimal container image
<a name="amis-2023.5.20240805.minimal-container-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240805-0.amzn2023` |
| `ca-certificates-2023.2.68-1.0.amzn2023.0.1` |
| `glibc-common-2.34-52.amzn2023.0.11` |
| `glibc-minimal-langpack-2.34-52.amzn2023.0.11` |
| `glibc-2.34-52.amzn2023.0.11` |
| `krb5-libs-1.21.3-1.amzn2023.0.1` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.14` |
| `system-release-2023.5.20240805-0.amzn2023` |

## Contact us
<a name="amis-2023.5.20240805.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
