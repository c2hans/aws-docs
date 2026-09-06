---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.7.20250331.html
---

# Amazon Linux 2023 version 2023.7.20250331 release notes
<a name="relnotes-2023.7.20250331"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.7.20250331.

**Topics**
+ [Major updates](#major-updates-2023.7.20250331)
+ [Repository](#amis-2023.7.20250331.repository)
+ [Image Updates](#ami-updates-2023.7.20250331)
+ [Contact us](#amis-2023.7.20250331.contact-us)

## Major updates
<a name="major-updates-2023.7.20250331"></a>

This is the seventh quarterly release of AL2023. AL2023 is the current version of Amazon Linux, bringing features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+ AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.
+  Running kernel 6.12 with `fips=1` is not supported at this point in time and will be enabled in a subsequent release. If you’re required to run in FIPS mode please use kernel 6.1. For more information on FIPS mode, see [Enable FIPS Mode on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html).

**Notable updates**
+  *Graphical desktop*: Amazon Linux 2023 now provides an optional, lightweight, cloud-optimized graphical interface based on GNOME. This modern desktop environment delivers enhanced productivity features with built-in tools like Firefox for secure browsing, while maintaining seamless AWS integration and Amazon DCV support for remote access. For more information, see: [AL2023 Graphical Desktop](https://docs.aws.amazon.com/linux/al2023/ug/graphical-desktop-al2023.html)
+  *New kernel LTS version 6.12*: Amazon Linux 2023 now provides kernel 6.12, the latest LTS kernel released by the Linux kernel community, as a new kernel option. Customers can choose to run AMIs with kernel 6.12 as a default by querying the `/aws/service/ami-amazon-linux-latest/al2023-ami{-minimal}-kernel-6.12-{x86_64,arm64}` SSM parameter in each region.
**Note**
 Running kernel 6.12 with `fips=1` is not supported at this point in time and will be enabled in a subsequent release. If you’re required to run in FIPS mode please use kernel 6.1. For more information on FIPS mode, see [Enable FIPS Mode on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/fips-mode.html).

****Updating an existing instance to kernel 6.12****

  1.  Ensure you are running the 2023.7.20250331 release or later. For more information on updating AL2023, see [Updating AL2023](https://docs.aws.amazon.com/linux/al2023/ug/updating.html) in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

  1. Install the `kernel6.12` package.

     ```
     $ sudo dnf install kernel6.12
     ```

  1. Set kernel 6.12 as the default kernel.

     ```
     $ version=$(rpm -q --qf '%{version}-%{release}.%{arch}\n' kernel6.12 | sort -V | tail -1)
     $ sudo grubby --set-default "/boot/vmlinuz-$version"
     ```

  1. Reboot the instance.

     ```
     $ sudo reboot
     ```
+  OpenSSL has been updated to version 3.2.2. This update provides significant performance improvements, and some changes to how the OpenSSL FIPS provider is managed. For more information, see the [Security](https://docs.aws.amazon.com/linux/al2023/ug/security.html) section of the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/), and the upstream [OpenSSL 3.2 Release Notes](https://openssl-library.org/news/openssl-3.2-notes/). This resolves [GitHub issue \#819](https://github.com/amazonlinux/amazon-linux-2023/issues/819).
+  The gcc compiler collection version 14.2.1 is now available in the form of a set of namespaced packages `gcc14`, `gcc14-c++` , `gcc14-gfortran`, etc. These new GCC 14 packages and can co-exist with AL2023's default `gcc` (11.5.0). The system wide runtime shared libraries (`libgcc_s`, `libstdc++`, `libgfortran`, etc.) have been updated to version 14 which is fully backwards compatible. The `clang` toolchaing has been updated to use the `gcc14` runtime libraries, which fixes some issues with using 16-bit floating point types. An updated `llvm`/`clang` toolchain will be provided in a subsequent release.
+  To better support multiple versions of NodeJS in Amazon Linux, we are progressively migrating our NodeJS packages to use the `alternatives` system. This release contains the change to the `nodejs20` package. Switching to alternatives will allow multiple versions of NodeJS to be concurrently installed, and a single command to be used to select which NodeJS version's configuration and binaries (such as `npm` and `node`) are used. To support this change, there are changes to what paths the NodeJS binaries, globally installed NodeJS modules, and configuration files are in. Existing globally installed modules will be preserved across the update. This change will be non-disruptive for the majority of customers.
+  *ClamAV 1.4* is now available in the `clamav1.4` package, Amazon Linux 2023 will transition to ClamAV 1.4 being the default version of ClamAV around the September/October 2025 timeline. Since the `clamav1.4` package provides new versions of shared libraries, any applications that links to any of these libraries will need to be re-linked or rebuilt. The older clamav (v0.103.12) packages will remain available in the repositories for a period of time after ClamAV 1.4 is made the default, but will not receive any further updates or security fixes. To ensure continued security and support, customers should migrate to `clamav1.4` as soon as possible. Resolves [GitHub issue \#874](https://github.com/amazonlinux/amazon-linux-2023/issues/874).
+

**AWS Tools updates**
  + AWS CLI has been updated from 2.15.30 to 2.17.18
  + AWS Nitro Enclaves CLI has been updated from 1.3.3 to 1.4.0
  + `ecs-init` has been updated from 1.87.0 to 1.90.0
  + The Amazon CloudWatch Logs agent, `ecs-service-connect-agent`, `aws-kinesis-agent`, `amazon-ssm-agent`, `credentials-fetcher` , and `aws-cfn-bootstrap` have all received minor updates
+

**Container runtime updates**
  +  `containerd` has been updated from 1.7.22 to 1.7.25, coming with a number of stability updates.
    + Bug fix panic due to nil dereference cgroups v2
    + Bug fix "invalid metric type" error message for cgroup v1
    + Bug fix retry logic and concurrency issue with http fallback when resolving images
    + Bug fix to avoid locking in CNI plugins before tearing down pod network
    + Bug fix for a possible race condition during GC of snapshots when client retries pull operations
  +  Docker has been updated from 25.0.6 to 25.0.8, bringing several stability improvements. For more information, see the upstream release notes for [25.0.7](https://github.com/moby/moby/releases/tag/v25.0.7) and [25.0.8](https://github.com/moby/moby/releases/tag/v25.0.8).
    + Explicitly disable nvidia device injection for `--gpus=0` by [\#48493](https://github.com/moby/moby/pull/48493)
    + Bug fix for memory leak issue which causes each meter counter invocation to create a new instrument when the meter provider is not set [\#48711](https://github.com/moby/moby/pull/48711)
    + Bug fix for network chains when using live-restore [\#48717](https://github.com/moby/moby/pull/48717)
    + Bug fix anonymous volume not being labeled [\#48787](https://github.com/moby/moby/pull/48787)
    + Additionally, we have patched a security issue by upgrading the Go jwt build time library [\#49048](https://github.com/moby/moby/pull/49048)
  +  `nerdctl` has been updated from 1.7.7 to 2.0.3, bringing multiple stability and feature updates. While there is a major version update between these two versions, it only impacts rootless use cases which Amazon Linux 2023 was not shipping. Most of the updates involve adding support for several new commands, command arguments, or features which enhance `nerdctl’s` compatibility with the `docker` CLI interface. The update to version 2.0.0 is quite substantial, and for more information see the [full upstream release notes for 2.0.0](https://github.com/containerd/nerdctl/releases/tag/v2.0.0), [2.0.1](https://github.com/containerd/nerdctl/releases/tag/v2.0.1), [2.0.2](https://github.com/containerd/nerdctl/releases/tag/v2.0.2), and [2.0.3](https://github.com/containerd/nerdctl/releases/tag/v2.0.3).
  +  `runc` has been updated from 1.1.14 to 1.2.4. For more information see the upstream release notes for [v1.1.15](https://github.com/opencontainers/runc/releases/tag/v1.1.15), [v1.2.0](https://github.com/opencontainers/runc/releases/tag/v1.2.0), [v1.2.1](https://github.com/opencontainers/runc/releases/tag/v1.2.1), [v1.2.2](https://github.com/opencontainers/runc/releases/tag/v1.2.2), [v1.2.3](https://github.com/opencontainers/runc/releases/tag/v1.2.3), and [v1.2.4](https://github.com/opencontainers/runc/releases/tag/v1.2.4).
    + Addressed some performance impacts related to the mitigation of [CVE-2019-5736](https://github.com/advisories/GHSA-gxmr-w5mj-v8hh).
    +  Enhanced security around the usage of `os.MkdirAll` (related to [CVE-2024-45310](https://github.com/opencontainers/runc/security/advisories/GHSA-jfvp-7x6p-h2pv)) by using the [https://github.com/cyphar/filepath-securejoin](https://github.com/cyphar/filepath-securejoin) library.
    + Bug fix mount leak race condition.
    +  Update of the [https://github.com/cilium/ebpf](https://github.com/cilium/ebpf) library to v0.16.0, which contains several bug fixes.
    + Enhanced compatibility with SELinux
  + `finch` has been updated from 1.3.0 to 1.7.1. For more information, see the [upstream release notes](https://runfinch.com/docs/changelog/#171-2025-03-19).
  + `soci-snapshotter` has been updated from 0.7.0 to 0.9.0 bringing two new features: `systemd` socket activation, and ID-mapped layer support. For more information, see the upstream release notes for [v0.8.0](https://github.com/awslabs/soci-snapshotter/releases/tag/v0.9.0) and [v0.9.0](https://github.com/awslabs/soci-snapshotter/releases/tag/v0.9.0).
+

**Database updates**
  +  PostgreSQL version 17 has been added (resolves [GitHub issue \#860](https://github.com/amazonlinux/amazon-linux-2023/issues/860)).
  + PostgreSQL 15 has been updated to 15.12
  + PostgreSQL 16 has been updated to 16.8
  +  Valkey has been added, and AL2023 begins its transition from Redis to Valkey. For more information, see [Tutorial: Redis 6 to Valkey Transition on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/redis6-to-valkey-al2023.html) in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/). (resolves [GitHub issue \#833](https://github.com/amazonlinux/amazon-linux-2023/issues/833))
+

**Library updates**
  +  To better support a modern desktop environment, all usage of the `libsoup` library has been migrated to `libsoup3` . Any customer usage of `libsoup` should be migrated to `libsoup3` in order to maintain compatibility with OS provided libraries, as both `libsoup` and `libsoup3` cannot be used concurrently by the same process.
  + `glib2` has been updated from 2.74.7 to 2.82.2
  + GnuTLS has been updated from 3.8.0 to 3.8.2
  +  gstreamer has been added (resolves [GitHub issue \#241](https://github.com/amazonlinux/amazon-linux-2023/issues/241)
  + `pam_radius` has been added (resolves [GitHub issue \#467](https://github.com/amazonlinux/amazon-linux-2023/issues/467))
+  NVIDIA drivers are available for Amazon Linux 2023. By installing the `nvidia-release` package, a yum repository will be enabled which contains the NVIDIA drivers.
+ OpenDKIM has been added (resolves [GitHub issue \#337](https://github.com/amazonlinux/amazon-linux-2023/issues/337))
+

**Programming Languages**
  +  GoLang has been updated from 1.22 to 1.24. For more information, see the upstream release notes for [GoLang 1.23](https://tip.golang.org/doc/go1.23) and [GoLang 1.24](https://tip.golang.org/doc/go1.24).
  +  PHP 8.4 has been added, and PHP 8.1, 8.2, and 8.3 have received minor updates. (Resolves [GitHub issue \#844](https://github.com/amazonlinux/amazon-linux-2023/issues/844), [GitHub issue \#866](https://github.com/amazonlinux/amazon-linux-2023/issues/866), and [GitHub issue \#887"](https://github.com/amazonlinux/amazon-linux-2023/issues/887))
  +  Python 3.12 has been added, and both Python 3.9 and 3.11 have received updates. (Resolves [GitHub issue \#405](https://github.com/amazonlinux/amazon-linux-2023/issues/405) and [GitHub issue \#483](https://github.com/amazonlinux/amazon-linux-2023/issues/483))
  + Rust has been updated from 1.68.2 to 1.84.0. For more information, see the [upstream release notes](https://doc.rust-lang.org/stable/releases.html).
  +  [Corretto 24](https://docs.aws.amazon.com/corretto/latest/corretto-24-ug/) has been added. This is a feature release of Corretto, and for more information on support timelines, see the [Corretto Support Calendar FAQ](https://aws.amazon.com/corretto/faqs/#support_calendar).
  + Each major version of Corretto has received updates.
**Note**
 Corretto 23 is not a Long Term Support release of Corretto, and was introduced into Amazon Linux 2023 during the 2023.6 release. It will be going End of Life in April 2025, see the [Corretto Support Calendar FAQ](https://aws.amazon.com/corretto/faqs/#support_calendar).
  +  `dotnet6.0` has been updated from 6.0.32 to 6.0.36
  +  `dotnet8.0` has been updated from 8.0.7 to 8.0.12
+

**Utilities**
  + `git` has been updated from 2.40.1 to 2.47.1 (Resolves [GitHub issue \#756](https://github.com/amazonlinux/amazon-linux-2023/issues/756))
  + `man-pages` has been updated from 5.10 to 6.04
  + The `nano` text editor has been updated to version 8.3 (Resolves [GitHub issue \#711](https://github.com/amazonlinux/amazon-linux-2023/issues/711)
  + `rsync` has been updated to version 3.4
  + `tcsh` has been updated from 6.24.07 to 6.24.14
  + The `vim` editor has been updated from 9.0.2153 to 9.1.785
  + `wireshark` has been updated from 4.0.15 to 4.4.2
+

**Web, Application Servers, and proxies**
  + BIND has been updated from 9.18.28 to 9.18.33
  + Tomcat 9 and 10 have both received updates
  + `nginx` has been updated from 1.24.0 to 1.26.3
  + Squid has been updated from 6.6 to 6.13 (resolves [GitHub issue \#708](https://github.com/amazonlinux/amazon-linux-2023/issues/708))
  + `mod_auth_melon` has been added
  + `mod_auth_openidc` has been added (resolves [GitHub issue \#690)](https://github.com/amazonlinux/amazon-linux-2023/issues/690))

**Security updates**
+ For information on the CVEs addressed in this release, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.7.20250331.repository"></a>

### New packages in AL2023.7.20250331 since AL2023.6.20250317
<a name="new-AL2023.6.20250317-AL2023.7.20250331"></a>

 Comparing AL2023.6.20250317 version 2023.6.20250317 to AL2023.7.20250331 version [2023.7.20250331](#relnotes-2023.7.20250331).

| Package Type | Number of new packages in AL2023.7.20250331 compared to AL2023.6.20250317 |
| --- | --- |
| Source RPMs | 17 |
| Total Binary RPMs | 267 |
|  noarch binary RPMs | 9 |
|  x86\_64 binary RPMs | 132 |
|  aarch64 binary RPMs | 126 |

New packages in AL2023.7.20250331:

- ** `editorconfig` **
  - **RPM:**  editorconfig  / **Architectures:** aarch64, x86\_64
  - **RPM:**  editorconfig-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  editorconfig-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.12.9-2.amzn2023

- ** `freeradius` **
  - **RPM:**  freeradius  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-krb5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-mysql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-postgresql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-rest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-sqlite  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-unixODBC  / **Architectures:** aarch64, x86\_64
  - **RPM:**  freeradius-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-freeradius  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.2.5-4.amzn2023.0.1

- ** `gcc14` **
  - **RPM:**  amdgcn-common  / **Architectures:** x86\_64
  - **RPM:**  cpp14  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libasan8-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libatomic-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libgfortran-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libhwasan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libitm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libitm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-liblsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libquadmath-devel  / **Architectures:** x86\_64
  - **RPM:**  gcc14-libquadmath-static  / **Architectures:** x86\_64
  - **RPM:**  gcc14-libstdc\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libstdc\+\+-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libtsan2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-libubsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc14-offload-amdgcn  / **Architectures:** x86\_64
  - **RPM:**  gcc14-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  gcc14-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan8  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp-offload-amdgcn  / **Architectures:** x86\_64
  - **RPM:**  libhwasan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan2  / **Architectures:** aarch64, x86\_64
  - **Version:** 14.2.1-7.amzn2023.0.1

- ** `gnome-text-editor` **
  - **RPM:**  gnome-text-editor
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.2-1.amzn2023

- ** `gtksourceview5` **
  - **RPM:**  gtksourceview5  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtksourceview5-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtksourceview5-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 5.14.1-1.amzn2023.0.1

- ** `ibus` **
  - **RPM:**  ibus-gtk4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-panel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-xinit  / **Architectures:** noarch
  - **Version:** 1.5.31-1.amzn2023.0.1

- ** `java-24-amazon-corretto` **
  - **RPM:**  java-24-amazon-corretto  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-24-amazon-corretto-debugsymbols  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-24-amazon-corretto-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-24-amazon-corretto-headless  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-24-amazon-corretto-javadoc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  java-24-amazon-corretto-jmods  / **Architectures:** aarch64, x86\_64
  - **Version:** 24.0.0\+36-2.amzn2023.1

- ** `kernel6.12` **
  - **RPM:**  kernel6.12  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel6.12-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-livepatch-6.12.20-23.97  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf6.12  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf6.12  / **Architectures:** aarch64, x86\_64
  - **Version:** 6.12.20-23.97.amzn2023

- ** `kyotocabinet` **
  - **RPM:**  kyotocabinet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kyotocabinet-apidocs  / **Architectures:** noarch
  - **RPM:**  kyotocabinet-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kyotocabinet-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.2.80-6.amzn2023

- ** `libcap` **
  - **RPM:**  captree
  - **Architectures:** aarch64, x86\_64
  - **Version:** 2.73-1.amzn2023.0.1

- ** `libnbd` **
  - **RPM:**  libnbd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libnbd-bash-completion  / **Architectures:** noarch
  - **RPM:**  libnbd-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdfuse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libnbd  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.22.0-1.amzn2023.0.1

- ** `libspelling` **
  - **RPM:**  libspelling  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libspelling-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.4.5-14.amzn2023

- ** `loupe` **
  - **RPM:**  loupe
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.4-31.amzn2023

- ** `nbd` **
  - **RPM:**  nbd
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.25-1.amzn2023.0.1

- ** `nbdkit` **
  - **RPM:**  nbdkit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-bash-completion  / **Architectures:** noarch
  - **RPM:**  nbdkit-basic-filters  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-basic-plugins  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-curl-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-example-plugins  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-linuxdisk-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-nbd-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-selinux  / **Architectures:** noarch
  - **RPM:**  nbdkit-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-srpm-macros  / **Architectures:** noarch
  - **RPM:**  nbdkit-ssh-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nbdkit-tmpdisk-plugin  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.40.5-1.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl-fips-provider-latest
  - **Architectures:** aarch64, x86\_64
  - **Version:** 3.2.2-1.amzn2023.0.1

- ** `openssl-fips-provider-certified` **
  - **RPM:**  openssl-fips-provider-certified  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-fips-provider-certified-so  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.0.8-1.amzn2023.0.1

- ** `perl-Net-SSLeay` **
  - **RPM:**  perl-Net-SSLeay-tests
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.94-1.amzn2023.0.1

- ** `php8.4` **
  - **RPM:**  php8.4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-modphp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.4-zip  / **Architectures:** aarch64, x86\_64
  - **Version:** 8.4.5-1.amzn2023.0.1

- ** `postgresql17` **
  - **RPM:**  postgresql17  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql17-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql17-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 17.4-1.amzn2023.0.1

- ** `uthash` **
  - **RPM:**  uthash-devel  / **Architectures:** noarch
  - **RPM:**  uthash-doc  / **Architectures:** noarch
  - **RPM:**  uthash-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.3.0-8.amzn2023

### AL2023.7.20250331 upgrades from AL2023.6.20250317
<a name="vercmp-AL2023.6.20250317-AL2023.7.20250331"></a>

 Comparing [2023.6.20250317](relnotes-2023.6.20250317.md) to [2023.7.20250331](#relnotes-2023.7.20250331).

| Package Type | Count |
| --- | --- |
| Source | 56 |
| Total Binary | 978 |
|  noarch binary RPMs | 396 |
|  x86\_64 binary RPMs | 295 |
|  aarch64 binary RPMs | 287 |

The full comparison of RPM package versions is below.

- ** [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html) **
  - **RPM:**  [`amazon-efs-utils`](https://docs.aws.amazon.com/linux/al2023/ug/efs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.1.0-1.amzn2023
  - **AL2023.7.20250331 version:** 2.2.1-1.amzn2023

- ** `annobin` **
  - **RPM:**  annobin-annocheck  / **Architectures:** aarch64, x86\_64
  - **RPM:**  annobin-docs  / **Architectures:** noarch
  - **RPM:**  annobin-libannocheck  / **Architectures:** aarch64, x86\_64
  - **RPM:**  annobin-plugin-clang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  annobin-plugin-gcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  annobin-plugin-llvm  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 10.93-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 12.69-1.amzn2023.0.1

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.15.3-1.amzn2023.0.10
  - **AL2023.7.20250331 version:** 2.15.3-1.amzn2023.0.11

- ** `aws-nitro-enclaves-cli` **
  - **RPM:**  aws-nitro-enclaves-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aws-nitro-enclaves-cli-integration-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.4.0-0.amzn2023
  - **AL2023.7.20250331 version:** 1.4.2-0.amzn2023

- ** [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  [`binutils`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  binutils-gprofng  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.39-6.amzn2023.0.11
  - **AL2023.7.20250331 version:** 2.41-50.amzn2023.0.2

- ** `clang` **
  - **RPM:**  clang  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-analyzer  / **Architectures:** noarch
  - **RPM:**  clang-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-resource-filesystem  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-tools-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clang-tools-extra-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  git-clang-format  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-clang  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 15.0.7-3.amzn2023.0.1
  - **AL2023.7.20250331 version:** 15.0.7-3.amzn2023.0.2

- ** `containerd` **
  - **RPM:**  containerd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  containerd-stress  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.7.25-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.7.27-1.amzn2023.0.1

- ** `dotnet8.0` **
  - **RPM:**  aspnetcore-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  aspnetcore-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-apphost-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-host  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-hostfxr-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-runtime-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-8.0-source-built-artifacts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-sdk-dbg-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-targeting-pack-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  dotnet-templates-8.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  netstandard-targeting-pack-2.1  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 8.0.12-1.amzn2023
  - **AL2023.7.20250331 version:** 8.0.14-1.amzn2023.0.1

- ** `dwarves` **
  - **RPM:**  dwarves  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarves1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdwarves1-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.22-1.amzn2023.0.2
  - **AL2023.7.20250331 version:** 1.29-1.amzn2023.0.2

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.91.0-1.amzn2023
  - **AL2023.7.20250331 version:** 1.91.2-1.amzn2023

- ** `firefox` **
  - **RPM:**  firefox
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 128.7.0-1.amzn2023.0.2
  - **AL2023.7.20250331 version:** 128.8.0-1.amzn2023.0.1

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  gcc-plugin-annobin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libquadmath-devel  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-static  / **Architectures:** x86\_64
  - **RPM:**  libstdc\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcc1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  libitm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libquadmath  / **Architectures:** x86\_64
  - **RPM:**  libstdc\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nvptx-common  / **Architectures:** x86\_64
  - **AL2023.6.20250317 version:** 11.5.0-5.amzn2023.0.1
  - **AL2023.7.20250331 version:** 11.5.0-5.amzn2023.0.3

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
  - **AL2023.6.20250317 version:** 9.56.1-7.amzn2023.0.12
  - **AL2023.7.20250331 version:** 9.56.1-7.amzn2023.0.15

- ** `gnutls` **
  - **RPM:**  gnutls  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-dane  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnutls-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 3.8.0-381.amzn2023.0.7
  - **AL2023.7.20250331 version:** 3.8.3-6.amzn2023.0.1

- ** [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html) **
  - **RPM:**  [`golang`](https://docs.aws.amazon.com/linux/al2023/ug/go.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-bin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-docs  / **Architectures:** noarch
  - **RPM:**  golang-misc  / **Architectures:** noarch
  - **RPM:**  golang-shared  / **Architectures:** aarch64, x86\_64
  - **RPM:**  golang-src  / **Architectures:** noarch
  - **RPM:**  golang-tests  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 1.24.0-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.24.1-1.amzn2023.0.1

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
  - **AL2023.6.20250317 version:** 2.06-61.amzn2023.0.14
  - **AL2023.7.20250331 version:** 2.06-61.amzn2023.0.15

- ** `hunspell-en` **
  - **RPM:**  hunspell-en  / **Architectures:** noarch
  - **RPM:**  hunspell-en-GB  / **Architectures:** noarch
  - **RPM:**  hunspell-en-US  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 0.20140811.1-18.amzn2023.0.3
  - **AL2023.7.20250331 version:** 0.20201207-10.amzn2023.0.1

- ** `ibus` **
  - **RPM:**  ibus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-desktop-testing  / **Architectures:** noarch
  - **RPM:**  ibus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-devel-docs  / **Architectures:** noarch
  - **RPM:**  ibus-gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-setup  / **Architectures:** noarch
  - **RPM:**  ibus-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-wayland  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.5.26-7.amzn2023.0.4
  - **AL2023.7.20250331 version:** 1.5.31-1.amzn2023.0.1

- ** `ibus-anthy` **
  - **RPM:**  ibus-anthy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-anthy-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-anthy-python  / **Architectures:** noarch
  - **RPM:**  ibus-anthy-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.5.14-4.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.5.16-188.amzn2023

- ** `ibus-hangul` **
  - **RPM:**  ibus-hangul  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ibus-hangul-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.5.4-5.amzn2023.0.4
  - **AL2023.7.20250331 version:** 1.5.5-6.amzn2023.0.1

- ** `ibus-libpinyin` **
  - **RPM:**  ibus-libpinyin
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.12.0-3.amzn2023.0.3
  - **AL2023.7.20250331 version:** 1.15.8-1.amzn2023.0.1

- ** `ibus-libzhuyin` **
  - **RPM:**  ibus-libzhuyin
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.10.0-2.amzn2023.0.3
  - **AL2023.7.20250331 version:** 1.10.3-2.amzn2023.0.1

- ** `ibus-m17n` **
  - **RPM:**  ibus-m17n
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.4.5-1.amzn2023.0.4
  - **AL2023.7.20250331 version:** 1.4.35-164.amzn2023

- ** `ibus-table` **
  - **RPM:**  ibus-table  / **Architectures:** noarch
  - **RPM:**  ibus-table-devel  / **Architectures:** noarch
  - **RPM:**  ibus-table-tests  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 1.16.8-1.amzn2023.0.5
  - **AL2023.7.20250331 version:** 1.17.11-216.amzn2023

- ** `ibus-table-chinese` **
  - **RPM:**  ibus-table-chinese  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-array  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-cangjie  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-cantonese  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-cantonyale  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-easy  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-erbi  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-quick  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-scj  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-stroke5  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wu  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wubi-haifeng  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-wubi-jidian  / **Architectures:** noarch
  - **RPM:**  ibus-table-chinese-yong  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 1.8.8-1.amzn2023.0.4
  - **AL2023.7.20250331 version:** 1.8.12-6.amzn2023.0.1

- ** `ibus-table-others` **
  - **RPM:**  ibus-table-code  / **Architectures:** noarch
  - **RPM:**  ibus-table-cyrillic  / **Architectures:** noarch
  - **RPM:**  ibus-table-latin  / **Architectures:** noarch
  - **RPM:**  ibus-table-mathwriter  / **Architectures:** noarch
  - **RPM:**  ibus-table-mongol  / **Architectures:** noarch
  - **RPM:**  ibus-table-others  / **Architectures:** noarch
  - **RPM:**  ibus-table-translit  / **Architectures:** noarch
  - **RPM:**  ibus-table-tv  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 1.3.13-1.amzn2023.0.4
  - **AL2023.7.20250331 version:** 1.3.19-75.amzn2023

- ** `jq` **
  - **RPM:**  jq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  jq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.7.1-48.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.7.1-49.amzn2023.0.2

- ** `kernel` **
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 6.1.130-139.222.amzn2023
  - **AL2023.7.20250331 version:** 6.1.131-143.221.amzn2023

- ** `kpatch` **
  - **RPM:**  kpatch-build  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-dnf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kpatch-runtime  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 0.9.7-13.amzn2023.0.1
  - **AL2023.7.20250331 version:** 0.9.10-1.amzn2023.0.4

- ** `libcap` **
  - **RPM:**  libcap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.48-2.amzn2023.0.4
  - **AL2023.7.20250331 version:** 2.73-1.amzn2023.0.1

- ** `libpinyin` **
  - **RPM:**  libpinyin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-data  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpinyin-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libzhuyin  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.6.0-2.amzn2023.0.3
  - **AL2023.7.20250331 version:** 2.9.91-1.amzn2023.0.1

- ** `libpq` **
  - **RPM:**  libpq  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpq-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 16.8-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 17.4-1.amzn2023.0.1

- ** `libxslt` **
  - **RPM:**  libxslt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxslt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxslt  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.1.42-3.amzn2023
  - **AL2023.7.20250331 version:** 1.1.43-1.amzn2023.0.1

- ** `lustre-client` **
  - **RPM:**  lustre-client
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 2.15.6-13.amzn2023
  - **AL2023.7.20250331 version:** 2.15.6-17.amzn2023

- ** `mutter` **
  - **RPM:**  mutter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mutter-common  / **Architectures:** noarch
  - **RPM:**  mutter-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mutter-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 47.4-586.amzn2023
  - **AL2023.7.20250331 version:** 47.4-587.amzn2023

- ** `nettle` **
  - **RPM:**  nettle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nettle-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 3.8-1.amzn2023.0.2
  - **AL2023.7.20250331 version:** 3.10.1-1.amzn2023.0.1

- ** `nodejs20` **
  - **RPM:**  nodejs20  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-docs  / **Architectures:** noarch
  - **RPM:**  nodejs20-full-i18n  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nodejs20-npm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  v8-11.3-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 20.18.2-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 20.18.3-1.amzn2023.0.1

- ** `openssl` **
  - **RPM:**  openssl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  openssl-snapsafe-libs  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 3.0.8-1.amzn2023.0.19
  - **AL2023.7.20250331 version:** 3.2.2-1.amzn2023.0.1

- ** `perl-Net-SSLeay` **
  - **RPM:**  perl-Net-SSLeay
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.92-2.amzn2023.0.2
  - **AL2023.7.20250331 version:** 1.94-1.amzn2023.0.1

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
  - **AL2023.6.20250317 version:** 8.1.31-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 8.1.32-1.amzn2023.0.1

- ** [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html) **
  - **RPM:**  [`php8.3`](https://docs.aws.amazon.com/linux/al2023/ug/php.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-bcmath  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-cli  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dba  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-dbg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-embedded  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-enchant  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ffi  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-fpm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-gmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-intl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-ldap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mbstring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-modphp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-mysqlnd  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-odbc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-opcache  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pdo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pgsql  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-process  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-pspell  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-snmp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-soap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-sodium  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-tidy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-xml  / **Architectures:** aarch64, x86\_64
  - **RPM:**  php8.3-zip  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 8.3.16-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 8.3.19-1.amzn2023.0.1

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
  - **AL2023.6.20250317 version:** 15.12-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 15.12-1.amzn2023.0.2

- ** `postgresql16` **
  - **RPM:**  postgresql16  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-contrib  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-llvmjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plperl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-plpython3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-pltcl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-private-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-test-rpm-macros  / **Architectures:** noarch
  - **RPM:**  postgresql16-upgrade  / **Architectures:** aarch64, x86\_64
  - **RPM:**  postgresql16-upgrade-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 16.8-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 16.8-1.amzn2023.0.2

- ** [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.11`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.11-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 3.11.11-5.amzn2023.0.1
  - **AL2023.7.20250331 version:** 3.11.11-5.amzn2023.0.2

- ** `python3.11-pip` **
  - **RPM:**  python3.11-pip  / **Architectures:** noarch
  - **RPM:**  python3.11-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 22.3.1-2.amzn2023.0.5
  - **AL2023.7.20250331 version:** 22.3.1-2.amzn2023.0.6

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 3.9.21-1.amzn2023.0.2
  - **AL2023.7.20250331 version:** 3.9.21-1.amzn2023.0.3

- ** `python-pip` **
  - **RPM:**  python3-pip  / **Architectures:** noarch
  - **RPM:**  python3-pip-wheel  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 21.3.1-2.amzn2023.0.10
  - **AL2023.7.20250331 version:** 21.3.1-2.amzn2023.0.11

- ** `ruby3.2` **
  - **RPM:**  ruby3.2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-bundled-gems  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-default-gems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-doc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bigdecimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-bundler  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-io-console  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-irb  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-json  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-minitest  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-power\_assert  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-psych  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rake  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rbs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ruby3.2-rubygem-rdoc  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rexml  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-rss  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygems-devel  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-test-unit  / **Architectures:** noarch
  - **RPM:**  ruby3.2-rubygem-typeprof  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 3.2.2-180.amzn2023.0.5
  - **AL2023.7.20250331 version:** 3.2.7-183.amzn2023.0.1

- ** `runfinch-finch` **
  - **RPM:**  runfinch-finch
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.6.0-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.7.1-1.amzn2023.0.1

- ** [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html) **
  - **RPM:**  cargo  / **Architectures:** aarch64, x86\_64
  - **RPM:**  clippy  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`rust`](https://docs.aws.amazon.com/linux/al2023/ug/rust.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-analyzer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-debugger-common  / **Architectures:** noarch
  - **RPM:**  rust-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rustfmt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-gdb  / **Architectures:** noarch
  - **RPM:**  rust-lldb  / **Architectures:** noarch
  - **RPM:**  rust-src  / **Architectures:** noarch
  - **RPM:**  rust-std-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rust-std-static-wasm32-unknown-unknown  / **Architectures:** noarch
  - **RPM:**  rust-std-static-wasm32-wasip1  / **Architectures:** noarch
  - **RPM:**  rust-toolset  / **Architectures:** noarch
  - **RPM:**  rust-toolset-srpm-macros  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 1.84.0-4.amzn2023.0.1
  - **AL2023.7.20250331 version:** 1.85.0-1.amzn2023.0.1

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 2023.6.20250317-0.amzn2023
  - **AL2023.7.20250331 version:** 2023.7.20250331-0.amzn2023

- ** `tomcat10` **
  - **RPM:**  tomcat10  / **Architectures:** noarch
  - **RPM:**  tomcat10-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat10-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat10-el-5.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-jsp-3.1-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-lib  / **Architectures:** noarch
  - **RPM:**  tomcat10-servlet-6.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat10-webapps  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 10.1.34-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 10.1.39-1.amzn2023.0.1

- ** `tomcat9` **
  - **RPM:**  tomcat9  / **Architectures:** noarch
  - **RPM:**  tomcat9-admin-webapps  / **Architectures:** noarch
  - **RPM:**  tomcat9-docs-webapp  / **Architectures:** noarch
  - **RPM:**  tomcat9-el-3.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-jsp-2.3-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-lib  / **Architectures:** noarch
  - **RPM:**  tomcat9-servlet-4.0-api  / **Architectures:** noarch
  - **RPM:**  tomcat9-webapps  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 9.0.98-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 9.0.102-1.amzn2023.0.1

- ** `tzdata` **
  - **RPM:**  tzdata  / **Architectures:** noarch
  - **RPM:**  tzdata-java  / **Architectures:** noarch
  - **AL2023.6.20250317 version:** 2025a-1.amzn2023.0.1
  - **AL2023.7.20250331 version:** 2025b-1.amzn2023.0.1

- ** `xcalc` **
  - **RPM:**  xcalc
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 1.1.2-42.amzn2023
  - **AL2023.7.20250331 version:** 1.1.2-43.amzn2023

- ** `xorg-x11-server` **
  - **RPM:**  xorg-x11-server-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-source  / **Architectures:** noarch
  - **RPM:**  xorg-x11-server-Xephyr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xnest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xorg  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xvfb  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250317 version:** 21.1.13-5.amzn2023.0.3
  - **AL2023.7.20250331 version:** 21.1.13-5.amzn2023.0.4

## Image Updates
<a name="ami-updates-2023.7.20250331"></a>

### Default AMI
<a name="amis-2023.7.20250331.default-ami"></a>

This section provides details about default ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250331-0.amzn2023  |
|  binutils-2.41-50.amzn2023.0.2  |
|  gnutls-3.8.3-6.amzn2023.0.1  |
|  grub2-common-1:2.06-61.amzn2023.0.15  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.15  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.15  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.15  |
|  grub2-tools-1:2.06-61.amzn2023.0.15  |
|  hunspell-en-GB-0.20201207-10.amzn2023.0.1  |
|  hunspell-en-US-0.20201207-10.amzn2023.0.1  |
|  hunspell-en-0.20201207-10.amzn2023.0.1  |
|  jq-1.7.1-49.amzn2023.0.2  |
|  kernel-libbpf-6.12.20-23.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250331-0.amzn2023  |
|  kernel-tools-6.12.20-23.97.amzn2023  |
|  kernel-6.1.131-143.221.amzn2023  |
|  kpatch-runtime-0.9.10-1.amzn2023.0.4  |
|  libcap-2.73-1.amzn2023.0.1  |
|  libgcc-14.2.1-7.amzn2023.0.1  |
|  libgomp-14.2.1-7.amzn2023.0.1  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.1  |
|  nettle-3.10.1-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.1  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.1  |
|  openssl-1:3.2.2-1.amzn2023.0.1  |
|  python3-libs-3.9.21-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.11  |
|  python3-3.9.21-1.amzn2023.0.3  |
|  rust-toolset-srpm-macros-1.85.0-1.amzn2023.0.1  |
|  system-release-2023.7.20250331-0.amzn2023  |
|  tzdata-2025b-1.amzn2023.0.1  |

### Default Container
<a name="amis-2023.7.20250331.default-container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250331-0.amzn2023  |
|  cracklib-2.9.6-27.amzn2023.0.2  |
|  gzip-1.12-1.amzn2023.0.1  |
|  libcap-2.73-1.amzn2023.0.1  |
|  libdb-5.3.28-49.amzn2023.0.2  |
|  libeconf-0.4.0-1.amzn2023.0.3  |
|  libgcc-14.2.1-7.amzn2023.0.1  |
|  libgomp-14.2.1-7.amzn2023.0.1  |
|  libpwquality-1.4.4-6.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.1  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.1  |
|  pam-1.5.1-8.amzn2023.0.4  |
|  python3-libs-3.9.21-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.11  |
|  python3-3.9.21-1.amzn2023.0.3  |
|  system-release-2023.7.20250331-0.amzn2023  |
|  tzdata-2025b-1.amzn2023.0.1  |

### Minimal AMI
<a name="amis-2023.7.20250331.minimal-ami"></a>

This section provides details about minimal ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.7.20250331-0.amzn2023  |
|  gnutls-3.8.3-6.amzn2023.0.1  |
|  grub2-common-1:2.06-61.amzn2023.0.15  |
|  grub2-efi-x64-ec2-1:2.06-61.amzn2023.0.15  |
|  grub2-pc-modules-1:2.06-61.amzn2023.0.15  |
|  grub2-tools-minimal-1:2.06-61.amzn2023.0.15  |
|  grub2-tools-1:2.06-61.amzn2023.0.15  |
|  jq-1.7.1-49.amzn2023.0.2  |
|  kernel-libbpf-6.12.20-23.97.amzn2023  |
|  kernel-livepatch-repo-s3-2023.7.20250331-0.amzn2023  |
|  kernel-6.1.131-143.221.amzn2023  |
|  libcap-2.73-1.amzn2023.0.1  |
|  libgcc-14.2.1-7.amzn2023.0.1  |
|  libgomp-14.2.1-7.amzn2023.0.1  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.1  |
|  nettle-3.10.1-1.amzn2023.0.1  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.1  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.1  |
|  openssl-1:3.2.2-1.amzn2023.0.1  |
|  python3-libs-3.9.21-1.amzn2023.0.3  |
|  python3-pip-wheel-21.3.1-2.amzn2023.0.11  |
|  python3-3.9.21-1.amzn2023.0.3  |
|  system-release-2023.7.20250331-0.amzn2023  |
|  tzdata-2025b-1.amzn2023.0.1  |

### Minimal Container
<a name="amis-2023.7.20250331.minimal-container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.7.20250331-0.amzn2023  |
|  cracklib-2.9.6-27.amzn2023.0.2  |
|  gzip-1.12-1.amzn2023.0.1  |
|  libcap-2.73-1.amzn2023.0.1  |
|  libdb-5.3.28-49.amzn2023.0.2  |
|  libeconf-0.4.0-1.amzn2023.0.3  |
|  libgcc-14.2.1-7.amzn2023.0.1  |
|  libpwquality-1.4.4-6.amzn2023.0.2  |
|  libstdc\+\+-14.2.1-7.amzn2023.0.1  |
|  libxcrypt-4.4.33-7.amzn2023  |
|  openssl-fips-provider-latest-1:3.2.2-1.amzn2023.0.1  |
|  openssl-libs-1:3.2.2-1.amzn2023.0.1  |
|  pam-1.5.1-8.amzn2023.0.4  |
|  system-release-2023.7.20250331-0.amzn2023  |
|  tzdata-2025b-1.amzn2023.0.1  |

## Contact us
<a name="amis-2023.7.20250331.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
