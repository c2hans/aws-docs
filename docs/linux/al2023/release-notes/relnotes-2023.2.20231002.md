---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20231002.html
---

# Amazon Linux 2023 version 2023.2.20231002 release notes
<a name="relnotes-2023.2.20231002"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20231002 release

## Major updates
<a name="major-updates-2023.2.20231002"></a>

This release represents an update to the second quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+ An update to the `amazon-ec2-net-utils` package corrects an issue that could lead to mis-routed packets in some multi-ENI configurations, resulting in packet loss.
+ The EC2 Rescue utility was added to AL2023. For more information, see [Use EC2Rescue for Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.html).
+ The Amazon Corretto 21 binding for Maven was added.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).
+ For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.2.20231002)
+ [Repository](#amis-2023.2.20231002.repository)
+ [Docker container image](#amis-2023.2.20231002.container-image)
+ [Default AMI](#amis-2023.2.20231002.default-ami)
+ [Minimal AMI](#amis-2023.2.20231002.minimal-ami)
+ [Minimal container image](#amis-2023.2.20231002.minimal-container-ami)

## Repository
<a name="amis-2023.2.20231002.repository"></a>

### New packages in AL2023.2.20231002 since AL2023.2.20230920
<a name="new-AL2023.2.20230920-AL2023.2.20231002"></a>

 Comparing AL2023.2.20230920 version 2023.2.20230920 to AL2023.2.20231002 version [2023.2.20231002](#relnotes-2023.2.20231002).

| Package Type | Number of new packages in AL2023.2.20231002 compared to AL2023.2.20230920 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 3 |
|  noarch binary RPMs | 3 |

New packages in AL2023.2.20231002:

- ** `ec2rl` **
  - **RPM:**  ec2rl
  - **Architectures:** noarch
  - **Version:** 1.1.6-1.amzn2023.0.2

- ** `javapackages-tools` **
  - **RPM:**  maven-local-amazon-corretto21
  - **Architectures:** noarch
  - **Version:** 6.0.0-7.amzn2023.0.6

- ** `maven` **
  - **RPM:**  maven-amazon-corretto21
  - **Architectures:** noarch
  - **Version:** 3.8.4-3.amzn2023.0.5

### AL2023.2.20231002 upgrades from AL2023.2.20230920
<a name="vercmp-AL2023.2.20230920-AL2023.2.20231002"></a>

 Comparing [2023.2.20230920](relnotes-2023.2.20230920.md) to [2023.2.20231002](#relnotes-2023.2.20231002).

| Package Type | Count |
| --- | --- |
| Source | 26 |
| Total Binary | 816 |
|  noarch binary RPMs | 200 |
|  x86\_64 binary RPMs | 308 |
|  aarch64 binary RPMs | 308 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 1.300026.3-2.amzn2023
  - **AL2023.2.20231002 version:** 1.300028.1-1.amzn2023

- ** [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html) **
  - **RPM:**  [`amazon-ec2-net-utils`](https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html)
  - **Architectures:** noarch
  - **AL2023.2.20230920 version:** 2.3.0-1.amzn2023.0.2
  - **AL2023.2.20231002 version:** 2.4.0-1.amzn2023.0.1

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 3.2.1377.0-1.amzn2023
  - **AL2023.2.20231002 version:** 3.2.1630.0-1.amzn2023

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
  - **AL2023.2.20230920 version:** 9.16.42-1.amzn2023.0.4
  - **AL2023.2.20231002 version:** 9.16.42-1.amzn2023.0.5

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 2.3.3op2-18.amzn2023.0.6
  - **AL2023.2.20231002 version:** 2.3.3op2-18.amzn2023.0.7

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 8.2.1-1.amzn2023.0.3
  - **AL2023.2.20231002 version:** 8.3.0-1.amzn2023.0.1

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 6.0.21-1.amzn2023.0.2
  - **AL2023.2.20231002 version:** 6.0.22-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 1.75.3-1.amzn2023
  - **AL2023.2.20231002 version:** 1.76.0-1.amzn2023

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
  - **AL2023.2.20230920 version:** 9.56.1-7.amzn2023.0.3
  - **AL2023.2.20231002 version:** 9.56.1-7.amzn2023.0.4

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
  - **AL2023.2.20230920 version:** 2.34-52.amzn2023.0.5
  - **AL2023.2.20231002 version:** 2.34-52.amzn2023.0.6

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 1.20.7-1.amzn2023.0.1
  - **AL2023.2.20231002 version:** 1.20.8-1.amzn2023.0.1

- ** `javapackages-tools` **
  - **RPM:**  javapackages-filesystem  / **Architectures:** noarch
  - **RPM:**  javapackages-generators  / **Architectures:** noarch
  - **RPM:**  javapackages-local  / **Architectures:** noarch
  - **RPM:**  javapackages-tools  / **Architectures:** noarch
  - **RPM:**  maven-local  / **Architectures:** noarch
  - **RPM:**  maven-local-amazon-corretto11  / **Architectures:** noarch
  - **RPM:**  maven-local-amazon-corretto17  / **Architectures:** noarch
  - **RPM:**  maven-local-amazon-corretto8  / **Architectures:** noarch
  - **RPM:**  python3-javapackages  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 6.0.0-7.amzn2023.0.5
  - **AL2023.2.20231002 version:** 6.0.0-7.amzn2023.0.6

- ** `jbigkit` **
  - **RPM:**  jbigkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbigkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbigkit-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 2.1-21.amzn2023.0.1
  - **AL2023.2.20231002 version:** 2.1-21.amzn2023.0.2

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
  - **AL2023.2.20230920 version:** 6.1.52-71.125.amzn2023
  - **AL2023.2.20231002 version:** 6.1.55-75.123.amzn2023

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 4.4.0-4.amzn2023.0.14
  - **AL2023.2.20231002 version:** 4.4.0-4.amzn2023.0.16

- ** `libtommath` **
  - **RPM:**  libtommath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtommath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtommath-doc  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 1.2.0-9.amzn2023.0.1
  - **AL2023.2.20231002 version:** 1.2.0-62.amzn2023.0.1

- ** `libwebp` **
  - **RPM:**  libwebp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 1.2.4-1.amzn2023.0.4
  - **AL2023.2.20231002 version:** 1.2.4-1.amzn2023.0.6

- ** `maven` **
  - **RPM:**  maven  / **Architectures:** noarch
  - **RPM:**  maven-amazon-corretto11  / **Architectures:** noarch
  - **RPM:**  maven-amazon-corretto17  / **Architectures:** noarch
  - **RPM:**  maven-amazon-corretto8  / **Architectures:** noarch
  - **RPM:**  maven-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-lib  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 3.8.4-3.amzn2023.0.4
  - **AL2023.2.20231002 version:** 3.8.4-3.amzn2023.0.5

- ** `mutt` **
  - **RPM:**  mutt
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 2.2.9-1.amzn2023.0.1
  - **AL2023.2.20231002 version:** 2.2.9-1.amzn2023.0.2

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 1.1.0-1.amzn2023.0.3
  - **AL2023.2.20231002 version:** 1.1.0-1.amzn2023.0.4

- ** `pmix` **
  - **RPM:**  pmix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pmix-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pmix-pmi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pmix-pmi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pmix-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 3.2.3-1.amzn2023.0.2
  - **AL2023.2.20231002 version:** 3.2.3-1.amzn2023.0.3

- ** `poppler` **
  - **RPM:**  poppler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-doc  / **Architectures:** noarch
  - **RPM:**  poppler-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 22.08.0-3.amzn2023.0.3
  - **AL2023.2.20231002 version:** 22.08.0-3.amzn2023.0.4

- ** `snakeyaml` **
  - **RPM:**  snakeyaml  / **Architectures:** noarch
  - **RPM:**  snakeyaml-javadoc  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 1.27-6.amzn2023.0.2
  - **AL2023.2.20231002 version:** 1.27-6.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 2023.2.20230920-0.amzn2023
  - **AL2023.2.20231002 version:** 2023.2.20231002-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.2.20230920 version:** 9.0.71-1.amzn2023.0.4
  - **AL2023.2.20231002 version:** 9.0.71-1.amzn2023.0.5

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20230920 version:** 9.0.1592-1.amzn2023.0.1
  - **AL2023.2.20231002 version:** 9.0.1882-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.2.20231002.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20231002-0.amzn2023`
+ `curl-minimal-8.3.0-1.amzn2023.0.1`
+ `glibc-2.34-52.amzn2023.0.6`
+ `glibc-common-2.34-52.amzn2023.0.6`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.6`
+ `libcurl-minimal-8.3.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231002-0.amzn2023`

## Default AMI
<a name="amis-2023.2.20231002.default-ami"></a>

|  |
| --- |
| `amazon-ec2-net-utils-2.4.0-1.amzn2023.0.1` |
| `amazon-linux-repo-s3-2023.2.20231002-0.amzn2023` |
| `amazon-ssm-agent-3.2.1630.0-1.amzn2023` |
| `bind-libs-32:9.16.42-1.amzn2023.0.5` |
| `bind-license-32:9.16.42-1.amzn2023.0.5` |
| `bind-utils-32:9.16.42-1.amzn2023.0.5` |
| `curl-minimal-8.3.0-1.amzn2023.0.1` |
| `glibc-2.34-52.amzn2023.0.6` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.6` |
| `glibc-common-2.34-52.amzn2023.0.6` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.6` |
| `glibc-locale-source-2.34-52.amzn2023.0.6` |
| `kernel-6.1.55-75.123.amzn2023` |
| `kernel-livepatch-repo-s3-2023.2.20231002-0.amzn2023` |
| `kernel-tools-6.1.55-75.123.amzn2023` |
| `libcurl-minimal-8.3.0-1.amzn2023.0.1` |
| `system-release-2023.2.20231002-0.amzn2023` |
| `vim-common-2:9.0.1882-1.amzn2023.0.1` |
| `vim-data-2:9.0.1882-1.amzn2023.0.1` |
| `vim-enhanced-2:9.0.1882-1.amzn2023.0.1` |
| `vim-filesystem-2:9.0.1882-1.amzn2023.0.1` |
| `vim-minimal-2:9.0.1882-1.amzn2023.0.1` |
| `xxd-2:9.0.1882-1.amzn2023.0.1` |

## Minimal AMI
<a name="amis-2023.2.20231002.minimal-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231002-0.amzn2023`
+ `curl-minimal-8.3.0-1.amzn2023.0.1`
+ `glibc-2.34-52.amzn2023.0.6`
+ `glibc-common-2.34-52.amzn2023.0.6`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.6`
+ `libcurl-minimal-8.3.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231002-0.amzn2023`

## Minimal container image
<a name="amis-2023.2.20231002.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20231002-0.amzn2023`
+ `curl-minimal-8.3.0-1.amzn2023.0.1`
+ `glibc-2.34-52.amzn2023.0.6`
+ `glibc-common-2.34-52.amzn2023.0.6`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.6`
+ `libcurl-minimal-8.3.0-1.amzn2023.0.1`
+ `system-release-2023.2.20231002-0.amzn2023`
