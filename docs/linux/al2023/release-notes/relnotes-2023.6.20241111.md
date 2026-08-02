---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241111.html
---

# Amazon Linux 2023 version 2023.6.20241111 release notes
<a name="relnotes-2023.6.20241111"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20241111.

**Topics**
+ [Major updates](#major-updates-2023.6.20241111)
+ [Repository](#amis-2023.6.20241111.repository)
+ [Docker container image](#amis-2023.6.20241111.container-image)
+ [Default AMI](#amis-2023.6.20241111.default-ami)
+ [Minimal AMI](#amis-2023.6.20241111.minimal-ami)
+ [Minimal container image](#amis-2023.6.20241111.minimal-container-ami)
+ [Contact us](#amis-2023.6.20241111.contact-us)

## Major updates
<a name="major-updates-2023.6.20241111"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Note**
Amazon Linux 2023 minimal AMIs were incorrectly configured with 8GB root volume by default. We addressed this issue in the 2023.6.20241111.0 release, ensuring that minimal AMIs have a default root volume size of 2GB, consistent with Amazon Linux 2 minimal AMIs. We regret any inconvenience this may have caused. These volume sizes will not shrink in any future Amazon Linux 2023 release.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20241111.repository"></a>

### New packages in AL2023.6.20241111 since AL2023.6.20241031
<a name="new-AL2023.6.20241031-AL2023.6.20241111"></a>

 Comparing AL2023.6.20241031 version 2023.6.20241031 to AL2023.6.20241111 version [2023.6.20241111](#relnotes-2023.6.20241111).

| Package Type | Number of new packages in AL2023.6.20241111 compared to AL2023.6.20241031 |
| --- | --- |
| Source RPMs | 10 |
| Total Binary RPMs | 64 |
|  noarch binary RPMs | 8 |
|  x86\_64 binary RPMs | 28 |
|  aarch64 binary RPMs | 28 |

New packages in AL2023.6.20241111:

- ** `libdbusmenu` **
  - **RPM:**  libdbusmenu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-doc  / **Architectures:** noarch
  - **RPM:**  libdbusmenu-gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-gtk3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-jsonloader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-jsonloader-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 16.04.0-27.amzn2023.0.1

- ** `libdecor` **
  - **RPM:**  libdecor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdecor-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.2.2-3.amzn2023

- ** `libei` **
  - **RPM:**  libei  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libei-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libeis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libeis-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libei-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboeffis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboeffis-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.0-1.amzn2023.0.1

- ** `mesa-demos` **
  - **RPM:**  egl-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glx-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-demos  / **Architectures:** aarch64, x86\_64
  - **Version:** 9.0.0-8.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-tkinter  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.12.6-1.amzn2023.0.2

- ** `python3.12-flit-core` **
  - **RPM:**  python3.12-flit-core
  - **Architectures:** noarch
  - **Version:** 3.9.0-3.amzn2023.0.2

- ** `python3.12-pip` **
  - **RPM:**  python3.12-pip  / **Architectures:** noarch
  - **RPM:**  python3.12-pip-wheel  / **Architectures:** noarch
  - **Version:** 23.2.1-4.amzn2023.0.1

- ** `python3.12-setuptools` **
  - **RPM:**  python3.12-setuptools  / **Architectures:** noarch
  - **RPM:**  python3.12-setuptools-wheel  / **Architectures:** noarch
  - **Version:** 68.2.2-4.amzn2023.0.2

- ** `python3.12-wheel` **
  - **RPM:**  python3.12-wheel  / **Architectures:** noarch
  - **RPM:**  python3.12-wheel-wheel  / **Architectures:** noarch
  - **Version:** 0.41.2-3.amzn2023.0.2

- ** `xorg-x11-server-Xwayland` **
  - **RPM:**  xorg-x11-server-Xwayland  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xwayland-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 24.1.3-1.amzn2023

### AL2023.6.20241111 upgrades from AL2023.6.20241031
<a name="vercmp-AL2023.6.20241031-AL2023.6.20241111"></a>

 Comparing [2023.6.20241031](relnotes-2023.6.20241031.md) to [2023.6.20241111](#relnotes-2023.6.20241111).

| Package Type | Count |
| --- | --- |
| Source | 34 |
| Total Binary | 768 |
|  noarch binary RPMs | 144 |
|  x86\_64 binary RPMs | 312 |
|  aarch64 binary RPMs | 312 |

The full comparison of RPM package versions is below.

- ** `amazon-rpm-config` **
  - **RPM:**  amazon-rpm-config
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 228-3.amzn2023.0.2
  - **AL2023.6.20241111 version:** 228-4.amzn2023.0.1

- ** `aws-kinesis-agent` **
  - **RPM:**  aws-kinesis-agent
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 2.0.9-3.amzn2023
  - **AL2023.6.20241111 version:** 2.0.10-1.amzn2023

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.7.22-1.amzn2023.0.2
  - **AL2023.6.20241111 version:** 1.7.23-1.amzn2023.0.1

- ** `container-selinux` **
  - **RPM:**  container-selinux
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 2.222.0-325.amzn2023
  - **AL2023.6.20241111 version:** 2.233.0-1.amzn2023

- ** `dracut` **
  - **RPM:**  dracut  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-caps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-generic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-rescue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-squash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 055-6.amzn2023.0.8
  - **AL2023.6.20241111 version:** 102-3.amzn2023.0.1

- ** `ec2-utils` **
  - **RPM:**  ec2-utils
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 2.2.0-1.amzn2023.0.1
  - **AL2023.6.20241111 version:** 2.2.0-1.amzn2023.0.2

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** v1.29.6.1-1.amzn2023
  - **AL2023.6.20241111 version:** v1.29.9.0-1.amzn2023

- ** `expat` **
  - **RPM:**  expat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 2.5.0-1.amzn2023.0.4
  - **AL2023.6.20241111 version:** 2.6.3-1.amzn2023.0.1

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
  - **AL2023.6.20241031 version:** 2.34-52.amzn2023.0.11
  - **AL2023.6.20241111 version:** 2.34-117.amzn2023.0.1

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
  - **AL2023.6.20241031 version:** 6.1.112-124.190.amzn2023
  - **AL2023.6.20241111 version:** 6.1.115-126.197.amzn2023

- ** `libevdev` **
  - **RPM:**  libevdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevdev-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevdev-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.11.0-1.amzn2023.0.2
  - **AL2023.6.20241111 version:** 1.13.3-1.amzn2023.0.1

- ** `libinput` **
  - **RPM:**  libinput  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libinput-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libinput-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libinput-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.19.4-1.amzn2023.0.2
  - **AL2023.6.20241111 version:** 1.26.2-1.amzn2023.0.1

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 16.4-1.amzn2023.0.1
  - **AL2023.6.20241111 version:** 16.4-1.amzn2023.0.2

- ** `man-pages` **
  - **RPM:**  man-pages
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 5.10-2.amzn2023.0.3
  - **AL2023.6.20241111 version:** 6.04-3.amzn2023.0.1

- ** `mesa` **
  - **RPM:**  mesa-dri-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libd3d  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libd3d-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libglapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOpenCL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOpenCL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libxatracker  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libxatracker-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-va-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-vdpau-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-vulkan-drivers  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 24.1.7-1251.amzn2023.0.2
  - **AL2023.6.20241111 version:** 24.2.6-1267.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 18.20.2-1.amzn2023.0.1
  - **AL2023.6.20241111 version:** 18.20.4-1.amzn2023.0.1

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 20.12.2-1.amzn2023.0.2
  - **AL2023.6.20241111 version:** 20.18.0-1.amzn2023.0.2

- ** `nvme-cli` **
  - **RPM:**  nvme-cli
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.11.1-3.amzn2023.0.3
  - **AL2023.6.20241111 version:** 1.11.1-3.amzn2023.0.4

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 3.11.6-1.amzn2023.0.3
  - **AL2023.6.20241111 version:** 3.11.6-1.amzn2023.0.4

- ** `python3.11-pip` **
  - **RPM:**  python3.11-pip  / **Architectures:** noarch
  - **RPM:**  python3.11-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20241031 version:** 22.3.1-2.amzn2023.0.3
  - **AL2023.6.20241111 version:** 22.3.1-2.amzn2023.0.4

- ** `python-idna` **
  - **RPM:**  python3-idna
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 2.10-3.amzn2023.0.2
  - **AL2023.6.20241111 version:** 2.10-3.amzn2023.0.3

- ** `python-pillow` **
  - **RPM:**  python3-pillow  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-tk  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 9.4.0-2.amzn2023.0.5
  - **AL2023.6.20241111 version:** 9.4.0-2.amzn2023.0.6

- ** `python-pip` **
  - **RPM:**  python3-pip  / **Architectures:** noarch
  - **RPM:**  python3-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20241031 version:** 21.3.1-2.amzn2023.0.8
  - **AL2023.6.20241111 version:** 21.3.1-2.amzn2023.0.9

- ** `python-rpm-generators` **
  - **RPM:**  python3-rpm-generators
  - **Architectures:** noarch
  - **AL2023.6.20241031 version:** 12-15.amzn2023.0.4
  - **AL2023.6.20241111 version:** 12-15.amzn2023.0.5

- ** `python-rpm-macros` **
  - **RPM:**  python3-rpm-macros  / **Architectures:** noarch
  - **RPM:**  python-rpm-macros  / **Architectures:** noarch
  - **RPM:**  python-srpm-macros  / **Architectures:** noarch
  - **AL2023.6.20241031 version:** 3.9-41.amzn2023.0.5
  - **AL2023.6.20241111 version:** 3.9-41.amzn2023.0.6

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.3.0-1.amzn2023.0.1
  - **AL2023.6.20241111 version:** 1.4.1-1.amzn2023.0.1

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.6.20241031 version:** 38.1.45-1.amzn2023.0.1
  - **AL2023.6.20241111 version:** 38.1.47-1.amzn2023.0.1

- ** `soci-snapshotter` **
  - **RPM:**  soci-snapshotter
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 0.7.0-1.amzn2023.0.2
  - **AL2023.6.20241111 version:** 0.8.0-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20241031 version:** 2023.6.20241031-0.amzn2023
  - **AL2023.6.20241111 version:** 2023.6.20241111-0.amzn2023

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.17.1-1.amzn2023.0.6
  - **AL2023.6.20241111 version:** 1.17.1-1.amzn2023.0.7

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 9.0.2153-1.amzn2023
  - **AL2023.6.20241111 version:** 9.1.785-1.amzn2023.0.1

- ** `xorg-x11-drv-dummy` **
  - **RPM:**  xorg-x11-drv-dummy
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 0.3.7-14.amzn2023.0.2
  - **AL2023.6.20241111 version:** 0.4.1-2.amzn2023.0.1

- ** `xorg-x11-drv-libinput` **
  - **RPM:**  xorg-x11-drv-libinput  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-drv-libinput-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.0.1-2.amzn2023.0.2
  - **AL2023.6.20241111 version:** 1.4.0-2.amzn2023.0.1

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20241031 version:** 1.20.14-30.amzn2023.0.2
  - **AL2023.6.20241111 version:** 21.1.13-5.amzn2023.0.2

## Docker container image
<a name="amis-2023.6.20241111.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241111-0.amzn2023 |
| expat-2.6.3-1.amzn2023.0.1 |
| glibc-common-2.34-117.amzn2023.0.1  |
| glibc-minimal-langpack-2.34-117.amzn2023.0.1  |
| glibc-2.34-117.amzn2023.0.1 |
| python3-pip-wheel-21.3.1-2.amzn2023.0.9  |
| system-release-2023.6.20241111-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20241111.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241111-0.amzn2023 |
| amazon-rpm-config-228-4.amzn2023.0.1  |
| ec2-utils-2.2.0-1.amzn2023.0.2  |
| expat-2.6.3-1.amzn2023.0.1  |
| glibc-all-langpacks-2.34-117.amzn2023.0.1  |
| glibc-common-2.34-117.amzn2023.0.1  |
| glibc-gconv-extra-2.34-117.amzn2023.0.1  |
| glibc-locale-source-2.34-117.amzn2023.0.1 |
| glibc-2.34-117.amzn2023.0.1  |
| kernel-libbpf-6.1.115-126.197.amzn2023  |
| kernel-livepatch-repo-s3-2023.6.20241111-0.amzn2023  |
| kernel-tools-6.1.115-126.197.amzn2023 |
| kernel-6.1.115-126.197.amzn2023 |
| man-pages-6.04-3.amzn2023.0.1  |
| python-srpm-macros-3.9-41.amzn2023.0.6  |
| python3-idna-2.10-3.amzn2023.0.3  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.9  |
| selinux-policy-targeted-38.1.47-1.amzn2023.0.1  |
| selinux-policy-38.1.47-1.amzn2023.0.1  |
| system-release-2023.6.20241111-0.amzn2023  |
| vim-common-2:9.1.785-1.amzn2023.0.1  |
| vim-data-2:9.1.785-1.amzn2023.0.1  |
| vim-enhanced-2:9.1.785-1.amzn2023.0.1  |
| vim-filesystem-2:9.1.785-1.amzn2023.0.1  |
| vim-minimal-2:9.1.785-1.amzn2023.0.1 |
| xxd-2:9.1.785-1.amzn2023.0.1 |

## Minimal AMI
<a name="amis-2023.6.20241111.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20241111-0.amzn2023 |
| ec2-utils-2.2.0-1.amzn2023.0.2  |
| expat-2.6.3-1.amzn2023.0.1  |
| glibc-all-langpacks-2.34-117.amzn2023.0.1  |
| glibc-common-2.34-117.amzn2023.0.1  |
| glibc-locale-source-2.34-117.amzn2023.0.1 |
| glibc-2.34-117.amzn2023.0.1  |
| kernel-libbpf-6.1.115-126.197.amzn2023  |
| kernel-livepatch-repo-s3-2023.6.20241111-0.amzn2023  |
| kernel-6.1.115-126.197.amzn2023 |
| python3-idna-2.10-3.amzn2023.0.3  |
| python3-pip-wheel-21.3.1-2.amzn2023.0.9  |
| selinux-policy-targeted-38.1.47-1.amzn2023.0.1  |
| selinux-policy-38.1.47-1.amzn2023.0.1  |
| system-release-2023.6.20241111-0.amzn2023  |
| vim-data-2:9.1.785-1.amzn2023.0.1  |
| vim-minimal-2:9.1.785-1.amzn2023.0.1 |

## Minimal container image
<a name="amis-2023.6.20241111.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20241111-0.amzn2023  |
| glibc-common-2.34-117.amzn2023.0.1  |
| glibc-minimal-langpack-2.34-117.amzn2023.0.1 |
| glibc-2.34-117.amzn2023.0.1  |
| system-release-2023.6.20241111-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20241111.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
