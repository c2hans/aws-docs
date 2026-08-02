---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/security-inplace-update.html
---

# Applying security updates in-place
<a name="security-inplace-update"></a>

 For an overview of applying updates, see [Applying security updates using DNF and repository versions](managing-repos-os-updates.md#apply-security-updates). The `--security` option to `dnf upgrade` will restrict package updates to only those which have an Advisory. The remainder of this section will cover how to install only specific security updates.

**Note**
 It is recommended to apply *all* updates available in a new AL2023 release. Picking just security updates, or only specific updates should be the exception rather than rule.

## Applying updates mentioned in an Advisory
<a name="applying-advisory-updates"></a>

 The advisory identifiers in the first column of the output of `dnf upgradeinfo` can be used to apply updates for the packages mentioned in the advisory. The `dnf` package manager can be instructed to update the packages in the advisory to either the latest available, or only up to the versions mentioned in the advisory. If the updates are already installed, the update command is a no-op.

 To apply the updates for affected packages *only up to the version mention in the advisory*, use the `dnf upgrade-minimal` command while using the `--advisory` option to specify the advisory. The following example is running `dnf upgrade-minimal` in an AL2023 version [2023.0.20230315](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html) container.

```
$ dnf upgrade-minimal -y --releasever={{2023.1.20230628}} --advisory ALAS2023-2023-193
Amazon Linux 2023 repository                     46 MB/s |  15 MB     00:00
Last metadata expiration check: 0:00:03 ago on Mon Jul 22 20:36:13 2024.
Dependencies resolved.
================================================================================
 Package              Arch        Version                Repository        Size
================================================================================
Upgrading:
 curl-minimal         x86_64      8.0.1-1.amzn2023       amazonlinux      150 k
 libcurl-minimal      x86_64      8.0.1-1.amzn2023       amazonlinux      249 k

Transaction Summary
================================================================================
Upgrade  2 Packages

Total download size: 399 k
Downloading Packages:
(1/2): curl-minimal-8.0.1-1.amzn2023.x86_64.rpm 2.7 MB/s | 150 kB     00:00
(2/2): libcurl-minimal-8.0.1-1.amzn2023.x86_64. 3.8 MB/s | 249 kB     00:00
--------------------------------------------------------------------------------
Total                                           2.5 MB/s | 399 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1
  Upgrading        : libcurl-minimal-8.0.1-1.amzn2023.x86_64                1/4
  Upgrading        : curl-minimal-8.0.1-1.amzn2023.x86_64                   2/4
  Cleanup          : curl-minimal-7.88.1-1.amzn2023.0.1.x86_64              3/4
  Cleanup          : libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64           4/4
  Running scriptlet: libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64           4/4
  Verifying        : libcurl-minimal-8.0.1-1.amzn2023.x86_64                1/4
  Verifying        : libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64           2/4
  Verifying        : curl-minimal-8.0.1-1.amzn2023.x86_64                   3/4
  Verifying        : curl-minimal-7.88.1-1.amzn2023.0.1.x86_64              4/4

Upgraded:
  curl-minimal-8.0.1-1.amzn2023.x86_64  libcurl-minimal-8.0.1-1.amzn2023.x86_64

Complete!
```

 The same package versions are updated even if `--releasever=latest` is used as the request is for `dnf` to do the *minimal update required* to address the advisory.

 Using the regular `dnf upgrade` command with the `--advisory` option will update the relevant packages mentioned in the advisory to the *latest* version available, which may be newer than the version mentioned in the advisory.

**Note**
 Unless the `system-release` package is updated, the version of the AL2023 repositories which `dnf` is locked to *does not change*.

**Warning**
 When installing updates from a different release of AL2023 without changing the version of the repository that `dnf` is locked to, care *must* be taken on any subsequent mutating `dnf` operations. For example, when installing or updating packages, since package dependencies may have changed in the newer release, the older release that you remain on may not be able to satisfy these new dependencies.

 The following example is run in an AL2023 version [2023.0.20230315](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html) container referring to the latest release of AL2023 which the time of writing was [2023.5.20240708](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html). Note that both the version of `curl` being updated to is newer than the version `update-minimal` updated to, but that this newer version brings in new dependencies.

```
$ dnf upgrade -y --releasever={{latest}} --advisory ALAS2023-2023-193
Amazon Linux 2023 repository                     80 MB/s |  25 MB     00:00
Last metadata expiration check: 0:00:04 ago on Mon Jul 22 20:48:38 2024.
Dependencies resolved.
================================================================================
 Package                   Arch     Version                 Repository     Size
================================================================================
Upgrading:
 curl-minimal              x86_64   8.5.0-1.amzn2023.0.4    amazonlinux   160 k
 libcurl-minimal           x86_64   8.5.0-1.amzn2023.0.4    amazonlinux   275 k
 libnghttp2                x86_64   1.59.0-3.amzn2023.0.1   amazonlinux    79 k
Installing dependencies:
 libpsl                    x86_64   0.21.1-3.amzn2023.0.2   amazonlinux    61 k
 publicsuffix-list-dafsa   noarch   20240212-61.amzn2023    amazonlinux    59 k

Transaction Summary
================================================================================
Install  2 Packages
Upgrade  3 Packages

Total download size: 634 k
Downloading Packages:
(1/5): publicsuffix-list-dafsa-20240212-61.amzn 1.1 MB/s |  59 kB     00:00
(2/5): curl-minimal-8.5.0-1.amzn2023.0.4.x86_64 2.6 MB/s | 160 kB     00:00
(3/5): libpsl-0.21.1-3.amzn2023.0.2.x86_64.rpm  949 kB/s |  61 kB     00:00
(4/5): libnghttp2-1.59.0-3.amzn2023.0.1.x86_64. 3.7 MB/s |  79 kB     00:00
(5/5): libcurl-minimal-8.5.0-1.amzn2023.0.4.x86 6.7 MB/s | 275 kB     00:00
--------------------------------------------------------------------------------
Total                                           3.5 MB/s | 634 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1
  Upgrading        : libnghttp2-1.59.0-3.amzn2023.0.1.x86_64                1/8
  Installing       : publicsuffix-list-dafsa-20240212-61.amzn2023.noarch    2/8
  Installing       : libpsl-0.21.1-3.amzn2023.0.2.x86_64                    3/8
  Upgrading        : libcurl-minimal-8.5.0-1.amzn2023.0.4.x86_64            4/8
  Upgrading        : curl-minimal-8.5.0-1.amzn2023.0.4.x86_64               5/8
  Cleanup          : curl-minimal-7.88.1-1.amzn2023.0.1.x86_64              6/8
  Cleanup          : libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64           7/8
  Cleanup          : libnghttp2-1.51.0-1.amzn2023.x86_64                    8/8
  Running scriptlet: libnghttp2-1.51.0-1.amzn2023.x86_64                    8/8
  Verifying        : libpsl-0.21.1-3.amzn2023.0.2.x86_64                    1/8
  Verifying        : publicsuffix-list-dafsa-20240212-61.amzn2023.noarch    2/8
  Verifying        : curl-minimal-8.5.0-1.amzn2023.0.4.x86_64               3/8
  Verifying        : curl-minimal-7.88.1-1.amzn2023.0.1.x86_64              4/8
  Verifying        : libcurl-minimal-8.5.0-1.amzn2023.0.4.x86_64            5/8
  Verifying        : libcurl-minimal-7.88.1-1.amzn2023.0.1.x86_64           6/8
  Verifying        : libnghttp2-1.59.0-3.amzn2023.0.1.x86_64                7/8
  Verifying        : libnghttp2-1.51.0-1.amzn2023.x86_64                    8/8

Upgraded:
  curl-minimal-8.5.0-1.amzn2023.0.4.x86_64
  libcurl-minimal-8.5.0-1.amzn2023.0.4.x86_64
  libnghttp2-1.59.0-3.amzn2023.0.1.x86_64
Installed:
  libpsl-0.21.1-3.amzn2023.0.2.x86_64
  publicsuffix-list-dafsa-20240212-61.amzn2023.noarch

Complete!
```
