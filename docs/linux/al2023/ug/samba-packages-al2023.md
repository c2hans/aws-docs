---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/samba-packages-al2023.html
---

# Samba packages for AL2023
<a name="samba-packages-al2023"></a>

## Samba packages
<a name="samba-packages"></a>

### Overview
<a name="overview"></a>

 Customers can now install the latest version of Samba on their instances using the new `samba-latest`, `libtalloc-latest`, `libtdb-latest`, and `libtevent-latest` packages, available in the Amazon Linux 2023 core RPM repository. These packages always include the newest features and security fixes."

 The current `samba` RPM package will remain on version 4.17 and will continue to receive security patches. Use this option if you are not able to move to the latest Samba version.

**Important**
The `samba` and `samba-latest` packages conflict with each other. You must choose which version you want to run.

**Note**
 At this time, `sssd-ad` and `sssd-ipa` will not work with `samba-latest`. If you use SSSD for authentication to Active Directory or similar setups,use the `samba` package.

### Package update policy
<a name="package-update-policy"></a>

 The `samba-latest`, `libtalloc-latest`, `libtdb-latest`, and `libtevent-latest` packages follow the latest upstream stable releases. Security fixes and bug fixes are implemented by updating the versions of these packages, which could introduce ABI/API changes. There will be no advance warning of version updates, so you should plan accordingly.

### Installing samba-latest RPM packages
<a name="installing-samba-latest-rpm-packages"></a>

 To install `samba-latest` and its dependencies on a newly launched instance, run the following command:

```
sudo dnf install samba-latest
```

 If you need additional packages, you can use the same `dnf` command to install them.

### Upgrading from samba to samba-latest
<a name="upgrading-from-samba-to-samba-latest"></a>

 The Amazon Linux team does not generally recommend performing an in-place upgrade from `samba` to `samba-latest`. Changes in the latest version of Samba might cause incompatibilities with a functioning system.

 With this caveat in mind, run the following command to swap the samba package for samba-latest:

```
sudo dnf swap samba samba-latest --allowerasing
```

**Warning**
 This command could fail depending on what RPM packages are currently installed on the system. Additional troubleshooting or commands might be required to complete the migration to `samba-latest`
