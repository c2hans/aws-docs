---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/deterministic-upgrades.html
---

# Deterministic upgrades through versioned repositories on AL2027
<a name="deterministic-upgrades"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

**Note**
By default, your AL2027 instance doesn't automatically receive additional security updates at launch. Your instance initially contains the updates that were available in the AL2027 release of the chosen AMI.

AL2027 uses deterministic upgrades through versioned repositories, the same update model as AL2023. The feature is turned on by default. To unlock a system so that every `dnf` operation uses the newest release, see [Using persistent override with deterministic upgrade](deterministic-upgrades-usage.md#deterministic-upgrade-override-persist). Each AL2027 release is a version of the package repositories. Each AMI and container image locks to the release version it was built from. Whenever we release new package updates, there is a new version to lock to. New AMIs and container images lock to that new version.

With this model, you control consistency of package versions and updates across your environment:
+ Multiple instances launched from the same AMI install identical package versions, even when you provision them at different times. Additional packages installed during provisioning come from the repository version of that AMI.
+ AL2027 does not apply updates automatically. You apply updates on a schedule that meets your needs, to a release version you have tested.
+ After we publish a release, it is immutable. Newer releases do not affect in-progress deployments.

**Topics**
+ [Differences between minor and major version upgrades](#differences-updates-upgrades)
+ [Knowing when updates are available](#knowing-when-to-update)
+ [Control the package updates available from the AL2027 repositories](#control-package-updates)
+ [Deterministic updates through instance replacement](security-instance-replacement.md)
+ [Using deterministic upgrades through versioned repositories](deterministic-upgrades-usage.md)

## Differences between minor and major version upgrades
<a name="differences-updates-upgrades"></a>

Major version releases of Amazon Linux (such as AL2023 to AL2027) include large-scale updates and might add, remove, or change packages. Upgrade to a new major version only after you test your application on that version.

Minor version releases of AL2027 include feature and security updates while keeping Linux features and the system library API stable. Testing your application before a minor update is not required, but staged rollouts remain best practice. For more information, see [Best practices for safely deploying updates](updating-best-practice.md).

## Knowing when updates are available
<a name="knowing-when-to-update"></a>

To apply an update, you need to know that one is available. The changes in each release are documented in the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html), and security issues addressed in package updates are covered by [Amazon Linux Security advisories for AL2027](alas.md). On a running system, `dnf check-release-update` reports newer releases. You can also [Receive notifications on new updates](receive-update-notifications.md).

For building derived AMIs when new AL2027 AMIs are released, [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/) can automatically build, patch, and test AMIs. For patching in-place across a fleet, you can use tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html).

Other AMIs and container images based on AL2027 might have their own release schedule and notification methods. When you use derived images, check the publisher's documentation for when updates are released.

## Control the package updates available from the AL2027 repositories
<a name="control-package-updates"></a>

When we publish a new version of the AL2027 repositories, all previous versions remain available. By default, the system locks to the release version that was used to build the AMI or container image. To move to a newer version:

1. Discover available repository versions.

   ```
   sudo dnf check-release-update
   ```

1. Upgrade to the version you selected.

   ```
   sudo dnf upgrade --releasever=<version>
   ```

The command lists the package updates and asks for confirmation before applying them. After the upgrade completes, the new release version becomes the default release version for all future `dnf` operations. For more information, see [Manage package and operating system updates in AL2027](manage-updates.md).
