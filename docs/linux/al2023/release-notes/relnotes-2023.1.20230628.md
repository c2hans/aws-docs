---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230628.html
---

# Amazon Linux 2023 version 2023.1.20230628 release notes
<a name="relnotes-2023.1.20230628"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes for the 2023.1.20230628 release.

## Major updates
<a name="major-updates-2023.1.20230628"></a>

This release represents the first quarterly update to AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [ Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/) for more information about UEFI Secure Boot in AL2023.

AL2023 includes the following major updates.
+ AL2023 now supports UEFI Secure Boot on Amazon EC2 instances that support the UEFI firmware. For more information, see [UEFI Secure Boot](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html).
+ We added PHP 8.2 to this release of AL2023.
+ The [CIS Amazon Linux Benchmarks](https://www.cisecurity.org/benchmark/amazon_linux) now also includes one for AL2023, and is available from [CIS WorkBench](https://workbench.cisecurity.org/) (log in is required).
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ The kernel in this version of AL2023 (kernel-6.1.34-56.100.amzn2023) panics and fails to boot when fips mode is enabled. The Amazon Linux team is working on a fix for this issue.

  **Work-Around** - Avoid enabling fips mode until this issue is resolved.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information about the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated Amazon Web Services representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230628)
+ [Repository](#amis-2023.1.20230628.repository)
+ [Docker container image](#amis-2023.1.20230628.container-image)
+ [Default AMI](#amis-2023.1.20230628.default-ami)
+ [Minimal AMI](#amis-2023.1.20230628.minimal-ami)

## Repository
<a name="amis-2023.1.20230628.repository"></a>

### New packages in AL2023.1.20230628 since AL2023.0.20230614
<a name="new-AL2023.0.20230614-AL2023.1.20230628"></a>

 Comparing AL2023.0.20230614 version 2023.0.20230614 to AL2023.1.20230628 version [2023.1.20230628](#relnotes-2023.1.20230628).

| Package Type | Number of new packages in AL2023.1.20230628 compared to AL2023.0.20230614 |
| --- | --- |
| Source RPMs | 17 |
| Total Binary RPMs | 102 |
|  noarch binary RPMs | 6 |
|  x86\_64 binary RPMs | 48 |
|  aarch64 binary RPMs | 48 |

New packages in AL2023.1.20230628:

- ** [https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)
  - **Architectures:** noarch
  - **Version:** 2023.1-1.amzn2023.0.3

- ** `haproxy` **
  - **RPM:**  haproxy
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.8.0-1.amzn2023.0.1

- ** `hdparm` **
  - **RPM:**  hdparm
  - **Architectures:** aarch64, x86\_64
  - **Version:** 9.65-1.amzn2023.0.1

- ** `ipvsadm` **
  - **RPM:**  ipvsadm
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.31-9.amzn2023.0.1

- ** `iscsi-initiator-utils` **
  - **RPM:**  iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-iscsiuio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **Version:** 6.2.1.4-10.git2a8f9d8.amzn2023

- ** `isns-utils` **
  - **RPM:**  isns-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  isns-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  isns-utils-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.101-6.amzn2023

- ** `keepalived` **
  - **RPM:**  keepalived
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.2.7-6.amzn2023.0.1

- ** `libgit2` **
  - **RPM:**  libgit2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgit2-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.6.4-114.amzn2023.0.1

- ** `libiscsi` **
  - **RPM:**  libiscsi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libiscsi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libiscsi-utils  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.19.0-7.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.1.16-1.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  php8.2-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.2.7-1.amzn2023.0.1

- ** `python-configshell` **
  - **RPM:**  python3-configshell
  - **Architectures:** noarch
  - **Version:** 1.1.29-10.amzn2023

- ** `python-linux-procfs` **
  - **RPM:**  python3-linux-procfs
  - **Architectures:** noarch
  - **Version:** 0.7.1-1.amzn2023.0.1

- ** `python-uefivars` **
  - **RPM:**  python3-uefivars
  - **Architectures:** noarch
  - **Version:** 1.0.0-1.amzn2023.0.1

- ** `python-urwid` **
  - **RPM:**  python3-urwid
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.1.2-5.amzn2023

- ** `smartmontools` **
  - **RPM:**  smartmontools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  smartmontools-selinux  / **Architectures:** noarch
  - **Version:** 7.2-11.amzn2023.0.1

- ** `targetcli` **
  - **RPM:**  targetcli
  - **Architectures:** noarch
  - **Version:** 2.1.54-7.amzn2023

- ** `virt-what` **
  - **RPM:**  virt-what
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.25-2.amzn2023.0.1

### AL2023.1.20230628 upgrades from AL2023.0.20230614
<a name="vercmp-AL2023.0.20230614-AL2023.1.20230628"></a>

 Comparing [2023.0.20230614](relnotes-2023.0.20230614.md) to [2023.1.20230628](#relnotes-2023.1.20230628).

| Package Type | Count |
| --- | --- |
| Source | 28 |
| Total Binary | 1110 |
|  noarch binary RPMs | 408 |
|  x86\_64 binary RPMs | 352 |
|  aarch64 binary RPMs | 350 |

The full comparison of RPM package versions is below.

- ** [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 2.39-6.amzn2023.0.5
  - **AL2023.1.20230628 version:** 2.39-6.amzn2023.0.6

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 2.3.3op2-18.amzn2023.0.3
  - **AL2023.1.20230628 version:** 2.3.3op2-18.amzn2023.0.4

- ** `cups-filters` **
  - **RPM:**  cups-filters  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 1.28.10-1.amzn2023.0.2
  - **AL2023.1.20230628 version:** 1.28.16-3.amzn2023.0.1

- ** `dbus` **
  - **RPM:**  dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-common  / **Architectures:** noarch
  - **RPM:**  dbus-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-doc  / **Architectures:** noarch
  - **RPM:**  dbus-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-x11  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 1.12.24-1.amzn2023.0.2
  - **AL2023.1.20230628 version:** 1.12.28-1.amzn2023.0.1

- ** `dnf-plugin-support-info` **
  - **RPM:**  dnf-plugin-support-info
  - **Architectures:** noarch
  - **AL2023.0.20230614 version:** 1.1-1.amzn2023
  - **AL2023.1.20230628 version:** 1.2-1.amzn2023

- ** `dracut` **
  - **RPM:**  dracut  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-caps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-generic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-rescue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-squash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 055-6.amzn2023.0.6
  - **AL2023.1.20230628 version:** 055-6.amzn2023.0.7

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 1.71.2-1.amzn2023
  - **AL2023.1.20230628 version:** 1.72.0-1.amzn2023

- ** `glib2` **
  - **RPM:**  glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-doc  / **Architectures:** noarch
  - **RPM:**  glib2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 2.73.2-680.amzn2023.0.3
  - **AL2023.1.20230628 version:** 2.74.7-688.amzn2023.0.1

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
  - **RPM:**  sysroot-i386-fc34-glibc  / **Architectures:** noarch
  - **RPM:**  sysroot-x86\_64-fc34-glibc  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 2.34-52.amzn2023.0.2
  - **AL2023.1.20230628 version:** 2.34-52.amzn2023.0.3

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
  - **AL2023.0.20230614 version:** 2.06-61.amzn2023.0.6
  - **AL2023.1.20230628 version:** 2.06-61.amzn2023.0.7

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
  - **AL2023.0.20230614 version:** 6.1.29-50.88.amzn2023
  - **AL2023.1.20230628 version:** 6.1.34-56.100.amzn2023

- ** `kpatch` **
  - **RPM:**  kpatch-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-dnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-runtime  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 0.9.7-10.amzn2023.0.1
  - **AL2023.1.20230628 version:** 0.9.7-12.amzn2023.0.3

- ** `libeconf` **
  - **RPM:**  libeconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libeconf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libeconf-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 0.4.0-1.amzn2023.0.2
  - **AL2023.1.20230628 version:** 0.4.0-1.amzn2023.0.3

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 4.4.0-4.amzn2023.0.4
  - **AL2023.1.20230628 version:** 4.4.0-4.amzn2023.0.5

- ** `ncurses` **
  - **RPM:**  ncurses  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-base  / **Architectures:** noarch
  - **RPM:**  ncurses-c\+\+-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-compat-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-term  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 6.2-4.20200222.amzn2023.0.3
  - **AL2023.1.20230628 version:** 6.2-4.20200222.amzn2023.0.4

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 18.12.1-1.amzn2023.0.4
  - **AL2023.1.20230628 version:** 18.12.1-1.amzn2023.0.5

- ** `openldap` **
  - **RPM:**  openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-servers  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 2.4.57-6.amzn2023.0.4
  - **AL2023.1.20230628 version:** 2.4.57-6.amzn2023.0.5

- ** `opensmtpd` **
  - **RPM:**  opensmtpd
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 6.8.0p2-2.amzn2023.0.3
  - **AL2023.1.20230628 version:** 6.8.0p2-11.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 3.0.8-1.amzn2023.0.2
  - **AL2023.1.20230628 version:** 3.0.8-1.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/perl.html](https://docs.aws.amazon.com/linux/al2023/ug/perl.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/perl.html](https://docs.aws.amazon.com/linux/al2023/ug/perl.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Attribute-Handlers  / **Architectures:** noarch
  - **RPM:**  perl-AutoLoader  / **Architectures:** noarch
  - **RPM:**  perl-AutoSplit  / **Architectures:** noarch
  - **RPM:**  perl-autouse  / **Architectures:** noarch
  - **RPM:**  perl-B  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-base  / **Architectures:** noarch
  - **RPM:**  perl-Benchmark  / **Architectures:** noarch
  - **RPM:**  perl-blib  / **Architectures:** noarch
  - **RPM:**  perl-Class-Struct  / **Architectures:** noarch
  - **RPM:**  perl-Config-Extensions  / **Architectures:** noarch
  - **RPM:**  perl-DBM\_Filter  / **Architectures:** noarch
  - **RPM:**  perl-debugger  / **Architectures:** noarch
  - **RPM:**  perl-deprecate  / **Architectures:** noarch
  - **RPM:**  perl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Devel-Peek  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Devel-SelfStubber  / **Architectures:** noarch
  - **RPM:**  perl-diagnostics  / **Architectures:** noarch
  - **RPM:**  perl-DirHandle  / **Architectures:** noarch
  - **RPM:**  perl-doc  / **Architectures:** noarch
  - **RPM:**  perl-Dumpvalue  / **Architectures:** noarch
  - **RPM:**  perl-DynaLoader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-encoding-warnings  / **Architectures:** noarch
  - **RPM:**  perl-English  / **Architectures:** noarch
  - **RPM:**  perl-Errno  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-ExtUtils-Constant  / **Architectures:** noarch
  - **RPM:**  perl-ExtUtils-Embed  / **Architectures:** noarch
  - **RPM:**  perl-ExtUtils-Miniperl  / **Architectures:** noarch
  - **RPM:**  perl-Fcntl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-fields  / **Architectures:** noarch
  - **RPM:**  perl-File-Basename  / **Architectures:** noarch
  - **RPM:**  perl-FileCache  / **Architectures:** noarch
  - **RPM:**  perl-File-Compare  / **Architectures:** noarch
  - **RPM:**  perl-File-Copy  / **Architectures:** noarch
  - **RPM:**  perl-File-DosGlob  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-File-Find  / **Architectures:** noarch
  - **RPM:**  perl-FileHandle  / **Architectures:** noarch
  - **RPM:**  perl-File-stat  / **Architectures:** noarch
  - **RPM:**  perl-filetest  / **Architectures:** noarch
  - **RPM:**  perl-FindBin  / **Architectures:** noarch
  - **RPM:**  perl-GDBM\_File  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Getopt-Std  / **Architectures:** noarch
  - **RPM:**  perl-Hash-Util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Hash-Util-FieldHash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-I18N-Collate  / **Architectures:** noarch
  - **RPM:**  perl-I18N-Langinfo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-I18N-LangTags  / **Architectures:** noarch
  - **RPM:**  perl-if  / **Architectures:** noarch
  - **RPM:**  perl-interpreter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-IO  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-IPC-Open3  / **Architectures:** noarch
  - **RPM:**  perl-less  / **Architectures:** noarch
  - **RPM:**  perl-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-libnetcfg  / **Architectures:** noarch
  - **RPM:**  perl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-locale  / **Architectures:** noarch
  - **RPM:**  perl-Locale-Maketext-Simple  / **Architectures:** noarch
  - **RPM:**  perl-macros  / **Architectures:** noarch
  - **RPM:**  perl-Math-Complex  / **Architectures:** noarch
  - **RPM:**  perl-Memoize  / **Architectures:** noarch
  - **RPM:**  perl-meta-notation  / **Architectures:** noarch
  - **RPM:**  perl-Module-Loaded  / **Architectures:** noarch
  - **RPM:**  perl-mro  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-NDBM\_File  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Net  / **Architectures:** noarch
  - **RPM:**  perl-NEXT  / **Architectures:** noarch
  - **RPM:**  perl-ODBM\_File  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Opcode  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-open  / **Architectures:** noarch
  - **RPM:**  perl-overload  / **Architectures:** noarch
  - **RPM:**  perl-overloading  / **Architectures:** noarch
  - **RPM:**  perl-ph  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Pod-Functions  / **Architectures:** noarch
  - **RPM:**  perl-Pod-Html  / **Architectures:** noarch
  - **RPM:**  perl-POSIX  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Safe  / **Architectures:** noarch
  - **RPM:**  perl-Search-Dict  / **Architectures:** noarch
  - **RPM:**  perl-SelectSaver  / **Architectures:** noarch
  - **RPM:**  perl-SelfLoader  / **Architectures:** noarch
  - **RPM:**  perl-sigtrap  / **Architectures:** noarch
  - **RPM:**  perl-sort  / **Architectures:** noarch
  - **RPM:**  perl-subs  / **Architectures:** noarch
  - **RPM:**  perl-Symbol  / **Architectures:** noarch
  - **RPM:**  perl-Sys-Hostname  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Term-Complete  / **Architectures:** noarch
  - **RPM:**  perl-Term-ReadLine  / **Architectures:** noarch
  - **RPM:**  perl-Test  / **Architectures:** noarch
  - **RPM:**  perl-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Text-Abbrev  / **Architectures:** noarch
  - **RPM:**  perl-Thread  / **Architectures:** noarch
  - **RPM:**  perl-Thread-Semaphore  / **Architectures:** noarch
  - **RPM:**  perl-Tie  / **Architectures:** noarch
  - **RPM:**  perl-Tie-File  / **Architectures:** noarch
  - **RPM:**  perl-Tie-Memoize  / **Architectures:** noarch
  - **RPM:**  perl-Time  / **Architectures:** noarch
  - **RPM:**  perl-Time-Piece  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Unicode-UCD  / **Architectures:** noarch
  - **RPM:**  perl-User-pwent  / **Architectures:** noarch
  - **RPM:**  perl-utils  / **Architectures:** noarch
  - **RPM:**  perl-vars  / **Architectures:** noarch
  - **RPM:**  perl-vmsish  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 5.32.1-477.amzn2023.0.4
  - **AL2023.1.20230628 version:** 5.32.1-477.amzn2023.0.5

- ** `perl-HTTP-Tiny` **
  - **RPM:**  perl-HTTP-Tiny  / **Architectures:** noarch
  - **RPM:**  perl-HTTP-Tiny-tests  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 0.078-1.amzn2023.0.2
  - **AL2023.1.20230628 version:** 0.078-1.amzn2023.0.3

- ** `perl-Pod-Perldoc` **
  - **RPM:**  perl-Pod-Perldoc
  - **Architectures:** noarch
  - **AL2023.0.20230614 version:** 3.28.01-459.amzn2023.0.2
  - **AL2023.1.20230628 version:** 3.28.01-459.amzn2023.0.3

- ** `pesign` **
  - **RPM:**  pesign
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 116-2.amzn2023.0.1
  - **AL2023.1.20230628 version:** 116-2.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 8.1.16-1.amzn2023.0.1
  - **AL2023.1.20230628 version:** 8.1.16-1.amzn2023.0.2

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 1.1.5-1.amzn2023.0.1
  - **AL2023.1.20230628 version:** 1.1.7-1.amzn2023.0.1

- ** `screen` **
  - **RPM:**  screen
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 4.8.0-5.amzn2023.0.2
  - **AL2023.1.20230628 version:** 4.8.0-5.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230614 version:** 2023.0.20230614-0.amzn2023
  - **AL2023.1.20230628 version:** 2023.1.20230628-0.amzn2023

- ** `yajl` **
  - **RPM:**  yajl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yajl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230614 version:** 2.1.0-16.amzn2023.0.2
  - **AL2023.1.20230628 version:** 2.1.0-16.amzn2023.0.3

## Docker container image
<a name="amis-2023.1.20230628.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230628-0.amzn2023`
+ `glib2-2.74.7-688.amzn2023.0.1`
+ `glibc-common-2.34-52.amzn2023.0.3`
+ `glibc-minimal-langpack-2.34-52.amzn2023.0.3`
+ `glibc-2.34-52.amzn2023.0.3`
+ `ncurses-base-6.2-4.20200222.amzn2023.0.4`
+ `openssl-libs-1:3.0.8-1.amzn2023`
+ `system-release-2023.1.20230628-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230628.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230628-0.amzn2023` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.3` |
| `binutils-2.39-6.amzn2023.0.6` |
| `dbus-common-1:1.12.28-1.amzn2023.0.1` |
| `dbus-libs-1:1.12.28-1.amzn2023.0.1` |
| `dbus-1:1.12.28-1.amzn2023.0.1` |
| `dnf-plugin-support-info-1.2-1.amzn2023` |
| `dracut-config-generic-055-6.amzn2023.0.7` |
| `dracut-055-6.amzn2023.0.7` |
| `efivar-libs-38-2.amzn2023.0.1` |
| `efivar-38-2.amzn2023.0.1` |
| `glib2-2.74.7-688.amzn2023.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.3` |
| `glibc-common-2.34-52.amzn2023.0.3` |
| `glibc-gconv-extra-2.34-52.amzn2023.0.3` |
| `glibc-locale-source-2.34-52.amzn2023.0.3` |
| `glibc-2.34-52.amzn2023.0.3` |
| `grub2-common-1:2.06-61.amzn2023.0.7` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.7` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.7` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.7` |
| `grub2-tools-1:2.06-61.amzn2023.0.7` |
| `kernel-livepatch-repo-s3-2023.1.20230628-0` |
| `kernel-tools-6.1.34-56.100.amzn2023` |
| `kernel-tools-6.1.34-56.100.amzn2023`x |
| `kpatch-runtime-0.9.7-12.amzn2023.0.3` |
| `libeconf-0.4.0-1.amzn2023.0.3` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.4` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.4` |
| `ncurses-6.2-4.20200222.amzn2023.0.4` |
| `openldap-2.4.57-6.amzn2023.0.5` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.3` |
| `openssl-1:3.0.8-1.amzn2023.0.3` |
| `perl-Class-Struct-0.66-477.amzn2023.0.5` |
| `perl-DynaLoader-1.47-477.amzn2023.0.5` |
| `perl-Errno-1.30-477.amzn2023.0.5` |
| `perl-Fcntl-1.13-477.amzn2023.0.5` |
| `perl-File-Basename-2.85-477.amzn2023.0.5` |
| `perl-File-stat-1.09-477.amzn2023.0.5` |
| `perl-Getopt-Std-1.12-477.amzn2023.0.5` |
| `perl-HTTP-Tiny-0.078-1.amzn2023.0.3` |
| `perl-IO-1.43-477.amzn2023.0.5` |
| `perl-IPC-Open3-1.21-477.amzn2023.0.5` |
| `perl-POSIX-1.94-477.amzn2023.0.5` |
| `perl-Pod-Perldoc-3.28.01-459.amzn2023.0.3` |
| `perl-SelectSaver-1.02-477.amzn2023.0.5` |
| `perl-Symbol-1.08-477.amzn2023.0.5` |
| `perl-if-0.60.800-477.amzn2023.0.5` |
| `perl-interpreter-4:5.32.1-477.amzn2023.0.5` |
| `perl-libs-4:5.32.1-477.amzn2023.0.5` |
| `perl-mro-1.23-477.amzn2023.0.5` |
| `perl-overload-1.31-477.amzn2023.0.5` |
| `perl-overloading-0.02-477.amzn2023.0.5` |
| `perl-subs-1.03-477.amzn2023.0.5` |
| `perl-vars-1.05-477.amzn2023.0.5` |
| `sbsigntools-0.9.4-8.amzn2023.0.2` |
| `screen-4.8.0-5.amzn2023.0.3` |
| `system-release-2023.1.20230628-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.1.20230628.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230628-0.amzn2023` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.3` |
| `dbus-common-1:1.12.28-1.amzn2023.0.1` |
| `dbus-libs-1:1.12.28-1.amzn2023.0.1` |
| `dbus-1:1.12.28-1.amzn2023.0.1` |
| `dnf-plugin-support-info-1.2-1.amzn2023` |
| `dracut-config-generic-055-6.amzn2023.0.7` |
| `dracut-055-6.amzn2023.0.7` |
| `efivar-libs-38-2.amzn2023.0.1` |
| `efivar-38-2.amzn2023.0.1` |
| `glib2-2.74.7-688.amzn2023.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2023.0.3` |
| `glibc-common-2.34-52.amzn2023.0.3` |
| `glibc-locale-source-2.34-52.amzn2023.0.3` |
| `glibc-2.34-52.amzn2023.0.3` |
| `grub2-common-1:2.06-61.amzn2023.0.7` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.7` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.7` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.7` |
| `grub2-tools-1:2.06-61.amzn2023.0.7` |
| `kernel-livepatch-repo-s3-2023.1.20230628-0` |
| `kernel-6.1.34-56.100.amzn2023`x |
| `libeconf-0.4.0-1.amzn2023.0.3` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.4` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.4` |
| `ncurses-6.2-4.20200222.amzn2023.0.4` |
| `openldap-2.4.57-6.amzn2023.0.5` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.3` |
| `openssl-1:3.0.8-1.amzn2023.0.3` |
| `sbsigntools-0.9.4-8.amzn2023.0.2` |
| `system-release-2023.1.20230628-0.amzn2023` |
