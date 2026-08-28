---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html
---

# Deprecated in AL2023
<a name="deprecated-al2023"></a>

 This section describes functionality that exists in AL2023 and is likely to be removed in a future version of Amazon Linux. Each section will describe what the functionality is and when it is expected to removed from Amazon Linux.

**Note**
 This section will be updated over time as the Linux ecosystem evolves and future major versions of Amazon Linux are closer to release.

**Topics**
+ [32bit x86 (i686) runtime support](#deprecated-32bit)
+ [`aspell`](#deprecated-aspell)
+ [Berkeley DB (`libdb`)](#deprecated-bdb)
+ [`cron`](#deprecated-cron)
+ [IMDSv1](#deprecated-imdsv1)
+ [`pcre` version 1](#deprecated-pcre)
+ [System V init (`sysvinit`)](#deprecated-sysv-init)
+ [EOL Packages are deprecated](#deprecated-eol-packages)

## 32bit x86 (i686) runtime support
<a name="deprecated-32bit"></a>

 AL2023 retains the ability to run 32bit x86 (i686) binaries. It is likely that the next major version of Amazon Linux will no longer support running 32bit user space binaries.

## `aspell`
<a name="deprecated-aspell"></a>

 While AL2023 ships with the `aspell` package, it is deprecated and will be removed in the next major release of Amazon Linux. Customers are advised to migrate to modern replacements such as `hunspell` or `enchant2`.

 The deprecation of `aspell` in AL2023 follows the broader community shift, for example [`aspell` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/AspellDeprecation).

## Berkeley DB (`libdb`)
<a name="deprecated-bdb"></a>

 AL2023 ships with version 5.3.28 of the Berkeley DB (`libdb`) library. This is the last version of Berkeley DB before the license changed to the GNU Affero GPLv3 (AGPL) license, from the less restrictive Sleepycat license.

 There are few packages in AL2023 that remain reliant on Berkeley DB (`libdb`), and the library will be removed in the next major release of Amazon Linux.

**Note**
 The `dnf` package manager in AL2023 retains read-only support for a Berkeley DB (BDB) format `rpm` database. This support will be removed in the next major release of Amazon Linux.

 The deprecation of `libdb` follows the broader community shift away from it, for example the [`libdb` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/Libdb_deprecated).

## `cron`
<a name="deprecated-cron"></a>

 The `cronie` package was installed by default on the AL2 AMI, providing support for the traditional `crontab` way of scheduling periodic tasks. In AL2023, `cronie` is not included by default. Therefore, support for `crontab` is no longer provided by default.

 In AL2023, you can optionally install the `cronie` package to use classic `cron` jobs. We recommend that you migrate to `systemd` timers due to the added functionality provided by `systemd`.

 It is possible that a future version of Amazon Linux, possibly the next major version, will no longer include support for classic `cron` jobs and complete the transition to `systemd` timers. We recommend that you migrate away from using `cron`.

## IMDSv1
<a name="deprecated-imdsv1"></a>

 By default, AL2023 AMIs are configured to launch in IMDSv2-only mode, disabling the use of IMDSv1. There is still the option to use AL2023 with IMDSv1 enabled. A future version of Amazon Linux is likely to enforce IMDSv2-only.

 For more information on IMDS configuration for AMIs, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.

## `pcre` version 1
<a name="deprecated-pcre"></a>

 The legacy `pcre` package is deprecated and will be removed in the next major release of Amazon Linux. The `pcre2` package is the successor. Although the first versions of AL2023 shipped with a limited number of packages building against `pcre`, these packages will be migrated to `pcre2` within AL2023. The deprecated `pcre` library will remain available in AL2023.

**Note**
 The deprecated version of `pcre` will not receive security updates for the full lifetime of AL2023. For more information about the `pcre` support lifecycle and the amount of time that the package will receive security updates, see the [package support statements on the `pcre` package](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

 The deprecation of `pcre` in favor of `pcre2` follows the broader community shift in this direction, for example [`pcre` deprecation in Fedora](https://fedoraproject.org/wiki/Changes/PcreDeprecation).

## System V init (`sysvinit`)
<a name="deprecated-sysv-init"></a>

 Although AL2023 retains backwards compatibility with System V service (init) scripts, the upstream `systemd` project, as part of its [v254 release](https://github.com/systemd/systemd/releases/tag/v254), announced the [deprecation of support for System V service scripts](https://github.com/systemd/systemd/blob/08423f6d30f5db045b8a25307857f111f45ff292/NEWS), and indicated that support will be removed in a future version of `systemd`. For more information, see [systemd](https://systemd.io/).

 AL2023 will retain backwards compatibility with System V service (init) scripts, but users are encouraged to migrate to using native `systemd` unit files in order to be prepared for when support for System V service (init) scripts is removed from Amazon Linux, likely in the next major release.

## EOL Packages are deprecated
<a name="deprecated-eol-packages"></a>

 Each package available in AL2023 has an associated [support statement](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html) which covers Amazon Linux specific information. These statements cover the core of the OS and its lifetime, as well as packages such as [PHP in AL2023](php.md) and [Python in AL2023](python.md), where AL2023 ships multiple versions and each are supported for the duration that the upstream Open Source project does.

 In AL2023 you can get package support information using the `dnf` package manager. For more information, see [Getting package support information](managing-repos-os-updates.md#dnf-support-info-plugin).

 Where a package is no longer supported before the end of the major version of Amazon Linux, it should be assumed that this package is deprecated and will not be present in the next major version of Amazon Linux.

 For packages such as [PHP in AL2023](php.md) and [Python in AL2023](python.md), where each major Amazon Linux version has shipped multiple versions, each with a different support lifecycle, it is likely that they will continue to be present in new major versions of Amazon Linux, albeit with little or no overlap of major versions of the packages. It is recommended to keep the Amazon Linux package support timelines in mind when selecting dependencies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
