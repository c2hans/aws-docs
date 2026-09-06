---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/deterministic-upgrades-usage.html
---

# Using deterministic upgrades through versioned repositories
<a name="deterministic-upgrades-usage"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

**Topics**
+ [Using a deterministic upgraded system](#using-a-deterministic-upgraded-system)
+ [Selective update of a deterministic upgraded system](#deterministic-upgrade-selective-update)
+ [Using persistent override with deterministic upgrade](#deterministic-upgrade-override-persist)

## Using a deterministic upgraded system
<a name="using-a-deterministic-upgraded-system"></a>

Deterministic upgrades let you test every change before it reaches production. Each AL2027 AMI is locked to a specific release, so instances launched from it start with the same package versions. In-place updates target a specific release version, so the same tested set of changes rolls out across a fleet. Test each new AMI or release version in your CI/CD pipeline before deployment. This catches issues before they reach production.

When you run the `dnf upgrade` command, the system checks for upgrades in the repository version that the `releasever` variable specifies. A valid `releasever` is either `latest` or a date-stamped version such as `2027.0.20260817`. The following methods determine the value of `releasever`, in descending priority. Method 1 overrides methods 2 and 3, and method 2 overrides method 3.

1. The command line flag `--releasever={{version}}`, if it's used.

1. The value in the override variable file `/etc/dnf/vars/releasever`, if it's set.

1. The currently installed version of the `system-release` package.

To see the release version your system is locked to, query the `system-release` package. In the following example, the system is locked to the 2027.0.20260803 release:

```
rpm -q system-release
```

```
system-release-2027.0.20260803-1.amzn2027.noarch
```

In a newly installed system, the override variable file `/etc/dnf/vars/releasever` does not exist, so the system is locked to the installed version of `system-release`. Because the locked release is immutable, running `sudo dnf upgrade` on an up-to-date system makes no changes:

```
sudo dnf upgrade
```

```
Updating and loading repositories:
Repositories loaded.
Nothing to do.
```

To upgrade to a specific release version, pass it with the `--releasever` option:

```
sudo dnf upgrade --releasever=2027.0.20260817
```

```
Updating and loading repositories:
 Amazon Linux 2027 repository           100% |  11.7 MiB/s |   2.4 MiB |  00m00s
Repositories loaded.
Package                                   Arch   Version                      Repository       Size
Upgrading:
 amazon-linux-repo-cdn                    noarch 0:2027.0.20260817-2.amzn2027 amazonlinux   1.1 KiB
   replacing amazon-linux-repo-cdn        noarch 0:2027.0.20260803-1.amzn2027 amazonlinux   1.1 KiB
 krb5-libs                                x86_64 0:1.22.2-6.amzn2027          amazonlinux   2.4 MiB
   replacing krb5-libs                    x86_64 0:1.22.2-1.amzn2027          amazonlinux   2.4 MiB

   ... [ list edited for clarity ]

 openssl                                  x86_64 1:3.5.7-2.amzn2027           amazonlinux   1.8 MiB
   replacing openssl                      x86_64 1:3.5.5-3.amzn2027           amazonlinux   1.8 MiB

   ... [ list edited for clarity ]

 system-release                           noarch 0:2027.0.20260817-2.amzn2027 amazonlinux  15.6 KiB
   replacing system-release               noarch 0:2027.0.20260803-1.amzn2027 amazonlinux  15.6 KiB
 systemd                                  x86_64 0:260.1-11.amzn2027.0.8      amazonlinux  13.3 MiB
   replacing systemd                      x86_64 0:260.1-11.amzn2027.0.7      amazonlinux  13.3 MiB

   ... [ list edited for clarity ]

Transaction Summary:
 Upgrading:         23 packages
 Replacing:         23 packages

Total size of inbound packages is 28 MiB. Need to download 28 MiB.
After this operation, 81 KiB will be freed (install 102 MiB, remove 102 MiB).
```

Because the `--releasever` option overrides both `system-release` and `/etc/dnf/vars/releasever`, this upgrade does the following:

1. Replaces all installed packages that changed between the previous and new versions.

1. When the target release contains a newer `system-release` package, the transaction includes it, which locks the system to the new release for all future `dnf` operations.

By always specifying which AL2027 release to update to, you get a deterministic set of changes across a fleet: you launched version A, updated to B, and then updated to C.

## Selective update of a deterministic upgraded system
<a name="deterministic-upgrade-selective-update"></a>

**Note**
We recommend installing all updates in a new release rather than selecting specific updates. Applying only part of an update should be the exception, not standard practice. For restricting updates to those from a specific security advisory, see [Applying security updates in-place](security-update-advisory.md).

You might want to install selected packages from a newer release while leaving the system locked to the original release version. First, identify the packages that you want to upgrade:

```
sudo dnf check-update --releasever=latest
```

```
Updating and loading repositories:
 Amazon Linux 2027 repository           100% |   6.6 MiB/s |   2.4 MiB |  00m00s
Repositories loaded.
Upgrades
amazon-linux-repo-cdn.noarch        2027.0.20260817-2.amzn2027 amazonlinux
krb5-libs.x86_64                    1.22.2-6.amzn2027          amazonlinux
libssh.x86_64                       0.12.2-1.amzn2027          amazonlinux
libssh-config.noarch                0.12.2-1.amzn2027          amazonlinux
openldap.x86_64                     2.6.13-3.amzn2027          amazonlinux
openssh.x86_64                      9.9p1-28.amzn2027          amazonlinux
openssh-clients.x86_64              9.9p1-28.amzn2027          amazonlinux
openssl.x86_64                      1:3.5.7-2.amzn2027         amazonlinux
openssl-fips-provider-latest.x86_64 1:3.5.7-2.amzn2027         amazonlinux
openssl-libs.x86_64                 1:3.5.7-2.amzn2027         amazonlinux
python-unversioned-command.noarch   3.14.5-2.amzn2027.0.4      amazonlinux
python3.x86_64                      3.14.5-2.amzn2027.0.4      amazonlinux
python3-libs.x86_64                 3.14.5-2.amzn2027.0.4      amazonlinux
qrencode-libs.x86_64                4.1.1-3.amzn2027.0.2       amazonlinux
system-release.noarch               2027.0.20260817-2.amzn2027 amazonlinux
systemd.x86_64                      260.1-11.amzn2027.0.8      amazonlinux
systemd-libs.x86_64                 260.1-11.amzn2027.0.8      amazonlinux
systemd-networkd.x86_64             260.1-11.amzn2027.0.8      amazonlinux
systemd-pam.x86_64                  260.1-11.amzn2027.0.8      amazonlinux
systemd-resolved.x86_64             260.1-11.amzn2027.0.8      amazonlinux
systemd-shared.x86_64               260.1-11.amzn2027.0.8      amazonlinux
systemd-sysusers.x86_64             260.1-11.amzn2027.0.8      amazonlinux
systemd-udev.x86_64                 260.1-11.amzn2027.0.8      amazonlinux
```

Then upgrade only those packages by naming them. Naming specific packages keeps the `system-release` package, and therefore the version lock, unchanged. The transaction includes related packages that the named packages require at the same version, such as `openssl-fips-provider-latest` here:

```
sudo dnf upgrade --releasever=latest openssl openssl-libs
```

```
Updating and loading repositories:
Repositories loaded.
Package                                   Arch   Version            Repository       Size
Upgrading:
 openssl                                  x86_64 1:3.5.7-2.amzn2027 amazonlinux   1.8 MiB
   replacing openssl                      x86_64 1:3.5.5-3.amzn2027 amazonlinux   1.8 MiB
 openssl-fips-provider-latest             x86_64 1:3.5.7-2.amzn2027 amazonlinux   2.5 MiB
   replacing openssl-fips-provider-latest x86_64 1:3.5.5-3.amzn2027 amazonlinux   2.5 MiB
 openssl-libs                             x86_64 1:3.5.7-2.amzn2027 amazonlinux   6.9 MiB
   replacing openssl-libs                 x86_64 1:3.5.5-3.amzn2027 amazonlinux   6.9 MiB

Transaction Summary:
 Upgrading:          3 packages
 Replacing:          3 packages

Total size of inbound packages is 4 MiB. Need to download 4 MiB.
After this operation, 14 KiB will be freed (install 11 MiB, remove 11 MiB).
```

**Note**
Running `sudo dnf upgrade --releasever=latest` without naming packages updates all packages, including `system-release`. The system then remains locked to the new `system-release` version unless you set the persistent override.

## Using persistent override with deterministic upgrade
<a name="deterministic-upgrade-override-persist"></a>

Instead of adding `--releasever=latest` to each command, you can *unlock* the system by setting the variable file to `latest`. This reverts AL2027 to the AL2 update model, where every package manager invocation uses the latest release and does not lock to any specific version of the OS:

```
echo latest | sudo tee /etc/dnf/vars/releasever
```

```
latest
```

**Warning**
Unlocking the package manager with a persistent override removes the ability to test an OS update before it reaches production. A new AL2027 release can happen at any point in time, so all uses of `latest` in production carry the risk of discovering an incompatibility between your application and an OS update in production.

To restore the default locking behavior, remove the override file:

```
sudo rm /etc/dnf/vars/releasever
```

Rather than disabling deterministic upgrades, we recommend replacing instances with ones launched from a new AMI. If instance replacement is not an option, use tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to orchestrate applying updates across a fleet, or [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/) to automatically build, patch, and test your own AMIs derived from AL2027 base images.
