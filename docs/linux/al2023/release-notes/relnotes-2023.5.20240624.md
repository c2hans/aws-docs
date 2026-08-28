---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240624.html
---

# Amazon Linux 2023 version 2023.5.20240624 release notes
<a name="relnotes-2023.5.20240624"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240624.

**Topics**
+ [Major updates](#major-updates-2023.5.20240624)
+ [Repository](#amis-2023.5.20240624.repository)
+ [Docker container image](#amis-2023.5.20240624.container-image)
+ [Default AMI](#amis-2023.5.20240624.default-ami)
+ [Minimal AMI](#amis-2023.5.20240624.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240624.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240624.contact-us)

## Major updates
<a name="major-updates-2023.5.20240624"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240624.repository"></a>

### New packages in AL2023.5.20240624 since AL2023.4.20240611
<a name="new-AL2023.4.20240611-AL2023.5.20240624"></a>

 Comparing AL2023.4.20240611 version 2023.4.20240611 to AL2023.5.20240624 version [2023.5.20240624](#relnotes-2023.5.20240624).

| Package Type | Number of new packages in AL2023.5.20240624 compared to AL2023.4.20240611 |
| --- | --- |
| Source RPMs | 13 |
| Total Binary RPMs | 113 |
|  noarch binary RPMs | 17 |
|  x86\_64 binary RPMs | 48 |
|  aarch64 binary RPMs | 48 |

New packages in AL2023.5.20240624:

- ** `certmonger` **
  - **RPM:**  certmonger
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.79.18-2.amzn2023.0.1

- ** `dotnet8.0` **
  - **RPM:**  aspnetcore-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-8.0  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.0.5-1.amzn2023

- ** `freeipa` **
  - **RPM:**  freeipa-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-client-common  / **Architectures:** noarch
  - **RPM:**  freeipa-client-epn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-client-samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipa-common  / **Architectures:** noarch
  - **RPM:**  freeipa-python-compat  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux-luna  / **Architectures:** noarch
  - **RPM:**  freeipa-selinux-nfast  / **Architectures:** noarch
  - **RPM:**  python3-ipaclient  / **Architectures:** noarch
  - **RPM:**  python3-ipalib  / **Architectures:** noarch
  - **RPM:**  python3-ipatests  / **Architectures:** noarch
  - **Version:** 4.12.0-1.amzn2023.0.1

- ** [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-modphp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-zip  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.3.7-1.amzn2023.0.1

- ** `python-deprecated` **
  - **RPM:**  python3-deprecated
  - **Architectures:** noarch
  - **Version:** 1.2.14-3.amzn2023

- ** `python-ifaddr` **
  - **RPM:**  python3-ifaddr
  - **Architectures:** noarch
  - **Version:** 0.1.7-11.amzn2023

- ** `python-jwcrypto` **
  - **RPM:**  python3-jwcrypto
  - **Architectures:** noarch
  - **Version:** 1.4.2-46.amzn2023

- ** `python-ldap` **
  - **RPM:**  python3-ldap
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.4.4-103.amzn2023

- ** `python-pypng` **
  - **RPM:**  python3-pypng
  - **Architectures:** noarch
  - **Version:** 0.0.21-6.amzn2023

- ** `python-qrcode` **
  - **RPM:**  python3-qrcode
  - **Architectures:** noarch
  - **Version:** 7.4.2-55.amzn2023

- ** `python-wrapt` **
  - **RPM:**  python3-wrapt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-wrapt-doc  / **Architectures:** noarch
  - **Version:** 1.15.0-70.amzn2023.0.1

- ** `python-yubico` **
  - **RPM:**  python3-yubico
  - **Architectures:** noarch
  - **Version:** 1.3.3-13.amzn2023

- ** `pyusb` **
  - **RPM:**  python3-pyusb
  - **Architectures:** noarch
  - **Version:** 1.2.1-7.amzn2023.0.1

### AL2023.5.20240624 upgrades from AL2023.4.20240611
<a name="vercmp-AL2023.4.20240611-AL2023.5.20240624"></a>

 Comparing [2023.4.20240611](relnotes-2023.4.20240611.md) to [2023.5.20240624](#relnotes-2023.5.20240624).

| Package Type | Count |
| --- | --- |
| Source | 14 |
| Total Binary | 222 |
|  noarch binary RPMs | 56 |
|  x86\_64 binary RPMs | 83 |
|  aarch64 binary RPMs | 83 |

The full comparison of RPM package versions is below.

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 2.15.3-1.amzn2023.0.3
  - **AL2023.5.20240624 version:** 2.15.3-1.amzn2023.0.4

- ** `authselect` **
  - **RPM:**  authselect  / **Architectures:** aarch64, x86\_64
  - **RPM:**  authselect-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  authselect-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  authselect-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 1.2.3-1.amzn2023.0.2
  - **AL2023.5.20240624 version:** 1.2.5-1.amzn2023.0.1

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 1.3.0-0.amzn2023
  - **AL2023.5.20240624 version:** 1.3.1-0.amzn2023

- ** `BabelfishDump` **
  - **RPM:**  BabelfishDump
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 16.3-1.amzn2023.0.1
  - **AL2023.5.20240624 version:** 16.3-2.amzn2023.0.1

- ** `dotnet8.0` (`dotnet6.0` in AL2023.4.20240611) **
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 6.0.129-1.amzn2023.0.1
  - **AL2023.5.20240624 version:** 8.0.105-1.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 1.83.0-1.amzn2023
  - **AL2023.5.20240624 version:** 1.84.0-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** v1.27.3.0-1.amzn2023
  - **AL2023.5.20240624 version:** v1.29.5.0-1.amzn2023

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.4.20240611 version:** 1.22.3-1.amzn2023.0.1
  - **AL2023.5.20240624 version:** 1.22.4-1.amzn2023.0.1

- ** `grubby` **
  - **RPM:**  grubby
  - **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 8.40-51.amzn2023.0.4
  - **AL2023.5.20240624 version:** 8.40-73.amzn2023.0.1

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
  - **AL2023.4.20240611 version:** 6.1.92-99.174.amzn2023
  - **AL2023.5.20240624 version:** 6.1.94-99.176.amzn2023

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-10.2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 18.18.2-1.amzn2023.0.4
  - **AL2023.5.20240624 version:** 18.18.2-1.amzn2023.0.5

- ** `python-jinja2` **
  - **RPM:**  python3-jinja2
  - **Architectures:** noarch
  - **AL2023.4.20240611 version:** 2.11.3-1.amzn2023.0.3
  - **AL2023.5.20240624 version:** 2.11.3-1.amzn2023.0.4

- ** `sssd` **
  - **RPM:**  libipa\_hbac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libipa\_hbac-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_autofs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_certmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_certmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_idmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_nss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_nss\_idmap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_simpleifp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_simpleifp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsss\_sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libipa\_hbac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libsss\_nss\_idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-sss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-sssdconfig  / **Architectures:** noarch
  - **RPM:**  python3-sss-murmur  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common-pac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-idp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ipa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-kcm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-nfs-idmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-proxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-winbind-idmap  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 2.9.4-1.amzn2023.0.1
  - **AL2023.5.20240624 version:** 2.9.4-1.amzn2023.0.2

- ** `systemd` **
  - **RPM:**  systemd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-boot-unsigned  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-container  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-journal-remote  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-networkd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-oomd-defaults  / **Architectures:** noarch
  - **RPM:**  systemd-pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-resolved  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-rpm-macros  / **Architectures:** noarch
  - **RPM:**  systemd-standalone-sysusers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-standalone-tmpfiles  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-udev  / **Architectures:** aarch64, x86\_64
  - **AL2023.4.20240611 version:** 252.16-1.amzn2023.0.2
  - **AL2023.5.20240624 version:** 252.23-2.amzn2023

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.4.20240611 version:** 2023.4.20240611-1.amzn2023
  - **AL2023.5.20240624 version:** 2023.5.20240624-0.amzn2023

## Docker container image
<a name="amis-2023.5.20240624.container-image"></a>
+ `amazon-linux-repo-cdn-2023.5.20240624-0.amzn2023`
+ `system-release-2023.5.20240624-0.amzn2023`

## Default AMI
<a name="amis-2023.5.20240624.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240624-0.amzn2023` |
| `grubby-8.40-73.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.5.20240624-0.amzn2023` |
| `kernel-tools-6.1.94-99.176.amzn2023` |
| `kernel-6.1.94-99.176.amzn2023` |
| `libsss_certmap-2.9.4-1.amzn2023.0.2` |
| `libsss_idmap-2.9.4-1.amzn2023.0.2` |
| `libsss_nss_idmap-2.9.4-1.amzn2023.0.2` |
| `libsss_sudo-2.9.4-1.amzn2023.0.2` |
| `python3-jinja2-2.11.3-1.amzn2023.0.4` |
| `sssd-client-2.9.4-1.amzn2023.0.2` |
| `sssd-common-2.9.4-1.amzn2023.0.2` |
| `sssd-kcm-2.9.4-1.amzn2023.0.2` |
| `sssd-nfs-idmap-2.9.4-1.amzn2023.0.2` |
| `system-release-2023.5.20240624-0.amzn2023` |
| `systemd-libs-252.23-2.amzn2023` |
| `systemd-networkd-252.23-2.amzn2023` |
| `systemd-pam-252.23-2.amzn2023` |
| `systemd-resolved-252.23-2.amzn2023` |
| `systemd-udev-252.23-2.amzn2023` |
| `systemd-252.23-2.amzn2023` |

## Minimal AMI
<a name="amis-2023.5.20240624.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240624-0.amzn2023` |
| `grubby-8.40-73.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.5.20240624-0.amzn2023` |
| `kernel-6.1.94-99.176.amzn2023` |
| `python3-jinja2-2.11.3-1.amzn2023.0.4` |
| `system-release-2023.5.20240624-0.amzn2023` |
| `systemd-libs-252.23-2.amzn2023` |
| `systemd-networkd-252.23-2.amzn2023` |
| `systemd-pam-252.23-2.amzn2023` |
| `systemd-resolved-252.23-2.amzn2023` |
| `systemd-udev-252.23-2.amzn2023` |
| `systemd-252.23-2.amzn2023` |

## Minimal container image
<a name="amis-2023.5.20240624.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.5.20240624-0.amzn2023`
+ `system-release-2023.5.20240624-0.amzn2023`

## Contact us
<a name="amis-2023.5.20240624.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
