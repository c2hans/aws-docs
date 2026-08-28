---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/vercmp-AL2-AL2023.12.html
---

# AL2023.12 upgrades from AL2
<a name="vercmp-AL2-AL2023.12"></a>

 Comparing AL2 version 2026-08-28 to AL2023.12 version [2023.12.20260817](relnotes-2023.12.20260817.md).

| Package Type | Count |
| --- | --- |
| Source | 1607 |
| Total Binary | 7580 |
|  noarch binary RPMs | 1708 |
|  x86\_64 binary RPMs | 2967 |
|  aarch64 binary RPMs | 2905 |

The full comparison of RPM package versions is below.

**Topics**
+ [AL2 Core packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-al2-core)
+ [awscli1 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-awscli1)
+ [BCC AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-BCC)
+ [selinux-ng AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-selinux-ng)
+ [ruby2.4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-ruby2.4)
+ [rust1 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-rust1)
+ [dnsmasq AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-dnsmasq)
+ [dnsmasq2.85 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-dnsmasq2.85)
+ [golang1.11 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-golang1.11)
+ [golang1.19 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-golang1.19)
+ [kernel-5.10 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-kernel-5.10)
+ [kernel-5.15 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-kernel-5.15)
+ [kernel-5.4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-kernel-5.4)
+ [kernel-ng AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-kernel-ng)
+ [mate-desktop1.x AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-mate-desktop1.x)
+ [php7.2 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php7.2)
+ [lamp-mariadb10.2-php7.2 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-lamp-mariadb10.2-php7.2)
+ [mariadb10.5 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-mariadb10.5)
+ [php7.3 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php7.3)
+ [php7.4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php7.4)
+ [php8.0 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php8.0)
+ [php8.1 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php8.1)
+ [php8.2 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-php8.2)
+ [postgresql10 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql10)
+ [postgresql11 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql11)
+ [postgresql12 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql12)
+ [postgresql13 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql13)
+ [postgresql14 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql14)
+ [postgresql9.6 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-postgresql9.6)
+ [mock2 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-mock2)
+ [ruby2.6 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-ruby2.6)
+ [ruby3.0 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-ruby3.0)
+ [squid4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-squid4)
+ [tomcat8.5 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-tomcat8.5)
+ [tomcat9 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-tomcat9)
+ [unbound1.13 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-unbound1.13)
+ [unbound1.17 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-unbound1.17)
+ [vim AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-vim)
+ [ansible2 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-ansible2)
+ [httpd\_modules AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-httpd_modules)
+ [redis4.0 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-redis4.0)
+ [redis6 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-redis6)
+ [R3.4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-R3.4)
+ [R4 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-R4)
+ [docker AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-docker)
+ [ecs AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-ecs)
+ [GraphicsMagick1.3 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-GraphicsMagick1.3)
+ [testing AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-testing)
+ [corretto8 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-corretto8)
+ [lustre AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-lustre)
+ [lustre2.10 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-lustre2.10)
+ [lynis AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-lynis)
+ [nginx1 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-nginx1)
+ [python3.8 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-python3.8)
+ [collectd AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-collectd)
+ [collectd-python3 AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-collectd-python3)
+ [aws-nitro-enclaves-cli AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-aws-nitro-enclaves-cli)
+ [firefox AL2 Extra packages updated in Amazon Linux 2023](#vercmp-AL2023.12-AL2-ex2-firefox)

## AL2 Core packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-al2-core"></a>

- ** `a2ps` **
  - **RPM:**  a2ps
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.14-23.amzn2.0.2
  - **AL2023.12 version:** 4.14-48.amzn2023.0.2

- ** `abattis-cantarell-fonts` **
  - **RPM:**  abattis-cantarell-fonts
  - **Architectures:** noarch
  - **AL2 version:** 0.0.25-1.amzn2
  - **AL2023.12 version:** 0.301-2.amzn2023.0.1

- ** `accountsservice` **
  - **RPM:**  accountsservice  / **Architectures:** aarch64, x86\_64
  - **RPM:**  accountsservice-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  accountsservice-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.6.45-7.amzn2
  - **AL2023.12 version:** 23.13.9-5.amzn2023

- ** `acl` **
  - **RPM:**  acl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libacl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libacl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.51-14.amzn2.0.1
  - **AL2023.12 version:** 2.4.0-1.amzn2023.0.1

- ** `acpica-tools` **
  - **RPM:**  acpica-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20160527-3.amzn2
  - **AL2023.12 version:** 20210604-1.amzn2023.0.2

- ** `acpid` **
  - **RPM:**  acpid
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.19-9.amzn2.0.2
  - **AL2023.12 version:** 2.0.32-4.amzn2023.0.3

- ** `adcli` **
  - **RPM:**  adcli
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.1-16.amzn2.1.0.1
  - **AL2023.12 version:** 0.9.1-10.amzn2023.0.3

- ** `adobe-mappings-cmap` **
  - **RPM:**  adobe-mappings-cmap  / **Architectures:** noarch
  - **RPM:**  adobe-mappings-cmap-deprecated  / **Architectures:** noarch
  - **RPM:**  adobe-mappings-cmap-devel  / **Architectures:** noarch
  - **AL2 version:** 20171205-3.amzn2
  - **AL2023.12 version:** 20190730-1.amzn2023.0.2

- ** `adobe-mappings-pdf` **
  - **RPM:**  adobe-mappings-pdf  / **Architectures:** noarch
  - **RPM:**  adobe-mappings-pdf-devel  / **Architectures:** noarch
  - **AL2 version:** 20180407-1.amzn2
  - **AL2023.12 version:** 20180407-8.amzn2023.0.2

- ** `adwaita-icon-theme` **
  - **RPM:**  adwaita-cursor-theme  / **Architectures:** noarch
  - **RPM:**  adwaita-icon-theme  / **Architectures:** noarch
  - **RPM:**  adwaita-icon-theme-devel  / **Architectures:** noarch
  - **AL2 version:** 3.26.0-1.amzn2
  - **AL2023.12 version:** 47.0-1.amzn2023.0.1

- ** `aide` **
  - **RPM:**  aide
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.16.2-1.amzn2.0.3
  - **AL2023.12 version:** 0.18.6-1.amzn2023.0.2

- ** `alsa-lib` **
  - **RPM:**  alsa-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-lib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.4.1-2.amzn2
  - **AL2023.12 version:** 1.2.7.2-1.amzn2023.0.3

- ** `alsa-plugins` **
  - **RPM:**  alsa-plugins-arcamav  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-plugins-maemo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-plugins-oss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-plugins-pulseaudio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-plugins-speex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  alsa-plugins-usbstream  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.1-1.amzn2.0.2
  - **AL2023.12 version:** 1.2.7.1-1.amzn2023.0.3

- ** `alsa-utils` **
  - **RPM:**  alsa-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.3-2.amzn2.0.1
  - **AL2023.12 version:** 1.2.7-1.amzn2023.0.3

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.300069.1-1.amzn2
  - **AL2023.12 version:** 1.300069.1-1.amzn2023

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, noarch, x86\_64
  - **AL2 version:** 3.2.0-2.amzn2
  - **AL2023.12 version:** 3.2.0-2.amzn2023

- ** [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html) **
  - **RPM:**  [`amazon-linux-onprem`](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html)
  - **Architectures:** noarch
  - **AL2 version:** 1.0-0.amzn2
  - **AL2023.12 version:** 1.2-0.amzn2023

- ** `amazon-ssm-agent` **
  - **RPM:**  amazon-ssm-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.4624.0-1.amzn2
  - **AL2023.12 version:** 3.3.4624.0-1.amzn2023

- ** `ant` **
  - **RPM:**  ant  / **Architectures:** noarch
  - **RPM:**  ant-antlr  / **Architectures:** noarch
  - **RPM:**  ant-apache-bcel  / **Architectures:** noarch
  - **RPM:**  ant-apache-bsf  / **Architectures:** noarch
  - **RPM:**  ant-apache-oro  / **Architectures:** noarch
  - **RPM:**  ant-apache-regexp  / **Architectures:** noarch
  - **RPM:**  ant-apache-resolver  / **Architectures:** noarch
  - **RPM:**  ant-apache-xalan2  / **Architectures:** noarch
  - **RPM:**  ant-commons-logging  / **Architectures:** noarch
  - **RPM:**  ant-commons-net  / **Architectures:** noarch
  - **RPM:**  ant-javadoc  / **Architectures:** noarch
  - **RPM:**  ant-javamail  / **Architectures:** noarch
  - **RPM:**  ant-jdepend  / **Architectures:** noarch
  - **RPM:**  ant-jmf  / **Architectures:** noarch
  - **RPM:**  ant-jsch  / **Architectures:** noarch
  - **RPM:**  ant-junit  / **Architectures:** noarch
  - **RPM:**  ant-manual  / **Architectures:** noarch
  - **RPM:**  ant-swing  / **Architectures:** noarch
  - **RPM:**  ant-testutil  / **Architectures:** noarch
  - **AL2 version:** 1.9.16-1.amzn2.0.1
  - **AL2023.12 version:** 1.10.12-5.amzn2023.0.4

- ** `antlr` **
  - **RPM:**  antlr-C\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  antlr-javadoc  / **Architectures:** noarch
  - **RPM:**  antlr-manual  / **Architectures:** noarch
  - **RPM:**  antlr-tool  / **Architectures:** noarch
  - **AL2 version:** 2.7.7-30.amzn2.0.2
  - **AL2023.12 version:** 2.7.7-69.amzn2023.0.3

- ** `aopalliance` **
  - **RPM:**  aopalliance  / **Architectures:** noarch
  - **RPM:**  aopalliance-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-8.1.amzn2
  - **AL2023.12 version:** 1.0-28.amzn2023.0.3

- ** `apache-commons-beanutils` **
  - **RPM:**  apache-commons-beanutils  / **Architectures:** noarch
  - **RPM:**  apache-commons-beanutils-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.8.3-15.amzn2.0.1
  - **AL2023.12 version:** 1.11.0-10.amzn2023.0.1

- ** `apache-commons-cli` **
  - **RPM:**  apache-commons-cli  / **Architectures:** noarch
  - **RPM:**  apache-commons-cli-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2-13.amzn2
  - **AL2023.12 version:** 1.5.0-3.amzn2023.0.3

- ** `apache-commons-codec` **
  - **RPM:**  apache-commons-codec  / **Architectures:** noarch
  - **RPM:**  apache-commons-codec-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.8-7.amzn2
  - **AL2023.12 version:** 1.15-6.amzn2023.0.3

- ** `apache-commons-collections` **
  - **RPM:**  apache-commons-collections  / **Architectures:** noarch
  - **RPM:**  apache-commons-collections-javadoc  / **Architectures:** noarch
  - **RPM:**  apache-commons-collections-testframework  / **Architectures:** noarch
  - **AL2 version:** 3.2.1-22.amzn2
  - **AL2023.12 version:** 3.2.2-27.amzn2023.0.3

- ** `apache-commons-compress` **
  - **RPM:**  apache-commons-compress  / **Architectures:** noarch
  - **RPM:**  apache-commons-compress-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.5-4.amzn2.0.2
  - **AL2023.12 version:** 1.21-4.amzn2023.0.4

- ** `apache-commons-exec` **
  - **RPM:**  apache-commons-exec  / **Architectures:** noarch
  - **RPM:**  apache-commons-exec-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1-11.amzn2
  - **AL2023.12 version:** 1.3-22.amzn2023.0.2

- ** `apache-commons-io` **
  - **RPM:**  apache-commons-io  / **Architectures:** noarch
  - **RPM:**  apache-commons-io-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4-12.amzn2.0.2
  - **AL2023.12 version:** 2.8.0-7.amzn2023.0.5

- ** `apache-commons-jxpath` **
  - **RPM:**  apache-commons-jxpath  / **Architectures:** noarch
  - **RPM:**  apache-commons-jxpath-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.3-20.amzn2
  - **AL2023.12 version:** 1.3-43.amzn2023.0.3

- ** `apache-commons-lang3` **
  - **RPM:**  apache-commons-lang3  / **Architectures:** noarch
  - **RPM:**  apache-commons-lang3-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.1-9.amzn2
  - **AL2023.12 version:** 3.18.0-1.amzn2023.0.1

- ** `apache-commons-logging` **
  - **RPM:**  apache-commons-logging  / **Architectures:** noarch
  - **RPM:**  apache-commons-logging-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1.2-7.amzn2
  - **AL2023.12 version:** 1.2-30.amzn2023.0.3

- ** `apache-commons-net` **
  - **RPM:**  apache-commons-net  / **Architectures:** noarch
  - **RPM:**  apache-commons-net-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.2-8.amzn2
  - **AL2023.12 version:** 3.6-17.amzn2023.0.1

- ** `apache-commons-parent` **
  - **RPM:**  apache-commons-parent
  - **Architectures:** noarch
  - **AL2 version:** 26-8.amzn2
  - **AL2023.12 version:** 52-6.amzn2023.0.3

- ** `apache-ivy` **
  - **RPM:**  apache-ivy  / **Architectures:** noarch
  - **RPM:**  apache-ivy-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.3.0-4.amzn2.0.2
  - **AL2023.12 version:** 2.5.1-1.amzn2023.0.2

- ** `apache-parent` **
  - **RPM:**  apache-parent
  - **Architectures:** noarch
  - **AL2 version:** 10-14.amzn2
  - **AL2023.12 version:** 23-8.amzn2023.0.3

- ** `apache-resource-bundles` **
  - **RPM:**  apache-resource-bundles
  - **Architectures:** noarch
  - **AL2 version:** 2-11.amzn2
  - **AL2023.12 version:** 30-5.amzn2023.0.3

- ** `appstream-data` **
  - **RPM:**  appstream-data
  - **Architectures:** noarch
  - **AL2 version:** 7-20180614.amzn2
  - **AL2023.12 version:** 2023-103.amzn2023

- ** `apr` **
  - **RPM:**  apr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.2-1.amzn2.0.1
  - **AL2023.12 version:** 1.7.5-1.amzn2023.0.4

- ** `apr-util` **
  - **RPM:**  apr-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  apr-util-sqlite  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.3-1.amzn2.0.1
  - **AL2023.12 version:** 1.6.3-1.amzn2023.0.2

- ** `aqute-bnd` **
  - **RPM:**  aqute-bnd  / **Architectures:** noarch
  - **RPM:**  aqute-bnd-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0.0.363-11.amzn2
  - **AL2023.12 version:** 5.2.0-9.amzn2023.0.3

- ** `args4j` **
  - **RPM:**  args4j  / **Architectures:** noarch
  - **RPM:**  args4j-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0.16-13.amzn2
  - **AL2023.12 version:** 2.33-19.amzn2023.0.1

- ** `asciidoc` **
  - **RPM:**  asciidoc  / **Architectures:** noarch
  - **RPM:**  asciidoc-doc  / **Architectures:** noarch
  - **RPM:**  asciidoc-latex  / **Architectures:** noarch
  - **AL2 version:** 8.6.8-5.amzn2
  - **AL2023.12 version:** 9.1.0-1.amzn2023.0.2

- ** `aspell` **
  - **RPM:**  aspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspell-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.60.6.1-22.amzn2
  - **AL2023.12 version:** 0.60.8-7.amzn2023.0.2

- ** `at` **
  - **RPM:**  at
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.13-24.amzn2
  - **AL2023.12 version:** 3.1.23-6.amzn2023.0.2

- ** `atinject` **
  - **RPM:**  atinject  / **Architectures:** noarch
  - **RPM:**  atinject-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1-13.20100611svn86.amzn2
  - **AL2023.12 version:** 1.0.5-3.amzn2023.0.3

- ** `atkmm` **
  - **RPM:**  atkmm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  atkmm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  atkmm-doc  / **Architectures:** noarch
  - **AL2 version:** 2.24.2-1.amzn2.0.2
  - **AL2023.12 version:** 2.28.2-1.amzn2023.0.2

- ** `atlas` **
  - **RPM:**  atlas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  atlas-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  atlas-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.10.1-12.amzn2.0.2
  - **AL2023.12 version:** 3.10.3-18.amzn2023.0.2

- ** `at-spi2-core` **
  - **RPM:**  at-spi2-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  at-spi2-core-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.22.0-1.amzn2.0.2
  - **AL2023.12 version:** 2.54.0-1.amzn2023.0.1

- ** `attr` **
  - **RPM:**  attr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libattr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libattr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.46-12.amzn2.0.2
  - **AL2023.12 version:** 2.5.1-3.amzn2023.0.2

- ** `audit` **
  - **RPM:**  audispd-plugins  / **Architectures:** aarch64, x86\_64
  - **RPM:**  audit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  audit-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  audit-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.8.1-3.amzn2.1
  - **AL2023.12 version:** 3.1.5-1.amzn2023.0.2

- ** `augeas` **
  - **RPM:**  augeas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  augeas-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  augeas-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.0-9.amzn2
  - **AL2023.12 version:** 1.13.0-1.amzn2023.0.2

- ** `autoconf` **
  - **RPM:**  autoconf
  - **Architectures:** noarch
  - **AL2 version:** 2.69-11.amzn2
  - **AL2023.12 version:** 2.69-36.amzn2023.0.3

- ** `autoconf-archive` **
  - **RPM:**  autoconf-archive
  - **Architectures:** noarch
  - **AL2 version:** 2017.03.21-1.amzn2
  - **AL2023.12 version:** 2019.01.06-7.amzn2023.0.2

- ** `autofs` **
  - **RPM:**  autofs
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.0.7-106.amzn2
  - **AL2023.12 version:** 5.1.8-7.amzn2023.0.2

- ** `automake` **
  - **RPM:**  automake
  - **Architectures:** noarch
  - **AL2 version:** 1.13.4-3.1.amzn2
  - **AL2023.12 version:** 1.16.5-9.amzn2023.0.3

- ** `autotrace` **
  - **RPM:**  autotrace  / **Architectures:** aarch64, x86\_64
  - **RPM:**  autotrace-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.31.1-38.amzn2.0.1
  - **AL2023.12 version:** 0.31.9-86.amzn2023.0.1

- ** `avahi` **
  - **RPM:**  avahi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-autoipd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-howl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-howl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-libdns\_sd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-compat-libdns\_sd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-dnsconfd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-ui-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  avahi-ui-gtk3  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.6.31-20.amzn2.0.7
  - **AL2023.12 version:** 0.8-14.amzn2023.0.14

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2 version:** 2.0-40.amzn2
  - **AL2023.12 version:** 2.0-40.amzn2023

- ** `awscli-2` (`awscli` in AL2) **
  - **RPM:**  awscli-2 (awscli in AL2)
  - **Architectures:** noarch
  - **AL2 version:** 1.18.147-1.amzn2.0.2
  - **AL2023.12 version:** 2.33.15-1.amzn2023.0.1

- ** `aws-kinesis-agent` **
  - **RPM:**  aws-kinesis-agent
  - **Architectures:** noarch
  - **AL2 version:** 2.0.13-1.amzn2
  - **AL2023.12 version:** 2.0.13-1.amzn2023

- ** `babel` **
  - **RPM:**  babel
  - **Architectures:** noarch
  - **AL2 version:** 0.9.6-8.amzn2.0.2
  - **AL2023.12 version:** 2.9.1-1.amzn2023.0.2

- ** `baekmuk-ttf-fonts` **
  - **RPM:**  baekmuk-ttf-batang-fonts  / **Architectures:** noarch
  - **RPM:**  baekmuk-ttf-dotum-fonts  / **Architectures:** noarch
  - **RPM:**  baekmuk-ttf-fonts-common  / **Architectures:** noarch
  - **RPM:**  baekmuk-ttf-gulim-fonts  / **Architectures:** noarch
  - **RPM:**  baekmuk-ttf-hline-fonts  / **Architectures:** noarch
  - **AL2 version:** 2.2-36.amzn2
  - **AL2023.12 version:** 2.2-54.amzn2023.0.2

- ** `basesystem` **
  - **RPM:**  basesystem
  - **Architectures:** noarch
  - **AL2 version:** 10.0-7.amzn2.0.1
  - **AL2023.12 version:** 11-11.amzn2023.0.2

- ** `bash` **
  - **RPM:**  bash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bash-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.2.46-34.amzn2
  - **AL2023.12 version:** 5.2.15-1.amzn2023.0.2

- ** `bash-completion` **
  - **RPM:**  bash-completion
  - **Architectures:** noarch
  - **AL2 version:** 2.1-6.amzn2
  - **AL2023.12 version:** 2.11-2.amzn2023.0.2

- ** `bc` **
  - **RPM:**  bc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.06.95-13.amzn2.0.2
  - **AL2023.12 version:** 1.07.1-14.amzn2023.0.2

- ** `bcc` **
  - **RPM:**  bcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bcc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bcc-doc  / **Architectures:** noarch
  - **RPM:**  bcc-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbpf-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-bcc  / **Architectures:** noarch
  - **AL2 version:** 0.24.0-3.amzn2.0.5
  - **AL2023.12 version:** 0.35.0-4.amzn2023.0.2

- ** `bcel` **
  - **RPM:**  bcel  / **Architectures:** noarch
  - **RPM:**  bcel-javadoc  / **Architectures:** noarch
  - **AL2 version:** 5.2-18.amzn2.0.1
  - **AL2023.12 version:** 6.5.0-3.amzn2023.0.2

- ** `beust-jcommander` **
  - **RPM:**  beust-jcommander  / **Architectures:** noarch
  - **RPM:**  beust-jcommander-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.30-5.amzn2
  - **AL2023.12 version:** 1.78-9.amzn2023.0.3

- ** `bind` **
  - **RPM:**  bind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-chroot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-license  / **Architectures:** noarch
  - **RPM:**  bind-pkcs11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-pkcs11-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bind-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.11.4-26.P2.amzn2.13.17
  - **AL2023.12 version:** 9.18.50-1.amzn2023.0.2

- ** [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.29.1-31.amzn2.0.2
  - **AL2023.12 version:** 2.41-50.amzn2023.0.5

- ** [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (`gcc10-binutils` in AL2) **
  - **RPM:**  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (gcc10-binutils in AL2)  / **Architectures:**
  - **RPM:**  binutils-devel (gcc10-binutils-devel in AL2)  / **Architectures:**
  - **AL2 version:** 2.35.2-9.amzn2.0.5
  - **AL2023.12 version:** 2.41-50.amzn2023.0.5

- ** `bison` **
  - **RPM:**  bison  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bison-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bison-runtime  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.4-6.amzn2.0.2
  - **AL2023.12 version:** 3.7.4-2.amzn2023.0.2

- ** `blktrace` **
  - **RPM:**  blktrace
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.5-9.amzn2
  - **AL2023.12 version:** 1.2.0-17.amzn2023.0.2

- ** `bluez` **
  - **RPM:**  bluez  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-hid2hci  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bluez-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.44-7.amzn2.0.4
  - **AL2023.12 version:** 5.62-2.amzn2023.0.5

- ** `boost` **
  - **RPM:**  boost  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-atomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-build  / **Architectures:** noarch
  - **RPM:**  boost-chrono  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-context  / **Architectures:** x86\_64
  - **RPM:**  boost-date-time  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-graph  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-iostreams  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-locale  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-math  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-program-options  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-random  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-regex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-serialization  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-system  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-thread  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-timer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  boost-wave  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.53.0-27.amzn2.0.7
  - **AL2023.12 version:** 1.75.0-4.amzn2023.0.4

- ** `bpftrace` **
  - **RPM:**  bpftrace
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12.1-2.amzn2.0.2
  - **AL2023.12 version:** 0.17.0-1.amzn2023.0.2

- ** `bsf` **
  - **RPM:**  bsf
  - **Architectures:** noarch
  - **AL2 version:** 2.4.0-19.amzn2
  - **AL2023.12 version:** 2.4.0-44.amzn2023.0.2

- ** `bsh` **
  - **RPM:**  bsh  / **Architectures:** noarch
  - **RPM:**  bsh-javadoc  / **Architectures:** noarch
  - **RPM:**  bsh-manual  / **Architectures:** noarch
  - **AL2 version:** 1.3.0-29.1.amzn2
  - **AL2023.12 version:** 2.1.0-5.amzn2023.0.2

- ** `byacc` **
  - **RPM:**  byacc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.20130304-3.amzn2.0.2
  - **AL2023.12 version:** 2.0.20210109-2.amzn2023.0.3

- ** `byaccj` **
  - **RPM:**  byaccj
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.15-8.amzn2.0.2
  - **AL2023.12 version:** 1.15-25.amzn2023.0.2

- ** `byteman` **
  - **RPM:**  byteman  / **Architectures:** noarch
  - **RPM:**  byteman-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0.4-5.amzn2
  - **AL2023.12 version:** 4.0.16-4.amzn2023.0.3

- ** `bzip2` **
  - **RPM:**  bzip2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bzip2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bzip2-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.6-13.amzn2.0.3
  - **AL2023.12 version:** 1.0.8-6.amzn2023.0.2

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2 version:** 2025.2.76-1.amzn2.0.2
  - **AL2023.12 version:** 2025.2.76-1.0.amzn2023.0.3

- ** `cairo` **
  - **RPM:**  cairo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-gobject-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairo-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.15.12-4.amzn2.0.1
  - **AL2023.12 version:** 1.18.0-4.amzn2023.0.3

- ** `cairomm` **
  - **RPM:**  cairomm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cairomm-doc  / **Architectures:** noarch
  - **AL2 version:** 1.12.0-1.amzn2.0.2
  - **AL2023.12 version:** 1.14.5-141.amzn2023

- ** `can-utils` **
  - **RPM:**  can-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2023.03-3.amzn2
  - **AL2023.12 version:** 2023.03-3.amzn2023

- ** `capstone` **
  - **RPM:**  capstone  / **Architectures:** aarch64, x86\_64
  - **RPM:**  capstone-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  capstone-java  / **Architectures:** noarch
  - **AL2 version:** 3.0.5-1.amzn2.0.2
  - **AL2023.12 version:** 4.0.2-9.amzn2023.0.5

- ** `c-ares` **
  - **RPM:**  c-ares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  c-ares-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.19.1-1.amzn2.0.1
  - **AL2023.12 version:** 1.19.1-1.amzn2023.0.1

- ** `cdi-api` **
  - **RPM:**  cdi-api  / **Architectures:** noarch
  - **RPM:**  cdi-api-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-11.SP4.amzn2
  - **AL2023.12 version:** 2.0.2-6.amzn2023.0.3

- ** `certmonger` **
  - **RPM:**  certmonger
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.78.4-11.amzn2
  - **AL2023.12 version:** 0.79.18-2.amzn2023.0.2

- ** `cglib` **
  - **RPM:**  cglib  / **Architectures:** noarch
  - **RPM:**  cglib-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.2-18.1.amzn2
  - **AL2023.12 version:** 3.3.0-7.amzn2023.0.3

- ** `check` **
  - **RPM:**  check  / **Architectures:** aarch64, x86\_64
  - **RPM:**  check-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  check-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.9-5.amzn2.0.2
  - **AL2023.12 version:** 0.15.2-5.amzn2023.0.3

- ** `checkpolicy` **
  - **RPM:**  checkpolicy
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5-6.amzn2
  - **AL2023.12 version:** 3.4-3.amzn2023.0.2

- ** `checksec` **
  - **RPM:**  checksec
  - **Architectures:** noarch
  - **AL2 version:** 2.4.0-2.amzn2.0.1
  - **AL2023.12 version:** 2.4.0-2.amzn2023.0.2

- ** `chkconfig` **
  - **RPM:**  chkconfig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ntsysv  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.4-1.amzn2.0.2
  - **AL2023.12 version:** 1.15-2.amzn2023.0.2

- ** `chrony` **
  - **RPM:**  chrony
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.2-5.amzn2.0.2
  - **AL2023.12 version:** 4.3-1.amzn2023.0.6

- ** `chrpath` **
  - **RPM:**  chrpath
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.16-0.amzn2.0.2
  - **AL2023.12 version:** 0.16-15.amzn2023.0.2

- ** `cifs-utils` **
  - **RPM:**  cifs-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cifs-utils-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.2-10.amzn2.0.4
  - **AL2023.12 version:** 7.7-144.amzn2023

- ** `cjkuni-uming-fonts` **
  - **RPM:**  cjkuni-uming-fonts
  - **Architectures:** noarch
  - **AL2 version:** 0.2.20080216.1-53.amzn2
  - **AL2023.12 version:** 0.2.20080216.1-66.amzn2023.0.2

- ** `clamav` **
  - **RPM:**  clamav  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-data  / **Architectures:** noarch
  - **RPM:**  clamav-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-doc  / **Architectures:** noarch
  - **RPM:**  clamav-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav-update  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.103.12-1.amzn2.0.1
  - **AL2023.12 version:** 0.103.12-1.amzn2023.0.1

- ** `clamav1.4` **
  - **RPM:**  clamav1.4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-data  / **Architectures:** noarch
  - **RPM:**  clamav1.4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-doc  / **Architectures:** noarch
  - **RPM:**  clamav1.4-filesystem  / **Architectures:** noarch
  - **RPM:**  clamav1.4-freshclam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamav1.4-milter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clamd1.4  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.5-1.amzn2.0.1
  - **AL2023.12 version:** 1.4.5-1.amzn2023.0.1

- ** `clang` **
  - **RPM:**  clang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-analyzer  / **Architectures:** noarch
  - **RPM:**  clang-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-resource-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-clang-format  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-clang  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.1.0-1.amzn2.0.2
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.4

- ** `cloud-init` **
  - **RPM:**  cloud-init
  - **Architectures:** noarch
  - **AL2 version:** 19.3-46.amzn2.0.7
  - **AL2023.12 version:** 22.2.2-1.amzn2023.1.15

- ** `cmake` **
  - **RPM:**  cmake
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.8.12.2-2.amzn2.0.2
  - **AL2023.12 version:** 3.22.2-1.amzn2023.0.6

- ** `cmake` (`cmake3` in AL2) **
  - **RPM:**  cmake (cmake3 in AL2)  / **Architectures:**
  - **RPM:**  cmake-data (cmake3-data in AL2)  / **Architectures:** noarch
  - **RPM:**  cmake-doc (cmake3-doc in AL2)  / **Architectures:** noarch
  - **AL2 version:** 3.17.5-1.amzn2
  - **AL2023.12 version:** 3.22.2-1.amzn2023.0.6

- ** `cmocka` **
  - **RPM:**  libcmocka  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcmocka-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcmocka-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.1-8.amzn2
  - **AL2023.12 version:** 1.1.5-8.amzn2023.0.2

- ** `cni-plugins` **
  - **RPM:**  cni-plugins
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.1-1.amzn2.0.7
  - **AL2023.12 version:** 1.7.1-1.amzn2023.0.7

- ** `codehaus-parent` **
  - **RPM:**  codehaus-parent
  - **Architectures:** noarch
  - **AL2 version:** 4-5.amzn2
  - **AL2023.12 version:** 4-23.amzn2023.0.2

- ** `colord` **
  - **RPM:**  colord  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-devel-docs  / **Architectures:** noarch
  - **RPM:**  colord-extra-profiles  / **Architectures:** noarch
  - **RPM:**  colord-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.4-1.amzn2.0.2
  - **AL2023.12 version:** 1.4.5-2.amzn2023.0.2

- ** `colord-gtk` **
  - **RPM:**  colord-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-gtk-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.25-4.amzn2.0.3
  - **AL2023.12 version:** 0.3.1-2.amzn2023

- ** `color-filesystem` **
  - **RPM:**  color-filesystem
  - **Architectures:** noarch
  - **AL2 version:** 1-13.amzn2
  - **AL2023.12 version:** 1-26.amzn2023.0.2

- ** `compiler-rt` **
  - **RPM:**  compiler-rt
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.1.0-1.amzn2.0.1
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.1

- ** `conntrack-tools` **
  - **RPM:**  conntrack-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.4-5.amzn2.2
  - **AL2023.12 version:** 1.4.6-2.amzn2023.0.2

- ** `console-setup` **
  - **RPM:**  console-setup
  - **Architectures:** noarch
  - **AL2 version:** 1.111-1.amzn2
  - **AL2023.12 version:** 1.200-2.amzn2023.0.2

- ** `copy-jdk-configs` **
  - **RPM:**  copy-jdk-configs
  - **Architectures:** noarch
  - **AL2 version:** 3.3-10.amzn2
  - **AL2023.12 version:** 4.0-1.amzn2023.0.2

- ** `coreutils` **
  - **RPM:**  coreutils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.22-24.amzn2
  - **AL2023.12 version:** 8.32-30.amzn2023.0.5

- ** `corosync` **
  - **RPM:**  corosync  / **Architectures:** aarch64, x86\_64
  - **RPM:**  corosynclib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  corosynclib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.3-6.amzn2.1.1
  - **AL2023.12 version:** 3.1.9-3.amzn2023.0.2

- ** `cowsay` **
  - **RPM:**  cowsay
  - **Architectures:** noarch
  - **AL2 version:** 3.04-6.amzn2
  - **AL2023.12 version:** 3.04-17.amzn2023.0.2

- ** `cpio` **
  - **RPM:**  cpio
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.12-11.amzn2.0.1
  - **AL2023.12 version:** 2.13-13.amzn2023.0.3

- ** `cppunit` **
  - **RPM:**  cppunit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cppunit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cppunit-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.12.1-11.amzn2.0.2
  - **AL2023.12 version:** 1.15.1-5.amzn2023.0.2

- ** `cpuid` **
  - **RPM:**  cpuid
  - **Architectures:** x86\_64
  - **AL2 version:** 20170122-6.amzn2.0.2
  - **AL2023.12 version:** 20230120-70.amzn2023

- ** `cracklib` **
  - **RPM:**  cracklib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cracklib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cracklib-dicts  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.0-11.amzn2.0.2
  - **AL2023.12 version:** 2.9.6-27.amzn2023.0.2

- ** `crash` **
  - **RPM:**  crash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  crash-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.0.4-4.amzn2.0.1
  - **AL2023.12 version:** 8.0.5-5.amzn2023.0.1

- ** `createrepo_c` **
  - **RPM:**  createrepo\_c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  createrepo\_c-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  createrepo\_c-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12.2-2.amzn2.0.2
  - **AL2023.12 version:** 0.20.0-1.amzn2023.0.3

- ** `criu` **
  - **RPM:**  crit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  criu  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.5-4.amzn2
  - **AL2023.12 version:** 3.17.1-1.amzn2023.0.3

- ** [`cronie`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-cron) **
  - **RPM:**  [`cronie`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-cron)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cronie-anacron  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cronie-noanacron  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.11-23.amzn2
  - **AL2023.12 version:** 1.5.7-1.amzn2023.0.2

- ** `crontabs` **
  - **RPM:**  crontabs
  - **Architectures:** noarch
  - **AL2 version:** 1.11-6.20121102git.amzn2
  - **AL2023.12 version:** 1.11-24.20190603git.amzn2023.0.2

- ** `cryptsetup` **
  - **RPM:**  cryptsetup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cryptsetup-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cryptsetup-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  veritysetup  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.4-4.amzn2
  - **AL2023.12 version:** 2.6.1-1.amzn2023.0.1

- ** `cscope` **
  - **RPM:**  cscope
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 15.8-10.amzn2.0.2
  - **AL2023.12 version:** 15.9-15.amzn2023.0.3

- ** `ctags` **
  - **RPM:**  ctags
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.8-23.amzn2
  - **AL2023.12 version:** 5.9-1.20210725.0.amzn2023.0.2

- ** `CUnit` **
  - **RPM:**  CUnit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  CUnit-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.3-11.amzn2.0.2
  - **AL2023.12 version:** 2.1.3-23.amzn2023.0.2

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.3-51.amzn2.0.9
  - **AL2023.12 version:** 2.4.19-1.amzn2023.0.1

- ** `cups-filters` **
  - **RPM:**  cups-filters  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filters-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.35-26.amzn2.0.2
  - **AL2023.12 version:** 1.28.16-3.amzn2023.0.5

- ** `cups-pk-helper` **
  - **RPM:**  cups-pk-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.6-2.amzn2.0.2
  - **AL2023.12 version:** 0.2.7-8.amzn2023

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.3.0-1.amzn2.0.12
  - **AL2023.12 version:** 8.17.0-1.amzn2023.0.3

- ** `cvs` **
  - **RPM:**  cvs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cvs-doc  / **Architectures:** noarch
  - **AL2 version:** 1.11.23-35.amzn2.0.2
  - **AL2023.12 version:** 1.11.23-56.amzn2023.0.3

- ** `cvsps` **
  - **RPM:**  cvsps
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2-0.14.b1.amzn2.0.2
  - **AL2023.12 version:** 2.2-0.28.b1.amzn2023.0.2

- ** `cyrus-sasl` **
  - **RPM:**  cyrus-sasl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-gs2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-gssapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-md5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-ntlm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-plain  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-scram  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cyrus-sasl-sql  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.26-24.amzn2.0.1
  - **AL2023.12 version:** 2.1.27-18.amzn2023.0.3

- ** `Cython` **
  - **RPM:**  python3-Cython
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.27.3-2.amzn2.0.2
  - **AL2023.12 version:** 0.29.21-5.amzn2023.0.2

- ** `dblatex` **
  - **RPM:**  dblatex
  - **Architectures:** noarch
  - **AL2 version:** 0.3.4-11.amzn2
  - **AL2023.12 version:** 0.3.12-2.amzn2023.0.2

- ** `dbus` **
  - **RPM:**  dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-doc  / **Architectures:** noarch
  - **RPM:**  dbus-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-x11  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.10.24-7.amzn2.0.4
  - **AL2023.12 version:** 1.12.28-1.amzn2023.0.1

- ** `dbus-glib` **
  - **RPM:**  dbus-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dbus-glib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.100-7.2.amzn2
  - **AL2023.12 version:** 0.110-11.amzn2023.0.2

- ** `dbus-python` **
  - **RPM:**  dbus-python-devel
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.1-9.amzn2.0.2
  - **AL2023.12 version:** 1.2.18-1.amzn2023.0.2

- ** `dconf` **
  - **RPM:**  dconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dconf-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.28.0-4.amzn2
  - **AL2023.12 version:** 0.40.0-3.amzn2023.0.2

- ** `dconf-editor` **
  - **RPM:**  dconf-editor
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.0-1.amzn2
  - **AL2023.12 version:** 45.0.1-5.amzn2023.0.1

- ** `dejagnu` **
  - **RPM:**  dejagnu
  - **Architectures:** noarch
  - **AL2 version:** 1.5.1-3.amzn2
  - **AL2023.12 version:** 1.6.1-9.amzn2023.0.2

- ** `dejavu-fonts` **
  - **RPM:**  dejavu-lgc-sans-fonts  / **Architectures:** noarch
  - **RPM:**  dejavu-lgc-sans-mono-fonts  / **Architectures:** noarch
  - **RPM:**  dejavu-lgc-serif-fonts  / **Architectures:** noarch
  - **RPM:**  dejavu-sans-fonts  / **Architectures:** noarch
  - **RPM:**  dejavu-sans-mono-fonts  / **Architectures:** noarch
  - **RPM:**  dejavu-serif-fonts  / **Architectures:** noarch
  - **AL2 version:** 2.33-6.amzn2
  - **AL2023.12 version:** 2.37-16.amzn2023.0.2

- ** `desktop-file-utils` **
  - **RPM:**  desktop-file-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.23-2.amzn2
  - **AL2023.12 version:** 0.27-2.amzn2023.0.1

- ** `device-mapper-multipath` **
  - **RPM:**  device-mapper-multipath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-multipath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-multipath-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpartx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmmp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.9-136.amzn2
  - **AL2023.12 version:** 0.8.7-16.amzn2023.0.2

- ** `device-mapper-persistent-data` **
  - **RPM:**  device-mapper-persistent-data
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.3-3.amzn2
  - **AL2023.12 version:** 0.9.0-7.amzn2023.0.4

- ** `dialog` **
  - **RPM:**  dialog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dialog-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2-5.20130523.amzn2
  - **AL2023.12 version:** 1.3-51.20240101.amzn2023

- ** `diffstat` **
  - **RPM:**  diffstat
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.57-4.amzn2.0.2
  - **AL2023.12 version:** 1.64-4.amzn2023.0.2

- ** `diffutils` **
  - **RPM:**  diffutils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3-5.amzn2
  - **AL2023.12 version:** 3.8-1.amzn2023.0.2

- ** `ding-libs` **
  - **RPM:**  libbasicobjects  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbasicobjects-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcollection  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcollection-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdhash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdhash-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libini\_config  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libini\_config-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpath\_utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpath\_utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libref\_array  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libref\_array-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.1-29.amzn2
  - **AL2023.12 version:** 0.1.1-47.amzn2023.0.2

- ** `dkms` **
  - **RPM:**  dkms
  - **Architectures:** noarch
  - **AL2 version:** 2.6.1-1.amzn2.0.1
  - **AL2023.12 version:** 3.4.1-184.amzn2023

- ** `dmidecode` **
  - **RPM:**  dmidecode
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2-5.amzn2.1.1
  - **AL2023.12 version:** 3.6-1.amzn2023.0.1

- ** `dmraid` **
  - **RPM:**  dmraid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dmraid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dmraid-events  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.0.rc16-28.amzn2.0.2
  - **AL2023.12 version:** 1.0.0.rc16-50.amzn2023.0.2

- ** `dnf` (`yum` in AL2) **
  - **RPM:**  dnf (yum in AL2)
  - **Architectures:** noarch
  - **AL2 version:** 3.4.3-158.amzn2.0.7
  - **AL2023.12 version:** 4.14.0-1.amzn2023.0.7

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dnsmasq-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.76-16.amzn2.1.6
  - **AL2023.12 version:** 2.90-1.amzn2023.0.3

- ** `docbook5-schemas` **
  - **RPM:**  docbook5-schemas
  - **Architectures:** noarch
  - **AL2 version:** 5.0-10.amzn2
  - **AL2023.12 version:** 5.1-3.amzn2023.0.2

- ** `docbook5-style-xsl` **
  - **RPM:**  docbook5-style-xsl
  - **Architectures:** noarch
  - **AL2 version:** 1.78.1-4.amzn2
  - **AL2023.12 version:** 1.79.2-11.amzn2023.0.2

- ** `docbook-dtds` **
  - **RPM:**  docbook-dtds
  - **Architectures:** noarch
  - **AL2 version:** 1.0-60.amzn2
  - **AL2023.12 version:** 1.0-77.amzn2023.0.2

- ** `docbook-style-dsssl` **
  - **RPM:**  docbook-style-dsssl
  - **Architectures:** noarch
  - **AL2 version:** 1.79-18.amzn2
  - **AL2023.12 version:** 1.79-31.amzn2023.0.2

- ** `docbook-style-xsl` **
  - **RPM:**  docbook-style-xsl
  - **Architectures:** noarch
  - **AL2 version:** 1.78.1-3.amzn2
  - **AL2023.12 version:** 1.79.2-14.amzn2023.0.2

- ** `docbook-utils` **
  - **RPM:**  docbook-utils  / **Architectures:** noarch
  - **RPM:**  docbook-utils-pdf  / **Architectures:** noarch
  - **AL2 version:** 0.6.14-36.amzn2
  - **AL2023.12 version:** 0.6.14-52.amzn2023.0.2

- ** `dom4j` **
  - **RPM:**  dom4j  / **Architectures:** noarch
  - **RPM:**  dom4j-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.6.1-20.1.amzn2
  - **AL2023.12 version:** 2.0.3-4.amzn2023.0.1

- ** `dos2unix` **
  - **RPM:**  dos2unix
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.0.3-7.amzn2.0.3
  - **AL2023.12 version:** 7.4.2-2.amzn2023.0.2

- ** `dosfstools` **
  - **RPM:**  dosfstools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.20-10.amzn2
  - **AL2023.12 version:** 4.2-1.amzn2023.0.2

- ** `dotconf` **
  - **RPM:**  dotconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotconf-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3-8.amzn2.0.2
  - **AL2023.12 version:** 1.3-26.amzn2023.0.2

- ** `dovecot` **
  - **RPM:**  dovecot  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dovecot-pigeonhole  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.36-6.amzn2.1.3
  - **AL2023.12 version:** 2.3.20-1.amzn2023.0.3

- ** `doxygen` **
  - **RPM:**  doxygen  / **Architectures:** aarch64, x86\_64
  - **RPM:**  doxygen-latex  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.5-4.amzn2
  - **AL2023.12 version:** 1.12.0-2.amzn2023.0.1

- ** `dracut` **
  - **RPM:**  dracut  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-caps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-generic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-config-rescue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dracut-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 033-535.amzn2.1.7
  - **AL2023.12 version:** 102-3.amzn2023.0.3

- ** `dracut-config-ec2` **
  - **RPM:**  dracut-config-ec2
  - **Architectures:** noarch
  - **AL2 version:** 2.0-3.amzn2
  - **AL2023.12 version:** 3.1-1.amzn2023.0.1

- ** `drbd` **
  - **RPM:**  drbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  drbd-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.9.6-1
  - **AL2023.12 version:** 9.33.0-1.amzn2023.0.1

- ** `dtc` **
  - **RPM:**  dtc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfdt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfdt-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.7-1.amzn2.0.1
  - **AL2023.12 version:** 1.6.1-4.amzn2023.0.2

- ** `dwarves` **
  - **RPM:**  dwarves  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarves1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarves1-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.22-1.amzn2
  - **AL2023.12 version:** 1.29-1.amzn2023.0.2

- ** `dwz` **
  - **RPM:**  dwz
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.11-3.amzn2.0.3
  - **AL2023.12 version:** 0.16-2.amzn2023.0.1

- ** `dyninst` **
  - **RPM:**  dyninst  / **Architectures:** x86\_64
  - **RPM:**  dyninst-devel  / **Architectures:** x86\_64
  - **RPM:**  dyninst-doc  / **Architectures:** x86\_64
  - **RPM:**  dyninst-testsuite  / **Architectures:** x86\_64
  - **AL2 version:** 9.3.1-3.amzn2
  - **AL2023.12 version:** 10.2.1-6.amzn2023.0.2

- ** `e2fsprogs` **
  - **RPM:**  e2fsprogs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  e2fsprogs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  e2fsprogs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  e2fsprogs-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcom\_err  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcom\_err-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libss-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.42.9-19.amzn2.0.1
  - **AL2023.12 version:** 1.46.5-2.amzn2023.0.2

- ** `easymock` **
  - **RPM:**  easymock  / **Architectures:** noarch
  - **RPM:**  easymock-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2-22.amzn2
  - **AL2023.12 version:** 4.2-7.amzn2023.0.3

- ** `ec2-hibinit-agent` **
  - **RPM:**  ec2-hibinit-agent
  - **Architectures:** noarch
  - **AL2 version:** 1.0.11-1.amzn2
  - **AL2023.12 version:** 1.0.11-0.amzn2023

- ** [`ec2-instance-connect`](https://docs.aws.amazon.com/linux/al2023/ug/connecting-to-instances.html) **
  - **RPM:**  [`ec2-instance-connect`](https://docs.aws.amazon.com/linux/al2023/ug/connecting-to-instances.html)
  - **Architectures:** noarch
  - **AL2 version:** 1.1-19.amzn2
  - **AL2023.12 version:** 1.1-19.amzn2023

- ** `ec2-instance-connect-selinux` **
  - **RPM:**  ec2-instance-connect-selinux
  - **Architectures:** noarch
  - **AL2 version:** 1.1-19.amzn2
  - **AL2023.12 version:** 1.1-19.amzn2023

- ** `ec2rl` **
  - **RPM:**  ec2rl
  - **Architectures:** noarch
  - **AL2 version:** 1.1.6-1.amzn2.0.2
  - **AL2023.12 version:** 1.1.7-1.amzn2023

- ** `ec2-utils` **
  - **RPM:**  ec2-utils
  - **Architectures:** noarch
  - **AL2 version:** 1.2-48.amzn2
  - **AL2023.12 version:** 2.2.0-1.amzn2023.0.2

- ** `ed` **
  - **RPM:**  ed
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9-4.amzn2.0.2
  - **AL2023.12 version:** 1.14.2-10.amzn2023.0.2

- ** `efibootmgr` **
  - **RPM:**  efibootmgr
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 15-2.amzn2.0.2
  - **AL2023.12 version:** 18-6.amzn2023

- ** `efitools` **
  - **RPM:**  efitools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.2-7.amzn2.0.1
  - **AL2023.12 version:** 1.9.2-7.amzn2023.0.3

- ** `efivar` **
  - **RPM:**  efivar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  efivar-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  efivar-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 31-4.amzn2.0.4
  - **AL2023.12 version:** 38-2.amzn2023.0.1

- ** `elfutils` **
  - **RPM:**  elfutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  elfutils-default-yama-scope  / **Architectures:** noarch
  - **RPM:**  elfutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  elfutils-libelf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  elfutils-libelf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  elfutils-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.176-2.amzn2.0.2
  - **AL2023.12 version:** 0.188-3.amzn2023.0.3

- ** `elinks` **
  - **RPM:**  elinks
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12-0.57.pre6.amzn2.0.2
  - **AL2023.12 version:** 0.12-0.65.pre6.amzn2023.0.2

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2 version:** 27.2-4.amzn2.0.7
  - **AL2023.12 version:** 28.2-3.amzn2023.0.10

- ** `emacs-auctex` **
  - **RPM:**  emacs-auctex  / **Architectures:** noarch
  - **RPM:**  emacs-auctex-doc  / **Architectures:** noarch
  - **RPM:**  tex-preview  / **Architectures:** noarch
  - **AL2 version:** 11.87-4.amzn2
  - **AL2023.12 version:** 12.3-1.amzn2023.0.2

- ** `enchant` **
  - **RPM:**  enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  enchant-aspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  enchant-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  enchant-voikko  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.0-8.amzn2.0.2
  - **AL2023.12 version:** 1.6.0-27.amzn2023.0.2

- ** `environment-modules` **
  - **RPM:**  environment-modules
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2.10-10.amzn2.0.2
  - **AL2023.12 version:** 4.8.0-1.amzn2023.0.2

- ** `espeak` **
  - **RPM:**  espeak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  espeak-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.47.11-4.amzn2.0.2
  - **AL2023.12 version:** 1.48.04-32.amzn2023

- ** `ethtool` **
  - **RPM:**  ethtool
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.8-10.amzn2
  - **AL2023.12 version:** 5.15-1.amzn2023.0.2

- ** `evolution-data-server` **
  - **RPM:**  evolution-data-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-doc  / **Architectures:** noarch
  - **RPM:**  evolution-data-server-langpacks  / **Architectures:** noarch
  - **RPM:**  evolution-data-server-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.5-4.amzn2.0.2
  - **AL2023.12 version:** 3.54.3-1.amzn2023.0.2

- ** `exec-maven-plugin` **
  - **RPM:**  exec-maven-plugin  / **Architectures:** noarch
  - **RPM:**  exec-maven-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2.1-13.amzn2
  - **AL2023.12 version:** 3.0.0-4.amzn2023.0.1

- ** `execstack` **
  - **RPM:**  execstack
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.5.0-22.amzn2
  - **AL2023.12 version:** 0.5.0-20.amzn2023.0.2

- ** `exempi` **
  - **RPM:**  exempi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exempi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.0-9.amzn2.0.1
  - **AL2023.12 version:** 2.6.4-6.amzn2023

- ** `exiv2` **
  - **RPM:**  exiv2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exiv2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  exiv2-doc  / **Architectures:** noarch
  - **RPM:**  exiv2-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.27.0-4.amzn2.0.7
  - **AL2023.12 version:** 0.28.5-132.amzn2023

- ** `expat` **
  - **RPM:**  expat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expat-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.0-15.amzn2.0.8
  - **AL2023.12 version:** 2.6.3-1.amzn2023.0.6

- ** `expect` **
  - **RPM:**  expect  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expect-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  expectk  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.45-14.amzn2.0.2
  - **AL2023.12 version:** 5.45.4-13.amzn2023.0.2

- ** `felix-parent` **
  - **RPM:**  felix-parent
  - **Architectures:** noarch
  - **AL2 version:** 1.2.1-15.amzn2
  - **AL2023.12 version:** 7-8.amzn2023.0.3

- ** `felix-utils` **
  - **RPM:**  felix-utils  / **Architectures:** noarch
  - **RPM:**  felix-utils-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2.0-5.amzn2
  - **AL2023.12 version:** 1.11.6-5.amzn2023.0.3

- ** `fetchmail` **
  - **RPM:**  fetchmail
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.3.24-7.amzn2.0.2
  - **AL2023.12 version:** 6.5.7-1.amzn2023

- ** `fftw` **
  - **RPM:**  fftw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-doc  / **Architectures:** noarch
  - **RPM:**  fftw-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-libs-double  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-libs-long  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-libs-single  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fftw-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.3-8.amzn2.0.2
  - **AL2023.12 version:** 3.3.8-10.amzn2023.0.2

- ** `file` **
  - **RPM:**  file  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  file-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.11-36.amzn2.0.1
  - **AL2023.12 version:** 5.39-7.amzn2023.0.4

- ** `filesystem` **
  - **RPM:**  filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  filesystem-content  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2-25.amzn2.0.4
  - **AL2023.12 version:** 3.14-5.amzn2023.0.3

- ** `findutils` **
  - **RPM:**  findutils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.5.11-6.amzn2
  - **AL2023.12 version:** 4.8.0-2.amzn2023.0.2

- ** `fio` **
  - **RPM:**  fio
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.14-1.amzn2.0.3
  - **AL2023.12 version:** 3.32-2.amzn2023.0.3

- ** `firewalld` **
  - **RPM:**  firewalld  / **Architectures:** noarch
  - **RPM:**  firewalld-filesystem  / **Architectures:** noarch
  - **AL2 version:** 0.4.4.4-6.amzn2.0.1
  - **AL2023.12 version:** 1.2.3-1.amzn2023.0.2

- ** `flac` **
  - **RPM:**  flac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flac-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flac-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.0-5.amzn2.0.5
  - **AL2023.12 version:** 1.3.4-1.amzn2023.0.2

- ** `flatpak` **
  - **RPM:**  flatpak  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flatpak-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.9-10.amzn2.0.7
  - **AL2023.12 version:** 1.16.6-1.amzn2023

- ** `flex` **
  - **RPM:**  flex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  flex-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.37-3.amzn2.0.3
  - **AL2023.12 version:** 2.6.4-7.amzn2023.0.2

- ** `fltk` **
  - **RPM:**  fltk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fltk-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fltk-fluid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fltk-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.4-1.amzn2.0.2
  - **AL2023.12 version:** 1.3.6-1.amzn2023.0.2

- ** `fontawesome-fonts` **
  - **RPM:**  fontawesome-fonts  / **Architectures:** noarch
  - **RPM:**  fontawesome-fonts-web  / **Architectures:** noarch
  - **AL2 version:** 4.1.0-2.amzn2
  - **AL2023.12 version:** 4.7.0-11.amzn2023.0.2

- ** `fontconfig` **
  - **RPM:**  fontconfig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fontconfig-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fontconfig-devel-doc  / **Architectures:** noarch
  - **AL2 version:** 2.13.0-4.3.amzn2
  - **AL2023.12 version:** 2.13.94-2.amzn2023.0.2

- ** `fontforge` **
  - **RPM:**  fontforge  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fontforge-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20120731b-13.amzn2.0.5
  - **AL2023.12 version:** 20201107-3.amzn2023.0.6

- ** `freeglut` **
  - **RPM:**  freeglut  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeglut-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.0-8.amzn2
  - **AL2023.12 version:** 3.2.1-7.amzn2023.0.2

- ** `freeipmi` **
  - **RPM:**  freeipmi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipmi-bmc-watchdog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipmi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipmi-ipmidetectd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeipmi-ipmiseld  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.7-3.amzn2
  - **AL2023.12 version:** 1.6.15-159.amzn2023

- ** `freeradius` **
  - **RPM:**  freeradius  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-krb5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-postgresql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-unixODBC  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.27-1.amzn2.0.1
  - **AL2023.12 version:** 3.2.5-4.amzn2023.0.1

- ** `freerdp` **
  - **RPM:**  freerdp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freerdp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freerdp-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwinpr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwinpr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.11.7-1.amzn2.0.13
  - **AL2023.12 version:** 3.6.3-1.amzn2023.0.14

- ** `freetype` **
  - **RPM:**  freetype  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-demos  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freetype-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.8-14.amzn2.1.4
  - **AL2023.12 version:** 2.13.2-5.amzn2023.0.2

- ** `fribidi` **
  - **RPM:**  fribidi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fribidi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-1.amzn2.1.2
  - **AL2023.12 version:** 1.0.11-3.amzn2023.0.2

- ** `fuse` **
  - **RPM:**  fuse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fuse-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fuse-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.2-11.amzn2
  - **AL2023.12 version:** 2.9.9-13.amzn2023.0.2

- ** `fusesource-pom` **
  - **RPM:**  fusesource-pom
  - **Architectures:** noarch
  - **AL2 version:** 1.9-7.amzn2
  - **AL2023.12 version:** 1.12-10.amzn2023.0.4

- ** `gawk` **
  - **RPM:**  gawk
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0.2-4.amzn2.1.3
  - **AL2023.12 version:** 5.1.0-3.amzn2023.0.4

- ** `gc` **
  - **RPM:**  gc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.6.4-3.amzn2.0.2
  - **AL2023.12 version:** 8.0.4-5.amzn2023.0.2

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.3.1-18.amzn2
  - **AL2023.12 version:** 11.5.0-5.amzn2023.0.5

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (`gcc10` in AL2) **
  - **RPM:**  cpp (cpp10 in AL2)  / **Architectures:**
  - **RPM:**  [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (gcc10 in AL2)  / **Architectures:**
  - **RPM:**  gcc-c\+\+ (gcc10-c\+\+ in AL2)  / **Architectures:**
  - **RPM:**  gcc-gdb-plugin (gcc10-gdb-plugin in AL2)  / **Architectures:**
  - **RPM:**  gcc-gfortran (gcc10-gfortran in AL2)  / **Architectures:**
  - **RPM:**  gcc-plugin-devel (gcc10-plugin-devel in AL2)  / **Architectures:**
  - **RPM:**  libasan (libasan10 in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-devel (libitm10-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-devel (libstdc\+\+10-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs (libstdc\+\+10-docs in AL2)  / **Architectures:**
  - **AL2 version:** 10.5.0-1.amzn2.0.3
  - **AL2023.12 version:** 11.5.0-5.amzn2023.0.5

- ** `gcr` **
  - **RPM:**  gcr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.0-1.amzn2
  - **AL2023.12 version:** 4.3.0-3.amzn2023.0.1

- ** `gd` **
  - **RPM:**  gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gd-progs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.35-27.amzn2.0.1
  - **AL2023.12 version:** 2.3.3-5.amzn2023.0.3

- ** `gdb` **
  - **RPM:**  gdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdb-doc  / **Architectures:** noarch
  - **RPM:**  gdb-gdbserver  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.0.1-36.amzn2.0.2
  - **AL2023.12 version:** 16.3-1.amzn2023.0.1

- ** `gdbm` **
  - **RPM:**  gdbm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdbm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.13-6.amzn2.0.2
  - **AL2023.12 version:** 1.19-2.amzn2023.0.2

- ** `gdisk` **
  - **RPM:**  gdisk
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.10-3.amzn2
  - **AL2023.12 version:** 1.0.8-1.amzn2023.0.2

- ** `gdk-pixbuf2` **
  - **RPM:**  gdk-pixbuf2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdk-pixbuf2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.36.12-3.amzn2.0.3
  - **AL2023.12 version:** 2.42.12-185.amzn2023

- ** `gdm` **
  - **RPM:**  gdm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdm-pam-extensions-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-16.amzn2.0.2
  - **AL2023.12 version:** 47.0-970.amzn2023

- ** `generic-logos` **
  - **RPM:**  generic-logos  / **Architectures:** noarch
  - **RPM:**  generic-logos-httpd  / **Architectures:** noarch
  - **AL2 version:** 18.0.0-4.amzn2
  - **AL2023.12 version:** 18.0.0-12.amzn2023.0.3

- ** `geoclue2` **
  - **RPM:**  geoclue2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-demos  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geoclue2-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.5-1.amzn2.0.2
  - **AL2023.12 version:** 2.7.0-6.amzn2023.0.2

- ** `geocode-glib` **
  - **RPM:**  geocode-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  geocode-glib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.20.1-1.amzn2.0.2
  - **AL2023.12 version:** 3.26.4-1.amzn2023.0.2

- ** `gettext` **
  - **RPM:**  emacs-gettext  / **Architectures:** noarch
  - **RPM:**  gettext  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gettext-common-devel  / **Architectures:** noarch
  - **RPM:**  gettext-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gettext-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.19.8.1-3.amzn2
  - **AL2023.12 version:** 0.21-4.amzn2023.0.2

- ** `ghostscript` **
  - **RPM:**  ghostscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ghostscript-doc  / **Architectures:** noarch
  - **RPM:**  ghostscript-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.54.0-9.amzn2.0.13
  - **AL2023.12 version:** 9.56.1-7.amzn2023.0.19

- ** `giflib` **
  - **RPM:**  giflib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  giflib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  giflib-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.1.6-9.amzn2.0.5
  - **AL2023.12 version:** 5.2.1-9.amzn2023.0.4

- ** `git` **
  - **RPM:**  git  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-all  / **Architectures:** noarch
  - **RPM:**  git-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-core-doc  / **Architectures:** noarch
  - **RPM:**  git-credential-libsecret  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-cvs  / **Architectures:** noarch
  - **RPM:**  git-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-email  / **Architectures:** noarch
  - **RPM:**  git-gui  / **Architectures:** noarch
  - **RPM:**  git-instaweb  / **Architectures:** noarch
  - **RPM:**  gitk  / **Architectures:** noarch
  - **RPM:**  git-p4  / **Architectures:** noarch
  - **RPM:**  git-subtree  / **Architectures:** noarch
  - **RPM:**  git-svn  / **Architectures:** noarch
  - **RPM:**  gitweb  / **Architectures:** noarch
  - **RPM:**  perl-Git  / **Architectures:** noarch
  - **RPM:**  perl-Git-SVN  / **Architectures:** noarch
  - **AL2 version:** 2.47.3-1.amzn2.0.1
  - **AL2023.12 version:** 2.50.1-1.amzn2023.0.1

- ** `gjs` **
  - **RPM:**  gjs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gjs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gjs-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.52.5-1.amzn2
  - **AL2023.12 version:** 1.80.2-11.amzn2023.0.1

- ** `glew` **
  - **RPM:**  glew  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glew-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libGLEW  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.10.0-5.amzn2.0.2
  - **AL2023.12 version:** 2.1.0-9.amzn2023.0.2

- ** `glib2` **
  - **RPM:**  glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-doc  / **Architectures:** noarch
  - **RPM:**  glib2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.56.1-9.amzn2.0.15
  - **AL2023.12 version:** 2.82.2-771.amzn2023

- ** [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html) **
  - **RPM:**  [`glibc`](https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-all-langpacks  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-benchtests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-aa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-af  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  glibc-langpack-bn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-br  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-brx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-bs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-byn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ca  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-chr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cmn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-crh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-csb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-cy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-da  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-de  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-doi  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  glibc-langpack-mg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mhr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-ml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-mni  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  glibc-langpack-sat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-se  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sgs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-shs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-si  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-sl  / **Architectures:** aarch64, x86\_64
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
  - **RPM:**  glibc-langpack-zh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-langpack-zu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-locale-source  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-minimal-langpack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibc-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nscd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_db  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss\_hesiod  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.26-64.amzn2.0.6
  - **AL2023.12 version:** 2.34-231.amzn2023.0.5

- ** `glibmm24` **
  - **RPM:**  glibmm24  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm24-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glibmm24-doc  / **Architectures:** noarch
  - **AL2 version:** 2.56.0-1.amzn2
  - **AL2023.12 version:** 2.66.2-1.amzn2023.0.2

- ** `glib-networking` **
  - **RPM:**  glib-networking  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib-networking-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.56.1-1.amzn2
  - **AL2023.12 version:** 2.80.0-186.amzn2023.0.1

- ** `gl-manpages` **
  - **RPM:**  gl-manpages
  - **Architectures:** noarch
  - **AL2 version:** 1.1-7.20130122.amzn2
  - **AL2023.12 version:** 1.1-22.20190306.amzn2023.0.2

- ** `gmp` **
  - **RPM:**  gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gmp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gmp-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.0.0-15.amzn2.0.3
  - **AL2023.12 version:** 6.2.1-2.amzn2023.0.2

- ** `gnome-backgrounds` **
  - **RPM:**  gnome-backgrounds
  - **Architectures:** noarch
  - **AL2 version:** 3.28.0-1.amzn2
  - **AL2023.12 version:** 47.0-1.amzn2023

- ** `gnome-calculator` **
  - **RPM:**  gnome-calculator
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-1.amzn2
  - **AL2023.12 version:** 47.2-1.amzn2023.0.1

- ** `gnome-common` **
  - **RPM:**  gnome-common
  - **Architectures:** noarch
  - **AL2 version:** 3.18.0-1.amzn2
  - **AL2023.12 version:** 3.18.0-20.amzn2023

- ** `gnome-desktop3` **
  - **RPM:**  gnome-desktop3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop3-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-2.amzn2
  - **AL2023.12 version:** 44.1-332.amzn2023

- ** `gnome-keyring` **
  - **RPM:**  gnome-keyring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-keyring-pam  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-1.amzn2
  - **AL2023.12 version:** 46.2-341.amzn2023

- ** `gnome-menus` **
  - **RPM:**  gnome-menus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-menus-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.13.3-3.amzn2.0.2
  - **AL2023.12 version:** 3.36.0-12.amzn2023.0.1

- ** `gnome-online-accounts` **
  - **RPM:**  gnome-online-accounts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-online-accounts-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.26.2-1.amzn2.0.1
  - **AL2023.12 version:** 3.53.0-253.amzn2023.0.1

- ** `gnome-session` **
  - **RPM:**  gnome-session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-session-wayland-session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-session-xsession  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.1-7.amzn2
  - **AL2023.12 version:** 47.0.1-575.amzn2023

- ** `gnome-settings-daemon` **
  - **RPM:**  gnome-settings-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-settings-daemon-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.1-5.amzn2.0.2
  - **AL2023.12 version:** 47.2-608.amzn2023

- ** `gnome-shell` **
  - **RPM:**  gnome-shell
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.3-34.amzn2.0.1
  - **AL2023.12 version:** 47.3-705.amzn2023

- ** `gnome-shell-extensions` **
  - **RPM:**  gnome-classic-session  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-apps-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-auto-move-windows  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-common  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-drive-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-launch-new-instance  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-native-window-placement  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-places-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-screenshot-window-sizer  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-user-theme  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-window-list  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-windowsNavigator  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-workspace-indicator  / **Architectures:** noarch
  - **AL2 version:** 3.26.2-3.amzn2.0.1
  - **AL2023.12 version:** 47.1-275.amzn2023

- ** `gnome-system-monitor` **
  - **RPM:**  gnome-system-monitor
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-1.amzn2.0.1
  - **AL2023.12 version:** 47.0-1.amzn2023

- ** `gnome-user-docs` **
  - **RPM:**  gnome-user-docs
  - **Architectures:** noarch
  - **AL2 version:** 3.28.2-1.amzn2
  - **AL2023.12 version:** 47.6-1.amzn2023

- ** `gnu-efi` **
  - **RPM:**  gnu-efi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnu-efi-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.8-4.amzn2.0.1
  - **AL2023.12 version:** 3.0.11-9.amzn2023.0.2

- ** [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal) **
  - **RPM:**  [`gnupg2`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#gnupg-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnupg2-smime  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.22-5.amzn2.0.6
  - **AL2023.12 version:** 2.3.7-1.amzn2023.0.9

- ** `gnuplot` **
  - **RPM:**  gnuplot-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnuplot-doc  / **Architectures:** noarch
  - **RPM:**  gnuplot-latex  / **Architectures:** noarch
  - **RPM:**  gnuplot-minimal  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.6.2-3.amzn2.0.2
  - **AL2023.12 version:** 5.4.3-3.amzn2023.0.4

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.29-9.amzn2.0.4
  - **AL2023.12 version:** 3.8.10-4.amzn2023.0.2

- ** `gobject-introspection` **
  - **RPM:**  gobject-introspection  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gobject-introspection-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.56.1-1.amzn2
  - **AL2023.12 version:** 1.82.0-1.amzn2023

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-race  / **Architectures:** x86\_64
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2 version:** 1.25.12-1.amzn2.0.1
  - **AL2023.12 version:** 1.25.12-1.amzn2023.0.1

- ** `golist` **
  - **RPM:**  golist
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.10.1-10.amzn2.0.15
  - **AL2023.12 version:** 0.10.4-12.amzn2023.0.11

- ** `google-guice` **
  - **RPM:**  google-guice  / **Architectures:** noarch
  - **RPM:**  google-guice-javadoc  / **Architectures:** noarch
  - **RPM:**  guice-parent  / **Architectures:** noarch
  - **AL2 version:** 3.1.3-9.amzn2
  - **AL2023.12 version:** 4.2.3-8.amzn2023.0.6

- ** `google-noto-emoji-fonts` **
  - **RPM:**  google-noto-emoji-color-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-emoji-fonts  / **Architectures:** noarch
  - **AL2 version:** 20180508-4.amzn2
  - **AL2023.12 version:** 20200916-2.amzn2023.0.2

- ** `google-noto-fonts` **
  - **RPM:**  google-noto-fonts-common  / **Architectures:** noarch
  - **RPM:**  google-noto-kufi-arabic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-naskh-arabic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-naskh-arabic-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-armenian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-avestan-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-balinese-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-bamum-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-batak-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-bengali-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-bengali-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-brahmi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-buginese-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-buhid-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-canadian-aboriginal-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-carian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-cham-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-cherokee-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-coptic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-cuneiform-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-cypriot-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-deseret-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-devanagari-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-devanagari-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-egyptian-hieroglyphs-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-ethiopic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-georgian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-glagolitic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-gothic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-gujarati-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-gujarati-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-gurmukhi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-gurmukhi-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-hanunoo-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-hebrew-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-imperial-aramaic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-inscriptional-pahlavi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-inscriptional-parthian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-javanese-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-kaithi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-kannada-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-kannada-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-kayah-li-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-kharoshthi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-khmer-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-khmer-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lao-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lao-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lepcha-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-limbu-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-linear-b-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lisu-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lycian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-lydian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-malayalam-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-malayalam-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-mandaic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-meetei-mayek-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-mongolian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-myanmar-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-myanmar-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-new-tai-lue-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-nko-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-ogham-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-ol-chiki-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-old-italic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-old-persian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-old-south-arabian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-old-turkic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-osmanya-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-phags-pa-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-phoenician-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-rejang-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-runic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-samaritan-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-saurashtra-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-shavian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-sinhala-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-sundanese-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-syloti-nagri-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-symbols-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-syriac-eastern-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-syriac-western-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tagalog-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tagbanwa-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tai-le-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tai-tham-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tai-viet-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tamil-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tamil-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-telugu-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-telugu-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-thaana-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-thai-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-thai-ui-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-tifinagh-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-ugaritic-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-vai-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-sans-yi-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-armenian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-georgian-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-khmer-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-lao-fonts  / **Architectures:** noarch
  - **RPM:**  google-noto-serif-thai-fonts  / **Architectures:** noarch
  - **AL2 version:** 20141117-5.amzn2
  - **AL2023.12 version:** 20240401-1.amzn2023.0.2

- ** `go-rpm-macros` **
  - **RPM:**  go-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  go-rpm-macros  / **Architectures:** aarch64, x86\_64
  - **RPM:**  go-srpm-macros  / **Architectures:** noarch
  - **AL2 version:** 3.0.15-23.amzn2.0.2
  - **AL2023.12 version:** 3.8.0-1.amzn2023.0.1

- ** `gperf` **
  - **RPM:**  gperf
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.4-8.amzn2.0.2
  - **AL2023.12 version:** 3.1-11.amzn2023.0.2

- ** `gperftools` **
  - **RPM:**  gperftools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gperftools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gperftools-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pprof  / **Architectures:** noarch
  - **AL2 version:** 2.6.1-1.amzn2
  - **AL2023.12 version:** 2.9.1-1.amzn2023.0.3

- ** `gpgme` **
  - **RPM:**  gpgme  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gpgme-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.2-5.amzn2.0.2
  - **AL2023.12 version:** 1.23.2-182.amzn2023.0.1

- ** `gpm` **
  - **RPM:**  gpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gpm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gpm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gpm-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.20.7-15.amzn2.0.2
  - **AL2023.12 version:** 1.20.7-26.amzn2023.amzn2023.0.3

- ** `graphene` **
  - **RPM:**  graphene  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphene-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphene-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.10.6-2.amzn2.0.2
  - **AL2023.12 version:** 1.10.6-9.amzn2023.0.1

- ** `graphite2` **
  - **RPM:**  graphite2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphite2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.10-1.amzn2.0.3
  - **AL2023.12 version:** 1.3.14-7.amzn2023.0.3

- ** `graphviz` **
  - **RPM:**  graphviz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-graphs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-ocaml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  graphviz-tcl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.30.1-21.amzn2.0.1
  - **AL2023.12 version:** 2.44.0-25.amzn2023.0.7

- ** `grep` **
  - **RPM:**  grep
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.20-3.amzn2.0.2
  - **AL2023.12 version:** 3.8-1.amzn2023.0.4

- ** `groff` **
  - **RPM:**  groff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  groff-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  groff-doc  / **Architectures:** noarch
  - **RPM:**  groff-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  groff-x11  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.22.2-8.amzn2.0.2
  - **AL2023.12 version:** 1.22.4-7.amzn2023.0.2

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
  - **AL2 version:** 2.06-14.amzn2.0.7
  - **AL2023.12 version:** 2.06-61.amzn2023.0.22

- ** `grubby` **
  - **RPM:**  grubby
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.28-23.amzn2.0.3
  - **AL2023.12 version:** 8.40-73.amzn2023.0.1

- ** `gsettings-desktop-schemas` **
  - **RPM:**  gsettings-desktop-schemas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsettings-desktop-schemas-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.0-3.amzn2.0.1
  - **AL2023.12 version:** 47.1-206.amzn2023

- ** `gsl` **
  - **RPM:**  gsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.15-13.amzn2.0.3
  - **AL2023.12 version:** 2.6-4.amzn2023.0.5

- ** `gsm` **
  - **RPM:**  gsm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsm-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.13-11.amzn2.0.2
  - **AL2023.12 version:** 1.0.19-5.amzn2023.0.3

- ** `gsound` **
  - **RPM:**  gsound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsound-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-2.amzn2.0.2
  - **AL2023.12 version:** 1.0.3-9.amzn2023.0.1

- ** `gssdp` **
  - **RPM:**  gssdp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gssdp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gssdp-docs  / **Architectures:** noarch
  - **RPM:**  gssdp-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-1.amzn2
  - **AL2023.12 version:** 1.6.3-3.amzn2023.0.1

- ** `gssproxy` **
  - **RPM:**  gssproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.0-17.amzn2
  - **AL2023.12 version:** 0.9.2-6.amzn2023.0.1

- ** `gstreamer1` **
  - **RPM:**  gstreamer1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.18.4-4.amzn2.0.2
  - **AL2023.12 version:** 1.24.10-1.amzn2023.0.1

- ** `gstreamer1-plugins-bad-free` **
  - **RPM:**  gstreamer1-plugins-bad-free  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-bad-free-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.18.4-5.amzn2.0.8
  - **AL2023.12 version:** 1.24.10-1.amzn2023.0.8

- ** `gstreamer1-plugins-base` **
  - **RPM:**  gstreamer1-plugins-base  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-base-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-base-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.18.4-5.amzn2.0.10
  - **AL2023.12 version:** 1.24.10-1.amzn2023.0.3

- ** `gstreamer1-plugins-good` **
  - **RPM:**  gstreamer1-plugins-good  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-good-gtk  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.18.4-6.amzn2.0.12
  - **AL2023.12 version:** 1.24.10-1.amzn2023.0.7

- ** `gtest` **
  - **RPM:**  gtest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtest-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.0-11.amzn2.0.1
  - **AL2023.12 version:** 1.11.0-1.amzn2023.0.3

- ** `gtk3` **
  - **RPM:**  gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-devel-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-immodules  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-immodule-xim  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk3-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk-update-icon-cache  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.22.30-3.amzn2.0.1
  - **AL2023.12 version:** 3.24.43-1.amzn2023.0.1

- ** `gtk-doc` **
  - **RPM:**  gtk-doc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.28-2.amzn2
  - **AL2023.12 version:** 1.34.0-2.amzn2023.0.1

- ** `guava` **
  - **RPM:**  guava  / **Architectures:** noarch
  - **RPM:**  guava-javadoc  / **Architectures:** noarch
  - **AL2 version:** 13.0-6.amzn2
  - **AL2023.12 version:** 31.0.1-3.amzn2023.0.6

- ** `gvfs` **
  - **RPM:**  gvfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-archive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-fuse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-goa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-smb  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.36.2-3.amzn2.0.2
  - **AL2023.12 version:** 1.56.1-1.amzn2023.0.2

- ** `gzip` **
  - **RPM:**  gzip
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5-10.amzn2.0.1
  - **AL2023.12 version:** 1.12-1.amzn2023.0.1

- ** `hamcrest` **
  - **RPM:**  hamcrest  / **Architectures:** noarch
  - **RPM:**  hamcrest-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.3-6.1.amzn2
  - **AL2023.12 version:** 2.2-7.amzn2023.0.3

- ** `haproxy` **
  - **RPM:**  haproxy
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.18-9.amzn2
  - **AL2023.12 version:** 3.0.23-2.amzn2023.0.1

- ** `harfbuzz` **
  - **RPM:**  harfbuzz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  harfbuzz-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  harfbuzz-icu  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.5-2.amzn2.0.2
  - **AL2023.12 version:** 7.0.0-2.amzn2023.0.2

- ** `hawtjni` **
  - **RPM:**  hawtjni  / **Architectures:** noarch
  - **RPM:**  hawtjni-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-hawtjni-plugin  / **Architectures:** noarch
  - **AL2 version:** 1.6-10.amzn2
  - **AL2023.12 version:** 1.18-4.amzn2023.0.2

- ** `hdparm` **
  - **RPM:**  hdparm
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.43-5.amzn2.0.2
  - **AL2023.12 version:** 9.65-1.amzn2023.0.1

- ** `help2man` **
  - **RPM:**  help2man
  - **Architectures:** noarch
  - **AL2 version:** 1.41.1-3.amzn2
  - **AL2023.12 version:** 1.48.5-1.amzn2023.0.3

- ** `hicolor-icon-theme` **
  - **RPM:**  hicolor-icon-theme
  - **Architectures:** noarch
  - **AL2 version:** 0.12-7.amzn2
  - **AL2023.12 version:** 0.17-10.amzn2023.0.3

- ** `highlight` **
  - **RPM:**  highlight
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.13-3.amzn2.0.2
  - **AL2023.12 version:** 4.2-2.amzn2023.0.4

- ** `hostname` **
  - **RPM:**  hostname
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.13-3.amzn2.0.2
  - **AL2023.12 version:** 3.23-4.amzn2023.0.3

- ** `html2ps` **
  - **RPM:**  html2ps  / **Architectures:** noarch
  - **RPM:**  xhtml2ps  / **Architectures:** noarch
  - **AL2 version:** 1.0-0.14.b7.amzn2
  - **AL2023.12 version:** 1.0-0.39.b7.amzn2023.0.3

- ** `htop` **
  - **RPM:**  htop
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.2-1.amzn2.0.2
  - **AL2023.12 version:** 3.2.1-87.amzn2023.0.3

- ** `httpcomponents-client` **
  - **RPM:**  httpcomponents-client  / **Architectures:** noarch
  - **RPM:**  httpcomponents-client-javadoc  / **Architectures:** noarch
  - **AL2 version:** 4.2.5-5.amzn2.0.1
  - **AL2023.12 version:** 4.5.13-4.amzn2023.0.4

- ** `httpcomponents-core` **
  - **RPM:**  httpcomponents-core  / **Architectures:** noarch
  - **RPM:**  httpcomponents-core-javadoc  / **Architectures:** noarch
  - **AL2 version:** 4.2.4-6.amzn2.0.1
  - **AL2023.12 version:** 4.4.13-6.amzn2023.0.4

- ** `httpcomponents-project` **
  - **RPM:**  httpcomponents-project
  - **Architectures:** noarch
  - **AL2 version:** 6-4.amzn2
  - **AL2023.12 version:** 12-6.amzn2023.0.3

- ** `httpd` **
  - **RPM:**  httpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  httpd-filesystem  / **Architectures:** noarch
  - **RPM:**  httpd-manual  / **Architectures:** noarch
  - **RPM:**  httpd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_proxy\_html  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_ssl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.68-1.amzn2.0.1
  - **AL2023.12 version:** 2.4.68-1.amzn2023.0.1

- ** `hunspell` **
  - **RPM:**  hunspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hunspell-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.2-16.amzn2
  - **AL2023.12 version:** 1.7.0-9.amzn2023.0.3

- ** `hunspell-en` **
  - **RPM:**  hunspell-en  / **Architectures:** noarch
  - **RPM:**  hunspell-en-GB  / **Architectures:** noarch
  - **RPM:**  hunspell-en-US  / **Architectures:** noarch
  - **AL2 version:** 0.20121024-6.amzn2.0.1
  - **AL2023.12 version:** 0.20201207-10.amzn2023.0.1

- ** `hwloc` **
  - **RPM:**  hwloc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-gui  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  hwloc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.11.8-4.amzn2.0.2
  - **AL2023.12 version:** 2.4.1-3.amzn2023.0.6

- ** [`hyperv-daemons`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html) **
  - **RPM:**  [`hyperv-daemons`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** x86\_64
  - **RPM:**  [`hyperv-daemons-license`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** noarch
  - **RPM:**  [`hypervfcopyd`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** x86\_64
  - **RPM:**  [`hypervkvpd`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** x86\_64
  - **RPM:**  [`hyperv-tools`](https://docs.aws.amazon.com/linux/al2023/ug/hyperv-supported-configurations.html)  / **Architectures:** noarch
  - **RPM:**  hypervvssd  / **Architectures:** x86\_64
  - **AL2 version:** 0-0.32.20161211git.amzn2
  - **AL2023.12 version:** 0-0.42.20220731git.amzn2023.0.1

- ** `ibus` **
  - **RPM:**  ibus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-devel-docs  / **Architectures:** noarch
  - **RPM:**  ibus-gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-setup  / **Architectures:** noarch
  - **AL2 version:** 1.5.17-11.amzn2
  - **AL2023.12 version:** 1.5.31-1.amzn2023.0.2

- ** `ibus-hangul` **
  - **RPM:**  ibus-hangul
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.2-11.amzn2
  - **AL2023.12 version:** 1.5.5-6.amzn2023.0.1

- ** `ibus-libpinyin` **
  - **RPM:**  ibus-libpinyin
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.91-4.amzn2.0.2
  - **AL2023.12 version:** 1.15.8-1.amzn2023.0.1

- ** `ibus-m17n` **
  - **RPM:**  ibus-m17n
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.4-13.amzn2.0.3
  - **AL2023.12 version:** 1.4.35-164.amzn2023

- ** `ibus-table` **
  - **RPM:**  ibus-table  / **Architectures:** noarch
  - **RPM:**  ibus-table-devel  / **Architectures:** noarch
  - **AL2 version:** 1.5.0-5.amzn2
  - **AL2023.12 version:** 1.17.11-216.amzn2023

- ** `ibus-table-chinese` **
  - **RPM:**  ibus-table-chinese  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-array  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-cangjie  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-cantonese  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-easy  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-erbi  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-quick  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-scj  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-stroke5  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wu  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wubi-haifeng  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wubi-jidian  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-yong  / **Architectures:** noarch
  - **AL2 version:** 1.4.6-3.amzn2
  - **AL2023.12 version:** 1.8.12-6.amzn2023.0.1

- ** `icc-profiles-openicc` **
  - **RPM:**  icc-profiles-openicc
  - **Architectures:** noarch
  - **AL2 version:** 1.3.1-5.amzn2
  - **AL2023.12 version:** 1.3.1-20.amzn2023.0.3

- ** `icu` **
  - **RPM:**  icu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libicu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libicu-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libicu-doc  / **Architectures:** noarch
  - **AL2 version:** 50.2-4.amzn2.0.2
  - **AL2023.12 version:** 67.1-7.amzn2023.0.4

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.9.10.97-1.amzn2.0.31
  - **AL2023.12 version:** 6.9.13.50-1.amzn2023.0.2

- ** `indent` **
  - **RPM:**  indent
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.11-13.amzn2.0.4
  - **AL2023.12 version:** 2.2.12-7.amzn2023.0.6

- ** `infinipath-psm` **
  - **RPM:**  infinipath-psm  / **Architectures:** x86\_64
  - **RPM:**  infinipath-psm-devel  / **Architectures:** x86\_64
  - **AL2 version:** 3.3-26\_g604758e\_open.2.amzn2
  - **AL2023.12 version:** 3.3-26\_g604758e\_open.6.amzn2023.3.0.3

- ** `initscripts` **
  - **RPM:**  initscripts
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.49.47-1.amzn2.0.3
  - **AL2023.12 version:** 10.09-1.amzn2023.0.2

- ** `intltool` **
  - **RPM:**  intltool
  - **Architectures:** noarch
  - **AL2 version:** 0.50.2-7.amzn2
  - **AL2023.12 version:** 0.51.0-18.amzn2023.0.3

- ** `ipa-gothic-fonts` **
  - **RPM:**  ipa-gothic-fonts
  - **Architectures:** noarch
  - **AL2 version:** 003.03-5.amzn2
  - **AL2023.12 version:** 003.03-27.amzn2023

- ** `ipa-mincho-fonts` **
  - **RPM:**  ipa-mincho-fonts
  - **Architectures:** noarch
  - **AL2 version:** 003.03-5.amzn2
  - **AL2023.12 version:** 003.03-26.amzn2023

- ** `ipa-pgothic-fonts` **
  - **RPM:**  ipa-pgothic-fonts
  - **Architectures:** noarch
  - **AL2 version:** 003.03-5.amzn2
  - **AL2023.12 version:** 003.03-24.amzn2023

- ** `ipa-pmincho-fonts` **
  - **RPM:**  ipa-pmincho-fonts
  - **Architectures:** noarch
  - **AL2 version:** 003.03-5.amzn2
  - **AL2023.12 version:** 003.03-25.amzn2023

- ** `iperf3` **
  - **RPM:**  iperf3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iperf3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.7-2.amzn2.0.5
  - **AL2023.12 version:** 3.19.1-1.amzn2023

- ** `ipmitool` **
  - **RPM:**  bmc-snmp-proxy  / **Architectures:** noarch
  - **RPM:**  exchange-bmc-os-info  / **Architectures:** noarch
  - **RPM:**  ipmitool  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.18-9.amzn2
  - **AL2023.12 version:** 1.8.19-7.amzn2023

- ** `iproute` **
  - **RPM:**  iproute  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iproute-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iproute-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iproute-tc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.10.0-2.amzn2.0.3
  - **AL2023.12 version:** 6.10.0-319.amzn2023.0.1

- ** `ipset` **
  - **RPM:**  ipset  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ipset-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ipset-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ipset-service  / **Architectures:** noarch
  - **AL2 version:** 6.29-1.amzn2.0.1
  - **AL2023.12 version:** 7.11-1.amzn2023.0.3

- ** `iputils` **
  - **RPM:**  iputils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iputils-ninfod  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20180629-11.amzn2.1.20160308
  - **AL2023.12 version:** 20210202-2.amzn2023.0.4

- ** `ipvsadm` **
  - **RPM:**  ipvsadm
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.27-7.amzn2.0.2
  - **AL2023.12 version:** 1.31-9.amzn2023.0.1

- ** `irqbalance` **
  - **RPM:**  irqbalance
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.0-4.amzn2.0.1
  - **AL2023.12 version:** 1.9.0-1.amzn2023.0.3

- ** `iscsi-initiator-utils` **
  - **RPM:**  iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-iscsiuio  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.2.0.874-7.amzn2.0.1
  - **AL2023.12 version:** 6.2.1.4-10.git2a8f9d8.amzn2023.0.3

- ** `isl` **
  - **RPM:**  isl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  isl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.16.1-6.amzn2
  - **AL2023.12 version:** 0.16.1-13.amzn2023.0.3

- ** `isns-utils` **
  - **RPM:**  isns-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.93-7.amzn2.0.3
  - **AL2023.12 version:** 0.101-6.amzn2023.0.1

- ** `iso-codes` **
  - **RPM:**  iso-codes  / **Architectures:** noarch
  - **RPM:**  iso-codes-devel  / **Architectures:** noarch
  - **AL2 version:** 4.6.0-3.amzn2
  - **AL2023.12 version:** 4.6.0-1.amzn2023.0.3

- ** `itstool` **
  - **RPM:**  itstool
  - **Architectures:** noarch
  - **AL2 version:** 2.0.2-1.amzn2
  - **AL2023.12 version:** 2.0.6-5.amzn2023.0.3

- ** `jakarta-oro` **
  - **RPM:**  jakarta-oro  / **Architectures:** noarch
  - **RPM:**  jakarta-oro-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0.8-16.1.amzn2
  - **AL2023.12 version:** 2.0.8-36.amzn2023.0.1

- ** `jansi-native` **
  - **RPM:**  jansi-native
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4-11.amzn2.0.2
  - **AL2023.12 version:** 1.8-9.amzn2023.0.2

- ** `jansson` **
  - **RPM:**  jansson  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jansson-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jansson-devel-doc  / **Architectures:** noarch
  - **AL2 version:** 2.10-1.amzn2.0.2
  - **AL2023.12 version:** 2.14-0.amzn2023

- ** `jasper` **
  - **RPM:**  jasper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.900.1-33.amzn2.0.1
  - **AL2023.12 version:** 2.0.33-1.amzn2023.0.2

- ** `java_cup` **
  - **RPM:**  java\_cup  / **Architectures:** noarch
  - **RPM:**  java\_cup-javadoc  / **Architectures:** noarch
  - **RPM:**  java\_cup-manual  / **Architectures:** noarch
  - **AL2 version:** 0.11a-16.1.amzn2
  - **AL2023.12 version:** 0.11b-21.amzn2023.0.3

- ** [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-11-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.0.32\+9-1.amzn2
  - **AL2023.12 version:** 11.0.32\+9-1.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-17-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 17.0.20\+8-1.amzn2.1
  - **AL2023.12 version:** 17.0.20\+8-1.amzn2023.1

- ** `javacc` **
  - **RPM:**  javacc  / **Architectures:** noarch
  - **RPM:**  javacc-demo  / **Architectures:** noarch
  - **RPM:**  javacc-javadoc  / **Architectures:** noarch
  - **RPM:**  javacc-manual  / **Architectures:** noarch
  - **AL2 version:** 5.0-10.1.amzn2
  - **AL2023.12 version:** 7.0.4-11.amzn2023.0.1

- ** `javacc-maven-plugin` **
  - **RPM:**  javacc-maven-plugin  / **Architectures:** noarch
  - **RPM:**  javacc-maven-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.6-17.amzn2
  - **AL2023.12 version:** 2.6-35.amzn2023.0.1

- ** `javapackages-tools` **
  - **RPM:**  javapackages-tools  / **Architectures:** noarch
  - **RPM:**  maven-local  / **Architectures:** noarch
  - **AL2 version:** 3.4.1-11.amzn2
  - **AL2023.12 version:** 6.0.0-7.amzn2023.0.6

- ** `javassist` **
  - **RPM:**  javassist  / **Architectures:** noarch
  - **RPM:**  javassist-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.16.1-10.amzn2
  - **AL2023.12 version:** 3.28.0-4.amzn2023.0.1

- ** `jaxen` **
  - **RPM:**  jaxen  / **Architectures:** noarch
  - **RPM:**  jaxen-demo  / **Architectures:** noarch
  - **RPM:**  jaxen-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1.3-11.1.amzn2
  - **AL2023.12 version:** 1.2.0-10.amzn2023.0.1

- ** `jbigkit` **
  - **RPM:**  jbigkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbigkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbigkit-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0-11.amzn2.0.3
  - **AL2023.12 version:** 2.1-21.amzn2023.0.2

- ** `jboss-parent` **
  - **RPM:**  jboss-parent
  - **Architectures:** noarch
  - **AL2 version:** 6-12.amzn2
  - **AL2023.12 version:** 20-14.amzn2023.0.1

- ** `jboss-servlet-3.0-api` **
  - **RPM:**  jboss-servlet-3.0-api  / **Architectures:** noarch
  - **RPM:**  jboss-servlet-3.0-api-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0.1-9.amzn2
  - **AL2023.12 version:** 1.0.2-16.amzn2023.0.1

- ** `jdepend` **
  - **RPM:**  jdepend  / **Architectures:** noarch
  - **RPM:**  jdepend-demo  / **Architectures:** noarch
  - **RPM:**  jdepend-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.9.1-10.amzn2
  - **AL2023.12 version:** 2.9.1-29.amzn2023.0.2

- ** `jdependency` **
  - **RPM:**  jdependency  / **Architectures:** noarch
  - **RPM:**  jdependency-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0.7-10.amzn2
  - **AL2023.12 version:** 2.8.0-1.amzn2023.0.2

- ** `jdom` **
  - **RPM:**  jdom  / **Architectures:** noarch
  - **RPM:**  jdom-demo  / **Architectures:** noarch
  - **RPM:**  jdom-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1.3-6.1.amzn2.0.1
  - **AL2023.12 version:** 1.1.3-30.amzn2023.0.3

- ** `jflex` **
  - **RPM:**  jflex  / **Architectures:** noarch
  - **RPM:**  jflex-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4.3-20.amzn2
  - **AL2023.12 version:** 1.7.0-10.amzn2023.0.3

- ** `jna` **
  - **RPM:**  jna  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jna-contrib  / **Architectures:** noarch
  - **RPM:**  jna-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.5.2-8.amzn2.0.2
  - **AL2023.12 version:** 5.9.0-1.amzn2023.0.3

- ** `jomolhari-fonts` **
  - **RPM:**  jomolhari-fonts
  - **Architectures:** noarch
  - **AL2 version:** 0.003-17.amzn2
  - **AL2023.12 version:** 0.003-32.amzn2023.0.1

- ** `jq` **
  - **RPM:**  jq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6-17.amzn2.0.2
  - **AL2023.12 version:** 1.8.1-60.amzn2023

- ** `jsch` **
  - **RPM:**  jsch  / **Architectures:** noarch
  - **RPM:**  jsch-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0.1.50-5.amzn2
  - **AL2023.12 version:** 0.1.55-7.amzn2023.0.1

- ** `json-c` **
  - **RPM:**  json-c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-c-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-c-doc  / **Architectures:** noarch
  - **AL2 version:** 0.11-4.amzn2.0.4
  - **AL2023.12 version:** 0.14-8.amzn2023.0.2

- ** `jsoncpp` **
  - **RPM:**  jsoncpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jsoncpp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jsoncpp-doc  / **Architectures:** noarch
  - **AL2 version:** 1.7.2-3.amzn2.0.2
  - **AL2023.12 version:** 1.9.4-3.amzn2023.0.2

- ** `json-glib` **
  - **RPM:**  json-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  json-glib-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.2-2.amzn2
  - **AL2023.12 version:** 1.10.0-1.amzn2023.0.2

- ** `jsoup` **
  - **RPM:**  jsoup  / **Architectures:** noarch
  - **RPM:**  jsoup-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.16.1-4.amzn2.0.1
  - **AL2023.12 version:** 1.16.1-4.amzn2023.0.2

- ** `jsr-305` **
  - **RPM:**  jsr-305  / **Architectures:** noarch
  - **RPM:**  jsr-305-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0-0.18.20090319svn.amzn2
  - **AL2023.12 version:** 3.0.2-5.amzn2023.0.4

- ** `jtidy` **
  - **RPM:**  jtidy  / **Architectures:** noarch
  - **RPM:**  jtidy-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-0.16.20100930svn1125.amzn2.0.1
  - **AL2023.12 version:** 1.0-0.38.20100930svn1125.amzn2023.0.2

- ** `junit` **
  - **RPM:**  junit  / **Architectures:** noarch
  - **RPM:**  junit-javadoc  / **Architectures:** noarch
  - **RPM:**  junit-manual  / **Architectures:** noarch
  - **AL2 version:** 4.11-8.1.amzn2.0.1
  - **AL2023.12 version:** 4.13.1-7.amzn2023.0.3

- ** `jzlib` **
  - **RPM:**  jzlib  / **Architectures:** noarch
  - **RPM:**  jzlib-demo  / **Architectures:** noarch
  - **RPM:**  jzlib-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1.1-6.amzn2
  - **AL2023.12 version:** 1.1.3-21.amzn2023.0.1

- ** `kbd` **
  - **RPM:**  kbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kbd-legacy  / **Architectures:** noarch
  - **RPM:**  kbd-misc  / **Architectures:** noarch
  - **AL2 version:** 1.15.5-15.amzn2
  - **AL2023.12 version:** 2.4.0-2.amzn2023.0.3

- ** `kde-filesystem` **
  - **RPM:**  kde-filesystem
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4-47.amzn2.0.2
  - **AL2023.12 version:** 4-65.amzn2023.0.3

- ** `keepalived` **
  - **RPM:**  keepalived
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.5-16.amzn2.0.4
  - **AL2023.12 version:** 2.2.7-6.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.14.355-284.741.amzn2
  - **AL2023.12 version:** 6.1.180-225.360.amzn2023

- ** `kexec-tools` **
  - **RPM:**  kexec-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.23-1.amzn2.0.2
  - **AL2023.12 version:** 2.0.29-1.amzn2023.0.1

- ** `keyutils` **
  - **RPM:**  keyutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  keyutils-libs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.8-3.amzn2.0.2
  - **AL2023.12 version:** 1.6.3-1.amzn2023.0.2

- ** `kmod` **
  - **RPM:**  kmod  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kmod-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kmod-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 25-3.amzn2.0.2
  - **AL2023.12 version:** 29-2.amzn2023.0.5

- ** `krb5` **
  - **RPM:**  krb5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-pkinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-server-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  krb5-workstation  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libkadm5  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.15.1-55.amzn2.2.10
  - **AL2023.12 version:** 1.21.3-8.amzn2023.0.1

- ** `ksh` **
  - **RPM:**  ksh
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20120801-247.amzn2.0.2
  - **AL2023.12 version:** 20120801-255.amzn2023.0.2

- ** `ladspa` **
  - **RPM:**  ladspa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ladspa-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.13-12.amzn2.0.2
  - **AL2023.12 version:** 1.17-1.amzn2023

- ** `langtable` **
  - **RPM:**  langtable
  - **Architectures:** noarch
  - **AL2 version:** 0.0.31-4.amzn2
  - **AL2023.12 version:** 0.0.68-2.amzn2023

- ** `lapack` **
  - **RPM:**  blas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  blas64  / **Architectures:** aarch64, x86\_64
  - **RPM:**  blas-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  blas-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lapack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lapack64  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lapack-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lapack-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.4.2-8.amzn2.0.2
  - **AL2023.12 version:** 3.10.0-4.amzn2023.0.3

- ** `lasso` **
  - **RPM:**  lasso  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lasso-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-lasso  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.0-1.amzn2.0.1
  - **AL2023.12 version:** 2.9.0-1.amzn2023.0.1

- ** `latex2html` **
  - **RPM:**  latex2html
  - **Architectures:** noarch
  - **AL2 version:** 2012-3.amzn2
  - **AL2023.12 version:** 2020.2-3.amzn2023.0.3

- ** `lcms2` **
  - **RPM:**  lcms2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lcms2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lcms2-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.6-3.amzn2.0.4
  - **AL2023.12 version:** 2.19-75.amzn2023.0.1

- ** `ldns` **
  - **RPM:**  ldns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ldns-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ldns-doc  / **Architectures:** noarch
  - **AL2 version:** 1.6.16-10.amzn2.0.3
  - **AL2023.12 version:** 1.8.3-2.amzn2023.0.3

- ** `less` **
  - **RPM:**  less
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 458-9.amzn2.0.4
  - **AL2023.12 version:** 608-2.amzn2023.0.2

- ** `lftp` **
  - **RPM:**  lftp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lftp-scripts  / **Architectures:** noarch
  - **AL2 version:** 4.4.8-12.amzn2.1
  - **AL2023.12 version:** 4.9.2-2.amzn2023

- ** `libabigail` **
  - **RPM:**  libabigail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libabigail-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libabigail-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3-1.amzn2.0.1
  - **AL2023.12 version:** 2.3-1.amzn2023.0.2

- ** `libaio` **
  - **RPM:**  libaio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libaio-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.109-13.amzn2.0.2
  - **AL2023.12 version:** 0.3.111-11.amzn2023.0.2

- ** `libao` **
  - **RPM:**  libao  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libao-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.0-8.amzn2.0.2
  - **AL2023.12 version:** 1.2.0-20.amzn2023.0.2

- ** `libappstream-glib` **
  - **RPM:**  libappstream-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libappstream-glib-builder  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libappstream-glib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.8-2.amzn2
  - **AL2023.12 version:** 0.8.3-139.amzn2023

- ** `libarchive` **
  - **RPM:**  bsdcpio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bsdtar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libarchive-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.2-14.amzn2.0.6
  - **AL2023.12 version:** 3.7.4-2.amzn2023.0.4

- ** `libassuan` **
  - **RPM:**  libassuan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libassuan-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.0-3.amzn2.0.2
  - **AL2023.12 version:** 2.5.5-1.amzn2023.0.2

- ** `libasyncns` **
  - **RPM:**  libasyncns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasyncns-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8-7.amzn2.0.2
  - **AL2023.12 version:** 0.8-20.amzn2023.0.2

- ** `libatasmart` **
  - **RPM:**  libatasmart  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatasmart-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.19-6.amzn2.0.2
  - **AL2023.12 version:** 0.19-20.amzn2023.0.2

- ** `libatomic_ops` **
  - **RPM:**  libatomic\_ops  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic\_ops-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic\_ops-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.6.2-3.amzn2.0.1
  - **AL2023.12 version:** 7.6.10-7.amzn2023.0.2

- ** `libblockdev` **
  - **RPM:**  libblockdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-crypto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-crypto-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-dm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-dm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-fs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-fs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-kbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-kbd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-loop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-loop-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-lvm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mdraid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mdraid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mpath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-mpath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-nvdimm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-nvdimm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-part  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-part-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-plugins-all  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-swap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-swap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libblockdev-utils-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.18-4.amzn2.0.2
  - **AL2023.12 version:** 3.2.1-1.amzn2023.0.3

- ** `libbpf` **
  - **RPM:**  libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbpf-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.5.0-2.amzn2.0.4
  - **AL2023.12 version:** 1.6.1-3.amzn2023

- ** `libburn` **
  - **RPM:**  cdrskin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libburn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libburn-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.8-4.amzn2.0.2
  - **AL2023.12 version:** 1.5.4-2.amzn2023.0.2

- ** `libbytesize` **
  - **RPM:**  libbytesize  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbytesize-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2-1.amzn2
  - **AL2023.12 version:** 2.6-1.amzn2023.0.2

- ** `libcanberra` **
  - **RPM:**  libcanberra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcanberra-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcanberra-gtk3  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.30-5.amzn2.0.3
  - **AL2023.12 version:** 0.30-35.amzn2023

- ** `libcap` **
  - **RPM:**  libcap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.54-1.amzn2.0.3
  - **AL2023.12 version:** 2.73-1.amzn2023.0.7

- ** `libcap-ng` **
  - **RPM:**  libcap-ng  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-ng-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-ng-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.5-4.amzn2.0.4
  - **AL2023.12 version:** 0.8.2-4.amzn2023.0.2

- ** `libcgroup` **
  - **RPM:**  libcgroup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcgroup-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcgroup-pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcgroup-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.41-21.amzn2
  - **AL2023.12 version:** 3.0-1.amzn2023.0.1

- ** `libcomps` **
  - **RPM:**  libcomps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcomps-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcomps-doc  / **Architectures:** noarch
  - **RPM:**  python-libcomps-doc  / **Architectures:** noarch
  - **AL2 version:** 0.1.8-3.amzn2.0.2
  - **AL2023.12 version:** 0.1.20-1.amzn2023

- ** `libconfig` **
  - **RPM:**  libconfig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libconfig-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.9-5.amzn2.0.2
  - **AL2023.12 version:** 1.7.2-7.amzn2023.0.2

- ** `libdaemon` **
  - **RPM:**  libdaemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdaemon-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.14-7.amzn2.0.2
  - **AL2023.12 version:** 0.14-21.amzn2023.0.2

- ** [`libdb`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-bdb) **
  - **RPM:**  [`libdb`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-bdb)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-cxx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-cxx-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-devel-doc  / **Architectures:** noarch
  - **RPM:**  libdb-devel-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-sql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-sql-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-tcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-tcl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdb-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.3.21-24.amzn2.0.5
  - **AL2023.12 version:** 5.3.28-49.amzn2023.0.2

- ** `libdbi` **
  - **RPM:**  libdbi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.4-6.amzn2.0.2
  - **AL2023.12 version:** 0.9.0-20.amzn2023.0.1

- ** `libdbusmenu` **
  - **RPM:**  libdbusmenu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-doc  / **Architectures:** noarch
  - **RPM:**  libdbusmenu-gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-gtk3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-jsonloader  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-jsonloader-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdbusmenu-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 16.04.0-4.amzn2.0.2
  - **AL2023.12 version:** 16.04.0-27.amzn2023.0.1

- ** `libdmx` **
  - **RPM:**  libdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdmx-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.3-3.amzn2.0.2
  - **AL2023.12 version:** 1.1.5-3.amzn2023.0.3

- ** `libdrm` **
  - **RPM:**  drm-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdrm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdrm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.97-2.amzn2
  - **AL2023.12 version:** 2.4.123-1.amzn2023.0.1

- ** `libdwarf` **
  - **RPM:**  libdwarf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarf-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20130207-4.amzn2.0.3
  - **AL2023.12 version:** 0.5.0-1.amzn2023.0.3

- ** `libecap` **
  - **RPM:**  libecap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libecap-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.0-1.amzn2.0.2
  - **AL2023.12 version:** 1.0.1-10.amzn2023

- ** `libedit` **
  - **RPM:**  libedit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libedit-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0-12.20121213cvs.amzn2.0.2
  - **AL2023.12 version:** 3.1-38.20210714cvs.amzn2023.0.2

- ** `libepoxy` **
  - **RPM:**  libepoxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libepoxy-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.8-1.amzn2.0.1
  - **AL2023.12 version:** 1.5.9-1.amzn2023.0.2

- ** `liberation-fonts` **
  - **RPM:**  liberation-fonts  / **Architectures:** noarch
  - **RPM:**  liberation-fonts-common  / **Architectures:** noarch
  - **RPM:**  liberation-mono-fonts  / **Architectures:** noarch
  - **RPM:**  liberation-sans-fonts  / **Architectures:** noarch
  - **RPM:**  liberation-serif-fonts  / **Architectures:** noarch
  - **AL2 version:** 1.07.2-16.amzn2
  - **AL2023.12 version:** 2.1.5-1.amzn2023.0.2

- ** `libesmtp` **
  - **RPM:**  libesmtp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libesmtp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.6-7.amzn2.0.2
  - **AL2023.12 version:** 1.0.6-25.amzn2023.0.2

- ** `libestr` **
  - **RPM:**  libestr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libestr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.9-2.amzn2.0.2
  - **AL2023.12 version:** 0.1.11-1.amzn2023.0.2

- ** `libev` **
  - **RPM:**  libev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libev-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libev-libevent-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libev-source  / **Architectures:** noarch
  - **AL2 version:** 4.24-4.amzn2.0.2
  - **AL2023.12 version:** 4.33-3.amzn2023.0.2

- ** `libevdev` **
  - **RPM:**  libevdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevdev-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevdev-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.6-1.amzn2.0.2
  - **AL2023.12 version:** 1.13.3-1.amzn2023.0.1

- ** `libevent` **
  - **RPM:**  libevent  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevent-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libevent-doc  / **Architectures:** noarch
  - **AL2 version:** 2.0.21-4.amzn2.0.3
  - **AL2023.12 version:** 2.1.12-3.amzn2023.0.3

- ** `libexif` **
  - **RPM:**  libexif  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libexif-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libexif-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.6.22-2.amzn2
  - **AL2023.12 version:** 0.6.22-4.amzn2023.0.2

- ** `libfabric` **
  - **RPM:**  libfabric  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfabric-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.0-3.amzn2.0.2
  - **AL2023.12 version:** 1.14.0-2.amzn2023.0.2

- ** `libfastjson` **
  - **RPM:**  libfastjson  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfastjson-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.99.4-3.amzn2.0.1
  - **AL2023.12 version:** 0.99.9-1.amzn2023.0.3

- ** `libffi` **
  - **RPM:**  libffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libffi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.13-18.amzn2.0.2
  - **AL2023.12 version:** 3.4.4-1.amzn2023.0.1

- ** `libfontenc` **
  - **RPM:**  libfontenc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libfontenc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.3-3.amzn2.0.2
  - **AL2023.12 version:** 1.1.7-3.amzn2023.0.1

- ** `libgcrypt` **
  - **RPM:**  libgcrypt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcrypt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.3-14.amzn2.0.3
  - **AL2023.12 version:** 1.10.2-1.amzn2023.0.3

- ** `libgee` **
  - **RPM:**  libgee  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgee-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.18.1-1.amzn2.0.2
  - **AL2023.12 version:** 0.20.6-7.amzn2023.0.1

- ** `libgexiv2` **
  - **RPM:**  libgexiv2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgexiv2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.10.4-4.amzn2.0.1
  - **AL2023.12 version:** 0.14.3-2.amzn2023

- ** `libglvnd` **
  - **RPM:**  libglvnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-gles  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-glx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libglvnd-opengl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.1-1.amzn2.0.2
  - **AL2023.12 version:** 1.7.0-4.amzn2023.0.2

- ** `libgpg-error` **
  - **RPM:**  libgpg-error  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgpg-error-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.31-1.amzn2.0.1
  - **AL2023.12 version:** 1.42-1.amzn2023.0.2

- ** `libgtop2` **
  - **RPM:**  libgtop2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgtop2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.38.0-3.amzn2
  - **AL2023.12 version:** 2.41.3-2.amzn2023.0.1

- ** `libgusb` **
  - **RPM:**  libgusb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgusb-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.9-1.amzn2.0.2
  - **AL2023.12 version:** 0.3.8-1.amzn2023.0.2

- ** `libgweather` **
  - **RPM:**  libgweather  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgweather-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.2-2.amzn2
  - **AL2023.12 version:** 4.4.4-1.amzn2023.0.1

- ** `libhangul` **
  - **RPM:**  libhangul  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libhangul-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.0-8.amzn2.0.2
  - **AL2023.12 version:** 0.1.0-23.amzn2023.0.3

- ** `libical` **
  - **RPM:**  libical  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libical-glib-doc  / **Architectures:** noarch
  - **AL2 version:** 3.0.3-2.amzn2.0.1
  - **AL2023.12 version:** 3.0.18-2.amzn2023.0.1

- ** `libICE` **
  - **RPM:**  libICE  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libICE-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.9-9.amzn2.0.2
  - **AL2023.12 version:** 1.1.1-3.amzn2023.0.1

- ** `libicns` **
  - **RPM:**  libicns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libicns-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libicns-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.1-10.amzn2.0.2
  - **AL2023.12 version:** 0.8.1-21.amzn2023.0.2

- ** `libid3tag` **
  - **RPM:**  libid3tag  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libid3tag-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.15.1b-17.amzn2.0.2
  - **AL2023.12 version:** 0.16.3-1.amzn2023

- ** `libidn` **
  - **RPM:**  libidn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.28-4.amzn2.0.5
  - **AL2023.12 version:** 1.38-4.amzn2023.0.6

- ** `libidn2` **
  - **RPM:**  idn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libidn2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.0-1.amzn2.0.3
  - **AL2023.12 version:** 2.3.2-1.amzn2023.0.5

- ** `libinput` **
  - **RPM:**  libinput  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libinput-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.4-2.amzn2.0.1
  - **AL2023.12 version:** 1.26.2-1.amzn2023.0.2

- ** `libiscsi` **
  - **RPM:**  libiscsi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libiscsi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libiscsi-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.0-7.amzn2.0.1
  - **AL2023.12 version:** 1.19.0-7.amzn2023

- ** `libisofs` **
  - **RPM:**  libisofs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libisofs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.8-4.amzn2.0.2
  - **AL2023.12 version:** 1.5.4-1.amzn2023.0.2

- ** `libjpeg-turbo` **
  - **RPM:**  libjpeg-turbo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libjpeg-turbo-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  turbojpeg-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.90-2.amzn2.0.6
  - **AL2023.12 version:** 2.1.4-2.amzn2023.0.5

- ** `libksba` **
  - **RPM:**  libksba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libksba-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.0-6.amzn2.0.1
  - **AL2023.12 version:** 1.6.3-1.amzn2023.0.2

- ** `libldb` **
  - **RPM:**  ldb-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libldb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libldb-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.4-2.amzn2
  - **AL2023.12 version:** 2.6.2-1.amzn2023.0.2

- ** `liblockfile` **
  - **RPM:**  liblockfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblockfile-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.08-17.amzn2.0.2
  - **AL2023.12 version:** 1.14-7.amzn2023.0.2

- ** `liblognorm` **
  - **RPM:**  liblognorm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblognorm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblognorm-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblognorm-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.2-1.amzn2.0.2
  - **AL2023.12 version:** 2.0.6-1.amzn2023.0.3

- ** `libmbim` **
  - **RPM:**  libmbim  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmbim-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmbim-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.14.2-1.amzn2
  - **AL2023.12 version:** 1.26.0-1.amzn2023.0.2

- ** `libmetalink` **
  - **RPM:**  libmetalink  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmetalink-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.3-13.amzn2
  - **AL2023.12 version:** 0.1.3-14.amzn2023.0.2

- ** `libmicrohttpd` **
  - **RPM:**  libmicrohttpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmicrohttpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmicrohttpd-doc  / **Architectures:** noarch
  - **AL2 version:** 0.9.33-2.amzn2.0.3
  - **AL2023.12 version:** 0.9.73-1.amzn2023.0.4

- ** `libmnl` **
  - **RPM:**  libmnl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmnl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmnl-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.3-7.amzn2.0.2
  - **AL2023.12 version:** 1.0.4-13.amzn2023.0.2

- ** `libmpc` **
  - **RPM:**  libmpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmpc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.1-3.amzn2.0.2
  - **AL2023.12 version:** 1.2.1-2.amzn2023.0.2

- ** `libmspack` **
  - **RPM:**  libmspack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmspack-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.5-0.8.alpha.amzn2
  - **AL2023.12 version:** 0.10.1-0.8.alpha.amzn2023

- ** `libnet` **
  - **RPM:**  libnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnet-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.6-7.amzn2.0.2
  - **AL2023.12 version:** 1.2-2.amzn2023.0.2

- ** `libnetfilter_conntrack` **
  - **RPM:**  libnetfilter\_conntrack  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetfilter\_conntrack-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.6-1.amzn2.0.2
  - **AL2023.12 version:** 1.0.8-2.amzn2023.0.2

- ** `libnetfilter_cthelper` **
  - **RPM:**  libnetfilter\_cthelper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetfilter\_cthelper-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.0-10.amzn2.1
  - **AL2023.12 version:** 1.0.0-21.amzn2023.0.2

- ** `libnetfilter_cttimeout` **
  - **RPM:**  libnetfilter\_cttimeout  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetfilter\_cttimeout-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.0-6.amzn2.1
  - **AL2023.12 version:** 1.0.0-19.amzn2023.0.2

- ** `libnetfilter_queue` **
  - **RPM:**  libnetfilter\_queue  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnetfilter\_queue-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-2.amzn2.0.2
  - **AL2023.12 version:** 1.0.5-2.amzn2023.0.2

- ** `libnfnetlink` **
  - **RPM:**  libnfnetlink  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnfnetlink-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.1-4.amzn2.0.2
  - **AL2023.12 version:** 1.0.1-19.amzn2023.0.2

- ** `libnfs` **
  - **RPM:**  libnfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnfs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnfs-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.11.0-1.amzn2.0.2
  - **AL2023.12 version:** 4.0.0-4.amzn2023.0.3

- ** `libnftnl` **
  - **RPM:**  libnftnl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnftnl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.5-4.amzn2
  - **AL2023.12 version:** 1.2.2-2.amzn2023.0.2

- ** `libnl3` **
  - **RPM:**  libnl3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnl3-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnl3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnl3-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2.28-4.amzn2.0.1
  - **AL2023.12 version:** 3.5.0-6.amzn2023.0.2

- ** `libnotify` **
  - **RPM:**  libnotify  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnotify-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.7-1.amzn2.0.2
  - **AL2023.12 version:** 0.8.3-4.amzn2023.0.1

- ** `libntlm` **
  - **RPM:**  libntlm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libntlm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3-6.amzn2.0.2
  - **AL2023.12 version:** 1.6-2.amzn2023.0.2

- ** `libogg` **
  - **RPM:**  libogg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libogg-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libogg-devel-docs  / **Architectures:** noarch
  - **AL2 version:** 1.3.0-7.amzn2.0.2
  - **AL2023.12 version:** 1.3.4-4.amzn2023.0.2

- ** `libosinfo` **
  - **RPM:**  libosinfo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libosinfo-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.0-5.amzn2
  - **AL2023.12 version:** 1.12.0-1.amzn2023.0.1

- ** `libotf` **
  - **RPM:**  libotf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libotf-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.13-4.amzn2.0.2
  - **AL2023.12 version:** 0.9.13-18.amzn2023.0.2

- ** `libpaper` **
  - **RPM:**  libpaper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpaper-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.24-8.amzn2.0.2
  - **AL2023.12 version:** 1.1.28-2.amzn2023.0.2

- ** `libpcap` **
  - **RPM:**  libpcap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpcap-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.3-11.amzn2
  - **AL2023.12 version:** 1.10.1-1.amzn2023.0.2

- ** `libpciaccess` **
  - **RPM:**  libpciaccess  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpciaccess-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.14-1.amzn2
  - **AL2023.12 version:** 0.16-4.amzn2023.0.3

- ** `libpeas` **
  - **RPM:**  libpeas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpeas-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpeas-gtk  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.20.0-1.amzn2.0.3
  - **AL2023.12 version:** 1.32.0-1.amzn2023.0.3

- ** `libpfm` **
  - **RPM:**  libpfm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpfm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpfm-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.7.0-10.amzn2
  - **AL2023.12 version:** 4.11.0-4.amzn2023.0.2

- ** `libpinyin` **
  - **RPM:**  libpinyin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-data  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.93-4.amzn2.0.2
  - **AL2023.12 version:** 2.9.91-1.amzn2023.0.1

- ** `libpipeline` **
  - **RPM:**  libpipeline  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpipeline-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.3-3.amzn2.0.2
  - **AL2023.12 version:** 1.5.3-2.amzn2023.0.2

- ** `libplist` **
  - **RPM:**  libplist  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libplist-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.12-3.amzn2.0.5
  - **AL2023.12 version:** 2.2.0-3.amzn2023.0.3

- ** `libpng` **
  - **RPM:**  libpng  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpng-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.13-8.amzn2.0.9
  - **AL2023.12 version:** 1.6.37-10.amzn2023.0.13

- ** `libproxy` **
  - **RPM:**  libproxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libproxy-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libproxy-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.11-10.amzn2.0.3
  - **AL2023.12 version:** 0.5.7-3.amzn2023.0.1

- ** `libpsl` **
  - **RPM:**  libpsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpsl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  psl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  psl-make-dafsa  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.21.5-1.amzn2
  - **AL2023.12 version:** 0.21.5-1.amzn2023.0.1

- ** `libpsm2` **
  - **RPM:**  libpsm2  / **Architectures:** x86\_64
  - **RPM:**  libpsm2-compat  / **Architectures:** x86\_64
  - **RPM:**  libpsm2-devel  / **Architectures:** x86\_64
  - **AL2 version:** 10.3.8-3.amzn2.0.2
  - **AL2023.12 version:** 11.2.86-8.amzn2023.0.2

- ** `libpwquality` **
  - **RPM:**  libpwquality  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpwquality-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.3-5.amzn2
  - **AL2023.12 version:** 1.4.4-6.amzn2023.0.2

- ** `libqb` **
  - **RPM:**  libqb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libqb-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.5-1.amzn2
  - **AL2023.12 version:** 2.0.6-1.amzn2023.0.1

- ** `librepo` **
  - **RPM:**  librepo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librepo-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.1-8.amzn2.0.2
  - **AL2023.12 version:** 1.14.5-2.amzn2023.0.2

- ** `libreswan` **
  - **RPM:**  libreswan
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.25-4.8.amzn2.0.3
  - **AL2023.12 version:** 4.12-3.amzn2023.0.3

- ** `librevenge` **
  - **RPM:**  librevenge  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librevenge-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librevenge-doc  / **Architectures:** noarch
  - **AL2 version:** 0.0.2-2.amzn2.0.2
  - **AL2023.12 version:** 0.0.4-20.amzn2023.0.2

- ** `librsvg2` **
  - **RPM:**  librsvg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librsvg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.40.20-1.amzn2
  - **AL2023.12 version:** 2.59.2-319.amzn2023

- ** `libsamplerate` **
  - **RPM:**  libsamplerate  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsamplerate-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.8-6.amzn2.0.2
  - **AL2023.12 version:** 0.2.2-1.amzn2023

- ** `libseccomp` **
  - **RPM:**  libseccomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libseccomp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libseccomp-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.2-1.amzn2.0.1
  - **AL2023.12 version:** 2.5.3-1.amzn2023.0.2

- ** `libsecret` **
  - **RPM:**  libsecret  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsecret-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.18.5-2.amzn2.0.2
  - **AL2023.12 version:** 0.21.4-3.amzn2023.0.1

- ** `libselinux` **
  - **RPM:**  libselinux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libselinux-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libselinux-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libselinux-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5-12.amzn2.0.2
  - **AL2023.12 version:** 3.4-5.amzn2023.0.2

- ** `libsemanage` **
  - **RPM:**  libsemanage  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsemanage-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsemanage-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5-11.amzn2
  - **AL2023.12 version:** 3.4-5.amzn2023.0.2

- ** `libsepol` **
  - **RPM:**  libsepol  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsepol-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsepol-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5-10.amzn2.0.1
  - **AL2023.12 version:** 3.4-3.amzn2023.0.3

- ** `libsigc++20` **
  - **RPM:**  libsigc\+\+20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsigc\+\+20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsigc\+\+20-doc  / **Architectures:** noarch
  - **AL2 version:** 2.10.0-1.amzn2.0.2
  - **AL2023.12 version:** 2.10.7-1.amzn2023.0.3

- ** `libSM` **
  - **RPM:**  libSM  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libSM-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.2-2.amzn2.0.2
  - **AL2023.12 version:** 1.2.4-3.amzn2023.0.1

- ** `libsmi` **
  - **RPM:**  libsmi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.8-13.amzn2.0.2
  - **AL2023.12 version:** 0.4.8-28.amzn2023.0.2

- ** `libsndfile` **
  - **RPM:**  libsndfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.25-12.amzn2.2.1
  - **AL2023.12 version:** 1.2.2-3.amzn2023.0.3

- ** `libsodium` **
  - **RPM:**  libsodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsodium-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.18-3.amzn2.0.1
  - **AL2023.12 version:** 1.0.19-5.amzn2023

- ** `libsolv` **
  - **RPM:**  libsolv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsolv-demo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsolv-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsolv-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.6.34-4.amzn2.0.1
  - **AL2023.12 version:** 0.7.22-1.amzn2023.0.4

- ** `libsoup` **
  - **RPM:**  libsoup  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsoup-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.56.0-6.amzn2.0.7
  - **AL2023.12 version:** 2.72.0-6.amzn2023.0.12

- ** `libspiro` **
  - **RPM:**  libspiro  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libspiro-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20071029-12.amzn2.0.2
  - **AL2023.12 version:** 20200505-3.amzn2023.0.2

- ** `libsrtp` **
  - **RPM:**  libsrtp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsrtp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.4-11.20101004cvs.amzn2
  - **AL2023.12 version:** 2.6.0-1.amzn2023.0.1

- ** `libssh2` **
  - **RPM:**  libssh2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libssh2-docs  / **Architectures:** noarch
  - **AL2 version:** 1.4.3-12.amzn2.2.9
  - **AL2023.12 version:** 1.10.0-1.amzn2023.0.6

- ** `libstoragemgmt` **
  - **RPM:**  libstoragemgmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstoragemgmt-arcconf-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstoragemgmt-hpsa-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-local-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-megaraid-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-smis-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-targetd-plugin  / **Architectures:** noarch
  - **RPM:**  libstoragemgmt-udev  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.1-2.amzn2
  - **AL2023.12 version:** 1.9.4-5.amzn2023.0.2

- ** `libtalloc` **
  - **RPM:**  libtalloc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtalloc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.16-1.amzn2
  - **AL2023.12 version:** 2.3.4-1.amzn2023.0.2

- ** `libtasn1` **
  - **RPM:**  libtasn1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtasn1-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.10-1.amzn2.0.8
  - **AL2023.12 version:** 4.19.0-1.amzn2023.0.6

- ** `libtdb` **
  - **RPM:**  libtdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtdb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tdb-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.18-1.amzn2
  - **AL2023.12 version:** 1.4.7-1.amzn2023.0.2

- ** `libtevent` **
  - **RPM:**  libtevent  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtevent-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.39-1.amzn2
  - **AL2023.12 version:** 0.13.0-1.amzn2023.0.2

- ** `libthai` **
  - **RPM:**  libthai  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libthai-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.14-9.amzn2.0.2
  - **AL2023.12 version:** 0.1.28-6.amzn2023.0.2

- ** `libtheora` **
  - **RPM:**  libtheora  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtheora-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtheora-devel-docs  / **Architectures:** noarch
  - **RPM:**  theora-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.1-8.amzn2.0.2
  - **AL2023.12 version:** 1.1.1-29.amzn2023.0.3

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0.3-35.amzn2.0.31
  - **AL2023.12 version:** 4.4.0-4.amzn2023.0.27

- ** `libtirpc` **
  - **RPM:**  libtirpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtirpc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.4-0.16.amzn2
  - **AL2023.12 version:** 1.3.3-0.amzn2023

- ** `libtool` **
  - **RPM:**  libtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtool-ltdl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtool-ltdl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.2-22.2.amzn2.0.2
  - **AL2023.12 version:** 2.4.7-1.amzn2023.0.3

- ** `libuninameslist` **
  - **RPM:**  libuninameslist  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuninameslist-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 20091231-8.amzn2.0.2
  - **AL2023.12 version:** 20200413-3.amzn2023.0.2

- ** `libunistring` **
  - **RPM:**  libunistring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libunistring-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.3-9.amzn2.0.2
  - **AL2023.12 version:** 0.9.10-10.amzn2023.0.2

- ** `libunwind` **
  - **RPM:**  libunwind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libunwind-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2-2.amzn2.0.3
  - **AL2023.12 version:** 1.4.0-5.amzn2023.0.3

- ** `libusb` **
  - **RPM:**  libusb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libusb-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.4-3.amzn2.0.2
  - **AL2023.12 version:** 0.1.7-6.amzn2023.0.2

- ** `libusbx` **
  - **RPM:**  libusbx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libusbx-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libusbx-devel-doc  / **Architectures:** noarch
  - **AL2 version:** 1.0.21-1.amzn2.0.1
  - **AL2023.12 version:** 1.0.24-2.amzn2023.0.3

- ** `libuser` **
  - **RPM:**  libuser  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuser-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.60-9.amzn2
  - **AL2023.12 version:** 0.63-4.amzn2023.0.2

- ** `libutempter` **
  - **RPM:**  libutempter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libutempter-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.6-4.amzn2.0.2
  - **AL2023.12 version:** 1.2.1-4.amzn2023.0.2

- ** `libuv` **
  - **RPM:**  libuv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.39.0-1.amzn2.0.2
  - **AL2023.12 version:** 1.51.0-1.amzn2023.0.1

- ** `libvdpau` **
  - **RPM:**  libvdpau  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvdpau-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvdpau-docs  / **Architectures:** noarch
  - **AL2 version:** 1.1.1-3.amzn2.0.2
  - **AL2023.12 version:** 1.5-6.amzn2023.0.1

- ** `libverto` **
  - **RPM:**  libverto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libverto-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libverto-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libverto-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libverto-libevent  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libverto-libevent-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.5-4.amzn2.0.2
  - **AL2023.12 version:** 0.3.2-1.amzn2023.0.2

- ** `libvoikko` **
  - **RPM:**  libvoikko  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvoikko-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  voikko-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.6-5.amzn2.0.1
  - **AL2023.12 version:** 4.3.3-1.amzn2023.0.1

- ** `libvorbis` **
  - **RPM:**  libvorbis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvorbis-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvorbis-devel-docs  / **Architectures:** noarch
  - **AL2 version:** 1.3.3-8.amzn2.0.2
  - **AL2023.12 version:** 1.3.7-3.amzn2023.0.2

- ** `libvpx` **
  - **RPM:**  libvpx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvpx-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libvpx-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.0-5.amzn2.0.4
  - **AL2023.12 version:** 1.11.0-1.amzn2023.0.5

- ** `libwacom` **
  - **RPM:**  libwacom  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwacom-data  / **Architectures:** noarch
  - **RPM:**  libwacom-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.24-4.amzn2
  - **AL2023.12 version:** 1.12-1.amzn2023.0.2

- ** `libwebp` **
  - **RPM:**  libwebp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwebp-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.0-10.amzn2.0.2
  - **AL2023.12 version:** 1.2.4-1.amzn2023.0.6

- ** `libwpd` **
  - **RPM:**  libwpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwpd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwpd-doc  / **Architectures:** noarch
  - **RPM:**  libwpd-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.10.0-2.amzn2
  - **AL2023.12 version:** 0.10.3-8.amzn2023.0.2

- ** `libX11` **
  - **RPM:**  libX11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libX11-common  / **Architectures:** noarch
  - **RPM:**  libX11-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.7-3.amzn2.0.5
  - **AL2023.12 version:** 1.8.10-2.amzn2023.0.1

- ** `libXau` **
  - **RPM:**  libXau  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXau-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.8-2.1.amzn2.0.2
  - **AL2023.12 version:** 1.0.11-6.amzn2023.0.1

- ** `libXaw` **
  - **RPM:**  libXaw  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXaw-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.13-4.amzn2.0.2
  - **AL2023.12 version:** 1.0.15-3.amzn2023.0.1

- ** `libxcb` **
  - **RPM:**  libxcb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxcb-doc  / **Architectures:** noarch
  - **AL2 version:** 1.12-1.amzn2.0.2
  - **AL2023.12 version:** 1.17.0-1.amzn2023.0.1

- ** `libXcomposite` **
  - **RPM:**  libXcomposite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXcomposite-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.4-4.1.amzn2.0.2
  - **AL2023.12 version:** 0.4.6-3.amzn2023.0.1

- ** `libXcursor` **
  - **RPM:**  libXcursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXcursor-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.15-1.amzn2
  - **AL2023.12 version:** 1.2.1-7.amzn2023.0.1

- ** `libXdamage` **
  - **RPM:**  libXdamage  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXdamage-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.4-4.1.amzn2.0.2
  - **AL2023.12 version:** 1.1.6-3.amzn2023.0.1

- ** `libXdmcp` **
  - **RPM:**  libXdmcp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXdmcp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.2-6.amzn2.0.2
  - **AL2023.12 version:** 1.1.4-3.amzn2023.0.1

- ** `libXext` **
  - **RPM:**  libXext  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXext-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.3-3.amzn2.0.2
  - **AL2023.12 version:** 1.3.6-1.amzn2023.0.1

- ** `libXfixes` **
  - **RPM:**  libXfixes  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXfixes-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.0.3-1.amzn2.0.2
  - **AL2023.12 version:** 6.0.1-3.amzn2023.0.1

- ** `libXfont2` **
  - **RPM:**  libXfont2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXfont2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.3-1.amzn2.0.1
  - **AL2023.12 version:** 2.0.7-1.amzn2023.0.2

- ** `libXft` **
  - **RPM:**  libXft  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXft-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.2-2.amzn2.0.2
  - **AL2023.12 version:** 2.3.8-6.amzn2023.0.1

- ** `libXi` **
  - **RPM:**  libXi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXi-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.9-1.amzn2.0.2
  - **AL2023.12 version:** 1.8.2-1.amzn2023.0.1

- ** `libXinerama` **
  - **RPM:**  libXinerama  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXinerama-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.3-2.1.amzn2.0.2
  - **AL2023.12 version:** 1.1.5-6.amzn2023.0.1

- ** `libxkbcommon` **
  - **RPM:**  libxkbcommon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbcommon-x11-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.1-3.amzn2
  - **AL2023.12 version:** 1.6.0-2.amzn2023.0.1

- ** `libxkbfile` **
  - **RPM:**  libxkbfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxkbfile-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.9-3.amzn2.0.2
  - **AL2023.12 version:** 1.1.3-1.amzn2023.0.1

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.1-6.amzn2.5.26
  - **AL2023.12 version:** 2.10.4-1.amzn2023.0.20

- ** `libXmu` **
  - **RPM:**  libXmu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXmu-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.2-2.amzn2.0.2
  - **AL2023.12 version:** 1.2.1-1.amzn2023.0.1

- ** `libXpm` **
  - **RPM:**  libXpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXpm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.5.12-9.amzn2.0.4
  - **AL2023.12 version:** 3.5.17-3.amzn2023.0.2

- ** `libXrandr` **
  - **RPM:**  libXrandr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXrandr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.1-2.amzn2.0.3
  - **AL2023.12 version:** 1.5.4-3.amzn2023.0.1

- ** `libXrender` **
  - **RPM:**  libXrender  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXrender-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.10-1.amzn2.0.2
  - **AL2023.12 version:** 0.9.11-6.amzn2023.0.1

- ** `libXres` **
  - **RPM:**  libXres  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXres-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.0-1.amzn2
  - **AL2023.12 version:** 1.2.2-3.amzn2023.0.1

- ** `libXScrnSaver` **
  - **RPM:**  libXScrnSaver  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXScrnSaver-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.2-6.1.amzn2.0.2
  - **AL2023.12 version:** 1.2.4-3.amzn2023.0.1

- ** `libxshmfence` **
  - **RPM:**  libxshmfence  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxshmfence-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2-1.amzn2.0.2
  - **AL2023.12 version:** 1.3.2-3.amzn2023.0.1

- ** `libxslt` **
  - **RPM:**  libxslt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxslt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.28-6.amzn2.0.5
  - **AL2023.12 version:** 1.1.43-1.amzn2023.0.3

- ** `libXt` **
  - **RPM:**  libXt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.5-3.amzn2.0.2
  - **AL2023.12 version:** 1.3.0-3.amzn2023.0.1

- ** `libXtst` **
  - **RPM:**  libXtst  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXtst-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.3-1.amzn2.0.2
  - **AL2023.12 version:** 1.2.5-1.amzn2023.0.1

- ** `libXv` **
  - **RPM:**  libXv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXv-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.11-1.amzn2.0.2
  - **AL2023.12 version:** 1.0.12-3.amzn2023.0.1

- ** `libXxf86dga` **
  - **RPM:**  libXxf86dga  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXxf86dga-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.4-2.1.amzn2.0.2
  - **AL2023.12 version:** 1.1.6-3.amzn2023.0.1

- ** `libXxf86vm` **
  - **RPM:**  libXxf86vm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXxf86vm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.4-1.amzn2.0.2
  - **AL2023.12 version:** 1.1.5-6.amzn2023.0.1

- ** `libyaml` **
  - **RPM:**  libyaml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libyaml-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1.4-11.amzn2.0.2
  - **AL2023.12 version:** 0.2.5-5.amzn2023.0.2

- ** `libzip` **
  - **RPM:**  libzip  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzip-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzip-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.2-1.amzn2.0.1
  - **AL2023.12 version:** 1.7.3-4.amzn2023.0.3

- ** `linuxdoc-tools` **
  - **RPM:**  linuxdoc-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.68-5.amzn2.0.2
  - **AL2023.12 version:** 0.9.72-11.amzn2023.0.3

- ** `linux-firmware` **
  - **RPM:**  amd-ucode-firmware  / **Architectures:** noarch
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
  - **RPM:**  linux-firmware  / **Architectures:** noarch
  - **AL2 version:** 20200421-85.git78c0348.amzn2
  - **AL2023.12 version:** 20210208-117.amzn2023.0.7

- ** `lklug-fonts` **
  - **RPM:**  lklug-fonts
  - **Architectures:** noarch
  - **AL2 version:** 0.6-10.20090803cvs.amzn2
  - **AL2023.12 version:** 0.6-24.20090803cvs.amzn2023.0.3

- ** `lksctp-tools` **
  - **RPM:**  lksctp-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lksctp-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lksctp-tools-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.17-2.amzn2.0.2
  - **AL2023.12 version:** 1.0.18-9.amzn2023.0.3

- ** `lldpad` **
  - **RPM:**  lldpad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lldpad-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.1-5.git036e314.amzn2.0.1
  - **AL2023.12 version:** 1.1.0-12.git85e5583.amzn2023

- ** [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-doc  / **Architectures:** noarch
  - **RPM:**  llvm-googletest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  llvm-test  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.1.0-1.amzn2.0.2
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.1

- ** [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (`llvm7.0` in AL2) **
  - **RPM:**  [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (llvm7.0 in AL2)  / **Architectures:**
  - **RPM:**  llvm-devel (llvm7.0-devel in AL2)  / **Architectures:**
  - **RPM:**  llvm-doc (llvm7.0-doc in AL2)  / **Architectures:**
  - **RPM:**  llvm-libs (llvm7.0-libs in AL2)  / **Architectures:**
  - **RPM:**  llvm-static (llvm7.0-static in AL2)  / **Architectures:**
  - **AL2 version:** 7.0.1-1.amzn2.0.3
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.1

- ** `lm_sensors` **
  - **RPM:**  lm\_sensors  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lm\_sensors-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lm\_sensors-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lm\_sensors-sensord  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.4.0-8.20160601gitf9185e5.amzn2
  - **AL2023.12 version:** 3.6.0-8.amzn2023.0.3

- ** `lockdev` **
  - **RPM:**  lockdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lockdev-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.4-0.13.20111007git.amzn2.0.2
  - **AL2023.12 version:** 1.0.4-0.35.20111007git.amzn2023.0.3

- ** `log4j` **
  - **RPM:**  log4j
  - **Architectures:** noarch
  - **AL2 version:** 1.2.17-18.amzn2
  - **AL2023.12 version:** 2.17.2-1.amzn2023.0.5

- ** `logrotate` **
  - **RPM:**  logrotate
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.8.6-15.amzn2
  - **AL2023.12 version:** 3.20.1-2.amzn2023.0.3

- ** `lohit-assamese-fonts` **
  - **RPM:**  lohit-assamese-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-2.amzn2
  - **AL2023.12 version:** 2.91.5-11.amzn2023.0.3

- ** `lohit-bengali-fonts` **
  - **RPM:**  lohit-bengali-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-4.amzn2
  - **AL2023.12 version:** 2.91.5-11.amzn2023.0.3

- ** `lohit-devanagari-fonts` **
  - **RPM:**  lohit-devanagari-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-4.amzn2
  - **AL2023.12 version:** 2.95.4-12.amzn2023.0.3

- ** `lohit-gujarati-fonts` **
  - **RPM:**  lohit-gujarati-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-2.amzn2
  - **AL2023.12 version:** 2.92.4-11.amzn2023.0.3

- ** `lohit-kannada-fonts` **
  - **RPM:**  lohit-kannada-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-3.amzn2
  - **AL2023.12 version:** 2.5.4-10.amzn2023.0.3

- ** `lohit-marathi-fonts` **
  - **RPM:**  lohit-marathi-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-2.amzn2
  - **AL2023.12 version:** 2.94.2-12.amzn2023.0.3

- ** `lohit-tamil-fonts` **
  - **RPM:**  lohit-tamil-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-2.amzn2
  - **AL2023.12 version:** 2.91.3-11.amzn2023.0.3

- ** `lohit-telugu-fonts` **
  - **RPM:**  lohit-telugu-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.5.3-3.amzn2
  - **AL2023.12 version:** 2.5.5-10.amzn2023.0.3

- ** `lshw` **
  - **RPM:**  lshw
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** B.02.18-12.amzn2
  - **AL2023.12 version:** B.02.19.2-7.amzn2023.0.3

- ** `lsof` **
  - **RPM:**  lsof
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.87-6.amzn2
  - **AL2023.12 version:** 4.94.0-1.amzn2023.0.3

- ** `lsscsi` **
  - **RPM:**  lsscsi
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.27-6.amzn2.0.2
  - **AL2023.12 version:** 0.32-2.amzn2023.0.1

- ** `ltrace` **
  - **RPM:**  ltrace
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.91-14.amzn2.0.1
  - **AL2023.12 version:** 0.7.91-44.amzn2023.0.2

- ** `lua` **
  - **RPM:**  lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lua-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lua-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.1.4-15.amzn2.0.2
  - **AL2023.12 version:** 5.4.4-3.amzn2023.0.2

- ** `lua` (`lua53` in AL2) **
  - **RPM:**  lua (lua53 in AL2)  / **Architectures:**
  - **RPM:**  lua-devel (lua53-devel in AL2)  / **Architectures:**
  - **RPM:**  lua-libs (lua53-libs in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lua-static (lua53-static in AL2)  / **Architectures:**
  - **AL2 version:** 5.3.5-7.amzn2.0.1
  - **AL2023.12 version:** 5.4.4-3.amzn2023.0.2

- ** `lvm2` **
  - **RPM:**  device-mapper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-event-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  device-mapper-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lvm2-lockd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.02.170-6.amzn2.5
  - **AL2023.12 version:** 1.02.185-1.amzn2023.0.5

- ** `lynx` **
  - **RPM:**  lynx
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.8.9-4.amzn2
  - **AL2023.12 version:** 2.8.9-13.amzn2023.0.3

- ** `lz4` **
  - **RPM:**  lz4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lz4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lz4-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.5-2.amzn2.0.2
  - **AL2023.12 version:** 1.9.4-1.amzn2023.0.3

- ** `lzo` **
  - **RPM:**  lzo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lzo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  lzo-minilzo  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.06-8.amzn2.0.4
  - **AL2023.12 version:** 2.10-4.amzn2023.0.2

- ** `lzop` **
  - **RPM:**  lzop
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.03-10.amzn2.0.1
  - **AL2023.12 version:** 1.04-6.amzn2023.0.2

- ** `m17n-db` **
  - **RPM:**  m17n-db  / **Architectures:** noarch
  - **RPM:**  m17n-db-devel  / **Architectures:** noarch
  - **RPM:**  m17n-db-extras  / **Architectures:** noarch
  - **AL2 version:** 1.6.4-4.amzn2
  - **AL2023.12 version:** 1.8.0-21.amzn2023.0.3

- ** `m17n-lib` **
  - **RPM:**  m17n-lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  m17n-lib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  m17n-lib-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.4-14.amzn2.0.2
  - **AL2023.12 version:** 1.8.0-9.amzn2023.0.3

- ** `m4` **
  - **RPM:**  m4
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.16-10.amzn2.0.2
  - **AL2023.12 version:** 1.4.19-2.amzn2023.0.2

- ** `mailcap` **
  - **RPM:**  mailcap
  - **Architectures:** noarch
  - **AL2 version:** 2.1.41-2.amzn2
  - **AL2023.12 version:** 2.1.49-3.amzn2023.0.3

- ** `mailx` **
  - **RPM:**  mailx
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 12.5-19.amzn2
  - **AL2023.12 version:** 12.5-43.amzn2023.0.1

- ** `make` **
  - **RPM:**  make
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.82-24.amzn2
  - **AL2023.12 version:** 4.3-5.amzn2023.0.2

- ** `mallard-rng` **
  - **RPM:**  mallard-rng
  - **Architectures:** noarch
  - **AL2 version:** 1.0.2-1.amzn2
  - **AL2023.12 version:** 1.1.0-5.amzn2023.0.3

- ** `man-db` **
  - **RPM:**  man-db
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.6.3-9.amzn2.0.3
  - **AL2023.12 version:** 2.9.3-3.amzn2023.0.3

- ** `man-pages` **
  - **RPM:**  man-pages
  - **Architectures:** noarch
  - **AL2 version:** 3.53-5.amzn2
  - **AL2023.12 version:** 6.04-3.amzn2023.0.1

- ** `mariadb105` (`mariadb` in AL2) **
  - **RPM:**  mariadb105 (mariadb in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-devel (mariadb-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-server (mariadb-server in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-test (mariadb-test in AL2)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.5.68-1.amzn2.0.1
  - **AL2023.12 version:** 10.5.29-1.amzn2023.0.1

- ** `maven` **
  - **RPM:**  maven  / **Architectures:** noarch
  - **RPM:**  maven-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.0.5-17.amzn2
  - **AL2023.12 version:** 3.8.4-3.amzn2023.0.5

- ** `maven2` **
  - **RPM:**  maven2-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-artifact  / **Architectures:** noarch
  - **RPM:**  maven-artifact-manager  / **Architectures:** noarch
  - **RPM:**  maven-model  / **Architectures:** noarch
  - **RPM:**  maven-monitor  / **Architectures:** noarch
  - **RPM:**  maven-plugin-descriptor  / **Architectures:** noarch
  - **RPM:**  maven-plugin-registry  / **Architectures:** noarch
  - **RPM:**  maven-profile  / **Architectures:** noarch
  - **RPM:**  maven-project  / **Architectures:** noarch
  - **RPM:**  maven-settings  / **Architectures:** noarch
  - **RPM:**  maven-toolchain  / **Architectures:** noarch
  - **AL2 version:** 2.2.1-47.amzn2
  - **AL2023.12 version:** 2.2.1-70.amzn2023.0.1

- ** `maven-antrun-plugin` **
  - **RPM:**  maven-antrun-plugin  / **Architectures:** noarch
  - **RPM:**  maven-antrun-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.7-8.amzn2
  - **AL2023.12 version:** 3.0.0-5.amzn2023.0.3

- ** `maven-archiver` **
  - **RPM:**  maven-archiver  / **Architectures:** noarch
  - **RPM:**  maven-archiver-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.5-9.amzn2
  - **AL2023.12 version:** 3.5.1-1.amzn2023.0.2

- ** `maven-assembly-plugin` **
  - **RPM:**  maven-assembly-plugin  / **Architectures:** noarch
  - **RPM:**  maven-assembly-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4-8.amzn2
  - **AL2023.12 version:** 3.3.0-8.amzn2023.0.3

- ** `maven-clean-plugin` **
  - **RPM:**  maven-clean-plugin  / **Architectures:** noarch
  - **RPM:**  maven-clean-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.5-8.amzn2
  - **AL2023.12 version:** 3.1.0-10.amzn2023.0.1

- ** `maven-common-artifact-filters` **
  - **RPM:**  maven-common-artifact-filters  / **Architectures:** noarch
  - **RPM:**  maven-common-artifact-filters-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-11.amzn2
  - **AL2023.12 version:** 3.2.0-3.amzn2023.0.3

- ** `maven-compiler-plugin` **
  - **RPM:**  maven-compiler-plugin  / **Architectures:** noarch
  - **RPM:**  maven-compiler-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.1-4.amzn2
  - **AL2023.12 version:** 3.8.1-12.amzn2023.0.3

- ** `maven-dependency-analyzer` **
  - **RPM:**  maven-dependency-analyzer  / **Architectures:** noarch
  - **RPM:**  maven-dependency-analyzer-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.3-9.amzn2
  - **AL2023.12 version:** 1.11.3-6.amzn2023.0.3

- ** `maven-dependency-plugin` **
  - **RPM:**  maven-dependency-plugin  / **Architectures:** noarch
  - **RPM:**  maven-dependency-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.7-3.amzn2
  - **AL2023.12 version:** 3.1.2-9.amzn2023.0.3

- ** `maven-dependency-tree` **
  - **RPM:**  maven-dependency-tree  / **Architectures:** noarch
  - **RPM:**  maven-dependency-tree-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0-7.amzn2
  - **AL2023.12 version:** 3.0.1-10.amzn2023.0.3

- ** `maven-doxia` **
  - **RPM:**  maven-doxia  / **Architectures:** noarch
  - **RPM:**  maven-doxia-core  / **Architectures:** noarch
  - **RPM:**  maven-doxia-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-doxia-logging-api  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-apt  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-confluence  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-docbook-simple  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-fml  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-latex  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-rtf  / **Architectures:** noarch
  - **RPM:**  maven-doxia-modules  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-twiki  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-xdoc  / **Architectures:** noarch
  - **RPM:**  maven-doxia-module-xhtml  / **Architectures:** noarch
  - **RPM:**  maven-doxia-sink-api  / **Architectures:** noarch
  - **RPM:**  maven-doxia-test-docs  / **Architectures:** noarch
  - **RPM:**  maven-doxia-tests  / **Architectures:** noarch
  - **AL2 version:** 1.4-5.amzn2
  - **AL2023.12 version:** 1.9.1-7.amzn2023.0.2

- ** `maven-doxia-sitetools` **
  - **RPM:**  maven-doxia-sitetools  / **Architectures:** noarch
  - **RPM:**  maven-doxia-sitetools-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-3.amzn2
  - **AL2023.12 version:** 1.9.2-7.amzn2023.0.1

- ** `maven-enforcer` **
  - **RPM:**  maven-enforcer  / **Architectures:** noarch
  - **RPM:**  maven-enforcer-api  / **Architectures:** noarch
  - **RPM:**  maven-enforcer-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-enforcer-plugin  / **Architectures:** noarch
  - **RPM:**  maven-enforcer-rules  / **Architectures:** noarch
  - **AL2 version:** 1.2-8.amzn2
  - **AL2023.12 version:** 3.0.0\~M3-8.amzn2023.0.3

- ** `maven-file-management` **
  - **RPM:**  maven-file-management  / **Architectures:** noarch
  - **RPM:**  maven-file-management-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2.1-8.amzn2
  - **AL2023.12 version:** 3.0.0-17.amzn2023.0.3

- ** `maven-filtering` **
  - **RPM:**  maven-filtering  / **Architectures:** noarch
  - **RPM:**  maven-filtering-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1-3.amzn2
  - **AL2023.12 version:** 3.2.0-5.amzn2023.0.3

- ** `maven-invoker` **
  - **RPM:**  maven-invoker  / **Architectures:** noarch
  - **RPM:**  maven-invoker-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.1.1-9.amzn2
  - **AL2023.12 version:** 3.1.0-3.amzn2023.0.1

- ** `maven-invoker-plugin` **
  - **RPM:**  maven-invoker-plugin  / **Architectures:** noarch
  - **RPM:**  maven-invoker-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.8-8.amzn2
  - **AL2023.12 version:** 3.2.1-8.amzn2023.0.1

- ** `maven-jar-plugin` **
  - **RPM:**  maven-jar-plugin  / **Architectures:** noarch
  - **RPM:**  maven-jar-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4-8.amzn2
  - **AL2023.12 version:** 3.2.0-9.amzn2023.0.3

- ** `maven-parent` **
  - **RPM:**  maven-parent
  - **Architectures:** noarch
  - **AL2 version:** 20-5.amzn2
  - **AL2023.12 version:** 34-10.amzn2023.0.3

- ** `maven-plugin-build-helper` **
  - **RPM:**  maven-plugin-build-helper  / **Architectures:** noarch
  - **RPM:**  maven-plugin-build-helper-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.5-13.amzn2
  - **AL2023.12 version:** 3.2.0-7.amzn2023.0.3

- ** `maven-plugin-bundle` **
  - **RPM:**  maven-plugin-bundle  / **Architectures:** noarch
  - **RPM:**  maven-plugin-bundle-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.3.7-12.amzn2
  - **AL2023.12 version:** 5.1.1-5.amzn2023.0.3

- ** `maven-plugin-testing` **
  - **RPM:**  maven-plugin-testing  / **Architectures:** noarch
  - **RPM:**  maven-plugin-testing-harness  / **Architectures:** noarch
  - **RPM:**  maven-plugin-testing-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.1-11.amzn2
  - **AL2023.12 version:** 3.3.0-25.amzn2023.0.3

- ** `maven-plugin-tools` **
  - **RPM:**  maven-plugin-annotations  / **Architectures:** noarch
  - **RPM:**  maven-plugin-plugin  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools-annotations  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools-api  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools-generators  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools-java  / **Architectures:** noarch
  - **RPM:**  maven-plugin-tools-javadocs  / **Architectures:** noarch
  - **AL2 version:** 3.1-17.amzn2
  - **AL2023.12 version:** 3.6.0-12.amzn2023.0.4

- ** `maven-remote-resources-plugin` **
  - **RPM:**  maven-remote-resources-plugin  / **Architectures:** noarch
  - **RPM:**  maven-remote-resources-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-7.amzn2
  - **AL2023.12 version:** 1.7.0-9.amzn2023.0.3

- ** `maven-reporting-api` **
  - **RPM:**  maven-reporting-api  / **Architectures:** noarch
  - **RPM:**  maven-reporting-api-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.0-5.amzn2
  - **AL2023.12 version:** 3.1.0-1.amzn2023.0.1

- ** `maven-reporting-impl` **
  - **RPM:**  maven-reporting-impl  / **Architectures:** noarch
  - **RPM:**  maven-reporting-impl-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.2-8.amzn2
  - **AL2023.12 version:** 3.1.0-1.amzn2023.0.1

- ** `maven-resources-plugin` **
  - **RPM:**  maven-resources-plugin  / **Architectures:** noarch
  - **RPM:**  maven-resources-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.6-6.amzn2
  - **AL2023.12 version:** 3.2.0-6.amzn2023.0.3

- ** `maven-script-interpreter` **
  - **RPM:**  maven-script-interpreter  / **Architectures:** noarch
  - **RPM:**  maven-script-interpreter-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-7.amzn2
  - **AL2023.12 version:** 1.2-11.amzn2023.0.1

- ** `maven-shade-plugin` **
  - **RPM:**  maven-shade-plugin  / **Architectures:** noarch
  - **RPM:**  maven-shade-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0-6.amzn2
  - **AL2023.12 version:** 3.2.4-7.amzn2023.0.1

- ** `maven-shared-incremental` **
  - **RPM:**  maven-shared-incremental  / **Architectures:** noarch
  - **RPM:**  maven-shared-incremental-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1-6.amzn2
  - **AL2023.12 version:** 1.1-25.amzn2023.0.3

- ** `maven-shared-io` **
  - **RPM:**  maven-shared-io  / **Architectures:** noarch
  - **RPM:**  maven-shared-io-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1-7.amzn2
  - **AL2023.12 version:** 3.0.0-17.amzn2023.0.3

- ** `maven-shared-utils` **
  - **RPM:**  maven-shared-utils  / **Architectures:** noarch
  - **RPM:**  maven-shared-utils-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0.4-4.amzn2
  - **AL2023.12 version:** 3.3.4-4.amzn2023.0.4

- ** `maven-source-plugin` **
  - **RPM:**  maven-source-plugin  / **Architectures:** noarch
  - **RPM:**  maven-source-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.2.1-7.amzn2
  - **AL2023.12 version:** 3.2.1-8.amzn2023.0.3

- ** `maven-surefire` **
  - **RPM:**  maven-failsafe-plugin  / **Architectures:** noarch
  - **RPM:**  maven-surefire  / **Architectures:** noarch
  - **RPM:**  maven-surefire-javadoc  / **Architectures:** noarch
  - **RPM:**  maven-surefire-plugin  / **Architectures:** noarch
  - **RPM:**  maven-surefire-provider-junit  / **Architectures:** noarch
  - **RPM:**  maven-surefire-provider-testng  / **Architectures:** noarch
  - **AL2 version:** 2.15-3.amzn2
  - **AL2023.12 version:** 3.0.0\~M4-6.amzn2023.0.4

- ** `maven-verifier` **
  - **RPM:**  maven-verifier  / **Architectures:** noarch
  - **RPM:**  maven-verifier-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-7.amzn2
  - **AL2023.12 version:** 1.7.2-8.amzn2023.0.3

- ** `maven-verifier-plugin` **
  - **RPM:**  maven-verifier-plugin  / **Architectures:** noarch
  - **RPM:**  maven-verifier-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-10.amzn2
  - **AL2023.12 version:** 1.0-30.amzn2023.0.2

- ** `maven-wagon` **
  - **RPM:**  maven-wagon  / **Architectures:** noarch
  - **RPM:**  maven-wagon-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4-3.amzn2
  - **AL2023.12 version:** 3.4.2-6.amzn2023.0.4

- ** `mc` **
  - **RPM:**  mc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.8.29-1.amzn2
  - **AL2023.12 version:** 4.8.28-2.amzn2023.0.3

- ** `mcstrans` **
  - **RPM:**  mcstrans
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.4-5.amzn2.0.2
  - **AL2023.12 version:** 3.4-3.amzn2023.0.2

- ** `mdadm` **
  - **RPM:**  mdadm
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0-5.amzn2.0.3
  - **AL2023.12 version:** 4.2-3.amzn2023.0.5

- ** `memcached` **
  - **RPM:**  memcached  / **Architectures:** aarch64, x86\_64
  - **RPM:**  memcached-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.15-10.amzn2.1.2
  - **AL2023.12 version:** 1.6.42-2.amzn2023.0.1

- ** `memkind` **
  - **RPM:**  memkind  / **Architectures:** x86\_64
  - **RPM:**  memkind-devel  / **Architectures:** x86\_64
  - **AL2 version:** 1.5.0-1.amzn2.0.2
  - **AL2023.12 version:** 1.13.0-1.amzn2023.0.3

- ** `mercurial` **
  - **RPM:**  mercurial  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mercurial-hgk  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.6.2-10.amzn2
  - **AL2023.12 version:** 5.7.1-1.amzn2023.0.3

- ** `mesa` **
  - **RPM:**  mesa-dri-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libEGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libgbm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libglapi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGL-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libOSMesa-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libxatracker  / **Architectures:** x86\_64
  - **RPM:**  mesa-libxatracker-devel  / **Architectures:** x86\_64
  - **RPM:**  mesa-vdpau-drivers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-vulkan-drivers  / **Architectures:** x86\_64
  - **AL2 version:** 18.3.4-5.amzn2.0.2
  - **AL2023.12 version:** 24.2.6-1268.amzn2023.0.1

- ** `mesa-demos` **
  - **RPM:**  glx-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-demos  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.2.0-3.amzn2.0.1
  - **AL2023.12 version:** 9.0.0-8.amzn2023

- ** `mesa-libGLU` **
  - **RPM:**  mesa-libGLU  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mesa-libGLU-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.0.0-4.amzn2.0.2
  - **AL2023.12 version:** 9.0.1-4.amzn2023.0.3

- ** `metacity` **
  - **RPM:**  metacity  / **Architectures:** aarch64, x86\_64
  - **RPM:**  metacity-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.34.13-7.amzn2.0.1
  - **AL2023.12 version:** 3.54.0-334.amzn2023

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2 version:** 2.1-47.amzn2.4.27
  - **AL2023.12 version:** 2.1-53.amzn2023.0.15

- ** `mlocate` **
  - **RPM:**  mlocate
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.26-8.amzn2
  - **AL2023.12 version:** 0.26-351.amzn2023

- ** `mod_auth_mellon` **
  - **RPM:**  mod\_auth\_mellon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_auth\_mellon-diagnostics  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.14.0-9.amzn2.0.1
  - **AL2023.12 version:** 0.19.0-2.amzn2023

- ** `mod_auth_openidc` **
  - **RPM:**  mod\_auth\_openidc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.8-7.amzn2
  - **AL2023.12 version:** 2.4.16.11-1.amzn2023.0.1

- ** `mod_fcgid` **
  - **RPM:**  mod\_fcgid
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.9-6.amzn2
  - **AL2023.12 version:** 2.3.9-24.amzn2023.0.3

- ** `mod_http2` **
  - **RPM:**  mod\_http2
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.42-1.amzn2.0.1
  - **AL2023.12 version:** 2.0.42-1.amzn2023.0.1

- ** `mod_security` **
  - **RPM:**  mod\_security  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mod\_security-mlogc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.12-1.amzn2.0.1
  - **AL2023.12 version:** 2.9.12-1.amzn2023.0.1

- ** `mod_security_crs` **
  - **RPM:**  mod\_security\_crs
  - **Architectures:** noarch
  - **AL2 version:** 2.2.9-1.amzn2
  - **AL2023.12 version:** 4.2.0-1.amzn2023.0.3

- ** `modello` **
  - **RPM:**  modello  / **Architectures:** noarch
  - **RPM:**  modello-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.7-4.amzn2
  - **AL2023.12 version:** 1.11-8.amzn2023.0.3

- ** `mojo-parent` **
  - **RPM:**  mojo-parent
  - **Architectures:** noarch
  - **AL2 version:** 32-4.amzn2
  - **AL2023.12 version:** 60-5.amzn2023.0.3

- ** `mokutil` **
  - **RPM:**  mokutil
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.0-10.amzn2.0.1
  - **AL2023.12 version:** 0.6.0-6.amzn2023

- ** `mozilla-filesystem` **
  - **RPM:**  mozilla-filesystem
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9-11.amzn2.0.2
  - **AL2023.12 version:** 1.9-25.amzn2023.0.3

- ** `mpfr` **
  - **RPM:**  mpfr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mpfr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.1-4.amzn2.0.2
  - **AL2023.12 version:** 4.1.0-7.amzn2023.0.2

- ** `mpg123` **
  - **RPM:**  mpg123  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mpg123-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mpg123-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mpg123-plugins-pulseaudio  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.32.9-1.amzn2
  - **AL2023.12 version:** 1.32.10-54.amzn2023

- ** `mtdev` **
  - **RPM:**  mtdev  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mtdev-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.5-5.amzn2.0.2
  - **AL2023.12 version:** 1.1.5-20.amzn2023.0.3

- ** `mtools` **
  - **RPM:**  mtools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0.18-5.amzn2.0.2
  - **AL2023.12 version:** 4.0.35-1.amzn2023.0.3

- ** `mtr` **
  - **RPM:**  mtr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mtr-gtk  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.92-2.amzn2.0.2
  - **AL2023.12 version:** 0.95-3.amzn2023.0.2

- ** `multilib-rpm-config` **
  - **RPM:**  multilib-rpm-config
  - **Architectures:** noarch
  - **AL2 version:** 1-6.amzn2
  - **AL2023.12 version:** 1-17.amzn2023.0.3

- ** `munge-maven-plugin` **
  - **RPM:**  munge-maven-plugin  / **Architectures:** noarch
  - **RPM:**  munge-maven-plugin-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-2.amzn2
  - **AL2023.12 version:** 1.0-24.amzn2023.0.3

- ** `mutt` **
  - **RPM:**  mutt
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.21-29.amzn2.0.2
  - **AL2023.12 version:** 2.2.9-1.amzn2023.0.2

- ** `mutter` **
  - **RPM:**  mutter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mutter-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.3-14.amzn2
  - **AL2023.12 version:** 47.4-587.amzn2023

- ** `nano` **
  - **RPM:**  nano
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.9.8-2.amzn2.0.2
  - **AL2023.12 version:** 8.3-1.amzn2023

- ** `nasm` **
  - **RPM:**  nasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nasm-doc  / **Architectures:** noarch
  - **RPM:**  nasm-rdoff  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.15.03-3.amzn2.0.3
  - **AL2023.12 version:** 2.15.05-1.amzn2023.0.6

- ** `nautilus` **
  - **RPM:**  nautilus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nautilus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nautilus-extensions  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.26.3.1-6.amzn2.0.1
  - **AL2023.12 version:** 47.1-719.amzn2023

- ** `ncompress` **
  - **RPM:**  ncompress
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.2.4.4-3.amzn2.0.2
  - **AL2023.12 version:** 4.2.4.4-19.amzn2023.0.3

- ** `ncurses` **
  - **RPM:**  ncurses  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-base  / **Architectures:** noarch
  - **RPM:**  ncurses-c\+\+-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-compat-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-term  / **Architectures:** noarch
  - **AL2 version:** 6.0-8.20170212.amzn2.1.8
  - **AL2023.12 version:** 6.6-1.amzn2023.0.1

- ** `ndctl` **
  - **RPM:**  daxctl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  daxctl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  daxctl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ndctl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ndctl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ndctl-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 64.1-2.amzn2
  - **AL2023.12 version:** 71.1-2.amzn2023.0.3

- ** `nerdctl` **
  - **RPM:**  nerdctl
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.2-1.amzn2.0.4
  - **AL2023.12 version:** 2.2.2-1.amzn2023.0.4

- ** `netlabel_tools` **
  - **RPM:**  netlabel\_tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.20-5.amzn2.0.2
  - **AL2023.12 version:** 0.30.0-13.amzn2023.0.1

- ** `netpbm` **
  - **RPM:**  netpbm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netpbm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netpbm-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netpbm-progs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 10.79.00-7.amzn2
  - **AL2023.12 version:** 10.96.00-1.amzn2023.0.3

- ** `net-snmp` **
  - **RPM:**  net-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-agent-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-gui  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  net-snmp-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.7.2-49.amzn2.1.3
  - **AL2023.12 version:** 5.9.3-2.amzn2023.0.4

- ** `nettle` **
  - **RPM:**  nettle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nettle-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.7.1-9.amzn2
  - **AL2023.12 version:** 3.10.1-1.amzn2023.0.1

- ** `net-tools` **
  - **RPM:**  net-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0-0.22.20131004git.amzn2.0.3
  - **AL2023.12 version:** 2.0-0.59.20160912git.amzn2023.0.3

- ** `newt` **
  - **RPM:**  newt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  newt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.52.15-4.amzn2.0.2
  - **AL2023.12 version:** 0.52.21-9.amzn2023.0.3

- ** `nfs4-acl-tools` **
  - **RPM:**  nfs4-acl-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.3-17.amzn2
  - **AL2023.12 version:** 0.4.2-1.amzn2023

- ** `nfs-utils` **
  - **RPM:**  nfs-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.0-0.54.amzn2.0.2
  - **AL2023.12 version:** 2.5.4-2.rc3.amzn2023.0.3

- ** `nftables` **
  - **RPM:**  nftables  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nftables-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.0-14.amzn2.0.1
  - **AL2023.12 version:** 1.0.4-3.amzn2023.0.3

- ** `nghttp2` **
  - **RPM:**  libnghttp2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnghttp2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nghttp2  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.52.0-1.amzn2.0.1
  - **AL2023.12 version:** 1.59.0-3.amzn2023.0.2

- ** `ninja-build` **
  - **RPM:**  ninja-build
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.2-2.amzn2.0.1
  - **AL2023.12 version:** 1.10.2-2.amzn2023.0.3

- ** `nmap` **
  - **RPM:**  nmap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nmap-ncat  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.40-19.amzn2.0.1
  - **AL2023.12 version:** 7.93-4.amzn2023

- ** `nodejs-packaging` **
  - **RPM:**  nodejs-packaging
  - **Architectures:** noarch
  - **AL2 version:** 17-3.amzn2.0.1
  - **AL2023.12 version:** 2021.06-2.amzn2023.0.3

- ** `nss` **
  - **RPM:**  nss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-sysinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.90.0-2.amzn2.0.3
  - **AL2023.12 version:** 3.112.0-8.amzn2023.0.2

- ** `nss_wrapper` **
  - **RPM:**  nss\_wrapper
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.3-1.amzn2.0.2
  - **AL2023.12 version:** 1.1.11-5.amzn2023.0.2

- ** `nss-pam-ldapd` **
  - **RPM:**  nss-pam-ldapd
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.9-3.amzn2.0.1
  - **AL2023.12 version:** 0.9.10-9.amzn2023.0.2

- ** `nss-pem` **
  - **RPM:**  nss-pem
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.3-5.amzn2
  - **AL2023.12 version:** 1.0.8-1.amzn2023.0.2

- ** `numactl` **
  - **RPM:**  numactl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  numactl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  numactl-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.9-7.amzn2
  - **AL2023.12 version:** 2.0.14-3.amzn2023.0.3

- ** `numad` **
  - **RPM:**  numad
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.5-18.20150602git.amzn2
  - **AL2023.12 version:** 0.5-34.20150602git.amzn2023.0.3

- ** `nvme-cli` **
  - **RPM:**  nvme-cli
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.11.1-1.amzn2.0.7
  - **AL2023.12 version:** 2.13-1.amzn2023.0.3

- ** `nvml` **
  - **RPM:**  libpmem  / **Architectures:** x86\_64
  - **RPM:**  libpmemblk  / **Architectures:** x86\_64
  - **RPM:**  libpmemblk-debug  / **Architectures:** x86\_64
  - **RPM:**  libpmemblk-devel  / **Architectures:** x86\_64
  - **RPM:**  libpmem-debug  / **Architectures:** x86\_64
  - **RPM:**  libpmem-devel  / **Architectures:** x86\_64
  - **RPM:**  libpmemlog  / **Architectures:** x86\_64
  - **RPM:**  libpmemlog-debug  / **Architectures:** x86\_64
  - **RPM:**  libpmemlog-devel  / **Architectures:** x86\_64
  - **RPM:**  libpmemobj  / **Architectures:** x86\_64
  - **RPM:**  libpmemobj-debug  / **Architectures:** x86\_64
  - **RPM:**  libpmemobj-devel  / **Architectures:** x86\_64
  - **RPM:**  libpmempool  / **Architectures:** x86\_64
  - **RPM:**  libpmempool-debug  / **Architectures:** x86\_64
  - **RPM:**  libpmempool-devel  / **Architectures:** x86\_64
  - **RPM:**  librpmem  / **Architectures:** x86\_64
  - **RPM:**  librpmem-debug  / **Architectures:** x86\_64
  - **RPM:**  librpmem-devel  / **Architectures:** x86\_64
  - **RPM:**  rpmemd  / **Architectures:** x86\_64
  - **AL2 version:** 1.3-3.amzn2
  - **AL2023.12 version:** 1.10.1-1.amzn2023.0.4

- ** `objectweb-asm` **
  - **RPM:**  objectweb-asm  / **Architectures:** noarch
  - **RPM:**  objectweb-asm-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.3.1-9.amzn2
  - **AL2023.12 version:** 9.2-3.amzn2023.0.3

- ** `ocaml` **
  - **RPM:**  ocaml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-compiler-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-ocamldoc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-source  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.05.0-6.amzn2
  - **AL2023.12 version:** 4.13.1-4.amzn2023.0.3

- ** `ocaml-findlib` **
  - **RPM:**  ocaml-findlib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-findlib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.3-8.amzn2
  - **AL2023.12 version:** 1.9.3-2.amzn2023.0.3

- ** `ocaml-ocamlbuild` **
  - **RPM:**  ocaml-ocamlbuild  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-ocamlbuild-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ocaml-ocamlbuild-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.11.0-9.amzn2
  - **AL2023.12 version:** 0.14.0-32.amzn2023.0.3

- ** `ocaml-srpm-macros` **
  - **RPM:**  ocaml-srpm-macros
  - **Architectures:** noarch
  - **AL2 version:** 5-2.amzn2
  - **AL2023.12 version:** 6-6.amzn2023.0.2

- ** `oddjob` **
  - **RPM:**  oddjob  / **Architectures:** aarch64, x86\_64
  - **RPM:**  oddjob-mkhomedir  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.31.5-4.amzn2.0.1
  - **AL2023.12 version:** 0.34.7-2.amzn2023.0.3

- ** `oniguruma` **
  - **RPM:**  oniguruma  / **Architectures:** aarch64, x86\_64
  - **RPM:**  oniguruma-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.9.6-1.amzn2.0.7
  - **AL2023.12 version:** 6.9.7.1-1.amzn2023.0.2

- ** `openjade` **
  - **RPM:**  openjade
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.2-45.amzn2.0.3
  - **AL2023.12 version:** 1.3.2-66.amzn2023.0.3

- ** `openjpeg2` **
  - **RPM:**  openjpeg2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openjpeg2-devel-docs  / **Architectures:** noarch
  - **RPM:**  openjpeg2-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.0-5.amzn2.0.2
  - **AL2023.12 version:** 2.5.2-5.amzn2023.0.1

- ** `openldap` **
  - **RPM:**  openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-servers  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.4.44-25.amzn2.0.7
  - **AL2023.12 version:** 2.4.57-6.amzn2023.0.7

- ** `openmpi` **
  - **RPM:**  openmpi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openmpi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openmpi-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openmpi-java-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-openmpi  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0.1-11.amzn2.0.1
  - **AL2023.12 version:** 4.1.2-3.amzn2023.0.4

- ** `opensc` **
  - **RPM:**  opensc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.19.0-6.amzn2.0.4
  - **AL2023.12 version:** 0.24.0-1.amzn2023.0.6

- ** `openscap` **
  - **RPM:**  openscap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-containers  / **Architectures:** noarch
  - **RPM:**  openscap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-engine-sce-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-scanner  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openscap-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.17-2.amzn2.0.1
  - **AL2023.12 version:** 1.3.13-1.amzn2023.0.1

- ** `opensm` **
  - **RPM:**  opensm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opensm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opensm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opensm-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.20-2.amzn2
  - **AL2023.12 version:** 3.3.23-6.amzn2023.0.3

- ** `opensp` **
  - **RPM:**  opensp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opensp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.2-19.amzn2.0.2
  - **AL2023.12 version:** 1.5.2-36.amzn2023.0.3

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.4p1-22.amzn2.0.13
  - **AL2023.12 version:** 9.9p1-10.amzn2023.0.2

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2k-24.amzn2.0.21
  - **AL2023.12 version:** 3.5.7-2.amzn2023.0.1

- ** `openssl` (`openssl11` in AL2) **
  - **RPM:**  openssl (openssl11 in AL2)  / **Architectures:**
  - **RPM:**  openssl-devel (openssl11-devel in AL2)  / **Architectures:**
  - **RPM:**  openssl-libs (openssl11-libs in AL2)  / **Architectures:**
  - **AL2 version:** 1.1.1zh-1.amzn2.0.1
  - **AL2023.12 version:** 3.5.7-2.amzn2023.0.1

- ** `openssl-pkcs11` **
  - **RPM:**  libp11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-pkcs11  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.10-3.amzn2.0.1
  - **AL2023.12 version:** 0.4.12-3.amzn2023.0.1

- ** `openssl-pkcs11` (`openssl11-pkcs11` in AL2) **
  - **RPM:**  openssl-pkcs11 (openssl11-pkcs11 in AL2)
  - **Architectures:**
  - **AL2 version:** 0.4.10-6.amzn2.0.1
  - **AL2023.12 version:** 0.4.12-3.amzn2023.0.1

- ** `open-vmdk` **
  - **RPM:**  open-vmdk
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.6-1.amzn2
  - **AL2023.12 version:** 0.3.6-1.amzn2023

- ** `open-vm-tools` **
  - **RPM:**  open-vm-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-salt-minion  / **Architectures:** x86\_64
  - **RPM:**  open-vm-tools-sdmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  open-vm-tools-test  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 12.3.0-1.amzn2.0.4
  - **AL2023.12 version:** 12.3.0-1.amzn2023.0.5

- ** `opus` **
  - **RPM:**  opus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  opus-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-6.amzn2.0.2
  - **AL2023.12 version:** 1.3.1-8.amzn2023.0.3

- ** `orc` **
  - **RPM:**  orc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-compiler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  orc-doc  / **Architectures:** noarch
  - **AL2 version:** 0.4.26-1.amzn2.0.3
  - **AL2023.12 version:** 0.4.31-4.amzn2023.0.4

- ** `osinfo-db` **
  - **RPM:**  osinfo-db
  - **Architectures:** noarch
  - **AL2 version:** 20170813-6.amzn2
  - **AL2023.12 version:** 20240701-1.amzn2023.0.1

- ** `osinfo-db-tools` **
  - **RPM:**  osinfo-db-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.0-1.amzn2.0.2
  - **AL2023.12 version:** 1.12.0-1.amzn2023.0.1

- ** `os-prober` **
  - **RPM:**  os-prober
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.58-9.amzn2.0.2
  - **AL2023.12 version:** 1.77-7.amzn2023.0.3

- ** `overpass-fonts` **
  - **RPM:**  overpass-fonts
  - **Architectures:** noarch
  - **AL2 version:** 2.1-1.amzn2
  - **AL2023.12 version:** 3.0.4-5.amzn2023.0.3

- ** `p11-kit` **
  - **RPM:**  p11-kit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p11-kit-trust  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.23.22-1.amzn2.0.1
  - **AL2023.12 version:** 0.24.1-2.amzn2023.0.3

- ** `pacemaker` **
  - **RPM:**  pacemaker  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pacemaker-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pacemaker-cluster-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pacemaker-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pacemaker-libs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pacemaker-remote  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.23-1.amzn2.1
  - **AL2023.12 version:** 3.0.1-0.4.rc2.amzn2023.0.1

- ** `PackageKit` **
  - **RPM:**  PackageKit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-command-not-found  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-cron  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  PackageKit-gtk3-module  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.5-2.amzn2.0.4
  - **AL2023.12 version:** 1.2.8-2.amzn2023.0.2

- ** `paktype-naskh-basic-fonts` **
  - **RPM:**  paktype-naskh-basic-fonts
  - **Architectures:** noarch
  - **AL2 version:** 4.1-3.amzn2
  - **AL2023.12 version:** 6.0-1.amzn2023.0.3

- ** `pam` **
  - **RPM:**  pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.8-23.amzn2.0.5
  - **AL2023.12 version:** 1.5.1-8.amzn2023.0.8

- ** `pam_radius` **
  - **RPM:**  pam\_radius
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.0-17.amzn2
  - **AL2023.12 version:** 3.0.0-2.amzn2023.0.1

- ** `pango` **
  - **RPM:**  pango  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pango-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pango-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.42.4-4.amzn2
  - **AL2023.12 version:** 1.54.0-2.amzn2023.0.4

- ** `pangomm` **
  - **RPM:**  pangomm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pangomm-doc  / **Architectures:** noarch
  - **AL2 version:** 2.40.1-1.amzn2.0.2
  - **AL2023.12 version:** 2.46.4-101.amzn2023

- ** `papi` **
  - **RPM:**  papi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  papi-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  papi-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.2.0-26.amzn2
  - **AL2023.12 version:** 6.0.0-8.amzn2023.0.5

- ** `parted` **
  - **RPM:**  parted  / **Architectures:** aarch64, x86\_64
  - **RPM:**  parted-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1-29.amzn2
  - **AL2023.12 version:** 3.4-2.amzn2023.0.2

- ** `passwd` **
  - **RPM:**  passwd
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.79-5.amzn2
  - **AL2023.12 version:** 0.80-10.amzn2023.0.2

- ** `patch` **
  - **RPM:**  patch
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.7.1-12.amzn2.0.2
  - **AL2023.12 version:** 2.7.6-14.amzn2023.0.2

- ** `patchelf` **
  - **RPM:**  patchelf
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.17.0-1.amzn2.0.1
  - **AL2023.12 version:** 0.17.0-1.amzn2023.0.2

- ** `patchutils` **
  - **RPM:**  patchutils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.3-4.amzn2.0.1
  - **AL2023.12 version:** 0.4.2-5.amzn2023.0.2

- ** `pciutils` **
  - **RPM:**  pciutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pciutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pciutils-devel-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pciutils-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.5.1-3.amzn2
  - **AL2023.12 version:** 3.7.0-3.amzn2023.0.2

- ** [`pcre`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre) **
  - **RPM:**  [`pcre`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`pcre-devel`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`pcre-static`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`pcre-tools`](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-pcre)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.32-17.amzn2.0.3
  - **AL2023.12 version:** 8.44-3.amzn2023.1.0.3

- ** `pcre2` **
  - **RPM:**  pcre2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-utf16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-utf32  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 10.23-11.amzn2.0.2
  - **AL2023.12 version:** 10.40-1.amzn2023.0.3

- ** `pcs` **
  - **RPM:**  pcs
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.169-3.amzn2.3.0.7
  - **AL2023.12 version:** 0.12.1-1.amzn2023.0.2

- ** `pcsc-lite` **
  - **RPM:**  pcsc-lite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcsc-lite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcsc-lite-doc  / **Architectures:** noarch
  - **RPM:**  pcsc-lite-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.8-7.amzn2
  - **AL2023.12 version:** 1.9.1-1.amzn2023.0.4

- ** `pcsc-lite-ccid` **
  - **RPM:**  pcsc-lite-ccid
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.10-13.amzn2
  - **AL2023.12 version:** 1.4.34-1.amzn2023.0.3

- ** [`perl`](https://docs.aws.amazon.com/linux/al2023/ug/perl.html) **
  - **RPM:**  [`perl`](https://docs.aws.amazon.com/linux/al2023/ug/perl.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-ExtUtils-Embed  / **Architectures:** noarch
  - **RPM:**  perl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Locale-Maketext-Simple  / **Architectures:** noarch
  - **RPM:**  perl-Module-Loaded  / **Architectures:** noarch
  - **RPM:**  perl-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Time-Piece  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.16.3-299.amzn2.0.4
  - **AL2023.12 version:** 5.32.1-477.amzn2023.0.9

- ** `perl-Algorithm-Diff` **
  - **RPM:**  perl-Algorithm-Diff
  - **Architectures:** noarch
  - **AL2 version:** 1.1902-17.amzn2
  - **AL2023.12 version:** 1.2010-2.amzn2023.0.2

- ** `perl-AppConfig` **
  - **RPM:**  perl-AppConfig
  - **Architectures:** noarch
  - **AL2 version:** 1.66-20.amzn2
  - **AL2023.12 version:** 1.71-20.amzn2023.0.2

- ** `perl-Archive-Extract` **
  - **RPM:**  perl-Archive-Extract
  - **Architectures:** noarch
  - **AL2 version:** 0.68-3.amzn2
  - **AL2023.12 version:** 0.88-1.amzn2023.0.2

- ** `perl-Archive-Tar` **
  - **RPM:**  perl-Archive-Tar
  - **Architectures:** noarch
  - **AL2 version:** 1.92-3.amzn2.0.2
  - **AL2023.12 version:** 3.04-522.amzn2023.0.3

- ** `perl-Archive-Zip` **
  - **RPM:**  perl-Archive-Zip
  - **Architectures:** noarch
  - **AL2 version:** 1.30-11.amzn2
  - **AL2023.12 version:** 1.68-4.amzn2023.0.2

- ** `perl-Authen-SASL` **
  - **RPM:**  perl-Authen-SASL
  - **Architectures:** noarch
  - **AL2 version:** 2.15-10.amzn2.0.1
  - **AL2023.12 version:** 2.16-23.amzn2023.0.3

- ** `perl-autodie` **
  - **RPM:**  perl-autodie
  - **Architectures:** noarch
  - **AL2 version:** 2.16-2.amzn2.0.1
  - **AL2023.12 version:** 2.37-522.amzn2023.0.1

- ** `perl-Bit-Vector` **
  - **RPM:**  perl-Bit-Vector
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.3-3.amzn2.0.2
  - **AL2023.12 version:** 7.4-22.amzn2023.0.4

- ** `perl-B-Keywords` **
  - **RPM:**  perl-B-Keywords
  - **Architectures:** noarch
  - **AL2 version:** 1.13-2.amzn2
  - **AL2023.12 version:** 1.22-1.amzn2023.0.2

- ** `perl-Browser-Open` **
  - **RPM:**  perl-Browser-Open
  - **Architectures:** noarch
  - **AL2 version:** 0.04-6.amzn2
  - **AL2023.12 version:** 0.04-27.amzn2023.0.2

- ** `perl-Business-ISBN` **
  - **RPM:**  perl-Business-ISBN
  - **Architectures:** noarch
  - **AL2 version:** 2.06-2.amzn2
  - **AL2023.12 version:** 3.006-2.amzn2023.0.2

- ** `perl-Business-ISBN-Data` **
  - **RPM:**  perl-Business-ISBN-Data
  - **Architectures:** noarch
  - **AL2 version:** 20120719.001-2.amzn2
  - **AL2023.12 version:** 20210112.006-1.amzn2023.0.2

- ** `perl-Capture-Tiny` **
  - **RPM:**  perl-Capture-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 0.24-1.amzn2
  - **AL2023.12 version:** 0.50-4.amzn2023.0.1

- ** `perl-Carp` **
  - **RPM:**  perl-Carp
  - **Architectures:** noarch
  - **AL2 version:** 1.26-244.amzn2
  - **AL2023.12 version:** 1.50-458.amzn2023.0.2

- ** `perl-Carp-Clan` **
  - **RPM:**  perl-Carp-Clan
  - **Architectures:** noarch
  - **AL2 version:** 6.04-10.amzn2
  - **AL2023.12 version:** 6.08-6.amzn2023.0.2

- ** `perl-CGI` **
  - **RPM:**  perl-CGI
  - **Architectures:** noarch
  - **AL2 version:** 3.63-4.amzn2
  - **AL2023.12 version:** 4.71-1.amzn2023.0.1

- ** `perl-Class-Data-Inheritable` **
  - **RPM:**  perl-Class-Data-Inheritable
  - **Architectures:** noarch
  - **AL2 version:** 0.08-14.amzn2
  - **AL2023.12 version:** 0.10-4.amzn2023.0.1

- ** `perl-Class-Inspector` **
  - **RPM:**  perl-Class-Inspector
  - **Architectures:** noarch
  - **AL2 version:** 1.28-2.amzn2
  - **AL2023.12 version:** 1.36-5.amzn2023.0.2

- ** `perl-Class-ISA` **
  - **RPM:**  perl-Class-ISA
  - **Architectures:** noarch
  - **AL2 version:** 0.36-1010.amzn2
  - **AL2023.12 version:** 0.36-1032.amzn2023.0.2

- ** `perl-Class-Load` **
  - **RPM:**  perl-Class-Load
  - **Architectures:** noarch
  - **AL2 version:** 0.20-3.amzn2
  - **AL2023.12 version:** 0.25-14.amzn2023.0.2

- ** `perl-Class-Load-XS` **
  - **RPM:**  perl-Class-Load-XS
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.06-3.amzn2.0.2
  - **AL2023.12 version:** 0.10-14.amzn2023.0.3

- ** `perl-Class-Singleton` **
  - **RPM:**  perl-Class-Singleton
  - **Architectures:** noarch
  - **AL2 version:** 1.4-14.amzn2
  - **AL2023.12 version:** 1.6-2.amzn2023.0.2

- ** `perl-Clone` **
  - **RPM:**  perl-Clone
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.34-5.amzn2.0.2
  - **AL2023.12 version:** 0.47-4.amzn2023.0.2

- ** `perl-Compress-Raw-Bzip2` **
  - **RPM:**  perl-Compress-Raw-Bzip2
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.061-3.amzn2.0.2
  - **AL2023.12 version:** 2.217-1.amzn2023.0.2

- ** `perl-Compress-Raw-Zlib` **
  - **RPM:**  perl-Compress-Raw-Zlib
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.061-4.amzn2.0.2
  - **AL2023.12 version:** 2.221-1.amzn2023.0.2

- ** `perl-Config-Simple` **
  - **RPM:**  perl-Config-Simple
  - **Architectures:** noarch
  - **AL2 version:** 4.59-15.amzn2
  - **AL2023.12 version:** 4.59-36.amzn2023.0.2

- ** `perl-Config-Tiny` **
  - **RPM:**  perl-Config-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 2.14-7.amzn2
  - **AL2023.12 version:** 2.26-1.amzn2023.0.2

- ** `perl-constant` **
  - **RPM:**  perl-constant
  - **Architectures:** noarch
  - **AL2 version:** 1.27-2.amzn2.0.1
  - **AL2023.12 version:** 1.33-459.amzn2023.0.2

- ** `perl-Convert-ASN1` **
  - **RPM:**  perl-Convert-ASN1
  - **Architectures:** noarch
  - **AL2 version:** 0.26-4.amzn2
  - **AL2023.12 version:** 0.34-7.amzn2023.0.1

- ** `perl-Convert-BinHex` **
  - **RPM:**  perl-Convert-BinHex
  - **Architectures:** noarch
  - **AL2 version:** 1.119-20.amzn2.0.1
  - **AL2023.12 version:** 1.125-30.amzn2023.0.1

- ** `perl-CPAN-Changes` **
  - **RPM:**  perl-CPAN-Changes
  - **Architectures:** noarch
  - **AL2 version:** 0.20-2.amzn2
  - **AL2023.12 version:** 0.400002-17.amzn2023.0.2

- ** `perl-CPAN-Meta` **
  - **RPM:**  perl-CPAN-Meta
  - **Architectures:** noarch
  - **AL2 version:** 2.120921-5.amzn2
  - **AL2023.12 version:** 2.150013-1.amzn2023.0.1

- ** `perl-CPAN-Meta-Requirements` **
  - **RPM:**  perl-CPAN-Meta-Requirements
  - **Architectures:** noarch
  - **AL2 version:** 2.122-7.amzn2
  - **AL2023.12 version:** 2.145-1.amzn2023.0.1

- ** `perl-CPAN-Meta-YAML` **
  - **RPM:**  perl-CPAN-Meta-YAML
  - **Architectures:** noarch
  - **AL2 version:** 0.008-14.amzn2
  - **AL2023.12 version:** 0.020-522.amzn2023.0.1

- ** `perl-Crypt-CBC` **
  - **RPM:**  perl-Crypt-CBC
  - **Architectures:** noarch
  - **AL2 version:** 2.33-2.amzn2
  - **AL2023.12 version:** 3.07-2.amzn2023.0.1

- ** `perl-Crypt-DES` **
  - **RPM:**  perl-Crypt-DES
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.05-20.amzn2.0.2
  - **AL2023.12 version:** 2.07-30.amzn2023.0.4

- ** `perl-Crypt-OpenSSL-Bignum` **
  - **RPM:**  perl-Crypt-OpenSSL-Bignum
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.04-18.amzn2.0.2
  - **AL2023.12 version:** 0.09-23.amzn2023.0.1

- ** `perl-Crypt-OpenSSL-Random` **
  - **RPM:**  perl-Crypt-OpenSSL-Random
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.04-21.amzn2.0.2
  - **AL2023.12 version:** 0.17-6.amzn2023.0.2

- ** `perl-Crypt-OpenSSL-RSA` **
  - **RPM:**  perl-Crypt-OpenSSL-RSA
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.28-7.amzn2.0.3
  - **AL2023.12 version:** 0.33-3.amzn2023.0.1

- ** `perl-Crypt-PasswdMD5` **
  - **RPM:**  perl-Crypt-PasswdMD5
  - **Architectures:** noarch
  - **AL2 version:** 1.3-17.amzn2.0.1
  - **AL2023.12 version:** 1.4.1-1.amzn2023.0.3

- ** `perl-Crypt-SSLeay` **
  - **RPM:**  perl-Crypt-SSLeay
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.64-5.amzn2.0.2
  - **AL2023.12 version:** 0.72-45.amzn2023.0.2

- ** `perl-CSS-Tiny` **
  - **RPM:**  perl-CSS-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 1.19-5.amzn2
  - **AL2023.12 version:** 1.20-15.amzn2023.0.2

- ** `perl-Data-Dumper` **
  - **RPM:**  perl-Data-Dumper
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.145-3.amzn2.0.2
  - **AL2023.12 version:** 2.191-522.amzn2023.0.3

- ** `perl-Data-OptList` **
  - **RPM:**  perl-Data-OptList
  - **Architectures:** noarch
  - **AL2 version:** 0.107-9.amzn2
  - **AL2023.12 version:** 0.110-15.amzn2023.0.2

- ** `perl-Date-Calc` **
  - **RPM:**  perl-Date-Calc
  - **Architectures:** noarch
  - **AL2 version:** 6.3-14.amzn2
  - **AL2023.12 version:** 6.4-18.amzn2023.0.2

- ** `perl-Date-Manip` **
  - **RPM:**  perl-Date-Manip
  - **Architectures:** noarch
  - **AL2 version:** 6.41-2.amzn2.0.1
  - **AL2023.12 version:** 6.85-1.amzn2023.0.3

- ** `perl-DateTime` **
  - **RPM:**  perl-DateTime
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.04-6.amzn2.1.0
  - **AL2023.12 version:** 1.54-2.amzn2023.0.3

- ** `perl-DateTime-Format-DateParse` **
  - **RPM:**  perl-DateTime-Format-DateParse
  - **Architectures:** noarch
  - **AL2 version:** 0.05-5.amzn2
  - **AL2023.12 version:** 0.05-25.amzn2023.0.2

- ** `perl-DateTime-Locale` **
  - **RPM:**  perl-DateTime-Locale
  - **Architectures:** noarch
  - **AL2 version:** 0.45-6.amzn2
  - **AL2023.12 version:** 1.32-1.amzn2023.0.2

- ** `perl-DateTime-TimeZone` **
  - **RPM:**  perl-DateTime-TimeZone
  - **Architectures:** noarch
  - **AL2 version:** 1.70-2.amzn2
  - **AL2023.12 version:** 2.51-1.amzn2023.0.2

- ** `perl-DB_File` **
  - **RPM:**  perl-DB\_File
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.830-6.amzn2.0.2
  - **AL2023.12 version:** 1.860-1.amzn2023.0.2

- ** `perl-DBD-MySQL` **
  - **RPM:**  perl-DBD-MySQL
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.023-6.amzn2
  - **AL2023.12 version:** 4.050-10.amzn2023.0.3

- ** `perl-DBD-Pg` **
  - **RPM:**  perl-DBD-Pg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-DBD-Pg-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.19.3-4.amzn2.0.2
  - **AL2023.12 version:** 3.18.0-6.amzn2023.0.2

- ** `perl-DBD-SQLite` **
  - **RPM:**  perl-DBD-SQLite
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.39-3.amzn2.0.2
  - **AL2023.12 version:** 1.66-3.amzn2023.0.4

- ** `perl-DBI` **
  - **RPM:**  perl-DBI
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.627-4.amzn2.0.6
  - **AL2023.12 version:** 1.651-1.amzn2023.0.1

- ** `perl-Devel-CheckLib` **
  - **RPM:**  perl-Devel-CheckLib
  - **Architectures:** noarch
  - **AL2 version:** 0.99-2.amzn2
  - **AL2023.12 version:** 1.14-6.amzn2023.0.2

- ** `perl-Devel-Cover` **
  - **RPM:**  perl-Devel-Cover
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.03-3.amzn2.0.2
  - **AL2023.12 version:** 1.36-4.amzn2023.0.3

- ** `perl-Devel-Cycle` **
  - **RPM:**  perl-Devel-Cycle
  - **Architectures:** noarch
  - **AL2 version:** 1.11-13.amzn2
  - **AL2023.12 version:** 1.12-20.amzn2023.0.2

- ** `perl-Devel-EnforceEncapsulation` **
  - **RPM:**  perl-Devel-EnforceEncapsulation
  - **Architectures:** noarch
  - **AL2 version:** 0.50-8.amzn2
  - **AL2023.12 version:** 0.51-21.amzn2023.0.2

- ** `perl-Devel-Leak` **
  - **RPM:**  perl-Devel-Leak
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.03-22.amzn2.0.2
  - **AL2023.12 version:** 0.03-45.amzn2023.0.3

- ** `perl-Devel-StackTrace` **
  - **RPM:**  perl-Devel-StackTrace
  - **Architectures:** noarch
  - **AL2 version:** 1.30-2.amzn2
  - **AL2023.12 version:** 2.05-7.amzn2023.0.1

- ** `perl-Devel-Symdump` **
  - **RPM:**  perl-Devel-Symdump
  - **Architectures:** noarch
  - **AL2 version:** 2.10-2.amzn2
  - **AL2023.12 version:** 2.18-17.amzn2023.0.2

- ** `perl-Digest` **
  - **RPM:**  perl-Digest
  - **Architectures:** noarch
  - **AL2 version:** 1.17-245.amzn2
  - **AL2023.12 version:** 1.20-1.amzn2023.0.2

- ** `perl-Digest-HMAC` **
  - **RPM:**  perl-Digest-HMAC
  - **Architectures:** noarch
  - **AL2 version:** 1.03-5.amzn2
  - **AL2023.12 version:** 1.05-4.amzn2023.0.1

- ** `perl-Digest-MD5` **
  - **RPM:**  perl-Digest-MD5
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.52-3.amzn2.0.2
  - **AL2023.12 version:** 2.59-521.amzn2023.0.2

- ** `perl-Digest-SHA` **
  - **RPM:**  perl-Digest-SHA
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.85-4.amzn2.0.2
  - **AL2023.12 version:** 6.04-522.amzn2023.0.2

- ** `perl-Digest-SHA1` **
  - **RPM:**  perl-Digest-SHA1
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.13-9.amzn2.0.2
  - **AL2023.12 version:** 2.13-32.amzn2023.0.3

- ** `perl-Dist-CheckConflicts` **
  - **RPM:**  perl-Dist-CheckConflicts
  - **Architectures:** noarch
  - **AL2 version:** 0.06-2.amzn2
  - **AL2023.12 version:** 0.11-21.amzn2023.0.2

- ** `perl-Email-Date-Format` **
  - **RPM:**  perl-Email-Date-Format
  - **Architectures:** noarch
  - **AL2 version:** 1.002-15.amzn2
  - **AL2023.12 version:** 1.008-8.amzn2023.0.1

- ** `perl-Encode` **
  - **RPM:**  perl-Encode  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Encode-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.51-7.amzn2.0.2
  - **AL2023.12 version:** 3.21-520.amzn2023.0.2

- ** `perl-Encode-Detect` **
  - **RPM:**  perl-Encode-Detect
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.01-13.amzn2.0.2
  - **AL2023.12 version:** 1.01-44.amzn2023.0.1

- ** `perl-Encode-Locale` **
  - **RPM:**  perl-Encode-Locale
  - **Architectures:** noarch
  - **AL2 version:** 1.03-5.amzn2
  - **AL2023.12 version:** 1.05-19.amzn2023.0.2

- ** `perl-Env` **
  - **RPM:**  perl-Env
  - **Architectures:** noarch
  - **AL2 version:** 1.04-2.amzn2
  - **AL2023.12 version:** 1.04-458.amzn2023.0.2

- ** `perl-Error` **
  - **RPM:**  perl-Error
  - **Architectures:** noarch
  - **AL2 version:** 0.17020-2.amzn2
  - **AL2023.12 version:** 0.17030-2.amzn2023.0.1

- ** `perl-Exception-Class` **
  - **RPM:**  perl-Exception-Class
  - **Architectures:** noarch
  - **AL2 version:** 1.37-3.amzn2
  - **AL2023.12 version:** 1.44-11.amzn2023.0.2

- ** `perl-Exporter` **
  - **RPM:**  perl-Exporter
  - **Architectures:** noarch
  - **AL2 version:** 5.68-3.amzn2
  - **AL2023.12 version:** 5.79-520.amzn2023.0.1

- ** `perl-ExtUtils-MakeMaker` **
  - **RPM:**  perl-ExtUtils-MakeMaker
  - **Architectures:** noarch
  - **AL2 version:** 6.68-3.amzn2
  - **AL2023.12 version:** 7.62-1.amzn2023.0.2

- ** `perl-ExtUtils-Manifest` **
  - **RPM:**  perl-ExtUtils-Manifest
  - **Architectures:** noarch
  - **AL2 version:** 1.61-244.amzn2
  - **AL2023.12 version:** 1.75-521.amzn2023.0.1

- ** `perl-ExtUtils-ParseXS` **
  - **RPM:**  perl-ExtUtils-ParseXS
  - **Architectures:** noarch
  - **AL2 version:** 3.18-3.amzn2
  - **AL2023.12 version:** 3.61-2.amzn2023.0.1

- ** `perl-File-Copy-Recursive` **
  - **RPM:**  perl-File-Copy-Recursive
  - **Architectures:** noarch
  - **AL2 version:** 0.38-14.amzn2
  - **AL2023.12 version:** 0.45-5.amzn2023.0.2

- ** `perl-File-Fetch` **
  - **RPM:**  perl-File-Fetch
  - **Architectures:** noarch
  - **AL2 version:** 0.42-2.amzn2
  - **AL2023.12 version:** 1.08-4.amzn2023.0.1

- ** `perl-File-Find-Rule` **
  - **RPM:**  perl-File-Find-Rule
  - **Architectures:** noarch
  - **AL2 version:** 0.33-5.amzn2.0.1
  - **AL2023.12 version:** 0.35-3.amzn2023.0.1

- ** `perl-File-Find-Rule-Perl` **
  - **RPM:**  perl-File-Find-Rule-Perl
  - **Architectures:** noarch
  - **AL2 version:** 1.13-2.amzn2.0.2
  - **AL2023.12 version:** 1.15-19.amzn2023.0.3

- ** `perl-File-HomeDir` **
  - **RPM:**  perl-File-HomeDir
  - **Architectures:** noarch
  - **AL2 version:** 1.00-4.amzn2
  - **AL2023.12 version:** 1.006-2.amzn2023.0.2

- ** `perl-File-Inplace` **
  - **RPM:**  perl-File-Inplace
  - **Architectures:** noarch
  - **AL2 version:** 0.20-8.amzn2
  - **AL2023.12 version:** 0.20-28.amzn2023.0.2

- ** `perl-File-Listing` **
  - **RPM:**  perl-File-Listing
  - **Architectures:** noarch
  - **AL2 version:** 6.04-7.amzn2
  - **AL2023.12 version:** 6.14-2.amzn2023.0.2

- ** `perl-File-Path` **
  - **RPM:**  perl-File-Path
  - **Architectures:** noarch
  - **AL2 version:** 2.09-2.amzn2.0.1
  - **AL2023.12 version:** 2.18-2.amzn2023.0.2

- ** `perl-File-pushd` **
  - **RPM:**  perl-File-pushd
  - **Architectures:** noarch
  - **AL2 version:** 1.005-2.amzn2
  - **AL2023.12 version:** 1.016-10.amzn2023.0.2

- ** `perl-File-Remove` **
  - **RPM:**  perl-File-Remove
  - **Architectures:** noarch
  - **AL2 version:** 1.52-6.amzn2
  - **AL2023.12 version:** 1.61-11.amzn2023.0.1

- ** `perl-File-ShareDir` **
  - **RPM:**  perl-File-ShareDir
  - **Architectures:** noarch
  - **AL2 version:** 1.03-8.amzn2
  - **AL2023.12 version:** 1.118-2.amzn2023.0.2

- ** `perl-File-Slurp` **
  - **RPM:**  perl-File-Slurp
  - **Architectures:** noarch
  - **AL2 version:** 9999.19-6.amzn2
  - **AL2023.12 version:** 9999.32-3.amzn2023.0.2

- ** `perl-File-Temp` **
  - **RPM:**  perl-File-Temp
  - **Architectures:** noarch
  - **AL2 version:** 0.23.01-3.amzn2
  - **AL2023.12 version:** 0.231.200-2.amzn2023.0.1

- ** `perl-File-Which` **
  - **RPM:**  perl-File-Which
  - **Architectures:** noarch
  - **AL2 version:** 1.09-12.amzn2
  - **AL2023.12 version:** 1.27-15.amzn2023.0.1

- ** `perl-Filter` **
  - **RPM:**  perl-Filter
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.49-3.amzn2.0.2
  - **AL2023.12 version:** 1.65-2.amzn2023.0.2

- ** `perl-Font-AFM` **
  - **RPM:**  perl-Font-AFM
  - **Architectures:** noarch
  - **AL2 version:** 1.20-13.amzn2
  - **AL2023.12 version:** 1.20-35.amzn2023.0.2

- ** `perl-Font-TTF` **
  - **RPM:**  perl-Font-TTF
  - **Architectures:** noarch
  - **AL2 version:** 1.02-3.amzn2
  - **AL2023.12 version:** 1.06-15.amzn2023.0.2

- ** `perl-FreezeThaw` **
  - **RPM:**  perl-FreezeThaw
  - **Architectures:** noarch
  - **AL2 version:** 0.5001-10.amzn2
  - **AL2023.12 version:** 0.5001-35.amzn2023.0.2

- ** `perl-GD` **
  - **RPM:**  perl-GD
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.49-3.amzn2.0.3
  - **AL2023.12 version:** 2.80-1.amzn2023.0.3

- ** `perl-GD-Barcode` **
  - **RPM:**  perl-GD-Barcode
  - **Architectures:** noarch
  - **AL2 version:** 1.15-15.amzn2
  - **AL2023.12 version:** 1.15-37.amzn2023.0.2

- ** `perl-Getopt-Long` **
  - **RPM:**  perl-Getopt-Long
  - **Architectures:** noarch
  - **AL2 version:** 2.40-3.amzn2
  - **AL2023.12 version:** 2.58-521.amzn2023.0.1

- ** `perl-GSSAPI` **
  - **RPM:**  perl-GSSAPI
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.28-9.amzn2.0.2
  - **AL2023.12 version:** 0.28-35.amzn2023.0.3

- ** `perl-Hook-LexWrap` **
  - **RPM:**  perl-Hook-LexWrap
  - **Architectures:** noarch
  - **AL2 version:** 0.24-2.amzn2
  - **AL2023.12 version:** 0.26-13.amzn2023.0.2

- ** `perl-HTML-FormatText-WithLinks` **
  - **RPM:**  perl-HTML-FormatText-WithLinks
  - **Architectures:** noarch
  - **AL2 version:** 0.14-8.amzn2
  - **AL2023.12 version:** 0.15-18.amzn2023.0.2

- ** `perl-HTML-FormatText-WithLinks-AndTables` **
  - **RPM:**  perl-HTML-FormatText-WithLinks-AndTables
  - **Architectures:** noarch
  - **AL2 version:** 0.02-4.amzn2
  - **AL2023.12 version:** 0.07-14.amzn2023.0.2

- ** `perl-HTML-Parser` **
  - **RPM:**  perl-HTML-Parser
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.71-4.amzn2.0.3
  - **AL2023.12 version:** 3.76-1.amzn2023.0.4

- ** `perl-HTML-Tagset` **
  - **RPM:**  perl-HTML-Tagset
  - **Architectures:** noarch
  - **AL2 version:** 3.20-15.amzn2
  - **AL2023.12 version:** 3.24-5.amzn2023.0.1

- ** `perl-HTML-Tree` **
  - **RPM:**  perl-HTML-Tree
  - **Architectures:** noarch
  - **AL2 version:** 5.03-2.amzn2
  - **AL2023.12 version:** 5.07-14.amzn2023.0.2

- ** `perl-HTTP-Cookies` **
  - **RPM:**  perl-HTTP-Cookies
  - **Architectures:** noarch
  - **AL2 version:** 6.01-5.amzn2
  - **AL2023.12 version:** 6.10-2.amzn2023.0.2

- ** `perl-HTTP-Daemon` **
  - **RPM:**  perl-HTTP-Daemon
  - **Architectures:** noarch
  - **AL2 version:** 6.01-8.amzn2.0.2
  - **AL2023.12 version:** 6.16-1.amzn2023.0.1

- ** `perl-HTTP-Date` **
  - **RPM:**  perl-HTTP-Date
  - **Architectures:** noarch
  - **AL2 version:** 6.02-8.amzn2
  - **AL2023.12 version:** 6.06-8.amzn2023.0.1

- ** `perl-HTTP-Message` **
  - **RPM:**  perl-HTTP-Message
  - **Architectures:** noarch
  - **AL2 version:** 6.06-6.amzn2
  - **AL2023.12 version:** 6.34-1.amzn2023.0.2

- ** `perl-HTTP-Negotiate` **
  - **RPM:**  perl-HTTP-Negotiate
  - **Architectures:** noarch
  - **AL2 version:** 6.01-5.amzn2
  - **AL2023.12 version:** 6.01-28.amzn2023.0.2

- ** `perl-HTTP-Tiny` **
  - **RPM:**  perl-HTTP-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 0.033-3.amzn2.0.2
  - **AL2023.12 version:** 0.092-2.amzn2023.0.2

- ** `perl-Image-Base` **
  - **RPM:**  perl-Image-Base
  - **Architectures:** noarch
  - **AL2 version:** 1.07-23.amzn2
  - **AL2023.12 version:** 1.17-19.amzn2023.0.2

- ** `perl-Image-Info` **
  - **RPM:**  perl-Image-Info
  - **Architectures:** noarch
  - **AL2 version:** 1.33-3.amzn2
  - **AL2023.12 version:** 1.42-5.amzn2023.0.2

- ** `perl-Image-Xbm` **
  - **RPM:**  perl-Image-Xbm
  - **Architectures:** noarch
  - **AL2 version:** 1.08-21.amzn2
  - **AL2023.12 version:** 1.11-4.amzn2023.0.1

- ** `perl-Image-Xpm` **
  - **RPM:**  perl-Image-Xpm
  - **Architectures:** noarch
  - **AL2 version:** 1.09-21.amzn2
  - **AL2023.12 version:** 1.13-14.amzn2023.0.2

- ** `perl-IO-CaptureOutput` **
  - **RPM:**  perl-IO-CaptureOutput
  - **Architectures:** noarch
  - **AL2 version:** 1.1102-9.amzn2
  - **AL2023.12 version:** 1.1105-5.amzn2023.0.2

- ** `perl-IO-Compress` **
  - **RPM:**  perl-IO-Compress
  - **Architectures:** noarch
  - **AL2 version:** 2.061-2.amzn2.0.1
  - **AL2023.12 version:** 2.217-1.amzn2023.0.2

- ** `perl-IO-HTML` **
  - **RPM:**  perl-IO-HTML
  - **Architectures:** noarch
  - **AL2 version:** 1.00-2.amzn2
  - **AL2023.12 version:** 1.004-2.amzn2023.0.2

- ** `perl-IO-SessionData` **
  - **RPM:**  perl-IO-SessionData
  - **Architectures:** noarch
  - **AL2 version:** 1.03-1.amzn2
  - **AL2023.12 version:** 1.03-31.amzn2023.0.1

- ** `perl-IO-Socket-INET6` **
  - **RPM:**  perl-IO-Socket-INET6
  - **Architectures:** noarch
  - **AL2 version:** 2.69-5.amzn2
  - **AL2023.12 version:** 2.72-22.amzn2023.0.2

- ** `perl-IO-Socket-IP` **
  - **RPM:**  perl-IO-Socket-IP
  - **Architectures:** noarch
  - **AL2 version:** 0.21-5.amzn2
  - **AL2023.12 version:** 0.43-522.amzn2023.0.1

- ** `perl-IO-Socket-SSL` **
  - **RPM:**  perl-IO-Socket-SSL
  - **Architectures:** noarch
  - **AL2 version:** 1.94-7.amzn2.0.1
  - **AL2023.12 version:** 2.075-1.amzn2023.0.3

- ** `perl-IO-String` **
  - **RPM:**  perl-IO-String
  - **Architectures:** noarch
  - **AL2 version:** 1.08-19.amzn2
  - **AL2023.12 version:** 1.08-41.amzn2023.0.2

- ** `perl-IO-stringy` **
  - **RPM:**  perl-IO-stringy
  - **Architectures:** noarch
  - **AL2 version:** 2.110-22.amzn2
  - **AL2023.12 version:** 2.113-5.amzn2023.0.2

- ** `perl-IO-Tty` **
  - **RPM:**  perl-IO-Tty
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.10-11.amzn2.0.2
  - **AL2023.12 version:** 1.20-9.amzn2023.0.2

- ** `perl-IPC-Cmd` **
  - **RPM:**  perl-IPC-Cmd
  - **Architectures:** noarch
  - **AL2 version:** 0.80-4.amzn2
  - **AL2023.12 version:** 1.04-459.amzn2023.0.2

- ** `perl-IPC-Run` **
  - **RPM:**  perl-IPC-Run
  - **Architectures:** noarch
  - **AL2 version:** 0.92-2.amzn2
  - **AL2023.12 version:** 20200505.0-4.amzn2023.0.2

- ** `perl-IPC-Run3` **
  - **RPM:**  perl-IPC-Run3
  - **Architectures:** noarch
  - **AL2 version:** 0.045-6.amzn2
  - **AL2023.12 version:** 0.049-5.amzn2023.0.1

- ** `perl-JSON` **
  - **RPM:**  perl-JSON  / **Architectures:** noarch
  - **RPM:**  perl-JSON-tests  / **Architectures:** noarch
  - **AL2 version:** 2.59-2.amzn2
  - **AL2023.12 version:** 4.10-9.amzn2023.0.1

- ** `perl-JSON-PP` **
  - **RPM:**  perl-JSON-PP
  - **Architectures:** noarch
  - **AL2 version:** 2.27202-2.amzn2
  - **AL2023.12 version:** 4.06-2.amzn2023.0.2

- ** `perl-JSON-XS` **
  - **RPM:**  perl-JSON-XS
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.01-2.amzn2.0.1
  - **AL2023.12 version:** 4.04-2.amzn2023.0.2

- ** `perl-LDAP` **
  - **RPM:**  perl-LDAP
  - **Architectures:** noarch
  - **AL2 version:** 0.56-6.amzn2
  - **AL2023.12 version:** 0.68-3.amzn2023.0.2

- ** `perl-libwww-perl` **
  - **RPM:**  perl-libwww-perl
  - **Architectures:** noarch
  - **AL2 version:** 6.05-2.amzn2.0.1
  - **AL2023.12 version:** 6.58-1.amzn2023.0.3

- ** `perl-libxml-perl` **
  - **RPM:**  perl-libxml-perl
  - **Architectures:** noarch
  - **AL2 version:** 0.08-19.amzn2
  - **AL2023.12 version:** 0.08-42.amzn2023.0.2

- ** `perl-Locale-Codes` **
  - **RPM:**  perl-Locale-Codes
  - **Architectures:** noarch
  - **AL2 version:** 3.26-2.amzn2
  - **AL2023.12 version:** 3.68-1.amzn2023.0.2

- ** `perl-Locale-Maketext` **
  - **RPM:**  perl-Locale-Maketext
  - **Architectures:** noarch
  - **AL2 version:** 1.23-3.amzn2
  - **AL2023.12 version:** 1.29-459.amzn2023.0.2

- ** `perl-local-lib` **
  - **RPM:**  perl-homedir  / **Architectures:** noarch
  - **RPM:**  perl-local-lib  / **Architectures:** noarch
  - **AL2 version:** 1.008010-4.amzn2
  - **AL2023.12 version:** 2.000024-11.amzn2023.0.2

- ** `perl-Log-Message` **
  - **RPM:**  perl-Log-Message
  - **Architectures:** noarch
  - **AL2 version:** 0.08-3.amzn2
  - **AL2023.12 version:** 0.08-24.amzn2023.0.2

- ** `perl-Log-Message-Simple` **
  - **RPM:**  perl-Log-Message-Simple
  - **Architectures:** noarch
  - **AL2 version:** 0.10-2.amzn2
  - **AL2023.12 version:** 0.10-311.amzn2023.0.2

- ** `perl-LWP-MediaTypes` **
  - **RPM:**  perl-LWP-MediaTypes
  - **Architectures:** noarch
  - **AL2 version:** 6.02-2.amzn2
  - **AL2023.12 version:** 6.04-7.amzn2023.0.2

- ** `perl-LWP-Protocol-https` **
  - **RPM:**  perl-LWP-Protocol-https
  - **Architectures:** noarch
  - **AL2 version:** 6.04-4.amzn2
  - **AL2023.12 version:** 6.10-2.amzn2023.0.2

- ** `perl-Mail-DKIM` **
  - **RPM:**  perl-Mail-DKIM
  - **Architectures:** noarch
  - **AL2 version:** 0.39-8.amzn2
  - **AL2023.12 version:** 1.20230630-1.amzn2023

- ** `perl-Mail-SPF` **
  - **RPM:**  perl-Mail-SPF
  - **Architectures:** noarch
  - **AL2 version:** 2.8.0-4.amzn2
  - **AL2023.12 version:** 2.9.0-32.amzn2023

- ** `perl-MailTools` **
  - **RPM:**  perl-MailTools
  - **Architectures:** noarch
  - **AL2 version:** 2.12-2.amzn2
  - **AL2023.12 version:** 2.21-7.amzn2023.0.2

- ** `perl-MIME-Lite` **
  - **RPM:**  perl-MIME-Lite
  - **Architectures:** noarch
  - **AL2 version:** 3.030-1.amzn2
  - **AL2023.12 version:** 3.031-5.amzn2023.0.2

- ** `perl-MIME-tools` **
  - **RPM:**  perl-MIME-tools
  - **Architectures:** noarch
  - **AL2 version:** 5.505-1.amzn2
  - **AL2023.12 version:** 5.515-3.amzn2023.0.1

- ** `perl-MIME-Types` **
  - **RPM:**  perl-MIME-Types
  - **Architectures:** noarch
  - **AL2 version:** 1.38-2.amzn2
  - **AL2023.12 version:** 2.18-2.amzn2023.0.2

- ** `perl-Mixin-Linewise` **
  - **RPM:**  perl-Mixin-Linewise
  - **Architectures:** noarch
  - **AL2 version:** 0.004-2.amzn2
  - **AL2023.12 version:** 0.108-19.amzn2023.0.2

- ** `perl-Module-Build` **
  - **RPM:**  perl-Module-Build
  - **Architectures:** noarch
  - **AL2 version:** 0.40.05-2.amzn2
  - **AL2023.12 version:** 0.42.31-7.amzn2023.0.2

- ** `perl-Module-Implementation` **
  - **RPM:**  perl-Module-Implementation
  - **Architectures:** noarch
  - **AL2 version:** 0.06-6.amzn2
  - **AL2023.12 version:** 0.09-28.amzn2023.0.2

- ** `perl-Module-Install` **
  - **RPM:**  perl-Module-Install
  - **Architectures:** noarch
  - **AL2 version:** 1.06-4.amzn2
  - **AL2023.12 version:** 1.19-16.amzn2023.0.2

- ** `perl-Module-Load` **
  - **RPM:**  perl-Module-Load
  - **Architectures:** noarch
  - **AL2 version:** 0.24-3.amzn2
  - **AL2023.12 version:** 0.36-2.amzn2023.0.2

- ** `perl-Module-Load-Conditional` **
  - **RPM:**  perl-Module-Load-Conditional
  - **Architectures:** noarch
  - **AL2 version:** 0.54-3.amzn2
  - **AL2023.12 version:** 0.74-2.amzn2023.0.2

- ** `perl-Module-Manifest` **
  - **RPM:**  perl-Module-Manifest
  - **Architectures:** noarch
  - **AL2 version:** 1.08-10.amzn2
  - **AL2023.12 version:** 1.09-12.amzn2023.0.2

- ** `perl-Module-Metadata` **
  - **RPM:**  perl-Module-Metadata
  - **Architectures:** noarch
  - **AL2 version:** 1.000018-2.amzn2
  - **AL2023.12 version:** 1.000037-458.amzn2023.0.2

- ** `perl-Module-Pluggable` **
  - **RPM:**  perl-Module-Pluggable
  - **Architectures:** noarch
  - **AL2 version:** 4.8-3.amzn2
  - **AL2023.12 version:** 5.2-16.amzn2023.0.2

- ** `perl-Module-Runtime` **
  - **RPM:**  perl-Module-Runtime
  - **Architectures:** noarch
  - **AL2 version:** 0.013-4.amzn2
  - **AL2023.12 version:** 0.016-11.amzn2023.0.2

- ** `perl-Module-ScanDeps` **
  - **RPM:**  perl-Module-ScanDeps
  - **Architectures:** noarch
  - **AL2 version:** 1.10-3.amzn2.0.1
  - **AL2023.12 version:** 1.37-1.amzn2023.0.1

- ** `perl-Module-Signature` **
  - **RPM:**  perl-Module-Signature
  - **Architectures:** noarch
  - **AL2 version:** 0.73-2.amzn2
  - **AL2023.12 version:** 0.87-3.amzn2023.0.2

- ** `perl-Mozilla-CA` **
  - **RPM:**  perl-Mozilla-CA
  - **Architectures:** noarch
  - **AL2 version:** 20130114-5.amzn2
  - **AL2023.12 version:** 20200520-4.amzn2023.0.2

- ** `perl-NetAddr-IP` **
  - **RPM:**  perl-NetAddr-IP
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.069-3.amzn2.0.2
  - **AL2023.12 version:** 4.079-25.amzn2023.0.1

- ** `perl-Net-DNS-Resolver-Programmable` **
  - **RPM:**  perl-Net-DNS-Resolver-Programmable
  - **Architectures:** noarch
  - **AL2 version:** 0.003-15.amzn2
  - **AL2023.12 version:** 0.009-18.amzn2023

- ** `perl-Net-HTTP` **
  - **RPM:**  perl-Net-HTTP
  - **Architectures:** noarch
  - **AL2 version:** 6.06-2.amzn2
  - **AL2023.12 version:** 6.21-1.amzn2023.0.2

- ** `perl-Net-LibIDN` **
  - **RPM:**  perl-Net-LibIDN
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12-15.amzn2.0.2
  - **AL2023.12 version:** 0.12-39.amzn2023.0.4

- ** `perl-Net-SMTP-SSL` **
  - **RPM:**  perl-Net-SMTP-SSL
  - **Architectures:** noarch
  - **AL2 version:** 1.01-13.amzn2
  - **AL2023.12 version:** 1.04-14.amzn2023.0.2

- ** `perl-Net-SSLeay` **
  - **RPM:**  perl-Net-SSLeay
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.55-6.amzn2.0.1
  - **AL2023.12 version:** 1.94-3.amzn2023.0.4

- ** `perl-Number-Compare` **
  - **RPM:**  perl-Number-Compare
  - **Architectures:** noarch
  - **AL2 version:** 0.03-6.amzn2
  - **AL2023.12 version:** 0.03-28.amzn2023.0.2

- ** `perl-Object-Deadly` **
  - **RPM:**  perl-Object-Deadly
  - **Architectures:** noarch
  - **AL2 version:** 0.09-15.amzn2
  - **AL2023.12 version:** 0.09-37.amzn2023.0.2

- ** `perl-Package-DeprecationManager` **
  - **RPM:**  perl-Package-DeprecationManager
  - **Architectures:** noarch
  - **AL2 version:** 0.13-7.amzn2
  - **AL2023.12 version:** 0.17-14.amzn2023.0.2

- ** `perl-Package-Generator` **
  - **RPM:**  perl-Package-Generator
  - **Architectures:** noarch
  - **AL2 version:** 0.103-14.amzn2
  - **AL2023.12 version:** 1.106-21.amzn2023.0.2

- ** `perl-Package-Stash` **
  - **RPM:**  perl-Package-Stash
  - **Architectures:** noarch
  - **AL2 version:** 0.34-2.amzn2
  - **AL2023.12 version:** 0.39-2.amzn2023.0.2

- ** `perl-Package-Stash-XS` **
  - **RPM:**  perl-Package-Stash-XS
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.26-3.amzn2.0.2
  - **AL2023.12 version:** 0.29-9.amzn2023.0.3

- ** `perl-PadWalker` **
  - **RPM:**  perl-PadWalker
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.96-3.amzn2.0.2
  - **AL2023.12 version:** 2.5-2.amzn2023.0.3

- ** `perl-Parallel-Iterator` **
  - **RPM:**  perl-Parallel-Iterator
  - **Architectures:** noarch
  - **AL2 version:** 1.00-8.amzn2
  - **AL2023.12 version:** 1.00-28.amzn2023.0.2

- ** `perl-Params-Check` **
  - **RPM:**  perl-Params-Check
  - **Architectures:** noarch
  - **AL2 version:** 0.38-2.amzn2
  - **AL2023.12 version:** 0.38-459.amzn2023.0.2

- ** `perl-Params-Util` **
  - **RPM:**  perl-Params-Util
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.07-6.amzn2.0.2
  - **AL2023.12 version:** 1.102-3.amzn2023.0.3

- ** `perl-Params-Validate` **
  - **RPM:**  perl-Params-Validate
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.08-4.amzn2.0.2
  - **AL2023.12 version:** 1.30-2.amzn2023.0.3

- ** `perl-PAR-Dist` **
  - **RPM:**  perl-PAR-Dist
  - **Architectures:** noarch
  - **AL2 version:** 0.49-2.amzn2
  - **AL2023.12 version:** 0.51-2.amzn2023.0.2

- ** `perl-parent` **
  - **RPM:**  perl-parent
  - **Architectures:** noarch
  - **AL2 version:** 0.225-244.amzn2.0.1
  - **AL2023.12 version:** 0.238-458.amzn2023.0.2

- ** `perl-Parse-RecDescent` **
  - **RPM:**  perl-Parse-RecDescent
  - **Architectures:** noarch
  - **AL2 version:** 1.967009-5.amzn2
  - **AL2023.12 version:** 1.967015-13.amzn2023.0.2

- ** `perl-Parse-Yapp` **
  - **RPM:**  perl-Parse-Yapp
  - **Architectures:** noarch
  - **AL2 version:** 1.05-50.amzn2
  - **AL2023.12 version:** 1.21-10.amzn2023.0.2

- ** `perl-PathTools` **
  - **RPM:**  perl-PathTools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.40-5.amzn2.0.2
  - **AL2023.12 version:** 3.78-459.amzn2023.0.3

- ** `perl-Perl-Critic` **
  - **RPM:**  perl-Perl-Critic  / **Architectures:** noarch
  - **RPM:**  perl-Test-Perl-Critic-Policy  / **Architectures:** noarch
  - **AL2 version:** 1.118-5.amzn2
  - **AL2023.12 version:** 1.140-1.amzn2023.0.2

- ** `perl-Perl-Critic-More` **
  - **RPM:**  perl-Perl-Critic-More
  - **Architectures:** noarch
  - **AL2 version:** 1.000-9.amzn2
  - **AL2023.12 version:** 1.003-20.amzn2023.0.2

- ** `perl-Perl-MinimumVersion` **
  - **RPM:**  perl-Perl-MinimumVersion
  - **Architectures:** noarch
  - **AL2 version:** 1.32-2.amzn2
  - **AL2023.12 version:** 1.40-0.amzn2023.0.2

- ** `perl-Perl-OSType` **
  - **RPM:**  perl-Perl-OSType
  - **Architectures:** noarch
  - **AL2 version:** 1.003-3.amzn2
  - **AL2023.12 version:** 1.010-459.amzn2023.0.2

- ** `perl-Pod-Checker` **
  - **RPM:**  perl-Pod-Checker
  - **Architectures:** noarch
  - **AL2 version:** 1.60-2.amzn2
  - **AL2023.12 version:** 1.74-2.amzn2023.0.2

- ** `perl-Pod-Coverage` **
  - **RPM:**  perl-Pod-Coverage
  - **Architectures:** noarch
  - **AL2 version:** 0.23-3.amzn2
  - **AL2023.12 version:** 0.23-23.amzn2023.0.2

- ** `perl-Pod-Coverage-TrustPod` **
  - **RPM:**  perl-Pod-Coverage-TrustPod
  - **Architectures:** noarch
  - **AL2 version:** 0.100002-5.amzn2
  - **AL2023.12 version:** 0.100005-11.amzn2023.0.2

- ** `perl-Pod-Eventual` **
  - **RPM:**  perl-Pod-Eventual
  - **Architectures:** noarch
  - **AL2 version:** 0.093330-12.amzn2
  - **AL2023.12 version:** 0.094001-19.amzn2023.0.2

- ** `perl-podlators` **
  - **RPM:**  perl-podlators
  - **Architectures:** noarch
  - **AL2 version:** 2.5.1-3.amzn2.0.1
  - **AL2023.12 version:** 4.14-458.amzn2023.0.2

- ** `perl-Pod-Parser` **
  - **RPM:**  perl-Pod-Parser
  - **Architectures:** noarch
  - **AL2 version:** 1.61-2.amzn2
  - **AL2023.12 version:** 1.63-445.amzn2023.0.2

- ** `perl-Pod-Perldoc` **
  - **RPM:**  perl-Pod-Perldoc
  - **Architectures:** noarch
  - **AL2 version:** 3.20-4.amzn2.0.1
  - **AL2023.12 version:** 3.28.01-459.amzn2023.0.3

- ** `perl-Pod-POM` **
  - **RPM:**  perl-Pod-POM
  - **Architectures:** noarch
  - **AL2 version:** 0.27-10.amzn2
  - **AL2023.12 version:** 2.01-18.amzn2023.0.2

- ** `perl-Pod-Simple` **
  - **RPM:**  perl-Pod-Simple
  - **Architectures:** noarch
  - **AL2 version:** 3.28-4.amzn2
  - **AL2023.12 version:** 3.42-2.amzn2023.0.2

- ** `perl-Pod-Spell` **
  - **RPM:**  perl-Pod-Spell
  - **Architectures:** noarch
  - **AL2 version:** 1.04-4.amzn2
  - **AL2023.12 version:** 1.20-18.amzn2023.0.2

- ** `perl-Pod-Usage` **
  - **RPM:**  perl-Pod-Usage
  - **Architectures:** noarch
  - **AL2 version:** 1.63-3.amzn2
  - **AL2023.12 version:** 2.01-2.amzn2023.0.2

- ** `perl-PPI` **
  - **RPM:**  perl-PPI
  - **Architectures:** noarch
  - **AL2 version:** 1.215-12.amzn2
  - **AL2023.12 version:** 1.270-6.amzn2023.0.2

- ** `perl-PPI-HTML` **
  - **RPM:**  perl-PPI-HTML
  - **Architectures:** noarch
  - **AL2 version:** 1.08-4.amzn2
  - **AL2023.12 version:** 1.08-25.amzn2023.0.2

- ** `perl-PPIx-Regexp` **
  - **RPM:**  perl-PPIx-Regexp
  - **Architectures:** noarch
  - **AL2 version:** 0.034-3.amzn2
  - **AL2023.12 version:** 0.079-1.amzn2023.0.2

- ** `perl-PPIx-Utilities` **
  - **RPM:**  perl-PPIx-Utilities
  - **Architectures:** noarch
  - **AL2 version:** 1.001000-8.amzn2
  - **AL2023.12 version:** 1.001000-40.amzn2023.0.2

- ** `perl-prefork` **
  - **RPM:**  perl-prefork
  - **Architectures:** noarch
  - **AL2 version:** 1.04-11.amzn2
  - **AL2023.12 version:** 1.05-8.amzn2023.0.2

- ** `perl-Probe-Perl` **
  - **RPM:**  perl-Probe-Perl
  - **Architectures:** noarch
  - **AL2 version:** 0.02-3.amzn2
  - **AL2023.12 version:** 0.03-20.amzn2023.0.2

- ** `perl-Readonly` **
  - **RPM:**  perl-Readonly
  - **Architectures:** noarch
  - **AL2 version:** 1.03-22.amzn2
  - **AL2023.12 version:** 2.05-14.amzn2023.0.2

- ** `perl-Readonly-XS` **
  - **RPM:**  perl-Readonly-XS
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.05-15.amzn2.0.2
  - **AL2023.12 version:** 1.05-39.amzn2023.0.3

- ** `perl-Scalar-List-Utils` **
  - **RPM:**  perl-Scalar-List-Utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.27-248.amzn2.0.2
  - **AL2023.12 version:** 1.56-459.amzn2023.0.3

- ** `perl-SGMLSpm` **
  - **RPM:**  perl-SGMLSpm
  - **Architectures:** noarch
  - **AL2 version:** 1.03ii-31.amzn2
  - **AL2023.12 version:** 1.03ii-52.amzn2023.0.2

- ** `perl-SOAP-Lite` **
  - **RPM:**  perl-SOAP-Lite
  - **Architectures:** noarch
  - **AL2 version:** 1.10-1.amzn2
  - **AL2023.12 version:** 1.27-26.amzn2023.0.1

- ** `perl-Socket` **
  - **RPM:**  perl-Socket
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.010-4.amzn2.0.2
  - **AL2023.12 version:** 2.032-1.amzn2023.0.3

- ** `perl-Socket6` **
  - **RPM:**  perl-Socket6
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.23-15.amzn2.0.2
  - **AL2023.12 version:** 0.29-9.amzn2023.0.3

- ** `perl-Sort-Versions` **
  - **RPM:**  perl-Sort-Versions
  - **Architectures:** noarch
  - **AL2 version:** 1.5-22.amzn2
  - **AL2023.12 version:** 1.62-17.amzn2023.0.2

- ** `perl-srpm-macros` **
  - **RPM:**  perl-srpm-macros
  - **Architectures:** noarch
  - **AL2 version:** 1-8.amzn2.0.1
  - **AL2023.12 version:** 1-39.amzn2023.0.2

- ** `perl-Storable` **
  - **RPM:**  perl-Storable
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.45-3.amzn2.0.3
  - **AL2023.12 version:** 3.37-522.amzn2023.0.2

- ** `perl-String-CRC32` **
  - **RPM:**  perl-String-CRC32
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4-19.amzn2.0.2
  - **AL2023.12 version:** 2.100-1.amzn2023.0.1

- ** `perl-String-Format` **
  - **RPM:**  perl-String-Format
  - **Architectures:** noarch
  - **AL2 version:** 1.16-11.amzn2
  - **AL2023.12 version:** 1.18-10.amzn2023.0.2

- ** `perl-String-ShellQuote` **
  - **RPM:**  perl-String-ShellQuote
  - **Architectures:** noarch
  - **AL2 version:** 1.04-10.amzn2
  - **AL2023.12 version:** 1.04-44.amzn2023.0.1

- ** `perl-String-Similarity` **
  - **RPM:**  perl-String-Similarity
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.04-10.amzn2.0.2
  - **AL2023.12 version:** 1.04-31.amzn2023.0.3

- ** `perl-Sub-Exporter` **
  - **RPM:**  perl-Sub-Exporter
  - **Architectures:** noarch
  - **AL2 version:** 0.986-2.amzn2
  - **AL2023.12 version:** 0.987-25.amzn2023.0.2

- ** `perl-Sub-Install` **
  - **RPM:**  perl-Sub-Install
  - **Architectures:** noarch
  - **AL2 version:** 0.926-6.amzn2
  - **AL2023.12 version:** 0.928-26.amzn2023.0.2

- ** `perl-Sub-Uplevel` **
  - **RPM:**  perl-Sub-Uplevel
  - **Architectures:** noarch
  - **AL2 version:** 0.24-4.amzn2
  - **AL2023.12 version:** 0.2800-13.amzn2023.0.2

- ** `perl-Switch` **
  - **RPM:**  perl-Switch
  - **Architectures:** noarch
  - **AL2 version:** 2.16-7.amzn2
  - **AL2023.12 version:** 2.17-21.amzn2023.0.2

- ** `perl-Sys-Syslog` **
  - **RPM:**  perl-Sys-Syslog
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.33-3.amzn2.0.2
  - **AL2023.12 version:** 0.36-459.amzn2023.0.3

- ** `perl-Taint-Runtime` **
  - **RPM:**  perl-Taint-Runtime
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.03-19.amzn2.0.2
  - **AL2023.12 version:** 0.03-41.amzn2023.0.3

- ** `perl-Task-Weaken` **
  - **RPM:**  perl-Task-Weaken
  - **Architectures:** noarch
  - **AL2 version:** 1.04-6.amzn2
  - **AL2023.12 version:** 1.06-10.amzn2023.0.2

- ** `perl-Template-Toolkit` **
  - **RPM:**  perl-Template-Toolkit
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.24-5.amzn2.0.3
  - **AL2023.12 version:** 3.009-3.amzn2023.0.4

- ** `perl-TermReadKey` **
  - **RPM:**  perl-TermReadKey
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.30-20.amzn2.0.2
  - **AL2023.12 version:** 2.38-9.amzn2023.0.3

- ** `perl-Term-UI` **
  - **RPM:**  perl-Term-UI
  - **Architectures:** noarch
  - **AL2 version:** 0.36-2.amzn2
  - **AL2023.12 version:** 0.46-18.amzn2023.0.2

- ** `perl-Test-CPAN-Meta` **
  - **RPM:**  perl-Test-CPAN-Meta
  - **Architectures:** noarch
  - **AL2 version:** 0.23-2.amzn2
  - **AL2023.12 version:** 0.25-25.amzn2023.0.2

- ** `perl-Test-Deep` **
  - **RPM:**  perl-Test-Deep
  - **Architectures:** noarch
  - **AL2 version:** 0.110-2.amzn2
  - **AL2023.12 version:** 1.205-3.amzn2023.0.1

- ** `perl-Test-Differences` **
  - **RPM:**  perl-Test-Differences
  - **Architectures:** noarch
  - **AL2 version:** 0.5000-10.amzn2
  - **AL2023.12 version:** 0.6700-7.amzn2023.0.2

- ** `perl-Test-DistManifest` **
  - **RPM:**  perl-Test-DistManifest
  - **Architectures:** noarch
  - **AL2 version:** 1.012-6.amzn2
  - **AL2023.12 version:** 1.014-19.amzn2023.0.2

- ** `perl-Test-EOL` **
  - **RPM:**  perl-Test-EOL
  - **Architectures:** noarch
  - **AL2 version:** 1.3-7.amzn2
  - **AL2023.12 version:** 2.02-2.amzn2023.0.2

- ** `perl-Test-Exception` **
  - **RPM:**  perl-Test-Exception
  - **Architectures:** noarch
  - **AL2 version:** 0.32-2.amzn2
  - **AL2023.12 version:** 0.43-16.amzn2023.0.2

- ** `perl-Test-Fatal` **
  - **RPM:**  perl-Test-Fatal
  - **Architectures:** noarch
  - **AL2 version:** 0.010-5.amzn2
  - **AL2023.12 version:** 0.016-2.amzn2023.0.2

- ** `perl-Test-Harness` **
  - **RPM:**  perl-Test-Harness
  - **Architectures:** noarch
  - **AL2 version:** 3.28-3.amzn2
  - **AL2023.12 version:** 3.42-459.amzn2023.0.2

- ** `perl-Test-HasVersion` **
  - **RPM:**  perl-Test-HasVersion
  - **Architectures:** noarch
  - **AL2 version:** 0.012-7.amzn2
  - **AL2023.12 version:** 0.014-16.amzn2023.0.2

- ** `perl-Test-Inter` **
  - **RPM:**  perl-Test-Inter
  - **Architectures:** noarch
  - **AL2 version:** 1.05-2.amzn2
  - **AL2023.12 version:** 1.12-4.amzn2023.0.1

- ** `perl-Test-Manifest` **
  - **RPM:**  perl-Test-Manifest
  - **Architectures:** noarch
  - **AL2 version:** 1.23-2.amzn2
  - **AL2023.12 version:** 2.026-3.amzn2023.0.1

- ** `perl-Test-Memory-Cycle` **
  - **RPM:**  perl-Test-Memory-Cycle
  - **Architectures:** noarch
  - **AL2 version:** 1.04-17.amzn2
  - **AL2023.12 version:** 1.06-17.amzn2023.0.2

- ** `perl-Test-MinimumVersion` **
  - **RPM:**  perl-Test-MinimumVersion
  - **Architectures:** noarch
  - **AL2 version:** 0.101080-10.amzn2
  - **AL2023.12 version:** 0.101082-17.amzn2023.0.2

- ** `perl-Test-MockObject` **
  - **RPM:**  perl-Test-MockObject
  - **Architectures:** noarch
  - **AL2 version:** 1.20120301-3.amzn2
  - **AL2023.12 version:** 1.20200122-5.amzn2023.0.2

- ** `perl-Test-NoTabs` **
  - **RPM:**  perl-Test-NoTabs
  - **Architectures:** noarch
  - **AL2 version:** 1.3-5.amzn2
  - **AL2023.12 version:** 2.02-11.amzn2023.0.2

- ** `perl-Test-NoWarnings` **
  - **RPM:**  perl-Test-NoWarnings
  - **Architectures:** noarch
  - **AL2 version:** 1.04-2.amzn2
  - **AL2023.12 version:** 1.06-12.amzn2023.0.1

- ** `perl-Test-Object` **
  - **RPM:**  perl-Test-Object
  - **Architectures:** noarch
  - **AL2 version:** 0.07-17.amzn2
  - **AL2023.12 version:** 0.08-11.amzn2023.0.2

- ** `perl-Test-Output` **
  - **RPM:**  perl-Test-Output
  - **Architectures:** noarch
  - **AL2 version:** 1.01-7.amzn2
  - **AL2023.12 version:** 1.03.3-1.amzn2023.0.2

- ** `perl-Test-Perl-Critic` **
  - **RPM:**  perl-Test-Perl-Critic
  - **Architectures:** noarch
  - **AL2 version:** 1.02-10.amzn2
  - **AL2023.12 version:** 1.04-11.amzn2023.0.2

- ** `perl-Test-Pod` **
  - **RPM:**  perl-Test-Pod
  - **Architectures:** noarch
  - **AL2 version:** 1.48-3.amzn2
  - **AL2023.12 version:** 1.52-10.amzn2023.0.2

- ** `perl-Test-Pod-Coverage` **
  - **RPM:**  perl-Test-Pod-Coverage
  - **Architectures:** noarch
  - **AL2 version:** 1.08-21.amzn2
  - **AL2023.12 version:** 1.10-19.amzn2023.0.2

- ** `perl-Test-Portability-Files` **
  - **RPM:**  perl-Test-Portability-Files
  - **Architectures:** noarch
  - **AL2 version:** 0.05-18.amzn2
  - **AL2023.12 version:** 0.10-9.amzn2023.0.2

- ** `perl-Test-Requires` **
  - **RPM:**  perl-Test-Requires
  - **Architectures:** noarch
  - **AL2 version:** 0.06-10.amzn2
  - **AL2023.12 version:** 0.11-4.amzn2023.0.2

- ** `perl-Test-Script` **
  - **RPM:**  perl-Test-Script
  - **Architectures:** noarch
  - **AL2 version:** 1.07-12.amzn2
  - **AL2023.12 version:** 1.29-1.amzn2023.0.2

- ** `perl-Test-Simple` **
  - **RPM:**  perl-Test-Simple
  - **Architectures:** noarch
  - **AL2 version:** 0.98-243.amzn2.0.2
  - **AL2023.12 version:** 1.302219-2.amzn2023.0.1

- ** `perl-Test-Spelling` **
  - **RPM:**  perl-Test-Spelling
  - **Architectures:** noarch
  - **AL2 version:** 0.19-2.amzn2
  - **AL2023.12 version:** 0.25-7.amzn2023.0.2

- ** `perl-Test-SubCalls` **
  - **RPM:**  perl-Test-SubCalls
  - **Architectures:** noarch
  - **AL2 version:** 1.09-14.amzn2
  - **AL2023.12 version:** 1.10-11.amzn2023.0.2

- ** `perl-Test-Synopsis` **
  - **RPM:**  perl-Test-Synopsis
  - **Architectures:** noarch
  - **AL2 version:** 0.06-16.amzn2
  - **AL2023.12 version:** 0.16-10.amzn2023.0.2

- ** `perl-Test-Taint` **
  - **RPM:**  perl-Test-Taint
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.06-5.amzn2.0.2
  - **AL2023.12 version:** 1.08-6.amzn2023.0.3

- ** `perl-Test-Vars` **
  - **RPM:**  perl-Test-Vars
  - **Architectures:** noarch
  - **AL2 version:** 0.005-3.amzn2
  - **AL2023.12 version:** 0.014-18.amzn2023.0.2

- ** `perl-Test-Warn` **
  - **RPM:**  perl-Test-Warn
  - **Architectures:** noarch
  - **AL2 version:** 0.24-6.amzn2
  - **AL2023.12 version:** 0.36-11.amzn2023.0.2

- ** `perl-Test-Without-Module` **
  - **RPM:**  perl-Test-Without-Module
  - **Architectures:** noarch
  - **AL2 version:** 0.17-12.amzn2
  - **AL2023.12 version:** 0.20-14.amzn2023.0.2

- ** `perl-Text-CharWidth` **
  - **RPM:**  perl-Text-CharWidth
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.04-18.amzn2.0.2
  - **AL2023.12 version:** 0.04-42.amzn2023.0.3

- ** `perl-Text-CSV_XS` **
  - **RPM:**  perl-Text-CSV\_XS
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.00-3.amzn2.0.2
  - **AL2023.12 version:** 1.62-1.amzn2023.0.2

- ** `perl-Text-Diff` **
  - **RPM:**  perl-Text-Diff
  - **Architectures:** noarch
  - **AL2 version:** 1.41-5.amzn2
  - **AL2023.12 version:** 1.45-11.amzn2023.0.2

- ** `perl-Text-Glob` **
  - **RPM:**  perl-Text-Glob
  - **Architectures:** noarch
  - **AL2 version:** 0.09-7.amzn2
  - **AL2023.12 version:** 0.11-13.amzn2023.0.2

- ** `perl-Text-Iconv` **
  - **RPM:**  perl-Text-Iconv
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7-18.amzn2.0.2
  - **AL2023.12 version:** 1.7-41.amzn2023.0.3

- ** `perl-Text-ParseWords` **
  - **RPM:**  perl-Text-ParseWords
  - **Architectures:** noarch
  - **AL2 version:** 3.29-4.amzn2
  - **AL2023.12 version:** 3.30-458.amzn2023.0.2

- ** `perl-Text-Soundex` **
  - **RPM:**  perl-Text-Soundex
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.04-4.amzn2.0.2
  - **AL2023.12 version:** 3.05-18.amzn2023.0.3

- ** `perl-Text-Unidecode` **
  - **RPM:**  perl-Text-Unidecode
  - **Architectures:** noarch
  - **AL2 version:** 0.04-20.amzn2
  - **AL2023.12 version:** 1.30-14.amzn2023.0.2

- ** `perl-Text-WrapI18N` **
  - **RPM:**  perl-Text-WrapI18N
  - **Architectures:** noarch
  - **AL2 version:** 0.06-17.amzn2
  - **AL2023.12 version:** 0.06-39.amzn2023.0.2

- ** `perl-Thread-Queue` **
  - **RPM:**  perl-Thread-Queue
  - **Architectures:** noarch
  - **AL2 version:** 3.02-2.amzn2
  - **AL2023.12 version:** 3.14-458.amzn2023.0.2

- ** `perl-threads` **
  - **RPM:**  perl-threads
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.87-4.amzn2.0.2
  - **AL2023.12 version:** 2.25-458.amzn2023.0.4

- ** `perl-threads-shared` **
  - **RPM:**  perl-threads-shared
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.43-6.amzn2.0.2
  - **AL2023.12 version:** 1.61-458.amzn2023.0.3

- ** `perltidy` **
  - **RPM:**  perltidy
  - **Architectures:** noarch
  - **AL2 version:** 20121207-3.amzn2
  - **AL2023.12 version:** 20210402-1.amzn2023.0.3

- ** `perl-Tie-IxHash` **
  - **RPM:**  perl-Tie-IxHash
  - **Architectures:** noarch
  - **AL2 version:** 1.22-11.amzn2
  - **AL2023.12 version:** 1.23-26.amzn2023.0.2

- ** `perl-TimeDate` **
  - **RPM:**  perl-TimeDate
  - **Architectures:** noarch
  - **AL2 version:** 2.30-2.amzn2
  - **AL2023.12 version:** 2.33-4.amzn2023.0.2

- ** `perl-Time-HiRes` **
  - **RPM:**  perl-Time-HiRes
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9725-3.amzn2.0.2
  - **AL2023.12 version:** 1.9764-460.amzn2023.0.3

- ** `perl-Time-Local` **
  - **RPM:**  perl-Time-Local
  - **Architectures:** noarch
  - **AL2 version:** 1.2300-2.amzn2
  - **AL2023.12 version:** 1.300-5.amzn2023.0.2

- ** `perl-Tk` **
  - **RPM:**  perl-Tk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Tk-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 804.030-6.amzn2.0.2
  - **AL2023.12 version:** 804.036-3.amzn2023.0.3

- ** `perl-Try-Tiny` **
  - **RPM:**  perl-Try-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 0.12-2.amzn2
  - **AL2023.12 version:** 0.30-11.amzn2023.0.2

- ** `perl-Types-Serialiser` **
  - **RPM:**  perl-Types-Serialiser
  - **Architectures:** noarch
  - **AL2 version:** 1.0-1.amzn2
  - **AL2023.12 version:** 1.01-2.amzn2023.0.2

- ** `perl-Unicode-Map8` **
  - **RPM:**  perl-Unicode-Map8
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.13-13.amzn2.0.2
  - **AL2023.12 version:** 0.13-37.amzn2023.0.3

- ** `perl-Unicode-String` **
  - **RPM:**  perl-Unicode-String
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.09-29.amzn2.0.2
  - **AL2023.12 version:** 2.10-16.amzn2023.0.3

- ** `perl-UNIVERSAL-can` **
  - **RPM:**  perl-UNIVERSAL-can
  - **Architectures:** noarch
  - **AL2 version:** 1.20120726-3.amzn2
  - **AL2023.12 version:** 1.20140328-19.amzn2023.0.2

- ** `perl-UNIVERSAL-isa` **
  - **RPM:**  perl-UNIVERSAL-isa
  - **Architectures:** noarch
  - **AL2 version:** 1.20120726-3.amzn2
  - **AL2023.12 version:** 1.20171012-11.amzn2023.0.2

- ** `perl-URI` **
  - **RPM:**  perl-URI
  - **Architectures:** noarch
  - **AL2 version:** 1.60-9.amzn2
  - **AL2023.12 version:** 5.18-1.amzn2023.0.1

- ** `perl-version` **
  - **RPM:**  perl-version
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.99.07-3.amzn2
  - **AL2023.12 version:** 0.99.29-1.amzn2023.0.3

- ** `perl-WWW-RobotRules` **
  - **RPM:**  perl-WWW-RobotRules
  - **Architectures:** noarch
  - **AL2 version:** 6.02-5.amzn2
  - **AL2023.12 version:** 6.02-28.amzn2023.0.2

- ** `perl-XML-Catalog` **
  - **RPM:**  perl-XML-Catalog
  - **Architectures:** noarch
  - **AL2 version:** 1.0.1-1.amzn2
  - **AL2023.12 version:** 1.03-20.amzn2023.0.2

- ** `perl-XML-DOM` **
  - **RPM:**  perl-XML-DOM
  - **Architectures:** noarch
  - **AL2 version:** 1.44-19.amzn2
  - **AL2023.12 version:** 1.46-14.amzn2023.0.2

- ** `perl-XML-Dumper` **
  - **RPM:**  perl-XML-Dumper
  - **Architectures:** noarch
  - **AL2 version:** 0.81-17.amzn2
  - **AL2023.12 version:** 0.81-39.amzn2023.0.2

- ** `perl-XML-Filter-BufferText` **
  - **RPM:**  perl-XML-Filter-BufferText
  - **Architectures:** noarch
  - **AL2 version:** 1.01-17.amzn2
  - **AL2023.12 version:** 1.01-38.amzn2023.0.2

- ** `perl-XML-Handler-YAWriter` **
  - **RPM:**  perl-XML-Handler-YAWriter
  - **Architectures:** noarch
  - **AL2 version:** 0.23-18.amzn2
  - **AL2023.12 version:** 0.23-39.amzn2023.0.2

- ** `perl-XML-LibXML` **
  - **RPM:**  perl-XML-LibXML
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0018-5.amzn2.0.3
  - **AL2023.12 version:** 2.0210-7.amzn2023.0.3

- ** `perl-XML-LibXSLT` **
  - **RPM:**  perl-XML-LibXSLT
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.80-4.amzn2.0.2
  - **AL2023.12 version:** 1.99-5.amzn2023.0.3

- ** `perl-XML-NamespaceSupport` **
  - **RPM:**  perl-XML-NamespaceSupport
  - **Architectures:** noarch
  - **AL2 version:** 1.11-10.amzn2
  - **AL2023.12 version:** 1.12-13.amzn2023.0.2

- ** `perl-XML-Parser` **
  - **RPM:**  perl-XML-Parser
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.41-10.amzn2.0.3
  - **AL2023.12 version:** 2.51-1.amzn2023.0.2

- ** `perl-XML-RegExp` **
  - **RPM:**  perl-XML-RegExp
  - **Architectures:** noarch
  - **AL2 version:** 0.04-2.amzn2
  - **AL2023.12 version:** 0.04-23.amzn2023.0.2

- ** `perl-XML-SAX` **
  - **RPM:**  perl-XML-SAX
  - **Architectures:** noarch
  - **AL2 version:** 0.99-9.amzn2
  - **AL2023.12 version:** 1.02-6.amzn2023.0.2

- ** `perl-XML-SAX-Base` **
  - **RPM:**  perl-XML-SAX-Base
  - **Architectures:** noarch
  - **AL2 version:** 1.08-7.amzn2
  - **AL2023.12 version:** 1.09-13.amzn2023.0.2

- ** `perl-XML-SAX-Writer` **
  - **RPM:**  perl-XML-SAX-Writer
  - **Architectures:** noarch
  - **AL2 version:** 0.53-4.amzn2
  - **AL2023.12 version:** 0.57-11.amzn2023.0.2

- ** `perl-XML-Simple` **
  - **RPM:**  perl-XML-Simple
  - **Architectures:** noarch
  - **AL2 version:** 2.20-5.amzn2
  - **AL2023.12 version:** 2.25-10.amzn2023.0.2

- ** `perl-XML-TokeParser` **
  - **RPM:**  perl-XML-TokeParser
  - **Architectures:** noarch
  - **AL2 version:** 0.05-12.amzn2
  - **AL2023.12 version:** 0.05-34.amzn2023.0.2

- ** `perl-XML-TreeBuilder` **
  - **RPM:**  perl-XML-TreeBuilder
  - **Architectures:** noarch
  - **AL2 version:** 4.2-1.amzn2
  - **AL2023.12 version:** 5.4-20.amzn2023.0.2

- ** `perl-XML-Twig` **
  - **RPM:**  perl-XML-Twig
  - **Architectures:** noarch
  - **AL2 version:** 3.44-2.amzn2
  - **AL2023.12 version:** 3.52-16.amzn2023.0.2

- ** `perl-XML-Writer` **
  - **RPM:**  perl-XML-Writer
  - **Architectures:** noarch
  - **AL2 version:** 0.623-3.amzn2
  - **AL2023.12 version:** 0.900-3.amzn2023.0.2

- ** `perl-XML-XPath` **
  - **RPM:**  perl-XML-XPath
  - **Architectures:** noarch
  - **AL2 version:** 1.13-22.amzn2
  - **AL2023.12 version:** 1.44-9.amzn2023.0.2

- ** `perl-XML-XPathEngine` **
  - **RPM:**  perl-XML-XPathEngine
  - **Architectures:** noarch
  - **AL2 version:** 0.14-3.amzn2
  - **AL2023.12 version:** 0.14-21.amzn2023.0.2

- ** `perl-YAML` **
  - **RPM:**  perl-YAML
  - **Architectures:** noarch
  - **AL2 version:** 0.84-5.amzn2
  - **AL2023.12 version:** 1.31-7.amzn2023.0.1

- ** `perl-YAML-Syck` **
  - **RPM:**  perl-YAML-Syck
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.27-3.amzn2.0.6
  - **AL2023.12 version:** 1.37-1.amzn2023.0.4

- ** `perl-YAML-Tiny` **
  - **RPM:**  perl-YAML-Tiny
  - **Architectures:** noarch
  - **AL2 version:** 1.51-6.amzn2
  - **AL2023.12 version:** 1.73-11.amzn2023.0.3

- ** `pesign` **
  - **RPM:**  pesign
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.109-10.amzn2.0.1
  - **AL2023.12 version:** 116-2.amzn2023.0.2

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.4.16-46.amzn2.0.7
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

- ** `pigz` **
  - **RPM:**  pigz
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.4-1.amzn2.0.1
  - **AL2023.12 version:** 2.5-1.amzn2023.0.4

- ** `pinentry` **
  - **RPM:**  pinentry
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.1-17.amzn2.0.2
  - **AL2023.12 version:** 1.3.1-2.amzn2023.0.1

- ** `pixman` **
  - **RPM:**  pixman  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pixman-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.34.0-1.amzn2.0.3
  - **AL2023.12 version:** 0.43.4-1.amzn2023.0.4

- ** `plexus-archiver` **
  - **RPM:**  plexus-archiver  / **Architectures:** noarch
  - **RPM:**  plexus-archiver-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4.2-5.amzn2
  - **AL2023.12 version:** 4.2.7-4.amzn2023.0.1

- ** `plexus-build-api` **
  - **RPM:**  plexus-build-api  / **Architectures:** noarch
  - **RPM:**  plexus-build-api-javadoc  / **Architectures:** noarch
  - **AL2 version:** 0.0.7-11.amzn2
  - **AL2023.12 version:** 0.0.7-36.amzn2023.0.3

- ** `plexus-cipher` **
  - **RPM:**  plexus-cipher  / **Architectures:** noarch
  - **RPM:**  plexus-cipher-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.7-5.amzn2
  - **AL2023.12 version:** 1.8-3.amzn2023.0.3

- ** `plexus-classworlds` **
  - **RPM:**  plexus-classworlds  / **Architectures:** noarch
  - **RPM:**  plexus-classworlds-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.4.2-8.amzn2
  - **AL2023.12 version:** 2.6.0-10.amzn2023.0.4

- ** `plexus-compiler` **
  - **RPM:**  plexus-compiler  / **Architectures:** noarch
  - **RPM:**  plexus-compiler-extras  / **Architectures:** noarch
  - **RPM:**  plexus-compiler-javadoc  / **Architectures:** noarch
  - **RPM:**  plexus-compiler-pom  / **Architectures:** noarch
  - **AL2 version:** 2.2-7.amzn2
  - **AL2023.12 version:** 2.8.8-5.amzn2023.0.3

- ** `plexus-component-api` **
  - **RPM:**  plexus-component-api  / **Architectures:** noarch
  - **RPM:**  plexus-component-api-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-0.16.alpha15.amzn2
  - **AL2023.12 version:** 1.0-0.34.alpha15.amzn2023.0.3

- ** `plexus-components-pom` **
  - **RPM:**  plexus-components-pom
  - **Architectures:** noarch
  - **AL2 version:** 1.2-7.amzn2
  - **AL2023.12 version:** 6.5-6.amzn2023.0.3

- ** `plexus-containers` **
  - **RPM:**  plexus-containers  / **Architectures:** noarch
  - **RPM:**  plexus-containers-component-annotations  / **Architectures:** noarch
  - **RPM:**  plexus-containers-component-metadata  / **Architectures:** noarch
  - **RPM:**  plexus-containers-container-default  / **Architectures:** noarch
  - **RPM:**  plexus-containers-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.5.5-14.amzn2
  - **AL2023.12 version:** 2.1.0-9.amzn2023.0.4

- ** `plexus-i18n` **
  - **RPM:**  plexus-i18n  / **Architectures:** noarch
  - **RPM:**  plexus-i18n-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-0.6.b10.4.amzn2
  - **AL2023.12 version:** 1.0-0.19.b10.4.amzn2023.0.3

- ** `plexus-interpolation` **
  - **RPM:**  plexus-interpolation  / **Architectures:** noarch
  - **RPM:**  plexus-interpolation-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.15-8.amzn2
  - **AL2023.12 version:** 1.26-10.amzn2023.0.4

- ** `plexus-io` **
  - **RPM:**  plexus-io  / **Architectures:** noarch
  - **RPM:**  plexus-io-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.0.5-9.amzn2
  - **AL2023.12 version:** 3.2.0-9.amzn2023.0.3

- ** `plexus-pom` **
  - **RPM:**  plexus-pom
  - **Architectures:** noarch
  - **AL2 version:** 3.3.1-5.amzn2
  - **AL2023.12 version:** 7-5.amzn2023.0.3

- ** `plexus-resources` **
  - **RPM:**  plexus-resources  / **Architectures:** noarch
  - **RPM:**  plexus-resources-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.0-0.15.a7.amzn2
  - **AL2023.12 version:** 1.1.0-9.amzn2023.0.3

- ** `plexus-sec-dispatcher` **
  - **RPM:**  plexus-sec-dispatcher  / **Architectures:** noarch
  - **RPM:**  plexus-sec-dispatcher-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-13.amzn2
  - **AL2023.12 version:** 2.0-3.amzn2023.0.3

- ** `plexus-utils` **
  - **RPM:**  plexus-utils  / **Architectures:** noarch
  - **RPM:**  plexus-utils-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.0.9-9.amzn2.0.1
  - **AL2023.12 version:** 3.3.0-9.amzn2023.0.5

- ** `plexus-velocity` **
  - **RPM:**  plexus-velocity  / **Architectures:** noarch
  - **RPM:**  plexus-velocity-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.1.8-16.amzn2
  - **AL2023.12 version:** 1.2-15.amzn2023.0.2

- ** `plymouth` **
  - **RPM:**  plymouth  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-core-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-graphics-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-fade-throbber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-label  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-script  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-space-flares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-two-step  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-scripts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-system-theme  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-fade-in  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-script  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-solar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-spinfinity  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-spinner  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.9-0.28.20140113.amzn2.0.2
  - **AL2023.12 version:** 24.004.60-330.amzn2023

- ** `po4a` **
  - **RPM:**  po4a
  - **Architectures:** noarch
  - **AL2 version:** 0.44-10.amzn2
  - **AL2023.12 version:** 0.64-1.amzn2023.0.2

- ** `policycoreutils` **
  - **RPM:**  policycoreutils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  policycoreutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  policycoreutils-newrole  / **Architectures:** aarch64, x86\_64
  - **RPM:**  policycoreutils-restorecond  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5-22.amzn2
  - **AL2023.12 version:** 3.4-6.amzn2023.0.3

- ** `polkit` **
  - **RPM:**  polkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-docs  / **Architectures:** noarch
  - **AL2 version:** 0.112-26.amzn2.2.1
  - **AL2023.12 version:** 125-1.amzn2023.0.3

- ** `polkit-pkla-compat` **
  - **RPM:**  polkit-pkla-compat
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.1-4.amzn2.0.2
  - **AL2023.12 version:** 0.1-19.amzn2023.0.2

- ** `poppler` **
  - **RPM:**  poppler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-cpp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-glib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  poppler-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.26.5-43.amzn2.1.7
  - **AL2023.12 version:** 24.08.0-1.amzn2023.0.1

- ** `poppler-data` **
  - **RPM:**  poppler-data
  - **Architectures:** noarch
  - **AL2 version:** 0.4.6-3.amzn2.0.1
  - **AL2023.12 version:** 0.4.9-7.amzn2023.0.2

- ** `popt` **
  - **RPM:**  popt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  popt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  popt-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.13-16.amzn2.0.2
  - **AL2023.12 version:** 1.18-6.amzn2023.0.2

- ** `postfix` **
  - **RPM:**  postfix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postfix-perl-scripts  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.10.1-6.amzn2.0.4
  - **AL2023.12 version:** 3.7.2-4.amzn2023.0.6

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.2.24-8.amzn2.0.10
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

- ** `pps-tools` **
  - **RPM:**  pps-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pps-tools-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0-0.9.20120407git0deb9c.amzn2.0.2
  - **AL2023.12 version:** 1.0.2-7.amzn2023.0.2

- ** `procmail` **
  - **RPM:**  procmail
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.22-36.amzn2.1.2
  - **AL2023.12 version:** 3.24-1.amzn2023.0.2

- ** `procps-ng` **
  - **RPM:**  procps-ng  / **Architectures:** aarch64, x86\_64
  - **RPM:**  procps-ng-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.10-26.amzn2
  - **AL2023.12 version:** 3.3.17-1.amzn2023.0.2

- ** `protobuf` **
  - **RPM:**  protobuf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-compiler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-lite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-lite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-lite-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.0-8.amzn2.0.5
  - **AL2023.12 version:** 3.19.6-1.amzn2023.0.3

- ** `protobuf-c` **
  - **RPM:**  protobuf-c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-c-compiler  / **Architectures:** aarch64, x86\_64
  - **RPM:**  protobuf-c-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-3.amzn2.0.3
  - **AL2023.12 version:** 1.5.0-4.amzn2023.0.1

- ** `psacct` **
  - **RPM:**  psacct
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.6.1-13.amzn2.0.2
  - **AL2023.12 version:** 6.6.4-9.amzn2023.0.2

- ** `psmisc` **
  - **RPM:**  psmisc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 22.20-15.amzn2.0.2
  - **AL2023.12 version:** 23.4-1.amzn2023.0.2

- ** `publicsuffix-list` **
  - **RPM:**  publicsuffix-list  / **Architectures:** noarch
  - **RPM:**  publicsuffix-list-dafsa  / **Architectures:** noarch
  - **AL2 version:** 20240208-1.amzn2.0.1
  - **AL2023.12 version:** 20260116-1.amzn2023.0.1

- ** `pulseaudio` **
  - **RPM:**  pulseaudio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-libs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-libs-glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-module-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-module-zeroconf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pulseaudio-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 10.0-3.amzn2.0.3
  - **AL2023.12 version:** 15.0-5.amzn2023.0.4

- ** `pyOpenSSL` **
  - **RPM:**  pyOpenSSL-doc
  - **Architectures:** noarch
  - **AL2 version:** 0.13.1-3.amzn2.0.2
  - **AL2023.12 version:** 21.0.0-1.amzn2023.0.2

- ** `pyparsing` **
  - **RPM:**  pyparsing-doc
  - **Architectures:** noarch
  - **AL2 version:** 1.5.6-9.amzn2
  - **AL2023.12 version:** 2.4.7-6.amzn2023.0.2

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) (`python3` in AL2) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.7.16-1.amzn2.0.29
  - **AL2023.12 version:** 3.9.25-1.amzn2023.0.9

- ** `python-boto3` **
  - **RPM:**  python3-boto3
  - **Architectures:** noarch
  - **AL2 version:** 1.21.33-1.amzn2.0.1
  - **AL2023.12 version:** 1.40.31-1.amzn2023.0.1

- ** `python-bottle` **
  - **RPM:**  python3-bottle
  - **Architectures:** noarch
  - **AL2 version:** 0.12.21-2.amzn2
  - **AL2023.12 version:** 0.12.21-2.amzn2023.0.1

- ** `python-cffi` **
  - **RPM:**  python-cffi-doc
  - **Architectures:** noarch
  - **AL2 version:** 1.6.0-5.amzn2.0.2
  - **AL2023.12 version:** 1.14.5-1.amzn2023.0.3

- ** `python-chardet` (`python3-chardet` in AL2) **
  - **RPM:**  python3-chardet
  - **Architectures:** noarch
  - **AL2 version:** 3.0.4-1.amzn2.0.2
  - **AL2023.12 version:** 4.0.0-1.amzn2023.0.2

- ** `python-chevron` **
  - **RPM:**  python-chevron
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.13.1-1.amzn2.0.2
  - **AL2023.12 version:** 0.13.1-1.amzn2023.0.3

- ** `python-colorama` **
  - **RPM:**  python3-colorama
  - **Architectures:** noarch
  - **AL2 version:** 0.3.9-3.amzn2.0.1
  - **AL2023.12 version:** 0.4.4-2.amzn2023.0.2

- ** `python-coverage` **
  - **RPM:**  python3-coverage
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.5-1.amzn2.0.1
  - **AL2023.12 version:** 5.5-1.amzn2023.0.3

- ** `python-cups` **
  - **RPM:**  python-cups-doc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.63-6.amzn2.0.2
  - **AL2023.12 version:** 2.0.1-10.amzn2023.0.2

- ** `python-daemon` (`python3-daemon` in AL2) **
  - **RPM:**  python3-daemon
  - **Architectures:** noarch
  - **AL2 version:** 2.2.3-8.amzn2.0.2
  - **AL2023.12 version:** 2.3.0-4.amzn2023.0.2

- ** `python-dateutil` **
  - **RPM:**  python3-dateutil  / **Architectures:** noarch
  - **RPM:**  python-dateutil-doc  / **Architectures:** noarch
  - **AL2 version:** 2.6.1-3.amzn2
  - **AL2023.12 version:** 2.8.1-3.amzn2023.0.2

- ** `python-docutils` (`python3-docutils` in AL2) **
  - **RPM:**  python3-docutils
  - **Architectures:** noarch
  - **AL2 version:** 0.14-1.amzn2.0.2
  - **AL2023.12 version:** 0.16-4.amzn2023.0.2

- ** `python-extras` **
  - **RPM:**  python3-extras
  - **Architectures:** noarch
  - **AL2 version:** 1.0.0-11.amzn2.0.3
  - **AL2023.12 version:** 1.0.0-15.amzn2023.0.2

- ** `python-fixtures` **
  - **RPM:**  python3-fixtures
  - **Architectures:** noarch
  - **AL2 version:** 3.0.0-17.amzn2
  - **AL2023.12 version:** 3.0.0-22.amzn2023.0.2

- ** `python-idna` (`python3-idna` in AL2) **
  - **RPM:**  python3-idna
  - **Architectures:** noarch
  - **AL2 version:** 2.7-2.amzn2.0.3
  - **AL2023.12 version:** 2.10-3.amzn2023.0.4

- ** `python-jinja2` (`python3-jinja2` in AL2) **
  - **RPM:**  python3-jinja2
  - **Architectures:** noarch
  - **AL2 version:** 2.7.2-4.amzn2.0.7
  - **AL2023.12 version:** 2.11.3-1.amzn2023.0.6

- ** `python-jmespath` **
  - **RPM:**  python3-jmespath
  - **Architectures:** noarch
  - **AL2 version:** 0.9.3-1.amzn2.0.2
  - **AL2023.12 version:** 0.10.0-1.amzn2023.0.3

- ** `python-jsonschema` **
  - **RPM:**  python3-jsonschema
  - **Architectures:** noarch
  - **AL2 version:** 2.5.1-3.amzn2.0.2
  - **AL2023.12 version:** 3.2.0-9.amzn2023.0.3

- ** `python-lit` **
  - **RPM:**  python3-lit
  - **Architectures:** noarch
  - **AL2 version:** 0.11.1-1.amzn2.0.1
  - **AL2023.12 version:** 18.1.8-1.amzn2023.0.1

- ** `python-lockfile` **
  - **RPM:**  python3-lockfile  / **Architectures:** noarch
  - **RPM:**  python-lockfile-doc  / **Architectures:** noarch
  - **AL2 version:** 0.11.0-17.amzn2.0.2
  - **AL2023.12 version:** 0.12.2-5.amzn2023.0.3

- ** `python-lxml` **
  - **RPM:**  python3-lxml
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2.1-4.amzn2.0.8
  - **AL2023.12 version:** 4.7.1-3.amzn2023.0.3

- ** `python-markupsafe` (`python3-markupsafe` in AL2) **
  - **RPM:**  python3-markupsafe
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.11-10.amzn2.0.2
  - **AL2023.12 version:** 1.1.1-10.amzn2023.0.2

- ** `python-mimeparse` **
  - **RPM:**  python3-mimeparse
  - **Architectures:** noarch
  - **AL2 version:** 1.6.0-12.amzn2.0.3
  - **AL2023.12 version:** 1.6.0-16.amzn2023.0.2

- ** `python-mock` (`python3-mock` in AL2) **
  - **RPM:**  python3-mock
  - **Architectures:** noarch
  - **AL2 version:** 3.0.5-8.amzn2.0.3
  - **AL2023.12 version:** 3.0.5-14.amzn2023.0.2

- ** `python-netaddr` (`python3-netaddr` in AL2) **
  - **RPM:**  python3-netaddr
  - **Architectures:** noarch
  - **AL2 version:** 0.7.18-3.amzn2.0.2
  - **AL2023.12 version:** 0.8.0-3.amzn2023.0.2

- ** `python-pbr` (`python3-pbr` in AL2) **
  - **RPM:**  python3-pbr
  - **Architectures:** noarch
  - **AL2 version:** 5.4.3-3.amzn2.0.2
  - **AL2023.12 version:** 5.5.1-2.amzn2023.0.2

- ** `python-pip` **
  - **RPM:**  python3-pip
  - **Architectures:** noarch
  - **AL2 version:** 20.2.2-1.amzn2.0.18
  - **AL2023.12 version:** 21.3.1-2.amzn2023.0.20

- ** `python-psutil` **
  - **RPM:**  python3-psutil
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.6.7-1.amzn2.0.2
  - **AL2023.12 version:** 5.8.0-16.amzn2023.0.2

- ** `python-psycopg2` **
  - **RPM:**  python-psycopg2-doc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.1-3.amzn2.0.2
  - **AL2023.12 version:** 2.9.10-8.amzn2023.0.1

- ** `python-py` (`python3-py` in AL2) **
  - **RPM:**  python3-py
  - **Architectures:** noarch
  - **AL2 version:** 1.4.32-2.amzn2.0.3
  - **AL2023.12 version:** 1.10.0-2.amzn2023.0.2

- ** `python-pyasn1` **
  - **RPM:**  python3-pyasn1  / **Architectures:** noarch
  - **RPM:**  python3-pyasn1-modules  / **Architectures:** noarch
  - **AL2 version:** 0.1.9-7.amzn2.0.5
  - **AL2023.12 version:** 0.4.8-4.amzn2023.0.5

- ** `python-pycurl` (`python3-pycurl` in AL2) **
  - **RPM:**  python3-pycurl
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.43.0-7.amzn2.0.2
  - **AL2023.12 version:** 7.45.7-1.amzn2023.0.1

- ** `python-pygments` (`python3-pygments` in AL2) **
  - **RPM:**  python3-pygments
  - **Architectures:** noarch
  - **AL2 version:** 2.2.0-3.amzn2.0.4
  - **AL2023.12 version:** 2.7.4-1.amzn2023.0.3

- ** `python-pysocks` **
  - **RPM:**  python3-pysocks
  - **Architectures:** noarch
  - **AL2 version:** 1.7.1-7.amzn2.0.2
  - **AL2023.12 version:** 1.7.1-8.amzn2023.0.2

- ** `python-requests` (`python3-requests` in AL2) **
  - **RPM:**  python3-requests
  - **Architectures:** noarch
  - **AL2 version:** 2.14.2-2.amzn2.0.5
  - **AL2023.12 version:** 2.25.1-1.amzn2023.0.6

- ** `python-rpm-generators` **
  - **RPM:**  python3-rpm-generators
  - **Architectures:** noarch
  - **AL2 version:** 10-4.amzn2.0.1
  - **AL2023.12 version:** 12-15.amzn2023.0.5

- ** `python-rpm-macros` **
  - **RPM:**  python-rpm-macros  / **Architectures:** noarch
  - **RPM:**  python-rpm-macros (python3-rpm-macros in AL2)  / **Architectures:** noarch
  - **RPM:**  python-srpm-macros  / **Architectures:** noarch
  - **AL2 version:** 3-60.amzn2.0.1
  - **AL2023.12 version:** 3.9-41.amzn2023.0.6

- ** `python-rsa` **
  - **RPM:**  python3-rsa
  - **Architectures:** noarch
  - **AL2 version:** 3.4.1-1.amzn2.0.4
  - **AL2023.12 version:** 4.7.2-1.amzn2023.0.2

- ** `python-setuptools` **
  - **RPM:**  python3-setuptools
  - **Architectures:** noarch
  - **AL2 version:** 49.1.3-1.amzn2.0.6
  - **AL2023.12 version:** 59.6.0-2.amzn2023.0.6

- ** `python-simplejson` (`python3-simplejson` in AL2) **
  - **RPM:**  python3-simplejson
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2.0-1.amzn2.0.2
  - **AL2023.12 version:** 3.17.6-111.amzn2023.0.2

- ** `python-six` (`python3-six` in AL2) **
  - **RPM:**  python3-six
  - **Architectures:** noarch
  - **AL2 version:** 1.14.0-2.amzn2.0.3
  - **AL2023.12 version:** 1.15.0-5.amzn2023.0.2

- ** `python-sphinx` **
  - **RPM:**  python-sphinx-doc
  - **Architectures:** noarch
  - **AL2 version:** 1.1.3-11.amzn2
  - **AL2023.12 version:** 3.4.3-2.amzn2023.0.3

- ** `python-sphinx` (`python3-sphinx` in AL2) **
  - **RPM:**  python3-sphinx  / **Architectures:** noarch
  - **RPM:**  python-sphinx-doc (python3-sphinx-doc in AL2)  / **Architectures:**
  - **AL2 version:** 1.1.3-11.amzn2.0.2
  - **AL2023.12 version:** 3.4.3-2.amzn2023.0.3

- ** `python-sqlalchemy` (`python3-sqlalchemy` in AL2) **
  - **RPM:**  python3-sqlalchemy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-sqlalchemy-doc (python3-sqlalchemy-doc in AL2)  / **Architectures:** noarch
  - **AL2 version:** 1.1.3-3.amzn2.0.2
  - **AL2023.12 version:** 1.3.24-1.amzn2023.0.2

- ** `python-testscenarios` **
  - **RPM:**  python3-testscenarios
  - **Architectures:** noarch
  - **AL2 version:** 0.5.0-18.amzn2.0.2
  - **AL2023.12 version:** 0.5.0-21.amzn2023.0.2

- ** `python-testtools` **
  - **RPM:**  python3-testtools  / **Architectures:** noarch
  - **RPM:**  python-testtools-doc  / **Architectures:** noarch
  - **AL2 version:** 2.3.0-18.amzn2.0.3
  - **AL2023.12 version:** 2.4.0-8.amzn2023.0.2

- ** `python-tornado` **
  - **RPM:**  python-tornado-doc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.2.1-3.amzn2.0.6
  - **AL2023.12 version:** 6.1.0-2.amzn2023.0.9

- ** `python-tornado` (`python3-tornado` in AL2) **
  - **RPM:**  python3-tornado  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-tornado-doc (python3-tornado-doc in AL2)  / **Architectures:**
  - **AL2 version:** 5.0.2-4.amzn2.0.9
  - **AL2023.12 version:** 6.1.0-2.amzn2023.0.9

- ** `python-urllib3` (`python3-urllib3` in AL2) **
  - **RPM:**  python3-urllib3
  - **Architectures:** noarch
  - **AL2 version:** 1.25.6-2.amzn2.0.6
  - **AL2023.12 version:** 1.25.10-5.amzn2023.0.7

- ** `python-wheel` **
  - **RPM:**  python3-wheel
  - **Architectures:** noarch
  - **AL2 version:** 0.34.2-1.amzn2.0.2
  - **AL2023.12 version:** 0.37.1-1.amzn2023.0.3

- ** `qdox` **
  - **RPM:**  qdox  / **Architectures:** noarch
  - **RPM:**  qdox-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.12.1-10.amzn2
  - **AL2023.12 version:** 2.0.0-9.amzn2023.0.3

- ** `qemu` **
  - **RPM:**  qemu-img
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.0-8.amzn2.0.26
  - **AL2023.12 version:** 9.2.3-1082.amzn2023

- ** `qpdf` **
  - **RPM:**  qpdf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qpdf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qpdf-doc  / **Architectures:** noarch
  - **RPM:**  qpdf-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.0.1-4.amzn2.0.2
  - **AL2023.12 version:** 10.6.3-4.amzn2023.0.5

- ** `qrencode` **
  - **RPM:**  qrencode  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qrencode-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  qrencode-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.4.1-3.amzn2.0.2
  - **AL2023.12 version:** 4.1.1-2.amzn2023.0.2

- ** `quota` **
  - **RPM:**  quota  / **Architectures:** aarch64, x86\_64
  - **RPM:**  quota-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  quota-doc  / **Architectures:** noarch
  - **RPM:**  quota-nld  / **Architectures:** aarch64, x86\_64
  - **RPM:**  quota-nls  / **Architectures:** noarch
  - **RPM:**  quota-warnquota  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.01-17.amzn2
  - **AL2023.12 version:** 4.06-4.amzn2023.0.2

- ** `radvd` **
  - **RPM:**  radvd
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.9.2-9.amzn2.4
  - **AL2023.12 version:** 2.19-2.amzn2023.0.3

- ** `rclone` **
  - **RPM:**  rclone
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.55.1-1.amzn2.0.10
  - **AL2023.12 version:** 1.74.3-83.amzn2023

- ** `rdma-core` **
  - **RPM:**  ibacm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  infiniband-diags  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iwpmd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibumad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibverbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libibverbs-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librdmacm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  librdmacm-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rdma-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rdma-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  srp\_daemon  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 48.0-1.amzn2.0.3
  - **AL2023.12 version:** 48.0-1.amzn2023.0.1

- ** `re2c` **
  - **RPM:**  re2c
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1-2.amzn2.0.1
  - **AL2023.12 version:** 3.1-1.amzn2023.0.1

- ** `readline` **
  - **RPM:**  readline  / **Architectures:** aarch64, x86\_64
  - **RPM:**  readline-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  readline-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.2-10.amzn2.0.2
  - **AL2023.12 version:** 8.1-2.amzn2023.0.2

- ** `realmd` **
  - **RPM:**  realmd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  realmd-devel-docs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.16.1-9.amzn2.0.1
  - **AL2023.12 version:** 0.17.0-9.amzn2023.0.4

- ** `recode` **
  - **RPM:**  recode  / **Architectures:** aarch64, x86\_64
  - **RPM:**  recode-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.6-38.amzn2.0.1
  - **AL2023.12 version:** 3.7.8-2.amzn2023.0.2

- ** `regexp` **
  - **RPM:**  regexp  / **Architectures:** noarch
  - **RPM:**  regexp-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.5-13.amzn2
  - **AL2023.12 version:** 1.5-38.amzn2023.0.1

- ** `resource-agents` **
  - **RPM:**  resource-agents
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.9.5-124.amzn2
  - **AL2023.12 version:** 4.16.0-2.amzn2023.0.1

- ** `rest` **
  - **RPM:**  rest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rest-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.0-2.amzn2
  - **AL2023.12 version:** 0.9.1-11.amzn2023.0.1

- ** `rhash` **
  - **RPM:**  rhash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rhash-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.5-3.amzn2.0.2
  - **AL2023.12 version:** 1.4.0-3.amzn2023.0.2

- ** `rhino` **
  - **RPM:**  rhino  / **Architectures:** noarch
  - **RPM:**  rhino-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.7R5-1.amzn2
  - **AL2023.12 version:** 1.7.14.1-3.amzn2023.0.1

- ** `rng-tools` **
  - **RPM:**  rng-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.8-3.amzn2.0.5
  - **AL2023.12 version:** 6.17-1.amzn2023.0.1

- ** `rootfiles` **
  - **RPM:**  rootfiles
  - **Architectures:** noarch
  - **AL2 version:** 8.1-11.amzn2
  - **AL2023.12 version:** 8.1-29.amzn2023.0.2

- ** `rpcbind` **
  - **RPM:**  rpcbind
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.0-44.amzn2
  - **AL2023.12 version:** 1.2.6-0.amzn2023.0.2

- ** `rpm` **
  - **RPM:**  python3-rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-apidocs  / **Architectures:** noarch
  - **RPM:**  rpm-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-build-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-cron  / **Architectures:** noarch
  - **RPM:**  rpm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-systemd-inhibit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-sign  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.11.3-48.amzn2.0.5
  - **AL2023.12 version:** 4.16.1.3-29.amzn2023.0.7

- ** `rpmdevtools` **
  - **RPM:**  rpmdevtools
  - **Architectures:** noarch
  - **AL2 version:** 8.3-5.amzn2
  - **AL2023.12 version:** 9.6-1.amzn2023.0.3

- ** `rpmlint` **
  - **RPM:**  rpmlint
  - **Architectures:** noarch
  - **AL2 version:** 1.5-4.amzn2
  - **AL2023.12 version:** 1.11-19.amzn2023.0.2

- ** `rrdtool` **
  - **RPM:**  rrdtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rrdtool-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rrdtool-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rrdtool-lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rrdtool-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rrdtool-tcl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.8-9.amzn2.0.1
  - **AL2023.12 version:** 1.7.2-16.amzn2023.0.4

- ** `rsync` **
  - **RPM:**  rsync
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.2-11.amzn2.0.7
  - **AL2023.12 version:** 3.4.0-1.amzn2023.0.4

- ** `rsyslog` **
  - **RPM:**  rsyslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-crypto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-doc  / **Architectures:** noarch
  - **RPM:**  rsyslog-elasticsearch  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmaudit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmjsonparse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmkubernetes  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rsyslog-mmnormalize  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.24.0-57.amzn2.2.0.2
  - **AL2023.12 version:** 8.2204.0-3.amzn2023.0.4

- ** `rtkit` **
  - **RPM:**  rtkit
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.11-10.amzn2.0.1
  - **AL2023.12 version:** 0.11-26.amzn2023.0.2

- ** `ruby3.2` (`ruby` in AL2) **
  - **RPM:**  ruby3.2 (ruby in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-devel (ruby-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-doc (ruby-doc in AL2)  / **Architectures:** noarch
  - **RPM:**  ruby3.2-libs (ruby-libs in AL2)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.0.648-36.amzn2.0.20
  - **AL2023.12 version:** 3.2.8-184.amzn2023.0.6

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clippy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analysis  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-debugger-common  / **Architectures:** noarch
  - **RPM:**  rust-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rustfmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-gdb  / **Architectures:** noarch
  - **RPM:**  rust-src  / **Architectures:** noarch
  - **RPM:**  rust-std-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-toolset  / **Architectures:** noarch
  - **RPM:**  rust-toolset-srpm-macros  / **Architectures:** noarch
  - **AL2 version:** 1.97.0-2.amzn2
  - **AL2023.12 version:** 1.97.0-2.amzn2023

- ** `samba` **
  - **RPM:**  libsmbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsmbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwbclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-client-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common  / **Architectures:** noarch
  - **RPM:**  samba-common-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-common-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-dc-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-krb5-printing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-pidl  / **Architectures:** noarch
  - **RPM:**  samba-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-test-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-krb5-locator  / **Architectures:** aarch64, x86\_64
  - **RPM:**  samba-winbind-modules  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.10.16-24.amzn2.0.7
  - **AL2023.12 version:** 4.17.12-1.amzn2023.0.5

- ** `sanlock` **
  - **RPM:**  sanlock  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sanlock-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sanlock-lib  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.6.0-1.amzn2
  - **AL2023.12 version:** 3.8.4-1.amzn2023.0.2

- ** `satyr` **
  - **RPM:**  satyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  satyr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.13-14.amzn2.0.1
  - **AL2023.12 version:** 0.38-2.amzn2023.0.2

- ** `sbc` **
  - **RPM:**  sbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sbc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0-5.amzn2.0.1
  - **AL2023.12 version:** 1.4-7.amzn2023.0.2

- ** `sbsigntools` **
  - **RPM:**  sbsigntools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.4-8.amzn2
  - **AL2023.12 version:** 0.9.4-8.amzn2023.0.2

- ** `scap-security-guide` **
  - **RPM:**  scap-security-guide  / **Architectures:** noarch
  - **RPM:**  scap-security-guide-doc  / **Architectures:** noarch
  - **AL2 version:** 0.1.40-12.amzn2.0.1.1
  - **AL2023.12 version:** 0.1.80-1.amzn2023.0.1

- ** `screen` **
  - **RPM:**  screen
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.1.0-0.27.20120314git3c2946.amzn2.0.2
  - **AL2023.12 version:** 4.8.0-5.amzn2023.0.4

- ** `scrub` **
  - **RPM:**  scrub
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.2-7.amzn2.0.1
  - **AL2023.12 version:** 2.6.1-2.amzn2023.0.2

- ** `seahorse` **
  - **RPM:**  seahorse
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.20.0-1.amzn2.0.2
  - **AL2023.12 version:** 47.0.1-1.amzn2023.0.1

- ** `sed` **
  - **RPM:**  sed
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.2.2-5.amzn2.0.2
  - **AL2023.12 version:** 4.8-7.amzn2023.0.2

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2 version:** 3.13.1-192.amzn2.6.8
  - **AL2023.12 version:** 38.1.76-1.amzn2023.0.2

- ** `sendmail` **
  - **RPM:**  sendmail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sendmail-cf  / **Architectures:** noarch
  - **RPM:**  sendmail-doc  / **Architectures:** noarch
  - **RPM:**  sendmail-milter  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.14.7-5.amzn2.0.1
  - **AL2023.12 version:** 8.18.2-2.amzn2023.0.1

- ** `setools` **
  - **RPM:**  setools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  setools-console  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.3.8-2.amzn2.0.2
  - **AL2023.12 version:** 4.4.1-1.amzn2023

- ** `setup` **
  - **RPM:**  setup
  - **Architectures:** noarch
  - **AL2 version:** 2.8.71-10.amzn2.0.1
  - **AL2023.12 version:** 2.13.7-3.amzn2023.0.2

- ** `sgml-common` **
  - **RPM:**  sgml-common  / **Architectures:** noarch
  - **RPM:**  xml-common  / **Architectures:** noarch
  - **AL2 version:** 0.6.3-39.amzn2
  - **AL2023.12 version:** 0.6.3-56.amzn2023.0.2

- ** `sgpio` **
  - **RPM:**  sgpio
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.0.10-13.amzn2.0.1
  - **AL2023.12 version:** 1.2.0.10-28.amzn2023.0.2

- ** `shadow-utils` **
  - **RPM:**  shadow-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.1.5.1-24.amzn2.0.3
  - **AL2023.12 version:** 4.9-12.amzn2023.0.4

- ** `shared-mime-info` **
  - **RPM:**  shared-mime-info
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8-4.amzn2
  - **AL2023.12 version:** 2.2-2.amzn2023.0.1

- ** `sharutils` **
  - **RPM:**  sharutils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.13.3-8.amzn2.0.2
  - **AL2023.12 version:** 4.15.2-19.amzn2023.0.2

- ** `sil-padauk-fonts` **
  - **RPM:**  sil-padauk-book-fonts  / **Architectures:** noarch
  - **RPM:**  sil-padauk-fonts  / **Architectures:** noarch
  - **AL2 version:** 2.8-5.amzn2
  - **AL2023.12 version:** 3.003-7.amzn2023.0.2

- ** `sip` **
  - **RPM:**  sip
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.14.6-4.amzn2.0.1
  - **AL2023.12 version:** 4.19.24-3.amzn2023.0.2

- ** `sisu` **
  - **RPM:**  sisu  / **Architectures:** noarch
  - **RPM:**  sisu-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.3.0-11.amzn2
  - **AL2023.12 version:** 0.3.4-9.amzn2023.0.4

- ** `slang` **
  - **RPM:**  slang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  slang-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  slang-slsh  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.4-11.amzn2.0.2
  - **AL2023.12 version:** 2.3.2-9.amzn2023.0.3

- ** `slf4j` **
  - **RPM:**  slf4j  / **Architectures:** noarch
  - **RPM:**  slf4j-javadoc  / **Architectures:** noarch
  - **RPM:**  slf4j-manual  / **Architectures:** noarch
  - **AL2 version:** 1.7.4-4.amzn2
  - **AL2023.12 version:** 1.7.32-3.amzn2023.0.4

- ** `smartmontools` **
  - **RPM:**  smartmontools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.0-2.amzn2
  - **AL2023.12 version:** 7.2-11.amzn2023.0.1

- ** `smart-restart` **
  - **RPM:**  smart-restart
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2-1.amzn2.0.1
  - **AL2023.12 version:** 0.1-1.amzn2023.0.3

- ** `snakeyaml` **
  - **RPM:**  snakeyaml  / **Architectures:** noarch
  - **RPM:**  snakeyaml-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.11-8.amzn2.0.3
  - **AL2023.12 version:** 1.27-6.amzn2023.0.3

- ** `snappy` **
  - **RPM:**  snappy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  snappy-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1.0-3.amzn2.0.2
  - **AL2023.12 version:** 1.1.8-5.amzn2023.0.2

- ** `socat` **
  - **RPM:**  socat
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.3.2-2.amzn2.0.2
  - **AL2023.12 version:** 1.7.4.2-1.amzn2023.0.3

- ** `softhsm` **
  - **RPM:**  softhsm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  softhsm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.0-2.amzn2.0.2
  - **AL2023.12 version:** 2.6.1-5.amzn2023.4.0.2

- ** `sound-theme-freedesktop` **
  - **RPM:**  sound-theme-freedesktop
  - **Architectures:** noarch
  - **AL2 version:** 0.8-3.amzn2
  - **AL2023.12 version:** 0.8-22.amzn2023

- ** `source-highlight` **
  - **RPM:**  source-highlight  / **Architectures:** aarch64, x86\_64
  - **RPM:**  source-highlight-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.6-6.amzn2.0.2
  - **AL2023.12 version:** 3.1.9-9.amzn2023.0.2

- ** `sox` **
  - **RPM:**  sox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sox-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 14.4.1-7.amzn2.0.4
  - **AL2023.12 version:** 14.4.2.0-1.amzn2023

- ** `spamassassin` **
  - **RPM:**  spamassassin
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.4.4-3.amzn2.0.1
  - **AL2023.12 version:** 4.0.0-6.amzn2023.0.1

- ** `speex` **
  - **RPM:**  speex  / **Architectures:** aarch64, x86\_64
  - **RPM:**  speex-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  speex-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2-0.19.rc1.amzn2.0.1
  - **AL2023.12 version:** 1.2.0-8.amzn2023.0.2

- ** `spice-protocol` **
  - **RPM:**  spice-protocol
  - **Architectures:** noarch
  - **AL2 version:** 0.12.14-1.amzn2
  - **AL2023.12 version:** 0.14.4-6.amzn2023

- ** `spice-vdagent` **
  - **RPM:**  spice-vdagent
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.14.0-18.amzn2.0.2
  - **AL2023.12 version:** 0.22.1-7.amzn2023.0.1

- ** `sqlite` **
  - **RPM:**  lemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sqlite-doc  / **Architectures:** noarch
  - **RPM:**  sqlite-tcl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.7.17-8.amzn2.1.3
  - **AL2023.12 version:** 3.40.0-1.amzn2023.0.8

- ** `squashfs-tools` **
  - **RPM:**  squashfs-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.3-0.21.gitaae0aff4.amzn2.0.3
  - **AL2023.12 version:** 4.5-3.amzn2023.0.2

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.5.20-17.amzn2.7.27
  - **AL2023.12 version:** 6.13-1.amzn2023.0.5

- ** `sscg` **
  - **RPM:**  sscg
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.3-2.amzn2.0.1
  - **AL2023.12 version:** 3.0.3-77.amzn2023

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
  - **RPM:**  sssd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ad  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-common-pac  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-dbus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ipa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-kcm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-krb5-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-proxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sssd-winbind-idmap  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.16.5-12.amzn2.15
  - **AL2023.12 version:** 2.9.4-1.amzn2023.0.4

- ** `star` **
  - **RPM:**  rmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  scpio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  spax  / **Architectures:** aarch64, x86\_64
  - **RPM:**  star  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.2-13.amzn2.0.1
  - **AL2023.12 version:** 1.6-4.amzn2023.0.2

- ** `startup-notification` **
  - **RPM:**  startup-notification  / **Architectures:** aarch64, x86\_64
  - **RPM:**  startup-notification-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12-8.amzn2.0.1
  - **AL2023.12 version:** 0.12-21.amzn2023.0.2

- ** `strace` **
  - **RPM:**  strace
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.26-1.amzn2.0.1
  - **AL2023.12 version:** 6.12-1.amzn2023.0.1

- ** `stunnel` **
  - **RPM:**  stunnel
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.56-6.amzn2.0.3
  - **AL2023.12 version:** 5.58-1.amzn2023.0.2

- ** `stunnel` (`stunnel5` in AL2) **
  - **RPM:**  stunnel (stunnel5 in AL2)
  - **Architectures:**
  - **AL2 version:** 5.58-1.amzn2.0.1
  - **AL2023.12 version:** 5.58-1.amzn2023.0.2

- ** `subversion` **
  - **RPM:**  mod\_dav\_svn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  subversion  / **Architectures:** aarch64, x86\_64
  - **RPM:**  subversion-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  subversion-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  subversion-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  subversion-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.14-16.amzn2.0.1
  - **AL2023.12 version:** 1.14.5-3.amzn2023.0.1

- ** `sudo` **
  - **RPM:**  sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.23-10.amzn2.3.8
  - **AL2023.12 version:** 1.9.15-1.p5.amzn2023.0.3

- ** `suitesparse` **
  - **RPM:**  suitesparse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  suitesparse-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  suitesparse-doc  / **Architectures:** noarch
  - **RPM:**  suitesparse-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.0.2-10.amzn2.0.1
  - **AL2023.12 version:** 5.4.0-6.amzn2023.0.2

- ** `swig` **
  - **RPM:**  swig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  swig-doc  / **Architectures:** noarch
  - **RPM:**  swig-gdb  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.12-11.amzn2.0.3
  - **AL2023.12 version:** 4.1.1-4.amzn2023.0.5

- ** `symlinks` **
  - **RPM:**  symlinks
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4-9.amzn2.0.2
  - **AL2023.12 version:** 1.7-4.amzn2023.0.2

- ** `sysctl-defaults` **
  - **RPM:**  sysctl-defaults
  - **Architectures:** noarch
  - **AL2 version:** 1.0-3.amzn2
  - **AL2023.12 version:** 1.0-3.amzn2023

- ** `sysfsutils` **
  - **RPM:**  libsysfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsysfs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sysfsutils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.0-16.amzn2.0.2
  - **AL2023.12 version:** 2.1.1-1.amzn2023.0.2

- ** `syslinux` **
  - **RPM:**  syslinux  / **Architectures:** x86\_64
  - **RPM:**  syslinux-devel  / **Architectures:** x86\_64
  - **RPM:**  syslinux-extlinux  / **Architectures:** x86\_64
  - **RPM:**  syslinux-perl  / **Architectures:** x86\_64
  - **AL2 version:** 4.05-13.amzn2.0.1
  - **AL2023.12 version:** 6.04-0.22.amzn2023.0.3

- ** `sysstat` **
  - **RPM:**  sysstat
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 10.1.5-18.amzn2.0.3
  - **AL2023.12 version:** 12.5.6-1.amzn2023.0.3

- ** `systemd` **
  - **RPM:**  systemd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-networkd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemd-resolved  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 219-78.amzn2.0.24
  - **AL2023.12 version:** 252.23-12.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-initscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-virtguest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.5-1.amzn2.0.3
  - **AL2023.12 version:** 5.4-1.amzn2023.0.2

- ** `t1lib` **
  - **RPM:**  t1lib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  t1lib-apps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  t1lib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  t1lib-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.1.2-14.amzn2.0.2
  - **AL2023.12 version:** 5.1.2-29.amzn2023.0.2

- ** `t1utils` **
  - **RPM:**  t1utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.37-6.amzn2.0.2
  - **AL2023.12 version:** 1.42-2.amzn2023.0.2

- ** `taglib` **
  - **RPM:**  taglib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  taglib-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8-8.20130218git.amzn2
  - **AL2023.12 version:** 1.12-4.amzn2023.0.3

- ** `tar` **
  - **RPM:**  tar
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.26-35.amzn2.0.4
  - **AL2023.12 version:** 1.34-1.amzn2023.0.4

- ** `targetcli` **
  - **RPM:**  targetcli
  - **Architectures:** noarch
  - **AL2 version:** 2.1.53-1.amzn2
  - **AL2023.12 version:** 2.1.54-7.amzn2023

- ** `tbb` **
  - **RPM:**  tbb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tbb-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tbb-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.1-9.20130314.amzn2.0.1
  - **AL2023.12 version:** 2020.3-7.amzn2023.0.2

- ** `tcl` **
  - **RPM:**  tcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tcl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.5.13-8.amzn2.0.2
  - **AL2023.12 version:** 8.6.10-5.amzn2023.0.2

- ** `tclx` **
  - **RPM:**  tclx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tclx-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.4.0-22.amzn2.0.1
  - **AL2023.12 version:** 8.4.0-37.amzn2023.0.2

- ** `tcpdump` **
  - **RPM:**  tcpdump
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.9.2-4.amzn2.1.0.1
  - **AL2023.12 version:** 4.99.1-1.amzn2023.0.2

- ** `tcsh` **
  - **RPM:**  tcsh
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.18.01-15.amzn2.0.2
  - **AL2023.12 version:** 6.24.14-1.amzn2023

- ** `teckit` **
  - **RPM:**  teckit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  teckit-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.5.1-11.amzn2.0.2
  - **AL2023.12 version:** 2.5.9-6.amzn2023.0.2

- ** `telnet` **
  - **RPM:**  telnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  telnet-server  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.17-65.amzn2
  - **AL2023.12 version:** 0.17-83.amzn2023.0.2

- ** `testng` **
  - **RPM:**  testng  / **Architectures:** noarch
  - **RPM:**  testng-javadoc  / **Architectures:** noarch
  - **AL2 version:** 6.8.7-3.amzn2.0.1
  - **AL2023.12 version:** 7.4.0-3.amzn2023.0.4

- ** `texi2html` **
  - **RPM:**  texi2html
  - **Architectures:** noarch
  - **AL2 version:** 1.82-10.amzn2
  - **AL2023.12 version:** 5.0-15.amzn2023.0.2

- ** `texinfo` **
  - **RPM:**  info  / **Architectures:** aarch64, x86\_64
  - **RPM:**  texinfo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  texinfo-tex  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.1-5.amzn2
  - **AL2023.12 version:** 6.7-10.amzn2023.0.2

- ** `texlive` **
  - **RPM:**  texlive-adjustbox  / **Architectures:** noarch
  - **RPM:**  texlive-adjustbox-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ae  / **Architectures:** noarch
  - **RPM:**  texlive-ae-doc  / **Architectures:** noarch
  - **RPM:**  texlive-algorithms  / **Architectures:** noarch
  - **RPM:**  texlive-algorithms-doc  / **Architectures:** noarch
  - **RPM:**  texlive-amscls  / **Architectures:** noarch
  - **RPM:**  texlive-amscls-doc  / **Architectures:** noarch
  - **RPM:**  texlive-amsfonts  / **Architectures:** noarch
  - **RPM:**  texlive-amsfonts-doc  / **Architectures:** noarch
  - **RPM:**  texlive-amsmath  / **Architectures:** noarch
  - **RPM:**  texlive-amsmath-doc  / **Architectures:** noarch
  - **RPM:**  texlive-anysize  / **Architectures:** noarch
  - **RPM:**  texlive-anysize-doc  / **Architectures:** noarch
  - **RPM:**  texlive-appendix  / **Architectures:** noarch
  - **RPM:**  texlive-appendix-doc  / **Architectures:** noarch
  - **RPM:**  texlive-arabxetex  / **Architectures:** noarch
  - **RPM:**  texlive-arabxetex-doc  / **Architectures:** noarch
  - **RPM:**  texlive-arphic  / **Architectures:** noarch
  - **RPM:**  texlive-arphic-doc  / **Architectures:** noarch
  - **RPM:**  texlive-attachfile  / **Architectures:** noarch
  - **RPM:**  texlive-attachfile-doc  / **Architectures:** noarch
  - **RPM:**  texlive-avantgar  / **Architectures:** noarch
  - **RPM:**  texlive-babel  / **Architectures:** noarch
  - **RPM:**  texlive-babelbib  / **Architectures:** noarch
  - **RPM:**  texlive-babelbib-doc  / **Architectures:** noarch
  - **RPM:**  texlive-babel-doc  / **Architectures:** noarch
  - **RPM:**  texlive-beamer  / **Architectures:** noarch
  - **RPM:**  texlive-beamer-doc  / **Architectures:** noarch
  - **RPM:**  texlive-bera  / **Architectures:** noarch
  - **RPM:**  texlive-bera-doc  / **Architectures:** noarch
  - **RPM:**  texlive-beton  / **Architectures:** noarch
  - **RPM:**  texlive-beton-doc  / **Architectures:** noarch
  - **RPM:**  texlive-bibtopic  / **Architectures:** noarch
  - **RPM:**  texlive-bibtopic-doc  / **Architectures:** noarch
  - **RPM:**  texlive-bidi  / **Architectures:** noarch
  - **RPM:**  texlive-bidi-doc  / **Architectures:** noarch
  - **RPM:**  texlive-bigfoot  / **Architectures:** noarch
  - **RPM:**  texlive-bigfoot-doc  / **Architectures:** noarch
  - **RPM:**  texlive-bookman  / **Architectures:** noarch
  - **RPM:**  texlive-booktabs  / **Architectures:** noarch
  - **RPM:**  texlive-booktabs-doc  / **Architectures:** noarch
  - **RPM:**  texlive-breakurl  / **Architectures:** noarch
  - **RPM:**  texlive-breakurl-doc  / **Architectures:** noarch
  - **RPM:**  texlive-caption  / **Architectures:** noarch
  - **RPM:**  texlive-caption-doc  / **Architectures:** noarch
  - **RPM:**  texlive-carlisle  / **Architectures:** noarch
  - **RPM:**  texlive-carlisle-doc  / **Architectures:** noarch
  - **RPM:**  texlive-changebar  / **Architectures:** noarch
  - **RPM:**  texlive-changebar-doc  / **Architectures:** noarch
  - **RPM:**  texlive-changepage  / **Architectures:** noarch
  - **RPM:**  texlive-changepage-doc  / **Architectures:** noarch
  - **RPM:**  texlive-charter  / **Architectures:** noarch
  - **RPM:**  texlive-charter-doc  / **Architectures:** noarch
  - **RPM:**  texlive-chngcntr  / **Architectures:** noarch
  - **RPM:**  texlive-chngcntr-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cite  / **Architectures:** noarch
  - **RPM:**  texlive-cite-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cjk  / **Architectures:** noarch
  - **RPM:**  texlive-cjk-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cm  / **Architectures:** noarch
  - **RPM:**  texlive-cmap  / **Architectures:** noarch
  - **RPM:**  texlive-cmap-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cm-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cmextra  / **Architectures:** noarch
  - **RPM:**  texlive-cm-lgc  / **Architectures:** noarch
  - **RPM:**  texlive-cm-lgc-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cm-super  / **Architectures:** noarch
  - **RPM:**  texlive-cm-super-doc  / **Architectures:** noarch
  - **RPM:**  texlive-cns  / **Architectures:** noarch
  - **RPM:**  texlive-cns-doc  / **Architectures:** noarch
  - **RPM:**  texlive-collectbox  / **Architectures:** noarch
  - **RPM:**  texlive-collectbox-doc  / **Architectures:** noarch
  - **RPM:**  texlive-collection-basic  / **Architectures:** noarch
  - **RPM:**  texlive-collection-fontsrecommended  / **Architectures:** noarch
  - **RPM:**  texlive-collection-latex  / **Architectures:** noarch
  - **RPM:**  texlive-collection-latexrecommended  / **Architectures:** noarch
  - **RPM:**  texlive-collection-xetex  / **Architectures:** noarch
  - **RPM:**  texlive-colortbl  / **Architectures:** noarch
  - **RPM:**  texlive-colortbl-doc  / **Architectures:** noarch
  - **RPM:**  texlive-courier  / **Architectures:** noarch
  - **RPM:**  texlive-crop  / **Architectures:** noarch
  - **RPM:**  texlive-crop-doc  / **Architectures:** noarch
  - **RPM:**  texlive-csquotes  / **Architectures:** noarch
  - **RPM:**  texlive-csquotes-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ctable  / **Architectures:** noarch
  - **RPM:**  texlive-ctable-doc  / **Architectures:** noarch
  - **RPM:**  texlive-currfile  / **Architectures:** noarch
  - **RPM:**  texlive-currfile-doc  / **Architectures:** noarch
  - **RPM:**  texlive-datetime  / **Architectures:** noarch
  - **RPM:**  texlive-datetime-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ec  / **Architectures:** noarch
  - **RPM:**  texlive-ec-doc  / **Architectures:** noarch
  - **RPM:**  texlive-eepic  / **Architectures:** noarch
  - **RPM:**  texlive-eepic-doc  / **Architectures:** noarch
  - **RPM:**  texlive-enctex  / **Architectures:** noarch
  - **RPM:**  texlive-enctex-doc  / **Architectures:** noarch
  - **RPM:**  texlive-enumitem  / **Architectures:** noarch
  - **RPM:**  texlive-enumitem-doc  / **Architectures:** noarch
  - **RPM:**  texlive-epsf  / **Architectures:** noarch
  - **RPM:**  texlive-epsf-doc  / **Architectures:** noarch
  - **RPM:**  texlive-eso-pic  / **Architectures:** noarch
  - **RPM:**  texlive-eso-pic-doc  / **Architectures:** noarch
  - **RPM:**  texlive-etex  / **Architectures:** noarch
  - **RPM:**  texlive-etex-doc  / **Architectures:** noarch
  - **RPM:**  texlive-etex-pkg  / **Architectures:** noarch
  - **RPM:**  texlive-etex-pkg-doc  / **Architectures:** noarch
  - **RPM:**  texlive-etoolbox  / **Architectures:** noarch
  - **RPM:**  texlive-etoolbox-doc  / **Architectures:** noarch
  - **RPM:**  texlive-euenc  / **Architectures:** noarch
  - **RPM:**  texlive-euenc-doc  / **Architectures:** noarch
  - **RPM:**  texlive-euler  / **Architectures:** noarch
  - **RPM:**  texlive-euler-doc  / **Architectures:** noarch
  - **RPM:**  texlive-euro  / **Architectures:** noarch
  - **RPM:**  texlive-euro-doc  / **Architectures:** noarch
  - **RPM:**  texlive-eurosym  / **Architectures:** noarch
  - **RPM:**  texlive-eurosym-doc  / **Architectures:** noarch
  - **RPM:**  texlive-extsizes  / **Architectures:** noarch
  - **RPM:**  texlive-extsizes-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fancybox  / **Architectures:** noarch
  - **RPM:**  texlive-fancybox-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fancyhdr  / **Architectures:** noarch
  - **RPM:**  texlive-fancyhdr-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fancyref  / **Architectures:** noarch
  - **RPM:**  texlive-fancyref-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fancyvrb  / **Architectures:** noarch
  - **RPM:**  texlive-fancyvrb-doc  / **Architectures:** noarch
  - **RPM:**  texlive-filecontents  / **Architectures:** noarch
  - **RPM:**  texlive-filecontents-doc  / **Architectures:** noarch
  - **RPM:**  texlive-filehook  / **Architectures:** noarch
  - **RPM:**  texlive-filehook-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fix2col  / **Architectures:** noarch
  - **RPM:**  texlive-fix2col-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fixlatvian  / **Architectures:** noarch
  - **RPM:**  texlive-fixlatvian-doc  / **Architectures:** noarch
  - **RPM:**  texlive-float  / **Architectures:** noarch
  - **RPM:**  texlive-float-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fmtcount  / **Architectures:** noarch
  - **RPM:**  texlive-fmtcount-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fncychap  / **Architectures:** noarch
  - **RPM:**  texlive-fncychap-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fontbook  / **Architectures:** noarch
  - **RPM:**  texlive-fontbook-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fontspec  / **Architectures:** noarch
  - **RPM:**  texlive-fontspec-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fontwrap  / **Architectures:** noarch
  - **RPM:**  texlive-fontwrap-doc  / **Architectures:** noarch
  - **RPM:**  texlive-footmisc  / **Architectures:** noarch
  - **RPM:**  texlive-footmisc-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fp  / **Architectures:** noarch
  - **RPM:**  texlive-fp-doc  / **Architectures:** noarch
  - **RPM:**  texlive-fpl  / **Architectures:** noarch
  - **RPM:**  texlive-fpl-doc  / **Architectures:** noarch
  - **RPM:**  texlive-framed  / **Architectures:** noarch
  - **RPM:**  texlive-framed-doc  / **Architectures:** noarch
  - **RPM:**  texlive-garuda-c90  / **Architectures:** noarch
  - **RPM:**  texlive-geometry  / **Architectures:** noarch
  - **RPM:**  texlive-geometry-doc  / **Architectures:** noarch
  - **RPM:**  texlive-graphics  / **Architectures:** noarch
  - **RPM:**  texlive-graphics-doc  / **Architectures:** noarch
  - **RPM:**  texlive-helvetic  / **Architectures:** noarch
  - **RPM:**  texlive-hyperref  / **Architectures:** noarch
  - **RPM:**  texlive-hyperref-doc  / **Architectures:** noarch
  - **RPM:**  texlive-hyphenat  / **Architectures:** noarch
  - **RPM:**  texlive-hyphenat-doc  / **Architectures:** noarch
  - **RPM:**  texlive-hyphen-base  / **Architectures:** noarch
  - **RPM:**  texlive-hyph-utf8  / **Architectures:** noarch
  - **RPM:**  texlive-hyph-utf8-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ifmtarg  / **Architectures:** noarch
  - **RPM:**  texlive-ifmtarg-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ifoddpage  / **Architectures:** noarch
  - **RPM:**  texlive-ifoddpage-doc  / **Architectures:** noarch
  - **RPM:**  texlive-iftex  / **Architectures:** noarch
  - **RPM:**  texlive-iftex-doc  / **Architectures:** noarch
  - **RPM:**  texlive-index  / **Architectures:** noarch
  - **RPM:**  texlive-index-doc  / **Architectures:** noarch
  - **RPM:**  texlive-jknapltx  / **Architectures:** noarch
  - **RPM:**  texlive-jknapltx-doc  / **Architectures:** noarch
  - **RPM:**  texlive-kastrup  / **Architectures:** noarch
  - **RPM:**  texlive-kastrup-doc  / **Architectures:** noarch
  - **RPM:**  texlive-kerkis  / **Architectures:** noarch
  - **RPM:**  texlive-kerkis-doc  / **Architectures:** noarch
  - **RPM:**  texlive-koma-script  / **Architectures:** noarch
  - **RPM:**  texlive-l3experimental  / **Architectures:** noarch
  - **RPM:**  texlive-l3experimental-doc  / **Architectures:** noarch
  - **RPM:**  texlive-l3kernel  / **Architectures:** noarch
  - **RPM:**  texlive-l3kernel-doc  / **Architectures:** noarch
  - **RPM:**  texlive-l3packages  / **Architectures:** noarch
  - **RPM:**  texlive-l3packages-doc  / **Architectures:** noarch
  - **RPM:**  texlive-lastpage  / **Architectures:** noarch
  - **RPM:**  texlive-lastpage-doc  / **Architectures:** noarch
  - **RPM:**  texlive-latexconfig  / **Architectures:** noarch
  - **RPM:**  texlive-latex-fonts  / **Architectures:** noarch
  - **RPM:**  texlive-latex-fonts-doc  / **Architectures:** noarch
  - **RPM:**  texlive-lettrine  / **Architectures:** noarch
  - **RPM:**  texlive-lettrine-doc  / **Architectures:** noarch
  - **RPM:**  texlive-listings  / **Architectures:** noarch
  - **RPM:**  texlive-listings-doc  / **Architectures:** noarch
  - **RPM:**  texlive-lm  / **Architectures:** noarch
  - **RPM:**  texlive-lm-doc  / **Architectures:** noarch
  - **RPM:**  texlive-lm-math  / **Architectures:** noarch
  - **RPM:**  texlive-lm-math-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ltxmisc  / **Architectures:** noarch
  - **RPM:**  texlive-lua-alt-getopt  / **Architectures:** noarch
  - **RPM:**  texlive-lua-alt-getopt-doc  / **Architectures:** noarch
  - **RPM:**  texlive-lualatex-math  / **Architectures:** noarch
  - **RPM:**  texlive-lualatex-math-doc  / **Architectures:** noarch
  - **RPM:**  texlive-luatexbase  / **Architectures:** noarch
  - **RPM:**  texlive-luatexbase-doc  / **Architectures:** noarch
  - **RPM:**  texlive-makecmds  / **Architectures:** noarch
  - **RPM:**  texlive-makecmds-doc  / **Architectures:** noarch
  - **RPM:**  texlive-marginnote  / **Architectures:** noarch
  - **RPM:**  texlive-marginnote-doc  / **Architectures:** noarch
  - **RPM:**  texlive-marvosym  / **Architectures:** noarch
  - **RPM:**  texlive-marvosym-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mathpazo  / **Architectures:** noarch
  - **RPM:**  texlive-mathpazo-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mathspec  / **Architectures:** noarch
  - **RPM:**  texlive-mathspec-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mdwtools  / **Architectures:** noarch
  - **RPM:**  texlive-mdwtools-doc  / **Architectures:** noarch
  - **RPM:**  texlive-memoir  / **Architectures:** noarch
  - **RPM:**  texlive-memoir-doc  / **Architectures:** noarch
  - **RPM:**  texlive-metalogo  / **Architectures:** noarch
  - **RPM:**  texlive-metalogo-doc  / **Architectures:** noarch
  - **RPM:**  texlive-metapost-examples-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mflogo  / **Architectures:** noarch
  - **RPM:**  texlive-mflogo-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mfnfss  / **Architectures:** noarch
  - **RPM:**  texlive-mfnfss-doc  / **Architectures:** noarch
  - **RPM:**  texlive-microtype  / **Architectures:** noarch
  - **RPM:**  texlive-microtype-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mnsymbol  / **Architectures:** noarch
  - **RPM:**  texlive-mnsymbol-doc  / **Architectures:** noarch
  - **RPM:**  texlive-mparhack  / **Architectures:** noarch
  - **RPM:**  texlive-mparhack-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ms  / **Architectures:** noarch
  - **RPM:**  texlive-ms-doc  / **Architectures:** noarch
  - **RPM:**  texlive-multido  / **Architectures:** noarch
  - **RPM:**  texlive-multido-doc  / **Architectures:** noarch
  - **RPM:**  texlive-multirow  / **Architectures:** noarch
  - **RPM:**  texlive-multirow-doc  / **Architectures:** noarch
  - **RPM:**  texlive-natbib  / **Architectures:** noarch
  - **RPM:**  texlive-natbib-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ncctools  / **Architectures:** noarch
  - **RPM:**  texlive-ncctools-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ncntrsbk  / **Architectures:** noarch
  - **RPM:**  texlive-norasi-c90  / **Architectures:** noarch
  - **RPM:**  texlive-ntgclass  / **Architectures:** noarch
  - **RPM:**  texlive-ntgclass-doc  / **Architectures:** noarch
  - **RPM:**  texlive-overpic  / **Architectures:** noarch
  - **RPM:**  texlive-overpic-doc  / **Architectures:** noarch
  - **RPM:**  texlive-palatino  / **Architectures:** noarch
  - **RPM:**  texlive-paralist  / **Architectures:** noarch
  - **RPM:**  texlive-paralist-doc  / **Architectures:** noarch
  - **RPM:**  texlive-parallel  / **Architectures:** noarch
  - **RPM:**  texlive-parallel-doc  / **Architectures:** noarch
  - **RPM:**  texlive-parskip  / **Architectures:** noarch
  - **RPM:**  texlive-parskip-doc  / **Architectures:** noarch
  - **RPM:**  texlive-passivetex  / **Architectures:** noarch
  - **RPM:**  texlive-pdfpages  / **Architectures:** noarch
  - **RPM:**  texlive-pdfpages-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pgf  / **Architectures:** noarch
  - **RPM:**  texlive-pgf-doc  / **Architectures:** noarch
  - **RPM:**  texlive-philokalia  / **Architectures:** noarch
  - **RPM:**  texlive-philokalia-doc  / **Architectures:** noarch
  - **RPM:**  texlive-placeins  / **Architectures:** noarch
  - **RPM:**  texlive-placeins-doc  / **Architectures:** noarch
  - **RPM:**  texlive-plain  / **Architectures:** noarch
  - **RPM:**  texlive-polyglossia  / **Architectures:** noarch
  - **RPM:**  texlive-polyglossia-doc  / **Architectures:** noarch
  - **RPM:**  texlive-powerdot  / **Architectures:** noarch
  - **RPM:**  texlive-powerdot-doc  / **Architectures:** noarch
  - **RPM:**  texlive-preprint  / **Architectures:** noarch
  - **RPM:**  texlive-preprint-doc  / **Architectures:** noarch
  - **RPM:**  texlive-psfrag  / **Architectures:** noarch
  - **RPM:**  texlive-psfrag-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pslatex  / **Architectures:** noarch
  - **RPM:**  texlive-psnfss  / **Architectures:** noarch
  - **RPM:**  texlive-psnfss-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pspicture  / **Architectures:** noarch
  - **RPM:**  texlive-pspicture-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-3d  / **Architectures:** noarch
  - **RPM:**  texlive-pst-3d-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-blur  / **Architectures:** noarch
  - **RPM:**  texlive-pst-blur-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-coil  / **Architectures:** noarch
  - **RPM:**  texlive-pst-coil-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-eps  / **Architectures:** noarch
  - **RPM:**  texlive-pst-eps-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-fill  / **Architectures:** noarch
  - **RPM:**  texlive-pst-fill-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-grad  / **Architectures:** noarch
  - **RPM:**  texlive-pst-grad-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-math  / **Architectures:** noarch
  - **RPM:**  texlive-pst-math-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-node  / **Architectures:** noarch
  - **RPM:**  texlive-pst-node-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-plot  / **Architectures:** noarch
  - **RPM:**  texlive-pst-plot-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pstricks  / **Architectures:** noarch
  - **RPM:**  texlive-pstricks-add  / **Architectures:** noarch
  - **RPM:**  texlive-pstricks-add-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pstricks-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-slpe  / **Architectures:** noarch
  - **RPM:**  texlive-pst-slpe-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-text  / **Architectures:** noarch
  - **RPM:**  texlive-pst-text-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pst-tree  / **Architectures:** noarch
  - **RPM:**  texlive-pst-tree-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ptext  / **Architectures:** noarch
  - **RPM:**  texlive-ptext-doc  / **Architectures:** noarch
  - **RPM:**  texlive-pxfonts  / **Architectures:** noarch
  - **RPM:**  texlive-pxfonts-doc  / **Architectures:** noarch
  - **RPM:**  texlive-qstest  / **Architectures:** noarch
  - **RPM:**  texlive-qstest-doc  / **Architectures:** noarch
  - **RPM:**  texlive-rcs  / **Architectures:** noarch
  - **RPM:**  texlive-rcs-doc  / **Architectures:** noarch
  - **RPM:**  texlive-realscripts  / **Architectures:** noarch
  - **RPM:**  texlive-realscripts-doc  / **Architectures:** noarch
  - **RPM:**  texlive-rsfs  / **Architectures:** noarch
  - **RPM:**  texlive-rsfs-doc  / **Architectures:** noarch
  - **RPM:**  texlive-sansmath  / **Architectures:** noarch
  - **RPM:**  texlive-sansmath-doc  / **Architectures:** noarch
  - **RPM:**  texlive-sauerj  / **Architectures:** noarch
  - **RPM:**  texlive-sauerj-doc  / **Architectures:** noarch
  - **RPM:**  texlive-scheme-basic  / **Architectures:** noarch
  - **RPM:**  texlive-section  / **Architectures:** noarch
  - **RPM:**  texlive-section-doc  / **Architectures:** noarch
  - **RPM:**  texlive-sectsty  / **Architectures:** noarch
  - **RPM:**  texlive-sectsty-doc  / **Architectures:** noarch
  - **RPM:**  texlive-seminar  / **Architectures:** noarch
  - **RPM:**  texlive-seminar-doc  / **Architectures:** noarch
  - **RPM:**  texlive-sepnum  / **Architectures:** noarch
  - **RPM:**  texlive-sepnum-doc  / **Architectures:** noarch
  - **RPM:**  texlive-setspace  / **Architectures:** noarch
  - **RPM:**  texlive-setspace-doc  / **Architectures:** noarch
  - **RPM:**  texlive-showexpl  / **Architectures:** noarch
  - **RPM:**  texlive-showexpl-doc  / **Architectures:** noarch
  - **RPM:**  texlive-soul  / **Architectures:** noarch
  - **RPM:**  texlive-soul-doc  / **Architectures:** noarch
  - **RPM:**  texlive-stmaryrd  / **Architectures:** noarch
  - **RPM:**  texlive-stmaryrd-doc  / **Architectures:** noarch
  - **RPM:**  texlive-subfig  / **Architectures:** noarch
  - **RPM:**  texlive-subfig-doc  / **Architectures:** noarch
  - **RPM:**  texlive-subfigure  / **Architectures:** noarch
  - **RPM:**  texlive-subfigure-doc  / **Architectures:** noarch
  - **RPM:**  texlive-svn-prov  / **Architectures:** noarch
  - **RPM:**  texlive-svn-prov-doc  / **Architectures:** noarch
  - **RPM:**  texlive-symbol  / **Architectures:** noarch
  - **RPM:**  texlive-t2  / **Architectures:** noarch
  - **RPM:**  texlive-t2-doc  / **Architectures:** noarch
  - **RPM:**  texlive-tex-gyre  / **Architectures:** noarch
  - **RPM:**  texlive-tex-gyre-doc  / **Architectures:** noarch
  - **RPM:**  texlive-tex-gyre-math  / **Architectures:** noarch
  - **RPM:**  texlive-tex-gyre-math-doc  / **Architectures:** noarch
  - **RPM:**  texlive-textcase  / **Architectures:** noarch
  - **RPM:**  texlive-textcase-doc  / **Architectures:** noarch
  - **RPM:**  texlive-textpos  / **Architectures:** noarch
  - **RPM:**  texlive-textpos-doc  / **Architectures:** noarch
  - **RPM:**  texlive-threeparttable  / **Architectures:** noarch
  - **RPM:**  texlive-threeparttable-doc  / **Architectures:** noarch
  - **RPM:**  texlive-times  / **Architectures:** noarch
  - **RPM:**  texlive-tipa  / **Architectures:** noarch
  - **RPM:**  texlive-tipa-doc  / **Architectures:** noarch
  - **RPM:**  texlive-titlesec  / **Architectures:** noarch
  - **RPM:**  texlive-titlesec-doc  / **Architectures:** noarch
  - **RPM:**  texlive-titling  / **Architectures:** noarch
  - **RPM:**  texlive-titling-doc  / **Architectures:** noarch
  - **RPM:**  texlive-tocloft  / **Architectures:** noarch
  - **RPM:**  texlive-tocloft-doc  / **Architectures:** noarch
  - **RPM:**  texlive-tools  / **Architectures:** noarch
  - **RPM:**  texlive-tools-doc  / **Architectures:** noarch
  - **RPM:**  texlive-txfonts  / **Architectures:** noarch
  - **RPM:**  texlive-txfonts-doc  / **Architectures:** noarch
  - **RPM:**  texlive-type1cm  / **Architectures:** noarch
  - **RPM:**  texlive-type1cm-doc  / **Architectures:** noarch
  - **RPM:**  texlive-typehtml  / **Architectures:** noarch
  - **RPM:**  texlive-typehtml-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ucharclasses  / **Architectures:** noarch
  - **RPM:**  texlive-ucharclasses-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ucs  / **Architectures:** noarch
  - **RPM:**  texlive-ucs-doc  / **Architectures:** noarch
  - **RPM:**  texlive-uhc  / **Architectures:** noarch
  - **RPM:**  texlive-uhc-doc  / **Architectures:** noarch
  - **RPM:**  texlive-ulem  / **Architectures:** noarch
  - **RPM:**  texlive-ulem-doc  / **Architectures:** noarch
  - **RPM:**  texlive-underscore  / **Architectures:** noarch
  - **RPM:**  texlive-underscore-doc  / **Architectures:** noarch
  - **RPM:**  texlive-unicode-math  / **Architectures:** noarch
  - **RPM:**  texlive-unicode-math-doc  / **Architectures:** noarch
  - **RPM:**  texlive-unisugar  / **Architectures:** noarch
  - **RPM:**  texlive-unisugar-doc  / **Architectures:** noarch
  - **RPM:**  texlive-url  / **Architectures:** noarch
  - **RPM:**  texlive-url-doc  / **Architectures:** noarch
  - **RPM:**  texlive-utopia  / **Architectures:** noarch
  - **RPM:**  texlive-utopia-doc  / **Architectures:** noarch
  - **RPM:**  texlive-varwidth  / **Architectures:** noarch
  - **RPM:**  texlive-varwidth-doc  / **Architectures:** noarch
  - **RPM:**  texlive-wadalab  / **Architectures:** noarch
  - **RPM:**  texlive-wadalab-doc  / **Architectures:** noarch
  - **RPM:**  texlive-was  / **Architectures:** noarch
  - **RPM:**  texlive-was-doc  / **Architectures:** noarch
  - **RPM:**  texlive-wasy  / **Architectures:** noarch
  - **RPM:**  texlive-wasy-doc  / **Architectures:** noarch
  - **RPM:**  texlive-wasysym  / **Architectures:** noarch
  - **RPM:**  texlive-wasysym-doc  / **Architectures:** noarch
  - **RPM:**  texlive-wrapfig  / **Architectures:** noarch
  - **RPM:**  texlive-wrapfig-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xcolor  / **Architectures:** noarch
  - **RPM:**  texlive-xcolor-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xecjk  / **Architectures:** noarch
  - **RPM:**  texlive-xecjk-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xecolor  / **Architectures:** noarch
  - **RPM:**  texlive-xecolor-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xecyr  / **Architectures:** noarch
  - **RPM:**  texlive-xecyr-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xeindex  / **Architectures:** noarch
  - **RPM:**  texlive-xeindex-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xepersian  / **Architectures:** noarch
  - **RPM:**  texlive-xepersian-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xesearch  / **Architectures:** noarch
  - **RPM:**  texlive-xesearch-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xetexconfig  / **Architectures:** noarch
  - **RPM:**  texlive-xetexfontinfo  / **Architectures:** noarch
  - **RPM:**  texlive-xetexfontinfo-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-itrans  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-itrans-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-pstricks  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-pstricks-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-tibetan  / **Architectures:** noarch
  - **RPM:**  texlive-xetex-tibetan-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xifthen  / **Architectures:** noarch
  - **RPM:**  texlive-xifthen-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xkeyval  / **Architectures:** noarch
  - **RPM:**  texlive-xkeyval-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xltxtra  / **Architectures:** noarch
  - **RPM:**  texlive-xltxtra-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xstring  / **Architectures:** noarch
  - **RPM:**  texlive-xstring-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xtab  / **Architectures:** noarch
  - **RPM:**  texlive-xtab-doc  / **Architectures:** noarch
  - **RPM:**  texlive-xunicode  / **Architectures:** noarch
  - **RPM:**  texlive-xunicode-doc  / **Architectures:** noarch
  - **RPM:**  texlive-zapfchan  / **Architectures:** noarch
  - **RPM:**  texlive-zapfding  / **Architectures:** noarch
  - **AL2 version:** svn26555.0-38.amzn2.0.5
  - **AL2023.12 version:** svn56291-59.amzn2023.0.2

- ** `tftp` **
  - **RPM:**  tftp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tftp-server  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.2-22.amzn2
  - **AL2023.12 version:** 5.2-42.amzn2023.0.1

- ** `thai-scalable-fonts` **
  - **RPM:**  thai-scalable-fonts-common  / **Architectures:** noarch
  - **RPM:**  thai-scalable-garuda-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-kinnari-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-loma-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-norasi-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-purisa-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-sawasdee-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-tlwgmono-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-tlwgtypewriter-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-tlwgtypist-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-tlwgtypo-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-umpush-fonts  / **Architectures:** noarch
  - **RPM:**  thai-scalable-waree-fonts  / **Architectures:** noarch
  - **AL2 version:** 0.5.0-7.amzn2
  - **AL2023.12 version:** 0.7.2-3.amzn2023.0.2

- ** `tigervnc` **
  - **RPM:**  tigervnc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-icons  / **Architectures:** noarch
  - **RPM:**  tigervnc-license  / **Architectures:** noarch
  - **RPM:**  tigervnc-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-server-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-server-module  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.0-24.amzn2.0.10
  - **AL2023.12 version:** 1.14.1-3.amzn2023.0.6

- ** `time` **
  - **RPM:**  time
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7-45.amzn2.0.2
  - **AL2023.12 version:** 1.9-16.amzn2023.0.2

- ** `tix` **
  - **RPM:**  tix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tix-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tix-doc  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.4.3-12.amzn2.0.2
  - **AL2023.12 version:** 8.4.3-31.amzn2023.0.2

- ** `tk` **
  - **RPM:**  tk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tk-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 8.5.13-6.amzn2.0.2
  - **AL2023.12 version:** 8.6.10-6.amzn2023.0.2

- ** `tmux` **
  - **RPM:**  tmux
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8-4.amzn2.0.1
  - **AL2023.12 version:** 3.6a-1.amzn2023.0.1

- ** `tokyocabinet` **
  - **RPM:**  tokyocabinet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tokyocabinet-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tokyocabinet-devel-doc  / **Architectures:** noarch
  - **AL2 version:** 1.4.48-3.amzn2.0.2
  - **AL2023.12 version:** 1.4.48-17.amzn2023.0.2

- ** `tomcat9` (`tomcat` in AL2) **
  - **RPM:**  tomcat9 (tomcat in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps (tomcat-admin-webapps in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp (tomcat-docs-webapp in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib (tomcat-lib in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps (tomcat-webapps in AL2)  / **Architectures:** noarch
  - **AL2 version:** 7.0.76-10.amzn2.0.17
  - **AL2023.12 version:** 9.0.120-1.amzn2023.0.1

- ** `tpm2-abrmd` **
  - **RPM:**  tpm2-abrmd  / **Architectures:** x86\_64
  - **RPM:**  tpm2-abrmd-devel  / **Architectures:** x86\_64
  - **AL2 version:** 1.1.0-8.amzn2
  - **AL2023.12 version:** 3.0.0-7.amzn2023

- ** `tpm2-tools` **
  - **RPM:**  tpm2-tools
  - **Architectures:** x86\_64
  - **AL2 version:** 3.0.1-1.amzn2
  - **AL2023.12 version:** 5.5-4.amzn2023.0.2

- ** `tpm2-tss` **
  - **RPM:**  tpm2-tss  / **Architectures:** x86\_64
  - **RPM:**  tpm2-tss-devel  / **Architectures:** x86\_64
  - **AL2 version:** 1.3.0-2.amzn2
  - **AL2023.12 version:** 4.0.2-1.amzn2023.0.1

- ** `trace-cmd` **
  - **RPM:**  trace-cmd
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.6.0-10.amzn2
  - **AL2023.12 version:** 2.7-10.amzn2023.0.1

- ** `traceroute` **
  - **RPM:**  traceroute
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.22-2.amzn2.0.2
  - **AL2023.12 version:** 2.1.3-1.amzn2023

- ** `tracker` **
  - **RPM:**  tracker  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tracker-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.10.5-6.amzn2.0.1
  - **AL2023.12 version:** 3.7.3-3.amzn2023.0.1

- ** `transfig` **
  - **RPM:**  transfig
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.2.8b-7.amzn2
  - **AL2023.12 version:** 3.2.8b-4.amzn2023.0.2

- ** `tree` **
  - **RPM:**  tree
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.0-10.amzn2.0.1
  - **AL2023.12 version:** 1.8.0-6.amzn2023.0.2

- ** `trousers` **
  - **RPM:**  trousers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  trousers-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  trousers-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.14-2.amzn2.0.2
  - **AL2023.12 version:** 0.3.15-2.amzn2023.0.2

- ** `ttembed` **
  - **RPM:**  ttembed
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.1-8.amzn2.0.1
  - **AL2023.12 version:** 1.1-15.amzn2023.0.2

- ** `ttmkfdir` **
  - **RPM:**  ttmkfdir
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.9-42.amzn2.0.2
  - **AL2023.12 version:** 3.0.9-63.amzn2023.0.2

- ** `tuna` **
  - **RPM:**  tuna
  - **Architectures:** noarch
  - **AL2 version:** 0.13-5.amzn2.0.1
  - **AL2023.12 version:** 0.19-4.amzn2023.0.1

- ** `tuned` **
  - **RPM:**  tuned  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-atomic  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-compat  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-cpu-partitioning  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-nfv  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-nfv-guest  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-nfv-host  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-oracle  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-realtime  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-sap  / **Architectures:** noarch
  - **RPM:**  tuned-profiles-sap-hana  / **Architectures:** noarch
  - **RPM:**  tuned-utils  / **Architectures:** noarch
  - **RPM:**  tuned-utils-systemtap  / **Architectures:** noarch
  - **AL2 version:** 2.8.0-5.amzn2.0.1
  - **AL2023.12 version:** 2.25.1-2.amzn2023.0.2

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2 version:** 2026c-1.amzn2.0.1
  - **AL2023.12 version:** 2026c-1.amzn2023.0.1

- ** `ucs-miscfixed-fonts` **
  - **RPM:**  ucs-miscfixed-fonts
  - **Architectures:** noarch
  - **AL2 version:** 0.3-11.amzn2
  - **AL2023.12 version:** 0.3-26.amzn2023.0.2

- ** `udisks2` **
  - **RPM:**  libudisks2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libudisks2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2-lsm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  udisks2-lvm2  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.7.3-9.amzn2.0.4
  - **AL2023.12 version:** 2.10.1-6.amzn2023.0.3

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.7.3-15.amzn2.0.15
  - **AL2023.12 version:** 1.17.1-1.amzn2023.0.13

- ** `unicode-ucd` **
  - **RPM:**  unicode-ucd
  - **Architectures:** noarch
  - **AL2 version:** 6.3.0-2.amzn2
  - **AL2023.12 version:** 13.0.0-3.amzn2023.0.2

- ** `unixODBC` **
  - **RPM:**  unixODBC  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unixODBC-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.1-15.amzn2
  - **AL2023.12 version:** 2.3.9-3.amzn2023.0.3

- ** `unzip` **
  - **RPM:**  unzip
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 6.0-57.amzn2.0.2
  - **AL2023.12 version:** 6.0-68.amzn2023.0.2

- ** `update-motd` **
  - **RPM:**  update-motd
  - **Architectures:** noarch
  - **AL2 version:** 1.1.2-2.amzn2.0.2
  - **AL2023.12 version:** 2.3-1.amzn2023

- ** `upower` **
  - **RPM:**  upower  / **Architectures:** aarch64, x86\_64
  - **RPM:**  upower-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  upower-devel-docs  / **Architectures:** noarch
  - **AL2 version:** 0.99.7-1.amzn2
  - **AL2023.12 version:** 1.90.6-139.amzn2023

- ** `urlview` **
  - **RPM:**  urlview
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9-15.20121210git6cfcad.amzn2.0.2
  - **AL2023.12 version:** 0.9-32.20131022git08767a.amzn2023

- ** `urw-base35-fonts` **
  - **RPM:**  urw-base35-bookman-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-c059-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-d050000l-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-fonts-common  / **Architectures:** noarch
  - **RPM:**  urw-base35-fonts-devel  / **Architectures:** noarch
  - **RPM:**  urw-base35-fonts-legacy  / **Architectures:** noarch
  - **RPM:**  urw-base35-gothic-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-nimbus-mono-ps-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-nimbus-roman-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-nimbus-sans-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-p052-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-standard-symbols-ps-fonts  / **Architectures:** noarch
  - **RPM:**  urw-base35-z003-fonts  / **Architectures:** noarch
  - **AL2 version:** 20170801-10.amzn2
  - **AL2023.12 version:** 20200910-6.amzn2023.0.2

- ** `usbguard` **
  - **RPM:**  usbguard  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  usbguard-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.0-8.amzn2
  - **AL2023.12 version:** 1.1.3-4.amzn2023

- ** `userspace-rcu` **
  - **RPM:**  userspace-rcu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  userspace-rcu-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.7.16-1.amzn2.0.1
  - **AL2023.12 version:** 0.12.1-3.amzn2023.0.4

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
  - **RPM:**  util-linux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  util-linux-user  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuidd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.30.2-2.amzn2.0.14
  - **AL2023.12 version:** 2.37.4-1.amzn2023.0.6

- ** `uuid` **
  - **RPM:**  uuid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-dce  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-dce-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  uuid-perl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.2-26.amzn2.0.1
  - **AL2023.12 version:** 1.6.2-50.amzn2023.0.2

- ** `v4l-utils` **
  - **RPM:**  libv4l  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libv4l-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v4l-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v4l-utils-devel-tools  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.5-4.amzn2.0.1
  - **AL2023.12 version:** 1.26.1-6.amzn2023.0.2

- ** `vala` **
  - **RPM:**  vala  / **Architectures:** aarch64, x86\_64
  - **RPM:**  valadoc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vala-doc  / **Architectures:** noarch
  - **RPM:**  valadoc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.40.8-1.amzn2
  - **AL2023.12 version:** 0.56.17-1.amzn2023.0.1

- ** `valgrind` **
  - **RPM:**  valgrind  / **Architectures:** aarch64, x86\_64
  - **RPM:**  valgrind-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.19.0-1.amzn2.0.1
  - **AL2023.12 version:** 3.19.0-1.amzn2023.0.2

- ** `velocity` **
  - **RPM:**  velocity  / **Architectures:** noarch
  - **RPM:**  velocity-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.7-10.2.amzn2
  - **AL2023.12 version:** 1.7-38.amzn2023.0.3

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 9.0.2153-1.amzn2.0.9
  - **AL2023.12 version:** 9.2.780-1.amzn2023.0.1

- ** `virt-what` **
  - **RPM:**  virt-what
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.18-4.amzn2
  - **AL2023.12 version:** 1.25-2.amzn2023.0.1

- ** `volume_key` **
  - **RPM:**  volume\_key  / **Architectures:** aarch64, x86\_64
  - **RPM:**  volume\_key-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  volume\_key-libs  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.9-8.amzn2
  - **AL2023.12 version:** 0.3.12-14.amzn2023.0.2

- ** `vorbis-tools` **
  - **RPM:**  vorbis-tools
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.0-13.amzn2.0.2
  - **AL2023.12 version:** 1.4.2-2.amzn2023.0.4

- ** `vsftpd` **
  - **RPM:**  vsftpd
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.2-25.amzn2.0.2
  - **AL2023.12 version:** 3.0.5-1.amzn2023.0.3

- ** `vte291` **
  - **RPM:**  vte291  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte291-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte-profile  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.52.2-2.amzn2.0.1
  - **AL2023.12 version:** 0.78.2-1.amzn2023.0.1

- ** `watchdog` **
  - **RPM:**  watchdog
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.13-11.amzn2.0.1
  - **AL2023.12 version:** 5.16-11.amzn2023

- ** `wayland` **
  - **RPM:**  libwayland-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-cursor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-egl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libwayland-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wayland-doc  / **Architectures:** noarch
  - **AL2 version:** 1.17.0-1.amzn2.0.1
  - **AL2023.12 version:** 1.23.0-2.amzn2023.0.2

- ** `wayland-protocols` **
  - **RPM:**  wayland-protocols-devel
  - **Architectures:** noarch
  - **AL2 version:** 1.14-1.amzn2
  - **AL2023.12 version:** 1.36-1.amzn2023.0.1

- ** `webrtc-audio-processing` **
  - **RPM:**  webrtc-audio-processing  / **Architectures:** aarch64, x86\_64
  - **RPM:**  webrtc-audio-processing-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3-1.amzn2.0.1
  - **AL2023.12 version:** 0.3.1-6.amzn2023.0.2

- ** `weld-parent` **
  - **RPM:**  weld-parent
  - **Architectures:** noarch
  - **AL2 version:** 17-9.amzn2
  - **AL2023.12 version:** 45-3.amzn2023.0.1

- ** `wget` **
  - **RPM:**  wget
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.14-18.amzn2.1
  - **AL2023.12 version:** 1.21.3-1.amzn2023.0.5

- ** `which` **
  - **RPM:**  which
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.20-7.amzn2.0.2
  - **AL2023.12 version:** 2.21-26.amzn2023.0.2

- ** `whois` **
  - **RPM:**  whois
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.1.1-2.amzn2.0.1
  - **AL2023.12 version:** 5.5.10-1.amzn2023.0.2

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.6.2-15.amzn2.0.10
  - **AL2023.12 version:** 4.6.6-1.amzn2023.0.1

- ** `words` **
  - **RPM:**  words
  - **Architectures:** noarch
  - **AL2 version:** 3.0-22.amzn2
  - **AL2023.12 version:** 3.0-37.amzn2023.0.2

- ** `wsdl4j` **
  - **RPM:**  wsdl4j  / **Architectures:** noarch
  - **RPM:**  wsdl4j-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.6.3-3.1.amzn2
  - **AL2023.12 version:** 1.6.3-24.amzn2023.0.1

- ** `xalan-j2` **
  - **RPM:**  xalan-j2  / **Architectures:** noarch
  - **RPM:**  xalan-j2-manual  / **Architectures:** noarch
  - **RPM:**  xalan-j2-xsltc  / **Architectures:** noarch
  - **AL2 version:** 2.7.1-23.1.amzn2
  - **AL2023.12 version:** 2.7.2-12.amzn2023.0.4

- ** `Xaw3d` **
  - **RPM:**  Xaw3d  / **Architectures:** aarch64, x86\_64
  - **RPM:**  Xaw3d-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.2-12.amzn2.0.1
  - **AL2023.12 version:** 1.6.3-5.amzn2023.0.3

- ** `xbean` **
  - **RPM:**  xbean  / **Architectures:** noarch
  - **RPM:**  xbean-javadoc  / **Architectures:** noarch
  - **AL2 version:** 3.13-6.amzn2
  - **AL2023.12 version:** 4.18-7.amzn2023.0.3

- ** `xcb-proto` **
  - **RPM:**  xcb-proto
  - **Architectures:** noarch
  - **AL2 version:** 1.13-1.amzn2
  - **AL2023.12 version:** 1.17.0-1.amzn2023.0.2

- ** `xcb-util` **
  - **RPM:**  xcb-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.0-2.amzn2.0.2
  - **AL2023.12 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-image` **
  - **RPM:**  xcb-util-image  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-image-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.0-2.amzn2.0.2
  - **AL2023.12 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-keysyms` **
  - **RPM:**  xcb-util-keysyms  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-keysyms-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.0-1.amzn2.0.2
  - **AL2023.12 version:** 0.4.1-5.amzn2023.0.1

- ** `xcb-util-renderutil` **
  - **RPM:**  xcb-util-renderutil  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-renderutil-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.9-3.amzn2.0.2
  - **AL2023.12 version:** 0.3.10-5.amzn2023.0.1

- ** `xcb-util-wm` **
  - **RPM:**  xcb-util-wm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xcb-util-wm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.4.1-5.amzn2.0.2
  - **AL2023.12 version:** 0.4.2-5.amzn2023.0.1

- ** `xdg-desktop-portal` **
  - **RPM:**  xdg-desktop-portal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xdg-desktop-portal-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-1.amzn2.0.3
  - **AL2023.12 version:** 1.18.4-107.amzn2023

- ** `xdg-desktop-portal-gtk` **
  - **RPM:**  xdg-desktop-portal-gtk
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.2-1.amzn2
  - **AL2023.12 version:** 1.15.1-61.amzn2023

- ** `xdg-user-dirs` **
  - **RPM:**  xdg-user-dirs
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.15-5.amzn2.0.1
  - **AL2023.12 version:** 0.18-4.amzn2023.0.1

- ** `xdg-user-dirs-gtk` **
  - **RPM:**  xdg-user-dirs-gtk
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.10-4.amzn2.0.2
  - **AL2023.12 version:** 0.11-5.amzn2023.0.1

- ** `xdg-utils` **
  - **RPM:**  xdg-utils
  - **Architectures:** noarch
  - **AL2 version:** 1.1.0-0.17.20120809git.amzn2.0.1
  - **AL2023.12 version:** 1.2.1-1.amzn2023.0.1

- ** `xerces-j2` **
  - **RPM:**  xerces-j2  / **Architectures:** noarch
  - **RPM:**  xerces-j2-demo  / **Architectures:** noarch
  - **RPM:**  xerces-j2-javadoc  / **Architectures:** noarch
  - **AL2 version:** 2.11.0-17.amzn2.0.2
  - **AL2023.12 version:** 2.12.1-7.amzn2023.0.2

- ** `xfsdump` **
  - **RPM:**  xfsdump
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.1.8-6.amzn2
  - **AL2023.12 version:** 3.1.11-2.amzn2023.0.2

- ** `xfsprogs` **
  - **RPM:**  xfsprogs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xfsprogs-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.0.0-10.amzn2.0.1
  - **AL2023.12 version:** 6.12.0-3.amzn2023.0.1

- ** `xhtml1-dtds` **
  - **RPM:**  xhtml1-dtds
  - **Architectures:** noarch
  - **AL2 version:** 1.0-20020801.11.amzn2
  - **AL2023.12 version:** 1.0-20020801.15.amzn2023.0.2

- ** `xhtml2fo-style-xsl` **
  - **RPM:**  xhtml2fo-style-xsl
  - **Architectures:** noarch
  - **AL2 version:** 20051222-9.amzn2
  - **AL2023.12 version:** 20051222-24.amzn2023.0.2

- ** `xkeyboard-config` **
  - **RPM:**  xkeyboard-config  / **Architectures:** noarch
  - **RPM:**  xkeyboard-config-devel  / **Architectures:** noarch
  - **AL2 version:** 2.20-1.amzn2
  - **AL2023.12 version:** 2.41-1.amzn2023.0.1

- ** `xml-commons-apis` **
  - **RPM:**  xml-commons-apis  / **Architectures:** noarch
  - **RPM:**  xml-commons-apis-javadoc  / **Architectures:** noarch
  - **RPM:**  xml-commons-apis-manual  / **Architectures:** noarch
  - **AL2 version:** 1.4.01-16.amzn2
  - **AL2023.12 version:** 1.4.01-38.amzn2023.0.1

- ** `xml-commons-resolver` **
  - **RPM:**  xml-commons-resolver  / **Architectures:** noarch
  - **RPM:**  xml-commons-resolver-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.2-15.amzn2
  - **AL2023.12 version:** 1.2-37.amzn2023.0.1

- ** `xmlgraphics-commons` **
  - **RPM:**  xmlgraphics-commons  / **Architectures:** noarch
  - **RPM:**  xmlgraphics-commons-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.5-3.amzn2.0.2
  - **AL2023.12 version:** 2.7-2.amzn2023.0.3

- ** `xmlrpc-c` **
  - **RPM:**  xmlrpc-c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlrpc-c-apps  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlrpc-c-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlrpc-c-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlrpc-c-client\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlrpc-c-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.32.5-1905.svn2451.amzn2.0.2
  - **AL2023.12 version:** 1.51.08-2.amzn2023.0.2

- ** `xmlsec1` **
  - **RPM:**  xmlsec1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlsec1-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlsec1-openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlsec1-openssl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.20-7.amzn2.0.1
  - **AL2023.12 version:** 1.2.33-3.amzn2023.0.2

- ** `xmlto` **
  - **RPM:**  xmlto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xmlto-tex  / **Architectures:** noarch
  - **RPM:**  xmlto-xhtml  / **Architectures:** noarch
  - **AL2 version:** 0.0.25-7.amzn2.0.2
  - **AL2023.12 version:** 0.0.28-15.amzn2023.0.2

- ** `xmltoman` **
  - **RPM:**  xmltoman
  - **Architectures:** noarch
  - **AL2 version:** 0.4-9.amzn2
  - **AL2023.12 version:** 0.4-23.amzn2023.0.2

- ** `xmlunit` **
  - **RPM:**  xmlunit  / **Architectures:** noarch
  - **RPM:**  xmlunit-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.4-6.amzn2
  - **AL2023.12 version:** 2.8.2-6.amzn2023.0.4

- ** `xmvn` **
  - **RPM:**  xmvn  / **Architectures:** noarch
  - **RPM:**  xmvn-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.3.0-6.amzn2
  - **AL2023.12 version:** 4.0.0-8.amzn2023.0.3

- ** `xorg-x11-drv-dummy` **
  - **RPM:**  xorg-x11-drv-dummy
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.3.7-1.2.amzn2.0.2
  - **AL2023.12 version:** 0.4.1-2.amzn2023.0.1

- ** `xorg-x11-drv-libinput` **
  - **RPM:**  xorg-x11-drv-libinput  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-drv-libinput-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.27.1-2.amzn2.0.1
  - **AL2023.12 version:** 1.4.0-2.amzn2023.0.1

- ** `xorg-x11-fonts` **
  - **RPM:**  xorg-x11-fonts-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-cyrillic  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ethiopic  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-1-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-14-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-14-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-15-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-15-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-1-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-2-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-2-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-9-100dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-ISO8859-9-75dpi  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-misc  / **Architectures:** noarch
  - **RPM:**  xorg-x11-fonts-Type1  / **Architectures:** noarch
  - **AL2 version:** 7.5-9.amzn2
  - **AL2023.12 version:** 7.5-38.amzn2023.0.1

- ** `xorg-x11-font-utils` **
  - **RPM:**  xorg-x11-font-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.5-21.amzn2
  - **AL2023.12 version:** 7.5-59.amzn2023.0.1

- ** `xorg-x11-proto-devel` **
  - **RPM:**  xorg-x11-proto-devel
  - **Architectures:** noarch
  - **AL2 version:** 2018.4-1.amzn2.0.2
  - **AL2023.12 version:** 2024.1-2.amzn2023.0.2

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.20.4-22.amzn2.0.13
  - **AL2023.12 version:** 21.1.13-5.amzn2023.0.11

- ** `xorg-x11-server-utils` **
  - **RPM:**  xorg-x11-server-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.7-20.amzn2.0.2
  - **AL2023.12 version:** 7.7-39.amzn2023.0.2

- ** `xorg-x11-util-macros` **
  - **RPM:**  xorg-x11-util-macros
  - **Architectures:** noarch
  - **AL2 version:** 1.19.0-3.amzn2
  - **AL2023.12 version:** 1.20.0-4.amzn2023.0.1

- ** `xorg-x11-utils` **
  - **RPM:**  xorg-x11-utils
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 7.5-23.amzn2
  - **AL2023.12 version:** 7.5-38.amzn2023.0.2

- ** `xorg-x11-xauth` **
  - **RPM:**  xorg-x11-xauth
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.9-1.amzn2.0.2
  - **AL2023.12 version:** 1.1.2-6.amzn2023.0.1

- ** `xorg-x11-xbitmaps` **
  - **RPM:**  xorg-x11-xbitmaps
  - **Architectures:** noarch
  - **AL2 version:** 1.1.1-6.amzn2
  - **AL2023.12 version:** 1.1.3-2.amzn2023.0.1

- ** `xorg-x11-xinit` **
  - **RPM:**  xorg-x11-xinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-xinit-session  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.4-2.amzn2
  - **AL2023.12 version:** 1.4.2-2.amzn2023.0.1

- ** `xorg-x11-xtrans-devel` **
  - **RPM:**  xorg-x11-xtrans-devel
  - **Architectures:** noarch
  - **AL2 version:** 1.3.5-1.amzn2
  - **AL2023.12 version:** 1.4.0-13.amzn2023.0.1

- ** `xterm` **
  - **RPM:**  xterm
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 295-3.amzn2.1
  - **AL2023.12 version:** 394-1.amzn2023.0.1

- ** `xz` **
  - **RPM:**  xz  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xz-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xz-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xz-lzma-compat  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.2.2-1.amzn2.0.3
  - **AL2023.12 version:** 5.2.5-9.amzn2023.0.2

- ** `xz-java` **
  - **RPM:**  xz-java  / **Architectures:** noarch
  - **RPM:**  xz-java-javadoc  / **Architectures:** noarch
  - **AL2 version:** 1.3-3.amzn2
  - **AL2023.12 version:** 1.9-3.amzn2023.0.3

- ** `yajl` **
  - **RPM:**  yajl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yajl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.4-4.amzn2.0.3
  - **AL2023.12 version:** 2.1.0-16.amzn2023.0.5

- ** `yelp-tools` **
  - **RPM:**  yelp-tools
  - **Architectures:** noarch
  - **AL2 version:** 3.28.0-1.amzn2
  - **AL2023.12 version:** 42.1-6.amzn2023.0.2

- ** `yelp-xsl` **
  - **RPM:**  yelp-xsl  / **Architectures:** noarch
  - **RPM:**  yelp-xsl-devel  / **Architectures:** noarch
  - **AL2 version:** 3.28.0-1.amzn2.0.1
  - **AL2023.12 version:** 42.1-5.amzn2023.0.1

- ** `zenity` **
  - **RPM:**  zenity
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.28.1-1.amzn2
  - **AL2023.12 version:** 4.0.5-1.amzn2023

- ** `zip` **
  - **RPM:**  zip
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0-11.amzn2.0.2
  - **AL2023.12 version:** 3.0-28.amzn2023.0.3

- ** `zlib` **
  - **RPM:**  zlib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zlib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zlib-static  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.7-19.amzn2.0.3
  - **AL2023.12 version:** 1.2.11-33.amzn2023.0.6

- ** `zsh` **
  - **RPM:**  zsh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zsh-html  / **Architectures:** noarch
  - **AL2 version:** 5.8.1-1.amzn2.0.1
  - **AL2023.12 version:** 5.9-12.amzn2023

- ** `zstd` **
  - **RPM:**  libzstd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzstd-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zstd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.5.5-1.amzn2.0.1
  - **AL2023.12 version:** 1.5.5-1.amzn2023.0.1

- ** `zziplib` **
  - **RPM:**  zziplib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zziplib-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  zziplib-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.13.62-12.amzn2.0.2
  - **AL2023.12 version:** 0.13.78-1.amzn2023

## awscli1 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-awscli1"></a>

- ** `awscli-2` (`awscli` in AL2) **
  - **RPM:**  awscli-2 (awscli in AL2)
  - **Architectures:**
  - **AL2 version:** 1.27.51-1.amzn2.0.1
  - **AL2023.12 version:** 2.33.15-1.amzn2023.0.1

- ** `pyproject-rpm-macros` **
  - **RPM:**  pyproject-rpm-macros
  - **Architectures:** noarch
  - **AL2 version:** 0-36.amzn2.0.1
  - **AL2023.12 version:** 1.16.1-1.amzn2023.0.1

- ** `python-botocore` (`python3-botocore` in AL2) **
  - **RPM:**  python3-botocore
  - **Architectures:** noarch
  - **AL2 version:** 1.29.51-1.amzn2.0.2
  - **AL2023.12 version:** 1.40.31-1.amzn2023.0.1

- ** `python-s3transfer` **
  - **RPM:**  python3-s3transfer
  - **Architectures:** noarch
  - **AL2 version:** 0.6.0-1.amzn2.0.2
  - **AL2023.12 version:** 0.14.0-1.amzn2023.0.1

## BCC AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-BCC"></a>

- ** `bcc` **
  - **RPM:**  bcc  / **Architectures:**
  - **RPM:**  bcc-devel  / **Architectures:**
  - **RPM:**  bcc-doc  / **Architectures:**
  - **RPM:**  bcc-tools  / **Architectures:**
  - **AL2 version:** 0.10.0-1.amzn2.0.1
  - **AL2023.12 version:** 0.35.0-4.amzn2023.0.2

- ** `luajit` **
  - **RPM:**  luajit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  luajit-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.0-0.9beta3.amzn2
  - **AL2023.12 version:** 2.1.0-0.19beta3.amzn2023.0.2

## selinux-ng AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-selinux-ng"></a>

- ** `checkpolicy` **
  - **RPM:**  checkpolicy
  - **Architectures:**
  - **AL2 version:** 2.5-8.amzn2
  - **AL2023.12 version:** 3.4-3.amzn2023.0.2

- ** `container-selinux` **
  - **RPM:**  container-selinux
  - **Architectures:** noarch
  - **AL2 version:** 2.120.0-1.911c772.amzn2
  - **AL2023.12 version:** 2.245.0-1.amzn2023

- ** `libselinux` **
  - **RPM:**  libselinux  / **Architectures:**
  - **RPM:**  libselinux-devel  / **Architectures:**
  - **RPM:**  libselinux-static  / **Architectures:**
  - **RPM:**  libselinux-utils  / **Architectures:**
  - **AL2 version:** 2.5-15.amzn2.0.1
  - **AL2023.12 version:** 3.4-5.amzn2023.0.2

- ** `libsemanage` **
  - **RPM:**  libsemanage  / **Architectures:**
  - **RPM:**  libsemanage-devel  / **Architectures:**
  - **RPM:**  libsemanage-static  / **Architectures:**
  - **AL2 version:** 2.5-14.amzn2
  - **AL2023.12 version:** 3.4-5.amzn2023.0.2

- ** `policycoreutils` **
  - **RPM:**  policycoreutils  / **Architectures:**
  - **RPM:**  policycoreutils-devel  / **Architectures:**
  - **RPM:**  policycoreutils-newrole  / **Architectures:**
  - **RPM:**  policycoreutils-restorecond  / **Architectures:**
  - **AL2 version:** 2.5-34.amzn2
  - **AL2023.12 version:** 3.4-6.amzn2023.0.3

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:**
  - **RPM:**  selinux-policy-devel  / **Architectures:**
  - **RPM:**  selinux-policy-doc  / **Architectures:**
  - **RPM:**  selinux-policy-minimum  / **Architectures:**
  - **RPM:**  selinux-policy-mls  / **Architectures:**
  - **RPM:**  selinux-policy-sandbox  / **Architectures:**
  - **RPM:**  selinux-policy-targeted  / **Architectures:**
  - **AL2 version:** 3.13.1-268.amzn2.2.2
  - **AL2023.12 version:** 38.1.76-1.amzn2023.0.2

- ** `setools` **
  - **RPM:**  setools  / **Architectures:**
  - **RPM:**  setools-console  / **Architectures:**
  - **AL2 version:** 3.3.8-4.amzn2.0.1
  - **AL2023.12 version:** 4.4.1-1.amzn2023

## ruby2.4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-ruby2.4"></a>

- ** `checksec` **
  - **RPM:**  checksec
  - **Architectures:**
  - **AL2 version:** 1.7.4-4.amzn2.0.1
  - **AL2023.12 version:** 2.4.0-2.amzn2023.0.2

- ** `ruby3.2` (`ruby` in AL2) **
  - **RPM:**  ruby3.2 (ruby in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-devel (ruby-devel in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-doc (ruby-doc in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-libs (ruby-libs in AL2)  / **Architectures:**
  - **AL2 version:** 2.4.7-1.amzn2.0.1
  - **AL2023.12 version:** 3.2.8-184.amzn2023.0.6

## rust1 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-rust1"></a>

- ** `cmake` (`cmake3` in AL2) **
  - **RPM:**  cmake (cmake3 in AL2)  / **Architectures:**
  - **RPM:**  cmake-data (cmake3-data in AL2)  / **Architectures:**
  - **RPM:**  cmake-doc (cmake3-doc in AL2)  / **Architectures:**
  - **AL2 version:** 3.6.3-1.amzn2.0.1
  - **AL2023.12 version:** 3.22.2-1.amzn2023.0.6

- ** `jsoncpp` **
  - **RPM:**  jsoncpp  / **Architectures:**
  - **RPM:**  jsoncpp-devel  / **Architectures:**
  - **RPM:**  jsoncpp-doc  / **Architectures:**
  - **AL2 version:** 0.10.5-2.amzn2.0.1
  - **AL2023.12 version:** 1.9.4-3.amzn2023.0.2

- ** `libgit2` **
  - **RPM:**  libgit2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgit2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.28.4-1.amzn2.0.1
  - **AL2023.12 version:** 1.6.4-115.amzn2023.0.2

- ** [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (`llvm3.9` in AL2) **
  - **RPM:**  [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (llvm3.9 in AL2)  / **Architectures:**
  - **RPM:**  llvm-devel (llvm3.9-devel in AL2)  / **Architectures:**
  - **RPM:**  llvm-libs (llvm3.9-libs in AL2)  / **Architectures:**
  - **RPM:**  llvm-static (llvm3.9-static in AL2)  / **Architectures:**
  - **AL2 version:** 3.9.1-7.amzn2.0.1
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.1

- ** [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (`llvm5.0` in AL2) **
  - **RPM:**  [`llvm`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) (llvm5.0 in AL2)  / **Architectures:**
  - **RPM:**  llvm-devel (llvm5.0-devel in AL2)  / **Architectures:**
  - **RPM:**  llvm-doc (llvm5.0-doc in AL2)  / **Architectures:**
  - **RPM:**  llvm-libs (llvm5.0-libs in AL2)  / **Architectures:**
  - **RPM:**  llvm-static (llvm5.0-static in AL2)  / **Architectures:**
  - **AL2 version:** 5.0.1-7.amzn2.0.1
  - **AL2023.12 version:** 15.0.7-3.amzn2023.0.1

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:**
  - **RPM:**  clippy  / **Architectures:**
  - **RPM:**  [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:**
  - **RPM:**  rust-analysis  / **Architectures:**
  - **RPM:**  rust-debugger-common  / **Architectures:**
  - **RPM:**  rust-doc  / **Architectures:**
  - **RPM:**  rustfmt  / **Architectures:**
  - **RPM:**  rust-gdb  / **Architectures:**
  - **RPM:**  rust-src  / **Architectures:**
  - **RPM:**  rust-std-static  / **Architectures:**
  - **AL2 version:** 1.47.0-1.amzn2.0.1
  - **AL2023.12 version:** 1.97.0-2.amzn2023

## dnsmasq AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-dnsmasq"></a>

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:**
  - **RPM:**  dnsmasq-utils  / **Architectures:**
  - **AL2 version:** 2.90-1.amzn2.0.3
  - **AL2023.12 version:** 2.90-1.amzn2023.0.3

## dnsmasq2.85 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-dnsmasq2.85"></a>

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:**
  - **RPM:**  dnsmasq-utils  / **Architectures:**
  - **AL2 version:** 2.85-1.amzn2.0.3
  - **AL2023.12 version:** 2.90-1.amzn2023.0.3

## golang1.11 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-golang1.11"></a>

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:**
  - **RPM:**  golang-bin  / **Architectures:**
  - **RPM:**  golang-docs  / **Architectures:**
  - **RPM:**  golang-misc  / **Architectures:**
  - **RPM:**  golang-race  / **Architectures:**
  - **RPM:**  golang-shared  / **Architectures:**
  - **RPM:**  golang-src  / **Architectures:**
  - **RPM:**  golang-tests  / **Architectures:**
  - **AL2 version:** 1.11.13-2.amzn2.0.1
  - **AL2023.12 version:** 1.25.12-1.amzn2023.0.1

## golang1.19 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-golang1.19"></a>

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:**
  - **RPM:**  golang-bin  / **Architectures:**
  - **RPM:**  golang-docs  / **Architectures:**
  - **RPM:**  golang-misc  / **Architectures:**
  - **RPM:**  golang-race  / **Architectures:**
  - **RPM:**  golang-shared  / **Architectures:**
  - **RPM:**  golang-src  / **Architectures:**
  - **RPM:**  golang-tests  / **Architectures:**
  - **AL2 version:** 1.19.10-1.amzn2.0.2
  - **AL2023.12 version:** 1.25.12-1.amzn2023.0.1

## kernel-5.10 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-kernel-5.10"></a>

- ** `iproute` **
  - **RPM:**  iproute  / **Architectures:**
  - **RPM:**  iproute-devel  / **Architectures:**
  - **RPM:**  iproute-tc  / **Architectures:**
  - **AL2 version:** 5.10.0-2.amzn2.0.2
  - **AL2023.12 version:** 6.10.0-319.amzn2023.0.1

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:**
  - **RPM:**  kernel-devel  / **Architectures:**
  - **RPM:**  kernel-headers  / **Architectures:**
  - **RPM:**  kernel-tools  / **Architectures:**
  - **RPM:**  kernel-tools-devel  / **Architectures:**
  - **RPM:**  perf  / **Architectures:**
  - **AL2 version:** 5.10.262-262.1063.amzn2
  - **AL2023.12 version:** 6.1.180-225.360.amzn2023

## kernel-5.15 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-kernel-5.15"></a>

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:**
  - **RPM:**  kernel  / **Architectures:**
  - **RPM:**  kernel-devel  / **Architectures:**
  - **RPM:**  kernel-headers  / **Architectures:**
  - **RPM:**  kernel-tools  / **Architectures:**
  - **RPM:**  kernel-tools-devel  / **Architectures:**
  - **RPM:**  perf  / **Architectures:**
  - **AL2 version:** 5.15.213-150.251.amzn2
  - **AL2023.12 version:** 6.1.180-225.360.amzn2023

## kernel-5.4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-kernel-5.4"></a>

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:**
  - **RPM:**  kernel  / **Architectures:**
  - **RPM:**  kernel-devel  / **Architectures:**
  - **RPM:**  kernel-headers  / **Architectures:**
  - **RPM:**  kernel-tools  / **Architectures:**
  - **RPM:**  kernel-tools-devel  / **Architectures:**
  - **RPM:**  perf  / **Architectures:**
  - **AL2 version:** 5.4.302-226.485.amzn2
  - **AL2023.12 version:** 6.1.180-225.360.amzn2023

## kernel-ng AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-kernel-ng"></a>

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:**
  - **RPM:**  kernel  / **Architectures:**
  - **RPM:**  kernel-devel  / **Architectures:**
  - **RPM:**  kernel-headers  / **Architectures:**
  - **RPM:**  kernel-tools  / **Architectures:**
  - **RPM:**  kernel-tools-devel  / **Architectures:**
  - **RPM:**  perf  / **Architectures:**
  - **AL2 version:** 5.10.130-118.517.amzn2
  - **AL2023.12 version:** 6.1.180-225.360.amzn2023

## mate-desktop1.x AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-mate-desktop1.x"></a>

- ** `fdupes` **
  - **RPM:**  fdupes
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.3.0-1.amzn2
  - **AL2023.12 version:** 2.3.0-1.amzn2023

- ** `libdbusmenu` **
  - **RPM:**  libdbusmenu  / **Architectures:**
  - **RPM:**  libdbusmenu-devel  / **Architectures:**
  - **RPM:**  libdbusmenu-doc  / **Architectures:**
  - **RPM:**  libdbusmenu-gtk3  / **Architectures:**
  - **RPM:**  libdbusmenu-gtk3-devel  / **Architectures:**
  - **RPM:**  libdbusmenu-jsonloader  / **Architectures:**
  - **RPM:**  libdbusmenu-jsonloader-devel  / **Architectures:**
  - **RPM:**  libdbusmenu-tools  / **Architectures:**
  - **AL2 version:** 16.04.0-16.amzn2
  - **AL2023.12 version:** 16.04.0-27.amzn2023.0.1

- ** `libXpresent` **
  - **RPM:**  libXpresent  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libXpresent-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.0-12.amzn2
  - **AL2023.12 version:** 1.0.0-27.amzn2023

## php7.2 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php7.2"></a>

- ** `libsodium` **
  - **RPM:**  libsodium  / **Architectures:**
  - **RPM:**  libsodium-devel  / **Architectures:**
  - **RPM:**  libsodium-static  / **Architectures:**
  - **AL2 version:** 1.0.18-2.amzn2
  - **AL2023.12 version:** 1.0.19-5.amzn2023

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 7.2.34-1.amzn2
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

- ** `php8.2-pecl-apcu` (`php-pecl-apcu` in AL2) **
  - **RPM:**  php8.2-pecl-apcu (php-pecl-apcu in AL2)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.1.12-3.amzn2.0.1
  - **AL2023.12 version:** 5.1.24-3.amzn2023.0.1

- ** `php8.2-pecl-igbinary` (`php-pecl-igbinary` in AL2) **
  - **RPM:**  php8.2-pecl-igbinary (php-pecl-igbinary in AL2)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.7-3.amzn2.0.1
  - **AL2023.12 version:** 3.2.16-4.amzn2023.0.1

- ** `php8.2-pecl-memcached` (`php-pecl-memcached` in AL2) **
  - **RPM:**  php8.2-pecl-memcached (php-pecl-memcached in AL2)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.0.4-3.amzn2.0.1
  - **AL2023.12 version:** 3.4.0-1.amzn2023.0.1

- ** `php8.2-pecl-msgpack` (`php-pecl-msgpack` in AL2) **
  - **RPM:**  php8.2-pecl-msgpack (php-pecl-msgpack in AL2)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.2-3.amzn2.0.1
  - **AL2023.12 version:** 3.0.0-3.amzn2023.0.1

- ** `php8.2-pecl-redis6` (`php-pecl-redis` in AL2) **
  - **RPM:**  php8.2-pecl-redis6 (php-pecl-redis in AL2)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 4.3.0-1.amzn2
  - **AL2023.12 version:** 6.2.0-1.amzn2023.0.1

## lamp-mariadb10.2-php7.2 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-lamp-mariadb10.2-php7.2"></a>

- ** `jemalloc` **
  - **RPM:**  jemalloc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jemalloc-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.6.0-1.amzn2.0.1
  - **AL2023.12 version:** 5.2.1-7.amzn2023

- ** `Judy` **
  - **RPM:**  Judy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  Judy-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.0.5-8.amzn2.0.1
  - **AL2023.12 version:** 1.0.5-25.amzn2023.0.3

- ** `mariadb105` (`mariadb` in AL2) **
  - **RPM:**  mariadb105 (mariadb in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-backup (mariadb-backup in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-common (mariadb-common in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-connect-engine (mariadb-connect-engine in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-cracklib-password-check (mariadb-cracklib-password-check in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-devel (mariadb-devel in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-errmsg (mariadb-errmsg in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-gssapi-server (mariadb-gssapi-server in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-oqgraph-engine (mariadb-oqgraph-engine in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-rocksdb-engine (mariadb-rocksdb-engine in AL2)  / **Architectures:** x86\_64
  - **RPM:**  mariadb105-server (mariadb-server in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-server-utils (mariadb-server-utils in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-sphinx-engine (mariadb-sphinx-engine in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-test (mariadb-test in AL2)  / **Architectures:**
  - **AL2 version:** 10.2.38-1.amzn2.0.1
  - **AL2023.12 version:** 10.5.29-1.amzn2023.0.1

- ** `perl-generators` **
  - **RPM:**  perl-generators
  - **Architectures:** noarch
  - **AL2 version:** 1.08-6.amzn2
  - **AL2023.12 version:** 1.13-1.amzn2023.0.2

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 7.2.24-1.amzn2.0.1
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

- ** `sphinx` **
  - **RPM:**  libsphinxclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsphinxclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sphinx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sphinx-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sphinx-php  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.2.11-5.amzn2.0.1
  - **AL2023.12 version:** 2.2.11-24.amzn2023.0.4

## mariadb10.5 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-mariadb10.5"></a>

- ** `mariadb105` (`mariadb` in AL2) **
  - **RPM:**  mariadb105 (mariadb in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-backup (mariadb-backup in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-common (mariadb-common in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-connect-engine (mariadb-connect-engine in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-cracklib-password-check (mariadb-cracklib-password-check in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-devel (mariadb-devel in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-errmsg (mariadb-errmsg in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-gssapi-server (mariadb-gssapi-server in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-oqgraph-engine (mariadb-oqgraph-engine in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-pam (mariadb-pam in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb105-rocksdb-engine (mariadb-rocksdb-engine in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-server (mariadb-server in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-server-utils (mariadb-server-utils in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-sphinx-engine (mariadb-sphinx-engine in AL2)  / **Architectures:**
  - **RPM:**  mariadb105-test (mariadb-test in AL2)  / **Architectures:**
  - **AL2 version:** 10.5.29-1.amzn2.0.1
  - **AL2023.12 version:** 10.5.29-1.amzn2023.0.1

## php7.3 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php7.3"></a>

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 7.3.33-2.amzn2
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

- ** `php8.2-pecl-apcu` (`php-pecl-apcu` in AL2) **
  - **RPM:**  php8.2-pecl-apcu (php-pecl-apcu in AL2)
  - **Architectures:**
  - **AL2 version:** 5.1.12-3.amzn2.0.2
  - **AL2023.12 version:** 5.1.24-3.amzn2023.0.1

- ** `php8.2-pecl-igbinary` (`php-pecl-igbinary` in AL2) **
  - **RPM:**  php8.2-pecl-igbinary (php-pecl-igbinary in AL2)
  - **Architectures:**
  - **AL2 version:** 2.0.7-3.amzn2.0.2
  - **AL2023.12 version:** 3.2.16-4.amzn2023.0.1

- ** `php8.2-pecl-memcached` (`php-pecl-memcached` in AL2) **
  - **RPM:**  php8.2-pecl-memcached (php-pecl-memcached in AL2)
  - **Architectures:**
  - **AL2 version:** 3.1.3-1.amzn2
  - **AL2023.12 version:** 3.4.0-1.amzn2023.0.1

- ** `php8.2-pecl-msgpack` (`php-pecl-msgpack` in AL2) **
  - **RPM:**  php8.2-pecl-msgpack (php-pecl-msgpack in AL2)
  - **Architectures:**
  - **AL2 version:** 2.0.3-1.amzn2
  - **AL2023.12 version:** 3.0.0-3.amzn2023.0.1

- ** `php8.2-pecl-redis6` (`php-pecl-redis` in AL2) **
  - **RPM:**  php8.2-pecl-redis6 (php-pecl-redis in AL2)
  - **Architectures:**
  - **AL2 version:** 4.3.0-1.amzn2.0.1
  - **AL2023.12 version:** 6.2.0-1.amzn2023.0.1

## php7.4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php7.4"></a>

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 7.4.33-1.amzn2
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

- ** `php8.2-pecl-apcu` (`php-pecl-apcu` in AL2) **
  - **RPM:**  php8.2-pecl-apcu (php-pecl-apcu in AL2)
  - **Architectures:**
  - **AL2 version:** 5.1.18-1.amzn2
  - **AL2023.12 version:** 5.1.24-3.amzn2023.0.1

- ** `php8.2-pecl-igbinary` (`php-pecl-igbinary` in AL2) **
  - **RPM:**  php8.2-pecl-igbinary (php-pecl-igbinary in AL2)
  - **Architectures:**
  - **AL2 version:** 3.1.2-1.amzn2
  - **AL2023.12 version:** 3.2.16-4.amzn2023.0.1

- ** `php8.2-pecl-memcached` (`php-pecl-memcached` in AL2) **
  - **RPM:**  php8.2-pecl-memcached (php-pecl-memcached in AL2)
  - **Architectures:**
  - **AL2 version:** 3.1.5-1.amzn2
  - **AL2023.12 version:** 3.4.0-1.amzn2023.0.1

- ** `php8.2-pecl-msgpack` (`php-pecl-msgpack` in AL2) **
  - **RPM:**  php8.2-pecl-msgpack (php-pecl-msgpack in AL2)
  - **Architectures:**
  - **AL2 version:** 2.1.0-1.amzn2
  - **AL2023.12 version:** 3.0.0-3.amzn2023.0.1

- ** `php8.2-pecl-redis6` (`php-pecl-redis` in AL2) **
  - **RPM:**  php8.2-pecl-redis6 (php-pecl-redis in AL2)
  - **Architectures:**
  - **AL2 version:** 5.2.1-1.amzn2
  - **AL2023.12 version:** 6.2.0-1.amzn2023.0.1

## php8.0 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php8.0"></a>

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 8.0.30-1.amzn2
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

## php8.1 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php8.1"></a>

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 8.1.34-1.amzn2
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

## php8.2 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-php8.2"></a>

- ** [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (`php` in AL2) **
  - **RPM:**  [`php8.2`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) (php in AL2)  / **Architectures:**
  - **RPM:**  php8.2-bcmath (php-bcmath in AL2)  / **Architectures:**
  - **RPM:**  php8.2-cli (php-cli in AL2)  / **Architectures:**
  - **RPM:**  php8.2-common (php-common in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dba (php-dba in AL2)  / **Architectures:**
  - **RPM:**  php8.2-dbg (php-dbg in AL2)  / **Architectures:**
  - **RPM:**  php8.2-devel (php-devel in AL2)  / **Architectures:**
  - **RPM:**  php8.2-embedded (php-embedded in AL2)  / **Architectures:**
  - **RPM:**  php8.2-enchant (php-enchant in AL2)  / **Architectures:**
  - **RPM:**  php8.2-fpm (php-fpm in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gd (php-gd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-gmp (php-gmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-intl (php-intl in AL2)  / **Architectures:**
  - **RPM:**  php8.2-ldap (php-ldap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mbstring (php-mbstring in AL2)  / **Architectures:**
  - **RPM:**  php8.2-mysqlnd (php-mysqlnd in AL2)  / **Architectures:**
  - **RPM:**  php8.2-odbc (php-odbc in AL2)  / **Architectures:**
  - **RPM:**  php8.2-opcache (php-opcache in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pdo (php-pdo in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pgsql (php-pgsql in AL2)  / **Architectures:**
  - **RPM:**  php8.2-process (php-process in AL2)  / **Architectures:**
  - **RPM:**  php8.2-pspell (php-pspell in AL2)  / **Architectures:**
  - **RPM:**  php8.2-snmp (php-snmp in AL2)  / **Architectures:**
  - **RPM:**  php8.2-soap (php-soap in AL2)  / **Architectures:**
  - **RPM:**  php8.2-sodium (php-sodium in AL2)  / **Architectures:**
  - **RPM:**  php8.2-xml (php-xml in AL2)  / **Architectures:**
  - **AL2 version:** 8.2.33-1.amzn2.0.1
  - **AL2023.12 version:** 8.2.33-1.amzn2023.0.1

## postgresql10 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql10"></a>

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 10.21-1.amzn2.0.1
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## postgresql11 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql11"></a>

- ** `libecpg` **
  - **RPM:**  libecpg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libecpg-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpgtypes  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.2-2.amzn2
  - **AL2023.12 version:** 16.1-2.amzn2023

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 11.5-1.amzn2
  - **AL2023.12 version:** 18.4-1.amzn2023.0.1

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server-devel (postgresql-server-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test-rpm-macros (postgresql-test-rpm-macros in AL2)  / **Architectures:** noarch
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:**
  - **AL2 version:** 11.20-1.amzn2.0.2
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## postgresql12 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql12"></a>

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:**
  - **RPM:**  libpq-devel  / **Architectures:**
  - **AL2 version:** 12.20-1.amzn2.0.1
  - **AL2023.12 version:** 18.4-1.amzn2023.0.1

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-llvmjit (postgresql-llvmjit in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server-devel (postgresql-server-devel in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test-rpm-macros (postgresql-test-rpm-macros in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:**
  - **AL2 version:** 12.20-1.amzn2.0.1
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## postgresql13 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql13"></a>

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:**
  - **RPM:**  libpq-devel  / **Architectures:**
  - **AL2 version:** 13.22-1.amzn2.0.1
  - **AL2023.12 version:** 18.4-1.amzn2023.0.1

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-llvmjit (postgresql-llvmjit in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-private-devel (postgresql-private-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-libs (postgresql-private-libs in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server-devel (postgresql-server-devel in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test-rpm-macros (postgresql-test-rpm-macros in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:**
  - **AL2 version:** 13.22-1.amzn2.0.1
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## postgresql14 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql14"></a>

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:**
  - **RPM:**  libpq-devel  / **Architectures:**
  - **AL2 version:** 14.23-1.amzn2.0.1
  - **AL2023.12 version:** 18.4-1.amzn2023.0.1

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-llvmjit (postgresql-llvmjit in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server-devel (postgresql-server-devel in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test-rpm-macros (postgresql-test-rpm-macros in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:**
  - **AL2 version:** 14.23-1.amzn2.0.1
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## postgresql9.6 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-postgresql9.6"></a>

- ** `postgresql15` (`postgresql` in AL2) **
  - **RPM:**  postgresql15 (postgresql in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-contrib (postgresql-contrib in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-docs (postgresql-docs in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plperl (postgresql-plperl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-plpython3 (postgresql-plpython3 in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-pltcl (postgresql-pltcl in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-server (postgresql-server in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-static (postgresql-static in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-test (postgresql-test in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade (postgresql-upgrade in AL2)  / **Architectures:**
  - **RPM:**  postgresql15-upgrade-devel (postgresql-upgrade-devel in AL2)  / **Architectures:**
  - **AL2 version:** 9.6.22-1.amzn2.0.1
  - **AL2023.12 version:** 15.18-1.amzn2023.0.1

## mock2 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-mock2"></a>

- ** `distribution-gpg-keys` **
  - **RPM:**  distribution-gpg-keys  / **Architectures:** noarch
  - **RPM:**  distribution-gpg-keys-copr  / **Architectures:** noarch
  - **AL2 version:** 1.100-1.amzn2
  - **AL2023.12 version:** 1.104-1.amzn2023.0.1

- ** `dnf` **
  - **RPM:**  dnf  / **Architectures:**
  - **RPM:**  dnf-automatic  / **Architectures:** noarch
  - **RPM:**  dnf-data  / **Architectures:** noarch
  - **AL2 version:** 4.0.9.2-1.amzn2.0.1
  - **AL2023.12 version:** 4.14.0-1.amzn2023.0.7

- ** `dnf-plugins-core` **
  - **RPM:**  dnf-plugins-core
  - **Architectures:** noarch
  - **AL2 version:** 4.0.2.2-3.amzn2
  - **AL2023.12 version:** 4.3.0-13.amzn2023.0.6

- ** `libdnf` **
  - **RPM:**  libdnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdnf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-hawkey  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libdnf  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.22.5-2.amzn2.0.3
  - **AL2023.12 version:** 0.69.0-8.amzn2023.0.8

- ** `libmodulemd` **
  - **RPM:**  libmodulemd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libmodulemd-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.6.3-1.amzn2.0.1
  - **AL2023.12 version:** 2.13.0-2.amzn2023.0.2

- ** `mock` **
  - **RPM:**  mock  / **Architectures:** noarch
  - **RPM:**  mock-filesystem  / **Architectures:** noarch
  - **RPM:**  mock-lvm  / **Architectures:** noarch
  - **RPM:**  mock-scm  / **Architectures:** noarch
  - **AL2 version:** 2.17-1.amzn2.0.1
  - **AL2023.12 version:** 5.4-1.amzn2023.0.1

- ** `mock-core-configs` **
  - **RPM:**  mock-core-configs
  - **Architectures:** noarch
  - **AL2 version:** 38.3-1.amzn2.0.1
  - **AL2023.12 version:** 39.2-1.amzn2023.0.1

- ** `python-cov-core` **
  - **RPM:**  python3-cov-core
  - **Architectures:** noarch
  - **AL2 version:** 1.15.0-9.amzn2
  - **AL2023.12 version:** 1.15.0-21.amzn2023.0.2

- ** `python-distro` **
  - **RPM:**  python3-distro
  - **Architectures:** noarch
  - **AL2 version:** 1.5.0-5.amzn2.0.1
  - **AL2023.12 version:** 1.5.0-5.amzn2023.0.2

- ** `python-pyroute2` **
  - **RPM:**  python3-pyroute2
  - **Architectures:** noarch
  - **AL2 version:** 0.5.6-5.amzn2.0.1
  - **AL2023.12 version:** 0.7.3-1.amzn2023

- ** `python-pytest-cov` **
  - **RPM:**  python3-pytest-cov
  - **Architectures:** noarch
  - **AL2 version:** 2.6.0-1.amzn2.0.1
  - **AL2023.12 version:** 3.0.0-67.amzn2023.0.2

- ** `python-templated-dictionary` **
  - **RPM:**  python3-templated-dictionary
  - **Architectures:** noarch
  - **AL2 version:** 1.1-2.amzn2.0.2
  - **AL2023.12 version:** 1.4-1.amzn2023

- ** `rpm` **
  - **RPM:**  python3-rpm  / **Architectures:**
  - **RPM:**  rpm  / **Architectures:**
  - **RPM:**  rpm-apidocs  / **Architectures:**
  - **RPM:**  rpm-build  / **Architectures:**
  - **RPM:**  rpm-build-libs  / **Architectures:**
  - **RPM:**  rpm-cron  / **Architectures:**
  - **RPM:**  rpm-devel  / **Architectures:**
  - **RPM:**  rpm-libs  / **Architectures:**
  - **RPM:**  rpm-plugin-ima  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-prioreset  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-selinux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-syslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-systemd-inhibit  / **Architectures:**
  - **RPM:**  rpm-sign  / **Architectures:**
  - **AL2 version:** 4.14.3-4.amzn2.0.2
  - **AL2023.12 version:** 4.16.1.3-29.amzn2023.0.7

## ruby2.6 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-ruby2.6"></a>

- ** `ruby3.2` (`ruby` in AL2) **
  - **RPM:**  ruby3.2 (ruby in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-devel (ruby-devel in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-doc (ruby-doc in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-libs (ruby-libs in AL2)  / **Architectures:**
  - **AL2 version:** 2.6.10-130.amzn2.0.1
  - **AL2023.12 version:** 3.2.8-184.amzn2023.0.6

## ruby3.0 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-ruby3.0"></a>

- ** `ruby3.2` (`ruby` in AL2) **
  - **RPM:**  ruby3.2 (ruby in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-default-gems (ruby-default-gems in AL2)  / **Architectures:** noarch
  - **RPM:**  ruby3.2-devel (ruby-devel in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-doc (ruby-doc in AL2)  / **Architectures:**
  - **RPM:**  ruby3.2-libs (ruby-libs in AL2)  / **Architectures:**
  - **AL2 version:** 3.0.6-156.amzn2.0.2
  - **AL2023.12 version:** 3.2.8-184.amzn2023.0.6

## squid4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-squid4"></a>

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:**
  - **AL2 version:** 4.15-1.amzn2.0.5
  - **AL2023.12 version:** 6.13-1.amzn2023.0.5

## tomcat8.5 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-tomcat8.5"></a>

- ** `tomcat9` (`tomcat` in AL2) **
  - **RPM:**  tomcat9 (tomcat in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-admin-webapps (tomcat-admin-webapps in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-docs-webapp (tomcat-docs-webapp in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-el-3.0-api (tomcat-el-3.0-api in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api (tomcat-jsp-2.3-api in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib (tomcat-lib in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-webapps (tomcat-webapps in AL2)  / **Architectures:**
  - **AL2 version:** 8.5.100-1.amzn2.0.2
  - **AL2023.12 version:** 9.0.120-1.amzn2023.0.1

## tomcat9 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-tomcat9"></a>

- ** `tomcat9` (`tomcat` in AL2) **
  - **RPM:**  tomcat9 (tomcat in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-admin-webapps (tomcat-admin-webapps in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-docs-webapp (tomcat-docs-webapp in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-el-3.0-api (tomcat-el-3.0-api in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-jsp-2.3-api (tomcat-jsp-2.3-api in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-lib (tomcat-lib in AL2)  / **Architectures:**
  - **RPM:**  tomcat9-servlet-4.0-api (tomcat-servlet-4.0-api in AL2)  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps (tomcat-webapps in AL2)  / **Architectures:**
  - **AL2 version:** 9.0.120-1.amzn2.0.1
  - **AL2023.12 version:** 9.0.120-1.amzn2023.0.1

## unbound1.13 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-unbound1.13"></a>

- ** `fstrm` **
  - **RPM:**  fstrm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fstrm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fstrm-doc  / **Architectures:** noarch
  - **AL2 version:** 0.3.2-1.amzn2
  - **AL2023.12 version:** 0.6.1-2.amzn2023.0.2

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:**
  - **RPM:**  unbound  / **Architectures:**
  - **RPM:**  unbound-devel  / **Architectures:**
  - **RPM:**  unbound-libs  / **Architectures:**
  - **AL2 version:** 1.13.1-3.amzn2.0.5
  - **AL2023.12 version:** 1.17.1-1.amzn2023.0.13

## unbound1.17 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-unbound1.17"></a>

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:**
  - **RPM:**  unbound  / **Architectures:**
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:**
  - **RPM:**  unbound-libs  / **Architectures:**
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.17.0-2.amzn2.0.12
  - **AL2023.12 version:** 1.17.1-1.amzn2023.0.13

## vim AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-vim"></a>

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:**
  - **RPM:**  vim-enhanced  / **Architectures:**
  - **RPM:**  vim-minimal  / **Architectures:**
  - **AL2 version:** 8.0.1257-2.amzn2
  - **AL2023.12 version:** 9.2.780-1.amzn2023.0.1

## ansible2 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-ansible2"></a>

- ** `ansible` **
  - **RPM:**  ansible
  - **Architectures:** noarch
  - **AL2 version:** 2.9.23-1.amzn2
  - **AL2023.12 version:** 8.3.0-1.amzn2023.0.3

- ** `libtomcrypt` **
  - **RPM:**  libtomcrypt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtomcrypt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtomcrypt-doc  / **Architectures:** noarch
  - **AL2 version:** 1.18.2-1.amzn2.0.1
  - **AL2023.12 version:** 1.18.2-12.amzn2023.0.2

- ** `libtommath` **
  - **RPM:**  libtommath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtommath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtommath-doc  / **Architectures:** noarch
  - **AL2 version:** 1.0.1-4.amzn2.0.2
  - **AL2023.12 version:** 1.2.0-62.amzn2023.0.1

- ** `sshpass` **
  - **RPM:**  sshpass
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.06-1.amzn2.0.1
  - **AL2023.12 version:** 1.09-6.amzn2023.0.1

## httpd\_modules AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-httpd_modules"></a>

- ** `python-sphinx-theme-alabaster` **
  - **RPM:**  python3-sphinx-theme-alabaster
  - **Architectures:** noarch
  - **AL2 version:** 0.7.9-1.amzn2.0.2
  - **AL2023.12 version:** 0.7.12-11.amzn2023.0.2

## redis4.0 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-redis4.0"></a>

- ** `redis6` (`redis` in AL2) **
  - **RPM:**  redis6 (redis in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel (redis-devel in AL2)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc (redis-doc in AL2)  / **Architectures:** noarch
  - **AL2 version:** 4.0.10-2.amzn2.0.2
  - **AL2023.12 version:** 6.2.20-2.amzn2023.0.1

## redis6 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-redis6"></a>

- ** `redis6` (`redis` in AL2) **
  - **RPM:**  redis6 (redis in AL2)  / **Architectures:**
  - **RPM:**  redis6-devel (redis-devel in AL2)  / **Architectures:**
  - **RPM:**  redis6-doc (redis-doc in AL2)  / **Architectures:**
  - **AL2 version:** 6.2.20-2.amzn2.0.1
  - **AL2023.12 version:** 6.2.20-2.amzn2023.0.1

## R3.4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-R3.4"></a>

- ** `openblas` **
  - **RPM:**  openblas  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-openmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-openmp64  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-openmp64\_  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-serial64  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-serial64\_  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-threads  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-threads64  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-threads64\_  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.2.20-3.amzn2.0.1
  - **AL2023.12 version:** 0.3.18-1.amzn2023.0.3

- ** `R` **
  - **RPM:**  libRmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libRmath-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-core-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  R-java-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 3.4.3-1.amzn2.0.2
  - **AL2023.12 version:** 4.5.3-1.amzn2023.0.1

- ** `tre` **
  - **RPM:**  agrep  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tre  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tre-common  / **Architectures:** noarch
  - **RPM:**  tre-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.8.0-21.20140228gitc2f5d13.amzn2.0.1
  - **AL2023.12 version:** 0.8.0-32.20140228gitc2f5d13.amzn2023.0.3

## R4 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-R4"></a>

- ** `openblas` **
  - **RPM:**  openblas  / **Architectures:**
  - **RPM:**  openblas-devel  / **Architectures:**
  - **RPM:**  openblas-openmp  / **Architectures:**
  - **RPM:**  openblas-openmp64  / **Architectures:**
  - **RPM:**  openblas-openmp64\_  / **Architectures:**
  - **RPM:**  openblas-serial  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openblas-serial64  / **Architectures:**
  - **RPM:**  openblas-serial64\_  / **Architectures:**
  - **RPM:**  openblas-static  / **Architectures:**
  - **RPM:**  openblas-threads  / **Architectures:**
  - **RPM:**  openblas-threads64  / **Architectures:**
  - **RPM:**  openblas-threads64\_  / **Architectures:**
  - **AL2 version:** 0.3.9-1.amzn2.0.2
  - **AL2023.12 version:** 0.3.18-1.amzn2023.0.3

- ** `R` **
  - **RPM:**  libRmath  / **Architectures:**
  - **RPM:**  libRmath-devel  / **Architectures:**
  - **RPM:**  libRmath-static  / **Architectures:**
  - **RPM:**  R  / **Architectures:**
  - **RPM:**  R-core  / **Architectures:**
  - **RPM:**  R-core-devel  / **Architectures:**
  - **RPM:**  R-devel  / **Architectures:**
  - **RPM:**  R-java  / **Architectures:**
  - **RPM:**  R-java-devel  / **Architectures:**
  - **AL2 version:** 4.0.2-5.amzn2.0.3
  - **AL2023.12 version:** 4.5.3-1.amzn2023.0.1

- ** `tre` **
  - **RPM:**  agrep  / **Architectures:**
  - **RPM:**  python3-tre  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tre  / **Architectures:**
  - **RPM:**  tre-common  / **Architectures:**
  - **RPM:**  tre-devel  / **Architectures:**
  - **AL2 version:** 0.8.0-27.20140228gitc2f5d13.amzn2
  - **AL2023.12 version:** 0.8.0-32.20140228gitc2f5d13.amzn2023.0.3

## docker AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-docker"></a>

- ** `amazon-ecr-credential-helper` **
  - **RPM:**  amazon-ecr-credential-helper
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.12.0-3.amzn2
  - **AL2023.12 version:** 0.12.0-3.amzn2023

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.1.9-1.amzn2.0.2
  - **AL2023.12 version:** 2.2.5-1.amzn2023.0.2

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 25.0.16-1.amzn2.0.4
  - **AL2023.12 version:** 25.0.16-1.amzn2023.0.4

- ** `oci-add-hooks` **
  - **RPM:**  oci-add-hooks
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0-0.10.20200504git325a340.amzn2
  - **AL2023.12 version:** 0-0.1.20200504git268e3bb.amzn2023.0.11

- ** `runc` **
  - **RPM:**  runc
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.5-1.amzn2
  - **AL2023.12 version:** 1.3.5-1.amzn2023.0.2

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.17.2-1.amzn2.0.3
  - **AL2023.12 version:** 1.17.2-1.amzn2023.0.3

- ** `soci-snapshotter` **
  - **RPM:**  soci-snapshotter
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.14.1-1.amzn2.0.1
  - **AL2023.12 version:** 0.14.1-1.amzn2023.0.1

## ecs AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-ecs"></a>

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:**
  - **RPM:**  containerd-stress  / **Architectures:**
  - **AL2 version:** 2.1.9-1.amzn2.0.1
  - **AL2023.12 version:** 2.2.5-1.amzn2023.0.2

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:**
  - **AL2 version:** 25.0.16-1.amzn2.0.3
  - **AL2023.12 version:** 25.0.16-1.amzn2023.0.4

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.106.0-1.amzn2
  - **AL2023.12 version:** 1.106.0-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** v1.34.13.3-1.amzn2
  - **AL2023.12 version:** v1.34.13.3-1.amzn2023

## GraphicsMagick1.3 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-GraphicsMagick1.3"></a>

- ** `GraphicsMagick` **
  - **RPM:**  GraphicsMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  GraphicsMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  GraphicsMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  GraphicsMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  GraphicsMagick-doc  / **Architectures:** noarch
  - **RPM:**  GraphicsMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.3.45-1.amzn2.0.3
  - **AL2023.12 version:** 1.3.45-1.amzn2023.0.3

- ** `p7zip` **
  - **RPM:**  p7zip  / **Architectures:** aarch64, x86\_64
  - **RPM:**  p7zip-doc  / **Architectures:** noarch
  - **RPM:**  p7zip-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 16.02-20.amzn2.0.2
  - **AL2023.12 version:** 16.02-30.amzn2023.0.2

- ** `yasm` **
  - **RPM:**  yasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yasm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.2.0-4.amzn2.0.2
  - **AL2023.12 version:** 1.3.0-13.amzn2023.0.4

## testing AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-testing"></a>

- ** `iperf` **
  - **RPM:**  iperf
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.0.13-1.amzn2
  - **AL2023.12 version:** 2.1.9-2.amzn2023

- ** `libbsd` **
  - **RPM:**  libbsd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbsd-ctor-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libbsd-devel  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.9.1-2.amzn2.0.1
  - **AL2023.12 version:** 0.10.0-7.amzn2023.0.2

- ** `stress-ng` **
  - **RPM:**  stress-ng
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 0.07.29-7.amzn2
  - **AL2023.12 version:** 0.15.05-1.amzn2023

## corretto8 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-corretto8"></a>

- ** [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-1.8.0-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-1.8.0-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.8.0\_502.b07-1.amzn2
  - **AL2023.12 version:** 1.8.0\_502.b07-1.amzn2023

## lustre AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-lustre"></a>

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 2.12.8-14.amzn2
  - **AL2023.12 version:** 2.15.6-32.amzn2023

## lustre2.10 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-lustre2.10"></a>

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:**
  - **AL2 version:** 2.10.8-6.amzn2
  - **AL2023.12 version:** 2.15.6-32.amzn2023

## lynis AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-lynis"></a>

- ** `lynis` **
  - **RPM:**  lynis
  - **Architectures:** noarch
  - **AL2 version:** 3.1.1-1.amzn2.0.2
  - **AL2023.12 version:** 3.0.8-3.amzn2023.0.1

## nginx1 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-nginx1"></a>

- ** `nginx` **
  - **RPM:**  nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-all-modules  / **Architectures:** noarch
  - **RPM:**  nginx-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-filesystem  / **Architectures:** noarch
  - **RPM:**  nginx-mod-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-image-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-http-xslt-filter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-mail  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nginx-mod-stream  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.30.4-1.amzn2.0.1
  - **AL2023.12 version:** 1.30.4-1.amzn2023.0.1

## python3.8 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-python3.8"></a>

- ** `python-rpm-macros` (`python38-rpm-macros` in AL2) **
  - **RPM:**  python-rpm-macros (python38-rpm-macros in AL2)
  - **Architectures:**
  - **AL2 version:** 3-23.amzn2.0.1
  - **AL2023.12 version:** 3.9-41.amzn2023.0.6

## collectd AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-collectd"></a>

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
  - **RPM:**  collectd-dns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-drbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-email  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-generic-jmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-hugepages  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-iptables  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-lua  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mcelog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-netlink  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-nginx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-notify\_desktop  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-notify\_email  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-postgresql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-rrdcached  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-rrdtool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-sensors  / **Architectures:** x86\_64
  - **RPM:**  collectd-smart  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-synproxy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-web  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_prometheus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_sensu  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_tsdb  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-zookeeper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Collectd  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 5.8.1-1.amzn2.0.2
  - **AL2023.12 version:** 5.12.0-16.amzn2023.0.4

- ** `perl-Config-General` **
  - **RPM:**  perl-Config-General
  - **Architectures:** noarch
  - **AL2 version:** 2.61-1.amzn2
  - **AL2023.12 version:** 2.64-1.amzn2023.0.1

- ** `perl-Regexp-Common` **
  - **RPM:**  perl-Regexp-Common
  - **Architectures:** noarch
  - **AL2 version:** 2013031301-1.amzn2
  - **AL2023.12 version:** 2017060201-14.amzn2023.0.2

## collectd-python3 AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-collectd-python3"></a>

- ** `collectd` **
  - **RPM:**  collectd  / **Architectures:**
  - **RPM:**  collectd-apache  / **Architectures:**
  - **RPM:**  collectd-bind  / **Architectures:**
  - **RPM:**  collectd-ceph  / **Architectures:**
  - **RPM:**  collectd-chrony  / **Architectures:**
  - **RPM:**  collectd-curl  / **Architectures:**
  - **RPM:**  collectd-curl\_json  / **Architectures:**
  - **RPM:**  collectd-curl\_xml  / **Architectures:**
  - **RPM:**  collectd-dbi  / **Architectures:**
  - **RPM:**  collectd-disk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-dns  / **Architectures:**
  - **RPM:**  collectd-drbd  / **Architectures:**
  - **RPM:**  collectd-email  / **Architectures:**
  - **RPM:**  collectd-generic-jmx  / **Architectures:**
  - **RPM:**  collectd-hugepages  / **Architectures:**
  - **RPM:**  collectd-iptables  / **Architectures:**
  - **RPM:**  collectd-java  / **Architectures:**
  - **RPM:**  collectd-log\_logstash  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-lua  / **Architectures:**
  - **RPM:**  collectd-mcelog  / **Architectures:**
  - **RPM:**  collectd-mdevents  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-mysql  / **Architectures:**
  - **RPM:**  collectd-netlink  / **Architectures:**
  - **RPM:**  collectd-nginx  / **Architectures:**
  - **RPM:**  collectd-notify\_desktop  / **Architectures:**
  - **RPM:**  collectd-notify\_email  / **Architectures:**
  - **RPM:**  collectd-openldap  / **Architectures:**
  - **RPM:**  collectd-postgresql  / **Architectures:**
  - **RPM:**  collectd-python  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-rrdcached  / **Architectures:**
  - **RPM:**  collectd-rrdtool  / **Architectures:**
  - **RPM:**  collectd-sensors  / **Architectures:**
  - **RPM:**  collectd-smart  / **Architectures:**
  - **RPM:**  collectd-synproxy  / **Architectures:**
  - **RPM:**  collectd-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-web  / **Architectures:**
  - **RPM:**  collectd-write\_prometheus  / **Architectures:**
  - **RPM:**  collectd-write\_sensu  / **Architectures:**
  - **RPM:**  collectd-write\_syslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  collectd-write\_tsdb  / **Architectures:**
  - **RPM:**  collectd-zookeeper  / **Architectures:**
  - **RPM:**  libcollectdclient  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcollectdclient-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-Collectd  / **Architectures:**
  - **AL2 version:** 5.12.0-2.amzn2.0.1
  - **AL2023.12 version:** 5.12.0-16.amzn2023.0.4

## aws-nitro-enclaves-cli AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-aws-nitro-enclaves-cli"></a>

- ** `aws-nitro-enclaves-acm` **
  - **RPM:**  aws-nitro-enclaves-acm
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.0-2.amzn2
  - **AL2023.12 version:** 1.4.0-2.amzn2023

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2 version:** 1.4.5-0.amzn2
  - **AL2023.12 version:** 1.4.5-0.amzn2023

## firefox AL2 Extra packages updated in Amazon Linux 2023
<a name="vercmp-AL2023.12-AL2-ex2-firefox"></a>

- ** `firefox` **
  - **RPM:**  firefox
  - **Architectures:** aarch64, x86\_64
  - **AL2 version:** 140.13.0-1.amzn2.0.1
  - **AL2023.12 version:** 140.13.0-1.amzn2023.0.1

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
