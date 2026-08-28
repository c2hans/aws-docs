---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20240304.html
---

# Amazon Linux 2023 version 2023.3.20240304 release notes
<a name="relnotes-2023.3.20240304"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20240304 release

## Major updates
<a name="major-updates-2023.3.20240304"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20240304)
+ [Repository](#amis-2023.3.20240304.repository)
+ [Docker container image](#amis-2023.3.20240304.container-image)
+ [Default AMI](#amis-2023.3.20240304.default-ami)
+ [Minimal AMI](#amis-2023.3.20240304.minimal-ami)
+ [Minimal container image](#amis-2023.3.20240304.minimal-container-ami)

## Repository
<a name="amis-2023.3.20240304.repository"></a>

### AL2023.3.20240304 upgrades from AL2023.3.20240219
<a name="vercmp-AL2023.3.20240219-AL2023.3.20240304"></a>

 Comparing [2023.3.20240219](relnotes-2023.3.20240219.md) to [2023.3.20240304](#relnotes-2023.3.20240304).

| Package Type | Count |
| --- | --- |
| Source | 25 |
| Total Binary | 342 |
|  noarch binary RPMs | 104 |
|  x86\_64 binary RPMs | 120 |
|  aarch64 binary RPMs | 118 |

The full comparison of RPM package versions is below.

- ** `amazon-cloudwatch-agent` **
  - **RPM:**  amazon-cloudwatch-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 1.300032.3-1.amzn2023
  - **AL2023.3.20240304 version:** 1.300033.0-1.amzn2023

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
  - **AL2023.3.20240219 version:** 9.16.42-1.amzn2023.0.5
  - **AL2023.3.20240304 version:** 9.16.48-1.amzn2023.0.1

- ** `composer` **
  - **RPM:**  composer
  - **Architectures:** noarch
  - **AL2023.3.20240219 version:** 2.5.8-2.amzn2023.0.1
  - **AL2023.3.20240304 version:** 2.5.8-2.amzn2023.0.2

- ** `cpio` **
  - **RPM:**  cpio
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 2.13-13.amzn2023.0.2
  - **AL2023.3.20240304 version:** 2.13-13.amzn2023.0.3

- ** [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal) **
  - **RPM:**  [`curl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`curl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcurl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`libcurl-minimal`](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html#curl-minimal)  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 8.5.0-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 8.5.0-1.amzn2023.0.2

- ** `dnsmasq` **
  - **RPM:**  dnsmasq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dnsmasq-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 2.89-2.amzn2023.0.1
  - **AL2023.3.20240304 version:** 2.90-1.amzn2023.0.1

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 24.0.5-1.amzn2023.0.3
  - **AL2023.3.20240304 version:** 25.0.3-1.amzn2023.0.1

- ** `dotnet6.0` **
  - **RPM:**  aspnetcore-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-6.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-6.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 6.0.26-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 6.0.27-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 1.81.0-1.amzn2023
  - **AL2023.3.20240304 version:** 1.81.1-1.amzn2023

- ** `ecs-service-connect-agent` **
  - **RPM:**  ecs-service-connect-agent
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** v1.27.2.0-1.amzn2023
  - **AL2023.3.20240304 version:** v1.27.3.0-1.amzn2023

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 3.8.0-378.amzn2023.0.4
  - **AL2023.3.20240304 version:** 3.8.0-379.amzn2023.0.5

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
  - **AL2023.3.20240219 version:** 2.06-61.amzn2023.0.9
  - **AL2023.3.20240304 version:** 2.06-61.amzn2023.0.11

- ** `iscsi-initiator-utils` **
  - **RPM:**  iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  iscsi-initiator-utils-iscsiuio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-iscsi-initiator-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 6.2.1.4-10.git2a8f9d8.amzn2023
  - **AL2023.3.20240304 version:** 6.2.1.4-10.git2a8f9d8.amzn2023.0.1

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
  - **AL2023.3.20240219 version:** 6.1.77-99.164.amzn2023
  - **AL2023.3.20240304 version:** 6.1.79-99.164.amzn2023

- ** `libgit2` **
  - **RPM:**  libgit2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgit2-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 1.6.4-114.amzn2023.0.1
  - **AL2023.3.20240304 version:** 1.6.4-115.amzn2023.0.2

- ** `libuv` **
  - **RPM:**  libuv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 1.47.0-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 1.47.0-1.amzn2023.0.2

- ** `ncurses` **
  - **RPM:**  ncurses  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-base  / **Architectures:** noarch
  - **RPM:**  ncurses-c\+\+-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-compat-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ncurses-term  / **Architectures:** noarch
  - **AL2023.3.20240219 version:** 6.2-4.20200222.amzn2023.0.5
  - **AL2023.3.20240304 version:** 6.2-4.20200222.amzn2023.0.6

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 20.10.0-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 20.11.1-1.amzn2023.0.1

- ** `openexr` **
  - **RPM:**  openexr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openexr-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openexr-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 3.1.5-1.amzn2023.0.3
  - **AL2023.3.20240304 version:** 3.1.5-1.amzn2023.0.4

- ** `perl-Cpanel-JSON-XS` **
  - **RPM:**  perl-Cpanel-JSON-XS
  - **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 4.25-2.amzn2023.0.5
  - **AL2023.3.20240304 version:** 4.25-2.amzn2023.0.6

- ** `postgresql15` **
  - **RPM:**  postgresql15  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql15-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql15-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 15.5-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 15.6-1.amzn2023.0.1

- ** `publicsuffix-list` **
  - **RPM:**  publicsuffix-list  / **Architectures:** noarch
  - **RPM:**  publicsuffix-list-dafsa  / **Architectures:** noarch
  - **AL2023.3.20240219 version:** 20221208-60.amzn2023
  - **AL2023.3.20240304 version:** 20240212-61.amzn2023

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
  - **AL2023.3.20240219 version:** 1.68.2-1.amzn2023.0.3
  - **AL2023.3.20240304 version:** 1.68.2-1.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.3.20240219 version:** 2023.3.20240219-0.amzn2023
  - **AL2023.3.20240304 version:** 2023.3.20240304-0.amzn2023

- ** `unbound` **
  - **RPM:**  python3-unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-anchor  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  unbound-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.3.20240219 version:** 1.17.1-1.amzn2023.0.1
  - **AL2023.3.20240304 version:** 1.17.1-1.amzn2023.0.2

## Docker container image
<a name="amis-2023.3.20240304.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20240304-0.amzn2023`
+ `curl-minimal-8.5.0-1.amzn2023.0.2`
+ `libcurl-minimal-8.5.0-1.amzn2023.0.2`
+ `libpsl-0.21.1-3.amzn2023.0.2`
+ `ncurses-base-6.2-4.20200222.amzn2023.0.6`
+ `ncurses-libs-6.2-4.20200222.amzn2023.0.6`
+ `publicsuffix-list-dafsa-20240212-61.amzn2023`
+ `system-release-2023.3.20240304-0.amzn2023`

## Default AMI
<a name="amis-2023.3.20240304.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240304-0.amzn2023` |
| `bind-libs-32:9.16.48-1.amzn2023.0.1` |
| `bind-license-32:9.16.48-1.amzn2023.0.1` |
| `bind-utils-32:9.16.48-1.amzn2023.0.1` |
| `cpio-2.13-13.amzn2023.0.3` |
| `curl-minimal-8.5.0-1.amzn2023.0.2` |
| `gnutls-3.8.0-379.amzn2023.0.5` |
| `grub2-common-1:2.06-61.amzn2023.0.11` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.11` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.11` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.11` |
| `grub2-tools-1:2.06-61.amzn2023.0.11` |
| `kernel-livepatch-repo-s3-2023.3.20240304-0.amzn2023` |
| `kernel-tools-6.1.79-99.164.amzn2023` |
| `kernel-6.1.79-99.164.amzn2023` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.2` |
| `libuv-1:1.47.0-1.amzn2023.0.2` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.6` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.6` |
| `ncurses-6.2-4.20200222.amzn2023.0.6` |
| `publicsuffix-list-dafsa-20240212-61.amzn2023` |
| `system-release-2023.3.20240304-0.amzn2023` |

## Minimal AMI
<a name="amis-2023.3.20240304.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20240304-0.amzn2023` |
| `cpio-2.13-13.amzn2023.0.3` |
| `curl-minimal-8.5.0-1.amzn2023.0.2` |
| `gnutls-3.8.0-379.amzn2023.0.5` |
| `grub2-common-1:2.06-61.amzn2023.0.11` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.11` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.11` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.11` |
| `grub2-tools-1:2.06-61.amzn2023.0.11` |
| `kernel-livepatch-repo-s3-2023.3.20240304-0.amzn2023` |
| `kernel-6.1.79-99.164.amzn2023` |
| `libcurl-minimal-8.5.0-1.amzn2023.0.2` |
| `libpsl-0.21.1-3.amzn2023.0.2` |
| `ncurses-base-6.2-4.20200222.amzn2023.0.6` |
| `ncurses-libs-6.2-4.20200222.amzn2023.0.6` |
| `ncurses-6.2-4.20200222.amzn2023.0.6` |
| `publicsuffix-list-dafsa-20240212-61.amzn2023` |
| `system-release-2023.3.20240304-0.amzn2023` |

## Minimal container image
<a name="amis-2023.3.20240304.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20240304-0.amzn2023`
+ `curl-minimal-8.5.0-1.amzn2023.0.2`
+ `libcurl-minimal-8.5.0-1.amzn2023.0.2`
+ `libpsl-0.21.1-3.amzn2023.0.2`
+ `ncurses-base-6.2-4.20200222.amzn2023.0.6`
+ `ncurses-libs-6.2-4.20200222.amzn2023.0.6`
+ `publicsuffix-list-dafsa-20240212-61.amzn2023`
+ `system-release-2023.3.20240304-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
