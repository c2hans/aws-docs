---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20221207.html
---

# Amazon Linux 2023 version 2022.0.20221207 release notes
<a name="relnotes-2022.0.20221207"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20221207"></a>

Review [Comparing Amazon Linux 2 and Amazon Linux 2022](https://docs.aws.amazon.com/linux/al2022/ug/compare-al2-to-AL2022.html) for more details about the changes since Amazon Linux 2.

Amazon Linux 2022 includes the following major updates.
+ `collectd` was added to the repos.
+ As part of this release we have removed packages from the repo where newer versions have superseded older versions. For example, we have removed `ImageMagick-6.9.12.48-2.amzn2022.0.6` from the repos, as we have included the newer version `ImageMagick-6.9.12.64-1.amzn2022.0.1`. This is done as part of the tech preview cleanup and will not be done after Amazon Linux 2022 becomes Generally Available.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a `config` file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.
+ Installing `collected-java` fails because the Amazon Corretto package doesn't announce that it provides `libjvm.so`. Once the Amazon Corretto package is updated, the `collectd-java` install is expected to work.

  **Work-Around** ‐ Install manually with `rpm —nodeps -i collectd-java-5.12.0-16.amzn2022.0.1.x86_64.rpm`.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major changes since the first Tech Preview release
<a name="major-changes-20221207"></a>
+ Addressed a security issue in `openssl`. For details, see `[ALAS2022-2022-157](https://alas.aws.amazon.com/AL2022/ALAS-2022-157.html)`.
+ `Kernel` updated from 5.10 to 5.15
+ `OpenSSL` updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in Amazon Linux 2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ **Curation of packages** - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.
+ The Java ecosystem is now based on Amazon Corretto 17 rather than OpenJDK 11. Java build tools have been rebuilt to newer versions and run with Amazon Corretto.
+ The triplet for GCC and other compilers changed, indicating Amazon as the vendor.

**Kernel CONFIG\_HZ changed from `250` to `100` on both `arm64` and `x86`.**

The kernel configuration has been better optimized for memory usage and further hardened by disabling some functionality unused in Amazon EC2. Notable changes include:
+ Set `NR_CPUS=512` from `8192`
+ Remove several older filesystems and use `ext4`-only
+ Remove some physical adapters not used in Amazon EC2
+ Drop a variety of unused or old network protocols
+ Remove CDROM support
+ Remove PS2 support
+ Remove "media" and `v4l2` support
+ Drop older `NFS`/`CIFS` API versions except `nfsv3`
+ Turn on a few performance-friendly security options
+ Set `PANIC_ON_OOPS` for all hangs
+ Enable `TCMU CONFIG_TCM_USER2` Module
+ Drop unused `arm64` platforms
+ Enable `CONFIG_KEXEC_SIG`
+ Disable `CONFIG_SCHED_CORE` and `CONFIG_SCHED_SMT` on `arm64`
+ Disable `CONFIG_LDISC_AUTOLOAD`
+ Enable CAKE `qdisc` support `CONFIG_NET_SCH_CAKE`
+ Update Lustre client to `2.12.8`
+ Disable `CONFIG_KSM`

   ‐ `CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`

   ‐ `CONFIG_GCC_PLUGIN_STACKLEAK`

   ‐ `CONFIG_INIT_ON_ALLOC_DEFAULT_ON`

   ‐ `CONFIG_ZERO_CALL_USED_REGS`

   ‐ `CONFIG_KFENCE`

**Topics**
+ [Major updates](#major-updates-20221207)
+ [Major changes since the first Tech Preview release](#major-changes-20221207)
+ [Repository](#amis-2022020221207.repository)
+ [Docker container image](#amis-2022020221207.container-image)
+ [Default AMI](#amis-2022020221207.default-ami)
+ [Minimal AMI](#amis-2022020221207.minimal-ami)

## Repository
<a name="amis-2022020221207.repository"></a>

The repository includes the following packages that were added since the last release.
+ `aws-nitro-enclaves-acm-0:1.2.0-2.amzn2022.src`
+ `aws-nitro-enclaves-cli-0:1.2.1-0.amzn2022.src`
+ `collectd-0:5.12.0-16.amzn2022.0.1.src`

The repository includes the following packages that were updated since the last release.
+ `annobin-10.93-1.amzn2022.src`
+ `aws-cfn-bootstrap-2.0-20.amzn2022.src`
+ `aws-c-io-0.10.12-5.amzn2022.0.7.src`
+ `bash-5.2.9-2.amzn2022.0.1.src`
+ `chkrootkit-0.55-3.amzn2022.0.3.src`
+ `curl-7.86.0-1.amzn2022.0.1.src`
+ `dbus-1.12.24-1.amzn2022.0.1.src`
+ `dnsmasq-2.86-10.amzn2022.0.1.src`
+ `dotnet6.0-6.0.111-1.amzn2022.0.1.src`
+ `e2fsprogs-1.46.5-2.amzn2022.0.1.src`
+ `ecs-init-1.66.2-1.amzn2022.src`
+ `expat-2.5.0-1.amzn2022.0.1.src`
+ `freetype-2.12.1-3.amzn2022.src`
+ `ghostscript-9.56.1-5.amzn2022.src`
+ `git-2.38.1-1.amzn2022.0.1.src`
+ `glibc-2.34-49.amzn2022.0.3.src`
+ `golang-1.19.3-2.amzn2022.0.1.src`
+ `golist-0.10.1-11.amzn2022.0.2.src`
+ `ImageMagick-6.9.12.64-1.amzn2022.0.1.src`
+ `libksba-1.6.2-1.amzn2022.0.1.src`
+ `libldb-2.5.2-1.amzn2022.0.1.src`
+ `libtiff-4.4.0-4.amzn2022.0.2.src`
+ `libxml2-2.10.3-2.amzn2022.src`
+ `mariadb105-10.5.16-1.amzn2022.0.5.src`
+ `ncurses-6.2-4.20200222.amzn2022.0.2.src`
+ `perl-IO-Socket-SSL-2.075-1.amzn2022.0.1.src`
+ `php8.1-8.1.12-1.amzn2022.0.1.src`
+ `pkgconf-1.7.3-7.amzn2022.0.3.src`
+ `poppler-22.08.0-3.amzn2022.0.1.src`
+ `protobuf-c-1.4.1-2.amzn2022.0.1.src`
+ `python3.10-3.10.8-1.amzn2022.0.1.src`
+ `python-jwt-2.4.0-1.amzn2022.src`
+ `python-twisted-22.4.0-123.amzn2022.0.1.src`
+ `python-waitress-2.1.2-1.amzn2022.0.1.src`
+ `samba-4.16.5-0.amzn2022.0.1.src`
+ `scap-security-guide-0.1.58-1.amzn2022.0.2.src`
+ `sysstat-12.5.6-1.amzn2022.0.1.src`
+ `system-release-2022.0.20221207-0.amzn2022.src`
+ `unzip-6.0-57.amzn2022.0.1.src`
+ `vim-9.0.828-1.amzn2022.0.1.src`
+ `wireshark-3.6.8-1.amzn2022.0.1.src`
+ `xfsprogs-5.18.0-1.amzn2022.0.2.src`
+ `xmlsec1-1.2.33-3.amzn2022.0.1.src`
+ `xorg-x11-server-1.20.14-9.amzn2022.0.1.src`
+ `zlib-1.2.11-33.amzn2022.0.3.src`

## Docker container image
<a name="amis-2022020221207.container-image"></a>

The Docker container image includes the following packages that were updated since the last release.
+ `amazon-linux-repo-cdn-2022.0.20221207-0.amzn2022`
+ `bash-5.2.9-2.amzn2022.0.1`
+ `curl-minimal-7.86.0-1.amzn2022.0.1`
+ `expat-2.5.0-1.amzn2022.0.1`
+ `glibc-2.34-49.amzn2022.0.3`
+ `glibc-common-2.34-49.amzn2022.0.3`
+ `glibc-minimal-langpack-2.34-49.amzn2022.0.3`
+ `libcom_err-1.46.5-2.amzn2022.0.1`
+ `libcurl-minimal-7.86.0-1.amzn2022.0.1`
+ `libxml2-2.10.3-2.amzn2022`
+ `ncurses-base-6.2-4.20200222.amzn2022.0.2`
+ `ncurses-libs-6.2-4.20200222.amzn2022.0.2`
+ `system-release-2022.0.20221207-0.amzn2022`
+ `vim-data-9.0.828-1.amzn2022.0.1`
+ `vim-minimal-9.0.828-1.amzn2022.0.1`
+ `zlib-1.2.11-33.amzn2022.0.3`

## Default AMI
<a name="amis-2022020221207.default-ami"></a>

The default AMI includes the following packages that were added since the last release.
+ `amazon-rpm-config-221-13.amzn2022.0.2`
+ `dwz-0.14-6.amzn2022.0.1`
+ `glibc-gconv-extra-2.34-49.amzn2022.0.3`

The default AMI includes the following packages that were updated since the last release.
+ `amazon-linux-repo-s3-2022.0.20221207-0.amzn2022`
+ `aws-c-io-libs-0.10.12-5.amzn2022.0.7`
+ `aws-cfn-bootstrap-2.0-20.amzn2022`
+ `bash-5.2.9-2.amzn2022.0.1`
+ `curl-minimal-7.86.0-1.amzn2022.0.1`
+ `dbus-1.12.24-1.amzn2022.0.1`
+ `dbus-common-1.12.24-1.amzn2022.0.1`
+ `dbus-libs-1.12.24-1.amzn2022.0.1`
+ `e2fsprogs-1.46.5-2.amzn2022.0.1`
+ `e2fsprogs-libs-1.46.5-2.amzn2022.0.1`
+ `efi-srpm-macros-5-4.amzn2022.0.4`
+ `expat-2.5.0-1.amzn2022.0.1`
+ `fonts-srpm-macros-2.0.5-5.amzn2022.0.1`
+ `ghc-srpm-macros-1.5.0-4.amzn2022.0.1`
+ `glibc-2.34-49.amzn2022.0.3`
+ `glibc-all-langpacks-2.34-49.amzn2022.0.3`
+ `glibc-common-2.34-49.amzn2022.0.3`
+ `glibc-locale-source-2.34-49.amzn2022.0.3`
+ `go-srpm-macros-3.1.0-30.amzn2022`
+ `kernel-livepatch-repo-s3-2022.0.20221207-0.amzn2022`
+ `kernel-srpm-macros-1.0-14.amzn2022.0.1`
+ `libcom_err-1.46.5-2.amzn2022.0.1`
+ `libcurl-minimal-7.86.0-1.amzn2022.0.1`
+ `libldb-2.5.2-1.amzn2022.0.1`
+ `libpkgconf-1.7.3-7.amzn2022.0.3`
+ `libss-1.46.5-2.amzn2022.0.1`
+ `libxml2-2.10.3-2.amzn2022`
+ `lua-srpm-macros-1-4.amzn2022.0.1`
+ `ncurses-6.2-4.20200222.amzn2022.0.2`
+ `ncurses-base-6.2-4.20200222.amzn2022.0.2`
+ `ncurses-libs-6.2-4.20200222.amzn2022.0.2`
+ `ocaml-srpm-macros-6-6.amzn2022.0.1`
+ `openblas-srpm-macros-2-9.amzn2022.0.1`
+ `package-notes-srpm-macros-0.4-14.amzn2022`
+ `perl-srpm-macros-1-39.amzn2022.0.1`
+ `pkgconf-1.7.3-7.amzn2022.0.3`
+ `pkgconf-m4-1.7.3-7.amzn2022.0.3`
+ `pkgconf-pkg-config-1.7.3-7.amzn2022.0.3`
+ `protobuf-c-1.4.1-2.amzn2022.0.1`
+ `python-srpm-macros-3.9-41.amzn2022.0.4`
+ `qt5-srpm-macros-5.15.2-2.amzn2022.0.1`
+ `rust-srpm-macros-21-40.amzn2022`
+ `sysstat-12.5.6-1.amzn2022.0.1`
+ `system-release-2022.0.20221207-0.amzn2022`
+ `unzip-6.0-57.amzn2022.0.1`
+ `vim-common-9.0.828-1.amzn2022.0.1`
+ `vim-data-9.0.828-1.amzn2022.0.1`
+ `vim-enhanced-9.0.828-1.amzn2022.0.1`
+ `vim-filesystem-9.0.828-1.amzn2022.0.1`
+ `vim-minimal-9.0.828-1.amzn2022.0.1`
+ `xfsprogs-5.18.0-1.amzn2022.0.2`
+ `zlib-1.2.11-33.amzn2022.0.3`

## Minimal AMI
<a name="amis-2022020221207.minimal-ami"></a>

The minimal AMI includes the following packages that were updated since the last release.
+ `amazon-linux-repo-s3-2022.0.20221207-0.amzn2022`
+ `aws-c-io-libs-0.10.12-5.amzn2022.0.7`
+ `bash-5.2.9-2.amzn2022.0.1`
+ `curl-minimal-7.86.0-1.amzn2022.0.1`
+ `dbus-1.12.24-1.amzn2022.0.1`
+ `dbus-common-1.12.24-1.amzn2022.0.1`
+ `dbus-libs-1.12.24-1.amzn2022.0.1`
+ `e2fsprogs-1.46.5-2.amzn2022.0.1`
+ `e2fsprogs-libs-1.46.5-2.amzn2022.0.1`
+ `expat-2.5.0-1.amzn2022.0.1`
+ `glibc-2.34-49.amzn2022.0.3`
+ `glibc-all-langpacks-2.34-49.amzn2022.0.3`
+ `glibc-common-2.34-49.amzn2022.0.3`
+ `glibc-locale-source-2.34-49.amzn2022.0.3`
+ `kernel-livepatch-repo-s3-2022.0.20221207-0.amzn2022`
+ `libcom_err-1.46.5-2.amzn2022.0.1`
+ `libcurl-minimal-7.86.0-1.amzn2022.0.1`
+ `libss-1.46.5-2.amzn2022.0.1`
+ `libxml2-2.10.3-2.amzn2022`
+ `ncurses-6.2-4.20200222.amzn2022.0.2`
+ `ncurses-base-6.2-4.20200222.amzn2022.0.2`
+ `ncurses-libs-6.2-4.20200222.amzn2022.0.2`
+ `system-release-2022.0.20221207-0.amzn2022`
+ `vim-data-9.0.828-1.amzn2022.0.1`
+ `vim-minimal-9.0.828-1.amzn2022.0.1`
+ `xfsprogs-5.18.0-1.amzn2022.0.2`
+ `zlib-1.2.11-33.amzn2022.0.3`
