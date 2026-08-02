---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/epel.html
---

# Extra Packages for Enterprise Linux (EPEL)
<a name="epel"></a>

**Warning**
 The AL2 `epel` Extra enabled the third party EPEL7 repository. As of 2024-06-30 the third-party EPEL7 repository is *no longer being maintained*.
 This third-party repository will have *no future updates*. This means there will be *no security fixes* for packages in the *EPEL* repository.
 This section will cover options in AL2023 for packages found in EPEL.

 Extra Packages for Enterprise Linux (EPEL) is a project in the Fedora community with the objective of creating a large array of packages for enterprise-level Linux operating systems. The project has primarily produced RHEL and CentOS packages. AL2 features a high level of compatibility with CentOS 7. As a result, many EPEL7 packages work on AL2.

 There are no EPEL versions that are binary compatible with AL2023. However, customers that want to use their EPEL7 packages in AL2023 have a few options. Some EPEL packages have alternatives in AL2023, while others are provided as part of [Supplementary Packages for Amazon Linux](spal.md).

**Warning**
 Only add repositories designed to be used with AL2023.
 While repositories designed for other distributions may work today, there is no guarantee they will continue to do so with any package update in AL2023 or the repository not designed for use with AL2023.

 This page provides information about the EPEL7 packages used by customers on AL2 and their AL2023 counterparts.

 For the rest of the packages, customers might be able to use Supplementary Packages for Amazon Linux (SPAL). SPAL provides thousands of EPEL9 packages, built specifically for Amazon Linux 2023, but these packages are not covered by AWS Support Plans. This means CVEs are not being tracked for SPAL packages, and patches are only provided when available upstream.

**Important**
 Consult documentation of [Supplementary Packages for Amazon Linux](spal.md) before using it.

