---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230517.html
---

# Amazon Linux 2023 version 2023.0.20230517 release notes
<a name="relnotes-2023.0.20230517"></a>

This topic includes release notes for the 2023.0.20230517 version of AL2023.

## Major updates
<a name="major-updates-20230517"></a>

This release represents an update to the General Availability (GA) release of Amazon Linux 2023 (AL2023). AL2023 is the next generation of Amazon Linux. It comes with 5 years of support and brings features like Deterministic Updates, better optimizations for Graviton processors and others into Amazon Linux. AL2023 is ready for customer production workloads, and customers are encouraged to start migrations from previous versions of Amazon Linux today.

See the [Amazon Linux What's New Post](https://aws.amazon.com/about-aws/whats-new/2023/03/amazon-linux-2023/) for more information about AL2023.

AL2023 includes the following major updates.
+ AL2023 now uses the AWS TimeSync time sources by default.
+ For an in-depth look at the changes since Amazon Linux 2, see [Comparing Amazon Linux 2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Known Issues**
+ AL2023 is not yet FIPS certified. It is in process of being certified for `FIPS 140-3`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, refer to [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.

**Topics**
+ [Major updates](#major-updates-20230517)
+ [Repository](#amis-2023.0.20230517.repository)
+ [Default AMI](#amis-2023020230517.default-ami)
+ [Minimal AMI](#amis-2023020230517.minimal-ami)

## Repository
<a name="amis-2023.0.20230517.repository"></a>

### AL2023.0.20230517 upgrades from AL2023.0.20230503
<a name="vercmp-AL2023.0.20230503-AL2023.0.20230517"></a>

 Comparing [2023.0.20230503](relnotes-2023.0.20230503.md) to [2023.0.20230517](#relnotes-2023.0.20230517).

| Package Type | Count |
| --- | --- |
| Source | 10 |
| Total Binary | 510 |
|  noarch binary RPMs | 392 |
|  x86\_64 binary RPMs | 59 |
|  aarch64 binary RPMs | 59 |

The full comparison of RPM package versions is below.

- ** `chrony` **
  - **RPM:**  amazon-chrony-config  / **Architectures:** noarch
  - **RPM:**  chrony  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230503 version:** 4.3-1.amzn2023.0.2
  - **AL2023.0.20230517 version:** 4.3-1.amzn2023.0.3

- ** `docker` **
  - **RPM:**  docker
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230503 version:** 20.10.17-1.amzn2023.0.6
  - **AL2023.0.20230517 version:** 20.10.23-1.amzn2023.0.1

- ** `ec2-utils` **
  - **RPM:**  ec2-utils
  - **Architectures:** noarch
  - **AL2023.0.20230503 version:** 2.0.1-1.amzn2023.0.2
  - **AL2023.0.20230517 version:** 2.1.0-1.amzn2023.0.1

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230503 version:** 1.70.2-1.amzn2023
  - **AL2023.0.20230517 version:** 1.71.0-1.amzn2023

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
  - **AL2023.0.20230503 version:** 2.39.2-1.amzn2023.0.1
  - **AL2023.0.20230517 version:** 2.40.1-1.amzn2023.0.1

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
  - **AL2023.0.20230503 version:** 6.1.25-37.47.amzn2023
  - **AL2023.0.20230517 version:** 6.1.27-43.48.amzn2023

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **AL2023.0.20230503 version:** 3.0.8-1.amzn2023.0.1
  - **AL2023.0.20230517 version:** 3.0.8-1.amzn2023.0.2

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
  - **AL2023.0.20230503 version:** 5.32.1-477.amzn2023.0.3
  - **AL2023.0.20230517 version:** 5.32.1-477.amzn2023.0.4

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
  - **AL2023.0.20230503 version:** 252.4-1161.amzn2023.0.3
  - **AL2023.0.20230517 version:** 252.4-1161.amzn2023.0.4

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.0.20230503 version:** 2023.0.20230503-0.amzn2023
  - **AL2023.0.20230517 version:** 2023.0.20230517-0.amzn2023

## Default AMI
<a name="amis-2023020230517.default-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-chrony-config-4.3-1.amzn2023.0.3` |
| `amazon-linux-repo-cdn-2023.0.20230517-0.amzn2023` |
| `amazon-linux-repo-s3-2023.0.20230517-0.amzn2023` |
| `chrony-4.3-1.amzn2023.0.3` |
| `ec2-utils-2.1.0-1.amzn2023.0.1` |
| `kernel-livepatch-repo-s3-2023.0.20230517-0.amzn2023` |
| `logrotate-3.20.1-2.amzn2023.0.3` |
| `oniguruma-6.9.7.1-1.amzn2023.0.2` |
| `openssl-1:3.0.8-1.amzn2023.0.2` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.2` |
| `perl-Class-Struct-0.66-477.amzn2023` |
| `perl-DynaLoader-1.47-477.amzn2023.0.4` |
| `perl-Errno-1.30-477.amzn2023.0.4` |
| `perl-Fcntl-1.13-477.amzn2023.0.4` |
| `perl-File-Basename-2.85-477.amzn2023` |
| `perl-File-stat-1.09-477.amzn2023.0.4` |
| `perl-Getopt-Std-1.12-477.amzn2023.0.4` |
| `perl-if-0.60.800-477.amzn2023.0.4` |
| `perl-interpreter-4:5.32.1-477.amzn2023.0.4` |
| `perl-IO-1.43-477.amzn2023.0.4` |
| `perl-IPC-Open3-1.21-477.amzn2023.0.4` |
| `perl-libs-4:5.32.1-477.amzn2023.0.4` |
| `perl-mro-1.23-477.amzn2023.0.4` |
| `perl-overload-1.31-477.amzn2023.0.4` |
| `perl-overloading-0.02-477.amzn2023.0.4` |
| `perl-POSIX-1.94-477.amzn2023.0.4` |
| `perl-SelectSaver-1.02-477.amzn2023.0.4` |
| `perl-subs-1.03-477.amzn2023.0.4` |
| `perl-Symbol-1.08-477.amzn2023.0.4` |
| `perl-vars-1.05-477.amzn2023.0.4` |
| `systemd-252.4-1161.amzn2023.0.4` |
| `systemd-libs-252.4-1161.amzn2023.0.4` |
| `systemd-networkd-252.4-1161.amzn2023.0.4` |
| `systemd-pam-252.4-1161.amzn2023.0.4` |
| `systemd-resolved-252.4-1161.amzn2023.0.4` |
| `systemd-udev-252.4-1161.amzn2023.0.4` |
| `system-release-2023.0.20230517-0.amzn2023` |

## Minimal AMI
<a name="amis-2023020230517.minimal-ami"></a>

The following packages have been **updated**.

|  |
| --- |
| `amazon-chrony-config-4.3-1.amzn2023.0.3` |
| `amazon-linux-repo-s3-2023.0.20230517-0.amzn2023` |
| `ca-certificates-2023.2.60-1.0.amzn2023.0.2` |
| `chrony-4.3-1.amzn2023.0.3` |
| `ec2-utils-2.1.0-1.amzn2023.0.1` |
| `gnutls-3.7.8-360.amzn2023.0.4` |
| `gpg-pubkey-d832c631-63977702` |
| `grub2-common-1:2.06-61.amzn2023.0.6` |
| `grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.6` |
| `grub2-pc-modules-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-minimal-1:2.06-61.amzn2023.0.6` |
| `grub2-tools-1:2.06-61.amzn2023.0.6` |
| `kernel-livepatch-repo-s3-2023.0.20230517-0.amzn2023` |
| `kernel-6.1.27-43.48.amzn2023` |
| `libxml2-2.10.4-1.amzn2023.0.1` |
| `openssl-libs-1:3.0.8-1.amzn2023.0.2` |
| `openssl-1:3.0.8-1.amzn2023.0.2` |
| `python3-rpm-4.16.1.3-12.amzn2023.0.6` |
| `rpm-build-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-selinux-4.16.1.3-12.amzn2023.0.6` |
| `rpm-plugin-systemd-inhibit-4.16.1.3-12.amzn2023.0.6` |
| `rpm-sign-libs-4.16.1.3-12.amzn2023.0.6` |
| `rpm-4.16.1.3-12.amzn2023.0.6` |
| `system-release-2023.0.20230517-0.amzn2023` |
| `systemd-libs-252.4-1161.amzn2023.0.4` |
| `systemd-networkd-252.4-1161.amzn2023.0.4` |
| `systemd-pam-252.4-1161.amzn2023.0.4` |
| `systemd-resolved-252.4-1161.amzn2023.0.4` |
| `systemd-udev-252.4-1161.amzn2023.0.4` |
| `systemd-252.4-1161.amzn2023.0.4` |
