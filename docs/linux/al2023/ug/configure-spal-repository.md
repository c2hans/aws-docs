---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/configure-spal-repository.html
---

# Tutorial: Configure SPAL repository on AL2023
<a name="configure-spal-repository"></a>

Supplementary Packages for Amazon Linux (SPAL) is an additional package repository for AL2023 that provides customers access to thousands of open-source packages.

 The following tutorial helps you configure the SPAL repository on your AL2023 instance. By installing the repository, you will gain access to all RPM packages available in SPAL. Once installed, you can use your package manager to install and use these packages on your system.

**Topics**
+ [Prerequisites](#configure-spal-prereqs)
+ [Checking prerequisites](#configure-spal-check-prereqs)
+ [Installing SPAL on your system](#configure-spal-install)
+ [Installing SPAL packages](#configure-spal-install-pkgs)
+ [Downloading SPAL source packages](#configure-spal-source-pkgs)
+ [Installing SPAL debuginfo packages](#configure-spal-debuginfo-pkgs)
+ [Uninstalling SPAL repository from your system](#configure-spal-uninstall)
+ [Related topics](#configure-spal-more-info)

## Prerequisites
<a name="configure-spal-prereqs"></a>

This tutorial assumes that you have already launched an instance using AL2023 release version `2023.9.20251117` or later. For more information, see the [AL2023 on Amazon EC2](ec2.md) and [Updating AL2023](updating.md) pages.

## Checking prerequisites
<a name="configure-spal-check-prereqs"></a><a name="check-prereqs"></a>
+ To verify your instance satisfies the prerequisites, you can check the version of `system-release` installed on your system.

  To check the version of the package, you can use the following command.

  ```
  [ec2-user ~]$ rpm -qi system-release
  ```

  The command will display information about the package, including the major version.

  ```
  Name        : system-release
  Version     : 2023.9.20251117
  ...
  ```
**Note**
Make sure to have the latest version of `system-release` installed. You can run `sudo dnf upgrade` to update to the latest version.

## Installing SPAL on your system
<a name="configure-spal-install"></a><a name="install-spal"></a>

1. Install the `spal-release` package on your system. This adds the `.repo` configuration file and the GPG keys to your system.

   ```
   [ec2-user ~]$ sudo dnf install spal-release
   ```
**Note**
 During the installation, the support statement will be displayed. The statement explains SPAL's scope of support and limitations. Please take time to review this information carefully.

1. Verify the SPAL repository configuration was successfully added to your system.

   ```
   [ec2-user ~]$ cat /etc/yum.repos.d/amazonlinux-spal.repo
   ```

   You should see the three repositories configured on your system: `amazonlinux-spal`, `amazonlinux-spal-source`, and `amazonlinux-spal-debuginfo`.

   You can also check the list of configured repositories by running `dnf repolist`.

   ```
   [ec2-user ~]$ dnf repolist --all
   ```
**Note**
 The `--all` flag is required to see both enabled and disabled repositories.

   All three SPAL repositories should be available. Note that the **Amazon Linux 2023 SPAL repository - Source packages** and **Amazon Linux 2023 SPAL repository - Debug** repositories are disabled by default.

   ```
   repo id                       repo name                                                status
   amazonlinux-spal              Amazon Linux 2023 SPAL repository                        enabled
   amazonlinux-spal-source       Amazon Linux 2023 SPAL repository - Source packages      disabled
   amazonlinux-spal-debuginfo    Amazon Linux 2023 SPAL repository - Debug                disabled
   ```

## Installing SPAL packages
<a name="configure-spal-install-pkgs"></a><a name="install-pkgs-spal"></a>
+ Install SPAL packages on your system by running `dnf install` command.

  ```
  [ec2-user ~]$ sudo dnf install {{package}}
  ```
**Note**
 You can use `dnf list` to see a complete list of SPAL packages.

  ```
  [ec2-user ~]$ dnf list --repo=amazonlinux-spal
  ```
**Note**
 SPAL is a versioned repository. Make sure to have the latest version of `system-release` installed to see the most recent list of packages.
 For more information on deterministic updates, you can check [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md)

## Downloading SPAL source packages
<a name="configure-spal-source-pkgs"></a>

RPM source (SRPM) packages are primarily used by developers for building packages from source. The SPAL source repository is disabled by default. DNF automatically enables it when you use commands that require source packages.

To download the source RPM for an SPAL package, run the following command:

```
[ec2-user ~]$ dnf download --source {{package}}
```

## Installing SPAL debuginfo packages
<a name="configure-spal-debuginfo-pkgs"></a>

The debuginfo repository contains both debuginfo and debugsource packages. These packages provide debug symbols and source files that are useful for debugging and profiling applications. The SPAL debuginfo repository is disabled by default. DNF automatically enables it when you use commands that require debug packages.

To install debuginfo and debugsource packages for an SPAL package, run the following command:

```
[ec2-user ~]$ sudo dnf debuginfo-install {{package}}
```

## Uninstalling SPAL repository from your system
<a name="configure-spal-uninstall"></a><a name="uninstall-spal"></a>

1. Remove the SPAL repository configuration using `dnf remove` command.

   ```
   [ec2-user ~]$ sudo dnf remove spal-release
   ```

1. Verify the repository was removed by running `dnf repolist` command.

   ```
   [ec2-user ~]$ dnf repolist
   ```
**Important**
 Removing the SPAL repository configuration from your system does not remove any SPAL packages installed on the system.

## Related topics
<a name="configure-spal-more-info"></a>

For more information about the Supplementary Packages for Amazon Linux repository, see the following documentation:
+  [Supplementary Packages for Amazon Linux](spal.md)
