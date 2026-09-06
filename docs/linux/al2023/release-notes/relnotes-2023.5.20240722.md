---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240722.html
---

# Amazon Linux 2023 version 2023.5.20240722 release notes
<a name="relnotes-2023.5.20240722"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.5.20240722.

**Topics**
+ [Major updates](#major-updates-2023.5.20240722)
+ [Repository](#amis-2023.5.20240722.repository)
+ [Docker container image](#amis-2023.5.20240722.container-image)
+ [Default AMI](#amis-2023.5.20240722.default-ami)
+ [Minimal AMI](#amis-2023.5.20240722.minimal-ami)
+ [Minimal container image](#amis-2023.5.20240722.minimal-container-ami)
+ [Contact us](#amis-2023.5.20240722.contact-us)

## Major updates
<a name="major-updates-2023.5.20240722"></a>

This release represents an update to the fifth quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Known Issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.5.20240722.repository"></a>

### New packages in AL2023.5.20240722 since AL2023.5.20240708
<a name="new-AL2023.5.20240708-AL2023.5.20240722"></a>

 Comparing AL2023.5.20240708 version 2023.5.20240708 to AL2023.5.20240722 version [2023.5.20240722](#relnotes-2023.5.20240722).

| Package Type | Number of new packages in AL2023.5.20240722 compared to AL2023.5.20240708 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 4 |
|  x86\_64 binary RPMs | 2 |
|  aarch64 binary RPMs | 2 |

New packages in AL2023.5.20240722:

- ** `tftp` **
  - **RPM:**  tftp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tftp-server  / **Architectures:** aarch64, x86\_64
  - **Version:** 5.2-42.amzn2023.0.1

### AL2023.5.20240722 upgrades from AL2023.5.20240708
<a name="vercmp-AL2023.5.20240708-AL2023.5.20240722"></a>

 Comparing [2023.5.20240708](relnotes-2023.5.20240708.md) to [2023.5.20240722](#relnotes-2023.5.20240722).

| Package Type | Count |
| --- | --- |
| Source | 26 |
| Total Binary | 338 |
|  noarch binary RPMs | 120 |
|  x86\_64 binary RPMs | 109 |
|  aarch64 binary RPMs | 109 |

The full comparison of RPM package versions is below.

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 2.0.3-1.amzn2023
  - **AL2023.5.20240722 version:** 2.0.4-1.amzn2023

- ** `composer` **
  - **RPM:**  composer
  - **Architectures:** noarch
  - **AL2023.5.20240708 version:** 2.5.8-2.amzn2023.0.3
  - **AL2023.5.20240722 version:** 2.5.8-2.amzn2023.0.4

- ** `cups` **
  - **RPM:**  cups  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-filesystem  / **Architectures:** noarch
  - **RPM:**  cups-ipptool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-lpd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  cups-printerapp  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 2.3.3op2-18.amzn2023.0.7
  - **AL2023.5.20240722 version:** 2.3.3op2-18.amzn2023.0.8

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 25.0.3-1.amzn2023.0.1
  - **AL2023.5.20240722 version:** 25.0.3-1.amzn2023.0.2

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 1.84.0-1.amzn2023
  - **AL2023.5.20240722 version:** 1.85.1-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** v1.29.5.0-1.amzn2023
  - **AL2023.5.20240722 version:** v1.29.6.0-1.amzn2023

- ** `emacs` **
  - **RPM:**  emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-filesystem  / **Architectures:** noarch
  - **RPM:**  emacs-lucid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-nox  / **Architectures:** aarch64, x86\_64
  - **RPM:**  emacs-terminal  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 28.2-3.amzn2023.0.7
  - **AL2023.5.20240722 version:** 28.2-3.amzn2023.0.8

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
  - **AL2023.5.20240708 version:** 9.56.1-7.amzn2023.0.7
  - **AL2023.5.20240722 version:** 9.56.1-7.amzn2023.0.8

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 1.22.4-1.amzn2023.0.1
  - **AL2023.5.20240722 version:** 1.22.5-1.amzn2023.0.1

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
  - **AL2023.5.20240708 version:** 2.4.59-2.amzn2023
  - **AL2023.5.20240722 version:** 2.4.61-1.amzn2023

- ** [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-1.8.0-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 1.8.0\_412.b08-1.amzn2023
  - **AL2023.5.20240722 version:** 1.8.0\_422.b05-1.amzn2023

- ** [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 11.0.23\+9-1.amzn2023
  - **AL2023.5.20240722 version:** 11.0.24\+8-1.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 17.0.11\+9-1.amzn2023.1
  - **AL2023.5.20240722 version:** 17.0.12\+7-1.amzn2023.1

- ** [`java-21-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-21-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-21-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 21.0.3\+9-1.amzn2023.1
  - **AL2023.5.20240722 version:** 21.0.4\+7-1.amzn2023.1

- ** [`java-22-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-22-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-22-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 22.0.1\+8-1.amzn2023.1
  - **AL2023.5.20240722 version:** 22.0.2\+9-1.amzn2023.1

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
  - **AL2023.5.20240708 version:** 6.1.96-102.177.amzn2023
  - **AL2023.5.20240722 version:** 6.1.97-104.177.amzn2023

- ** `nano` **
  - **RPM:**  default-editor  / **Architectures:** noarch
  - **RPM:**  nano  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nano-default-editor  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 5.8-3.amzn2023.0.3
  - **AL2023.5.20240722 version:** 5.8-3.amzn2023.0.4

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 8.7p1-8.amzn2023.0.11
  - **AL2023.5.20240722 version:** 8.7p1-8.amzn2023.0.12

- ** [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.1`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
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
  - **AL2023.5.20240708 version:** 8.1.28-1.amzn2023.0.1
  - **AL2023.5.20240722 version:** 8.1.29-1.amzn2023.0.1

- ** `python3.11-setuptools` **
  - **RPM:**  python3.11-setuptools  / **Architectures:** noarch
  - **RPM:**  python3.11-setuptools-wheel  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 65.5.1-2.amzn2023.0.4
  - **AL2023.5.20240722 version:** 65.5.1-2.amzn2023.0.5

- ** `python-pycurl` **
  - **RPM:**  python3-pycurl
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 7.45.1-1.amzn2023.0.3
  - **AL2023.5.20240722 version:** 7.45.1-1.amzn2023.0.4

- ** `python-werkzeug` **
  - **RPM:**  python3-werkzeug  / **Architectures:** noarch
  - **RPM:**  python3-werkzeug-doc  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 1.0.1-5.amzn2023.0.4
  - **AL2023.5.20240722 version:** 1.0.1-5.amzn2023.0.5

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 2023.5.20240708-1.amzn2023
  - **AL2023.5.20240722 version:** 2023.5.20240722-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.5.20240708 version:** 9.0.87-1.amzn2023.0.2
  - **AL2023.5.20240722 version:** 9.0.90-1.amzn2023.0.2

- ** `wget` **
  - **RPM:**  wget
  - **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 1.21.3-1.amzn2023.0.3
  - **AL2023.5.20240722 version:** 1.21.3-1.amzn2023.0.4

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.5.20240708 version:** 4.0.8-2.amzn2023.0.6
  - **AL2023.5.20240722 version:** 4.0.15-1.amzn2023.0.1

## Docker container image
<a name="amis-2023.5.20240722.container-image"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240722-0.amzn2023` |
| `system-release-2023.5.20240722-0.amzn2023` |

## Default AMI
<a name="amis-2023.5.20240722.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240722-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240722-0.amzn2023` |
| `kernel-tools-6.1.97-104.177.amzn2023` |
| `kernel-6.1.97-104.177.amzn2023` |
| `nano-5.8-3.amzn2023.0.4` |
| `openssh-clients-8.7p1-8.amzn2023.0.12` |
| `openssh-server-8.7p1-8.amzn2023.0.12` |
| `openssh-8.7p1-8.amzn2023.0.12` |
| `system-release-2023.5.20240722-0.amzn2023` |
| `wget-1.21.3-1.amzn2023.0.4` |

## Minimal AMI
<a name="amis-2023.5.20240722.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.5.20240722-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.5.20240722-0.amzn2023` |
| `kernel-6.1.97-104.177.amzn2023` |
| `openssh-clients-8.7p1-8.amzn2023.0.12` |
| `openssh-server-8.7p1-8.amzn2023.0.12` |
| `openssh-8.7p1-8.amzn2023.0.12` |
| `system-release-2023.5.20240722-0.amzn2023` |

## Minimal container image
<a name="amis-2023.5.20240722.minimal-container-ami"></a>

|  |
| --- |
| `amazon-linux-repo-cdn-2023.5.20240722-0.amzn2023` |
| `system-release-2023.5.20240722-0.amzn2023` |

## Contact us
<a name="amis-2023.5.20240722.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
