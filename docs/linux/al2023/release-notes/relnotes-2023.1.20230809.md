---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230809.html
---

# Amazon Linux 2023 version 2023.1.20230809 release notes
<a name="relnotes-2023.1.20230809"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.1.20230809 release

## Major updates
<a name="major-updates-2023.1.20230809"></a>

This release represents an update to AL2023.1. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

For information about UEFI Secure Boot on AL2023, see [Amazon Linux announces support for secure boot with AL2023.1](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-linux-secure-boot-al2023-1/).

AL2023 includes the following major updates.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ Kernel Live Patches will fail to apply on a system where UEFI Secure Boot is enabled. This will be fixed in an upcoming release.
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, see [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.1.20230809)
+ [Repository](#amis-2023.1.20230809.repository)
+ [Docker container image](#amis-2023.1.20230809.container-image)
+ [Default AMI](#amis-2023.1.20230809.default-ami)
+ [Minimal AMI](#amis-2023.1.20230809.minimal-ami)

## Repository
<a name="amis-2023.1.20230809.repository"></a>

### AL2023.1.20230809 upgrades from AL2023.1.20230725
<a name="vercmp-AL2023.1.20230725-AL2023.1.20230809"></a>

 Comparing [2023.1.20230725](relnotes-2023.1.20230725.md) to [2023.1.20230809](#relnotes-2023.1.20230809).

| Package Type | Count |
| --- | --- |
| Source | 25 |
| Total Binary | 415 |
|  noarch binary RPMs | 252 |
|  x86\_64 binary RPMs | 82 |
|  aarch64 binary RPMs | 81 |

The full comparison of RPM package versions is below.

- ** `abseil-cpp` **
  - **RPM:**  abseil-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  abseil-cpp-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 20210324.2-5.amzn2023.0.3
  - **AL2023.1.20230809 version:** 20220623.1-4.amzn2023.0.1

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
  - **AL2023.1.20230725 version:** 0.8-14.amzn2023.0.7
  - **AL2023.1.20230809 version:** 0.8-14.amzn2023.0.8

- ** `bouncycastle` **
  - **RPM:**  bouncycastle  / **Architectures:** noarch
  - **RPM:**  bouncycastle-javadoc  / **Architectures:** noarch
  - **RPM:**  bouncycastle-mail  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pg  / **Architectures:** noarch
  - **RPM:**  bouncycastle-pkix  / **Architectures:** noarch
  - **RPM:**  bouncycastle-tls  / **Architectures:** noarch
  - **RPM:**  bouncycastle-util  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 1.70-4.amzn2023.0.2
  - **AL2023.1.20230809 version:** 1.70-4.amzn2023.0.3

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 1.2.0-1.amzn2023
  - **AL2023.1.20230809 version:** 1.2.0-1.amzn2023.0.1

- ** [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/ecs.html](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 1.73.1-1.amzn2023
  - **AL2023.1.20230809 version:** 1.74.1-1.amzn2023

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
  - **AL2023.1.20230725 version:** 9.56.1-7.amzn2023.0.1
  - **AL2023.1.20230809 version:** 9.56.1-7.amzn2023.0.2

- ** [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [https://docs.aws.amazon.com/linux/al2023/ug/go.html](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 1.20.5-1.amzn2023.0.2
  - **AL2023.1.20230809 version:** 1.20.6-1.amzn2023.0.1

- ** `grpc` **
  - **RPM:**  grpc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-data  / **Architectures:** noarch
  - **RPM:**  grpc-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  grpc-doc  / **Architectures:** noarch
  - **RPM:**  grpc-plugins  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 1.41.1-9.amzn2023
  - **AL2023.1.20230809 version:** 1.56.2-10.amzn2023

- ** `iperf3` **
  - **RPM:**  iperf3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iperf3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 3.11-1.amzn2023.0.3
  - **AL2023.1.20230809 version:** 3.11-1.amzn2023.0.4

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
  - **AL2023.1.20230725 version:** 6.1.38-59.109.amzn2023
  - **AL2023.1.20230809 version:** 6.1.41-63.114.amzn2023

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
  - **AL2023.1.20230725 version:** 39.31.5.1-117.amzn2023.0.3
  - **AL2023.1.20230809 version:** 39.31.5.1-117.amzn2023.0.4

- ** `microcode_ctl` **
  - **RPM:**  microcode\_ctl
  - **Architectures:** x86\_64
  - **AL2023.1.20230725 version:** 2.1-53.amzn2023.0.1
  - **AL2023.1.20230809 version:** 2.1-53.amzn2023.0.2

- ** `nghttp2` **
  - **RPM:**  libnghttp2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnghttp2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nghttp2  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 1.51.0-1.amzn2023
  - **AL2023.1.20230809 version:** 1.55.1-1.amzn2023.0.1

- ** `nodejs` **
  - **RPM:**  nodejs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-docs  / **Architectures:** noarch
  - **RPM:**  nodejs-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 18.12.1-1.amzn2023.0.7
  - **AL2023.1.20230809 version:** 18.12.1-1.amzn2023.0.9

- ** `openldap` **
  - **RPM:**  openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-servers  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 2.4.57-6.amzn2023.0.5
  - **AL2023.1.20230809 version:** 2.4.57-6.amzn2023.0.6

- ** `openssh` **
  - **RPM:**  openssh  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-keycat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssh-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pam\_ssh\_agent\_auth  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 8.7p1-8.amzn2023.0.6
  - **AL2023.1.20230809 version:** 8.7p1-8.amzn2023.0.7

- ** `pcre2` **
  - **RPM:**  pcre2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-syntax  / **Architectures:** noarch
  - **RPM:**  pcre2-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-utf16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pcre2-utf32  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 10.40-1.amzn2023.0.2
  - **AL2023.1.20230809 version:** 10.40-1.amzn2023.0.3

- ** `python-mako` **
  - **RPM:**  python3-mako  / **Architectures:** noarch
  - **RPM:**  python-mako-doc  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 1.1.4-3.amzn2023.0.2
  - **AL2023.1.20230809 version:** 1.1.4-3.amzn2023.0.3

- ** `redis6` **
  - **RPM:**  redis6  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 6.2.12-1.amzn2023.0.1
  - **AL2023.1.20230809 version:** 6.2.13-1.amzn2023.0.1

- ** `selinux-policy` **
  - **RPM:**  selinux-policy  / **Architectures:** noarch
  - **RPM:**  selinux-policy-devel  / **Architectures:** noarch
  - **RPM:**  selinux-policy-doc  / **Architectures:** noarch
  - **RPM:**  selinux-policy-minimum  / **Architectures:** noarch
  - **RPM:**  selinux-policy-mls  / **Architectures:** noarch
  - **RPM:**  selinux-policy-sandbox  / **Architectures:** noarch
  - **RPM:**  selinux-policy-targeted  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 36.16-1.amzn2023.0.2
  - **AL2023.1.20230809 version:** 36.16-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 2023.1.20230725-0.amzn2023
  - **AL2023.1.20230809 version:** 2023.1.20230809-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.1.20230725 version:** 9.0.71-1.amzn2023.0.3
  - **AL2023.1.20230809 version:** 9.0.71-1.amzn2023.0.4

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 4.0.6-1.amzn2023.0.1
  - **AL2023.1.20230809 version:** 4.0.7-1.amzn2023.0.1

- ** `yajl` **
  - **RPM:**  yajl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yajl-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 2.1.0-16.amzn2023.0.4
  - **AL2023.1.20230809 version:** 2.1.0-16.amzn2023.0.5

- ** `yasm` **
  - **RPM:**  yasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  yasm-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.1.20230725 version:** 1.3.0-13.amzn2023.0.3
  - **AL2023.1.20230809 version:** 1.3.0-13.amzn2023.0.4

## Docker container image
<a name="amis-2023.1.20230809.container-image"></a>
+ `amazon-linux-repo-cdn-2023.1.20230809-0.amzn2023`
+ `libnghttp2-1.55.1-1.amzn2023.0.1`
+ `pcre2-syntax-10.40-1.amzn2023.0.3`
+ `pcre2-10.40-1.amzn2023.0.3`
+ `system-release-2023.1.20230809-0.amzn2023`

## Default AMI
<a name="amis-2023.1.20230809.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230809-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.1.20230809-0.amzn2023` |
| `kernel-tools-6.1.41-63.114.amzn2023` |
| `kernel-6.1.41-63.114.amzn2023` |
| `libnghttp2-1.55.1-1.amzn2023.0.1` |
| `microcode_ctl-2:2.1-53.amzn2023.0.2` |
| `openldap-2.4.57-6.amzn2023.0.6` |
| `openssh-clients-8.7p1-8.amzn2023.0.7` |
| `openssh-server-8.7p1-8.amzn2023.0.7` |
| `openssh-8.7p1-8.amzn2023.0.7` |
| `pcre2-syntax-10.40-1.amzn2023.0.3` |
| `pcre2-10.40-1.amzn2023.0.3` |
| `selinux-policy-targeted-36.16-1.amzn2023.0.3` |
| `selinux-policy-36.16-1.amzn2023.0.3` |
| `system-release-2023.1.20230809-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.1.20230809.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.1.20230809-0.amzn2023` |
| `kernel-livepatch-repo-s3-2023.1.20230809-0.amzn2023` |
| `kernel-6.1.41-63.114.amzn2023` |
| `libnghttp2-1.55.1-1.amzn2023.0.1` |
| `openldap-2.4.57-6.amzn2023.0.6` |
| `openssh-clients-8.7p1-8.amzn2023.0.7` |
| `openssh-server-8.7p1-8.amzn2023.0.7` |
| `openssh-8.7p1-8.amzn2023.0.7` |
| `pcre2-syntax-10.40-1.amzn2023.0.3` |
| `pcre2-10.40-1.amzn2023.0.3` |
| `selinux-policy-targeted-36.16-1.amzn2023.0.3` |
| `selinux-policy-36.16-1.amzn2023.0.3` |
| `system-release-2023.1.20230809-0.amzn2023` |
