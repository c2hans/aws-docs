---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20230920.html
---

# Amazon Linux 2023 version 2023.2.20230920 release notes
<a name="relnotes-2023.2.20230920"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.2.20230920 release

## Major updates
<a name="major-updates-2023.2.20230920"></a>

This release represents the second quarterly update to AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

This new quarterly update of AL2023 (2023.2) includes the following updates from the previous quarterly release (2023.1).
+ Improvements for memory constrained instance types.
  + Out Of memory conditions on `nano` instances are partially mitigated by the addition of `zram` by default (compressed swap to RAM) on instances with less than 1 GB of memory.
  + For instance types with less than 800 MB of RAM, we now enable `zram` based swap by default. Examples of this instance type include `t4g.nano`, `t3a.nano`, `t3.nano`, `t2.nano`, and `t1.micro`. This means fewer out of memory scenarios for these instance types, because AL2023 will on-demand compress and decompress memory pages. This enables workloads that would otherwise require an instance type with more memory, at the expense of CPU usage needed to do the compression.
  + This feature is enabled by default on new AMIs. If you are upgrading an instance from a previously launched AMI, you can enable this feature by running the following command, and then rebooting the instance.

    ```
    dnf install -y zram-generator zram-generator-defaults
    ```
  + This feature is available on other instance types, but it isn't enabled by default on instance types with greater than 800 MB of RAM.
+ A new [Minimal Container Image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html).
  + This image differs from the standard [Base Container Image](https://docs.aws.amazon.com/linux/al2023/ug/base-container.html) because it contains only the bare minimum packages needed to install other packages. The base container image aims to be minimal but also broadly compatible with the [Minimal AMI](https://docs.aws.amazon.com/linux/al2023/ug/AMI-minimal-and-standard-differences.html). A notable difference in the AL2023 [Minimal Container Image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html) is using `microdnf` to provide the `dnf` package manager. This enables the image to be smaller (and still able to install other software) with the trade-off of not having the full feature set of the `dnf` package manager as present in other AL2023 images.
+ Although AL2023 is not yet FIPS certified, enabling FIPS mode is now supported. For more information, see [Enable FIPS mode](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html).
+ New packages were added.
  + Ansible has been added to AL2023 as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/57)
  + flatpak - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/349)
  + atop - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/306)
  + composer - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/371)
  + fping
  + git-lfs - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/365)
  + google-authenticator - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/307)
  + Corretto 21 - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/449)
  + kstart
  + libmemcached-awesome - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/208)
  + libsodium - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/377)
  + lttng-tools
  + mutt - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/318)
  + nethogs - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/331)
  + oath-toolkit
  + php8.2-zip - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/195)
  + php8.2-sodium - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/204)
  + postgresql-odbc
  + pwgen - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/374)
  + sshpass - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/338)
  + s-nail
