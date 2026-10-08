---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/updating.html
---

# Updating AL2023
<a name="updating"></a>

It's important to keep up to date with AL2023 releases so that you can benefit from security updates and new features. With AL2023, you can ensure consistency between package versions and updates across your environment through [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md).

**Warning**
 Running `dnf --releasever=latest update` is not best practice, and is likely to result in an OS update being first tested in production.
 Instead of using `latest`, use a specific AL2023 release version. This ensures you are deploying the same changes across production instances as you previously tested. For example, `dnf --releasever=2023.12.20260930 update` will always update to the 2023.12.20260930 release.
 For more information, see the [Updating AL2023](https://docs.aws.amazon.com/linux/al2023/ug/updating.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

**Topics**
+ [Best practices for safely deploying updates](updating-best-practice.md)
+ [Receive notifications on new updates](receive-update-notification.md)
+ [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md)
+ [Manage package and operating system updates in AL2023](managing-repos-os-updates.md)
+ [Kernel Live Patching on AL2023](live-patching.md)
+ [Updating the Linux Kernel on AL2023](kernel-update.md)
+ [Resolving a dracut error about the `systemd-pcrphase` module and `tpm2-tss`](dracut-tpm2-tss.md)
