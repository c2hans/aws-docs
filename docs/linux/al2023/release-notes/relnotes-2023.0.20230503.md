---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230503.html
---

# Amazon Linux 2023 version 2023.0.20230503 release notes
<a name="relnotes-2023.0.20230503"></a>

This topic includes release notes for the 2023.0.20230503 version of AL2023.

## Major updates
<a name="major-updates-20230503"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ The AMI deprecation time has changed to 90 days (from the AMI registration timestamp) instead of the current default of two years. We will also be updating the existing AL2023 releases to deprecate at 90 days from registration. For more information about AMI deprecation, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html).
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 contains a known issue where customer defined `NTP` servers via `DHCP` are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, please refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).

**Contact us**

If you find a security issue, follow this link to learn [how to contact our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a Github issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you just have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230503)
+ [Repository](#amis-2023.0.20230503.repository)
+ [Docker container image](#amis-2023020230503.container-image)
+ [Default AMI](#amis-2023020230503.default-ami)
+ [Minimal AMI](#amis-2023020230503.minimal-ami)

## Repository
<a name="amis-2023.0.20230503.repository"></a>

### New packages in AL2023.0.20230503 since AL2023.0.20230419
<a name="new-AL2023.0.20230419-AL2023.0.20230503"></a>

 Comparing AL2023.0.20230419 version 2023.0.20230419 to AL2023.0.20230503 version [2023.0.20230503](#relnotes-2023.0.20230503).

| Package Type | Number of new packages in AL2023.0.20230503 compared to AL2023.0.20230419 |
| --- | --- |
| Source RPMs | 9 |
| Total Binary RPMs | 24 |
|  x86\_64 binary RPMs | 12 |
|  aarch64 binary RPMs | 12 |

New packages in AL2023.0.20230503:

- ** `daemonize` **
  - **RPM:**  daemonize
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.7.8-5.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **Version:** v1.25.4.0-1.amzn2023

- ** `iftop` **
  - **RPM:**  iftop
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0-0.30.pre4.amzn2023

- ** `inotify-tools` **
  - **RPM:**  inotify-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  inotify-tools-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.22.1.0-4.amzn2023

- ** `jemalloc` **
  - **RPM:**  jemalloc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jemalloc-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 5.2.1-7.amzn2023

- ** `lockfile-progs` **
  - **RPM:**  lockfile-progs
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.1.17-16.amzn2023.0.1

- ** `mtr` **
  - **RPM:**  mtr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mtr-gtk  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.95-3.amzn2023.0.1

- ** `nfs4-acl-tools` **
  - **RPM:**  nfs4-acl-tools
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.4.2-1.amzn2023

- ** `wireguard-tools` **
  - **RPM:**  wireguard-tools
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.20210914-4.amzn2023

### AL2023.0.20230503 upgrades from AL2023.0.20230419
<a name="vercmp-AL2023.0.20230419-AL2023.0.20230503"></a>

 Comparing [2023.0.20230419](relnotes-2023.0.20230419.md) to [2023.0.20230503](#relnotes-2023.0.20230503).

| Package Type | Count |
| --- | --- |
| Source | 23 |
| Total Binary | 375 |
|  noarch binary RPMs | 160 |
|  x86\_64 binary RPMs | 109 |
|  aarch64 binary RPMs | 106 |

The full comparison of RPM package versions is below.

- ** `apache-ivy` **
  - **RPM:**  apache-ivy  / **Architectures:** noarch
  - **RPM:**  apache-ivy-javadoc  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 2.5.0-10.amzn2023.0.2
  - **AL2023.0.20230503 version:** 2.5.1-1.amzn2023.0.1

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
  - **AL2023.0.20230419 version:** 9.16.38-1.amzn2023
  - **AL2023.0.20230503 version:** 9.16.38-1.amzn2023.0.1

- ** `ca-certificates` **
  - **RPM:**  ca-certificates
  - **Architectures:** noarch
  - **AL2023.0.20230419 version:** 2023.2.60-1.0.amzn2023.0.1
  - **AL2023.0.20230503 version:** 2023.2.60-1.0.amzn2023.0.2

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 1.70.1-1.amzn2023
  - **AL2023.0.20230503 version:** 1.70.2-1.amzn2023

- ** `future` **
  - **RPM:**  python3-future
  - **Architectures:** noarch
  - **AL2023.0.20230419 version:** 0.18.2-9.amzn2023.0.2
  - **AL2023.0.20230503 version:** 0.18.3-1.amzn2023.0.1

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
  - **AL2023.0.20230419 version:** 9.56.1-5.amzn2023.0.1
  - **AL2023.0.20230503 version:** 9.56.1-7.amzn2023.0.1

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 3.7.8-359.amzn2023.0.3
  - **AL2023.0.20230503 version:** 3.7.8-360.amzn2023.0.4

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-race  / **Architectures:** x86\_64
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 1.19.6-1.amzn2023.0.1
  - **AL2023.0.20230503 version:** 1.19.8-1.amzn2023.0.1

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
  - **AL2023.0.20230419 version:** 2.06-61.amzn2023.0.5
  - **AL2023.0.20230503 version:** 2.06-61.amzn2023.0.6

- ** `ImageMagick` **
  - **RPM:**  ImageMagick  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-c\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ImageMagick-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 6.9.12.82-1.amzn2023.0.1
  - **AL2023.0.20230503 version:** 6.9.12.82-1.amzn2023.0.2

- ** [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-1.8.0-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-1.8.0-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 1.8.0\_362.b08-1.amzn2023
  - **AL2023.0.20230503 version:** 1.8.0\_372.b07-1.amzn2023

- ** [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-11-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-11-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 11.0.18\+10-1.amzn2023
  - **AL2023.0.20230503 version:** 11.0.19\+7-1.amzn2023

- ** [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html) **
  - **RPM:**  [`java-17-amazon-corretto`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-devel`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-headless`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-javadoc`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`java-17-amazon-corretto-jmods`](https://docs.aws.amazon.com/linux/al2023/ug/java.html)  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 17.0.6\+10-1.amzn2023.1
  - **AL2023.0.20230503 version:** 17.0.7\+7-1.amzn2023.1

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
  - **AL2023.0.20230419 version:** 6.1.23-36.46.amzn2023
  - **AL2023.0.20230503 version:** 6.1.25-37.47.amzn2023

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 2.10.3-2.amzn2023.0.1
  - **AL2023.0.20230503 version:** 2.10.4-1.amzn2023.0.1

- ** `nasm` **
  - **RPM:**  nasm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nasm-doc  / **Architectures:** noarch
  - **RPM:**  nasm-rdoff  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 2.15.05-1.amzn2023.0.3
  - **AL2023.0.20230503 version:** 2.15.05-1.amzn2023.0.4

- ** `openldap` **
  - **RPM:**  openldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-clients  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-compat  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openldap-servers  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 2.4.57-6.amzn2023.0.3
  - **AL2023.0.20230503 version:** 2.4.57-6.amzn2023.0.4

- ** `redis6` **
  - **RPM:**  redis6  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  redis6-doc  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 6.2.11-1.amzn2023.0.1
  - **AL2023.0.20230503 version:** 6.2.12-1.amzn2023.0.1

- ** `rpm` **
  - **RPM:**  python3-rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-apidocs  / **Architectures:** noarch
  - **RPM:**  rpm-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-build-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-cron  / **Architectures:** noarch
  - **RPM:**  rpm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-audit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-fapolicyd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-ima  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-prioreset  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-selinux  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-syslog  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-plugin-systemd-inhibit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-sign  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rpm-sign-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 4.16.1.3-12.amzn2023.0.5
  - **AL2023.0.20230503 version:** 4.16.1.3-12.amzn2023.0.6

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
  - **RPM:**  rust-lldb  / **Architectures:** noarch
  - **RPM:**  rust-src  / **Architectures:** noarch
  - **RPM:**  rust-std-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-std-static-wasm32-unknown-unknown  / **Architectures:** noarch
  - **RPM:**  rust-std-static-wasm32-wasi  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 1.66.1-1.amzn2023.0.3
  - **AL2023.0.20230503 version:** 1.68.2-1.amzn2023.0.1

- ** `rust-toolset` **
  - **RPM:**  rust-toolset
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230419 version:** 1.66.1-1.amzn2023.0.2
  - **AL2023.0.20230503 version:** 1.68.2-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 2023.0.20230419-0.amzn2023
  - **AL2023.0.20230503 version:** 2023.0.20230503-0.amzn2023

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.0.20230419 version:** 9.0.71-1.amzn2023.0.1
  - **AL2023.0.20230503 version:** 9.0.71-1.amzn2023.0.2

## Docker container image
<a name="amis-2023020230503.container-image"></a>

The following packages have been **updated**.
+ `amazon-linux-repo-cdn-2023.0.20230503-0.amzn2023`
+ `ca-certificates-2023.2.60-1.0.amzn2023.0.2`
+ `gpg-pubkey-d832c631-63977702`
+ `libxml2-2.10.4-1.amzn2023.0.1`
+ `python3-rpm-4.16.1.3-12.amzn2023.0.6`
+ `rpm-4.16.1.3-12.amzn2023.0.6`
+ `rpm-build-libs-4.16.1.3-12.amzn2023.0.6`
+ `rpm-libs-4.16.1.3-12.amzn2023.0.6`
+ `rpm-sign-libs-4.16.1.3-12.amzn2023.0.6`
+ `system-release-2023.0.20230503-0.amzn2023`

## Default AMI
<a name="amis-2023020230503.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230503-0.amzn2023` |
| `bind-libs-32:9.16.38-1.amzn2023.0.1` |
| `bind-license-32:9.16.38-1.amzn2023.0.1` |
| `bind-utils-32:9.16.38-1.amzn2023.0.1` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.2` |
| `gnutls-3.7.8-360.amzn2023.0.4` |
| `gpg-pubkey-d832c631-63977702` |
| `grub2-common-1:2.06-61.amzn2023.0.6` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.6` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.6` |
| `kernel-6.1.25-37.47.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230503-0.amzn2023` |
| `kernel-tools-6.1.25-37.47.amzn2023` |
| `libxml2-2.10.4-1.amzn2023.0.1` |
| `openldap-2.4.57-6.amzn2023.0.4` |
| `python3-rpm-4.16.1.3-12.amzn2023.0.6` |
| `rpm-4.16.1.3-12.amzn2023.0.6` |
| `rpm-build-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-12.amzn2023.0.6` |
| `system-release-2023.0.20230503-0.amzn2023` |

## Minimal AMI
<a name="amis-2023020230503.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-linux-repo-s3-2023.0.20230503-0.amzn2023` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.2` |
| `gnutls-3.7.8-360.amzn2023.0.4` |
| `gpg-pubkey-d832c631-63977702` |
| `grub2-common-1:2.06-61.amzn2023.0.6` |
| `grub2-efi-aa64-ec2-1:2.06-61.amzn2023.0.6` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.6` |
| `kernel-6.1.25-37.47.amzn2023` |
| `kernel-livepatch-repo-s3-2023.0.20230503-0.amzn2023` |
| `libxml2-2.10.4-1.amzn2023.0.1` |
| `openldap-2.4.57-6.amzn2023.0.4` |
| `python3-rpm-4.16.1.3-12.amzn2023.0.6` |
| `rpm-4.16.1.3-12.amzn2023.0.6` |
| `rpm-build-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-12.amzn2023.0.6` |
| `system-release-2023.0.20230503-0.amzn2023` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
