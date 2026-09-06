---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/manage-updates.html
---

# Manage package and operating system updates in AL2027
<a name="manage-updates"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 AMIs and container images lock to a specific version of the AL2027 repositories. To apply security and bug fixes to an existing system, update to a newer release version. Alternatively, launch a new instance from a newer AMI. This section describes how to manage packages and repositories on a running system. For the complete command reference, see the [DNF5 documentation](https://dnf5.readthedocs.io/en/latest/index.html) on the dnf5.readthedocs.io website.

We recommend applying *all* updates available in a new AL2027 release. Picking only security updates, or only specific updates, should be the exception rather than the rule. To list which security advisories are relevant to an instance, see [Listing applicable advisories](security-dnf-updateinfo.md). To install only the updates from a specific advisory, see [Applying security updates in-place](security-update-advisory.md).

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

**Topics**
+ [Checking for available package updates](#dnf-package-updates)
+ [Applying updates using DNF and repository versions](#apply-security-updates)
+ [Checking for newer repository versions with `dnf check-release-update`](#dnf-repository-updates)
+ [Getting package support information](#dnf-support-info-plugin)
+ [Launching an instance with a specific repository version enabled](#launch-an-instance-repo-version)
+ [Adding, enabling, or disabling new repositories](#dnf-repo-addition)
+ [Adding repositories with cloud-init](#cloud-init-repo-update)
+ [Automatic service restart after updates](#automatic-restart-services)
+ [When is a reboot required to apply updates?](#reboot)

## Checking for available package updates
<a name="dnf-package-updates"></a>

Use the `dnf check-update` command to check for updates. In AL2027 this is a compatibility alias for `dnf check-upgrade`; both spellings work. Without options, the command only checks the release version the system is locked to. Add `--releasever={{version}}` to check what a newer release would update.

In the following example, a system on the 2027.0.20260803 release checks what the 2027.0.20260817 release would update:

```
dnf check-update --releasever=2027.0.20260817
```

```
Updating and loading repositories:
 Amazon Linux 2027 repository           100% |  15.1 MiB/s |   2.4 MiB |  00m00s
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

To always check against the newest release, use `--releasever=latest`. On this system it reports the same packages, because 2027.0.20260817 is the newest release:

```
dnf check-update --releasever=latest
```

The command exits with return code 100 if newer packages are available, and 0 if there aren't any. Checking for updates does not require elevated privileges.

## Applying updates using DNF and repository versions
<a name="apply-security-updates"></a>

New package updates and security updates are made available in new repository versions only. For systems locked to an earlier release, pass the target release version to apply all updates available in it:

```
sudo dnf upgrade --releasever=<version>
```

DNF lists the package updates and asks for confirmation before applying them. Use the `-y` option to skip the confirmation prompt in scripts and other automation. After the upgrade, the system is locked to the new release version.

Applying updates is a privileged operation. On an Amazon EC2 instance, run the command as the `root` user, for example with `sudo`. In a container, elevated privileges are typically not required.

Applying all updates moves existing systems to the same package set as launching an updated AMI, which reduces variation of package versions across a fleet.

## Checking for newer repository versions with `dnf check-release-update`
<a name="dnf-repository-updates"></a>

The `dnf check-release-update` command reports when a newer AL2027 release than the one the system is locked to is available, and prints the exact command to upgrade to it:

```
sudo dnf check-release-update
```

```
WARNING:
  A newer release of Amazon Linux is available.

  Available Versions:

  Version 2027.0.20260817:
    Run the following command to upgrade to 2027.0.20260817:

      dnf upgrade --releasever=2027.0.20260817

    Release notes:
     https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes-2027.0.20260817.html
```

If the system is already on the newest release, the command prints nothing and exits with return code 0.

The `dnf-plugin-release-notification` package provides the command, which is installed by default on AL2027 AMIs. AL2027 container images don't include it. To use it in a container, install the package first:

```
sudo dnf install dnf-plugin-release-notification
```

## Getting package support information
<a name="dnf-support-info-plugin"></a>

Each package in AL2027 has an associated support timeline. Query it with the `dnf supportinfo` command:

```
dnf supportinfo --pkg bash
```

```
Name                         : bash
Version                      : 5.3.0-2.amzn2027
State                        : installed
Origin                       : Amazon Linux 2027 Core
Support Timeline             : from 2026-09-03     : supported (Low, Medium, Important, Critical)
                             : from 2027-03-31     : unsupported
Package Note                 : Amazon Linux will support this package until the end of the AL2027 public preview period
```

The `dnf-plugin-support-info` package provides the command. If it isn't present on your system, install it first:

```
sudo dnf install dnf-plugin-support-info
```

**Note**
During the preview period, the support timelines reflect the preview terms. Support statements for GA will be published before the public release.

## Launching an instance with a specific repository version enabled
<a name="launch-an-instance-repo-version"></a>

You can add DNF commands to a user data script to control which packages are installed when an AL2027 instance launches. In the following example, the user data script makes sure that every instance launched with it has the same package updates installed:

```
#!/bin/bash
dnf upgrade -y --releasever=2027.0.20260817
# Additional setup and install commands below
dnf install -y httpd mariadb1011-server
```

User data scripts run as the `root` user at launch. For more information, see [User data and shell scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-shell-scripts) in the *Amazon EC2 User Guide*.

**Note**
Instead of using a user data script, launch the latest AL2027 AMI, or a custom AMI based on it. The latest AMI has all current updates installed and is locked to the matching repository version.

## Adding, enabling, or disabling new repositories
<a name="dnf-repo-addition"></a>

**Warning**
Only add repositories designed to be used with AL2027. Repositories designed for other distributions might appear to work, but there is no guarantee they keep working across package updates.

Repositories are defined in configuration files in `/etc/yum.repos.d/`. Many third-party repositories provide either the configuration file content or an installable package that includes it. To list the configured repositories:

```
dnf repolist --all
```

```
repo id               repo name                                        status
amazonlinux           Amazon Linux 2027 repository                    enabled
amazonlinux-debuginfo Amazon Linux 2027 repository - Debug           disabled
amazonlinux-source    Amazon Linux 2027 repository - Source packages disabled
```

Repository management commands are provided by the `dnf5-plugins` package. If `dnf config-manager` reports an unknown command, install it first:

```
sudo dnf install dnf5-plugins
```

To add a repository from a repository configuration file URL:

```
sudo dnf config-manager addrepo --from-repofile=<url>
```

To define a repository directly:

```
sudo dnf config-manager addrepo --id=<repo-id> --set=baseurl=<url>
```

To enable or disable a repository:

```
sudo dnf config-manager setopt <repo-id>.enabled=1
sudo dnf config-manager setopt <repo-id>.enabled=0
```

**Note**
The DNF (version 4) spelling `dnf config-manager --add-repo` changed in DNF5 to the `addrepo` subcommand shown earlier in this section. The `yum-config-manager` command is not available in AL2027. Update scripts that use either spelling.

## Adding repositories with cloud-init
<a name="cloud-init-repo-update"></a>

You can also add a repository at launch time with `cloud-init` user data. The following template writes a repository definition to `/etc/yum.repos.d/`:

```
#cloud-config
yum_repos:
  repository.repo:
    baseurl: https://www.example.com/
    enabled: true
    gpgcheck: true
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EXAMPLE
    name: Example Repository
```

You can add a `packages:` section to the same file to install packages from the default repositories or from the repository you added. For details of the file format, see [Adding a YUM repository](https://cloudinit.readthedocs.io/en/latest/reference/examples.html#adding-a-yum-repository) in the `cloud-init` documentation on the cloudinit.readthedocs.io website. Pass the file to the instance with the `--user-data` option of `aws ec2 run-instances`.

## Automatic service restart after updates
<a name="automatic-restart-services"></a>

After you apply updates, running services can still use the old, replaced versions of libraries until they restart. The `smart-restart` package restarts affected `systemd` services automatically after each DNF transaction. It uses the `dnf needs-restarting` command to find the affected services, and it decides whether a full reboot is advised. When a reboot is advised, it writes a hint marker file at `/run/smart-restart/reboot-hint-marker`.

```
sudo dnf install smart-restart
```

After installation, every subsequent transaction triggers the `smart-restart` logic.

To exclude services from automatic restart, add a file with the `-denylist` suffix in `/etc/smart-restart-conf.d/`. Excluded services also don't count toward the reboot decision. All `*-denylist` files in the directory are evaluated:

```
cat /etc/smart-restart-conf.d/custom-denylist
```

```
# Services that smart-restart must not restart
myservice.service
```

To run your own steps around a restart, place scripts with the `-pre-restart` or `-post-restart` suffix in `/etc/smart-restart-conf.d/`. When order matters, prefix the script names with a number.

## When is a reboot required to apply updates?
<a name="reboot"></a>

In some situations, AL2027 requires a reboot to apply updates:
+ Updates to the Linux kernel package require a reboot to activate the new kernel.
+ On Amazon EC2 metal instances, CPU microcode updates (the `microcode_ctl` package for Intel and the `amd-ucode-firmware` package for AMD) activate on the next reboot. For virtualized instances, the underlying [AWS Nitro System](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html) handles microcode updates for you.
+ Some running `systemd` services only function correctly after a full system restart. The `smart-restart` mechanism informs you about these situations by leaving reboot hints. See [Automatic service restart after updates](#automatic-restart-services).