+ The `mmtaghostname` plugin for `rsyslog` was added in `rsyslog-mmtaghostname` - as requested in [GitHub](https://github.com/amazonlinux/amazon-linux-2023/issues/122).
+ Kernel live patches now work with UEFI Secure Boot.
+ For an in-depth look at the changes since AL2, see [Comparing Amazon Linux 2 and Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ `libffi` was updated to a newer version to solve a number of `aarch64` related issues. This update requires a shared library version (so-name) bump. The new version is `libffi.so.8`. The old version is `libffi.so.6` and will remain available (and if needed, security patched) with a `compat-libffi3.1` package at least until the next quarterly release (AL2023.3). Customers building software on top of AL2023 that uses `libffi` are advised to rebuild against this updated version. All packages in AL2023 with dependencies on the old version of library were rebuilt in AL2023.2 to link to the updated version.
+ amazon-cloudwatch-agent updated to 1.300026.3-2.amzn2023
+ amazon-ecr-credential-helper updated to 0.7.1
+ amazon-ssm-agent updated from 3.1.1927 to 3.2.1377
+ bind updated from 9.16.38 to 9.16.42
+ cairo updated from 1.17.4 to 1.17.6 and cairomm from 1.14.2 to 1.14.4
+ clamav updated from 0.103.8 to 0.103.9
+ clang updated from 15.0.6 to 15.0.7
+ collectd-java is now compatible with Java 8 and Java 11, not only Java 17
+ containerd updated from 1.6.19 to 1.7.2
+ Docker 24
+ curl updated from 8.0.1 to 8.2.1
+ dmidecode updated from 3.3 to 3.5
+ dnsmasq updated from 2.86 to 2.89
+ dotnet 6.0 updated to 6.0.121 and dotnet-runtime-6.0 from 6.0.11 to 6.0.21
+ ecs-init updated from 1.72 to 1.75
+ ecs-service-connect-agent updated from 1.25.4.0 to 1.27
+ GCC 11.3.1 to 11.4.1
+ Golang 1.19.9 updated to 1.20.7
+ Updates to Corretto 8, 11, and 17
+ krb5 updated from 1.20.1 to 1.21
+ MariaDB 10.5.18 updated to 10.5.20
+ NodeJS 18 updated from 18.12.1 to 18.17.1
+ nss updated from 3.88 to 3.90
+ PHP8.1 updated from 8.1.16 to 8.1.23
+ PHP8.2 updated from 8.2.7 to 8.2.9 and the php-zip and php-sodium modules were added
+ Redis 6 updated from 6.2.12 to 6.2.13
+ Samba updated from 4.17.8 to 4.17.10
+ systemd updated from 252.4 to 252.16 with several bug fixes, including a bug fix for Out-of-Memory (OOM) handling inside a cgroup that meant all processes in the cgroup were always killed instead of the intended behavior of the OOM-Killer choosing one process at a time.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

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
+ [Major updates](#major-updates-2023.2.20230920)
+ [Repository](#amis-2023.2.20230920.repository)
+ [Docker container image](#amis-2023.2.20230920.container-image)
+ [Default AMI](#2023.2.20230920.default-ami)
+ [Minimal AMI](#amis-2023.2.20230920.minimal-ami)
+ [Minimal container image](#amis-2023.2.20230920.minimal-container-ami)

## Repository
<a name="amis-2023.2.20230920.repository"></a>

### New packages in AL2023.2.20230920 since AL2023.1.20230912
<a name="new-AL2023.1.20230912-AL2023.2.20230920"></a>

 Comparing AL2023.1.20230912 version 2023.1.20230912 to AL2023.2.20230920 version [2023.2.20230920](#relnotes-2023.2.20230920).

| Package Type | Number of new packages in AL2023.2.20230920 compared to AL2023.1.20230912 |
| --- | --- |
| Source RPMs | 24 |
| Total Binary RPMs | 84 |
|  noarch binary RPMs | 14 |
|  x86\_64 binary RPMs | 35 |
|  aarch64 binary RPMs | 35 |

New packages in AL2023.2.20230920:

- ** `ansible` **
  - **RPM:**  ansible
  - **Architectures:** noarch
  - **Version:** 8.3.0-1.amzn2023.0.1

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.15.3-1.amzn2023.0.1

- ** `ansible-packaging` **
  - **RPM:**  ansible-packaging  / **Architectures:** noarch
  - **RPM:**  ansible-packaging-tests  / **Architectures:** noarch
  - **RPM:**  ansible-srpm-macros  / **Architectures:** noarch
  - **Version:** 1-11.amzn2023.0.1

- ** `atop` **
  - **RPM:**  atop
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.9.0-1.amzn2023

- ** `composer` **
  - **RPM:**  composer
  - **Architectures:** noarch
  - **Version:** 2.5.8-2.amzn2023

- ** `fping` **
  - **RPM:**  fping
  - **Architectures:** aarch64, x86\_64
  - **Version:** 5.1-3.amzn2023

- ** `google-authenticator` **
  - **RPM:**  google-authenticator
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.09-5.amzn2023

- ** `ipa-gothic-fonts` **
  - **RPM:**  ipa-gothic-fonts
  - **Architectures:** noarch
  - **Version:** 003.03-27.amzn2023

- ** `ipa-mincho-fonts` **
  - **RPM:**  ipa-mincho-fonts
  - **Architectures:** noarch
  - **Version:** 003.03-26.amzn2023

- ** `ipa-pgothic-fonts` **
  - **RPM:**  ipa-pgothic-fonts
  - **Architectures:** noarch
  - **Version:** 003.03-24.amzn2023

- ** `ipa-pmincho-fonts` **
  - **RPM:**  ipa-pmincho-fonts
  - **Architectures:** noarch
  - **Version:** 003.03-25.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **Version:** 21.0.0\+35-1.amzn2023.1

- ** `kstart` **
  - **RPM:**  kstart
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.3-4.amzn2023

- ** `libffi` **
  - **RPM:**  compat-libffi3.1
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.4.4-1.amzn2023.0.1

- ** `libmemcached-awesome` **
  - **RPM:**  libmemcached-awesome  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmemcached-awesome-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmemcached-awesome-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.4-2.amzn2023

- ** `libsodium` **
  - **RPM:**  libsodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-static  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.18-13.amzn2023.0.1

- ** `nethogs` **
  - **RPM:**  nethogs
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.8.7-3.amzn2023

- ** `oath-toolkit` **
  - **RPM:**  liboath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liboath-doc  / **Architectures:** noarch
  - **RPM:**  libpskc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpskc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpskc-doc  / **Architectures:** noarch
  - **RPM:**  oathtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_oath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pskctool  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.6.9-2.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/php.html](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  php8.2-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-zip  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.2.9-1.amzn2023.0.3

- ** `postgresql-odbc` **
  - **RPM:**  postgresql-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql-odbc-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 13.01.0000-5.amzn2023.0.1

- ** `pwgen` **
  - **RPM:**  pwgen
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.08-11.amzn2023

- ** `python-pkgconfig` **
  - **RPM:**  python3-pkgconfig
  - **Architectures:** noarch
  - **Version:** 1.5.5-7.amzn2023

- ** `rkhunter` **
  - **RPM:**  rkhunter
  - **Architectures:** noarch
  - **Version:** 1.4.6-22.amzn2023.0.1

- ** `rust-zram-generator` **
  - **RPM:**  zram-generator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zram-generator-defaults  / **Architectures:** noarch
  - **Version:** 1.1.2-67.amzn2023

- ** `s-nail` **
  - **RPM:**  s-nail
  - **Architectures:** aarch64, x86\_64
  - **Version:** 14.9.24-6.amzn2023

- ** `sshpass` **
  - **RPM:**  sshpass
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.09-6.amzn2023.0.1

- ** `systemd` **
  - **RPM:**  systemd-boot-unsigned
  - **Architectures:** aarch64, x86\_64
  - **Version:** 252.16-1.amzn2023.0.1

### AL2023.2.20230920 upgrades from AL2023.1.20230912
<a name="vercmp-AL2023.1.20230912-AL2023.2.20230920"></a>

 Comparing [2023.1.20230912](relnotes-2023.1.20230912.md) to [2023.2.20230920](#relnotes-2023.2.20230920).

| Package Type | Count |
| --- | --- |
| Source | 42 |
| Total Binary | 622 |
|  noarch binary RPMs | 148 |
|  x86\_64 binary RPMs | 238 |
|  aarch64 binary RPMs | 236 |

The full comparison of RPM package versions is below.

- ** `amazon-ecr-credential-helper` **
  - **RPM:**  amazon-ecr-credential-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 0.7.1-1.amzn2023
  - **AL2023.2.20230920 version:** 0.7.1-2.amzn2023

- ** `clang` **
  - **RPM:**  clang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-analyzer  / **Architectures:** noarch
  - **RPM:**  clang-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-resource-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-tools-extra-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-clang-format  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-clang  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-3.amzn2023.0.2
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2023.1.20230912 version:** 22.2.2-1.amzn2023.1.8
  - **AL2023.2.20230920 version:** 22.2.2-1.amzn2023.1.11

- ** `collectd` **
  - **RPM:**  collectd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-apache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-ceph  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-chrony  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-curl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-curl\_json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-curl\_xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-dbi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-disk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-dns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-drbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-email  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-generic-jmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-hugepages  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-iptables  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-log\_logstash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mcelog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mdevents  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-netlink  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-notify\_desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-notify\_email  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-postgresql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-python  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-rrdcached  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-rrdtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-sensors  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-smart  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-synproxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-web  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_http  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_prometheus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_sensu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_syslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_tsdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-zookeeper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcollectdclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcollectdclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Collectd  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 5.12.0-16.amzn2023.0.2
  - **AL2023.2.20230920 version:** 5.12.0-16.amzn2023.0.4

- ** `compiler-rt` **
  - **RPM:**  compiler-rt
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-2.amzn2023.0.1
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 20.10.25-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 24.0.5-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 1.75.0-1.amzn2023
  - **AL2023.2.20230920 version:** 1.75.3-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** v1.26.4.0-1.amzn2023
  - **AL2023.2.20230920 version:** v1.27.0.0-1.amzn2023

- ** `fonts-rpm-macros` **
  - **RPM:**  fonts-filesystem  / **Architectures:** noarch
  - **RPM:**  fonts-rpm-macros  / **Architectures:** noarch
  - **RPM:**  fonts-rpm-templates  / **Architectures:** noarch
  - **RPM:**  fonts-srpm-macros  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 2.0.5-5.amzn2023.0.2
  - **AL2023.2.20230920 version:** 2.0.5-12.amzn2023.0.2

- ** `gdk-pixbuf2` **
  - **RPM:**  gdk-pixbuf2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-modules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.42.6-1.amzn2023.0.3
  - **AL2023.2.20230920 version:** 2.42.10-1.amzn2023.0.1

- ** `glib2` **
  - **RPM:**  glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-doc  / **Architectures:** noarch
  - **RPM:**  glib2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.74.7-688.amzn2023.0.1
  - **AL2023.2.20230920 version:** 2.74.7-689.amzn2023.0.2

- ** `gobject-introspection` **
  - **RPM:**  gobject-introspection  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gobject-introspection-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 1.73.0-2.amzn2023.0.2
  - **AL2023.2.20230920 version:** 1.73.0-2.amzn2023.0.3

- ** `gsl` **
  - **RPM:**  gsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.6-4.amzn2023.0.3
  - **AL2023.2.20230920 version:** 2.6-4.amzn2023.0.4

- ** `guile22` **
  - **RPM:**  guile22  / **Architectures:** aarch64, x86\_64
  - **RPM:**  guile22-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.2.7-2.amzn2023.0.2
  - **AL2023.2.20230920 version:** 2.2.7-2.amzn2023.0.3

- ** `jna` **
  - **RPM:**  jna  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jna-contrib  / **Architectures:** noarch
  - **RPM:**  jna-javadoc  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 5.9.0-1.amzn2023.0.2
  - **AL2023.2.20230920 version:** 5.9.0-1.amzn2023.0.3

- ** `keepalived` **
  - **RPM:**  keepalived
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.2.7-6.amzn2023.0.1
  - **AL2023.2.20230920 version:** 2.2.7-6.amzn2023.0.2

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
  - **AL2023.1.20230912 version:** 6.1.49-70.116.amzn2023
  - **AL2023.2.20230920 version:** 6.1.52-71.125.amzn2023

- ** `libclc` **
  - **RPM:**  libclc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libclc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-1.amzn2023.0.3
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

- ** `libffi` **
  - **RPM:**  libffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libffi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 3.1-28.amzn2023.0.2
  - **AL2023.2.20230920 version:** 3.4.4-1.amzn2023.0.1

- ** `libgcrypt` **
  - **RPM:**  libgcrypt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcrypt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 1.10.1-7.amzn2023.0.1
  - **AL2023.2.20230920 version:** 1.10.2-1.amzn2023.0.1

- ** `libomp` **
  - **RPM:**  libomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libomp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libomp-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-1.amzn2023.0.3
  - **AL2023.2.20230920 version:** 15.0.7-5.amzn2023.0.1

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 4.4.0-4.amzn2023.0.13
  - **AL2023.2.20230920 version:** 4.4.0-4.amzn2023.0.14

- ** `lld` **
  - **RPM:**  lld  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lld-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lld-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-1.amzn2023.0.3
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

- ** `lldb` **
  - **RPM:**  lldb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lldb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-lldb  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-1.amzn2023.0.3
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-doc  / **Architectures:** noarch
  - **RPM:**  llvm-googletest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 15.0.6-2.amzn2023.0.2
  - **AL2023.2.20230920 version:** 15.0.7-3.amzn2023.0.1

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
  - **AL2023.1.20230912 version:** 10.5.18-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 10.5.20-1.amzn2023.0.1

- ** `nasm` **
  - **RPM:**  nasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nasm-doc  / **Architectures:** noarch
  - **RPM:**  nasm-rdoff  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 2.15.05-1.amzn2023.0.4
  - **AL2023.2.20230920 version:** 2.15.05-1.amzn2023.0.5

- ** `oci-add-hooks` **
  - **RPM:**  oci-add-hooks
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 0-0.1.20200504git268e3bb.amzn2023
  - **AL2023.2.20230920 version:** 0-0.1.20200504git268e3bb.amzn2023.0.1

- ** `open-vm-tools` **
  - **RPM:**  open-vm-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-salt-minion  / **Architectures:** x86\_64
  - **RPM:**  open-vm-tools-sdmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 12.2.5-1.amzn2023
  - **AL2023.2.20230920 version:** 12.3.0-1.amzn2023

- ** `p11-kit` **
  - **RPM:**  p11-kit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-trust  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 0.24.1-2.amzn2023.0.2
  - **AL2023.2.20230920 version:** 0.24.1-2.amzn2023.0.3

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
  - **RPM:**  php8.1-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.1-xml  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 8.1.22-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 8.1.23-1.amzn2023.0.1

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
  - **AL2023.1.20230912 version:** 8.2.9-1.amzn2023.0.2
  - **AL2023.2.20230920 version:** 8.2.9-1.amzn2023.0.3

- ** `pygobject3` **
  - **RPM:**  python3-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-gobject-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-gobject-base-noarch  / **Architectures:** noarch
  - **RPM:**  python3-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 3.42.2-2.amzn2023.0.2
  - **AL2023.2.20230920 version:** 3.42.2-2.amzn2023.0.3

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 3.11.2-2.amzn2023.0.10
  - **AL2023.2.20230920 version:** 3.11.2-2.amzn2023.0.11

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 3.9.16-1.amzn2023.0.5
  - **AL2023.2.20230920 version:** 3.9.16-1.amzn2023.0.6

- ** `python-cffi` **
  - **RPM:**  python3-cffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-cffi-doc  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 1.14.5-1.amzn2023.0.2
  - **AL2023.2.20230920 version:** 1.14.5-1.amzn2023.0.3

- ** `python-lit` **
  - **RPM:**  python3-lit
  - **Architectures:** noarch
  - **AL2023.1.20230912 version:** 15.0.6-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 15.0.7-2.amzn2023.0.1

- ** `ruby3.2` **
  - **RPM:**  ruby3.2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-bundled-gems  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-default-gems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-doc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bigdecimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bundler  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-io-console  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-irb  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-minitest  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-power\_assert  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-psych  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rake  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rdoc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rexml  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rss  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems-devel  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-test-unit  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-typeprof  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 3.2.2-180.amzn2023.0.1
  - **AL2023.2.20230920 version:** 3.2.2-180.amzn2023.0.2

- ** `systemd` **
  - **RPM:**  systemd  / **Architectures:** aarch64, x86\_64
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
  - **AL2023.1.20230912 version:** 252.4-1161.amzn2023.0.4
  - **AL2023.2.20230920 version:** 252.16-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 2023.1.20230912-0.amzn2023
  - **AL2023.2.20230920 version:** 2023.2.20230920-0.amzn2023

- ** `wayland` **
  - **RPM:**  libwayland-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-doc  / **Architectures:** noarch
  - **AL2023.1.20230912 version:** 1.22.0-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 1.22.0-1.amzn2023.0.2

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230912 version:** 4.0.7-1.amzn2023.0.1
  - **AL2023.2.20230920 version:** 4.0.8-2.amzn2023.0.1

## Docker container image
<a name="amis-2023.2.20230920.container-image"></a>
+ `amazon-linux-repo-cdn-2023.2.20230920-0.amzn2023`
+ `glib2-2.74.7-689.amzn2023.0.2`
+ `libffi-3.4.4-1.amzn2023.0.1`
+ `libgcrypt-1.10.2-1.amzn2023.0.1`
+ `p11-kit-trust-0.24.1-2.amzn2023.0.3`
+ `p11-kit-0.24.1-2.amzn2023.0.3`
+ `python3-libs-3.9.16-1.amzn2023.0.6`
+ `python3-3.9.16-1.amzn2023.0.6`
+ `system-release-2023.2.20230920-0.amzn2023`

## Default AMI
<a name="2023.2.20230920.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.2.20230920-0.amzn2023` |
| `cloud-init-22.2.2-1.amzn2023.1.11` |
| `fonts-srpm-macros-1:2.0.5-12.amzn2023.0.2` |
| `glib2-2.74.7-689.amzn2023.0.2` |
| `kernel-livepatch-repo-s3-2023.2.20230920-0.amzn2023` |
| `kernel-tools-6.1.52-71.125.amzn2023` |
| `kernel-6.1.52-71.125.amzn2023` |
| `libffi-3.4.4-1.amzn2023.0.1` |
| `libffi-3.4.4-1.amzn2023.0.1` |
| `p11-kit-trust-0.24.1-2.amzn2023.0.3` |
| `p11-kit-0.24.1-2.amzn2023.0.3` |
| `python3-cffi-1.14.5-1.amzn2023.0.3` |
| `python3-libs-3.9.16-1.amzn2023.0.6` |
| `python3-3.9.16-1.amzn2023.0.6` |
| `system-release-2023.2.20230920-0.amzn2023` |
| `systemd-libs-252.16-1.amzn2023.0.1` |
| `systemd-networkd-252.16-1.amzn2023.0.1` |
| `systemd-pam-252.16-1.amzn2023.0.1` |
| `systemd-resolved-252.16-1.amzn2023.0.1` |
| `systemd-udev-252.16-1.amzn2023.0.1` |
| `systemd-252.16-1.amzn2023.0.1` |
| `zram-generator-defaults-1.1.2-67.amzn2023` |
| `zram-generator-1.1.2-67.amzn2023` |

## Minimal AMI
<a name="amis-2023.2.20230920.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.2.20230920-0.amzn2023` |
| `cloud-init-22.2.2-1.amzn2023.1.11` |
| `glib2-2.74.7-689.amzn2023.0.2` |
| `kernel-livepatch-repo-s3-2023.2.20230920-0.amzn2023` |
| `kernel-6.1.52-71.125.amzn2023` |
| `libffi-3.4.4-1.amzn2023.0.1` |
| `libgcrypt-1.10.2-1.amzn2023.0.1` |
| `p11-kit-trust-0.24.1-2.amzn2023.0.3` |
| `p11-kit-0.24.1-2.amzn2023.0.3` |
| `python3-cffi-1.14.5-1.amzn2023.0.3` |
| `python3-libs-3.9.16-1.amzn2023.0.6` |
| `python3-3.9.16-1.amzn2023.0.6` |
| `system-release-2023.2.20230920-0` |
| `systemd-libs-252.16-1.amzn2023.0.1` |
| `systemd-networkd-252.16-1.amzn2023.0.1` |
| `systemd-pam-252.16-1.amzn2023.0.1` |
| `systemd-resolved-252.16-1.amzn2023.0.1` |
| `systemd-udev-252.16-1.amzn2023.0.1` |
| `systemd-252.16-1.amzn2023.0.1` |
| `zram-generator-defaults-1.1.2-67.amzn2023` |
| `zram-generator-1.1.2-67.amzn2023` |

## Minimal container image
<a name="amis-2023.2.20230920.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.2.20230920-0.amzn2023`
+ `glib2-2.74.7-689.amzn2023.0.2`
+ `gobject-introspection-1.73.0-2.amzn2023.0.3`
+ `libffi-3.4.4-1.amzn2023.0.1`
+ `libgcrypt-1.10.2-1.amzn2023.0.1`
+ `p11-kit-trust-0.24.1-2.amzn2023.0.3`
+ `p11-kit-0.24.1-2.amzn2023.0.3`
+ `system-release-2023.2.20230920-0.amzn2023`
