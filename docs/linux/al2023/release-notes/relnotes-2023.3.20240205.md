---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240205.html
---

# Amazon Linux 2023 version 2023.3.20240205 release notes
<a name="relnotes-2023.3.20240205"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240205 release

## Major updates
<a name="major-updates-2023.3.20240205"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

## Repository
<a name="amis-2023.3.20240205.repository"></a>

### New packages in AL2023.3.20240205 since AL2023.3.20240131
<a name="new-AL2023.3.20240131-AL2023.3.20240205"></a>

 Comparing AL2023.3.20240131 version 2023.3.20240131 to AL2023.3.20240205 version [2023.3.20240205](#relnotes-2023.3.20240205).

| Package Type | Number of new packages in AL2023.3.20240205 compared to AL2023.3.20240131 |
| --- | --- |
| Source RPMs | 1 |
| Total Binary RPMs | 2 |
|  x86\_64 binary RPMs | 1 |
|  aarch64 binary RPMs | 1 |

New packages in AL2023.3.20240205:

- ** `cabextract` **
  - **RPM:**  cabextract
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.11-1.amzn2023.0.1

### AL2023.3.20240205 upgrades from AL2023.3.20240131
<a name="vercmp-AL2023.3.20240131-AL2023.3.20240205"></a>

 Comparing [2023.3.20240131](relnotes-2023.3.20240131.md) to [2023.3.20240205](#relnotes-2023.3.20240205).

| Package Type | Count |
| --- | --- |
| Source | 20 |
| Total Binary | 315 |
|  noarch binary RPMs | 48 |
|  x86\_64 binary RPMs | 134 |
|  aarch64 binary RPMs | 133 |

The full comparison of RPM package versions is below.

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** noarch
  - **AL2023.3.20240131 version:** 1.35.0-1.amzn2023
  - **AL2023.3.20240205 version:** 1.35.1-1.amzn2023

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 2.15.3-1.amzn2023.0.2
  - **AL2023.3.20240205 version:** 2.15.3-1.amzn2023.0.3

- ** `BabelfishDump` **
  - **RPM:**  BabelfishDump
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 15.5-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 16.1-1.amzn2023.0.2

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 1.3.5-0.amzn2023
  - **AL2023.3.20240205 version:** 1.3.6-0.amzn2023

- ** `ec2-hibinit-agent` **
  - **RPM:**  ec2-hibinit-agent
  - **Architectures:** noarch
  - **AL2023.3.20240131 version:** 1.0.4-0.amzn2023.0.2
  - **AL2023.3.20240205 version:** 1.0.8-0.amzn2023

- ** `indent` **
  - **RPM:**  indent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 2.2.12-7.amzn2023.0.5
  - **AL2023.3.20240205 version:** 2.2.12-7.amzn2023.0.6

- ** `jasper` **
  - **RPM:**  jasper  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jasper-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 2.0.33-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 2.0.33-1.amzn2023.0.2

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
  - **AL2023.3.20240131 version:** 6.1.72-96.166.amzn2023
  - **AL2023.3.20240205 version:** 6.1.75-99.163.amzn2023

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
  - **AL2023.3.20240131 version:** 10.5.20-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 10.5.23-1.amzn2023.0.1

- ** `nss` **
  - **RPM:**  nspr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nspr-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-pkcs11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-softokn-freebl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-sysinit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nss-util-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 4.35.0-5.amzn2023.0.4
  - **AL2023.3.20240205 version:** 4.35.0-5.amzn2023.0.5

- ** `pam` **
  - **RPM:**  pam  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam-docs  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 1.5.1-8.amzn2023.0.3
  - **AL2023.3.20240205 version:** 1.5.1-8.amzn2023.0.4

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
  - **AL2023.3.20240131 version:** 8.1.23-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 8.1.27-1.amzn2023.0.1

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
  - **AL2023.3.20240131 version:** 8.2.9-1.amzn2023.0.3
  - **AL2023.3.20240205 version:** 8.2.15-1.amzn2023.0.1

- ** `polkit` **
  - **RPM:**  polkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  polkit-docs  / **Architectures:** noarch
  - **RPM:**  polkit-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 0.117-11.amzn2023
  - **AL2023.3.20240205 version:** 0.117-11.amzn2023.0.1

- ** `python-jinja2` **
  - **RPM:**  python3-jinja2
  - **Architectures:** noarch
  - **AL2023.3.20240131 version:** 2.11.3-1.amzn2023.0.2
  - **AL2023.3.20240205 version:** 2.11.3-1.amzn2023.0.3

- ** `python-pillow` **
  - **RPM:**  python3-pillow  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-tk  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 9.4.0-2.amzn2023.0.3
  - **AL2023.3.20240205 version:** 9.4.0-2.amzn2023.0.4

- ** `redis6` **
  - **RPM:**  redis6  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc  / **Architectures:** noarch
  - **AL2023.3.20240131 version:** 6.2.13-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 6.2.14-1.amzn2023.0.1

- ** `sudo` **
  - **RPM:**  sudo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-logsrvd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  sudo-python-plugin  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240131 version:** 1.9.13-1.p2.amzn2023.0.4
  - **AL2023.3.20240205 version:** 1.9.14-1.p3.amzn2023.0.1

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
  - **AL2023.3.20240131 version:** 252.16-1.amzn2023.0.1
  - **AL2023.3.20240205 version:** 252.16-1.amzn2023.0.2

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240131 version:** 2023.3.20240131-0.amzn2023
  - **AL2023.3.20240205 version:** 2023.3.20240205-0.amzn2023

## Amazon Linux 2023 image updates
<a name="amazon-linux-images"></a>

**Topics**
+ [Docker container image](#amis-2023.3.20240205.container-image)
+ [Default AMI](#amis-2023.3.20240205.default-ami)
+ [Minimal AMI](#amis-2023.3.20240205.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240205.minimal-container-ami)

### Docker container image
<a name="amis-2023.3.20240205.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240205-0.amzn2023.noarch`
+ `system-release-2023.3.20240205-0.amzn2023.noarch`

### Default AMI
<a name="amis-2023.3.20240205.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240205-0.amzn2023.noarch` |
| `ec2-hibinit-agent-1.0.8-0.amzn2023.noarch` |
| `kernel-livepatch-repo-s3-2023.3.20240205-0.amzn2023.noarch` |
| `kernel-tools-6.1.75-99.163.amzn2023.x86_64` |
| `kernel-6.1.75-99.163.amzn2023.x86_64` |
| `nspr-4.35.0-5.amzn2023.0.5.x86_64` |
| `nss-softokn-freebl-3.90.0-3.amzn2023.0.5.x86_64` |
| `nss-softokn-3.90.0-3.amzn2023.0.5.x86_64` |
| `nss-sysinit-3.90.0-3.amzn2023.0.5.x86_64` |
| `nss-util-3.90.0-3.amzn2023.0.5.x86_64` |
| `nss-3.90.0-3.amzn2023.0.5.x86_64` |
| `pam-1.5.1-8.amzn2023.0.4.x86_64` |
| `python3-jinja2-2.11.3-1.amzn2023.0.3.noarch` |
| `sudo-1.9.14-1.p3.amzn2023.0.1.x86_64` |
| `system-release-2023.3.20240205-0.amzn2023.noarch` |
| `systemd-libs-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-networkd-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-pam-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-resolved-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-udev-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-252.16-1.amzn2023.0.2.x86_64` |

### Minimal AMI
<a name="amis-2023.3.20240205.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240205-0.amzn2023.noarch` |
| `kernel-livepatch-repo-s3-2023.3.20240205-0.amzn2023.noarch` |
| `kernel-6.1.75-99.163.amzn2023.x86_64` |
| `pam-1.5.1-8.amzn2023.0.4.x86_64` |
| `python3-jinja2-2.11.3-1.amzn2023.0.3.noarch` |
| `sudo-1.9.14-1.p3.amzn2023.0.1.x86_64` |
| `system-release-2023.3.20240205-0.amzn2023.noarch` |
| `systemd-libs-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-networkd-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-pam-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-resolved-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-udev-252.16-1.amzn2023.0.2.x86_64` |
| `systemd-252.16-1.amzn2023.0.2.x86_64` |

### Minimal container image
<a name="amis-2023.3.20240205.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240205-0.amzn2023.noarch`
+ `system-release-2023.3.20240205-0.amzn2023.noarch`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
