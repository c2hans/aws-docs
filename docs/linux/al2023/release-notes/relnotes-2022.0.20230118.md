---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20230118.html
---

# Amazon Linux 2023 version 2022.0.20230118 release notes
<a name="relnotes-2022.0.20230118"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20230118"></a>

Review [Comparing Amazon Linux 2 and Amazon Linux 2022](https://docs.aws.amazon.com/linux/al2022/ug/compare-al2-to-AL2022.html) for more details about the changes since Amazon Linux 2.

Amazon Linux 2022 includes the following major updates.
+ As part of this release we have removed packages from the repo where newer versions have superseded older versions. For example, we have removed `ImageMagick-6.9.12.48-2.amzn2022.0.6` from the repos, as we have included the newer version `ImageMagick-6.9.12.64-1.amzn2022.0.1`. This is done as part of the tech preview cleanup and will not be done after Amazon Linux 2022 becomes Generally Available.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can [change SELinux settings to enforced mode](https://docs.aws.amazon.com/linux/al2022/ug/enforcing-mode.html) either using `cloud-init`, or using the command line by executing the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
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
<a name="major-changes-20230118"></a>
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

The kernel configuration has been better optimized for memory usage and futher hardened by disabling some functionality unused in Amazon EC2. Notable changes include:
+ `CONFIG_NR_CPUS=512` was changed from `CONFIG_NR_CPUS=8192`.
+ Removed several older filesystems and use `ext4`-only
+ Removed some physical adapters not used in Amazon EC2
+ Removed a variety of unused or old network protocols
+ Removed CDROM support
+ Removed PS2 support
+ Removed "media" and `v4l2` support
+ Removed older `NFS`/`CIFS` API versions, except `nfsv3`
+ Turned on a few performance-friendly security options.
+ The `CONFIG_PANIC_ON_OOPS` option is now turned on for all hangs.
+ The `CONFIG_TCM_USER2` option is now enabled, which enables TCMU.
+ Removed unused `arm64` platforms.
+ Enabled `CONFIG_KEXEC_SIG`

  The `CONFIG_SCHED_CORE` and `CONFIG_SCHED_SMT` options are disabled on the `arm64` architecture.
+ Disabled `CONFIG_LDISC_AUTOLOAD`
+ Enabled CAKE `qdisc` support `CONFIG_NET_SCH_CAKE`
+ Updated Lustre client to `2.12.8`
+ Disabled `CONFIG_KSM`

   ‐ `CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`

   ‐ `CONFIG_GCC_PLUGIN_STACKLEAK`

   ‐ `CONFIG_INIT_ON_ALLOC_DEFAULT_ON`

   ‐ `CONFIG_ZERO_CALL_USED_REGS`

   ‐ `CONFIG_KFENCE`

**Topics**
+ [Major updates](#major-updates-20230118)
+ [Major changes since the first Tech Preview release](#major-changes-20230118)
+ [Repository](#amis-2022020230118.repository)
+ [Docker container image](#amis-2022020230118.container-image)
+ [Default AMI](#amis-2022020230118.default-ami)
+ [Minimal AMI](#amis-2022020230118.minimal-ami)

## Repository
<a name="amis-2022020230118.repository"></a>

The repository includes the following packages that were removed since the last release.
+ `flatpak-1.12.4-1.amzn2022.0.1.src`
+ `flatpak-builder-1.2.2-1.amzn2022.0.1.src`
+ `ostree-2021.5-2.amzn2022.0.4.src`
+ `postgresql13-13.7-1.amzn2022.0.5.src`
+ `postgresql14-14.3-2.amzn2022.0.2.src`
+ `qt5-5.15.2-2.amzn2022.0.1.src`

The repository includes the following packages that were updated since the last release.

|  |
| --- |
| `amazon-efs-utils-1.34.4-1.amzn2022.src` |
| `amazon-rpm-config-228-3.amzn2022.0.1.src` |
| `apr-1.7.0-16.amzn2022.0.1.src` |
| `apr-util-1.6.1-16.amzn2022.0.2.src` |
| `bash-5.2.15-1.amzn2022.0.1.src` |
| `bcel-6.5.0-3.amzn2022.0.1.src` |
| `biber-2.17-5.amzn2022.0.1.src` |
| `binutils-2.39-6.amzn2022.0.3.src` |
| `ca-certificates-2021.2.50-1.0.amzn2022.0.4.src` |
| `chrony-4.3-1.amzn2022.0.1.src` |
| `clang-15.0.6-3.amzn2022.0.1.src` |
| `compiler-rt-15.0.6-2.amzn2022.src` |
| `cpio-2.13-13.amzn2022.0.1.src` |
| `curl-7.87.0-2.amzn2022.0.1.src` |
| `cyrus-sasl-2.1.27-18.amzn2022.0.2.src` |
| `ecs-init-1.68.0-1.amzn2022.src` |
| `elfutils-0.188-3.amzn2022.0.1.src` |
| `emacs-28.1-2.amzn2022.0.1.src` |
| `gcc-11.3.1-4.amzn2022.0.1.src` |
| `glibc-2.34-52.amzn2022.0.1.src` |
| `gnu-efi-3.0.11-9.amzn2022.0.1.src` |
| `grub2-2.06-42.amzn2022.0.2.src` |
| `java-1.8.0-amazon-corretto-1.8.0_362.b08-1.amzn2022.src` |
| `java-11-amazon-corretto-11.0.18+10-1.amzn2022.src` |
| `java-17-amazon-corretto-17.0.6+10-1.amzn2022.1.src` |
| `krb5-1.19.2-13.amzn2022.0.1.src` |
| `libclc-15.0.6-1.amzn2022.0.2.src` |
| `libdwarf-0.5.0-1.amzn2022.0.1.src` |
| `libomp-15.0.6-1.amzn2022.0.2.src` |
| `libpq-15.0-2.amzn2022.src` |
| `libtasn1-4.19.0-1.amzn2022.src` |
| `lld-15.0.6-1.amzn2022.0.2.src` |
| `lldb-15.0.6-1.amzn2022.0.2.src` |
| `llvm-15.0.6-2.amzn2022.0.1.src` |
| `mariadb105-10.5.16-1.amzn2022.0.6.src` |
| `nginx-1.22.1-1.amzn2022.0.1.src` |
| `patchelf-0.17.0-1.amzn2022.0.1.src` |
| `perl-DBD-Pg-3.14.2-3.amzn2022.0.3.src` |
| `php8.1-8.1.12-1.amzn2022.0.2.src` |
| `pkgconf-1.8.0-4.amzn2022.src` |
| `postfix-3.7.2-4.amzn2022.0.3.src` |
| `python3.10-3.10.9-1.amzn2022.0.1.src` |
| `python3.9-3.9.16-1.amzn2022.0.1.src` |
| `python-lit-15.0.6-1.amzn2022.src` |
| `python-lxml-4.7.1-3.amzn2022.src` |
| `python-psycopg2-2.8.6-3.amzn2022.0.2.src` |
| `ruby3.1-3.1.3-173.amzn2022.0.1.src` |
| `rust-1.66.1-1.amzn2022.0.2.src` |
| `rust-toolset-1.66.1-1.amzn2022.0.1.src` |
| `samba-4.16.7-0.amzn2022.0.1.src` |
| `sphinx-2.2.11-24.amzn2022.0.2.src` |
| `spirv-headers-1.5.5-41.amzn2022.src` |
| `spirv-llvm-translator-15.0.0-2.amzn2022.0.1.src` |
| `sqlite-3.40.0-1.amzn2022.0.1.src` |
| `system-release-2022.0.20230118-0.amzn2022.src` |
| `texlive-2021-59.amzn2022.0.1.src` |
| `texlive-base-20210325-52.amzn2022.0.1.src` |
| `tzdata-2022g-1.amzn2022.0.1.src` |
| `unbound-1.16.3-2.amzn2022.src` |
| `vim-9.0.1006-1.amzn2022.0.1.src` |
| `wireshark-4.0.2-1.amzn2022.0.1.src` |

## Docker container image
<a name="amis-2022020230118.container-image"></a>

The Docker container image includes the following packages that were added since the last release.

|  |
| --- |
| `amazon-linux-repo-cdn-2022.0.20230118-0.amzn2022` |
| `bash-5.2.15-1.amzn2022.0.1` |
| `ca-certificates-2021.2.50-1.0.amzn2022.0.4` |
| `curl-minimal-7.87.0-2.amzn2022.0.1.aarch64` |
| `elfutils-default-yama-scope-0.188-3.amzn2022.0` |
| `elfutils-libelf-0.188-3.amzn2022.0.1` |
| `elfutils-libs-0.188-3.amzn2022.0.1` |
| `glibc-2.34-52.amzn2022.0.1` |
| `glibc-common-2.34-52.amzn2022.0.1` |
| `glibc-minimal-langpack-2.34-52.amzn2022.0.1` |
| `krb5-libs-1.19.2-13.amzn2022.0.1` |
| `libcurl-minimal-7.87.0-2.amzn2022.0.1` |
| `libgcc-11.3.1-4.amzn2022.0.1` |
| `libgomp-11.3.1-4.amzn2022.0.1` |
| `libstdc-11.3.1-4.amzn2022.0.1` |
| `libtasn1-4.19.0-1.amzn2022` |
| `python3-3.9.16-1.amzn2022.0.1` |
| `python3-libs-3.9.16-1.amzn2022.0.1` |
| `sqlite-libs-3.40.0-1.amzn2022.0.1` |
| `system-release-2022.0.20230118-0.amzn2022` |
| `tzdata-2022g-1.amzn2022.0.1` |
| `vim-data-9.0.1006-1.amzn2022.0.1` |
| `vim-minimal-9.0.1006-1.amzn2022.0.1` |

## Default AMI
<a name="amis-2022020230118.default-ami"></a>

The Default AMI includes the following packages that were added since the last release.

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20230118-0.amzn2022` |
| `amazon-rpm-config-228-3.amzn2022.0` |
| `bash-5.2.15-1.amzn2022.0.1` |
| `binutils-2.39-6.amzn2022.0.3` |
| `ca-certificates-2021.2.50-1.0.amzn2022.0.4` |
| `chrony-4.3-1.amzn2022.0.1` |
| `cpio-2.13-13.amzn2022.0.1` |
| `curl-minimal-7.87.0-2.amzn2022.0.1` |
| `cyrus-sasl-lib-2.1.27-18.amzn2022.0.2` |
| `cyrus-sasl-plain-2.1.27-18.amzn2022.0.2` |
| `glibc-2.34-52.amzn2022.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2022.0.1` |
| `glibc-common-2.34-52.amzn2022.0.1` |
| `glibc-gconv-extra-2.34-52.amzn2022.0.1` |
| `glibc-locale-source-2.34-52.amzn2022.0.1` |
| `grub2-common-2.06-42.amzn2022.0.2` |
| `grub2-efi-x64-ec2-2.06-42.amzn2022.0.2` |
| `grub2-pc-modules-2.06-42.amzn2022.0.2` |
| `grub2-tools-2.06-42.amzn2022.0.2` |
| `grub2-tools-minimal-2.06-42.amzn2022.0.2` |
| `kernel-livepatch-repo-s3-2022.0.20230118-0.amzn2022` |
| `krb5-libs-1.19.2-13.amzn2022.0.1` |
| `libcurl-minimal-7.87.0-2.amzn2022.0.1` |
| `libgcc-11.3.1-4.amzn2022.0.1` |
| `libgomp-11.3.1-4.amzn2022.0.1` |
| `libpkgconf-1.8.0-4.amzn2022` |
| `libstdc-11.3.1-4.amzn2022.0.1` |
| `libtasn1-4.19.0-1.amzn2022` |
| `pkgconf-1.8.0-4.amzn2022` |
| `pkgconf-m4-1.8.0-4.amzn2022` |
| `pkgconf-pkg-config-1.8.0-4.amzn2022` |
| `python3-3.9.16-1.amzn2022.0.1` |
| `python3-libs-3.9.16-1.amzn2022.0.1` |
| `sqlite-libs-3.40.0-1.amzn2022.0.1` |
| `system-release-2022.0.20230118-0.amzn2022` |
| `tzdata-2022g-1.amzn2022.0.1` |
| `vim-common-9.0.1006-1.amzn2022.0.1` |
| `vim-data-9.0.1006-1.amzn2022.0.1` |
| `vim-enhanced-9.0.1006-1.amzn2022.0.1` |
| `vim-filesystem-9.0.1006-1.amzn2022.0.1` |
| `vim-minimal-9.0.1006-1.amzn2022.0.1` |

## Minimal AMI
<a name="amis-2022020230118.minimal-ami"></a>

The Minimal AMI includes the following packages that were added since the last release.

|  |
| --- |
| `amazon-linux-repo-s3-2022.0.20230118-0.amzn2022` |
| `bash-5.2.15-1.amzn2022.0.1` |
| `ca-certificates-2021.2.50-1.0.amzn2022.0.4` |
| `chrony-4.3-1.amzn2022.0.1.` |
| `cpio-2.13-13.amzn2022.0.1.` |
| `curl-minimal-7.87.0-2.amzn2022.0.1` |
| `cyrus-sasl-lib-2.1.27-18.amzn2022.0.2` |
| `elfutils-default-yama-scope-0.188-3.amzn2022.0.1` |
| `elfutils-libelf-0.188-3.amzn2022.0.1` |
| `elfutils-libs-0.188-3.amzn2022.0.1` |
| `glibc-2.34-52.amzn2022.0.1` |
| `glibc-all-langpacks-2.34-52.amzn2022.0.1` |
| `glibc-common-2.34-52.amzn2022.0.1` |
| `glibc-locale-source-2.34-52.amzn2022.0.1` |
| `grub2-common-2.06-42.amzn2022.0.2` |
| `grub2-efi-x64-ec2-2.06-42.amzn2022.0.2` |
| `grub2-pc-modules-2.06-42.amzn2022.0.2` |
| `grub2-tools-2.06-42.amzn2022.0.2` |
| `grub2-tools-minimal-2.06-42.amzn2022.0.2` |
| `kernel-livepatch-repo-s3-2022.0.20230118-0.amzn2022` |
| `krb5-libs-1.19.2-13.amzn2022.0.1` |
| `libcurl-minimal-7.87.0-2.amzn2022.0.1` |
| `libgcc-11.3.1-4.amzn2022.0.1` |
| `libgomp-11.3.1-4.amzn2022.0.1` |
| `libstdc-11.3.1-4.amzn2022.0.1` |
| `libtasn1-4.19.0-1.amzn2022` |
| `python3-3.9.16-1.amzn2022.0.1` |
| `python3-libs-3.9.16-1.amzn2022.0.1` |
| `sqlite-libs-3.40.0-1.amzn2022.0.1.` |
| `system-release-2022.0.20230118-0.amzn2022` |
| `tzdata-2022g-1.amzn2022.0.1` |
| `vim-data-9.0.1006-1.amzn2022.0.1` |
| `vim-minimal-9.0.1006-1.amzn2022.0.1` |
