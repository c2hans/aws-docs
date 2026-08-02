---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades-usage.html
---

# Using Deterministic upgrades through versioned repositories
<a name="deterministic-upgrades-usage"></a>

**Topics**
+ [Using a deterministic upgraded system](#using-a-deterministic-upgraded-system)
+ [Selective update of a deterministic upgraded system](#deterministic-upgrade-selective-update)
+ [Using persistent override with deterministic upgrade](#deterministic-upgrade-override-persist)

## Using a deterministic upgraded system
<a name="using-a-deterministic-upgraded-system"></a>

**Note**
 The default behavior of the package manager has changed from AL2.

 Deterministic upgrades are a powerful way to ensure all changes to production environments can be fully tested before wide deployment. Each new AL2023 AMI is locked to a particular version of AL2023. This provides deterministic behavior of what versions of OS packages are installed when launching the specific AMI. In-place updates can be to a specific release version, ensuring deterministic behavior across a fleet. As you move to new AMIs or in-place update versions, you can test each one in your CI/CD pipeline, catching any potential issues before deploying to production environments.

 You can use tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to orchestrate applying updates across a fleet. For building derived AMIs when new AL2023 AMIs are released, [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/) can automatically build, patch, and test AMIs, or you can [Receive notifications on new updates](receive-update-notification.md) to know when new base AMIs are available, or to trigger your own AMI building pipelines.

 For information on restricting updates to those from a particular advisory, see [Applying security updates in-place](security-inplace-update.md)

 For patching in-place, you can use the `dnf` package manager. When you run the `dnf upgrade` command, the system checks for upgrades in the repository that the `releasever` variable specifies. A valid `releasever` is either {{latest}} or a date-stamped version such as {{2023.12.20260724}}.

You can change the value of `releasever` using one of the following methods. These methods are listed in descending system priority. This means that method 1 overrides methods 2 and 3, and method 2 overrides method 3.

1. The value in the command line flag, `--releasever={{latest}}`, if it's used.

1. The value that's specified in the override variable file, `/etc/dnf/vars/releasever`, if it's set.

1. The currently installed version of the `system-release` package.

In the following example, the version is {{2023.0.20230210}}:

```
$ rpm -q system-release
system-release-2023.0.20230210-0.amzn2023.noarch
```

In a newly installed system, the override variable is not present. No upgrades are available because the system is locked to the installed version of `system-release`.

```
$ cat /etc/dnf/vars/releasever
cat: /etc/dnf/vars/releasever: No such file or directory
```

```
$ sudo dnf upgrade
Last metadata expiration check: 0:00:02 ago on Wed 15 Feb 2023 06:14:12 PM UTC.
Dependencies resolved.
Nothing to do.
Complete!
```

You can get packages of a specific version by using the `releasever` flag to provide the version that you want.

```
$ rpm -q system-release
system-release-2023.0.20230222-0.amzn2023.noarch
```

```
$ sudo dnf upgrade --releasever=2023.0.20230329
Amazon Linux 2023 repository                     26 MB/s |  12 MB     00:00
Dependencies resolved.
================================================================================
 Package                 Arch    Version                      Repository   Size
================================================================================
Installing:
 kernel                   aarch64 6.1.21-1.45.amzn2023        amazonlinux  26 M
Upgrading:
 amazon-linux-repo-s3     noarch  2023.0.20230329-0.amzn2023  amazonlinux  18 k
 ca-certificates          noarch  2023.2.60-1.0.amzn2023.0.1  amazonlinux 828 k
 cloud-init               noarch  22.2.2-1.amzn2023.1.7       amazonlinux 1.1 M

         ... [ list edited for clarity ]

 system-release           noarch  2023.0.20230329-0.amzn2023  amazonlinux  29 k

         ... [ list edited for clarity ]

 vim-data                 noarch  2:9.0.1403-1.amzn2023.0.1   amazonlinux  25 k
 vim-minimal              aarch64 2:9.0.1403-1.amzn2023.0.1   amazonlinux 753 k

Transaction Summary
================================================================================
Install    1 Package
Upgrade   42 Packages

Total download size: 56 M
```

Because the `--releasever` option overrides both `system-release` and `/etc/dnf/vars/releasever`, the result of this upgrade is the following:

1. The upgrade replaces all installed packages that changed between the previous and new versions.

1. The upgrade locks the system to the repository for the new version of `system-release`.

 By always specifying what `releasever` (i.e. AL2023 release) to update to, you have a deterministic set of changes across a fleet. You launched version {{A}}, updated to {{B}}, and then updated to {{C}}.

## Selective update of a deterministic upgraded system
<a name="deterministic-upgrade-selective-update"></a>

**Note**
 We recommend that all updates in a new release are installed rather than selecting specific updates. Only applying part of an update to the OS should be an exception to standard practice of taking the whole update.

You might want to install selected packages from a recent release, while leaving the system locked to the original release version.

You can use `dnf check-update` to identify the packages that you want to upgrade.

```
$ sudo dnf check-update --releasever=latest --security
Amazon Linux 2023 repository                     13 MB/s |  10 MB     00:00
Last metadata expiration check: 0:00:02 ago on Wed 15 Feb 2023 02:52:21 AM UTC.

bind-libs.aarch64                  32:9.16.27-1.amzn2023.0.1         amazonlinux
bind-license.noarch                32:9.16.27-1.amzn2023.0.1         amazonlinux
bind-utils.aarch64                 32:9.16.27-1.amzn2023.0.1         amazonlinux
cryptsetup.aarch64                 2.4.3-2.amzn2023.0.1              amazonlinux
cryptsetup-libs.aarch64            2.4.3-2.amzn2023.0.1              amazonlinux
curl-minimal.aarch64               7.85.0-1.amzn2023.0.1             amazonlinux
glibc.aarch64                      2.34-40.amzn2023.0.2              amazonlinux
glibc-all-langpacks.aarch64        2.34-40.amzn2023.0.2              amazonlinux
glibc-common.aarch64               2.34-40.amzn2023.0.2              amazonlinux
glibc-locale-source.aarch64        2.34-40.amzn2023.0.2              amazonlinux
gmp.aarch64                        1:6.2.1-2.amzn2023.0.1            amazonlinux
gnupg2-minimal.aarch64             2.3.7-1.amzn2023.0.2              amazonlinux
gzip.aarch64                       1.10-5.amzn2023.0.1               amazonlinux
kernel.aarch64                     6.1.12-17.42.amzn2023             amazonlinux
kernel-tools.aarch64               6.1.12-17.42.amzn2023             amazonlinux
libarchive.aarch64                 3.5.3-2.amzn2023.0.1              amazonlinux
libcurl-minimal.aarch64            7.85.0-1.amzn2023.0.1             amazonlinux
libsepol.aarch64                   3.4-3.amzn2023.0.2                amazonlinux
libsolv.aarch64                    0.7.22-1.amzn2023.0.1             amazonlinux
libxml2.aarch64                    2.9.14-1.amzn2023.0.1             amazonlinux
logrotate.aarch64                  3.20.1-2.amzn2023.0.2             amazonlinux
lua-libs.aarch64                   5.4.4-3.amzn2023.0.1              amazonlinux
lz4-libs.aarch64                   1.9.4-1.amzn2023.0.1              amazonlinux
openssl.aarch64                    1:3.0.5-1.amzn2023.0.3            amazonlinux
openssl-libs.aarch64               1:3.0.5-1.amzn2023.0.3            amazonlinux
pcre2.aarch64                      10.40-1.amzn2023.0.1              amazonlinux
pcre2-syntax.noarch                10.40-1.amzn2023.0.1              amazonlinux
rsync.aarch64                      3.2.6-1.amzn2023.0.2              amazonlinux
vim-common.aarch64                 2:9.0.475-1.amzn2023.0.1          amazonlinux
vim-data.noarch                    2:9.0.475-1.amzn2023.0.1          amazonlinux
vim-enhanced.aarch64               2:9.0.475-1.amzn2023.0.1          amazonlinux
vim-filesystem.noarch              2:9.0.475-1.amzn2023.0.1          amazonlinux
vim-minimal.aarch64                2:9.0.475-1.amzn2023.0.1          amazonlinux
xz.aarch64                         5.2.5-9.amzn2023.0.1              amazonlinux
xz-libs.aarch64                    5.2.5-9.amzn2023.0.1              amazonlinux
zlib.aarch64                       1.2.11-32.amzn2023.0.3            amazonlinux
```

Install the packages that you want to upgrade. Use `sudo dnf upgrade --releasever=latest` and the package names to ensure that the `system-release` package remains unchanged.

```
$ sudo dnf upgrade --releasever=latest openssl openssl-libs
Last metadata expiration check: 0:01:28 ago on Wed 15 Feb 2023 02:52:21 AM UTC.
Dependencies resolved.
================================================================================
 Package          Arch        Version                     Repository       Size
================================================================================
Upgrading:
 openssl          aarch64     1:3.0.5-1.amzn2023.0.3      amazonlinux     1.1 M
 openssl-libs     aarch64     1:3.0.5-1.amzn2023.0.3      amazonlinux     2.1 M

Transaction Summary
================================================================================
Upgrade  2 Packages

Total download size: 3.2 M
```

**Note**
Using `sudo dnf upgrade --releasever=latest` updates all packages, including `system-release`. Then, the version remains locked to the new `system-release` unless you set the persistent override.

## Using persistent override with deterministic upgrade
<a name="deterministic-upgrade-override-persist"></a>

**Note**
 With deterministic updates, you can integrate OS changes into your CI/CD pipeline. Disabling deterministic updates removes the ability to test before deploying.

Instead of adding `--releasever=latest`, you can use persistent override to *unlock* the system by setting the variable value to {{latest}}. By always using `latest`, this reverts the behavior of AL2023 to the AL2 update model, where any call to the package manager will *always* look at the latest release, and is not locked to any specific version of the OS.

**Warning**
 By unlocking the package manager by using a persistent override of deterministic updates, you take the risk discovering any possible incompatibility between your application and an OS update in production.
 While incompatibilites *are* rare, with an OS update you are integrating new code changes into your environment, integration tests can prevent deploying code changes that have a negative impact on production environments.

```
$ echo latest | sudo tee /etc/dnf/vars/releasever
latest
```

```
$ sudo dnf upgrade
Last metadata expiration check: 0:03:36 ago on Wed 15 Feb 2023 02:52:21 AM UTC.
Dependencies resolved.
================================================================================
 Package                 Arch    Version                      Repository   Size
================================================================================
Installing:
 kernel                  aarch64 6.1.73-45.135.amzn2023       amazonlinux  24 M
Upgrading:
 acl                     aarch64 2.3.1-2.amzn2023.0.1         amazonlinux  72 k
 alternatives            aarch64 1.15-2.amzn2023.0.1          amazonlinux  36 k
 amazon-ec2-net-utils    noarch  2.3.0-1.amzn2023.0.1         amazonlinux  16 k
 at                      aarch64 3.1.23-6.amzn2023.0.1        amazonlinux  60 k
 attr                    aarch64 2.5.1-3.amzn2023.0.1         amazonlinux  59 k
 audit                   aarch64 3.0.6-1.amzn2023.0.1         amazonlinux 249 k
 audit-libs              aarch64 3.0.6-1.amzn2023.0.1         amazonlinux 116 k
 aws-c-auth-libs         aarch64 0.6.5-6.amzn2023.0.2         amazonlinux  79 k
 aws-c-cal-libs          aarch64 0.5.12-7.amzn2023.0.2        amazonlinux  34 k
 aws-c-common-libs       aarch64 0.6.14-6.amzn2023.0.2        amazonlinux 119 k
 aws-c-compression-libs  aarch64 0.2.14-5.amzn2023.0.2        amazonlinux  22 k
 aws-c-event-stream-libs aarch64 0.2.7-5.amzn2023.0.2         amazonlinux  47 k
 aws-c-http-libs         aarch64 0.6.8-6.amzn2023.0.2         amazonlinux 147 k
 aws-c-io-libs           aarch64 0.10.12-5.amzn2023.0.6       amazonlinux 109 k
 aws-c-mqtt-libs         aarch64 0.7.8-7.amzn2023.0.2         amazonlinux  61 k
 aws-c-s3-libs           aarch64 0.1.27-5.amzn2023.0.3        amazonlinux  54 k
 aws-c-sdkutils-libs     aarch64 0.1.1-5.amzn2023.0.2         amazonlinux  26 k
 aws-checksums-libs      aarch64 0.1.12-5.amzn2023.0.2        amazonlinux  50 k
 awscli-2                noarch  2.7.8-1.amzn2023.0.4         amazonlinux 7.3 M
 basesystem              noarch  11-11.amzn2023.0.1           amazonlinux 7.8 k
 bash                    aarch64 5.1.8-2.amzn2023.0.1         amazonlinux 1.6 M
 bash-completion         noarch  1:2.11-2.amzn2023.0.1        amazonlinux 292 k
 bc                      aarch64 1.07.1-14.amzn2023.0.1       amazonlinux 120 k
 bind-libs               aarch64 32:9.16.27-1.amzn2023.0.1    amazonlinux 1.2 M
 bind-license            noarch  32:9.16.27-1.amzn2023.0.1    amazonlinux  14 k
 bind-utils              aarch64 32:9.16.27-1.amzn2023.0.1    amazonlinux 206 k
 binutils                aarch64 2.38-20.amzn2023.0.3         amazonlinux 4.6 M
 boost-filesystem        aarch64 1.75.0-4.amzn2023.0.1        amazonlinux  55 k
 boost-system            aarch64 1.75.0-4.amzn2023.0.1        amazonlinux  14 k
 boost-thread            aarch64 1.75.0-4.amzn2023.0.1        amazonlinux  54 k
 bzip2                   aarch64 1.0.8-6.amzn2023.0.1         amazonlinux  53 k
 bzip2-libs              aarch64 1.0.8-6.amzn2023.0.1         amazonlinux  44 k
 c-ares                  aarch64 1.17.2-1.amzn2023.0.1        amazonlinux 107 k
 ca-certificates         noarch  2021.2.50-1.0.amzn2023.0.3   amazonlinux 343 k
 checkpolicy             aarch64 3.4-3.amzn2023.0.1           amazonlinux 345 k
 chkconfig               aarch64 1.15-2.amzn2023.0.1          amazonlinux 162 k
 chrony                  aarch64 4.2-7.amzn2023.0.4           amazonlinux 314 k
 cloud-init              noarch  22.2.2-1.amzn2023.1.7        amazonlinux 1.1 M
 cloud-utils-growpart    aarch64 0.31-8.amzn2023.0.2          amazonlinux  31 k
 coreutils               aarch64 8.32-30.amzn2023.0.2         amazonlinux 1.1 M
 coreutils-common        aarch64 8.32-30.amzn2023.0.2         amazonlinux 2.0 M
 cpio                    aarch64 2.13-10.amzn2023.0.1         amazonlinux 269 k
 cracklib                aarch64 2.9.6-27.amzn2023.0.1        amazonlinux  83 k
 cracklib-dicts          aarch64 2.9.6-27.amzn2023.0.1        amazonlinux 3.6 M
 crontabs                noarch  1.11-24.20190603git.amzn2023.0.1
                                                              amazonlinux  19 k
 crypto-policies         noarch  20230128-1.gitdfb10ea.amzn2023.0.1
                                                              amazonlinux  61 k
 crypto-policies-scripts noarch  20230128-1.gitdfb10ea.amzn2023.0.1
                                                              amazonlinux  81 k
...
Installing dependencies:
 amazon-linux-repo-cdn   noarch  2023.0.20230210-0.amzn2023   amazonlinux  16 k
 xxhash-libs             aarch64 0.8.0-3.amzn2023.0.1         amazonlinux  32 k
Installing weak dependencies:
 amazon-chrony-config    noarch  4.2-7.amzn2023.0.4           amazonlinux  14 k
 gawk-all-langpacks      aarch64 5.1.0-3.amzn2023.0.1         amazonlinux 207 k

Transaction Summary
================================================================================
Install    5 Packages
Upgrade  413 Packages

Total download size: 199 M
```

**Note**
If you used the override variable `/etc/dnf/vars/releasever`, use the following command to restore the default locking behavior by erasing the override value.

```
$ sudo rm /etc/dnf/vars/releasever
```

 The use of a persistent override to using `latest` rather than a specfiic version is akin to the default behavior of AL2. There are services that build AMIs based on AL2 which disable this behavior, and lock to specific package versions like you get by default on AL2023.

 Rather than disabling deterministic updates, we recommend replacing instances with ones launched from a new AMI. If instance replacement is not an option, we recommend using tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to orchestrate applying updates across a fleet. [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/) can also automatically build, patch, and test your own AMIs derived from AL2023 base images. You can also [Receive notifications on new updates](receive-update-notification.md) which can be used to trigger your own AMI building pipelines.

 Using `latest` in a pre-production environment, and then deploying to production using `latest` does *not* provide protection from any issue between an OS update and your application. A new AL2023 release can be at any point in time, and thus all uses of `latest` in production carry risk.
