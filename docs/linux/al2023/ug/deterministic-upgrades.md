---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades.html
---

# Deterministic upgrades through versioned repositories on AL2023
<a name="deterministic-upgrades"></a>

**Note**
By default, your AL2023 instance doesn't automatically receive additional critical and important security updates at launch. Your instance initially contains the updates that were available in the version of AL2023 and the chosen AMI.

## Control the updates received from major and minor releases
<a name="controlling-release-updates"></a>

With AL2023, you can ensure consistency between package versions and updates across your environment. You can also ensure consistency for multiple instances of the same Amazon Machine Image (AMI). With the deterministic upgrades through versioned repositories feature, which is turned on by default, you can apply updates based on a schedule that meets your specific needs.

Whenever we release new package updates, there's a new version to lock to, and new AMIs that lock to that version.

AL2023 locks to a specific version of your repository. This is supported for both major or minor versions. The AL2023 AMI, exposed through our SSM parameters, is always the latest version. It has the most up-to-date packages and updates, including critical and important security updates.

If you launch an instance from an existing AMI, updates aren't automatically applied. Any additional packages that are installed as part of your provisioning map to the repository version of the existing AMI.

With this feature, you're in charge of ensuring consistency among package versions and updates across your environment. This is particularly the case if you're launching multiple instances from the same AMI. You can apply updates based on a schedule that meets your needs. You can also apply a specific set of updates on launch because these can also be locked to a specific repository version.

## Differences between minor and major version upgrades
<a name="differences-updates-upgrades"></a>

Major version releases of AL2023 include large-scale updates and might add, delete, or update packages. To ensure compatibility, upgrade your instance to a new major version only after you test your application on that version.

Minor version releases of AL2023 include feature and security updates, but don't include package changes. This ensures that Linux features and the system library API stay available on new versions. Testing your application before updating isn't necessary.

## Knowing when updates are available
<a name="knowing-when-to-update"></a>

 In order to apply an update, you need to know that one is available, and then know how to deploy the update.

 For building derived AMIs when new AL2023 AMIs are released, [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/) can automatically build, patch, and test AMIs. To trigger your own AMI building pipelines, or to use the base AMIs, you can [Receive notifications on new updates](receive-update-notification.md).

 For patching in-place, you can use tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to orchestrate applying updates across a fleet.

 For other public AMIs based on AL2023, the providers of those AMIs may have their own release schedule and notification methods. When using derived AMIs or container images, check the documentation from the publisher as to when updates are released.

 The changes in each release are documented in the [AL2023 release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes.html). Security updates are published on [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com).

## Control the package updates available from the AL2023 repositories
<a name="control-package-updates"></a>

When we publish a new version of the AL2023 repositories, all previous versions are still available. By default, the plugin for managing repository versions locks to the same version that was used to build the AMI. If you want to control package updates, follow these steps.

1. Discover available repository versions by running the following command.

   ```
   $ sudo dnf check-release-update
   ```

1. Select a version by running the following command.

   ```
   $ sudo dnf upgrade --releasever={{version}}
   ```

This command starts an update using `dnf` from your current Amazon Linux release version to the release version that's specified in the command line. A list of the package updates is presented by `dnf`. Before the update is processed, you must confirm the update. After the update is complete, the new release version becomes the default release version that `dnf` uses for all future activities.

For more information, see [Manage package and operating system updates in AL2023](managing-repos-os-updates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
