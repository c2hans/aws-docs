---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.3.20231211.html
---

# Amazon Linux 2023 version 2023.3.20231211 release notes
<a name="relnotes-2023.3.20231211"></a>

This topic includes Amazon Linux 2023 (AL2023) release notes updates for the 2023.3.20231211 release

## Major updates
<a name="major-updates-2023.3.20231211"></a>

This release represents an update to the [third quarterly release](https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-linux-kvm-vmware-images-al2023-3/) of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as Deterministic updates, better optimizations for Graviton processors, and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

AL2023 includes the following major updates.
+  AL2023 can now be run as a virtualized guest outside of being run on Amazon EC2. There are currently KVM (`qcow2`) and VMware (`OVA`) images available. See [Using Amazon Linux 2023 outside of Amazon EC2](https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2.html) for more information.
+ A fix was added to the `kernel-modules-extra` package so that the simple UEFI framebuffer now works when using KVM or VMware images in UEFI rather than BIOS mode. This allows the kernel console to work without using an emulated serial port. The `kernel-modules-extra` package is installed by default for on-premises images.
+ The on-premises image was shrunk by replacing `perl` with `perl-interpreter` which does not require bringing in dependencies such as `gcc`.

**Known Issues**
+ None.

**Security Updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVE's that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-2023.3.20231211)
+ [Repository](#amis-2023.3.20231211.repository)
+ [Docker container image](#amis-2023.3.20231211.container-image)
+ [Default AMI](#amis-2023.3.20231211.default-ami)
+ [Minimal AMI](#amis-2023.3.20231211.minimal-ami)
+ [Minimal container image](#amis-2023.3.20231211.minimal-container-ami)

## Repository
<a name="amis-2023.3.20231211.repository"></a>

### New packages in AL2023.3.20231211 since AL2023.2.20231113
<a name="new-AL2023.2.20231113-AL2023.3.20231211"></a>

 Comparing AL2023.2.20231113 version 2023.2.20231113 to AL2023.3.20231211 version [2023.3.20231211](#relnotes-2023.3.20231211).

| Package Type | Number of new packages in AL2023.3.20231211 compared to AL2023.2.20231113 |
| --- | --- |
| Source RPMs | 13 |
| Total Binary RPMs | 46 |
|  noarch binary RPMs | 20 |
|  x86\_64 binary RPMs | 13 |
|  aarch64 binary RPMs | 13 |

New packages in AL2023.3.20231211:

- ** `certbot` **
  - **RPM:**  certbot  / **Architectures:** noarch
  - **RPM:**  python3-acme  / **Architectures:** noarch
  - **RPM:**  python3-certbot  / **Architectures:** noarch
  - **RPM:**  python3-certbot-apache  / **Architectures:** noarch
  - **RPM:**  python3-certbot-dns-rfc2136  / **Architectures:** noarch
  - **RPM:**  python3-certbot-dns-route53  / **Architectures:** noarch
  - **RPM:**  python3-certbot-nginx  / **Architectures:** noarch
  - **RPM:**  python-certbot-dns-rfc2136-doc  / **Architectures:** noarch
  - **RPM:**  python-certbot-dns-route53-doc  / **Architectures:** noarch
  - **Version:** 2.6.0-4.amzn2023.0.1

- ** `ldns` **
  - **RPM:**  ldns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ldns-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ldns-doc  / **Architectures:** noarch
  - **RPM:**  ldns-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perl-ldns  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-ldns  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.8.3-2.amzn2023.0.1

- ** `libreswan` **
  - **RPM:**  libreswan
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.12-3.amzn2023

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 20.10.0-1.amzn2023.0.1

- ** `open-vmdk` **
  - **RPM:**  open-vmdk
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.3.6-1.amzn2023

- ** `python-augeas` **
  - **RPM:**  python3-augeas
  - **Architectures:** noarch
  - **Version:** 1.1.0-10.amzn2023

- ** `python-boto3` **
  - **RPM:**  python3-boto3
  - **Architectures:** noarch
  - **Version:** 1.33.6-1.amzn2023.0.1

- ** `python-botocore` **
  - **RPM:**  python3-botocore
  - **Architectures:** noarch
  - **Version:** 1.33.6-1.amzn2023.0.1

- ** `python-configargparse` **
  - **RPM:**  python3-configargparse
  - **Architectures:** noarch
  - **Version:** 1.7-1.amzn2023

- ** `python-josepy` **
  - **RPM:**  python3-josepy  / **Architectures:** noarch
  - **RPM:**  python-josepy-doc  / **Architectures:** noarch
  - **Version:** 1.13.0-6.amzn2023

- ** `python-parsedatetime` **
  - **RPM:**  python3-parsedatetime
  - **Architectures:** noarch
  - **Version:** 2.6-10.amzn2023

- ** `python-pyrfc3339` **
  - **RPM:**  python3-pyrfc3339
  - **Architectures:** noarch
  - **Version:** 1.1-16.amzn2023

- ** `python-s3transfer` **
  - **RPM:**  python3-s3transfer
  - **Architectures:** noarch
  - **Version:** 0.8.2-1.amzn2023.0.1

### AL2023.3.20231211 upgrades from AL2023.2.20231113
<a name="vercmp-AL2023.2.20231113-AL2023.3.20231211"></a>

 Comparing [2023.2.20231113](relnotes-2023.2.20231113.md) to [2023.3.20231211](#relnotes-2023.3.20231211).

| Package Type | Count |
| --- | --- |
| Source | 28 |
| Total Binary | 604 |
|  noarch binary RPMs | 372 |
|  x86\_64 binary RPMs | 116 |
|  aarch64 binary RPMs | 116 |

The full comparison of RPM package versions is below.

- ** [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html) **
  - **RPM:**  [`amazon-linux-sb-keys`](https://docs.aws.amazon.com/linux/al2023/ug/uefi-secure-boot.html)
  - **Architectures:** noarch
  - **AL2023.2.20231113 version:** 2023.1-1.amzn2023.0.3
  - **AL2023.3.20231211 version:** 2023.1-1.amzn2023.0.4

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
  - **AL2023.2.20231113 version:** 0.8-14.amzn2023.0.10
  - **AL2023.3.20231211 version:** 0.8-14.amzn2023.0.12

- ** `awscli-2` **
  - **RPM:**  awscli-2
  - **Architectures:** noarch
  - **AL2023.2.20231113 version:** 2.9.19-1.amzn2023.0.1
  - **AL2023.3.20231211 version:** 2.14.5-1.amzn2023.0.1

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 1.3.0-0.amzn2023
  - **AL2023.3.20231211 version:** 1.3.1-0.amzn2023

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 24.0.5-1.amzn2023.0.2
  - **AL2023.3.20231211 version:** 24.0.5-1.amzn2023.0.3

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
  - **AL2023.2.20231113 version:** 6.0.23-1.amzn2023.0.1
  - **AL2023.3.20231211 version:** 6.0.25-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 1.79.0-1.amzn2023
  - **AL2023.3.20231211 version:** 1.79.1-1.amzn2023

- ** `guava` **
  - **RPM:**  guava  / **Architectures:** noarch
  - **RPM:**  guava-javadoc  / **Architectures:** noarch
  - **RPM:**  guava-testlib  / **Architectures:** noarch
  - **AL2023.2.20231113 version:** 31.0.1-3.amzn2023.0.5
  - **AL2023.3.20231211 version:** 31.0.1-3.amzn2023.0.6

- ** `jbig2dec` **
  - **RPM:**  jbig2dec  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbig2dec-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jbig2dec-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 0.19-4.amzn2023.0.1
  - **AL2023.3.20231211 version:** 0.19-4.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 6.1.61-85.141.amzn2023
  - **AL2023.3.20231211 version:** 6.1.66-91.160.amzn2023

- ** `libtiff` **
  - **RPM:**  libtiff  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtiff-tools  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 4.4.0-4.amzn2023.0.16
  - **AL2023.3.20231211 version:** 4.4.0-4.amzn2023.0.17

- ** `libuv` **
  - **RPM:**  libuv  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libuv-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 1.44.1-156.amzn2023.0.2
  - **AL2023.3.20231211 version:** 1.47.0-1.amzn2023.0.1

- ** `memcached` **
  - **RPM:**  memcached  / **Architectures:** aarch64, x86\_64
  - **RPM:**  memcached-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  memcached-selinux  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 1.6.14-1.amzn2023.0.3
  - **AL2023.3.20231211 version:** 1.6.22-2.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 3.0.8-1.amzn2023.0.9
  - **AL2023.3.20231211 version:** 3.0.8-1.amzn2023.0.10

- ** [`perl`](https://docs.aws.amazon.com/linux/al2023/ug/perl.html) **
  - **RPM:**  [`perl`](https://docs.aws.amazon.com/linux/al2023/ug/perl.html)  / **Architectures:** aarch64, x86\_64
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
  - **AL2023.2.20231113 version:** 5.32.1-477.amzn2023.0.5
  - **AL2023.3.20231211 version:** 5.32.1-477.amzn2023.0.6

- ** [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 3.11.2-2.amzn2023.0.11
  - **AL2023.3.20231211 version:** 3.11.6-1.amzn2023.0.1

- ** `python-awscrt` **
  - **RPM:**  python3-awscrt
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 0.16.7-1.amzn2023.0.1
  - **AL2023.3.20231211 version:** 0.19.19-1.amzn2023.0.1

- ** `python-cryptography` **
  - **RPM:**  python3-cryptography
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 36.0.1-1.amzn2023.0.3
  - **AL2023.3.20231211 version:** 36.0.1-1.amzn2023.0.5

- ** `python-pillow` **
  - **RPM:**  python3-pillow  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-pillow-tk  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 9.4.0-2.amzn2023.0.1
  - **AL2023.3.20231211 version:** 9.4.0-2.amzn2023.0.3

- ** `python-pip` **
  - **RPM:**  python3-pip  / **Architectures:** noarch
  - **RPM:**  python3-pip-wheel  / **Architectures:** noarch
  - **AL2023.2.20231113 version:** 21.3.1-2.amzn2023.0.5
  - **AL2023.3.20231211 version:** 21.3.1-2.amzn2023.0.7

- ** `python-urllib3` **
  - **RPM:**  python3-urllib3
  - **Architectures:** noarch
  - **AL2023.2.20231113 version:** 1.25.10-5.amzn2023.0.2
  - **AL2023.3.20231211 version:** 1.25.10-5.amzn2023.0.3

- ** `shadow-utils` **
  - **RPM:**  shadow-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  shadow-utils-subid  / **Architectures:** aarch64, x86\_64
  - **RPM:**  shadow-utils-subid-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 4.9-12.amzn2023.0.2
  - **AL2023.3.20231211 version:** 4.9-12.amzn2023.0.4

- ** `squid` **
  - **RPM:**  squid
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 5.8-1.amzn2023.0.2
  - **AL2023.3.20231211 version:** 5.8-1.amzn2023.0.3

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.2.20231113 version:** 2023.2.20231113-1.amzn2023
  - **AL2023.3.20231211 version:** 2023.3.20231211-0.amzn2023

- ** `traceroute` **
  - **RPM:**  traceroute
  - **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 2.1.0-13.amzn2023.0.2
  - **AL2023.3.20231211 version:** 2.1.3-1.amzn2023

- ** `vim` **
  - **RPM:**  vim-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-data  / **Architectures:** noarch
  - **RPM:**  vim-default-editor  / **Architectures:** noarch
  - **RPM:**  vim-enhanced  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vim-filesystem  / **Architectures:** noarch
  - **RPM:**  vim-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xxd  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 9.0.2081-1.amzn2023
  - **AL2023.3.20231211 version:** 9.0.2120-1.amzn2023

- ** `wireshark` **
  - **RPM:**  wireshark-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  wireshark-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 4.0.8-2.amzn2023.0.2
  - **AL2023.3.20231211 version:** 4.0.8-2.amzn2023.0.3

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xdmx  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.2.20231113 version:** 1.20.14-26.amzn2023.0.1
  - **AL2023.3.20231211 version:** 1.20.14-26.amzn2023.0.2

## Docker container image
<a name="amis-2023.3.20231211.container-image"></a>
+ `amazon-linux-repo-cdn-2023.3.20231211-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.10`
+ `python3-pip-wheel-21.3.1-2.amzn2023.0.7`
+ `system-release-2023.3.20231211-0.amzn2023`

## Default AMI
<a name="amis-2023.3.20231211.default-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20231211-0.amzn2023` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.4` |
| `awscli-2-2.14.5-1.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.3.20231211-0.amzn2023` |
| `kernel-tools-6.1.66-91.160.amzn2023` |
| `kernel-6.1.66-91.160.amzn2023` |
| `libuv-1:1.47.0-1.amzn2023.0.1` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.10` |
| `openssl-1:3.0.8-1.amzn2023.0.10` |
| `perl-Class-Struct-0.66-477.amzn2023.0.6` |
| `perl-DynaLoader-1.47-477.amzn2023.0.6` |
| `perl-Errno-1.30-477.amzn2023.0.6` |
| `perl-Fcntl-1.13-477.amzn2023.0.6` |
| `perl-File-Basename-2.85-477.amzn2023.0.6` |
| `perl-File-stat-1.09-477.amzn2023.0.6` |
| `perl-Getopt-Std-1.12-477.amzn2023.0.6` |
| `perl-IO-1.43-477.amzn2023.0.6` |
| `perl-IPC-Open3-1.21-477.amzn2023.0.6` |
| `perl-POSIX-1.94-477.amzn2023.0.6` |
| `perl-SelectSaver-1.02-477.amzn2023.0.6` |
| `perl-Symbol-1.08-477.amzn2023.0.6` |
| `perl-if-0.60.800-477.amzn2023.0.6` |
| `perl-interpreter-4:5.32.1-477.amzn2023.0.6` |
| `perl-libs-4:5.32.1-477.amzn2023.0.6` |
| `perl-mro-1.23-477.amzn2023.0.6` |
| `perl-overload-1.31-477.amzn2023.0.6` |
| `perl-overloading-0.02-477.amzn2023.0.6` |
| `perl-subs-1.03-477.amzn2023.0.6` |
| `perl-vars-1.05-477.amzn2023.0.6` |
| `python3-awscrt-0.19.19-1.amzn2023.0.1` |
| `python3-cryptography-36.0.1-1.amzn2023.0.5` |
| `python3-pip-wheel-21.3.1-2.amzn2023.0.7` |
| `python3-urllib3-1.25.10-5.amzn2023.0.3` |
| `shadow-utils-2:4.9-12.amzn2023.0.4` |
| `system-release-2023.3.20231211-0.amzn2023` |
| `traceroute-3:2.1.3-1.amzn2023` |
| `vim-common-2:9.0.2120-1.amzn2023` |
| `vim-data-2:9.0.2120-1.amzn2023` |
| `vim-enhanced-2:9.0.2120-1.amzn2023` |
| `vim-filesystem-2:9.0.2120-1.amzn2023` |
| `vim-minimal-2:9.0.2120-1.amzn2023` |
| `xxd-2:9.0.2120-1.amzn2023` |

## Minimal AMI
<a name="amis-2023.3.20231211.minimal-ami"></a>

|  |
| --- |
| `amazon-linux-repo-s3-2023.3.20231211-0.amzn2023` |
| `amazon-linux-sb-keys-2023.1-1.amzn2023.0.4` |
| `awscli-2-2.14.5-1.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.3.20231211-0.amzn2023` |
| `kernel-6.1.66-91.160.amzn2023` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.10` |
| `openssl-1:3.0.8-1.amzn2023.0.10` |
| `python3-awscrt-0.19.19-1.amzn2023.0.1` |
| `python3-cryptography-36.0.1-1.amzn2023.0.5` |
| `python3-pip-wheel-21.3.1-2.amzn2023.0.7` |
| `python3-urllib3-1.25.10-5.amzn2023.0.3` |
| `shadow-utils-2:4.9-12.amzn2023.0.4` |
| `system-release-2023.3.20231211-0.amzn2023` |
| `vim-data-2:9.0.2120-1.amzn2023` |
| `vim-minimal-2:9.0.2120-1.amzn2023` |

## Minimal container image
<a name="amis-2023.3.20231211.minimal-container-ami"></a>
+ `amazon-linux-repo-cdn-2023.3.20231211-0.amzn2023`
+ `openssl-libs-1:3.0.8-1.amzn2023.0.10`
+ `system-release-2023.3.20231211-0.amzn2023`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
