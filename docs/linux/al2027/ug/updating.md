---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/updating.html
---

# Updating AL2027
<a name="updating"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Keep up to date with AL2027 releases to benefit from security updates and new features. AL2027 uses [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md), the same update model as AL2023. Each release locks to a specific set of package versions, which gives you consistent deployments across your fleet.

**Warning**
 Running `sudo dnf upgrade --releasever=latest` is not best practice, and is likely to result in an OS update being first tested in production.
 Instead of `latest`, use a specific AL2027 release version. This ensures that you deploy the same changes across production instances that you previously tested. For example, `sudo dnf upgrade --releasever=2027.0.20260817` always updates to the 2027.0.20260817 release.

To check for and apply updates within the locked release version:

```
# Check for available updates
dnf check-update

# Apply all available updates
sudo dnf upgrade
```

To move to a newer AL2027 release, pass the target release version. For more information, see [Manage package and operating system updates in AL2027](manage-updates.md).

```
sudo dnf upgrade --releasever=<version>
```

**Topics**
+ [Best practices for safely deploying updates](updating-best-practice.md)
+ [Receive notifications on new updates](receive-update-notifications.md)
+ [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md)
+ [Manage package and operating system updates in AL2027](manage-updates.md)
+ [Updating the Linux kernel on AL2027](updating-kernel.md)
