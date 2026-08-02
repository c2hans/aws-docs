---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250203.html
---

# Amazon Linux 2023 version 2023.6.20250203 release notes
<a name="relnotes-2023.6.20250203"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250203.

**Topics**
+ [Major updates](#major-updates-2023.6.20250203)
+ [Repository](#amis-2023.6.20250203.repository)
+ [Docker container image](#amis-2023.6.20250203.container-image)
+ [Default AMI](#amis-2023.6.20250203.default-ami)
+ [Minimal AMI](#amis-2023.6.20250203.minimal-ami)
+ [Minimal container image](#amis-2023.6.20250203.minimal-container-ami)
+ [Contact us](#amis-2023.6.20250203.contact-us)

## Major updates
<a name="major-updates-2023.6.20250203"></a>

This release represents an update to the sixth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250203.repository"></a>

### New packages in AL2023.6.20250203 since AL2023.6.20250128
<a name="new-AL2023.6.20250128-AL2023.6.20250203"></a>

 Comparing AL2023.6.20250128 version 2023.6.20250128 to AL2023.6.20250203 version [2023.6.20250203](#relnotes-2023.6.20250203).

| Package Type | Number of new packages in AL2023.6.20250203 compared to AL2023.6.20250128 |
| --- | --- |
| Source RPMs | 2 |
| Total Binary RPMs | 8 |
|  x86\_64 binary RPMs | 4 |
|  aarch64 binary RPMs | 4 |

New packages in AL2023.6.20250203:

- ** `lldpad` **
  - **RPM:**  lldpad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lldpad-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.0-12.git85e5583.amzn2023

- ** `valkey` **
  - **RPM:**  valkey  / **Architectures:** aarch64, x86\_64
  - **RPM:**  valkey-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.0.1-3.amzn2023.0.1

### AL2023.6.20250203 upgrades from AL2023.6.20250128
<a name="vercmp-AL2023.6.20250128-AL2023.6.20250203"></a>

 Comparing [2023.6.20250128](relnotes-2023.6.20250128.md) to [2023.6.20250203](#relnotes-2023.6.20250203).

| Package Type | Count |
| --- | --- |
| Source | 21 |
| Total Binary | 350 |
|  noarch binary RPMs | 104 |
|  x86\_64 binary RPMs | 123 |
|  aarch64 binary RPMs | 123 |

The full comparison of RPM package versions is below.

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 3.3.987.0-1.amzn2023
  - **AL2023.6.20250203 version:** 3.3.1611.0-1.amzn2023

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-dnssec-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-doc  / **Architectures:** noarch
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 9.18.28-1.amzn2023.0.2
  - **AL2023.6.20250203 version:** 9.18.33-1.amzn2023.0.2

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 1.3.6-0.amzn2023
  - **AL2023.6.20250203 version:** 1.3.7-0.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 1.8.0\_432.b06-1.amzn2023
  - **AL2023.6.20250203 version:** 1.8.0\_442.b06-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 11.0.25\+9-1.amzn2023
  - **AL2023.6.20250203 version:** 11.0.26\+4-1.amzn2023

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-17-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 17.0.13\+11-1.amzn2023.1
  - **AL2023.6.20250203 version:** 17.0.14\+7-1.amzn2023.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-21-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 21.0.5\+11-1.amzn2023.1
  - **AL2023.6.20250203 version:** 21.0.6\+7-1.amzn2023.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-23-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/java.html](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 23.0.1\+8-1.amzn2023.1
  - **AL2023.6.20250203 version:** 23.0.2\+7-1.amzn2023.1

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
  - **AL2023.6.20250128 version:** 6.1.124-134.200.amzn2023
  - **AL2023.6.20250203 version:** 6.1.127-135.201.amzn2023

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 2.0.2-1.amzn2023.0.1
  - **AL2023.6.20250203 version:** 2.0.3-1.amzn2023.0.1

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 20.18.1-1.amzn2023.0.1
  - **AL2023.6.20250203 version:** 20.18.2-1.amzn2023.0.1

- ** `openjpeg2` **
  - **RPM:**  openjpeg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel-docs  / **Architectures:** noarch
  - **RPM:**  openjpeg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 2.4.0-11.amzn2023.0.4
  - **AL2023.6.20250203 version:** 2.4.0-11.amzn2023.0.5

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
  - **RPM:**  php8.1-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 8.1.29-1.amzn2023.0.1
  - **AL2023.6.20250203 version:** 8.1.29-1.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 3.11.6-1.amzn2023.0.5
  - **AL2023.6.20250203 version:** 3.11.6-1.amzn2023.0.6

- ** [https://docs.aws.amazon.com/linux/al2023/ug/python.html](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.6.20250128 version:** 3.9.20-1.amzn2023.0.2
  - **AL2023.6.20250203 version:** 3.9.20-1.amzn2023.0.3

- ** `python-requests-unixsocket` **
  - **RPM:**  python3-requests-unixsocket
  - **Architectures:** noarch
  - **AL2023.6.20250128 version:** 0.1.5-9.amzn2023.0.2
  - **AL2023.6.20250203 version:** 0.1.5-9.amzn2023.0.3

- ** `python-virtualenv` **
  - **RPM:**  python3-virtualenv
  - **Architectures:** noarch
  - **AL2023.6.20250128 version:** 20.4.0-3.amzn2023.0.3
  - **AL2023.6.20250203 version:** 20.4.0-3.amzn2023.0.4

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
  - **AL2023.6.20250128 version:** 3.2.2-180.amzn2023.0.4
  - **AL2023.6.20250203 version:** 3.2.2-180.amzn2023.0.5

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250128 version:** 2023.6.20250128-0.amzn2023
  - **AL2023.6.20250203 version:** 2023.6.20250203-0.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-exporter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-initscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-jupyter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-virtguest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-dtrace  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 5.2-1.amzn2023.0.1
  - **AL2023.6.20250203 version:** 5.2-1.amzn2023.0.3

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250128 version:** 4.0.15-1.amzn2023.0.1
  - **AL2023.6.20250203 version:** 4.4.2-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.6.20250203.container-image"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250203-0.amzn2023 |
| python3-libs-3.9.20-1.amzn2023.0.3 |
| python3-3.9.20-1.amzn2023.0.3 |
| system-release-2023.6.20250203-0.amzn2023 |

## Default AMI
<a name="amis-2023.6.20250203.default-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250203-0.amzn2023 |
| amazon-ssm-agent-3.3.1611.0-1.amzn2023 |
| bind-libs-32:9.18.33-1.amzn2023.0.2 |
| bind-license-32:9.18.33-1.amzn2023.0.2 |
| bind-utils-32:9.18.33-1.amzn2023.0.2 |
| kernel-libbpf-6.1.127-135.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250203-0.amzn2023 |
| kernel-tools-6.1.127-135.201.amzn2023 |
| kernel-6.1.127-135.201.amzn2023 |
| python3-libs-3.9.20-1.amzn2023.0.3 |
| python3-3.9.20-1.amzn2023.0.3 |
| system-release-2023.6.20250203-0.amzn2023 |
| systemtap-runtime-5.2-1.amzn2023.0.3 |

## Minimal AMI
<a name="amis-2023.6.20250203.minimal-ami"></a>

|  |
| --- |
| amazon-linux-repo-s3-2023.6.20250203-0.amzn2023 |
| kernel-libbpf-6.1.127-135.201.amzn2023 |
| kernel-livepatch-repo-s3-2023.6.20250203-0.amzn2023 |
| kernel-6.1.127-135.201.amzn2023 |
| python3-libs-3.9.20-1.amzn2023.0.3 |
| python3-3.9.20-1.amzn2023.0.3 |
| system-release-2023.6.20250203-0.amzn2023 |

## Minimal container image
<a name="amis-2023.6.20250203.minimal-container-ami"></a>

|  |
| --- |
| amazon-linux-repo-cdn-2023.6.20250203-0.amzn2023 |
| system-release-2023.6.20250203-0.amzn2023 |

## Contact us
<a name="amis-2023.6.20250203.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
