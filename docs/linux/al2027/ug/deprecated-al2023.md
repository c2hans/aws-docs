---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/deprecated-al2023.html
---

# Deprecated in AL2023
<a name="deprecated-al2023"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 This section describes functionality that was deprecated in AL2023. Most deprecated functionality is removed in AL2027 as of the Preview release. Some functionality will be present in AL2027 Preview but will be removed prior to GA. For information on the current AL2027 Preview release, see the [AL2027 User Guide](https://docs.aws.amazon.com/linux/al2027/ug/) and [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/).

**Note**
 This section will be updated over time as the Linux ecosystem evolves and future major versions of Amazon Linux are closer to release.
 This section will be updated during the AL2027 Preview.

**Topics**
+ [DNF version 4 and its Python API](#deprecated-dnf4)
+ [32bit x86 (i686) runtime support](#deprecated-32bit)
+ [`aspell`](#deprecated-aspell)
+ [Berkeley DB (`libdb`)](#deprecated-bdb)
+ [`cron`](#deprecated-cron)
+ [IMDSv1](#deprecated-imdsv1)
+ [`pcre` version 1](#deprecated-pcre)
+ [System V init (`sysvinit`)](#deprecated-sysv-init)
+ [Control groups version 1 (cgroup v1)](#deprecated-cgroupv1)
+ [`ksh`](#deprecated-ksh)
+ [`opensmtpd`](#deprecated-opensmtpd)
+ [`ftp` client](#deprecated-ftp)
+ [EOL Packages are deprecated](#deprecated-eol-al2023-packages)

## DNF version 4 and its Python API
<a name="deprecated-dnf4"></a>

 AL2027 replaces DNF (version 4) with DNF5. The `dnf` and `yum` commands run DNF5, and compatibility aliases keep common DNF (version 4) command spellings working. The DNF (version 4) Python API (`python3-dnf`) is not available; port Python scripts to the `python3-libdnf5` bindings. For more information, see [Package management tool](package-management.md).

## 32bit x86 (i686) runtime support
<a name="deprecated-32bit"></a>

 AL2023 retains the ability to run 32bit x86 (i686) binaries on x86\_64, but does not ship any userspace packages to support doing so. AL2027 will have support for running 32bit x86 (i686) binaries disabled.

## `aspell`
<a name="deprecated-aspell"></a>

 While AL2023 ships with the `aspell` package, it is deprecated and is removed in AL2027. While still present in the initial AL2027 Preview release, it will be removed before general availability. We recommend that you migrate to modern replacements such as `hunspell` or `enchant2`.

 The deprecation of `aspell` in AL2023 follows the broader community shift, for example [`aspell` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/AspellDeprecation).

## Berkeley DB (`libdb`)
<a name="deprecated-bdb"></a>

 AL2023 ships with version 5.3.28 of the Berkeley DB (`libdb`) library. This is the last version of Berkeley DB before the license changed to the GNU Affero GPLv3 (AGPL) license, from the less restrictive Sleepycat license.

 There are few packages in AL2023 that remain reliant on Berkeley DB (`libdb`). The library is deprecated in AL2023 and is removed in AL2027.

**Note**
 The `dnf` package manager in AL2023 retains read-only support for a Berkeley DB (BDB) format `rpm` database. This support is removed in AL2027, which uses the SQLite `rpm` database format.

 The deprecation of `libdb` follows the broader community shift away from it, for example the [`libdb` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/Libdb_deprecated).

## `cron`
<a name="deprecated-cron"></a>

 The `cronie` package was installed by default on the AL2 AMI, providing support for the traditional `crontab` way of scheduling periodic tasks. In AL2023, `cronie` is not included by default. Therefore, support for `crontab` is no longer provided by default.

 You can optionally install the `cronie` package to use classic `cron` jobs. We recommend that you migrate to `systemd` timers due to the added functionality provided by `systemd`.

 It is possible that a future version of Amazon Linux will no longer include support for classic `cron` jobs and complete the transition to `systemd` timers. We recommend that you migrate away from using `cron`.

## IMDSv1
<a name="deprecated-imdsv1"></a>

 By default, AL2023 AMIs are configured to launch in IMDSv2-only mode, disabling the use of IMDSv1. There is still the option to use AL2023 with IMDSv1 enabled. A future version of Amazon Linux is likely to enforce IMDSv2-only.

 For more information on IMDS configuration for AMIs, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.

## `pcre` version 1
<a name="deprecated-pcre"></a>

 The legacy `pcre` package is deprecated and is removed in AL2027. The `pcre2` package is the successor. Although the first versions of AL2023 shipped with a limited number of packages building against `pcre`, these packages will be migrated to `pcre2` within AL2023. The deprecated `pcre` library will remain available in AL2023.

**Note**
 The deprecated version of `pcre` will not receive security updates for the full lifetime of AL2023. For more information about the `pcre` support lifecycle and the amount of time that the package will receive security updates, see the [package support statements on the `pcre` package](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

 The deprecation of `pcre` in favor of `pcre2` follows the broader community shift in this direction, for example [`pcre` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/PcreDeprecation).

## System V init (`sysvinit`)
<a name="deprecated-sysv-init"></a>

 Although AL2023 retains backwards compatibility with System V service (init) scripts, the upstream `systemd` project, as part of its [v254 release](https://github.com/systemd/systemd/releases/tag/v254), announced the [deprecation of support for System V service scripts](https://github.com/systemd/systemd/blob/08423f6d30f5db045b8a25307857f111f45ff292/NEWS), and indicated that support will be removed in a future version of `systemd`. For more information, see [systemd](https://systemd.io/).

 AL2023 retains backwards compatibility with System V service (init) scripts, but the support is deprecated. AL2027, which ships a newer `systemd`, removes support for System V service (init) scripts, so migrate to native `systemd` unit files.

## Control groups version 1 (cgroup v1)
<a name="deprecated-cgroupv1"></a>

 cgroup v1 was deprecated in AL2 and AL2023 ran cgroup v2 by default. The `systemd` project removed cgroup v1 support in v258, and AL2027 ships a `systemd` newer than v258, so AL2027 supports cgroup v2 only. Move any remaining tooling that mounts or reads the legacy cgroup v1 hierarchy to the cgroup v2 interfaces. For more information, see [Limiting process resource usage in Amazon Linux using cgroups](resource-limiting-raw-cgroups.md).

## `ksh`
<a name="deprecated-ksh"></a>

 The `ksh` shell is deprecated in AL2023 and is removed in AL2027. Port shell scripts to `bash`, which is included by default.

## `opensmtpd`
<a name="deprecated-opensmtpd"></a>

 The `opensmtpd` mail server is deprecated in AL2023 and is removed in AL2027. Use `postfix` or `sendmail`, both available in the repositories.

## `ftp` client
<a name="deprecated-ftp"></a>

 The legacy `ftp` package from AL2 was removed in AL2023 and remains unavailable in AL2027. The package was not actively maintained upstream, and the FTP protocol transmits data, including credentials, in plaintext. For file transfers, `lftp` supports FTP, FTPS, HTTP, HTTPS, and SFTP. For downloads, `curl` is installed by default. Where you control both endpoints, we recommend `sftp` from the `openssh-clients` package, because transfers and credentials are encrypted.

## EOL Packages are deprecated
<a name="deprecated-eol-al2023-packages"></a>

 Each package available in AL2023 has an associated [support statement](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html) which covers Amazon Linux specific information. These statements cover the core of the OS and its lifetime, as well as packages such as `php` and `python`, where AL2023 ships multiple versions and each are supported for the duration that the upstream Open Source project does.

 In AL2023 you can get package support information using the `dnf` package manager. For more information, see [Getting package support information](manage-updates.md#dnf-support-info-plugin).

 Where a package is no longer supported before the end of the major version of Amazon Linux, it should be assumed that this package is deprecated and will not be present in the next major version of Amazon Linux.

 For packages such as `php` and `python`, where each major Amazon Linux version has shipped multiple versions, each with a different support lifecycle, it is likely that they will continue to be present in new major versions of Amazon Linux, albeit with little or no overlap of major versions of the packages. It is recommended to keep the Amazon Linux package support timelines in mind when selecting dependencies.