**Topics**
+ [`axel` - HTTP/FTP client](#axel)
+ [`brotli` and `libbrotli` - compression](#brotli)
+ [`collectd` - Statistics collection daemon](#collectd)
+ [`cpulimit` - CPU Usage limiter](#cpulimit)
+ [`exim` - mail transfer agent](#exim)
+ [`fuse3` - File System in Userspace (FUSE) v3](#fuse3)
+ [`ganglia` - Distributed Monitoring System](#ganglia)
+ [`git-lfs` - version control large files with Git](#git-lfs)
+ [`haveged` - an entropy source using the HAVEGE algorithm](#haveged)
+ [`inotify-tools` - inotify command line tools](#inotify-tools)
+ [`iperf` - TCP/UDP Performance benchmark](#iperf)
+ [`jemalloc` - alternative `malloc` implementation](#jemalloc)
+ [`libbsd` - BSD-compatible function library](#libbsd)
+ [`libserf` - HTTP Client Library](#libserf)
+ [`libzstd` - zstd compression library](#libzstd)
+ [`lighttpd` web server](#lighttpd)
+ [`lshell` - a restricted shell](#lshell)
+ [`monit` - process, file, directory, and devices monitor](#monit)
+ [`nodejs`](#nodejs)
+ [`perl-Config-General`](#perl-Config-General)
+ [`python2-lockfile` - file locking](#python2-lockfile)
+ [`python2-rsa` - pure Python RSA](#python2-rsa)
+ [`python2-simplejson` - JSON routines for Python 2](#python2-simplejson)
+ [`rkhunter` - Rootkit Hunter](#rkhunter)
+ [`rssh` - a restricted shell for use with OpenSSH](#rssh)
+ [`sscg` - self-signed SSL certificate generator](#sscg)
+ [`stress` - Stress test](#stress)
+ [`stress-ng` - Stress test](#stress-ng)
+ [`tmpwatch` - removes files based on last accessed time](#tmpwatch)
+ [`xmlstarlet` - command line XML utilities](#xmlstarlet)

## `axel` - HTTP/FTP client
<a name="axel"></a>

 The `axel` package was in EPEL7, and has not ever shipped as part of Amazon Linux. Alternatives available in AL2023 are `curl` and `wget`.

**Warning**
 The `-S` option to `axel` uses an *unencrypted* http connection to discover mirrors for a file.

 It is highly recommended to migrate any use of `axel` over to either `curl` or `wget`.

## `brotli` and `libbrotli` - compression
<a name="brotli"></a>

 The `brotli` and `libbrotli` packages were in EPEL7, while just the `brotli` package was available in AL2 core.

 Both the `brotli` and `libbrotli` packages are included in AL2023.

 The `brotli` package can be installed on AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{brotli}}
```

 The `libbrotli` package can be installed on AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{libbrotli}}
```

## `collectd` - Statistics collection daemon
<a name="collectd"></a>

 The `collect` package was in EPEL7, and was also available in the `collectd` and `collectd-python3` AL2 Extras.

 The `collectd` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{collectd}}
```

## `cpulimit` - CPU Usage limiter
<a name="cpulimit"></a>

 In Amazon Linux 2023, `systemd` provides functionality to limit the CPU usage of processes, or groups of processes. This functionality is also easy to use for any `systemd` service.

 There are powerful resource control facilities provided by `systemd` which can be used to ensure any task or group of tasks is limited in what resources it can consume. For more information, see the upstream [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html) documentation, along with the [Limiting process resource usage in AL2023 using systemd](resource-limiting-systemd.md).

## `exim` - mail transfer agent
<a name="exim"></a>

 The `exim` package was in EPEL7, and previously available in AL1. Amazon Linux 2023 provides both the `postfix` and `sendmail` Mail Transfer Agents (MTAs).

## `fuse3` - File System in Userspace (FUSE) v3
<a name="fuse3"></a>

 The `fuse3` package (including `fuse3-libs` and `fuse3-devel`) were in EPEL7. These packages are part of AL2023, and each can be installed by running the relevant following command:

```
[ec2-user ~]$ sudo dnf install {{fuse3}}
```

```
[ec2-user ~]$ sudo dnf install {{fuse3-libs}}
```

```
[ec2-user ~]$ sudo dnf install {{fuse3-devel}}
```

## `ganglia` - Distributed Monitoring System
<a name="ganglia"></a>

 The `ganglia` package was in EPEL7, and previously available in AL1. It was not shipped with AL2.

 The upstream project had a period of inactivity where some open CVEs were not being addressed. While there has been recent activity in the upstream project, it is not planned to add `ganglia` to AL2023.

## `git-lfs` - version control large files with Git
<a name="git-lfs"></a>

 The `git-lfs` package was in EPEL7. In Amazon Linux 2023, the `git-lfs` package is included in the core repository. On AL2023, `git-lfs` can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{git-lfs}}
```

## `haveged` - an entropy source using the HAVEGE algorithm
<a name="haveged"></a>

 The `haveged` package was in EPEL7. Amazon Linux 2023 comes pre-configured with entropy sources, not requiring the use of `haveged`.

## `inotify-tools` - inotify command line tools
<a name="inotify-tools"></a>

 The `inotify-tools` package was in EPEL7, and is included in AL2023.

**Note**
 In AL2023, `systemd` supports path based activation which can be used for taking action on events such as when a path exists or changes.
 Much of what `inotify-tools` is used for can now be better accomplished in a more reliable manner using `systemd` path activation. For more information, see [systemd.path](https://www.freedesktop.org/software/systemd/man/latest/systemd.path.html).

 The `inotify-tools` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{inotify-tools}}
```

## `iperf` - TCP/UDP Performance benchmark
<a name="iperf"></a>

 The `iperf` version 2 package was in EPEL7, and was also available in the `testing` AL2 Extra. and was also available in AL1

**Note**
 The `iperf3` package is also available, providing version 3 of `iperf`.

 The `iperf` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{iperf}}
```

## `jemalloc` - alternative `malloc` implementation
<a name="jemalloc"></a>

 The `jemalloc` package was in EPEL7, and was available in the `lamp-mariadb10.2-php7.2` and `mariadb10.5` AL2 Extras.

 The `jemalloc` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{jemalloc}}
```

## `libbsd` - BSD-compatible function library
<a name="libbsd"></a>

 The `libbsd` package was in EPEL7, and was also available in the `testing` AL2 Extra.

 The `libbsd` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{libbsd}}
```

 The development files for `libbsd` can be installed by running the following command.

```
[ec2-user ~]$ sudo dnf install {{libbsd-devel}}
```

## `libserf` - HTTP Client Library
<a name="libserf"></a>

 The `libserf` package was in EPEL7. The `libserf` package is provided in Amazon Linux 2023. It can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{libserf}}
```

## `libzstd` - zstd compression library
<a name="libzstd"></a>

 The `libzstd` package was in AL2 core, as well as in EPEL7. The `libzstd` package is also part of AL2023.

```
[ec2-user ~]$ sudo dnf install {{libzstd}}
```

## `lighttpd` web server
<a name="lighttpd"></a>

 The `lighttpd` package was in EPEL7, and previously available in AL1. Amazon Linux 2023 provides both the Apache `httpd` and `nginx` web servers.

## `lshell` - a restricted shell
<a name="lshell"></a>

 The `lshell` package has never been shipped as part of Amazon Linux. It was available in EPEL6. The [Fedora packaging repository for `lshell`](https://src.fedoraproject.org/rpms/lshell) covers [why it was not packaged](https://src.fedoraproject.org/rpms/lshell/c/cb122f0a16c9f1d5c2af8582b740a3f62587a951?branch=rawhide) in EPEL7 or Fedora 30. It was also [removed from Debian](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=862302).

 The upstream `lshell` project is [no longer being actively maintained](https://github.com/ghantoos/lshell/issues/209), and contains [known unpatched](https://github.com/ghantoos/lshell/issues/188) *Critical CVEs*: [CVE-2016-6902](https://nvd.nist.gov/vuln/detail/CVE-2016-6902) and [CVE-2016-6903](https://nvd.nist.gov/vuln/detail/CVE-2016-6903).

 The alternative suggested in the Debian bug, [http://www.pizzashack.org/rssh/](http://www.pizzashack.org/rssh/) is also unmaintained upstream, with the author citing unfixable security issues as the reason.

 For these reasons, adding `lshell` to AL2023 is not planned.

## `monit` - process, file, directory, and devices monitor
<a name="monit"></a>

 In Amazon Linux 2023, `systemd` provides a wide array of functionality for monitoring, starting, stopping, and restarting services. This includes rate limiting restarts, waiting between restart attempts, and starting another service on failure. For more information, see the [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) documentation.

 In AL2023, `systemd` also supports path based activation which can be used for taking action on events such as when a path exists or changes. For more information, see [systemd.path](https://www.freedesktop.org/software/systemd/man/latest/systemd.path.html).

 There are common configuration options for `systemd` units which allow specifying dependencies, conditionals, and actions to take on success or failure. For more information, see the [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html) documentation.

 There are powerful resource control facilities provided by `systemd` which can be used to ensure any monitoring task does not use excessive CPU or memory. For more information, see [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html).

## `nodejs`
<a name="nodejs"></a>

 The `nodejs` version 16 package was in EPEL7, and `nodejs` is now included in AL2023. At the time of writing, both `nodejs` version 18 and 20 were available in AL2023. You can install `nodejs` 18 on AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{nodejs}}
```

 You can install `nodejs` 20 on AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{nodejs20}}
```

## `perl-Config-General`
<a name="perl-Config-General"></a>

 The `perl-Config-General` package was in EPEL7, and is now included in AL2023. You can install the `perl-Config-General` package in AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{perl-Config-General}}
```

 Perl modules can also be installed by asking DNF to install the package that provides a particular Perl module. With this method, you can use the more familiar Perl module name rather than the OS package name.

```
[ec2-user ~]$ sudo dnf install 'perl({{Confg::General}})'
```

## `python2-lockfile` - file locking
<a name="python2-lockfile"></a>

 The `python2-lockfile` package was in EPEL7, and AL2 included a `python-lockfile` package. In AL2023 [Python 2.7 has been replaced with Python 3](python2.7-no-more.md), so a *Python 2* variant of this package will not be added to AL2023.

 The *Python 3* version of this package *is included in AL2023*. You can install the `python3-lockfile` package in AL2023 with one of the following commands:

```
[ec2-user ~]$ sudo dnf install {{python3-lockfile}}
```

 Python modules can also be installed by asking DNF to install the package that provides a particular Python module.

```
[ec2-user ~]$ sudo dnf install 'python3dist({{lockfile}})'
```

## `python2-rsa` - pure Python RSA
<a name="python2-rsa"></a>

 The `python2-rsa` package was in EPEL7, and AL2 included a `python2-rsa` package. In AL2023 [Python 2.7 has been replaced with Python 3](python2.7-no-more.md), so a *Python 2* variant of this package will not be added to AL2023.

 The *Python 3* version of this package *is included in AL2023*. You can install the `python3-rsa` package in AL2023 with one of the following commands:

```
[ec2-user ~]$ sudo dnf install {{python3-rsa}}
```

 Python modules can also be installed by asking DNF to install the package that provides a particular Python module.

```
[ec2-user ~]$ sudo dnf install 'python3dist({{rsa}})'
```

## `python2-simplejson` - JSON routines for Python 2
<a name="python2-simplejson"></a>

 The `python2-simplejson` package was in EPEL7. In AL2023 [Python 2.7 has been replaced with Python 3](python2.7-no-more.md), so a *Python 2* variant of this package will not be added to AL2023.

 The *Python 3* version of this package *is included in AL2023*. You can install the `python3-simplejson` package in AL2023 with the following command:

```
[ec2-user ~]$ sudo dnf install {{python3-simplejson}}
```

 Python modules can also be installed by asking DNF to install the package that provides a particular Python module.

```
[ec2-user ~]$ sudo dnf install 'python3dist({{simplejson}})'
```

## `rkhunter` - Rootkit Hunter
<a name="rkhunter"></a>

 The `rkhunter` package is included in AL2023 along with `chkrootkit`.

```
[ec2-user ~]$ sudo dnf install {{rkhunter}}
```

```
[ec2-user ~]$ sudo dnf install {{chkrootkit}}
```

## `rssh` - a restricted shell for use with OpenSSH
<a name="rssh"></a>

 The `rssh` package was in EPEL7. The upstream [http://www.pizzashack.org/rssh/](http://www.pizzashack.org/rssh/) package is unmaintained, with the author citing unfixable security issues as the reason.

 With the author citing unfixable security issues, adding `rssh` to AL2023 is not planned.

## `sscg` - self-signed SSL certificate generator
<a name="sscg"></a>

 The `sscg` package was in AL2 core, as well as in EPEL7. The `sscg` package is also part of AL2023.

```
[ec2-user ~]$ sudo dnf install {{sscg}}
```

## `stress` - Stress test
<a name="stress"></a>

 The `stress` package was in EPEL7, and was also available in AL1

 The `stress` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{stress}}
```

## `stress-ng` - Stress test
<a name="stress-ng"></a>

 The `stress-ng` package was in EPEL7, and was also available in the `testing` AL2 Extra.

 The `stress-ng` package is included in AL2023 and can be installed by running the following command:

```
[ec2-user ~]$ sudo dnf install {{stress-ng}}
```

## `tmpwatch` - removes files based on last accessed time
<a name="tmpwatch"></a>

 In Amazon Linux 2023, this functionality is provided by [https://www.freedesktop.org/software/systemd/man/latest/systemd-tmpfiles.html](https://www.freedesktop.org/software/systemd/man/latest/systemd-tmpfiles.html).

## `xmlstarlet` - command line XML utilities
<a name="xmlstarlet"></a>

 The `xmlstarlet` package was in EPEL7, and is not available in AL2023.

 The upstream package has not been touched in over 9 years (last touched in August 2014). For an additional four years prior (since at least July 2010), a request for a new maintainer has gone unanswered. It is for this reason that it is not planned to add `xmlstarlet` to AL2023.
